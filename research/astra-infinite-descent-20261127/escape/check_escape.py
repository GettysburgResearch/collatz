"""Bounded exact replays for the original-source statements in this directory."""

from collections import defaultdict
from fractions import Fraction
from math import isqrt
import json


def check(condition, message):
    if not condition:
        raise ValueError(message)


def step(x):
    return (3 * x + 1) // 2 if x % 2 else x // 2


def trajectory(n, length):
    states = [n]
    grades = [0]
    offsets = [0]
    for t in range(length):
        bit = states[-1] % 2
        states.append(step(states[-1]))
        grades.append(grades[-1] + bit)
        offsets.append((3 if bit else 1) * offsets[-1] + bit * 2**t)
        check(
            2 ** (t + 1) * states[-1] == 3 ** grades[-1] * n + offsets[-1],
            "incorrect forward affine numerator",
        )
        check(
            2 ** grades[-1] * (offsets[-1] + 2 ** (t + 1))
            <= 3 ** grades[-1] * 2 ** (t + 1),
            "all-prefix grade bound failed",
        )
    return states, grades, offsets


def ceil_div(a, b):
    return (a + b - 1) // b


def check_meetings(J):
    native = 0
    K = J + isqrt(J)
    actual_unmet = {J: 0, K: 0}
    unaligned_sources = 0
    equal_slope_pairs = 0
    unequal_slope_pairs = 0
    protected_sources = 0
    for n in range(2**J, 2 ** (J + 1)):
        left, a, B = trajectory(n, K)
        right, b, C = trajectory(3 * n + 2, K)
        counted = left[J] == right[J] and a[J] == b[J] + 1
        if J <= 12:
            lift, al, _ = trajectory(n + 2**J, J)
            rlift, bl, _ = trajectory(3 * (n + 2**J) + 2, J)
            check(
                a[J] == al[J] and b[J] == bl[J]
                and (counted == (lift[J] == rlift[J] and al[J] == bl[J] + 1)),
                "native grade/meeting cylinder failed to lift",
            )
        native += not counted
        by_state = defaultdict(list)
        for j, value in enumerate(right):
            by_state[value].append(j)
        first_square = K + 1
        all_aligned = True
        for i, value in enumerate(left):
            for j in by_state.get(value, ()):
                first_square = min(first_square, max(i, j))
                P, Q = 2**j * 3**a[i], 2**i * 3 ** (b[j] + 1)
                L, R = 2**j * B[i], 2**i * (2 * 3**b[j] + C[j])
                check(P * n + L == Q * n + R, "two-clock affine crossing")
                if P == Q:
                    equal_slope_pairs += 1
                    check(i == j and a[i] == b[j] + 1, "equal slopes failed to align")
                else:
                    all_aligned = False
                    unequal_slope_pairs += 1
                    A = max(ceil_div(L, P), ceil_div(R, Q))
                    sep = ceil_div(min(P, Q), abs(P - Q))
                    check(n <= A * sep, "unequal slopes passed relative guard")
        for limit in actual_unmet:
            actual_unmet[limit] += first_square > limit
        if all_aligned and abs(a[J] - (b[J] + 1)) > K - J:
            protected_sources += 1
            check(first_square > K, "high native grade failed to protect the full square")
        unaligned_sources += not all_aligned
    check(actual_unmet[K] <= actual_unmet[J] <= native, "bounded search order")
    return {
        "J": J,
        "extended_deadline": K,
        "sources": 2**J,
        "native_counted_unmet": native,
        "native_two_clock_unmet": actual_unmet[J],
        "extended_two_clock_unmet": actual_unmet[K],
        "sources_with_some_unaligned_crossing": unaligned_sources,
        "equal_slope_crossings": equal_slope_pairs,
        "unequal_slope_crossings": unequal_slope_pairs,
        "high_gap_sources_certified_unmet": protected_sources,
    }


def in_octave(value, lower):
    # Both inputs are positive rational numbers. Return the unique dyadic lift
    # into [lower,2*lower), with its signed exponent.
    shift = lower.numerator.bit_length() - lower.denominator.bit_length()
    shift -= value.numerator.bit_length() - value.denominator.bit_length()
    scaled = value * Fraction(2) ** shift
    while scaled < lower:
        scaled *= 2
        shift += 1
    while scaled >= 2 * lower:
        scaled /= 2
        shift -= 1
    return scaled, shift


def max_gap(points):
    pts = sorted(set(points))
    return max(b / a for a, b in zip(pts, pts[1:] + [2 * pts[0]]))


def check_spreading(y, L, D):
    X = y * 2 ** (L + 3 + 6 * D) + 137
    S, B, v = 0, 0, y
    targets, realized = [], []
    largest_time = 0
    for d in range(D + 1):
        ideal, _ = in_octave(Fraction(1, 3**d), Fraction(1))
        targets.append(ideal)
        phase, _ = in_octave(Fraction(v, y), Fraction(1))
        realized.append(phase)
        z_ratio, r = in_octave(Fraction(v), Fraction(X))
        check(z_ratio.denominator == 1 and r >= 0, "integer leading halvings")
        z = int(z_ratio)
        t = S + r
        states, grades, _ = trajectory(z, t)
        check(states[-1] == y and y not in states[:-1], "first target arrival")
        check(grades[-1] == d and z % 3, "grade or unit error")
        check(2 * max(states) <= 3 * z + 1, "peak bound")
        check(3**d * v + B == 2**S * y, "inverse numerator")
        if d:
            check(5 * 2**L * B + 2**L * 3**d <= 8 * 2**S, "inverse slack")
        largest_time = max(largest_time, t)
        if d < D:
            low = L if d == 0 else 3
            e = next(e for e in range(low, low + 4) if 2**e * v % 9 in (4, 7))
            v = (2**e * v - 1) // 3
            B = 2**e * B + 3**d
            S += e
    factor = Fraction(5 * 2**L * y, 5 * 2**L * y - 8)
    check(max_gap(realized) <= factor * max_gap(targets), "actual phase maximum gap")
    return largest_time


def main():
    J_values = (4, 6, 8, 10, 12, 14)
    rows = [check_meetings(J) for J in J_values]
    targets = (1, 5, 7, 11, 43, 239, 1009, 2147483647)
    parameters = [(y, L, D) for y in targets for L in (3, 8, 19) for D in (1, 4, 9, 18)]
    times = [check_spreading(*p) for p in parameters]
    print(json.dumps({
        "two_clock_octaves": rows,
        "inverse_ladders": len(parameters),
        "checked_first_hits": sum(D + 1 for _, _, D in parameters),
        "maximum_replayed_first_hit_time": max(times),
    }, indent=2))


if __name__ == "__main__":
    main()
