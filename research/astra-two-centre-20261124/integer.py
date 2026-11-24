"""Exact replay of separated odd orbits and residue counting on finite examples."""

from math import comb


def odd_step(x):
    z = 3 * x + 1
    shift = (z & -z).bit_length() - 1
    return z >> shift, shift


def mixed_ball(depth):
    power = 3**depth
    binary_modulus = 1 << depth
    center = power * (-pow(power, -1, binary_modulus) % binary_modulus)
    frontier = {center}
    visited = {center}
    for step in range(1, depth + 1):
        upcoming = set()
        for x in frontier:
            upcoming.add(x // 2 if x % 2 == 0 else (3 * x + 1) // 2)
            upcoming.add(2 * x)
            if x % 3 == 2:
                upcoming.add((2 * x - 1) // 3)
        frontier = upcoming - visited
        visited.update(frontier)
        if min(visited) < center:
            raise ValueError(f"graph decrease from {center} by step {step}")
    return center, len(visited)


def replay():
    blocks = 0
    checkpoints = 0
    for t in range(3, 9):
        period = 1 << (t - 2)
        modulus = 1 << t
        for u in (1, 3, 5, 7, 9, 31):
            residues = {u * pow(3, j, modulus) % modulus for j in range(period)}
            if len(residues) != period:
                raise ValueError("incorrect period")
            for b in (1, 7, 27, 703):
                d = b.bit_length() + 2 * period
                x = b + (u << d)
                y = b
                divisions = 0
                weights = []
                for j in range(period):
                    tail = u * 3**j
                    if x != y + (tail << (d - divisions)):
                        raise ValueError("separated-state identity failed")
                    if x.bit_count() != y.bit_count() + tail.bit_count():
                        raise ValueError("digit additivity failed")
                    weights.append(x.bit_count())
                    x, _ = odd_step(x)
                    y, shift = odd_step(y)
                    divisions += shift
                for k in range(t + 1):
                    if sum(w <= k for w in weights) > sum(comb(t, i) for i in range(k + 1)):
                        raise ValueError("density bound failed")
                blocks += 1
                checkpoints += period
    for depth in (8, 12, 16, 20):
        center, vertices = mixed_ball(depth)
        print(f"radius {depth}, ordinary center {center}, {vertices} distinct vertices, center minimal")
    print(f"{blocks} separated blocks, {checkpoints} ordinary odd checkpoints")


if __name__ == "__main__":
    replay()
