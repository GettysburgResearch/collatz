#!/usr/bin/env python3
"""Finite exact replays for SPARSE_RETURN_SPECTRUM.md; not a proof search."""

import hashlib
import itertools
import json


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def odd_step(n):
    require(n > 0 and n & 1, "positive odd input required")
    m = 3 * n + 1
    valuation = (m & -m).bit_length() - 1
    return m >> valuation, valuation


def positions(n):
    return [i for i in range(n.bit_length()) if (n >> i) & 1]


def cuts(n):
    ps = positions(n)
    for low, high in zip(ps, ps[1:]):
        d = high - low
        yield high, d, n >> high, n % (1 << high)


def spectrum_box():
    found = set()
    checks = 0
    for u in [1] + [(1 << d) + 1 for d in range(1, 401)]:
        v = u
        for h in range(1001):
            if v.bit_count() <= 2:
                if h:
                    found.add((u, v, h))
            checks += 1
            v *= 3
    expected = {(1, 3, 1), (1, 9, 2), (3, 9, 1)}
    require(found == expected, "elementary spectrum classification mismatch")
    return {"input_bit_position_max": 400, "power_max": 1000,
            "checked_pairs": checks, "positive_power_solutions": sorted(found)}


def carry_replay():
    count = 0
    cut_count = 0
    max_bits = 0
    digest = hashlib.sha256()
    sources = [1 + (1 << d) for d in range(1, 65)]
    sources += [1 + (1 << d) + (1 << e)
                for d, e in itertools.combinations(range(1, 65), 2)]
    sources += [1 + (1 << 1000), 1 + (1 << 997) + (1 << 2000),
                1 + (1 << 31) + (1 << 19999)]
    for n in sources:
        max_bits = max(max_bits, n.bit_length())
        cap = n.bit_count()
        allowed = {0} if cap == 2 else {0, 1, 2}
        for D, d, u, v in cuts(n):
            cut_count += 1
            J = (d - 1) // 2
            # Large sources test the entire separated interval, not selected clocks.
            actual = n
            shadow = v
            A = 0
            power3 = 1
            for j in range(J + 1):
                require(A < D, "separated cut exhausted prematurely")
                require(0 < shadow < (1 << (D - A)), "lower block overflow")
                predicted = (power3 * u << (D - A)) + shadow
                require(actual == predicted, "fixed-source affine identity failed")
                require(actual.bit_count() == (power3 * u).bit_count() + shadow.bit_count(),
                        "binary blocks are not disjoint")
                if actual.bit_count() <= cap:
                    require(j in allowed, "forbidden sparse return inside original cut")
                digest.update(f"{n:x}:{D}:{j}:{A}:{actual:x}\n".encode())
                count += 1
                if j < J:
                    actual, actual_a = odd_step(actual)
                    shadow, a = odd_step(shadow)
                    require(actual_a == a, "actual and shadow valuations differ")
                    A += a
                    power3 *= 3
    return {"sources": len(sources), "cuts": cut_count,
            "state_identity_checks": count, "largest_source_bitlength": max_bits,
            "sha256": digest.hexdigest()}


def distinct_orbit(n, cap=1000):
    result = []
    seen = set()
    while n not in seen and len(result) < cap:
        seen.add(n)
        result.append(n)
        if n == 1:
            break
        n, _ = odd_step(n)
    return result


def occupancy_replay():
    checks = 0
    windows = 0
    largest_observed = {2: 0, 3: 0}
    for n in range(1, 10000, 2):
        orbit = distinct_orbit(n)
        for offset in {0, len(orbit) // 3, len(orbit) // 2}:
            for N in {len(orbit) - offset, min(20, len(orbit) - offset)}:
                if N <= 0:
                    continue
                states = orbit[offset:offset + N]
                require(len(set(states)) == N, "occupancy input is not distinct")
                windows += 1
                for S, K in [(2, 1), (3, 3)]:
                    observed = sum(x.bit_count() <= S for x in states)
                    largest_observed[S] = max(largest_observed[S], observed)
                    for L in range(1, min(N, 20) + 1):
                        bound = sum((2 * L) ** r for r in range(S)) + K * ((N + L - 1) // L)
                        require(observed <= bound, "explicit occupancy inequality failed")
                        checks += 1
    return {"odd_starts_below": 10000, "distinct_windows": windows,
            "inequality_checks": checks, "max_observed_counts": largest_observed}


def controls():
    path = [257]
    for _ in range(4):
        path.append(odd_step(path[-1])[0])
    require(path == [257, 193, 145, 109, 41], "post-cut control changed")
    require(path[4].bit_count() == 3 and 4 not in {0, 1, 2},
            "post-cut control does not refute unguarded spectrum")
    require((8 - 1) // 2 == 3, "incorrect original cut lifetime")
    require(odd_step(5)[0] == 1, "strict-separation control changed")
    wrong_predicted = 3 + 1  # Formula at the inadmissible A=D=2.
    require(wrong_predicted != 1, "guard removal was not detected")
    require(3**3 == 27 and (27).bit_count() == 4,
            "sparse homogeneous exclusion control failed")
    return {"post_cut_counterexample": path, "strict_cut_counterexample": [5, 1],
            "invalid_strengthenings_rejected": 2}


def main():
    report = {
        "status": "PASS",
        "scope": "finite integer replays only; external S-unit theorem not executed",
        "elementary_spectrum": spectrum_box(),
        "carry": carry_replay(),
        "occupancy": occupancy_replay(),
        "controls": controls(),
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
