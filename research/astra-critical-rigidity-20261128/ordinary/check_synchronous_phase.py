"""Exact finite checks for the shortcut phase and common-date decomposition."""
from collections import Counter
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def step(value):
    return (3 * value + 1) // 2 if value % 2 else value // 2


def orbit(value, clock):
    for _ in range(clock):
        value = step(value)
    return value


def entry_phase(value):
    elapsed = 0
    while value not in (1, 2):
        require(elapsed < 2000, "finite domain did not enter the known cycle")
        value = step(value)
        elapsed += 1
    return elapsed, (value - 1 - elapsed) % 2


def moment(counts, arms):
    return sum(count ** arms for count in counts.values())


def main():
    limit = 4096
    entries = {n: entry_phase(n) for n in range(1, 3 * limit + 2)}
    for n in range(1, limit + 1):
        require(entries[2 * n][1] == (entries[n][1] - 1) % 2, "even phase")
        if n % 2:
            require(entries[3 * n + 1][1] == entries[n][1], "odd triple phase")
    rows = []
    direct_pairs = 0
    for size in (15, 64, 257, 1024, 4096):
        phases = Counter(entries[n][1] for n in range(1, size + 1))
        for clock in (0, 3, 12, 32, 64, 173):
            entered = Counter()
            off = Counter()
            later_entry = {}
            values = [orbit(n, clock) for n in range(1, size + 1)]
            for n, val in enumerate(values, 1):
                t, phase = entries[n]
                if t <= clock:
                    require(val == 1 + (phase + clock) % 2, "entered phase state")
                    entered[phase] += 1
                else:
                    require(val > 2, "unentered state")
                    require(later_entry.setdefault(val, t) == t, "different later entry dates")
                    off[val] += 1
            histogram = Counter(values)
            off_entry_counts = Counter(entries[n][0] for n in range(1, size + 1)
                                       if entries[n][0] > clock)
            for arms in (2, 3, 4):
                observed = moment(histogram, arms)
                require(observed == moment(entered, arms) + moment(off, arms), "clock partition")
                require(moment(off, arms) <= moment(off_entry_counts, arms), "entry atom bound")
                require(observed <= moment(phases, arms), "eventual fusion bound")
                if size <= 64 and arms == 2:
                    direct_pairs += size * size
                    actual = sum(left == right for left in values for right in values)
                    require(actual == observed, "direct ordered pairs")
            rows.append([size, clock, sum(entered.values()), moment(histogram, 2),
                         moment(entered, 2), moment(phases, 2)])
    print(json.dumps({"cutoff": limit, "exact_even_edges": limit, "exact_odd_edges": limit // 2,
                      "distinct_integer_sources_certified": len(entries), "direct_pairs": direct_pairs,
                      "rows_size_clock_entered_observed_oncycle_eventual": rows}, indent=2))


if __name__ == "__main__":
    main()
