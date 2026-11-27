"""Reconstruct every branch of the recursive original-parent comparison."""
import json
import re
from collections import Counter
from fractions import Fraction
from pathlib import Path

from check_ternary_pump import delayed_class, power_class
from check_valuation_cover import require, trace

ROOT = Path(__file__).resolve().parent
P = 3**15
K = 2**106
BASE = 95*pow(K, -1, P) % P
INITIAL = (0, 0, -1)


def tree_rows():
    source = (ROOT/"NestedCover.lean").read_text(encoding="utf-8")
    body = source.split("def trie : Atlas Plan :=", 1)[1].split("set_option", 1)[0]
    token = re.compile(r"\s*(\(\.fork|\(\.leaf|\(\.query|\.finish|⟨[0-9,]+⟩|\))")
    tokens = []
    while body.strip():
        m = token.match(body)
        require(m is not None, "complete tree syntax")
        tokens.append(m[1])
        body = body[m.end():]
    stream = iter(tokens)

    def numbers(n):
        data = next(stream)
        require(data.startswith("⟨"), "numeric vector")
        values = tuple(map(int, re.findall(r"\d+", data)))
        require(len(values) == n, "vector length")
        return values

    def plan():
        tag = next(stream)
        if tag == ".finish":
            return ()
        require(tag == "(.query", "required ordinary query")
        link = numbers(5)
        g, d, offset = numbers(3)
        rest = plan()
        require(next(stream) == ")", "query arity")
        return ((link, (g, d, offset-17)),)+rest

    def tree(v, h):
        tag = next(stream)
        if tag == "(.leaf":
            result = plan()
            require(next(stream) == ")" and result, "nonempty comparison plan")
            yield v, h, result
            return
        require(tag == "(.fork", "ternary node")
        for i in range(3):
            yield from tree(v+i*3**h, h+1)
        require(next(stream) == ")", "three children")

    leaves = list(tree(0, 0))
    require(next(stream, None) is None, "exactly one certificate")
    return leaves


def endpoint(state, N):
    g, d, c = state
    require(0 <= d <= 100 and N % 2**d == 0, "integral positive scale")
    Y = 3**g*(N >> d)+c
    require(Y > 0, "positive ordinary target")
    return Y


def check_link(a, b, link, N):
    g, d, c = a
    r, f, debit, h, p = link
    weight = 3**g*((N << f) >> d)
    w, rem = divmod(weight-debit, 3**r)
    require(rem == 0 and 0 < w and w % 48 == 17, "canonical ordinary source")
    require(81*w+271 < 128*N, "strict original parent budget at every link")
    lo, lo_bits = trace(w, f)
    hi, hi_bits = trace(3*w, h)
    require((lo, sum(lo_bits)) == (endpoint(a, N), r), "whole lower word and odd count")
    require((hi, sum(hi_bits)) == (endpoint(b, N), p), "whole upper word and odd count")
    # Reconstruct the lower numerator from the actual odd positions.
    times = [i for i, bit in enumerate(lo_bits) if bit]
    require(r > 0 and times[0] == 0, "ordinary odd starts")
    exponents = [t-s for s, t in zip(times, times[1:]+[f])]
    bias = 0
    for i, e in enumerate(reversed(exponents)):
        bias = (bias << e)+3**i
    require(bias-(c << f) == debit, "reconstructed signed intercept")
    return w, lo, hi, lo_bits, hi_bits


def terminal(a):
    g, d, c = a
    require(c in (-1, 0, 1), "funded terminal type")
    if c == -1:
        require(d-g >= 5, "general earlier-offset gap")
    elif c == 0:
        require(2**40*3**g < 2**173, "pure-power endpoint below original floor")
    else:
        n, rem = divmod(173-d, 2)
        require(2**40*(2**rem*3**(g+n)+1) < 2**173, "positive-turn margin")
    return c


def literal(v, h, route, j):
    m = 11+162*j
    # For these two controls all 2^m bits of the ordinary source are materialized.
    N = 1 << m
    z, rem = divmod(128*N-271, 81)
    require(rem == 0 and (z+1) % 3**11 == 0, "literal divisibility")
    index, rem = divmod((N >> 100)-BASE, P)
    require(rem == 0 and index % 3**h == v, "literal selected leaf")
    require(trace(z, 7)[0] == N-1, "ordinary parent reaches original Mersenne")
    a, previous = INITIAL, None
    sizes = []
    for link, b in route:
        w, lo, hi, _, _ = check_link(a, b, link, N)
        require(lo == (N-1 if previous is None else previous), "chain joins at identical ordinary integer")
        sizes.append(w.bit_length())
        a, previous = b, hi
    return {"j": j, "m": m, "ternary_depth": h, "source_bits": sizes,
            "terminal_state": list(a), "terminal_bits": previous.bit_length()}


def main():
    leaves = tree_rows()
    mass = Fraction()
    levels, terminals = Counter(), Counter()
    strict_links = 0
    lower_max = upper_max = 0
    nested = []
    actual = []
    for v, h, route in leaves:
        x, S = BASE+P*v, P*3**h
        a = INITIAL
        route_json = []
        N, ns = x << 100, S << 100
        grade = len(route)
        levels[grade] += 1
        for link, b in route:
            r, f, _, ht, p = link
            w, lo, hi, low, high = check_link(a, b, link, N)
            wn, lon, hin, lown, highn = check_link(a, b, link, N+ns)
            A = wn-w
            require((low, high) == (lown, highn), "two independently iterated parity words")
            require(A > 0 and A % 48 == 0 and 81*A <= 128*ns, "strict budget transport at z")
            require((A % 2**f, (3*A) % 2**ht) == (0, 0), "physical parity periodicity")
            require((A >> f)*3**r == lon-lo == (ns >> a[1])*3**a[0], "lower slope transport")
            require(((3*A) >> ht)*3**p == hin-hi == (ns >> b[1])*3**b[0], "upper slope transport")
            strict_links += 1
            lower_max, upper_max = max(lower_max, f), max(upper_max, ht)
            route_json.append({"input": list(a), "link": list(link), "output": list(b)})
            a = b
        terminals[terminal(a)] += 1
        mass += Fraction(1, 3**h)
        C = ((K*x-95)//P) % 3**h
        j = power_class(95+P*C, 10+h)
        if grade > 1:
            nested.append({"C_residue": C, "ternary_depth": h, "j": j, "links": route_json})
        if j in (13193, 308438):
            actual.append(literal(v, h, route, j))
    require(mass == 1 and levels == {1: 19, 2: 2, 3: 2}, "complete recursive cover")
    require(len(actual) == 2 and any(len(s["source_bits"]) == 3 for s in actual), "ordinary nested control")
    j = power_class(95, 10)
    k = delayed_class(j, 10)
    density = sum((Fraction(1, 3**(s-2)) for s in range(6, 15)), Fraction(1, 3**10))
    require(density == Fraction(1, 54)+Fraction(17, 18*3**10), "disjoint shell union")
    print(json.dumps({"root_X": BASE, "root_step": P, "leaves": len(leaves),
          "leaf_mass": [mass.numerator, mass.denominator], "strict_original_parent_links": strict_links,
          "leaves_by_number_of_queries": dict(sorted(levels.items())),
          "leaves_by_terminal_constant": dict(sorted(terminals.items())),
          "maximum_lower_prefix": lower_max, "maximum_upper_prefix": upper_max,
          "d11_ball_address": {"modulus": 3**10, "j": j, "k": k},
          "combined_pump_and_ball_density": [density.numerator, density.denominator],
          "nested_branches": sorted(nested, key=lambda entry: entry["C_residue"]),
          "literal_ordinary_parents": sorted(actual, key=lambda entry: entry["m"])}, indent=2))


if __name__ == "__main__":
    main()
