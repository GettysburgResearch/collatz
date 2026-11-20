#!/usr/bin/env python3
"""Exact finite checks for CA1--CA3; not a Collatz decision procedure."""
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import json


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def oddpart(n):
    require(n > 0, "positive ordinary domain")
    while n % 2 == 0:
        n //= 2
    return n


def b(n, M):
    return int(oddpart(n) <= M)


def shortcut(n):
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def accelerated(n):
    require(n % 2 == 1, "odd source")
    return oddpart(3 * n + 1)


def enclose_decimal(lo, hi, scale=10**12):
    require(lo <= hi, "interval order")
    return {
        "scale": scale,
        "lower_integer": lo.numerator * scale // lo.denominator,
        "upper_integer": -((-hi.numerator * scale) // hi.denominator),
    }


def inward_fibers(M, terms=6, prefix_cap=None):
    lo = F(0)
    hi = F(0)
    prefix = F(0)
    fibers = 0
    terms_replayed = 0
    for t in range(1, M + 1, 2):
        if t % 3 == 0:
            continue
        a = 2 if t % 3 == 1 else 1
        x = ((1 << a) * t - 1) // 3
        while x <= M:
            a += 2
            x = 4 * x + 1
        fibers += 1
        if prefix_cap is not None:
            y = x
            while y <= prefix_cap:
                require(accelerated(y) == t, "literal predecessor")
                prefix += F(1, y)
                y = 4 * y + 1
        for _ in range(terms):
            require(x % 2 == 1 and accelerated(x) == t, "exact fiber legality")
            require(x > M, "inward crossing")
            term = F(1, x)
            lo += term
            hi += term
            terms_replayed += 1
            x = 4 * x + 1
        # Every remaining inverse exponent is included, with a two-sided tail.
        lo += F(4, 3 * x + 1)
        hi += F(4, 3 * x)
    return lo, hi, prefix, fibers, terms_replayed


def main():
    rows = []
    domain_checks = 0
    literal_checks = 0
    fibers_total = 0
    terms_total = 0
    cases = (1, 2, 3, 4, 7, 16, 31, 64, 127, 256, 511, 1024)
    for M in cases:
        L = 2 * sum((F(1, n) for n in range(1, M + 1, 2)), F(0))
        d3 = 2 * sum((F(1, n) for n in range(1, M + 1, 2) if 3*n > M), F(0))
        outward = sum((F(1, n) for n in range(1, M + 1, 2)
                       if accelerated(n) > M), F(0))
        cap = max(4096, 8*M)
        ilo, ihi, iprefix, fibers, terms = inward_fibers(M, prefix_cap=cap)
        dlo, dhi = outward + ilo, outward + ihi
        require(dhi < 4, "CA2 whole-source upper bound")
        require(dlo > 0, "cutoff is not exactly T invariant")
        direct = F(0)
        for n in range(1, cap + 1):
            direct += F(abs(b(shortcut(n), M) - b(n, M)), n)
            require(b(2*n, M) == b(n, M), "exact doubling invariance")
            require(abs(b(3*n, M)-b(n, M)) == int(M < 3*oddpart(n) <= 3*M),
                    "tripling boundary identity")
            literal_checks += 1
        require(direct == outward + iprefix, "independent literal/fiber prefix comparison")
        require(direct < dlo, "positive infinite input beyond the prefix")
        for n in range(1, M + 1, 2):
            a = 0
            value = 3*n + 1
            while value % 2 == 0:
                a += 1
                value //= 2
            require((3*n + 1) % (1 << (a+1)) == (1 << a), "exact valuation residue")
            domain_checks += 1
        rows.append({
            "M": M,
            "mass": enclose_decimal(L, L),
            "tripling_defect": enclose_decimal(d3, d3),
            "actual_T_defect": enclose_decimal(dlo, dhi),
            "T_normalized_l1_residual": enclose_decimal(dlo/L, dhi/L),
            "tripling_normalized_l1_residual": enclose_decimal(d3/L, d3/L),
            "literal_source_cutoff": cap,
            "inward_fibers": fibers,
        })
        fibers_total += fibers
        terms_total += terms

    # The fixed-valuation constant has a separate exact dyadic coefficient check.
    valuation_controls = []
    for A in (2, 3, 4, 8, 16, 32):
        mass = sum((F(1, 1 << (a+1)) for a in range(2, A+1)), F(0))
        moment = sum((F(a, 1 << (a+1)) for a in range(2, A+1)), F(0))
        require(mass + F(1, 1 << (A+1)) == F(1,4), "geometric mass")
        require(moment + F(A+2, 1 << (A+1)) == F(3,4), "geometric first moment")
        valuation_controls.append(A)

    # Meaningful controls against errors in the mathematical interface.
    for M in (3, 7, 31):
        require(b(M, M) == 1 and b(shortcut(M), M) == 0,
                "refute promotion of approximate to exact invariance")
    point_mass_2_norm = F(1,2)
    point_mass_2_pullback = F(1,1) + F(1,4)
    require(point_mass_2_pullback / point_mass_2_norm == F(5,2),
            "odd and even preimages in actual operator norm")
    require(b(shortcut(6), 3) == b(6, 3),
            "an even input must not inherit its odd part's T defect")
    require(accelerated(3) == 5 and 3 % 4 == 3,
            "valuation-one outflow cannot be dropped")
    require(all(accelerated(n) % 3 != 0 for n in range(1, 4096, 2)),
            "no odd preimages at a ternary-multiple endpoint")

    print(json.dumps({
        "schema": "collatz-critical-cutoffs/v1",
        "scope": "finite exact arithmetic and whole-source intervals at named M; no limiting proof or Collatz resolution",
        "source_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "cases": rows,
        "literal_source_checks": literal_checks,
        "valuation_domain_checks": domain_checks,
        "inward_fibers": fibers_total,
        "exact_fiber_terms": terms_total,
        "valuation_sum_controls": valuation_controls,
        "negative_controls": 7,
        "result": "PASS",
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
