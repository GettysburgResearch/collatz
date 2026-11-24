"""Finite ordinary checks for paired profiles, rank trimming, and cycle anchors."""
from collections import defaultdict
import json


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def step(x):
    return (3 * x + 1) // 2 if x % 2 else x // 2


def trace(x, h):
    odds = 0
    for _ in range(h):
        odds += x % 2
        x = step(x)
    return odds, x


def first_below(x, threshold, limit):
    odds = 0
    for clock in range(limit + 1):
        if x <= threshold:
            return clock, odds, x
        odds += x % 2
        x = step(x)
    raise RuntimeError("finite clock limit exhausted")


def unit(x):
    return x > 0 and x % 2 and x % 3 != 0


def native_profiles():
    starts = classes = actual_partners = translations = 0
    largest = 0
    example = None
    for h in (8, 11, 14, 18):
        size = 2**h
        blocks = (1,) if h == 18 else (0, 1, 5, 2**32 + 13)
        for block in blocks:
            grouped = defaultdict(list)
            for x in range(block * size, (block + 1) * size):
                if not unit(x):
                    continue
                p, low = trace(x, h)
                pp, high = trace(3 * x, h)
                first = (3**p, low, size * low - 3**p * x)
                second = (3**(pp + 1), high, size * high - 3**(pp + 1) * x)
                (s, u, small_carry), (big, v, big_carry) = sorted((first, second))
                require(min(small_carry, big_carry) >= 0, "negative real carry")
                require(size * abs(big * u - s * v) <= big * max(small_carry, big_carry),
                        "two-arm strip failed")
                grouped[(p, low, pp, high, x % 3)].append((x, big, big_carry))
                starts += 1
            classes += len(grouped)
            for key, members in grouped.items():
                x0, big, _ = members[0]
                R_num = max(carry for _, _, carry in members)
                require(big * (members[-1][0] - x0) <= R_num, "source diameter failed")
                largest = max(largest, len(members))
                actual_partners += max(0, len(members) - 1)
                if len(members) >= 3:
                    for t in (3, 12):
                        y = members[-1][0]
                        require(trace(x0 + size*t, h) == trace(y + size*t, h),
                                "lower translate failed")
                        require(trace(3*(x0 + size*t), h) == trace(3*(y + size*t), h),
                                "upper translate failed")
                        translations += 1
                    if example is None and key[1] != key[3]:
                        example = [h, x0, members[1][0], members[2][0], list(key[:4])]
    require(example is not None, "missing distinct literal targets")
    return {"ordinary_unit_starts": starts, "exact_profiles": classes,
            "largest_class": largest, "additional_members": actual_partners,
            "paired_translations": translations, "sample_distinct_targets": example}


def stopped_profiles():
    h = 15
    start = 2**h
    cutoff = 64
    records = {}
    for x in range(start, 2 * start):
        if unit(x):
            t, p, y = first_below(x, cutoff, 1000)
            tt, pp, yy = first_below(3*x, cutoff, 1000)
            records[x] = (t, p, y, tt, pp, yy, x % 3)
    stats = {}
    for length in (128, 512, 2048, 8192, start):
        groups = defaultdict(list)
        for x, record in records.items():
            groups[((x - start) // length, record)].append(x)
        inside = erased = 0
        minimum = 1 if length < start else 2
        for (_, record), members in groups.items():
            t, p, y, tt, pp, yy, _ = record
            h_common = max(t, tt)
            before, after = trace(y, h_common-t), trace(yy, h_common-tt)
            for u in (members[0], members[-1]):
                require(trace(u, h_common) == (p + before[0], before[1]), "clock alignment")
                require(trace(3*u, h_common) == (pp+after[0], after[1]), "upper alignment")
            trimmed = members[minimum:len(members)-minimum] if len(members)>2*minimum else []
            for u in trimmed:
                require(members[minimum-1] < u < members[-minimum], "two strict orders")
            inside += len(trimmed)
            erased += len(members) - len(trimmed)
        require(erased <= 2 * minimum * len(groups), "rank exception bound")
        stats[length] = {"interval_profile_classes": len(groups),
                         "strict_partners_each_side": minimum, "remaining_sources": inside,
                         "erased": erased}
    require(stats[start]["remaining_sources"] > 0, "no multiple-partner records")
    return {"octave": [start, 2*start], "literal_stop_threshold": cutoff,
            "sources": len(records), "scales": stats}


def anchors():
    count = pairs = 0
    for r in range(1, 302, 2):
        if not unit(r):
            continue
        h = max(1, first_below(r, 2, 1000)[0], first_below(3*r, 2, 1000)[0])
        require(trace(r, h)[1] in (1, 2) and trace(3*r, h)[1] in (1, 2), "anchor phases")
        count += 1
        for j in (1, 2, 4):
            for odd in (1, 3, 11):
                q = r + 2**(h+2*j)*odd
                for _ in range(j):
                    delta = q-r
                    require(delta % 2**(h+2) == 0, "unavailable anchor move")
                    smaller = r + 3*(delta//4)
                    require(unit(smaller) and smaller < q, "anchor descent")
                    for a in (1, 3):
                        require(trace(a*q, h+2)[1] == trace(a*smaller, h)[1], "anchor merger")
                    q = smaller
                    pairs += 1
                require((q-r) % 2**(h+2) != 0, "extra anchor step")
    return {"cycle_anchors": count, "two_arm_contractions": pairs}


if __name__ == "__main__":
    print(json.dumps({"native": native_profiles(), "stopping": stopped_profiles(),
                      "anchors": anchors()}, indent=2))
