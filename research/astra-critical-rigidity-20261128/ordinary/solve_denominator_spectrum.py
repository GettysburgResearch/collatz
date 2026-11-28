"""Compute the fixed-grade denominator spectrum by the Presburger theorem.

Requires SymPy for exact polynomial arithmetic and an installed Z3 shared
library with its SMT-LIB evaluator. A positive timeout aborts instead of
reporting an unresolved case as absent. --dump-dir saves each input query.
"""
import argparse
import ctypes
import ctypes.util
from fractions import Fraction
from functools import lru_cache
import json
from math import gcd, lcm
from pathlib import Path
import re

import sympy as sp


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def logical(op, args, empty):
    args = list(args)
    if not args:
        return empty
    if len(args) == 1:
        return args[0]
    return "(" + op + " " + " ".join(args) + ")"


def conjunction(args):
    return logical("and", args, "true")


def disjunction(args):
    return logical("or", args, "false")


def total(args):
    return logical("+", args, "0")


def factor(n, expr):
    if n == 0:
        return "0"
    if n == 1:
        return expr
    literal = str(n) if n >= 0 else f"(- {-n})"
    return f"(* {literal} {expr})"


def eq(a, b):
    return f"(= {a} {b})"


def le(a, b):
    return f"(<= {a} {b})"


def lt(a, b):
    return f"(< {a} {b})"


def difference(a, b):
    return f"(- {a} {b})"


def finite_lookup(variable, values):
    expr = values[-1]
    for i in reversed(range(len(values)-1)):
        expr = f"(ite (= {variable} {i}) {values[i]} {expr})"
    return expr


class Solver:
    """Keep one native context per (g,e,eta), reusing it for candidate degrees."""
    def __init__(self):
        name = ctypes.util.find_library("z3")
        require(name is not None, "the Z3 shared library is unavailable")
        self.lib = ctypes.CDLL(name)
        pointer = ctypes.c_void_p
        signatures = (
            ("Z3_mk_config", pointer, []),
            ("Z3_mk_context", pointer, [pointer]),
            ("Z3_eval_smtlib2_string", ctypes.c_char_p, [pointer, ctypes.c_char_p]),
            ("Z3_del_context", None, [pointer]),
            ("Z3_del_config", None, [pointer]),
        )
        for name, result, arguments in signatures:
            func = getattr(self.lib, name)
            func.restype = result
            func.argtypes = arguments
        self.config = self.lib.Z3_mk_config()
        self.context = self.lib.Z3_mk_context(self.config)

    def evaluate(self, query):
        raw = self.lib.Z3_eval_smtlib2_string(self.context, query.encode()).decode().strip()
        require("error" not in raw.lower(), f"SMT-LIB error: {raw}")
        return raw

    def close(self):
        self.lib.Z3_del_context(self.context)
        self.lib.Z3_del_config(self.config)


U = sp.Symbol("U")


@lru_cache(maxsize=None)
def field_coefficients(p, g, e, eta):
    """Return integer coordinate vectors in the power basis of a cyclotomic field."""
    t = g*e
    v = p//g
    conductor = lcm(t, 24) if e == 2 and (v % 2 or eta) else t
    cycl = sp.Poly(sp.cyclotomic_poly(conductor, U), U, domain=sp.ZZ)
    def poly(expr):
        return sp.Poly(expr, U, domain=sp.ZZ).rem(cycl)
    def root(m, j):
        return poly(U**((j*conductor//m) % conductor))
    constant = poly(3**(v//e))
    if e == 2 and v%2:
        constant = (constant*(root(12, 1)+root(12, -1))).rem(cycl)
    if eta:
        constant = (constant*(root(8, 1)+root(8, -1))).rem(cycl)
    # eta=1 brings 1/sqrt(2)=sqrt(2)/2. Clear 2^t across every z<=t.
    table = {}
    maximum = 0
    for j in range(t):
        coefficient = (constant*root(t, j)).rem(cycl)
        power = poly(1)
        for z in range(t+1):
            scaled = power.mul_ground(2**((t-z)*eta))
            vector = tuple(int(scaled.nth(h)) for h in range(cycl.degree()))
            table[j, z] = vector
            maximum = max(maximum, *(abs(value) for value in vector))
            power = (power*coefficient).rem(cycl)
    maximum *= 3**(p-1)
    threshold = (p*max(maximum, 1)).bit_length()
    return table, cycl.degree(), threshold


def galois_masks(p, g, e, eta):
    """Enumerate invariant nonzero labels with primitive image on the g-th roots."""
    t = g*e
    v = p//g
    conductor = lcm(t, 24)
    units = [u for u in range(conductor) if gcd(u, conductor) == 1]
    unseen = set(range(t))
    orbits = []
    while unseen:
        initial = min(unseen)
        orbit = set()
        for u in units:
            negative = e == 2 and v%2 and u%12 in (5, 7)
            if eta and u%8 in (3, 5):
                negative = not negative
            shift = t//2 if negative else 0
            orbit.add((u*initial+shift)%t)
        require(orbit <= unseen, "invalid character orbit partition")
        unseen -= orbit
        orbits.append(orbit)
    # The real positive root survives. The orders at surviving labels have
    # lcm g by the no-proper-shorter-congruence lemma for primitive words.
    masks = {frozenset(orbits[0])}
    for orbit in orbits[1:]:
        masks |= {old | orbit for old in masks}
    return {mask for mask in masks if lcm(*(g//gcd(g,j) for j in mask)) == g}


class Formula:
    def __init__(self, p, g, e, eta, timeout):
        self.p, self.g, self.e, self.eta = p, g, e, eta
        self.t = g*e
        self.lines = ["(set-logic QF_LIA)", "(set-option :produce-models true)"]
        if timeout:
            self.lines.append(f"(set-option :timeout {timeout})")
        self.names = []
        table, field_degree, threshold = field_coefficients(p, g, e, eta)
        self.calendar(threshold)
        self.characters(table, field_degree)

    def var(self, name, model=False):
        self.lines.append(f"(declare-const {name} Int)")
        if model:
            self.names.append(name)
        return name

    def put(self, clause):
        self.lines.append(f"(assert {clause})")

    def define(self, name, expr, sort="Int", model=False):
        self.lines.append(f"(define-fun {name} () {sort} {expr})")
        if model:
            self.names.append(name)
        return name

    def calendar(self, threshold):
        p, g, e, eta, t = self.p, self.g, self.e, self.eta, self.t
        self.var("d")
        self.var("w")
        self.put(le(1, "d"))
        self.put(le(0, "w"))
        self.put(lt("w", "d"))
        if e == 1:
            self.put(eq("(mod d 2)", 1))
        for prime in sp.factorint(p//g):
            self.put(f"(not (and (= (mod {factor(e, 'd')} {prime}) 0)"
                     f" (= (mod (+ {factor(e, 'w')} {eta}) {prime}) 0)))")
        self.define("kk", factor(t, "d"), model=True)
        self.define("aa", factor(g, f"(+ {factor(e, 'w')} {eta})"), model=True)
        bound = (p-1)*(threshold+1)
        # A single rotation puts the first odd native departure at time zero.
        for i in range(p):
            for prefix in ("z", "r", "B", "E"):
                self.var(f"{prefix}{i}")
            z, r, B, E = (f"{prefix}{i}" for prefix in ("z", "r", "B", "E"))
            self.put(conjunction([le(0, z), le(z, t), le(0, r), lt(r, "d"),
                                  le(0, E), le(E, bound)]))
            self.define(f"W{i}", finite_lookup(E, [str(2**x) for x in range(bound+1)]))
            self.define(f"c{i}", f"(+ {r} {finite_lookup(z, [factor(j, 'd') for j in range(t+1)])})",
                        model=True)
            self.define(f"b{i}", f"(+ {B} {finite_lookup(z, [factor(j, 'w') for j in range(t+1)])})",
                        model=True)
        self.put(eq("c0", 0))
        self.put(eq("b0", 0))
        for i in range(p):
            for j in range(p):
                dist = difference(f"B{j}", f"B{i}")
                short = difference(f"E{j}", f"E{i}")
                self.put(f"(=> (and (<= 0 {dist}) (<= {dist} {threshold})) (= {short} {dist}))")
                self.put(f"(=> (> {dist} {threshold}) (> {short} {threshold}))")
            nc = f"c{i+1}" if i+1<p else "kk"
            nb = f"b{i+1}" if i+1<p else "aa"
            self.define(f"dc{i}", difference(nc, f"c{i}"))
            self.define(f"db{i}", difference(nb, f"b{i}"))
            self.put(disjunction([lt(0, f"dc{i}"), conjunction([eq(f"dc{i}", 0), lt(0, f"db{i}")])]))
        for shift in range(1, p):
            same = []
            for i in range(p):
                j = (i+shift)%p
                same.extend([eq(f"dc{i}", f"dc{j}"), eq(f"db{i}", f"db{j}")])
            self.put(f"(not {conjunction(same)})")

    def characters(self, table, degree):
        p, t = self.p, self.t
        for j in range(t):
            columns = []
            for h in range(degree):
                raw = [table[j,z][h] for z in range(t+1)]
                if not any(raw):
                    continue
                for i in range(p):
                    scale = 3**(p-1-i)
                    key = f"v{j}_{h}_{i}"
                    # Each product below multiplies by an integer *literal* only.
                    values = [factor(scale*v, f"W{i}") for v in raw]
                    self.define(key, finite_lookup(f"z{i}", values))
                for i in range(p):
                    terms = [f"v{j}_{h}_{k}" if i == k else
                             f"(ite (= r{i} r{k}) v{j}_{h}_{k} 0)" for k in range(p)]
                    columns.append(eq(total(terms), 0))
            self.define(f"nz{j}", f"(not {conjunction(columns)})", "Bool")
        self.define("support", total(f"(ite nz{j} 1 0)" for j in range(t)))

    def source(self):
        return "\n".join(self.lines)+"\n"


def exact_witness(grade, model, expected):
    k, a = model["kk"], model["aa"]
    dates = [(model[f"c{i}"], model[f"b{i}"]) for i in range(grade)]
    require(dates[0] == (0, 0) and dates == sorted(set(dates)) and dates[-1] < (k, a),
            "unordered affine calendar returned by solver")
    closed = dates+[(k, a)]
    gaps = [(y[0]-x[0], y[1]-x[1]) for x, y in zip(closed, closed[1:])]
    require(all(gaps != gaps[j:]+gaps[:j] for j in range(1, grade)), "nonprimitive model")
    # Handle negative offsets as rational coefficients. The indeterminate is 2^n.
    v = sp.Symbol("v")
    D = sp.Poly(sp.Integer(2)**a*v**k-3**grade, v, domain=sp.QQ)
    A = sp.Poly(sum(3**(grade-1-i)*sp.Integer(2)**b*v**c for i, (c, b) in enumerate(dates)),
                v, domain=sp.QQ)
    residual = D.exquo(D.gcd(A))
    require(Fraction(residual.degree(), k) == expected, "independent polynomial gcd rejected model")
    return {"length": [k, a], "dates": dates}


def parse_model(raw):
    parts = re.findall(r"\((\w+)\s+(\d+|\(-\s+\d+\))\)", raw)
    return {name: (-int(value[2:-1].strip()) if value.startswith("(") else int(value))
            for name, value in parts}


def solve(grade, timeout, dump, use_orbits):
    require(grade >= 1, "grade must be positive")
    cases = 0
    absent = 0
    orbit_exclusions = 0
    spectra = {}
    for g in sp.divisors(grade):
        for e in (1, 2):
            for eta in range(e):
                t = g*e
                formula = Formula(grade, g, e, eta, timeout)
                masks = galois_masks(grade, g, e, eta)
                original = formula.source()
                solver = Solver()
                try:
                    solver.evaluate(original)
                    for num in range(1, t+1):
                        value = Fraction(num, t)
                        # Every actual limit times p is an integer by the degree
                        # valuations in PRIME_GRADE_DENOMINATORS and PR212.
                        if grade % value.denominator or value in spectra:
                            continue
                        eligible = [mask for mask in masks if len(mask) == num]
                        if use_orbits and not eligible:
                            orbit_exclusions += 1
                            continue
                        exact_labels = disjunction(conjunction(
                            f"nz{j}" if j in mask else f"(not nz{j})" for j in range(t))
                            for mask in sorted(eligible, key=lambda s: sorted(s)))
                        predicate = exact_labels if use_orbits else eq("support", num)
                        assertion = f"(assert {predicate})"
                        if dump:
                            path = dump/f"p{grade}_g{g}_e{e}_eta{eta}_support{num}.smt2"
                            path.write_text(original+assertion+"\n(check-sat)\n")
                        answer = solver.evaluate("(push)"+assertion+"(check-sat)")
                        cases += 1
                        if answer == "sat":
                            raw = solver.evaluate("(get-value ("+" ".join(formula.names)+"))")
                            spectra[value] = exact_witness(grade, parse_model(raw), value)
                        else:
                            require(answer == "unsat", f"unresolved p={grade},g={g},e={e},eta={eta},num={num}: {answer}")
                            absent += 1
                        solver.evaluate("(pop)")
                finally:
                    solver.close()
    return {"grade": grade, "satisfiability_queries": cases, "unsatisfiable_queries": absent,
            "excluded_by_character_orbits": orbit_exclusions,
            "witnesses": {str(k): spectra[k] for k in sorted(spectra)}}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("grades", type=int, nargs="+")
    parser.add_argument("--timeout-ms", type=int, default=0)
    parser.add_argument("--dump-dir", type=Path)
    parser.add_argument("--no-character-pruning", action="store_true",
                        help="test all rationality-compatible support sizes directly with SMT")
    args = parser.parse_args()
    require(args.timeout_ms >= 0, "timeout must be nonnegative")
    if args.dump_dir:
        args.dump_dir.mkdir(parents=True, exist_ok=True)
    for grade in args.grades:
        print(json.dumps(solve(grade, args.timeout_ms, args.dump_dir, not args.no_character_pruning), sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
