"""Exact replay on all primitive shortcut necklaces of length at most 12."""
from fractions import Fraction
from itertools import combinations, product
from math import gcd


def check():
    cycles = covers = mixed = empty = 0
    for period in range(2, 13):
        for word in product(range(2), repeat=period):
            rotations = [word[i:] + word[:i] for i in range(period)]
            if word != min(rotations) or len(set(rotations)) != period:
                continue
            odd = sum(word)
            delta = 2**period - 3**odd
            if delta <= 0 or not odd:
                continue
            carry = 0
            for i, bit in enumerate(word):
                if bit:
                    carry = 3 * carry + 2**i
            denominator = delta // gcd(delta, carry)
            cycles += 1
            for width in range(1, period // 2 + 1):
                groups = {}
                for i, rotation in enumerate(rotations):
                    groups.setdefault(rotation[:width], []).append(i)
                for prefix, indices in groups.items():
                    count = sum(prefix)
                    for k in range(2, min(len(indices), period // width) + 1):
                        for marks in combinations(indices, k):
                            gaps = [j-i for i,j in zip(marks, marks[1:] + (marks[0]+period,))]
                            if min(gaps) < width:
                                continue
                            ones = odd - k * count
                            zeros = period - k * width - ones
                            defect = max(2**zeros, Fraction(3, 2)**ones)
                            if denominator * k * 2**period * defect <= (k-1)*delta*2**count:
                                raise ArithmeticError((word, marks, width))
                            covers += 1
                            empty += min(gaps) == width
                            signs = [3**sum(rotations[i][:g]) > 2**g for i,g in zip(marks,gaps)]
                            mixed += any(signs) and not all(signs)
    return dict(cycles=cycles, covers=covers, mixed=mixed, with_empty_defect=empty)


if __name__ == '__main__':
    print(check())
