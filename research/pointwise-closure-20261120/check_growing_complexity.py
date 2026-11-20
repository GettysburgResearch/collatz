#!/usr/bin/env python3
"""Finite exact arithmetic for GROWING_COMPLEXITY.md."""

import hashlib
import json
from math import comb


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def odd_step(n):
    require(n > 0 and n & 1, "positive odd source required")
    z = 3 * n + 1
    a = (z & -z).bit_length() - 1
    return z >> a, a


def sparse_residue_bound(S, m):
    require(S >= 2 and m >= 3, "S>=2 and m>=3 required")
    return sum(comb(m - 1, i) for i in range(min(S - 2, m - 1) + 1))


def finite_bound(N, S, m):
    require(N >= 1, "nonempty segment required")
    B = sparse_residue_bound(S, m)
    L = 1 << (m - 2)
    return sum((2 * L) ** r for r in range(S)) + ((N + L - 1) // L) * min(L, B)


def check_residue_periods():
    states_checked = 0
    cap_comparisons = 0
    digest = hashlib.sha256()
    for m in range(3, 17):
        modulus = 1 << m
        L = 1 << (m - 2)
        cosets = []
        for u in (1, 5):
            states = []
            x = u
            for _ in range(L):
                states.append(x)
                x = (3 * x) % modulus
            require(x == u and len(set(states)) == L, "incorrect exact period")
            cosets.append(set(states))
            states_checked += L
            for S in range(2, m + 3):
                observed = sum(x.bit_count() <= S - 1 for x in states)
                B = sparse_residue_bound(S, m)
                require(observed <= min(L, B), "coset count exceeds binomial bound")
                cap_comparisons += 1
                digest.update(f"{m}:{u}:{S}:{observed}:{B}\n".encode())
        require(not (cosets[0] & cosets[1]), "cosets overlap")
        require(cosets[0] | cosets[1] == set(range(1, modulus, 2)), "cosets miss odd residues")
        for S in range(2, m + 3):
            direct = sum(x.bit_count() <= S - 1 for x in range(1, modulus, 2))
            require(direct == sparse_residue_bound(S, m), "complete residue count mismatch")
        require(sparse_residue_bound(2, m) == 1, "S=2 boundary")
    return {"moduli_exponents": [3, 16], "coset_states": states_checked,
            "cap_comparisons": cap_comparisons, "sha256": digest.hexdigest()}


def check_actual_windows():
    windows = 0
    state_checks = 0
    for S in range(2, 9):
        for m in range(3, 9):
            L = 1 << (m - 2)
            for upper_bits in range(1, S):
                lower_bits = S - upper_bits
                for gap_extra in (0, 1, 5):
                    u = sum(1 << (3 * i) for i in range(upper_bits))
                    v = sum(1 << (2 * i) for i in range(lower_bits))
                    D = v.bit_length() + 2 * L + gap_extra
                    actual = (u << D) + v
                    shadow = v
                    A = 0
                    power3 = 1
                    sparse_count = 0
                    residues = set()
                    for j in range(L):
                        require(A < D, "cut exhausted")
                        require(actual == (power3 * u << (D - A)) + shadow,
                                "actual affine identity failed")
                        require(actual.bit_count() == (power3 * u).bit_count() + shadow.bit_count(),
                                "binary overlap")
                        sparse_count += actual.bit_count() <= S
                        residues.add((power3 * u) % (1 << m))
                        state_checks += 1
                        if j + 1 < L:
                            actual, a_actual = odd_step(actual)
                            shadow, a = odd_step(shadow)
                            require(a == a_actual, "shadow valuation changed")
                            A += a
                            power3 *= 3
                    require(len(residues) == L, "homogeneous residues repeat within window")
                    require(sparse_count <= min(L, sparse_residue_bound(S, m)),
                            "actual sparse window exceeds bound")
                    windows += 1
    return {"caps": [2, 8], "moduli_exponents": [3, 8],
            "windows": windows, "actual_state_checks": state_checks}


def trajectory(n):
    result = []
    seen = set()
    while n not in seen and len(result) < 1000:
        seen.add(n)
        result.append(n)
        if n == 1:
            break
        n, _ = odd_step(n)
    return result


def check_finite_occupancy():
    windows = 0
    inequalities = 0
    for n in range(1, 3000, 2):
        orbit = trajectory(n)
        for offset in {0, len(orbit) // 2}:
            for N in {len(orbit) - offset, min(20, len(orbit) - offset)}:
                states = orbit[offset:offset + N]
                require(N >= 1 and len(set(states)) == N, "invalid distinct segment")
                windows += 1
                require(sum(x.bit_count() <= 1 for x in states) <= 1, "one-bit boundary")
                for S in range(2, 9):
                    observed = sum(x.bit_count() <= S for x in states)
                    for m in range(3, 10):
                        require(observed <= finite_bound(N, S, m), "all-N occupancy inequality failed")
                        inequalities += 1
    return {"odd_starts_below": 3000, "distinct_windows": windows,
            "inequality_checks": inequalities}


def main():
    print(json.dumps({
        "status": "PASS",
        "scope": "finite exact replays only; the universal and asymptotic claims have written proofs",
        "residue_periods": check_residue_periods(),
        "separated_actual_windows": check_actual_windows(),
        "finite_occupancy": check_finite_occupancy(),
    }, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
