"""Bounded exact replay for the proposed three-ray partial selector.

No external dependencies. Python integers are arbitrary precision. Nothing
here treats a bounded computation as proof of universal convergence.
"""

from __future__ import annotations

from fractions import Fraction
import json

if not __debug__:
    raise SystemExit("Refusing optimized execution: this verifier requires assertions.")


def step(n: int) -> int:
    assert isinstance(n, int) and n > 0
    return (3 * n + 1) // 2 if n & 1 else n // 2


def replay(n: int, h: int) -> tuple[int, int, int]:
    """Return endpoint, odd count and affine bonus, using actual parities."""
    assert n > 0 and h >= 0
    initial = n
    odds = 0
    bonus = 0
    for j in range(h):
        if n & 1:
            odds += 1
            bonus = 3 * bonus + (1 << j)
        n = step(n)
    assert (1 << h) * n == 3**odds * initial + bonus
    return n, odds, bonus


def first_arrival(n: int, cap: int = 10000) -> tuple[int, int, int]:
    h = q = 0
    while n != 1:
        assert h < cap, "finite checker failed to certify this start"
        q += n & 1
        n = step(n)
        h += 1
    return h, q, 2 * q - h


def valuation(n: int) -> int:
    assert n != 0
    n = abs(n)
    return (n & -n).bit_length() - 1


def one_return(n: int) -> tuple[int, int]:
    """Evaluate the candidate, then verify its physical guard and endpoints."""
    k = valuation(n + 1)
    assert k >= 3
    u = (n + 1) >> k
    rvalue = 3 ** (k - 1) * u
    assert rvalue % 16 == 9
    m = (rvalue - 1) // 8
    assert m > 0 and m & 1
    assert replay(n, k + 4)[0] == step(3 * m)
    assert replay(3 * n, k + 3)[0] == m
    return m, k


def block_coefficients(ks: tuple[int, ...]) -> tuple[int, int, int]:
    """P,C,Q for x -> (P*x+C)/Q; independently compose fractions below."""
    p = q = 1
    c = 0
    for k in ks:
        pk, qk, ck = 3 ** (k - 1), 1 << (k + 3), 7 << k
        p, c, q = pk * p, pk * c + ck * q, qk * q
    return p, c, q


def finite_schedule(ks: tuple[int, ...]) -> list[int]:
    """Construct actual positive returns with the given valuations.

    The last entry specifies the valuation of the final endpoint, so the
    number of transitions is len(ks)-1. Compose the odd-part recurrences
    and solve the final oddness congruence, then replay every ordinary path.
    """
    assert len(ks) >= 2 and min(ks) >= 3
    p = q = 1
    c = 0
    for ki, kj in zip(ks, ks[1:]):
        pi, qi = 3 ** (ki - 1), 1 << (kj + 3)
        p, c, q = pi * p, pi * c + 7 * q, qi * q
    modulus = 2 * q
    u = ((q - c) * pow(p, -1, modulus)) % modulus
    assert u > 0 and u & 1
    n = (u << ks[0]) - 1
    result = [n]
    for ki, kj in zip(ks, ks[1:]):
        assert valuation(n + 1) == ki
        n, observed = one_return(n)
        assert observed == ki and valuation(n + 1) == kj
        result.append(n)
    return result


def count_full_blocks(n: int, block: tuple[int, ...], cap: int) -> int:
    """Replay until a prescribed physical guard or valuation fails."""
    completed = 0
    for _ in range(cap):
        for i, k in enumerate(block):
            if valuation(n + 1) != k:
                return completed
            u = (n + 1) >> k
            rvalue = 3 ** (k - 1) * u
            if rvalue % 16 != 9:
                return completed
            m, _ = one_return(n)
            if valuation(m + 1) != block[(i + 1) % len(block)]:
                return completed
            n = m
        completed += 1
    raise AssertionError("the finite exact stopping bound was not attained")


def main() -> None:
    counts: dict[str, int] = {}

    # TR-001: known terminating data and actual common-clock affine words.
    uniform = nonuniform = 0
    for n in range(1, 2001):
        hn, _, gn = first_arrival(n)
        h3, _, g3 = first_arrival(3 * n)
        h = max(hn, h3) + 2
        en, an, bn = replay(n, h)
        e3, a3, b3 = replay(3 * n, h)
        affine_identity = (an == a3 + 1 and bn == b3)
        assert affine_identity == (gn - g3 == 2)
        if affine_identity:
            assert en == e3
            for lift in (1, 3, 11):
                x = n + (lift << h)
                assert replay(x, h)[0] == replay(3 * x, h)[0]
            uniform += 1
        else:
            nonuniform += 1
    counts["grade_pairs"] = uniform + nonuniform
    counts["uniform_grade_pairs"] = uniform
    counts["nonuniform_grade_pairs"] = nonuniform
    for n in (1, 5):
        for j in range(9):
            x = n << j
            assert first_arrival(x)[2] - first_arrival(3 * x)[2] != 2
    counts["pointwise_without_cylinder_controls"] = 18

    # TR-002: exhaustive bounded aligned diagrams, including unequal clocks.
    pullbacks = 0
    for u in range(1, 513):
        lower = [replay(u, h)[0] for h in range(18)]
        upper = [replay(3 * u, h)[0] for h in range(18)]
        for p, m in enumerate(lower):
            for q, upper_endpoint in enumerate(upper):
                if upper_endpoint != 3 * m:
                    continue
                assert u == m << q
                assert p >= q
                assert p == q or replay(m, p - q)[0] == m
                pullbacks += 1
    counts["aligned_pullbacks"] = pullbacks

    # TR-003: independently replay the displayed endpoints for a dense grid.
    initial = immediate = reduced = oddvaluation = descent = 0
    for k in range(3, 19):
        for u in range(1, 256, 2):
            n, rvalue = (u << k) - 1, 3 ** (k - 1) * u
            assert replay(n, k)[0] == 3 * rvalue - 1
            assert replay(3 * n, k)[0] == rvalue - 1
            initial += 1
            if rvalue % 4 == 3:
                assert replay(n, k + 2)[0] == replay(3 * n, k + 2)[0]
                immediate += 1
                continue
            v = (rvalue - 1) // 4
            assert replay(n, k + 2)[0] == 9 * v + 2
            assert replay(3 * n, k + 2)[0] == v
            reduced += 1
            j = valuation(v)
            if j & 1:
                r, m = (j - 1) // 2, v >> j
                assert replay(n, k + 4 + 2 * r)[0] == step(3 ** (r + 1) * m)
                assert replay(3 * n, k + 3 + 2 * r)[0] == m
                oddvaluation += 1
                if k <= 7:
                    assert 3**r * m < n
                descent += (3**r * m < n)
                if r == 0:
                    assert (m < n) == (k <= 7)
    counts.update(initial_guard_replays=initial, immediate_mergers=immediate,
                  offset_reductions=reduced, odd_valuation_returns=oddvaluation,
                  lower_input_lists=descent)

    # Force all tested odd valuation values, including values rare in a grid.
    forced = 0
    for k in range(3, 16):
        p = 3 ** (k - 1)
        for r in range(10):
            modulus = 1 << (2 * r + 4)
            u = ((1 + (1 << (2 * r + 3))) * pow(p, -1, modulus)) % modulus
            n, rvalue = (u << k) - 1, p * u
            v = (rvalue - 1) // 4
            assert valuation(v) == 2 * r + 1
            m = v >> (2 * r + 1)
            assert replay(n, k + 4 + 2 * r)[0] == step(3 ** (r + 1) * m)
            assert replay(3 * n, k + 3 + 2 * r)[0] == m
            forced += 1
    counts["forced_odd_valuation_replays"] = forced

    transitions = samek_growth = 0
    for k in range(3, 21):
        p = 3 ** (k - 1)
        for next_k in range(1, 21):
            modulus = 1 << (next_k + 4)
            u = (((1 << (next_k + 3)) - 7) * pow(p, -1, modulus)) % modulus
            n = (u << k) - 1
            m, _ = one_return(n)
            assert valuation(m + 1) == next_k
            transitions += 1
            if next_k == k and k >= 8:
                assert m > n
                samek_growth += 1
    counts["prescribed_valuation_transitions"] = transitions
    counts["same_valuation_growth_controls"] = samek_growth

    # TR-004: exact ordinary witnesses for long fixed and periodic blocks.
    constant_runs = periodic_runs = repeated_factor_divisibilities = 0
    for k in range(8, 17):
        p, q = 3 ** (k - 1), 1 << (k + 3)
        d = p - q
        for length in range(1, 13):
            modulus = 2 * q**length
            u = (-7 * pow(d, -1, modulus)) % modulus
            n = (u << k) - 1
            assert valuation(d * u + 7) >= length * (k + 3)
            maximum = (valuation(d * u + 7) - 1) // (k + 3)
            assert count_full_blocks(n, (k,), maximum + 1) == maximum
            for _ in range(length):
                n, observed_k = one_return(n)
                assert observed_k == k and valuation(n + 1) == k
            constant_runs += 1
    counts["constant_schedule_witnesses"] = constant_runs

    blocks = ((8,), (9,), (8, 9), (9, 8), (8, 9, 8), (8, 10, 9))
    for block in blocks:
        p, c, q = block_coefficients(block)
        assert p > q
        a, b = Fraction(1), Fraction(0)
        for k in block:
            ak = Fraction(3 ** (k - 1), 1 << (k + 3))
            a, b = ak * a, ak * b + Fraction(7, 8)
        assert a == Fraction(p, q) and b == Fraction(c, q)
        for repeats in range(1, 9):
            schedule = block * repeats + (block[0],)
            ns = finite_schedule(schedule)
            xs = [n + 1 for n in ns]
            pu = qu = 1
            cu = 0
            for ki, kj in zip(block, block[1:] + block[:1]):
                pi, qi = 3 ** (ki - 1), 1 << (kj + 3)
                pu, cu, qu = pi * pu, pi * cu + 7 * qu, qi * qu
            assert pu == p and qu == q and cu & 1
            u0 = xs[0] >> block[0]
            maximum = (valuation((p - q) * u0 + cu) - 1) // valuation(q)
            assert count_full_blocks(ns[0], block, maximum + 1) == maximum
            divisor = q**repeats
            assert ((p - q) * xs[0] + c) % divisor == 0
            assert repeats * valuation(q) <= valuation((p - q) * xs[0] + c)
            assert all(x < y for x, y in zip(xs, xs[1:]))
            for i in range(0, len(xs) - 1, len(block)):
                assert q * xs[i + len(block)] == p * xs[i] + c
            # Independently verify denominator divisibility of every pair of
            # equal finite blocks in this realized ordinary schedule.
            for length in range(1, min(9, len(schedule))):
                seen: dict[tuple[int, ...], int] = {}
                for j in range(len(schedule) - length):
                    factor = schedule[j:j + length]
                    if factor in seen:
                        i = seen[factor]
                        _, _, den = block_coefficients(factor)
                        assert (xs[j] - xs[i]) % den == 0
                        assert xs[j] - xs[i] >= den >= 1 << (11 * length)
                        repeated_factor_divisibilities += 1
                    else:
                        seen[factor] = j
            periodic_runs += 1
    counts["periodic_schedule_witnesses"] = periodic_runs
    counts["equal_factor_divisibility_checks"] = repeated_factor_divisibilities

    # Variable nonperiodic tested schedules are ordinary finite witnesses too.
    arbitrary_runs = 0
    for seed in range(16):
        schedule = tuple(8 + ((seed * 29 + j * j + 3 * j) % 5) for j in range(19))
        ns = finite_schedule(schedule)
        assert all(a < b for a, b in zip(ns, ns[1:]))
        arbitrary_runs += 1
    counts["variable_schedule_witnesses"] = arbitrary_runs

    print(json.dumps({"status": "PASS", "scope": "bounded exact ordinary replay",
                      "universal_collatz_claim": False, "checks": counts}, indent=2))


if __name__ == "__main__":
    main()
