#!/usr/bin/env python3
"""Exact finite checks for the Astra critical-mass attempt (stdlib only).

This program does NOT certify the uniform-in-time Green bound or Collatz.
The Green intervals do include every positive source, but only finite times.
"""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction
import hashlib
from itertools import product
import json
from pathlib import Path


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def step(n: int) -> int:
    return (3*n+1)//2 if n & 1 else n//2


def v3(n: int) -> int:
    require(n > 0, "valuation requires a positive integer")
    k = 0
    while n % 3 == 0:
        n //= 3
        k += 1
    return k


def ratio(x: Fraction) -> list[str]:
    return [str(x.numerator), str(x.denominator)]


def digest(obj: object) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def first_passage(n: int, floor: int, cap: int) -> tuple[int, int] | None:
    x = n
    for t in range(cap+1):
        if x <= floor:
            return t, x
        x = step(x)
    return None


def affine_check(X: int, Y: int, cap: int) -> dict:
    """Enumerate endpoint APs, not starting integers, then compare exact maps."""
    compiled = {}
    branches = 0
    for length in range(1, cap+1):
        for prefix in product((0, 1), repeat=length-1):
            word = prefix + (0,)
            q = A = 0
            data = [(0, 0)]
            for i, bit in enumerate(word):
                A = (3 if bit else 1)*A + bit*(1 << i)
                q += bit
                data.append((q, A))
            P, Q = 1 << length, 3**q
            low, high = Y//2+1, min(Y, (A+Q*X)//P)
            for i in range(length):
                qi, Ai = data[i]
                numerator = 3**qi*A + Q*((1 << i)*Y-Ai)
                low = max(low, numerator//(3**qi*P)+1)
            if low > high:
                continue
            residue = (A*pow(P, -1, Q)) % Q if Q > 1 else 0
            first = low + (residue-low) % Q
            if first > high:
                continue
            branches += 1
            for y in range(first, high+1, Q):
                require((P*y-A) % Q == 0, "nonintegral compiled source")
                n = (P*y-A)//Q
                require(n not in compiled, "duplicate first-passage source")
                compiled[n] = [length, y, ''.join(map(str, word))]
    direct = {}
    for n in range(Y+1, X+1):
        x, bits = n, []
        for t in range(1, cap+1):
            bits.append(x & 1)
            x = step(x)
            if x <= Y:
                direct[n] = [t, x, ''.join(map(str, bits))]
                break
    require(compiled == direct, "AP compiler/direct replay mismatch")
    return {"X": X, "Y": Y, "cap": cap, "nonempty_branches": branches,
            "sources": len(compiled), "mapping_sha256": digest(compiled)}


def passage_pilot(k: int) -> dict:
    X, Y, cap = 1 << k, 1 << (k//2), 4*k
    histogram = Counter()
    for n in range(Y+1, X+1):
        hit = first_passage(n, Y, cap)
        if hit is not None:
            t, y = hit
            require(Y//2 < y <= Y, "first-passage shell error")
            histogram[t, y] += 1
    tails = {}
    for q in (1, 2, 4):
        horizon = q*(k//2)
        tails[q] = {y for y in range(Y//2+1, Y+1)
                    if first_passage(y, 1, horizon) is None}
    rows = []
    for c in (1, 2, 4):
        good = sum(v for (t, _), v in histogram.items() if t <= c*k)
        for q in (1, 2, 4):
            bad = sum(v for (t, y), v in histogram.items()
                      if t <= c*k and y in tails[q])
            size = len(tails[q])
            rows.append({"stage_multiple": c, "tail_multiple": q,
                         "stage_good": good, "stage_unresolved": X-Y-good,
                         "tail_survivors_in_shell": size, "pullback_survivors": bad,
                         "shell_bias": ratio(Fraction(bad*(Y//2), good*size)) if size else None})
    triples = [[t, y, v] for (t, y), v in sorted(histogram.items())]
    return {"k": k, "X": X, "Y": Y, "source_domain": "Y<n<=X",
            "endpoint_domain": "Y/2<y<=Y", "histogram_sha256": digest(triples), "rows": rows}


def weight_interval(n: int, terms: int = 192, bits: int = 192) -> tuple[Fraction, Fraction]:
    """Enclose W_{3/2}(n) with exact dyadic rounding and an infinite tail."""
    scale, total = 1 << bits, 0
    for j in range(terms):
        z = (1 << j)*n+1
        total += (3**(j+v3(z))*scale)//((1 << j)*z*z)
    low = Fraction(total, scale)
    high = low + Fraction(terms, scale) + Fraction(4, n)*Fraction(3, 4)**terms
    return low, high


def weight_checks() -> dict:
    rows = []
    for h in range(1, 7):
        u = (3**(4*h+2)-1)//8
        y = (3**(4*h+3)+5)//16
        require(u & 1 and step(u) == y, "ordinary resonance ray failed")
        yl, yh = weight_interval(y)
        el, eh = weight_interval(2*y)
        ol, oh = weight_interval(u)
        lower, upper = (el+ol)/yh, (eh+oh)/yl
        require(lower > 1, "candidate failure was not certified")
        rows.append({"h": h, "source": u, "endpoint": y,
                     "LW_over_W_lower": ratio(lower), "LW_over_W_upper": ratio(upper)})
    checked = 0
    for y in range(2, 4097):
        w = Fraction(3**v3(y+1), (y+1)**2)
        Lw = Fraction(3**v3(2*y+1), (2*y+1)**2)
        if y % 3 == 2 and y > 2:
            u = (2*y-1)//3
            odd = Fraction(3**v3(u+1), (u+1)**2)
            require(odd == Fraction(3, 4)*w, "odd-branch ratio")
            Lw += odd
        if y % 3 == 0:
            require(Lw <= Fraction(16, 49)*w, "class-zero drift")
            checked += 1
        elif y % 3 == 2:
            require(Lw <= Fraction(87, 100)*w, "class-two drift")
            checked += 1
    return {"tested_endpoint_max": 4096, "partial_drift_cases": checked,
            "series_terms": 192, "rounding_bits": 192, "ordinary_failure_rays": rows}


def green_intervals(X: int = 1 << 18) -> dict:
    horizons, bits = (16, 32, 64, 128, 256), 80
    scale = 1 << bits
    geom = [Fraction(0)] + [Fraction(65**d-64**d, 64**(d-1)) for d in range(1, 258)]
    sums = {k: 0 for k in horizons}
    unresolved = 0
    for n in range(2, X+1):
        hit = first_passage(n, 1, max(horizons))
        t = hit[0] if hit is not None else max(horizons)+1
        unresolved += hit is None
        numerator, denominator = 3**v3(n+1), (n+1)**2
        for k in horizons:
            g = geom[min(k+1, t)]
            sums[k] += (scale*numerator*g.numerator)//(denominator*g.denominator)
    # Tail starts at n=X+1; n+1 >= X+2.
    power, log_floor = 1, 0
    while 3*power <= X+2:
        power *= 3
        log_floor += 1
    tail = Fraction(2*log_floor+5, X+2)
    rows = []
    for k in horizons:
        low = Fraction(sums[k], scale)
        high = low+Fraction(X-1, scale)+tail*geom[k+1]
        rows.append({"K": k, "finite_source_floor_sum": str(sums[k]),
                     "global_lower": ratio(low), "global_upper": ratio(high)})
    return {"source_cutoff": X, "lambda": [65, 64], "rounding_bits": bits,
            "source_tail_upper": ratio(tail), "sources_unresolved_at_K256": unresolved,
            "scope": "all integer sources n>=2, finite time k=0..K only", "rows": rows}


def algebra_checks() -> dict:
    chain_cases = 0
    for k in range(1, 49):
        for b in (2, 5):
            x = (1 << k)*b-1
            for j in range(k):
                require(x & 1, "all-odd path parity")
                x = step(x)
                require(x == 3**(j+1)*(1 << (k-j-1))*b-1, "all-odd affine identity")
            chain_cases += 1
    odd_cases = 0
    for S in ({1, 3, 9}, {5, 7, 21}, {o for o in range(1, 64, 2) if o % 7 in (1, 2)}):
        for X in (1, 16, 127, 512):
            for exponent in (1, 2):
                left = Fraction(0)
                for n in range(1, X+1):
                    core = n
                    while core % 2 == 0:
                        core //= 2
                    if core in S:
                        left += Fraction(1, n**exponent)
                right = Fraction(0)
                r = 0
                while (1 << r) <= X:
                    right += Fraction(1, 2**(r*exponent))*sum(
                        (Fraction(1, o**exponent) for o in S if o <= X//(1 << r)), Fraction(0))
                    r += 1
                require(left == right, "odd-core weighted identity")
                odd_cases += 1
    return {"ordinary_all_odd_paths": chain_cases, "odd_core_identity_cases": odd_cases,
            "odd_core_test_scope": "synthetic dyadically saturated sets; not assumed Collatz invariant"}


def build_report() -> dict:
    result = {"schema": "X-ASTRA-001-v1", "status": "FINITE_CHECKS_ONLY_NOT_A_COLLATZ_PROOF",
              "algebra": algebra_checks(),
              "affine_first_passage": [affine_check(256, 16, 8), affine_check(512, 32, 10)],
              "first_passage_pilot": [passage_pilot(k) for k in (8, 10, 12, 14, 16, 18)],
              "weights": weight_checks(), "green": green_intervals()}
    result["semantic_sha256"] = digest(result)
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", type=Path)
    parser.add_argument("--check", type=Path)
    args = parser.parse_args()
    result = build_report()
    if args.check:
        require(result == json.loads(args.check.read_text()), "canonical report mismatch")
        print("PASS", result["semantic_sha256"])
    if args.write:
        args.write.parent.mkdir(parents=True, exist_ok=True)
        args.write.write_text(json.dumps(result, indent=2, sort_keys=True)+"\n")
    if not args.write and not args.check:
        print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
