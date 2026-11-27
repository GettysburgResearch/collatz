"""Finite ordinary first-entrance controls, independent of the Lean recurrence."""

import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def first_passage(x, floor):
    trace = [x]
    while trace[-1] >= floor:
        require(len(trace) <= 2000, "first-entrance deadline")
        n = trace[-1]
        trace.append((3 * n + 1) // 2 if n % 2 else n // 2)
    return trace


def audit(x, floor, count):
    trace = first_passage(x, floor)
    h = len(trace) - 1
    y = trace[-1]
    require(floor <= 2 * y < 2 * floor, "first landing outside half-band")
    prefixes = [0]
    for n in trace[:-1]:
        prefixes.append(prefixes[-1] + n % 2)
    odds = prefixes[-1]
    den = 2**h
    carry = den * y - 3**odds * x
    weights = []
    impulse_sum = 0
    for j in range(h):
        power = odds - prefixes[h - j]
        weight = 2 ** (h - j) * 3**power
        weights.append(weight)
        require(weight <= den, "record gate suffix multiplier")
        impulse_sum += (trace[h - j - 1] % 2) * weight
    require(impulse_sum == 2 * carry, "backward impulse expansion")
    for b in (8, 16, 32):
        if h < b:
            continue
        if any(2 * 3 ** (prefixes[s+b]-prefixes[s]) > 2**b
               for s in range(h-b+1)):
            continue
        require(all(2 * weights[j+b] <= weights[j] for j in range(h-b)),
                "block-to-suffix implication")
        require(0 <= carry <= b * den, "exact additive landing budget")
        count[str(b)] += 1
    return {"n": x, "clock": h, "odds": odds, "gate": y}


def main():
    counts = {"8": 0, "16": 0, "32": 0}
    starts = range(2**14, 2**14 + 2048)
    for x in starts:
        audit(x, 1024, counts)
    require(min(counts.values()) > 0, "missing nonvacuous block class")
    pair = [audit(x, 10**6, counts) for x in (3*10**9, 3*10**9+1)]
    require(pair[0]["gate"] != pair[1]["gate"] and
            abs(pair[0]["clock"] - pair[1]["clock"]) > 1,
            "adjacent-start control")
    # Generic exact boundary test. These finite labels exercise the
    # combinatorial descent only; they are not invariant Collatz colors.
    for depth in range(9):
        high = 13 * 81**depth
        marked = {13 * 81**i for i in range(depth+1)}
        current = high
        for generation in range(depth+1):
            require(current in marked and current-1 not in marked,
                    "missing split")
            child_edge = any((z in marked) != (z//81 in marked)
                             for z in (current-1, current))
            require(child_edge == (generation == depth), "wrong first edge")
            if not child_edge:
                require(current % 81 == 0, "nonboundary persisted")
            current //= 81
    print(json.dumps({"tested_starts": len(starts)+len(pair),
                      "base81_boundary_depths": list(range(9)),
                      "nonvacuous_block_certificates": counts,
                      "adjacent_start_control": pair}, sort_keys=True))


if __name__ == "__main__":
    main()
