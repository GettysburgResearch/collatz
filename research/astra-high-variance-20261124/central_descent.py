"""Exact finite controls for CENTRAL_DESCENT.md. No external dependencies."""
from fractions import Fraction
from itertools import product


def require(condition, message):
    if not condition:
        raise ValueError(message)


def error_bound(j):
    return (8 * Fraction(1, 8)**j / (1 - Fraction(1, 8))
            + 12 * Fraction(5, 32)**j / (1 - Fraction(5, 32))) / 3


def signed_edges():
    suffixes = []
    for bits in product((0, 1), repeat=4):
        carry = 0
        for index, odd in enumerate(bits):
            if odd:
                carry = 3 * carry + 2**index
        power = 3**sum(bits)
        if (29 + carry) % power == 0:
            suffixes.append(((29 + carry) // power, sum(bits)))
    require(suffixes == [(29, 0), (11, 1), (10, 1), (4, 2)], "terminal list")
    hits = []
    for start in range(1, 36):
        mag, clocks, odds = start, 0, 0
        seen = {}
        while mag not in seen:
            seen[mag] = (clocks, odds)
            for target, tail_odds in suffixes:
                if mag != target:
                    continue
                r2 = odds + tail_odds - 3
                if r2 % 2 == 0 and 3 * odds - 2 * clocks >= 7 - 3 * tail_odds:
                    hits.append((start, mag, r2 // 2))
            odds += mag % 2
            mag = (3 * mag - 1) // 2 if mag % 2 else mag // 2
            clocks += 1
        cyclic_targets = {target for target, _ in suffixes
                          if target in seen and seen[target][0] >= seen[mag][0]}
        if cyclic_targets:
            first_clocks, first_odds = seen[mag]
            require(cyclic_targets == {10} and clocks - first_clocks == 3
                    and odds - first_odds == 2, "unaccounted terminal cycle")
    require(hits == [(3, 4, 0)], f"unexpected shorter paths: {hits}")
    return hits


def main():
    for start in range(1, 256, 2):
        x = start
        seen = set()
        while x != 1:
            require(x not in seen, "small positive cycle")
            seen.add(x)
            x = (3*x + 1)//2 if x % 2 else x//2
    require(error_bound(2) == Fraction(247, 1512), "reciprocal constant")
    print("odd sources below 256 reach 1; E(2) =", error_bound(2))
    print("signed short-clock candidates (start, terminal magnitude, r):", signed_edges())


if __name__ == "__main__":
    main()
