#!/usr/bin/env python3
"""Independent replay of X-ASTRA-001; never imports run.py.

Uses cached physical first hits, recursive geometric sums, rational weights,
and separate certificate reconstruction. Passing is not an all-time proof.
"""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path


def check(value: bool, message: str) -> None:
    if not value:
        raise ValueError(message)


def advance(x: int) -> int:
    return (x+(x % 2)*(2*x+1)) >> 1


def ord3(n: int) -> int:
    p, k = 3, 0
    while n % p == 0:
        p *= 3
        k += 1
    return k


def as_fraction(value: list[str] | list[int]) -> F:
    return F(int(value[0]), int(value[1]))


def encoded(value: F) -> list[str]:
    return [str(value.numerator), str(value.denominator)]


def seal(obj: object) -> str:
    data = json.dumps(obj, separators=(",", ":"), sort_keys=True).encode()
    return hashlib.sha256(data).hexdigest()


def cached_hit(n: int, cap: int, cache: dict) -> tuple[int, int] | None:
    x, path = n, []
    while x not in cache and len(path) <= cap:
        path.append(x)
        x = advance(x)
    if x not in cache:
        return None
    t, endpoint = cache[x]
    for x in reversed(path):
        t += 1
        cache[x] = t, endpoint
    answer = cache[n]
    return answer if answer[0] <= cap else None


def check_affine(row: dict) -> None:
    X, Y, cap = row["X"], row["Y"], row["cap"]
    found, words = {}, set()
    for n in range(Y+1, X+1):
        x, text = n, ""
        for j in range(1, cap+1):
            text += str(x % 2)
            x = advance(x)
            if x <= Y:
                check(2*x > Y, "endpoint outside first-passage shell")
                found[n] = [j, x, text]
                words.add(text)
                break
    check(len(found) == row["sources"], "AP source count")
    check(len(words) == row["nonempty_branches"], "AP branch count")
    check(seal(found) == row["mapping_sha256"], "AP mapping hash")


def check_pilot(item: dict) -> None:
    check([(r["stage_multiple"], r["tail_multiple"]) for r in item["rows"]] == [(c, q) for c in (1, 2, 4) for q in (1, 2, 4)], "pilot row coverage")
    k, X, Y = item["k"], item["X"], item["Y"]
    check(X == 2**k and Y == 2**(k//2), "pilot scales")
    check(item["source_domain"] == "Y<n<=X" and item["endpoint_domain"] == "Y/2<y<=Y", "pilot domain")
    cache = {y: (0, y) for y in range(1, Y+1)}
    histogram = Counter()
    for n in range(Y+1, X+1):
        answer = cached_hit(n, 4*k, cache)
        if answer is not None:
            histogram[answer] += 1
    triples = [[t, y, count] for (t, y), count in sorted(histogram.items())]
    check(seal(triples) == item["histogram_sha256"], "pilot histogram hash")
    for row in item["rows"]:
        c, q = row["stage_multiple"], row["tail_multiple"]
        survivors, terminal_cache = set(), {1: (0, 1)}
        for y in range(Y//2+1, Y+1):
            if cached_hit(y, q*(k//2), terminal_cache) is None:
                survivors.add(y)
        good = sum(count for (t, y), count in histogram.items() if t <= c*k)
        bad = sum(count for (t, y), count in histogram.items() if t <= c*k and y in survivors)
        expected = {"stage_multiple": c, "tail_multiple": q,
                    "stage_good": good, "stage_unresolved": X-Y-good,
                    "tail_survivors_in_shell": len(survivors), "pullback_survivors": bad,
                    "shell_bias": encoded(F(bad*(Y//2), good*len(survivors))) if survivors else None}
        check(row == expected, "survivor-bias row")


def enclose_weight(n: int, J: int, bits: int) -> tuple[F, F]:
    unit, partial, coefficient = 2**bits, 0, F(1)
    for j in range(J):
        z = n*2**j+1
        term = coefficient*F(3**ord3(z), z*z)
        partial += (unit*term.numerator)//term.denominator
        coefficient *= F(3, 2)
    lo = F(partial, unit)
    hi = lo+F(J, unit)+F(4, n)*F(3, 4)**J
    return lo, hi


def check_weights(item: dict) -> None:
    check((item["tested_endpoint_max"], item["series_terms"], item["rounding_bits"]) == (4096, 192, 192), "weight coverage")
    check([r["h"] for r in item["ordinary_failure_rays"]] == list(range(1, 7)), "ray coverage")
    count = 0
    for y in range(2, item["tested_endpoint_max"]+1):
        weight = lambda n: F(3**ord3(n+1), (n+1)**2)
        value = weight(2*y)
        if y % 3 == 2 and y != 2:
            u = (2*y-1)//3
            check(weight(u)/weight(y) == F(3, 4), "odd drift")
            value += weight(u)
        if y % 3 in (0, 2):
            bound = F(16, 49) if y % 3 == 0 else F(87, 100)
            check(value <= bound*weight(y), "partial drift bound")
            count += 1
    check(count == item["partial_drift_cases"], "drift case count")
    for row in item["ordinary_failure_rays"]:
        h, u, y = row["h"], row["source"], row["endpoint"]
        check(8*u+1 == 3**(4*h+2) and 16*y-5 == 3**(4*h+3), "ray source construction")
        check(advance(u) == y and u % 2 == 1, "ray dynamics")
        yl, yh = enclose_weight(y, item["series_terms"], item["rounding_bits"])
        el, eh = enclose_weight(2*y, item["series_terms"], item["rounding_bits"])
        ol, oh = enclose_weight(u, item["series_terms"], item["rounding_bits"])
        check(encoded((el+ol)/yh) == row["LW_over_W_lower"], "ray lower interval")
        check(encoded((eh+oh)/yl) == row["LW_over_W_upper"], "ray upper interval")
        check((el+ol)/yh > 1, "ray does not refute contraction")


def check_green(item: dict) -> None:
    check(item["lambda"] == [65, 64] and item["rounding_bits"] == 80, "Green parameters")
    X = item["source_cutoff"]
    check(X == 2**18, "Green source coverage")
    check(item["scope"] == "all integer sources n>=2, finite time k=0..K only", "Green scope")
    horizons = [r["K"] for r in item["rows"]]
    check(horizons == [16, 32, 64, 128, 256], "Green horizons")
    geometric, term, total = [F(0)], F(1), F(0)
    for _ in range(max(horizons)+1):
        total += term
        geometric.append(total)
        term *= F(65, 64)
    fixed = {k: 0 for k in horizons}
    cache, unresolved = {1: (0, 1)}, 0
    for n in range(2, X+1):
        answer = cached_hit(n, max(horizons), cache)
        stopping = answer[0] if answer is not None else max(horizons)+1
        unresolved += answer is None
        w = F(3**ord3(n+1), (n+1)**2)
        for k in horizons:
            g = geometric[min(k+1, stopping)]
            fixed[k] += (w.numerator*g.numerator*2**80)//(w.denominator*g.denominator)
    check(unresolved == item["sources_unresolved_at_K256"], "Green unresolved count")
    value, exponent = X+2, 0
    while value >= 3:
        value //= 3
        exponent += 1
    tail = F(2*exponent+5, X+2)
    check(encoded(tail) == item["source_tail_upper"], "analytic source tail")
    for row in item["rows"]:
        k = row["K"]
        check(str(fixed[k]) == row["finite_source_floor_sum"], "Green fixed-point sum")
        lower = F(fixed[k], 2**80)
        upper = lower+F(X-1, 2**80)+tail*geometric[k+1]
        check(encoded(lower) == row["global_lower"] and encoded(upper) == row["global_upper"], "Green global enclosure")
    check(as_fraction(item["rows"][-1]["global_lower"]) > F(86140, 10000), "rounded global lower")
    check(as_fraction(item["rows"][-1]["global_upper"]) < F(89619, 10000), "rounded global upper")


def check_algebra(item: dict) -> None:
    cases = 0
    for k in range(1, 49):
        for b in (2, 5):
            x = 3**k*b-1
            for j in range(k):
                check((2*x-1) % 3 == 0, "inverse all-odd integrality")
                previous = (2*x-1)//3
                check(advance(previous) == x and previous % 2 == 1, "inverse all-odd replay")
                x = previous
            check(x == 2**k*b-1, "inverse all-odd source")
            cases += 1
    check(cases == item["ordinary_all_odd_paths"], "ordinary-ray count")
    cases = 0
    for roots in ({1, 3, 9}, {5, 7, 21}, {o for o in range(1, 64, 2) if o % 7 in (1, 2)}):
        for X in (1, 16, 127, 512):
            for s in (1, 2):
                elements = set()
                right = F(0)
                for o in roots:
                    n, j = o, 0
                    while n <= X:
                        elements.add(n)
                        right += F(1, o**s)*F(1, 2**(j*s))
                        n *= 2
                        j += 1
                check(sum((F(1, n**s) for n in elements), F(0)) == right, "dyadic mass identity")
                cases += 1
    check(cases == item["odd_core_identity_cases"], "odd-core case count")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("report", type=Path)
    args = parser.parse_args()
    report = json.loads(args.report.read_text())
    expected_digest = report.pop("semantic_sha256")
    check(seal(report) == expected_digest, "semantic digest")
    check(report["schema"] == "X-ASTRA-001-v1" and report["status"] == "FINITE_CHECKS_ONLY_NOT_A_COLLATZ_PROOF", "scope metadata")
    check(set(report) == {"schema", "status", "algebra", "affine_first_passage", "first_passage_pilot", "weights", "green"}, "report fields")
    check([(r["X"], r["Y"], r["cap"]) for r in report["affine_first_passage"]] == [(256, 16, 8), (512, 32, 10)], "AP coverage")
    check([r["k"] for r in report["first_passage_pilot"]] == [8, 10, 12, 14, 16, 18], "pilot coverage")
    check_algebra(report["algebra"])
    for row in report["affine_first_passage"]:
        check_affine(row)
    for item in report["first_passage_pilot"]:
        check_pilot(item)
    check_weights(report["weights"])
    check_green(report["green"])
    print("INDEPENDENT REPLAY PASS", expected_digest)


if __name__ == "__main__":
    main()
