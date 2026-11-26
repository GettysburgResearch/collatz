"""Audit the entry-fibre reconstruction on finite, injective physical path segments."""

from collections import defaultdict
import itertools
import json
import math


def require(condition, label):
    if not condition:
        raise ValueError(label)


def shortcut(value):
    return (3 * value + 1) // 2 if value % 2 else value // 2


def trajectory_to_one(start):
    states = [start]
    visited = {start}
    while states[-1] != 1:
        value = shortcut(states[-1])
        require(value not in visited, "unexpected repetition on finite test path")
        visited.add(value)
        states.append(value)
    return states


def reconstruct(end, marked_times, end_time):
    first = min(marked_times)
    marked = set(marked_times)
    value = end
    for clock in reversed(range(first, end_time)):
        if clock in marked:
            require((2 * value - 1) % 3 == 0, "legal odd inverse")
            value = (2 * value - 1) // 3
            require(value % 2 == 1, "odd reconstructed source")
        else:
            value *= 2
    return value


def audit_seed(seed, starts):
    ray = trajectory_to_one(seed)
    position = {value: i for i, value in enumerate(ray)}
    target = {value for value in ray if value % 2}
    observations = defaultdict(dict)
    labels_by_group = defaultdict(set)
    case_counts = dict(downstream=0, straddling=0, earlier=0)
    straddling_even = 0
    rows = 0
    radii = (1, 2, 4, 8)
    clocks = (0, 1, 2, 4, 7, 12, 20)
    max_clock = max(clocks)
    for x in starts:
        path = trajectory_to_one(x)
        t = next((i for i, q in enumerate(path) if q in target), None)
        if t is None or t == 0 or path[t] == seed or position[path[t]] + max_clock >= len(ray):
            continue
        # Only physically injective extensions of each entry are in the experiment.
        require(path[t:t + max_clock + 1] == ray[position[path[t]]:position[path[t]] + max_clock + 1],
                "shared injective ray segment")
        odd_times = [i for i in range(t) if path[i] % 2]
        for h, radius in itertools.product(clocks, radii):
            z = path[h]
            key = h, radius, z
            for offset, b in enumerate(reversed(odd_times[-radius:]), start=1):
                y = path[b]
                if b >= h:
                    case = "downstream"
                    encoding = (case, offset)
                    suffix = [q for q in path[h:t] if q % 2]
                    recovered = suffix[-offset]
                elif h < t:
                    case = "straddling"
                    subset = tuple(i for i in range(b, h) if path[i] % 2)
                    encoding = (case, subset)
                    recovered = reconstruct(z, subset, h)
                    if z % 2 == 0:
                        straddling_even += 1
                else:
                    case = "earlier"
                    ray_clock = position[z] - (h - t)
                    require(ray_clock >= 0, "entry exists before coalesced state")
                    entry = ray[ray_clock]
                    require(entry == path[t], "unique physical entry on chosen ray")
                    subset = tuple(i for i in range(b, t) if path[i] % 2)
                    encoding = (case, t, subset)
                    recovered = reconstruct(entry, subset, t)
                require(recovered == y, "encoded marker recovers actual odd source")
                previous = observations[key].setdefault(encoding, y)
                require(previous == y, "one encoding cannot represent different markers")
                labels_by_group[key].add(y)
                case_counts[case] += 1
                rows += 1
    for (h, radius, z), values in labels_by_group.items():
        del z
        max_codes = (h + 2) * sum(math.comb(h, l) for l in range(min(h, radius) + 1)) + radius
        require(len(values) <= max_codes, "entry fibre cardinality bound")
    require(all(case_counts.values()) and straddling_even > 0, "all physical clock configurations tested")
    return {"spine_seed": seed, "physical_spine_states": len(ray), "rows": rows,
            "group_count": len(observations), "largest_distinct_marker_fibre":
            max(map(len, labels_by_group.values())), "cases": case_counts,
            "straddling_at_even_state": straddling_even}


if __name__ == "__main__":
    require(5**200 < 2**275 * 3**120 and 3**24 < 2**39, "entropy upper bound")
    starts = tuple(range(1, 10000, 2)) + tuple(range(800001, 801001, 2))
    result = {"source_count_per_spine": len(starts),
              "finite_spines": [audit_seed(seed, starts) for seed in (27, 871, 6171, 837799)]}
    print(json.dumps(result, indent=2))
