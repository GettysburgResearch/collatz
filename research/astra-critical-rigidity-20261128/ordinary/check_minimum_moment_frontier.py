"""Finite true minimum dates and independent first-landing/source moment ledgers."""

from collections import Counter
from hashlib import sha256
from pathlib import Path
import json


def guard(condition, message):
    if not condition:
        raise ValueError(message)


def step(n):
    return (3*n + 1) // 2 if n % 2 else n // 2


def native(n):
    path = [n]
    while path[-1] != 1:
        guard(len(path) < 1500, "ordinary finite trajectory exceeded the budget")
        path.append(step(path[-1]))
    return path


def odd_gates(n):
    values = [n]
    clocks = [0]
    while values[-1] != 1:
        numerator = 3*values[-1] + 1
        e = (numerator & -numerator).bit_length() - 1
        values.append(numerator >> e)
        clocks.append(clocks[-1] + e)
    return values, clocks


def main():
    nmax = 4096
    counts = Counter()
    dates = [0] + [len(native(n))-1 for n in range(1, nmax+1)]
    roots_by_experiment = {}
    for n in range(1, nmax+1):
        raw = native(n)
        i = (n & -n).bit_length()-1
        a = n >> i
        guard(dates[n] == i + dates[a], "even stripping lost the first minimum")
        counts["even_stripping_identities"] += 1
        if n % 6 == 3:
            moved = 4*n+1
            moved_path = native(moved)
            guard(moved % 3 != 0 and moved_path[3:] == raw[1:], "unit embedding tail")
            guard(dates[n] == 0 or len(moved_path)-1 == dates[n]+2, "unit embedding date")
            counts["odd_nonunit_embeddings"] += 1
        if n <= 1 or n % 2 == 0:
            continue
        values, clocks = odd_gates(n)
        for threshold in (1, 2, 4, 7, 16, 31, 63, 127, 511, 1023):
            if n <= threshold:
                continue
            j = next(i for i, x in enumerate(values) if x <= threshold)
            end, odd_date = values[j], clocks[j]
            native_date = next(i for i, x in enumerate(raw) if x <= threshold)
            guard(min(raw[:odd_date]) > end, "first odd entrance is not a strict record")
            guard((raw[native_date] == end << (odd_date-native_date)) and
                  dates[n] == odd_date + dates[end],
                  "native residual or last halving run is wrong")
            guard(raw[odd_date:] == native(end), "unfolded native suffix is wrong")
            for level in {1, 2, 3, 5, threshold, end, n, (n+end)//2}:
                t = next(k for k,x in enumerate(raw) if x <= level)
                frozen = next(k for k,x in enumerate(raw) if x <= max(threshold, level))
                guard(0 <= t-frozen <= dates[n]-native_date, "moving-cutoff path error")
                if level == 1:
                    guard(t-frozen == dates[n]-native_date, "endpoint does not attain max error")
                counts["native_cutoff_comparisons"] += 1
            if n > 1024:
                roots_by_experiment.setdefault(threshold, Counter())[end] += 1
                counts["ordinary_landing_atoms"] += 1
            counts["delayed_first_odd_arrivals"] += native_date < odd_date
            counts["clocked_first_landing_sources"] += 1
    for threshold, row in roots_by_experiment.items():
        guard(all(a % 2 == 1 and a <= threshold for a in row), "root outside window")
        guard(sum(row.values()) == 1536, "landing atoms fail to partition the source shell")
        counts["entire_disjoint_landing_rows"] += 1

    for M in (32, 63, 128, 1023, nmax):
        clocks = dates[1:M+1]
        histogram = Counter(clocks)
        for r in (1, 2, 3, 5):
            tail = M
            integral = 0
            for u in range(max(clocks)):
                tail -= histogram[u]
                integral += ((u+1)**r-u**r)*tail
            guard(integral == sum(k**r for k in clocks), "integer tail integration failed")
            counts["finite_empirical_moment_identities"] += 1
    guard(min(counts.values()) > 0, "uncovered control branch")
    folder = Path(__file__).resolve().parent
    names = ("MODERATE_DEVIATIONS_AT_THE_MINIMUM.md", "MINIMUM_CLOCK_MOMENT_INDEX.md")
    print(json.dumps({"scope": "exact finite ordinary ledgers, no inference on the limiting index",
                      "counts": dict(counts),
                      "manuscript_hashes": {name: sha256((folder/name).read_bytes()).hexdigest()
                                            for name in names}}, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
