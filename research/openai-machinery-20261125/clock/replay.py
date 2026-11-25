"""Exact finite rows for the PR 206 ordinary forward-clock crossing test."""

from math import comb
import argparse


def threshold(k):
    """Largest noncrossing elapsed clock at the kth odd return."""
    return (((k + 1) * 3 ** (6 * k)).bit_length() - 1) // 6


def survivor_counts(k):
    """Multiplicity for each clock after requiring all first k cuts to fail."""
    counts = [1]
    for i in range(1, k + 1):
        total = 0
        new = []
        for s in range(threshold(i) + 1):
            new.append(total)
            if s < len(counts):
                total += counts[s]
        counts = new
    return counts


def row(k):
    cut = threshold(k)
    counts = survivor_counts(k)
    survivors = sum(n << (cut - s) for s, n in enumerate(counts))
    last_only = sum(comb(s - 1, k - 1) << (cut - s) for s in range(k, cut + 1))
    return survivors, last_only, 1 << cut


def ordinary_tests(start, k):
    current = start
    elapsed = 0
    all_failed = True
    for i in range(1, k + 1):
        target = 3 * current + 1
        gap = (target & -target).bit_length() - 1
        elapsed += gap
        current = target >> gap
        last_failed = 2 ** (6 * elapsed) <= (i + 1) * 3 ** (6 * i)
        all_failed = all_failed and last_failed
    return all_failed, last_failed


def verify(k):
    alive, last, total = row(k)
    if not 0 < alive <= last <= total:
        raise ValueError(("row", k, alive, last, total))
    if k % 3 == 0:
        n = k // 3
        standard_row = 1 << (5 * n)
        if standard_row < total or 108 ** n * last * (standard_row // total) > 3125 ** n:
            raise ValueError(("pressure", k))
    witness = 3 * 2 ** (k + 1) - 1
    if witness % 3 != 2 or not ordinary_tests(witness, k)[0]:
        raise ValueError(("witness", k))
    return alive, last, total


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--depth", type=int, default=64)
    parser.add_argument("--direct", type=int, default=8,
                        help="exhaustively check full ordinary CRT rows through this depth")
    args = parser.parse_args()
    if args.depth < 1 or not 0 <= args.direct <= args.depth:
        parser.error("require depth >= 1 and 0 <= direct <= depth")
    print("k threshold all-fail kth-fail odd-row")
    for k in range(1, args.depth + 1):
        alive, last, total = verify(k)
        if k <= args.direct:
            # A full joint period contains exactly total odd starts of each residue mod 3.
            counts = [[0, 0] for _ in range(3)]
            for x in range(1, 6 * total, 2):
                all_failed, last_failed = ordinary_tests(x, k)
                counts[x % 3][0] += int(all_failed)
                counts[x % 3][1] += int(last_failed)
            if counts != [[alive, last]] * 3:
                raise ValueError(("ordinary CRT replay", k, counts, alive))
        if k <= args.direct or k in (16, 32, 64, args.depth):
            print(k, threshold(k), alive, last, total)


if __name__ == "__main__":
    main()
