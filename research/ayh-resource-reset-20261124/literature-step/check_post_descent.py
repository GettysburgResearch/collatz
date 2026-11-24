"""Bounded source-by-source replay of the two physical clocks in the transfer note."""

from collections import Counter
from functools import lru_cache
from math import log2, sqrt


def path(n, steps):
    values, counts = [n], [0]
    for _ in range(steps):
        is_odd = n % 2
        n = (3 * n + 1) // 2 if is_odd else n // 2
        counts.append(counts[-1] + is_odd)
        values.append(n)
    return values, counts


def census(j):
    scale = 81**j
    native = scale.bit_length() - 1
    h = int(0.5 * log2(scale) / log2(2 / sqrt(3)))
    b = int(0.5 * log2(scale))
    end = h + b

    @lru_cache(maxsize=2)
    def parent_history(m):
        val, count = path(m, end)
        return val, count, set(val[: native + 1]), set(val)

    profiles, loads = Counter(), Counter()
    missed_native = missed_end = escaped = 0
    for child in range(7 * scale, 8 * scale):
        parent, residue = divmod(child, 81)
        pv, pc, parent_native, parent_end = parent_history(parent)
        cv, cc = path(child, end)
        missed_native += parent_native.isdisjoint(cv[: native + 1])
        missed_end += parent_end.isdisjoint(cv)
        exp_gap = cc[h] + 4 - pc[h]
        if exp_gap >= 0:
            base, other, orientation = pv[h], cv[h], 0
        else:
            base, other, orientation = cv[h], pv[h], 1
        level = abs(exp_gap)
        off = other - 3**level * base
        profiles[(orientation, level, off)] += 1
        loads[(orientation, base)] += 1
        if residue == 0:
            # The physical endpoints of a higher lift have the claimed profile
            # even when the lift itself is far outside this head.
            lifted_parent = parent + 2**h
            lifted_child = 81 * lifted_parent
            lp = path(lifted_parent, h)[0][-1]
            lc = path(lifted_child, h)[0][-1]
            low, high = (lp, lc) if orientation == 0 else (lc, lp)
            if high != 3**level * low + off:
                raise ArithmeticError((j, child, level, off))
        escaped += max(
            abs((cc[h + i] - pc[h + i]) - (cc[h] - pc[h]))
            for i in range(b + 1)
        ) * 2 >= b
    return {
        "j": j, "children": scale, "native_clock": native,
        "restart_clock": h, "grid_depth": b,
        "missed_all_pairs_of_native_clocks": missed_native,
        "missed_all_pairs_of_extended_clocks": missed_end,
        "distinct_profiles": len(profiles),
        "max_arm_endpoint_multiplicity": max(loads.values()),
        "odd_difference_changed_by_at_least_half_block": escaped,
    }


if __name__ == "__main__":
    for level in (1, 2, 3):
        print(census(level))
