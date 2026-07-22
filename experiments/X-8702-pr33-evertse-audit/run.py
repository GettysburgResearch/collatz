#!/usr/bin/env python3
"""Independent exact arithmetic audit for PR #33 at frozen head c9d62bc."""
from __future__ import annotations
import argparse, functools, hashlib, itertools, json, platform, random, sys
from fractions import Fraction
from pathlib import Path

SEED = 0x870233
RNG = random.Random(SEED)
P = (5, 30, 20, 56)
B = (9, 54, 36, 24)


def digest(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def v2(n):
    n = abs(n)
    return 10**9 if n == 0 else (n & -n).bit_length() - 1


def v3(n):
    n = abs(n)
    if n == 0:
        return 10**9
    c = 0
    while n % 3 == 0:
        n //= 3
        c += 1
    return c


@functools.lru_cache(maxsize=None)
def tower(kind, height):
    H = 1 << (11 * (height + 1))
    N = 3 ** (7 * (height + 1))
    A = H * P[kind] // 64
    C = (N * P[kind] + B[kind]) // 64
    assert H * P[kind] % 64 == 0
    assert (N * P[kind] + B[kind]) % 64 == 0
    assert 0 <= A < H and 0 < C < N
    return H, N, A, C


@functools.lru_cache(maxsize=None)
def inverse_pair(source_height, target_height):
    _, N, _, _ = tower(0, source_height)
    H, _, _, _ = tower(0, target_height)
    return pow(N, -1, H)


def connector(source_kind, source_height, target_kind, target_height):
    _, N, _, source_cap = tower(source_kind, source_height)
    H, _, target_anchor, _ = tower(target_kind, target_height)
    eta = ((target_anchor - source_cap) * inverse_pair(source_height, target_height)) % H
    theta = (source_cap + N * eta - target_anchor) // H
    assert 0 <= eta < H and 0 <= theta < N
    X = P[source_kind] + 64 * eta
    Y = P[target_kind] + 64 * theta
    assert N * X + B[source_kind] == H * Y
    return eta, theta, X, Y


def actual_connectors():
    cases = local = 0
    sample_rows = []
    for m in (12, 13):
        base = 1 << m
        delta = 1 << (m - 8)
        heights = [base + j * delta for j in range(257)] + [2 * base + 2 * delta]
        positions = (0, 127, 255) if m == 12 else (0, 255)
        sample_rng = random.Random(SEED + m)
        triples = sample_rng.sample(list(itertools.product(range(4), repeat=3)), 4 if m == 12 else 2)
        for position in positions:
            for i, j, k in triples:
                _, _, X0, Y0 = connector(i, heights[position], j, heights[position + 1])
                _, _, X1, _ = connector(j, heights[position + 1], k, heights[position + 2])
                cases += 2
                Hmiddle = tower(j, heights[position + 1])[0]
                Hnext = tower(k, heights[position + 2])[0]
                Nsource = tower(i, heights[position])[1]
                difference = Y0 - X1
                assert difference % 64 == 0
                local_constant = difference // 64
                correction = (-local_constant * pow(Nsource, -1, Hnext)) % Hnext
                output = (Nsource * correction + local_constant) // Hnext
                Z0 = X0 + 64 * Hmiddle * correction
                Z1 = X1 + 64 * Hnext * output
                assert Hmiddle * Z1 == Nsource * Z0 + B[i]
                local += 1
                if len(sample_rows) < 12:
                    sample_rows.append({"m": m, "position": position, "types": [i, j, k],
                        "eta_bits": (X0 - P[i]).bit_length(),
                        "correction_bits": correction.bit_length(), "Z0_mod_64": Z0 % 64})

        A = 7 * sum(heights[j] + 1 for j in range(256))
        E = 11 * sum(heights[j] + 1 for j in range(1, 257))
        assert A == Fraction(5369, 2) * (1 << m) + 1792
        assert E == Fraction(8459, 2) * (1 << m) + 2816
        L = 1 << (m - 9)
        for j in range(256):
            U = 11 * sum(heights[s] + 1 for s in range(1, j + 1))
            V = 7 * sum(heights[s] + 1 for s in range(j + 1, 256))
            assert U == 11 * j * (j + 513) * L + 11 * j
            assert V == 7 * (255 - j) * (j + 768) * L + 7 * (255 - j)
    return cases, local, sample_rows


def signed_quotients():
    cases = nonnegative = negative = 0
    for _ in range(20_000):
        odd_multiplier = RNG.randrange(1, 10**8) | 1
        next_radix = RNG.randrange(4 * odd_multiplier + 1, 8 * odd_multiplier + 100)
        cap = RNG.randrange(odd_multiplier)
        quotient = RNG.randint(-10_000, 10_000)
        stage_output = cap + odd_multiplier * quotient
        next_quotient, next_correction = divmod(stage_output, next_radix)
        assert cap + odd_multiplier * quotient == next_correction + next_radix * next_quotient
        if quotient >= 0:
            assert next_quotient >= 0
            assert next_quotient < Fraction(odd_multiplier, next_radix) * (quotient + 1)
            nonnegative += 1
        else:
            assert next_quotient <= -1
            K = -quotient - 1
            Knext = -next_quotient - 1
            assert next_radix * Knext == odd_multiplier * K + (odd_multiplier - cap) - (next_radix - next_correction)
            assert Knext < Fraction(odd_multiplier, next_radix) * (K + 1)
            negative += 1
        cases += 1
    return {"cases": cases, "nonnegative": nonnegative, "negative": negative}


def arithmetic_gates():
    assert 3**53 > 2**84 and 3**41 < 2**65
    cap_ratio = Fraction(161341, 10496) / Fraction(1085579, 256)
    endpoint_ratio = Fraction(6498, 346819)
    assert cap_ratio == Fraction(161341, 44508739) < Fraction(1, 275)
    assert endpoint_ratio < Fraction(1, 50)
    assert Fraction(2166, 346819) + Fraction(4332, 346819) == endpoint_ratio
    rows = 0
    for first, last, endpoint in itertools.product(range(4), repeat=3):
        assert v2(B[first]) <= 3 and v3(B[last]) <= 3 and v2(P[endpoint]) <= 3
        rows += 1
    intervals = []
    previous_high = None
    for m in range(12, 31):
        E = int(Fraction(8459, 2) * (1 << m) + 2816)
        low, high = E - 3, E + 3
        if previous_high is not None:
            assert low > previous_high
        previous_high = high
        intervals.append([m, low, high])
    return {"cap_height_ratio": f"{cap_ratio.numerator}/{cap_ratio.denominator}",
        "endpoint_product_ratio": f"{endpoint_ratio.numerator}/{endpoint_ratio.denominator}",
        "primitive_gcd_cap": 216, "primitive_rows": rows,
        "projective_intervals": intervals,
        "evertse_parameters": {"n": 257, "c": 1, "d": "1/50", "S0": [2, 3]}}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    parser.add_argument("--check-results", type=Path)
    args = parser.parse_args()
    connector_cases, local_cases, rows = actual_connectors()
    payload = {"experiment_id": "X-8702", "agent": "gpt56-pdr-01", "issue": 40,
        "frozen_pr3_interface": "f274dfeee3c9c391c48e58d8b57cb9f1759236f8",
        "frozen_pr33": "c9d62bce3e93f5785f72e4520bc576863d9379eb", "seed": SEED,
        "actual_connectors": {"connector_cases": connector_cases,
            "local_conjugacy_cases": local_cases, "sample_digest": digest(rows)},
        "signed_quotients": signed_quotients(), "arithmetic_gates": arithmetic_gates(),
        "external_source": {"author": "J.-H. Evertse",
            "title": "On sums of S-units and linear recurrences",
            "journal": "Compositio Mathematica 53 (1984), 225-244",
            "result": "Corollary 1", "source_theorem_executed_by_script": False}}
    payload["semantic_digest"] = digest(payload)
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text)
    if args.check_results and payload != json.loads(args.check_results.read_text()):
        print("frozen result mismatch", file=sys.stderr)
        return 1
    print(text, end="")
    print(json.dumps({"python": platform.python_version(), "platform": platform.platform()}, sort_keys=True), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
