"""Check the finite run and packet ledgers on actual unmatched ordinary pairs."""
from collections import Counter
from dataclasses import dataclass
from itertools import groupby
import json

from check_line_shadow_structure import require, step


@dataclass(frozen=True)
class Date:
    states: tuple
    gap: int

    @property
    def bits(self):
        return tuple(x % 2 for x in self.states)

    def relative(self, arm):
        return self.gap if arm == 1 else -self.gap

    def descending_numerator(self, arm):
        level = -self.relative(arm)
        require(level >= 0, "not a descending line")
        return 3**level * self.states[arm] - self.states[1 - arm]


def native_states(source, cap):
    pair = source, 3 * source
    gap = 1
    states = [Date(pair, gap)]
    for _ in range(cap):
        first, second = pair
        gap += second % 2 - first % 2
        pair = step(first), step(second)
        if pair[0] == pair[1]:
            break
        states.append(Date(pair, gap))
    return states


def scalar_packet(level, u, k):
    require(level >= k and u > 0 and u % 2 and u % 3, "invalid scalar entry")
    times = []
    grade = 0
    while level and (grade < k or u % 2 == 0):
        odd = u % 2
        times.append((level, u, odd))
        level -= odd
        grade += odd
        u = (u + odd * 3**level) // 2
    return times


def inspect(states, k, counts):
    clock = len(states) - 1
    records = states[:-1]
    grade = sum(sum(row.bits) for row in records)
    size = grade + 2
    events = [index for index, row in enumerate(records) if sum(row.bits)]
    starts = []
    for index in events:
        if (not starts or records[index].bits == (1, 1)
                or records[index].bits != records[starts[-1]].bits):
            starts.append(index)
    require(events and starts[0] == 0 and records[0].bits == (1, 1), "missing initial piece")
    visits = Counter()
    packets = []
    labels = [None] * clock
    for position, start in enumerate(starts):
        end = starts[position + 1] if position + 1 < len(starts) else clock
        bits = records[start].bits
        if bits == (1, 1):
            require(all(row.bits == (0, 0) for row in records[start + 1:end]), "joint coast")
            labels[start:end] = ["joint"] * (end - start)
            continue
        arm = bits.index(1)
        for t in range(start, end):
            row = records[t]
            require(row.bits[1 - arm] == 0, "wrong physical moving arm")
            rel = row.relative(arm)
            odd = row.bits[arm]
            if rel < 0:
                d = row.descending_numerator(arm)
                after = states[t + 1].descending_numerator(arm)
                require(2 * after == d + odd * 3**(-rel - odd), "descending recurrence")
                require(d % 3 and d % 2 == odd, "incorrect scalar parity or ternary unit")
                labels[t] = "negative" if d < 0 else "positive"
                visits[-rel] += odd
                counts["negative_to_positive"] += d < 0 < after
                counts["arrivals_at_zero"] += rel == -1 and odd
                counts["descending_first_arm" if arm == 0 else "descending_second_arm"] += odd
            else:
                d = 3**rel * row.states[1 - arm] - row.states[arm]
                nxt = states[t + 1]
                after = 3**nxt.relative(arm) * nxt.states[1 - arm] - nxt.states[arm]
                require(d and after and 2 * after == (3**odd) * d - odd,
                        "outward recurrence including reorientation")
                labels[t] = "outward"
                counts["outward_from_zero"] += rel == 0 and odd
        for kind, dates in groupby(range(start, end), key=lambda t: labels[t]):
            dates = list(dates)
            if kind != "positive":
                continue
            marks = [t for t in dates if records[t].bits[arm]]
            for mark in range(0, len(marks), k):
                indices = marks[mark:mark + k]
                if len(indices) < k:
                    counts["incomplete_tails"] += 1
                    continue
                first = indices[0]
                stop = marks[mark + k] if mark + k < len(marks) else dates[-1] + 1
                row = records[first]
                level = -row.relative(arm)
                u = row.descending_numerator(arm)
                model = scalar_packet(level, u, k)
                actual = [(-records[t].relative(arm), records[t].descending_numerator(arm),
                           records[t].bits[arm]) for t in range(first, stop)]
                require(actual == model[:len(actual)] and len(actual) <= len(model),
                        "actual scalar packet is not an initial segment")
                require(len(model) <= k * (1 + (3**size).bit_length()), "coast ceiling")
                counts["truncated_full_packets"] += len(actual) < len(model)
                counts["complete_full_packets"] += len(actual) == len(model)
                packets.append((level, len(model), len(actual)))
    require(all(labels) and len(labels) == clock, "unassigned dates")
    require(max(visits.values(), default=0) <= len(starts), "run visitation bound")
    require(len(packets) * k <= grade, "disjoint grade budget")
    for level, multiplicity in Counter(h for h, _, _ in packets).items():
        require(multiplicity <= visits[level], "excess descending level usage")
    for cutoff in (2 * size, 2 * k + 1):
        bad = {h for h, d, _ in packets if d >= cutoff}
        charged = sum(h in bad for h, _, _ in packets)
        require(charged <= max(visits.values(), default=0) * len(bad),
                "charged packet multiplicity")
        require(all(actual < cutoff for h, _, actual in packets if h not in bad),
                "false regular clock")
        if cutoff == 2 * k + 1:
            counts["small_threshold_multiple_charges"] += charged > len(bad)
    counts["prefix_packet_partitions"] += 1
    counts["classified_dates"] += clock


def main():
    counts = Counter()
    for source in range(1, 2048, 2):
        states = native_states(source, 100)
        for end in sorted({min(13, len(states) - 1), len(states) - 1}):
            if end:
                for k in (1, 2, 3, 4):
                    inspect(states[:end + 1], k, counts)
        counts["ordinary_sources"] += 1
    for key in ("negative_to_positive", "arrivals_at_zero", "outward_from_zero",
                "descending_first_arm", "descending_second_arm", "incomplete_tails",
                "complete_full_packets", "truncated_full_packets", "small_threshold_multiple_charges"):
        require(counts[key] > 0, f"missing control {key}")
    print(json.dumps(dict(counts), sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
