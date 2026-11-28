"""Finite controls for the exact residue and binary-progression identities."""

from collections import Counter
from itertools import combinations


def require(condition, message):
    if not condition:
        raise ValueError(message)


def compositions(total, length):
    for cuts in combinations(range(1, total), length - 1):
        boundaries = (0, *cuts, total)
        yield tuple(b - a for a, b in zip(boundaries, boundaries[1:]))


def offset_mod(word, modulus):
    total = 0
    out = 0
    for i, gap in enumerate(word):
        total += gap
        out += pow(3, i, modulus) * pow(2, -total, modulus)
    return out % modulus


def physical_inverse(y, word):
    for gap in word:
        numerator = (y << gap) - 1
        if numerator % 3:
            return None
        y = numerator // 3
        require(y > 0 and y % 2 == 1, "integral inverse must be positive and odd")
    return y


def extra_trit_control():
    rows = 0
    for depth in range(1, 6):
        q = 3**depth
        for total in range(depth, 13):
            words = list(compositions(total, depth))
            for m in range(4):
                extra = 3**m
                modulus = q * extra
                offsets = Counter(offset_mod(w, modulus) for w in words)
                for y in range(1, 42, 2):
                    physical = Counter(
                        x % extra
                        for w in words
                        if (x := physical_inverse(y, w)) is not None
                    )
                    inverse_power = pow(2, -total, modulus)
                    modular = [
                        offsets[(y - q * inverse_power * digit) % modulus]
                        for digit in range(extra)
                    ]
                    require(
                        modular == [physical[digit] for digit in range(extra)],
                        f"physical trit row differs at depth={depth}, total={total}, m={m}, y={y}",
                    )
                    rows += 1
    return rows


def shortcut_path(x, depth):
    odds = []
    for j in range(depth):
        if x % 2:
            odds.append(j)
            x = (3 * x + 1) // 2
        else:
            x //= 2
    return x, tuple(odds)


def binary_progression_control():
    rows = 0
    for b in range(1, 9):
        modulus = 2**b
        seen = set()
        multiplicities = Counter()
        for w in range(modulus):
            x = modulus + w
            y, odd_positions = shortcut_path(x, b)
            require(odd_positions not in seen, f"repeated parity word for b={b}, w={w}")
            seen.add(odd_positions)
            d = len(odd_positions)
            q = 3**d
            offset_numerator = modulus * y - q * x
            require(
                0 <= offset_numerator < q * modulus,
                f"affine offset exceeds its bound for b={b}, w={w}",
            )
            root_residue = y % q
            multiplicities[d, root_residue] += 1
            if d:
                totals = sorted(b - i for i in odd_positions)
                word = tuple(v - u for u, v in zip((0, *totals), totals))
                require(
                    offset_mod(word, q) == root_residue,
                    f"reversed word reaches the wrong residue for b={b}, w={w}",
                )
            for m in range(4):
                extra = 3**m
                finer = {}
                for j in range(extra):
                    original = x + modulus * j
                    endpoint, positions = shortcut_path(original, b)
                    require(
                        positions == odd_positions and endpoint == y + q * j,
                        f"binary lift differs for b={b}, w={w}, j={j}",
                    )
                    finer[original % extra] = endpoint % (q * extra)
                require(len(finer) == extra, f"incomplete finer input for b={b}, w={w}, m={m}")
                require(
                    set(finer.values()) == {root_residue + q * i for i in range(extra)},
                    f"incomplete finer endpoint fibre for b={b}, w={w}, m={m}",
                )
                rows += 1
        require(len(seen) == modulus, f"incomplete binary parity partition for b={b}")
        for d in range(1, b + 1):
            q = 3**d
            raw = Counter()
            for total in range(d, b + 1):
                for word in compositions(total, d):
                    raw[offset_mod(word, q)] += 2 ** (b - total)
            for (odd_count, residue), count in multiplicities.items():
                if odd_count == d:
                    require(
                        count <= raw[residue],
                        f"multiplicity exceeds word mass for b={b}, d={d}, residue={residue}",
                    )
    return rows


if __name__ == "__main__":
    print(f"extra-ternary-digit rows checked: {extra_trit_control()}")
    print(f"binary-progression controls checked: {binary_progression_control()}")
