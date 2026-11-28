"""Exact finite controls for ordered pair sums and their punctured carry code."""

from collections import defaultdict
from itertools import combinations_with_replacement
import json
from math import gcd


def require(condition, description):
    if not condition:
        raise ArithmeticError(description)


def native_columns(floor):
    n = 2
    while 3 ** (n - 2) < 8 * floor:
        n += 1
    clock = [(t + 1) * 84 // 53 - t * 84 // 53 for t in range(n)]
    require(2 ** sum(clock) > 4 * floor, "source modulus")
    columns = []
    for start in range(floor, 2 * floor):
        states = [start]
        for b in clock:
            z = states[-1]
            c = z & -z
            if c > 2:
                break
            successor, remainder = divmod(3 * z + c, 2**b)
            tag = successor & -successor
            if remainder or tag > 2 or 2**b * tag < 2 * c:
                break
            x = z // c
            x_next = successor // tag
            native_power = (2**b * tag) // c
            require((3 * x + 1) // native_power == x_next and
                    (3 * x + 1) % native_power == 0 and x_next % 2 == 1,
                    "odd integer edge")
            states.append(successor)
        else:
            columns.append(states)
    return clock, columns


def integer_fixture(floor):
    clock, columns = native_columns(floor)
    n = len(clock)
    require(len(columns) >= 8, "parallel integer paths")
    pairs = list(combinations_with_replacement(range(len(columns)), 2))
    splits = 0
    for t, b in enumerate(clock):
        step = defaultdict(set)
        for i, j in pairs:
            x, y = columns[i][t], columns[j][t]
            current = x + y
            future = columns[i][t + 1] + columns[j][t + 1]
            require(2**b * future == 3 * current + (x & -x) + (y & -y),
                    "integer pair trace")
            step[current].add(future)
        previous_max = -1
        for current in sorted(step):
            require(previous_max < min(step[current]), "strict pair order")
            previous_max = max(step[current])
            splits += len(step[current]) - 1

    # Condition two rows, yielding genuinely forced positions to puncture.
    clipped = defaultdict(list)
    for col in columns:
        clipped[(col[0] & 1, col[-2] & 1)].append(col)
    family = max(clipped.values(), key=len)
    selected = []
    sums = set()
    for col in family:
        new = {2 * col[0], *(col[0] + v[0] for v in selected)}
        if sums.isdisjoint(new):
            selected.append(col)
            sums.update(new)
    bits = [[(z & -z) - 1 for z in col[:-1]] for col in selected]
    retained = [t for t in range(n) if len({w[t] for w in bits}) > 1]
    require(len(retained) <= n - 2 and len(selected) >= 2, "punctured code")
    words = [tuple(w[t] for t in retained) for w in bits]
    patterns = {}
    for i, j in combinations_with_replacement(range(len(words)), 2):
        total = tuple(a + b for a, b in zip(words[i], words[j]))
        require(total not in patterns, "binary B2 including doubled sources")
        patterns[total] = i, j

    # Without the spatial Sidon selection, integer aggregate collisions still
    # imply equality of the initial integer pair sums by exact divisibility.
    aggregate = {}
    collision_pairs = 0
    for i, j in pairs:
        row = tuple((x & -x) + (y & -y)
                    for x, y in zip(columns[i][:-1], columns[j][:-1]))
        val = columns[i][0] + columns[j][0]
        if row in aggregate:
            require(aggregate[row] == val, "aggregate-to-source injection")
            collision_pairs += 1
        aggregate[row] = val
    return dict(floor=floor, edges=n, columns=len(columns), pairs=len(pairs),
                strict_comparison_dates=n, equal_source_splits=splits,
                equal_aggregate_repetitions=collision_pairs,
                sidon_columns=len(selected), retained_positions=len(retained),
                distinct_binary_pair_sums=len(patterns))


def signed_rational_control():
    # Full genuinely rational cycle; common two-grade calendar, all ranks.
    exponents = [1, 2, 1, 2, 2, 2, 2]
    p, A = len(exponents), sum(exponents)
    y, q = 4663, 1909
    numerators = []
    for a in exponents:
        require(y % 2 == 1 and gcd(y, q) == 1, "reduced rational state")
        numerators.append(y)
        y, rem = divmod(3 * y + q, 2**a)
        require(rem == 0, "rational odd edge")
    require(y == numerators[0] and len(set(numerators)) == p, "primitive return")
    four_floor = 4 * min(numerators) + max(2 * min(numerators), max(numerators))
    chart = sorted((2 * y, 2) if 4 * y < four_floor else (y, 1)
                   for y in numerators)
    z, c = map(list, zip(*chart))
    z += [2 * v for v in z]
    c += [2 * v for v in c]
    height = [2 * z[r + 1] - z[r] - z[r + 2] for r in range(p)]
    for r in range(p):
        rr, b = (r + A) % p, (r + A) // p
        require((z[rr] << b) == 3 * z[r] + q * c[r], "rational rank winding")
        require(max(c[r:r + 3]) <= 2, "unwrapped two grades")
        d = 2 * c[r + 1] - c[r] - c[r + 2]
        require((height[rr] << b) == 3 * height[r] + q * d, "rational stencil")
    require(min(height) < 0 < max(height), "genuine rational sign change")
    return dict(period=p, A=A, denominator=q, odd_numerators=numerators,
                four_times_fold_floor_numerator=four_floor, signed_heights=height)


if __name__ == "__main__":
    samples = [integer_fixture(L) for L in (4096, 16384, 65536, 262144)]
    require(sum(s["equal_source_splits"] for s in samples) > 0,
            "finite integer equal source sums can split")
    require(sum(s["equal_aggregate_repetitions"] for s in samples) > 0,
            "exact coding boundary before Sidon selection")
    print(json.dumps(dict(integer_paths=samples, rational=signed_rational_control()),
                     indent=2))
