"""Exhaust the bounded-depth inverse comparison at a potential restricted minimum."""

from collections import defaultdict
from math import comb
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def restricted_residues(max_depth):
    powers = [3**i for i in range(max_depth + 2)]
    good = [{0}]
    states = [(0, 0, 0)]
    for depth in range(1, max_depth + 2):
        next_states = []
        for residue, terminal, previous_weight in states:
            for exponent in (1, 2):
                weight = previous_weight + exponent
                dyadic = 2**weight
                if dyadic <= powers[depth] or 30 * dyadic > 161 * powers[depth]:
                    continue
                increment = (pow(2, -exponent, 3) - terminal) * pow(2, -previous_weight, 3) % 3
                new_residue = residue + increment * powers[depth - 1]
                if depth >= 2 and new_residue % 9 != 1:
                    continue
                numerator = 2**exponent * (terminal + 2**previous_weight * increment) - 1
                require(numerator % 3 == 0, "nonintegral restricted predecessor")
                next_states.append((new_residue, numerator // 3, weight))
        states = next_states
        classes = {s for s, _, _ in states}
        require(len(classes) == len(states), "ambiguous restricted inverse word")
        good.append(classes)
    return good


def search(depth, viable, powers):
    max_weight = (2 * powers[depth]).bit_length() - 1
    q = powers[depth + 1]
    inverses = [pow(2, -w, q) for w in range(max_weight + 1)]
    hits = defaultdict(set)
    words = 0

    def visit(length, weight, carry):
        nonlocal words
        if length == depth:
            words += 1
            r = carry * inverses[weight] % q
            if 4 * 2**weight <= 3 * powers[depth] and r % powers[depth] in viable[depth]:
                hits["lower_interval"].add(r % powers[depth])
            if r in viable[depth + 1]:
                hits["smaller_multiple"].add(r)
            return
        remaining_after = depth - length - 1
        for exponent in range(1, max_weight - weight - remaining_after + 1):
            visit(length + 1, weight + exponent, (carry << exponent) + powers[length])

    visit(0, 0, 0)
    require(words == comb(max_weight, depth), "incomplete composition search")
    return words, hits


def main():
    last = 16
    viable = restricted_residues(last)
    powers = [3**i for i in range(last + 2)]
    rows = []
    for depth in range(1, last + 1):
        words, hits = search(depth, viable, powers)
        if depth < last:
            require(not any(hits.values()), "early coefficient witness")
        else:
            require(116582680 in hits["smaller_multiple"], "explicit class missing")
        rows.append({
            "depth": depth,
            "tested_compositions": words,
            "eligible_ternary_prefixes": len(viable[depth]),
            "smaller_interval_classes": len(hits["lower_interval"]),
            "smaller_multiple_classes": len(hits["smaller_multiple"]),
        })
    print(json.dumps({"protocol": "collatz-round9-critical-sieve-1", "rows": rows}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
