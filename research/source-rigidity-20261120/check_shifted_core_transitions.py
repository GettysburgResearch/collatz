#!/usr/bin/env python3
"""Exact finite algebra controls for shifted core transitions.

This is not a verifier of Evertse's theorem, an escaping orbit, the
optional compressed-word theorem, or the Collatz conjecture.
Assertions are explicit and remain active under python -OO.
"""

from __future__ import annotations

import json
from fractions import Fraction
from itertools import product
from math import gcd, lcm


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def val(n: int, p: int) -> int:
    require(n > 0 and p >= 2, "valuation domain")
    answer = 0
    while n % p == 0:
        n //= p
        answer += 1
    return answer


def odd_step(n: int) -> tuple[int, int]:
    require(n > 0 and n % 2 == 1, "ordinary odd domain")
    v = 3 * n + 1
    a = val(v, 2)
    return v >> a, a


def core(n: int, pool: tuple[int, ...]) -> tuple[int, int]:
    require(n > 0, "positive core domain")
    q = n
    for p in pool:
        while q % p == 0:
            q //= p
    return q, n // q


def pool_unit(u: Fraction, pool: tuple[int, ...]) -> bool:
    if u == 0:
        return False
    return core(abs(u.numerator), pool)[0] == 1 and core(u.denominator, pool)[0] == 1


def order_mod(a: int, p: int) -> int:
    require(gcd(a, p) == 1, "multiplicative order domain")
    residue = a % p
    answer = 1
    while residue != 1:
        residue = residue * a % p
        answer += 1
        require(answer <= p, "finite prime order")
    return answer


def subsums(values: tuple[Fraction, ...]) -> list[int]:
    return [
        mask
        for mask in range(1, 1 << len(values))
        if sum((v for i, v in enumerate(values) if mask >> i & 1), Fraction(0)) == 0
    ]


def audit_transition(
    n: int,
    pool: tuple[int, ...],
    encodings: dict[tuple, tuple[int, int, int]],
) -> dict[str, int]:
    nxt, a = odd_step(n)
    m, mp = n + 1, nxt + 1
    q, u = core(m, pool)
    qp, v = core(mp, pool)
    require(m == q * u and mp == qp * v, "full core factorization")
    require(all(q % p and qp % p for p in pool), "outside-pool cores")
    require((1 << a) * mp == 3 * m + (1 << a) - 2, "shifted affine identity")

    unit_triple = (Fraction(1 << (a - 1)), Fraction(u), Fraction((1 << (a - 1)) * v))
    coefficients = (Fraction(1), Fraction(3 * q, 2), Fraction(-qp))
    require(all(pool_unit(x, pool) for x in unit_triple), "the variables are P-units")
    values = tuple(c * x for c, x in zip(coefficients, unit_triple))
    require(sum(values) == 1, "three-term unit equation")
    zeros = subsums(values)
    if a >= 2:
        require(zeros == [], "every defect subsum nonzero")
        require(val(m, 2) == 1, "defect starts at sigma=1")
        require(((1 << (a - 1)) - 1) % gcd(q, qp) == 0, "core gcd localization")
    else:
        require(zeros == [6], "the unique exponent-one degeneracy is terms 2+3")
        require(q == qp, "exponent-one core is unchanged")

    encoding_key = (pool, q, qp, unit_triple)
    encoded_edge = (n, a, nxt)
    if encoding_key in encodings:
        require(encodings[encoding_key] == encoded_edge, "injective ordinary transition encoding")
    encodings[encoding_key] = encoded_edge

    if pool == (2, 3):
        sigma, tau = val(m, 2), val(m, 3)
        sigmap, taup = val(mp, 2), val(mp, 3)
        require(m == (1 << sigma) * 3**tau * q, "basic core coordinates")
        if a >= 2:
            b = a - 1
            require(
                (1 << b) + 3 ** (tau + 1) * q - (1 << (b + sigmap)) * 3**taup * qp == 1,
                "root-reconstructed defect equation",
            )

    return {
        "defect": int(a >= 2),
        "one_step": int(a == 1),
        "coefficient_outside_pool": int(any(not pool_unit(c, pool) for c in coefficients)),
        "a": a,
    }


def audit_run(n: int) -> int:
    sigma = val(n + 1, 2)
    current = n
    for h in range(sigma):
        require((current + 1) * (1 << h) == 3**h * (n + 1), "full exact one-run formula")
        nxt, a = odd_step(current)
        if h < sigma - 1:
            require(a == 1, "one-run interior")
        else:
            require(a >= 2, "first defect at exact endpoint")
        current = nxt
    return sigma


def audit_prefix(n0: int, cap: int = 150) -> dict[str, int]:
    ell = n0.bit_length()  # ceil(log2(n0+1)) for positive odd n0
    current = n0
    seen_odd = {n0}
    seen_shortcut = {n0}
    word: list[int] = []
    defects = 0
    length = 0
    run_completions = 0
    for N in range(1, cap + 1):
        nxt, a = odd_step(current)
        if nxt in seen_odd:
            break
        seen_odd.add(nxt)
        defects += int(a >= 2)
        require(N < ell * ((1 << (defects + 1)) - 1), "exact conservative fixed-source clock")
        require(nxt + 1 <= (n0 + 1) * (1 << N), "integer upward shifted-height bound")
        require(Fraction(nxt + 1) <= Fraction(3, 2) ** N * (n0 + 1), "sharp upward shifted-height bound")
        if a >= 2:
            run_completions += 1
            require(N <= ell * ((1 << defects) - 1), "integer completed-defect time bound")

        block = [1] + [0] * (a - 1)
        physical = current
        for bit in block:
            require(physical % 2 == bit, "shortcut parity spelling of actual exponent")
            physical = (3 * physical + 1) // 2 if bit else physical // 2
            require(physical not in seen_shortcut, "simple odd prefix gives simple shortcut segment")
            seen_shortcut.add(physical)
        require(physical == nxt, "same physical endpoint")
        word.extend(block)
        k = 1 + sum(left != right for left, right in zip(word, word[1:]))
        require(k <= 2 * defects + 1, "number of constant-letter blocks")
        require(len(word) >= N, "shortcut clock dominates odd clock")
        length = N
        current = nxt
    return {"odd_edges": length, "shortcut_edges": len(word), "defects": run_completions}


def audit_creation(pool: tuple[int, ...], multiplier: int) -> dict[str, int]:
    modulus = 1
    for p in pool:
        if p not in (2, 3):
            modulus = lcm(modulus, order_mod(3, p))
    k = modulus * multiplier
    n = 2 * 3 ** (2 * k) - 1
    nxt, a = odd_step(n)
    outgoing = (3 ** (2 * k + 1) + 1) // 4
    require(a == 2, "creation family fixed division exponent")
    require(nxt == (3 ** (2 * k + 1) - 1) // 2, "creation exact endpoint")
    require(core(n + 1, pool)[0] == 1, "creation incoming core")
    require(core(nxt + 1, pool)[0] == outgoing, "complete outside-pool endpoint")
    require(val(nxt + 1, 2) == 1 and val(nxt + 1, 3) == 0, "endpoint smooth part exactly two")
    require(all(outgoing % p != 0 for p in pool), "all selected primes avoided")
    require(all(outgoing % p == 1 for p in pool if p not in (2, 3)), "exact extra-prime residue")
    require(outgoing > 1, "nontrivial outgoing core")
    return {"k": k, "incoming_bits": n.bit_length(), "outgoing_core_bits": outgoing.bit_length()}


def main() -> None:
    pools = ((2, 3), (2, 3, 5), (2, 3, 5, 7, 11))
    sources = set(range(1, 2048, 2))
    sources.update((1 << sigma) * q - 1 for sigma, q in product(range(1, 21), (1, 5, 7, 35, 143)))
    sources.update(((1 << a) - 1) // 3 for a in (16, 64, 256, 1024))
    sources.update((5 * (1 << a) - 1) // 3 for a in (17, 65, 257, 1025))
    encodings: dict[tuple, tuple[int, int, int]] = {}
    transition_totals = {"defect": 0, "one_step": 0, "coefficient_outside_pool": 0}
    max_a = 0
    for n, pool in product(sorted(sources), pools):
        counts = audit_transition(n, pool, encodings)
        for key in transition_totals:
            transition_totals[key] += counts[key]
        max_a = max(max_a, counts["a"])

    run_checks = sum(audit_run(n) for n in sorted(sources))
    prefix_totals = {"odd_edges": 0, "shortcut_edges": 0, "defects": 0}
    prefix_sources = tuple(range(1, 100, 2)) + (127, 255, 511, 1023)
    for n0 in prefix_sources:
        counts = audit_prefix(n0)
        for key in prefix_totals:
            prefix_totals[key] += counts[key]

    creations = [
        {"pool": list(pool), **audit_creation(pool, multiplier)}
        for pool, multiplier in product(pools, range(1, 4))
    ]

    # Negative controls demonstrate why the theorem has its exact scope.
    controls = []
    nxt, a = odd_step(3)
    require(a == 1 and subsums((Fraction(1), Fraction(6), Fraction(-6))) == [6], "one-step degeneracy control")
    controls.append("a=1 has the forbidden zero subsum")

    cyc, acyc = odd_step(1)
    require((cyc, acyc) == (1, 2), "repeated-cycle control")
    repeated = [(1, 2, 1)] * 7
    require(len(set(repeated)) == 1 and len(repeated) == 7, "distinct transitions versus occurrences")
    controls.append("repeated cycle occurrences are one distinct transition")

    n5, a5 = odd_step(5)
    require((1 << a5) * (n5 + 1) != 3 * (5 + 1), "omitted shifted correction is false")
    controls.append("dropping 2^a-2 breaks the shifted identity")

    require(not pool_unit(Fraction(21, 2), (2, 3)), "coefficient support is not unit support")
    require(core(14, (2, 3))[0] == 7, "nonunit core coefficient control")
    controls.append("rational coefficients can use primes outside the unit pool")

    require(core(13, (2, 3))[0] != core(14, (2, 3))[0], "shifted versus unshifted core control")
    controls.append("the cofactor of n is not the cofactor of n+1")

    n17, a17 = odd_step(17)
    require(a17 == 2 and (core(18, (2, 3))[0], core(n17 + 1, (2, 3))[0]) == (1, 7), "last-endpoint core control")
    controls.append("the final endpoint must be included in the core set")

    try:
        odd_step(2)
    except RuntimeError:
        controls.append("even input rejected")
    else:
        raise RuntimeError("even-input validation failed")

    # Check the stated constant without evaluating transcendental logarithms.
    B2 = (9 * 2**35) ** 81
    require(B2 == 2**2835 * 3**162 and B2 < 2**3092, "source-theorem arithmetic constant")

    report = {
        "status": "finite exact controls passed",
        "scope": "No all-time, external S-unit, or compressed-word theorem verified by computation.",
        "pools": [list(pool) for pool in pools],
        "distinct_ordinary_sources": len(sources),
        "transition_checks": len(sources) * len(pools),
        "transition_counts": transition_totals,
        "maximum_observed_division_exponent": max_a,
        "injective_encoding_keys": len(encodings),
        "exact_run_formula_checks": run_checks,
        "simple_prefix_sources": len(prefix_sources),
        "simple_prefix_totals": prefix_totals,
        "outside_prime_creation_controls": creations,
        "negative_controls": controls,
        "B2_binary_length": B2.bit_length(),
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
