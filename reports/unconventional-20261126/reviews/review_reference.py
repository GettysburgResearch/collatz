"""Independent odd-gap enumeration of the all-clock reference enclosure.

This uses a gap tree, a low-bit trie, and direct forward clocks.  It does
not import the primary reverse-shortcut or residue-union implementation.
"""
from fractions import Fraction
import json


def require(test, message):
    if not test:
        raise ArithmeticError(message)


def gap_tree(depth):
    pending = [(1, 0)]
    leaves = []
    unit_nodes = 0
    while pending:
        target, used = pending.pop()
        unit_nodes += 1
        for gap in range(1, depth - used + 1):
            numerator = (target << gap) - 1
            if numerator % 3:
                continue
            source = numerator // 3
            if source == 1:
                continue
            require(source > 1 and source % 2 == 1, "Invalid odd inverse")
            clock = used + gap
            if source % 3 == 0:
                leaves.append((clock, source // 3))
            else:
                pending.append((source, clock))
    return leaves, unit_nodes


def clock_to_one(source, limit):
    for clock in range(limit + 1):
        if source == 1:
            return clock
        source = (source >> 1) if not source & 1 else (3 * source + 1) >> 1
    return None


def disjoint_cylinder_mass(cylinders):
    # A trie reads bits from the low end.  A marked node contains every
    # continuation, so no enumeration modulo the common denominator occurs.
    root = {}
    mass = Fraction()
    count = 0
    for bits, center in sorted(cylinders):
        node = root
        for i in range(bits):
            if "covered" in node:
                break
            node = node.setdefault((center >> i) & 1, {})
        else:
            if "covered" not in node:
                require(not node, "Shorter cylinder was inserted too late")
                node["covered"] = True
                mass += Fraction(1, 1 << (bits - 1))  # relative to odds
                count += 1
    return count, mass


def run():
    depth = 40
    leaves, live = gap_tree(depth)
    require((len(leaves), live) == (22289, 44474), "Tree counts differ")
    require(len({source for _, source in leaves}) == len(leaves), "Duplicate leaf")
    expected = {
        (False, 0): (13483, Fraction(3403055273, 34359738368)),
        (False, 1): (19783, Fraction(27668375859, 549755813888)),
        (False, 2): (20396, Fraction(27669397633, 1099511627776)),
        (True, 0): (4949, Fraction(36441516717, 549755813888)),
        (True, 1): (5817, Fraction(36448539097, 1099511627776)),
        (True, 2): (5862, Fraction(18224273713, 1099511627776)),
    }
    lower_clocks = {}
    for first, source in leaves:
        require(clock_to_one(3 * source, first) == first, "Wrong first clock")
        lower_clocks[source] = clock_to_one(source, depth)
    pending = sum(value is None for value in lower_clocks.values())
    require(pending == 16259, "Pending lower clocks differ")
    rows = []
    for both in (False, True):
        for reserve in (0, 1, 2):
            cylinders = []
            for first, source in leaves:
                lower = lower_clocks[source] if both else 0
                if lower is not None:
                    cylinders.append((max(first, lower) + reserve, source))
            count, mass = disjoint_cylinder_mass(cylinders)
            require((count, mass) == expected[both, reserve], "Cylinder union differs")
            error = Fraction(2 * live + (pending if both else 0),
                             1 << (depth + reserve))
            rows.append({"both": both, "reserve": reserve, "cylinders": count,
                         "lower": str(mass), "upper": str(mass + error)})
    # This finite sequence checks the exact symbolic progression and its
    # boundary valuation, independently of the larger primary examples.
    family = []
    for exponent in range(12, 211, 18):
        source, remainder = divmod((1 << exponent) - 19, 27)
        require(remainder == 0 and source & 1, "Wrong source progression")
        require(clock_to_one(source, exponent) == exponent, "Wrong lower arrival")
        require(clock_to_one(3 * source, exponent) == exponent, "Wrong upper arrival")
        if exponent >= 30:
            previous = ((1 << (exponent - 18)) - 19) // 27
            difference = source - previous
            require((difference & -difference).bit_length() - 1 == exponent - 18,
                    "Wrong sharp reserve")
        family.append(exponent)
    return {"independent_gap_tree_leaves": len(leaves), "live_prefixes": live,
            "pending_lower_clocks": pending, "exact_enclosures": rows,
            "family_exponents": family,
            "scope": "finite certificate replay; all-depth density inference is written"}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
