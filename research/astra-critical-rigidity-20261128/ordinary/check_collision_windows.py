"""Verify finite trace tests and the deterministic window and phase identities."""

from fractions import Fraction
from hashlib import sha256
from itertools import product
import json
from pathlib import Path


def require(condition, message):
    if not condition:
        raise ValueError(message)


def native_trace(source, deadline):
    path = [source]
    for _ in range(deadline):
        value = path[-1]
        path.append((3 * value + 1) // 2 if value % 2 else value // 2)
    return path


def ordinary_tests():
    counts = {"full": 0, "terminal": 0, "full_without_terminal": 0}
    dates = (18, 4)
    paths = [native_trace(n, dates[0]) for n in range(1, 97)]
    for left, right in product(paths, repeat=2):
        full = bool(set(left) & set(right))
        terminal = bool(set(left[-dates[1]:]) & set(right[-dates[1]:]))
        direct_full = any(x == y for x in left for y in right)
        direct_end = any(x == y for x in left[-dates[1]:] for y in right[-dates[1]:])
        require(direct_full == full and direct_end == terminal, "ordinary witness disagreement")
        require(not terminal or full, "terminal inclusion")
        counts["full"] += full
        counts["terminal"] += terminal
        counts["full_without_terminal"] += full and not terminal
    require(counts["full_without_terminal"] == counts["full"] - counts["terminal"], "event difference")
    require(0 < counts["terminal"] < counts["full"], "missing ordinary test class")
    return counts


def spine_tests():
    checked = 0
    for arrivals in product(range(6), repeat=3):
        for deadline in range(8):
            for width in range(9):
                # Identical nonnegative indices denote the shared injective tail.
                start = max(0, deadline - width)
                traces = [{t - a for t in range(start, deadline + 1) if t >= a} for a in arrivals]
                condition = max(arrivals) <= deadline and max(arrivals) - min(arrivals) <= width
                require(bool(set.intersection(*traces)) == condition, "spine interval test")
                checked += 1
    return checked


def phase_tests():
    checked = 0
    for period in range(1, 8):
        for arms in (2, 3, 4):
            hits = [Fraction(0)]
            for span in range(1, period + 2):
                count = sum(all((end - phases[0]) % period < span for end in phases[1:])
                            for phases in product(range(period), repeat=arms))
                hits.append(Fraction(count, period ** arms))
                require(hits[-1] == Fraction(min(span, period), period) ** (arms - 1),
                        "anchored phase probability")
                checked += period ** arms
            diffs = [None] + [(hits[t] - hits[t - 1]) / (t ** (arms - 1) - (t - 1) ** (arms - 1))
                              for t in range(1, len(hits))]
            for t in range(1, period + 1):
                recovered = t ** (arms - 1) * (diffs[t] - diffs[t + 1])
                require(recovered == int(t == period), "period recovery")
    return checked


if __name__ == "__main__":
    manuscript = Path(__file__).with_name("ORDINARY_COLLISIONS_IN_TIME_WINDOWS.md")
    print(json.dumps({"ordinary_pairs": 96 ** 2, "ordinary_events": ordinary_tests(),
                      "synthetic_injective_spine_cases": spine_tests(),
                      "synthetic_periodic_phase_tuples": phase_tests(),
                      "scope": "finite native checks and deterministic models only",
                      "manuscript_sha256": sha256(manuscript.read_bytes()).hexdigest()},
                     sort_keys=True, indent=2))
