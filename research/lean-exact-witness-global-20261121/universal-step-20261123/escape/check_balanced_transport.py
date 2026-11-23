#!/usr/bin/env python3
"""Finite exact checks for the ordinary balanced inverse-tree compiler.

This is not an all-orbit Collatz verifier. Infinite theorems have written
proofs in the adjacent notes. All guards remain active under python -O.
"""
from fractions import Fraction
from itertools import product
import copy
import json

TABLE = {1: {1: 2, 2: 4}, 2: {1: 1, 2: 3}, 4: {1: 6, 2: 2},
         5: {1: 3, 2: 5}, 7: {1: 4, 2: 6}, 8: {1: 5, 2: 1}}


def require(test, message):
    if not test:
        raise ValueError(message)


def validate_table(table):
    require(set(table) == {1, 2, 4, 5, 7, 8}, "unit rows")
    require(pow(2, 6, 9) == 1, "sixth power")
    require(len({pow(2, e, 9) for e in range(1, 7)}) == 6, "full order")
    for residue, row in table.items():
        require(set(row) == {1, 2}, "colours")
        for colour, exponent in row.items():
            require(type(exponent) is int and 1 <= exponent <= 6, "canonical exponent")
            good = [e for e in range(1, 7)
                    if (pow(2, e, 9) * residue) % 9 == 3 * colour + 1]
            require(good == [exponent], "unique colour exponent")
    return 12


def descend(root, address, table=TABLE):
    require(root > 0 and root % 2 == 1 and root % 3 != 0, "ordinary root")
    values, exponents = [root], []
    for colour, quotient in address:
        require(colour in (1, 2) and quotient >= 0, "address")
        exponent = table[values[-1] % 9][colour] + 6 * quotient
        numerator = (1 << exponent) * values[-1] - 1
        require(numerator % 3 == 0, "integer parent")
        parent = numerator // 3
        require(parent > 0 and parent % 2 == 1 and parent % 3 == colour, "ordinary coloured parent")
        require(3 * parent + 1 == (1 << exponent) * values[-1], "exact forward edge")
        require(((3 * parent + 1) >> exponent) % 2 == 1, "exact valuation")
        values.append(parent)
        exponents.append(exponent)
    return values, exponents


def recover(root, exponents, table=TABLE):
    address, q = [], root
    for exponent in exponents:
        parent = ((1 << exponent) * q - 1) // 3
        colour = parent % 3
        delta = exponent - table[q % 9][colour]
        require(delta >= 0 and delta % 6 == 0, "unique quotient recovery")
        address.append((colour, delta // 6))
        q = parent
    return tuple(address)


def main():
    entries = validate_table(TABLE)
    rejected = 0
    mutations = []
    wrong_colour = copy.deepcopy(TABLE)
    wrong_colour[1][1], wrong_colour[1][2] = wrong_colour[1][2], wrong_colour[1][1]
    mutations.append(wrong_colour)
    noncanonical = copy.deepcopy(TABLE)
    noncanonical[2][1] += 6
    mutations.append(noncanonical)
    wrong_branch = copy.deepcopy(TABLE)
    wrong_branch[7][2] = 1
    mutations.append(wrong_branch)
    for damaged in mutations:
        try:
            validate_table(damaged)
        except ValueError:
            rejected += 1
        else:
            raise ValueError("damaged table accepted")

    branch_alphabet = list(product((1, 2), range(3)))
    roots = (1, 5, 7, 11, 13, 17)
    cases, positive_costs, negative_costs, zero_costs = 0, 0, 0, 0
    for root in roots:
        sibling = 64 * root + 21
        for depth in range(4):
            source_vertices, target_vertices = set(), set()
            source_total = Fraction(0)
            target_total = Fraction(0)
            for address in product(branch_alphabet, repeat=depth):
                values, exponents = descend(root, address)
                paired, paired_exponents = descend(sibling, address)
                require(recover(root, exponents) == address, "source address recovery")
                require(recover(sibling, paired_exponents) == address, "target address recovery")
                require(values[-1] not in source_vertices, "source vertex injectivity at fixed depth")
                require(paired[-1] not in target_vertices, "target vertex injectivity at fixed depth")
                source_vertices.add(values[-1])
                target_vertices.add(paired[-1])
                shifts = [b - a for a, b in zip(exponents, paired_exponents)]
                require(all(d in (-4, -2, 0, 2, 4) for d in shifts), "per-edge shift")
                delta = sum(shifts)
                require(-4 * depth <= delta <= 4 * depth, "depth budget")
                cost = Fraction(2) ** delta
                physical = Fraction(root, sibling) * Fraction(paired[-1], values[-1])
                for a, b in zip(values[1:], paired[1:]):
                    physical *= Fraction(3 * a, 3 * a + 1) / Fraction(3 * b, 3 * b + 1)
                require(cost == physical, "exact physical cocycle")
                source_weight = Fraction(3 ** depth, 2 ** sum(exponents)) ** 2
                target_weight = Fraction(3 ** depth, 2 ** sum(paired_exponents)) ** 2
                require(target_weight == source_weight * Fraction(2) ** (-2 * delta), "exact pressure cost")
                source_total += source_weight
                target_total += target_weight
                positive_costs += delta > 0
                negative_costs += delta < 0
                zero_costs += delta == 0
                cases += 1
            require(source_total * Fraction(2) ** (-8 * depth) <= target_total,
                    "truncated lower comparison")
            require(target_total <= source_total * Fraction(2) ** (8 * depth),
                    "truncated upper comparison")
    require(positive_costs > 0 and negative_costs > 0, "both cost signs witnessed")
    print(json.dumps({
        "status": "PASS", "scope": "finite table and address controls only; not Collatz",
        "exhaustive_residue_colour_entries": entries,
        "damaged_tables_rejected": rejected,
        "ordinary_root_pairs": len(roots),
        "address_quotients": [0, 1, 2], "maximum_depth": 3,
        "paired_paths": cases,
        "positive_total_costs": positive_costs,
        "negative_total_costs": negative_costs,
        "zero_total_costs": zero_costs,
        "checks": ["unique base exponents", "actual integer branches", "exact valuations",
                   "reversible addresses", "fixed-depth vertex injectivity", "signed cost budget",
                   "exact rational height cocycle", "exact pressure cost", "truncated weight comparison"]
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
