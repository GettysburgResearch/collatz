#!/usr/bin/env python3
"""Exact finite controls for the all-length written and Lean block theorems.

This is not a cycle census or a proof of Collatz. No optimizer, external
package, floating-point number, or Python assert is used.
"""
from itertools import product
from math import gcd
import json


def require(ok, label):
    if not ok:
        raise ValueError(label)


def data(word):
    require(word and set(word) <= {"0", "1"}, "nonempty binary word")
    carry = 0
    for i, bit in enumerate(word):
        if bit == "1":
            carry = 3 * carry + 2**i
    return len(word), word.count("1"), carry


def six_free(n):
    require(n > 0, "positive smooth decomposition")
    for prime in (2, 3):
        while n % prime == 0:
            n //= prime
    return n


def pair_data(first, second, expected_carries=None):
    A, p, c0 = data(first)
    B, q, c1 = data(second)
    require(A == B and p == q, "equal shape")
    require(c0 != c1, "distinct carries")
    if expected_carries is not None:
        require([c0, c1] == expected_carries, "literal carries")
    P, Q = 3**p, 2**A
    delta = abs(c1 - c0)
    return {
        "words": [first, second], "A": A, "p": p, "P": P, "Q": Q,
        "carries": [c0, c1], "delta": delta,
        "delta_six_free": six_free(delta),
        "threshold": P + Q,
        "uniform_mixed_exclusion": six_free(delta) < P + Q,
    }


def check_mixed_words(pair, max_blocks):
    P, Q = pair["P"], pair["Q"]
    c0, c1 = pair["carries"]
    require(c0 < c1, "ordered carries")
    delta = c1 - c0
    count = 0
    for N in range(2, max_blocks + 1):
        weights = [Q**j * P**(N - 1 - j) for j in range(N)]
        S, D = sum(weights), Q**N - P**N
        require(D == (Q - P) * S, "complete denominator factorization")
        require(gcd(S, 6) == 1, "geometric sum units")
        for bits in product((0, 1), repeat=N):
            if not (0 in bits and 1 in bits):
                continue
            E = sum(w * bit for w, bit in zip(weights, bits))
            C = c0 * S + delta * E
            require(0 < E < S, "strict mixed digit interval")
            word = "".join(pair["words"][bit] for bit in bits)
            A, p, actual_carry = data(word)
            require(A == pair["A"] * N and p == pair["p"] * N,
                    "whole literal shape")
            require(actual_carry == C, "whole literal carry")
            require(C % D != 0, "finite control remains nonintegral")
            count += 1
    return count


def check_affine_cycle(P, Q, xs, denominator=None):
    """Nonvacuous controls of BC5; these are general affine, not Collatz."""
    N = len(xs)
    require(N > 1 and len(set(xs)) > 1, "nonconstant cyclic states")
    D = Q**N - P**N
    if denominator is not None:
        require(D == denominator, "retain complete closing denominator")
    cs = [Q * xs[(i + 1) % N] - P * xs[i] for i in range(N)]
    require(min(cs) >= 0, "nonnegative affine carries")
    G = 0
    for c in cs:
        G = gcd(G, abs(c - cs[0]))
    require(G > 0, "nonconstant carry gcd")
    span = max(cs) - min(cs)
    d = G // gcd(G, D)
    S = sum(Q**j * P**(N - 1 - j) for j in range(N))
    for i, x in enumerate(xs):
        complete = sum(Q**j * P**(N - 1 - j) * cs[(i + j) % N]
                       for j in range(N))
        require(complete == D * x, "all-cut complete cycle identities")
        require((complete - cs[0] * S) % G == 0, "common carry residue")
        require((x - xs[0]) % d == 0, "all boundary differences")
    require(span >= d * (P + Q), "minimum-edge capacity")
    return {"P": P, "Q": Q, "states": xs, "carries": cs,
            "D": D, "G": G, "lattice_step": d, "span": span,
            "capacity": d * (P + Q)}


def rejects(call):
    try:
        call()
    except ValueError:
        return True
    return False


def main():
    uv = pair_data("11101010", "11011010", [283, 319])
    require(uv["uniform_mixed_exclusion"], "UV all-period criterion")
    uv_count = check_mixed_words(uv, 12)
    nonsmooth = pair_data("11111000", "11110001", [211, 323])
    require(nonsmooth["delta_six_free"] == 7 and
            nonsmooth["uniform_mixed_exclusion"], "nonsmooth exclusion")
    nonsmooth_count = check_mixed_words(nonsmooth, 6)

    contexts = [("", ""), ("110", "10100"), ("0110110", "101010")]
    context_count = 0
    for first, second in [uv["words"], nonsmooth["words"]]:
        original = pair_data(first, second)
        for front, tail in contexts:
            contextual = pair_data(front + first + tail, front + second + tail)
            factor = 2**len(front) * 3**tail.count("1")
            require(contextual["delta"] == factor * original["delta"],
                    "literal common-context scaling")
            require(contextual["delta_six_free"] == original["delta_six_free"],
                    "context smooth-free invariance")
            require(contextual["uniform_mixed_exclusion"], "context criterion")
            context_count += 1

    run_count = 0
    for k in [1, 2, 5, 17, 41]:
        for left, right, delta in [
            ("1" + "0" * k, "0" * k + "1", 2**k - 1),
            ("1" * k + "0", "0" + "1" * k, 3**k - 2**k),
        ]:
            row = pair_data(left, right)
            require(row["delta"] == delta and row["uniform_mixed_exclusion"],
                    "run transposition exact criterion")
            run_count += 1

    affine_controls = 0
    for P, Q in [(3, 4), (9, 16), (243, 256)]:
        for pattern in [[0, 1], [0, 2, 1], [0, 3, 0, 1, 2], [0, 0, 1, 1]]:
            for scale in [1, 6, 35]:
                base = scale * (P + Q) * (max(pattern) + 1)
                check_affine_cycle(P, Q, [base + scale * t for t in pattern])
                affine_controls += 1

    sharp = check_affine_cycle(3, 4, [4, 5])
    require(sharp["span"] == sharp["capacity"] == 7,
            "sharp affine equality control")
    require(gcd(sharp["span"], sharp["D"]) == 7,
            "gcd cannot be dropped")
    not_covered = pair_data("1000011110", "0000111101", [2161, 3632])
    require(not_covered["delta_six_free"] == 1471 and
            not not_covered["uniform_mixed_exclusion"],
            "arbitrary mixed-word relocation is not automatically covered")

    damaged_rejections = [
        rejects(lambda: pair_data("11101010", "110110100")),
        rejects(lambda: pair_data("11101010", "11011010", [283, 320])),
        rejects(lambda: check_affine_cycle(3, 4, [4, 5], denominator=1)),
    ]
    require(all(damaged_rejections), "damaged controls rejected")
    print(json.dumps({
        "status": "PASS",
        "scope": "Exact finite controls of stated formulas; not a Collatz proof or all-word census",
        "uv": uv, "uv_mixed_schedules_checked": uv_count,
        "uv_max_block_count": 12,
        "nonsmooth": nonsmooth,
        "nonsmooth_mixed_schedules_checked": nonsmooth_count,
        "nonsmooth_max_block_count": 6,
        "common_context_controls": context_count,
        "run_transposition_controls": run_count,
        "nonvacuous_general_affine_controls": affine_controls,
        "sharp_affine_control_not_collatz": sharp,
        "uncovered_relocation_not_a_counterexample": not_covered,
        "damaged_controls_rejected": len(damaged_rejections),
    }, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
