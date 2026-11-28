#!/usr/bin/env python3
"""Verify exact ternary leading-cell prices and the complete width-seven dual."""

from fractions import Fraction
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def forward_cycle(radius):
    minimum = 3 ** (2 * radius - 1)
    seen = {}
    orbit = []
    h = minimum
    while h not in seen:
        seen[h] = len(orbit)
        orbit.append(h)
        multiplier = 3 if h < 2 * minimum else 1
        h = multiplier * h // 2
    cycle = orbit[seen[h]:]
    decrements = sum(h < 2 * minimum for h in cycle)
    return minimum, seen[h], cycle, decrements


def verify_all_edges(minimum, cycle, decrements):
    cuts = sorted(cycle)
    rank = {h: sum(h >= cut for cut in cuts)
            for h in range(minimum, 3 * minimum)}
    period = len(cycle)
    edges = 0
    tight = 0
    for h in range(minimum, 3 * minimum):
        down = int(h < 2 * minimum)
        multiplier = 3 ** down
        first = multiplier * h // 2
        last = (multiplier * (h + 1) - 1) // 2
        for g in range(first, last + 1):
            for parity in (0, 1):
                length_change = parity - down
                drift = -period * length_change + rank[h] - rank[g]
                price = decrements - period * parity
                require(drift <= price, (h, g, parity, drift, price))
                edges += 1
                tight += drift == price
    return edges, tight


def main():
    expected = ["2/3", "7/11", "12/19", "171/271", "983/1558"]
    cases = []
    width_seven = {}
    for radius, value in enumerate(expected, 1):
        minimum, transient, cycle, decrements = forward_cycle(radius)
        period = len(cycle)
        fraction = Fraction(decrements, period)
        require(str(fraction) == value, (radius, fraction))
        require(3 ** decrements > 2 ** period, "critical comparison")
        cases.append({"width": 2 * radius + 1, "transient": transient,
                      "period": period, "decrements": decrements,
                      "price": value})
        if radius == 3:
            edges, tight = verify_all_edges(minimum, cycle, decrements)
            width_seven = {"minimum_mantissa": minimum, "cycle": cycle,
                           "sorted_dual_cuts": sorted(cycle),
                           "both_parity_edges": edges, "tight_edges": tight}
    print(json.dumps({"prices": cases, "width_seven": width_seven},
                     indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
