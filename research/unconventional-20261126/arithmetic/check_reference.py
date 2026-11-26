"""Exact bounds for the ordinary positive first-one reference cylinders."""
import json
from fractions import Fraction


def step(x):
    return x // 2 if x % 2 == 0 else (3 * x + 1) // 2


def first_one(x, deadline):
    for h in range(deadline + 1):
        if x == 1:
            return h
        x = step(x)
    return None


def first_triple_leaves(deadline):
    live = [1]
    leaves = []
    for h in range(1, deadline + 1):
        following = []
        for y in live:
            following.append(2 * y)
            if y % 3 != 2:
                continue
            z = (2 * y - 1) // 3
            if z == 1:
                continue
            if z % 3 == 0:
                leaves.append((h, z // 3))
            else:
                following.append(z)
        live = following
    return leaves, len(live)


def fraction_data(p):
    return {"numerator": p.numerator, "denominator": p.denominator,
            "decimal": f"{float(p):.10f}"}


def cylinder_bounds(leaves, live, deadline, s, both):
    eligible = []
    undecided = 0
    for h, m in leaves:
        j = first_one(m, deadline) if both else 0
        if j is None:
            undecided += 1
            continue
        eligible.append((max(h, j) + s, m))
    occupied = [set() for _ in range(deadline + s + 1)]
    bits = 0
    for h, m in sorted(eligible):
        if any((m % (1 << j)) in occupied[j] for j in range(1, h + 1)):
            continue
        occupied[h].add(m % (1 << h))
        bits += 1 << (deadline + s - h)
    lower = Fraction(bits, 1 << (deadline + s - 1))
    remainder = Fraction(2 * live + undecided, 1 << (deadline + s))
    return {"both_arms": both, "reserve": s, "certified_cylinders": sum(map(len, occupied)),
            "pending_lower_first_hits": undecided,
            "relative_density_lower": fraction_data(lower),
            "relative_density_upper": fraction_data(lower + remainder)}


def main():
    d = 40
    leaves, live = first_triple_leaves(d)
    if len({m for _, m in leaves}) != len(leaves):
        raise ValueError("A first-hit triple has two depths")
    for h, m in leaves:
        if first_one(3 * m, h) != h:
            raise ValueError("Incorrect triple first-hit code")
    rows = []
    for n in (12, 30, 48, 66, 102, 192, 408, 1038, 1812):
        q, r = divmod(2**n - 19, 27)
        if r:
            raise ValueError("Incorrect source progression")
        for a, expected in ((q, [0, 1, 2]), (3 * q, [0, 4])):
            clock = 0
            dates = []
            while a != 1:
                if a % 2:
                    dates.append(clock)
                a = step(a)
                clock += 1
            if (clock, dates) != (n, expected):
                raise ValueError("Incorrect terminal dates")
        if n >= 30:
            previous = (2**(n - 18) - 19) // 27
            diff = q - previous
            if (diff & -diff).bit_length() - 1 != n - 18:
                raise ValueError("Previous source has incorrect common-prefix length")
        rows.append(n)
    report = {
        "depth": d, "first_hit_triple_leaves": len(leaves), "surviving_reverse_prefixes": live,
        "weighted_leaf_mass_lower": fraction_data(sum((Fraction(1, 1 << h) for h, _ in leaves), Fraction())),
        "weighted_leaf_mass_error_at_most": fraction_data(Fraction(live, 1 << d)),
        "relative_to_positive_odd_sources": [
            cylinder_bounds(leaves, live, d, s, both)
            for both in (False, True) for s in (0, 1, 2)],
        "delayed_merger_dates_and_sharp_margin_checked": rows,
    }
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
