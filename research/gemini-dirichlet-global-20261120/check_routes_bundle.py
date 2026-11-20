#!/usr/bin/env python3
"""Exact scoped replay for the supplied routes bundle; no Collatz claim.

All checks use explicit exceptions, so Python -O preserves verification.
The attachment is read for provenance and advertised counts, never imported.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from fractions import Fraction
import hashlib
import json
from math import gcd
from pathlib import Path


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def step(x: Fraction) -> Fraction:
    require(x.denominator % 2 == 1, "rational step requires odd denominator")
    return (3 * x + 1) / 2 if x.numerator % 2 else x / 2


def affine_orbit(a: int, b: int, length: int):
    out = [(a, b)]
    odd = 0
    for _ in range(length):
        require(a % 2 == 0, "whole-cylinder precision exhausted")
        if b % 2:
            a, b = 3 * a // 2, (3 * b + 1) // 2
            odd += 1
        else:
            a, b = a // 2, b // 2
        out.append((a, b))
    return out, odd


def replay_sieve(advertised):
    result = {}
    for key, mode in [("tripling_pairs_n_3n", "tripling"),
                      ("sibling_pairs_2n_2n1", "sibling"),
                      ("stopping_time_drop_sieve", "coefficient")]:
        result[key] = {}
        for depth_text, claim in advertised[key].items():
            depth = int(depth_text)
            modulus = 1 << depth
            residues = range(modulus) if mode == "sibling" else range(1, modulus, 2)
            successes = 0
            for r in residues:
                left, _ = affine_orbit(modulus, r, depth)
                if mode == "coefficient":
                    hit = any(a < modulus for a, _ in left[1:])
                else:
                    right, _ = affine_orbit(3 * modulus, 3 * r + (2 if mode == "sibling" else 0), depth)
                    hit = bool(set(left).intersection(right))
                successes += int(hit)
            label = "excluded_by_drop" if mode == "coefficient" else "coalesced"
            require(successes == claim[label], f"advertised {mode} count differs at depth {depth}")
            result[key][depth_text] = successes
    orbit, _ = affine_orbit(1 << 13, 1, 13)
    require(any(a < (1 << 13) for a, _ in orbit[1:]), "missing coefficient control")
    require(all(b >= 1 for _, b in orbit), "unexpected descent from one")
    return {"advertised_integer_counts_match": True, "counts": result,
            "coefficient_control": {"source": 1, "coefficient_crosses": True,
                                    "strict_descent": False}}


def replay_denominators_and_operators():
    cases = [("1", 2), ("-1", 1), ("-5", 3), ("-17", 11),
             ("-19/11", 4), ("23/5", 5), ("19/5", 5),
             ("211/13", 8), ("259/13", 8)]
    cycles = []
    positive_atoms = set()
    for text, period in cases:
        root = Fraction(text)
        x = root
        orbit = []
        for i in range(period):
            require(i == 0 or x != root, "claimed primitive period is too large")
            orbit.append(x)
            require(gcd(x.denominator, 6) == 1, "cycle left prime-to-six sector")
            require(x.denominator == root.denominator, "denominator changed")
            x = step(x)
        require(x == root, "cycle did not close")
        if root > 0:
            positive_atoms.update(orbit)
        cycles.append({"source": text, "primitive_period": period,
                       "denominator": root.denominator,
                       "orbit": [str(y) for y in orbit]})

    atoms = sorted(positive_atoms)
    f = {x: Fraction((-1) ** i * (i + 1), i + 2) for i, x in enumerate(atoms)}
    sector = lambda x: x.denominator ** 2 + 1
    weight = lambda x: x.numerator ** 2 + x.denominator ** 2

    def push(v):
        out = defaultdict(Fraction)
        for x, amount in v.items():
            out[step(x)] += amount
        return dict(out)

    left = {x: sector(x) * amount for x, amount in push(f).items()}
    right = push({x: sector(x) * amount for x, amount in f.items()})
    require(left == right, "sector conjugacy control failed")
    require(sum(weight(x) * sector(x) * abs(amount) for x, amount in f.items()) ==
            sum(weight(x) * abs(sector(x) * amount) for x, amount in f.items()),
            "sector isometry control failed")

    # Haar PF dual of the ordinary 1,2 cycle is different from pushforward.
    mu = {Fraction(1): Fraction(1, 2), Fraction(2): Fraction(1, 2)}
    require(push(mu) == mu, "ordinary cycle must be invariant under actual pushforward")
    lfdual = defaultdict(Fraction)
    for x, amount in mu.items():
        lfdual[2 * x] += amount / 2
        lfdual[(2 * x - 1) / 3] += amount / 2
    expected = {Fraction(x): Fraction(1, 4) for x in ("1", "2", "4", "1/3")}
    require(dict(lfdual) == expected and dict(lfdual) != mu, "dual operator distinction failed")

    galerkin = {}
    for depth in range(1, 10):
        modulus, half = 1 << depth, 1 << (depth - 1)
        for source in range(modulus):
            counts = {source: 1}
            for _ in range(depth):
                nxt = defaultdict(int)
                for r, count in counts.items():
                    base = r // 2 if r % 2 == 0 else ((3 * r + 1) // 2) % half
                    nxt[base] += count
                    nxt[base + half] += count
                counts = nxt
            require(len(counts) == modulus and all(v == 1 for v in counts.values()),
                    f"Galerkin exact M-step uniformity failed at M={depth}")
        galerkin[str(depth)] = {"columns_checked": modulus, "all_path_counts": 1,
                               "nonstationary_eigenvalues": "exactly zero"}
    return {"cycles": cycles, "sector_conjugacy_control": True,
            "haar_pf_dual_of_cycle": {str(k): str(v) for k, v in sorted(lfdual.items())},
            "galerkin": galerkin}


# H=2h, indexed by increasing units z modulo 243. This is the complete
# certificate, not the output of a floating point solver at verification time.
H_VALUES = [
    8,6,7,6,10,5,4,8,5,8,12,5,7,2,7,12,13,3,
    6,6,10,10,12,9,7,5,6,8,10,5,10,6,8,11,12,7,
    10,4,12,6,12,8,8,7,6,10,11,3,11,5,3,11,15,4,
    6,7,9,8,11,6,5,8,4,7,12,6,9,4,4,10,12,0,
    7,8,11,8,13,10,4,6,3,10,8,4,10,6,7,9,14,4,
    8,3,11,9,10,6,8,9,9,12,8,1,9,4,5,13,13,0,
    9,4,8,7,9,7,6,6,2,9,10,4,8,3,6,12,11,2,
    5,7,8,10,14,8,6,7,2,11,9,2,8,4,6,10,14,6,
    9,5,10,8,13,9,6,8,8,11,10,2,10,2,4,12,14,1,
]


def replay_bellman():
    units = [z for z in range(243) if z % 3]
    require(len(H_VALUES) == len(units) == 162, "wrong potential length")
    potential = dict(zip(units, H_VALUES))
    policy, worst_digit = {}, {}
    for z in units:
        e = 2 + potential[2 * z % 243]
        o = None
        if z % 9 in (2, 8):
            base = (2 * z - 1) // 3 % 81
            require(all(base + 81 * d in potential for d in range(3)), "illegal unit successor")
            worst_digit[z] = max(range(3), key=lambda d: potential[base + 81 * d])
            o = -3 + potential[base + 81 * worst_digit[z]]
        rhs = e if o is None else min(e, o)
        require(potential[z] == rhs, f"Bellman equality failed at z={z}")
        policy[z] = "E" if e == rhs else "O"

    def compile_tail(c, t):
        origin = c
        remaining, k = t, 0
        while remaining >= 5:
            if policy[c % 243] == "E":
                c *= 2
            else:
                require(c % 9 in (2, 8), "invalid robust odd inverse step")
                c = (2 * c - 1) // 3
                remaining -= 1
            k += 1
            require(k <= 10 * t + 100, "unexpected compiler nontermination")
        while remaining >= 2:
            doublings = 0
            while c % 9 not in (2, 8):
                c *= 2
                k += 1
                doublings += 1
            require(doublings <= 3, "terminal unit policy bound failed")
            c = (2 * c - 1) // 3
            remaining -= 1
            k += 1
        if remaining:
            if c % 3 == 1:
                c *= 2
                k += 1
            require(c % 3 == 2, "invalid final inverse step")
            c = (2 * c - 1) // 3
            k += 1
        require(0 < c < (1 << k), "compiled offset outside required range")
        path, odd = affine_orbit(1 << k, c, k)
        require(path[-1] == (3 ** t, origin) and odd == t,
                "compiler whole-cylinder identity failed")
        require(2 * k <= 5 * t + 23, "compiler terminal-adjusted bound failed")
        return k

    tails, maximum_clock = 0, 0
    for t in range(1, 7):
        for c in range(1, 3 ** t):
            if c % 3:
                maximum_clock = max(maximum_clock, compile_tail(c, t))
                tails += 1
    return {"P": 5, "modulus": 243, "states": 162, "alpha": "5/2",
            "H_scale": 2, "H_span": 15, "all_Bellman_equalities_exact": True,
            "H_in_increasing_unit_order": H_VALUES,
            "policy_in_increasing_unit_order": "".join(policy[z] for z in units),
            "terminal_adjusted_clock_bound": "k <= floor((5t+23)/2)",
            "finite_integration_controls": {"unit_tails_t1_to_t6": tails,
                                             "maximum_clock": maximum_clock}}


def replay_variation():
    controls = [(16,3,-1,0,4,2), (8,5,-1,0,3,1),
                (128,49,0,1,7,3), (32,5,0,1,5,2)]
    cylinder_report = []
    for modulus, residue, left_offset, right_offset, clock, odds in controls:
        left, a = affine_orbit(modulus, residue + left_offset, clock)
        right, b = affine_orbit(modulus, residue + right_offset, clock)
        require(left[-1] == right[-1] and a == b == odds, "variation cylinder mismatch")
        cylinder_report.append({"modulus": modulus, "residue": residue,
                                "clock": clock, "endpoint_coefficients": left[-1]})
    for w in range(1, 16, 2):
        require(any(3 ** j * w % 16 in (3, 5) for j in range(2, 6)),
                "minus residue coverage failed")
    for w in range(1, 128, 2):
        require(any(3 ** j * w % 128 == 49 or 3 ** j * w % 32 == 5
                    for j in range(2, 34)), "plus residue coverage failed")
    subgroup = {pow(3, j, 128) for j in range(32)}
    require(subgroup == {w for w in range(128) if w % 8 in (1, 3)},
            "modulo-128 subgroup description failed")

    offsets = [0,18,24,32,33,36,48,64,63,72,96,99,108,144,192,198,216,288]
    rows = [(16,1,0), (4,12,1), (4,9,1), (16,18,2), (4,24,3),
            (4,6,1), (3,6,1), (4,72,16), (4,8,2), (4,3,1),
            (16,6,2), (4,8,3), (4,2,1), (3,2,1), (16,3,2),
            (4,4,3), (4,1,1)]
    exponent_total = 0
    for (p, q), (kind, alpha, beta) in zip(zip(offsets, offsets[1:]), rows):
        scale = abs(p - q)
        require(288 % scale == p % scale == q % scale == 0, "nonintegral edge reduction")
        actual = sorted([(288 // scale, p // scale), (288 // scale, q // scale)])
        shift = -1 if kind == 4 else 1
        expected = sorted([(kind * alpha, kind * beta),
                           (kind * alpha, kind * beta + shift)])
        require(actual == expected, "wrong 17-edge affine identity")
        if kind == 3:
            require(alpha % 2 == 0 and beta % 2 == 1, "odd comparison parameter not odd")
        smooth = scale
        while smooth % 2 == 0:
            smooth //= 2
        while smooth % 3 == 0:
            exponent_total += 1
            smooth //= 3
        require(smooth == 1, "edge scale not 2,3-smooth")
    require(exponent_total == 19, "wrong smooth multiplier cost")
    return {"whole_cylinder_controls": cylinder_report,
            "minus_residues_checked": 8, "plus_residues_checked": 64,
            "all_17_affine_edges_exact": True, "sum_v3_edge_scales": 19,
            "dyadic_multiplicity": "proved in TRIPLING_VARIATION_REVIEW.md, not inferred from finite tests"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bundle", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    claim_path = args.bundle / "results/verified_computations.json"
    advertised = json.loads(claim_path.read_text(encoding="utf-8"))
    source_paths = ["BARRIER_AUDIT.md", "results/verified_computations.json",
                    "route1_tripling_and_sibling_mergers/PROPOSAL.md",
                    "route1_tripling_and_sibling_mergers/algebraic_coalescence_sieve.py",
                    "route1_tripling_and_sibling_mergers/lean4_x_min_exclusions_skeleton.lean",
                    "route2_inverse_compiler_and_bellman/PROPOSAL.md",
                    "route2_inverse_compiler_and_bellman/bellman_potential_certifier.py",
                    "route4_adelic_spectral_operators/PROPOSAL.md",
                    "route4_adelic_spectral_operators/transfer_operator_spectrum.py",
                    "route5_agentic_pr_roadmap/PR_BLUEPRINTS.md",
                    "route5_agentic_pr_roadmap/barrier_falsification_harness.py"]
    result = {"status": "PASS", "scope": "Exact finite controls and a complete finite Bellman certificate; no Collatz resolution",
              "source_sha256": {name: sha(args.bundle / name) for name in source_paths},
              "checker_sha256": sha(Path(__file__)),
              "sieve": replay_sieve(advertised["route1"]),
              "denominator_and_operator_controls": replay_denominators_and_operators(),
              "exact_Bellman_certificate": replay_bellman(),
              "ordinary_variation_controls": replay_variation()}
    output = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(output, encoding="utf-8")
    print(output, end="")


if __name__ == "__main__":
    main()
