"""Exact finite certificate for the constant-phase inverse tree and affine-shadow list."""
from fractions import Fraction
import json

TABLE = {
     1: ((6,8), (6,8), (10,16)),
     4: ((6,12), (6,10), (6,10)),
     5: ((7,13), (7,11), (7,11)),
    10: ((6,8), (6,8), (6,8)),
    13: ((8,12), (6,8), (6,8)),
    14: ((11,15), (9,11), (9,11)),
    17: ((7,9), (7,9), (7,9)),
    22: ((10,14), (8,10), (8,10)),
    23: ((7,9), (9,13), (7,9)),
    26: ((7,13), (7,9), (9,11)),
}


def require(condition, detail):
    if not condition:
        raise ValueError(detail)


def check_table():
    total = 0
    for residue, row in TABLE.items():
        for lift_index, pair in enumerate(row):
            lift = residue + 27 * lift_index
            left, right = pair
            require(6 <= left < right <= 16 and left+right <= 26, pair)
            for child_carry in pair:
                numerator = (4 * pow(4, child_carry, 81) * lift - pow(2, -child_carry, 81)) % 81
                require(numerator % 3 == 0 and numerator//3 in TABLE, (lift, child_carry))
                total += 1
    return total


def replay_tree(max_depth):
    level = [(1, 0)]
    all_sources = {1}
    sampled_gaps = []
    sizes = []
    for depth in range(max_depth):
        next_level = []
        for parent, carry in level:
            lift = parent * pow(2, -carry, 81) % 81
            for child_carry in TABLE[lift % 27][lift // 27]:
                gap = 2 + 3*child_carry - carry
                numerator = 2**gap * parent - 1
                require(numerator % 3 == 0, (parent, gap))
                child = numerator // 3
                require(child % 2 == 1 and child >= 5*parent, child)
                require(3*child+1 == 2**gap*parent, child)
                require(Fraction(gap+1+carry, 3) == 1+child_carry, child)
                require(child * pow(2, -child_carry, 27) % 27 in TABLE, child)
                require(child not in all_sources, (depth, child))
                all_sources.add(child)
                sampled_gaps.append(gap)
                next_level.append((child, child_carry))
        level = next_level
        sizes.append(len(level))
    return dict(depth=max_depth, level_sizes=sizes, distinct_vertices=len(all_sources),
                min_sampled_gap=min(sampled_gaps), max_sampled_gap=max(sampled_gaps))


def affine_states():
    rows = []
    for left in (5,7):
        for right in (5,7,11,19):
            slope = Fraction(23*left + right, 166)
            offset = 7*slope - left
            require(7*slope-offset == left and 5*slope+23*offset == right, (left,right))
            rows.append([left,right,str(slope),str(offset)])
    return rows


if __name__ == "__main__":
    print(json.dumps(dict(certificate_choices=check_table(), replay=replay_tree(12),
                          same_clock_shadows=affine_states()), indent=2))
