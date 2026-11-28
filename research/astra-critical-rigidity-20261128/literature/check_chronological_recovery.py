"""Replay finite real record gates, inverse recoveries and conditional low-bit fibres."""
from functools import lru_cache
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json


def require(condition, detail):
    if not condition:
        raise ArithmeticError(detail)


def step(n):
    return (3 * n + 1) // 2 if n % 2 else n // 2


def native(n, horizon):
    path = [n]
    for _ in range(horizon):
        path.append(step(path[-1]))
    return path


@lru_cache(maxsize=None)
def stopped(n):
    # Every integer actually used in this finite test must reach one within the cap.
    path = [n]
    while path[-1] != 1 and len(path) <= 5000:
        path.append(step(path[-1]))
    require(path[-1] == 1, ("finite stopping cap", n))
    return tuple(path)


def maximum_gain(path):
    low = path[0]
    numerator = denominator = 1
    for height in path:
        low = min(low, height)
        if height * denominator > numerator * low:
            numerator, denominator = height, low
    return Fraction(numerator, denominator)


def record_gates():
    gate_count = 0
    positive = 0
    largest = Fraction(1)
    for source in range(3, 1024, 2):
        path = stopped(source)
        gates = sorted({next(i for i, q in enumerate(path) if q % 2 and q <= bound)
                        for bound in (1, 3, 9, 27, 81, 243) if bound < source})
        for i in gates:
            require(min(path[:i]) > path[i], (source, "record", i))
        bounds = [0, *gates]
        gains = [maximum_gain(path[i:j + 1]) for i, j in zip(bounds, bounds[1:])]
        actual = maximum_gain(path)
        require(actual == max(gains), (source, "gate reset"))
        if actual >= 3:
            positive += 1
        largest = max(largest, actual)
        gate_count += len(gates)
    return {"positive_odd_sources": 511, "first_odd_records": gate_count,
            "gain_at_least_three": positive, "largest_ratio": str(largest)}


def inverse_paths(root=13, depth=14):
    stack = [(root,)]
    leaves = 0
    largest = Fraction(1)
    while stack:
        path = stack.pop()
        if len(path) == depth + 1:
            for i in range(1, len(path)):
                require(step(path[i]) == path[i - 1], ("true inverse", path))
            direct = max(Fraction(path[i], path[j])
                         for i in range(depth + 1) for j in range(i, depth + 1))
            require(direct == maximum_gain(path[::-1]), "inverse direction")
            largest = max(largest, direct)
            leaves += 1
            continue
        endpoint = path[-1]
        options = [2 * endpoint]
        if endpoint % 3 == 2:
            options.append((2 * endpoint - 1) // 3)
        for child in options:
            if child % 3 and child not in path:
                stack.append(path + (child,))
    require(leaves > 1 and largest > 1, "nontrivial inverse fixtures")
    return {"root": root, "depth": depth, "unit_leaves": leaves, "largest_ratio": str(largest)}


PATTERNS = ((3, 5), (7, 11, 17), (11, 17, 26))


@lru_cache(maxsize=None)
def avoids(n):
    path = stopped(n)
    return not any(path[i:i + len(pattern)] == pattern
                   for pattern in PATTERNS for i in range(len(path) - len(pattern)))


def has_completed_word(bits):
    # A stopped odd-to-odd word with multiplier >= 2 before first loss.
    one_dates = [i for i in range(1, len(bits)) if bits[i]]
    for start_index, first in enumerate(one_dates):
        for k, last in enumerate(one_dates[start_index + 1:], 1):
            if 3**k < 2**(last - first):
                break
            if 3**k >= 2 * 2**(last - first):
                return True
    return False


def conditional_fibres(t=6, h=6):
    shift = 1 << t
    period = 1 << h
    low = tuple(range(1, shift, 2))
    grade, intercept, event = {}, {}, set()
    for r in low:
        prefix = native(r, t)
        bits = [q % 2 for q in prefix[:-1]]
        grade[r], intercept[r] = sum(bits), prefix[-1]
        if has_completed_word(bits):
            event.add(r)
    require(0 < len(event) < len(low), "nontrivial conditioned event")
    used_pairs = joint_avoids = validated_absorptions = 0
    raw_comparison_avoidance = 0
    for m in range(1 << 12, (1 << 12) + period):
        final = {}
        for r in low:
            n = shift * m + r
            scaled = 3**grade[r]
            segment = native(scaled * m + intercept[r], h)
            require(native(n, t)[-1] == segment[0], ("affine entry", m, r))
            extra_grade = sum(q % 2 for q in segment[:-1])
            lifted = native(n + shift * period, t + h)[-1]
            require(lifted - segment[-1] == scaled * 3**extra_grade,
                    ("next high block", m, r))
            require(min(native(n, t + h)) > 26, "terminal-label cutoff")
            final[r] = (segment[-1], lifted, grade[r] + extra_grade, avoids(n))
            raw_comparison_avoidance += int(final[r][3])
        for r in event:
            for other in low:
                value, lifted, g, avoid = final[r]
                value2, lifted2, g2, avoid2 = final[other]
                canonical = value == value2 and g == g2
                require(canonical == (value == value2 and lifted == lifted2), "cylinder identity")
                if canonical:
                    require(avoid == avoid2, "terminal labels at merger")
                    validated_absorptions += 1
                joint_avoids += int(avoid2)
                used_pairs += 1
    require(joint_avoids == len(event) * raw_comparison_avoidance, "independent other label")
    require(0 < joint_avoids < used_pairs and 0 < validated_absorptions < used_pairs,
            "nonconstant labels and absorption on conditioned table")
    return {"prefix_bits": t, "comparison_bits": h, "conditioned_residues": len(event),
            "comparisons": used_pairs, "canonical_absorptions": validated_absorptions,
            "independent_arm_avoidance": str(Fraction(joint_avoids, used_pairs))}


if __name__ == "__main__":
    notes = ("MAXIMUM_PREMINIMUM_RECOVERY.md", "FIXED_ROOT_MAXIMUM_RECOVERY.md",
             "EXACT_LOG_SQUARE_CAPTURE.md")
    directory = Path(__file__).resolve().parent
    print(json.dumps({"source_sha256": {name: sha256((directory / name).read_bytes()).hexdigest()
                                         for name in notes},
                      "record_gates": record_gates(), "inverse_paths": inverse_paths(),
                      "conditioned_fibres": conditional_fibres(),
                      "scope": "exact finite native fixtures; no asymptotic estimate is tested"},
                     sort_keys=True, indent=2))
