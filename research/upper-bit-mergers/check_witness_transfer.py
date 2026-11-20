"""Certify the four-generation inverse-tree weight used for witness transfer."""


SCALE = 1000
WEIGHTS = (866, 657, 497, 377, 285, 216, 164, 124, 94, 71, 54, 41, 31, 23, 17, 13, 10, 7)


def check_weights():
    # Each weight divided by SCALE is the truncation of
    # (3 / 2**(b + 11/10))**(2/5). Compare 25th powers as integers.
    target = SCALE**25 * 3**10
    for b, weight in enumerate(WEIGHTS, 1):
        denominator = 2**(10*b + 11)
        if not weight**25 * denominator <= target < (weight + 1)**25 * denominator:
            raise AssertionError(("incorrect edge weight", b, weight))


def minimum_block_weight():
    # At depth d, a starting residue modulo 3**(d+1) determines the
    # d inverse divisions and the final residue modulo three.
    row = [0, 1, 1]
    for depth in range(1, 5):
        modulus = 3**(depth + 1)
        next_row = [0] * modulus
        for start in range(modulus):
            if start % 3 == 0:
                continue
            for b, weight in enumerate(WEIGHTS, 1):
                numerator = ((2**b) * start - 1) % modulus
                if numerator % 9 in (3, 6):
                    next_row[start] += weight * row[numerator // 3]
        row = next_row
    return min(row[r] for r in range(len(row)) if r % 3)


if __name__ == "__main__":
    check_weights()
    minimum = minimum_block_weight()
    if minimum != 1_022_566_376_746 or minimum <= SCALE**4:
        raise AssertionError(("insufficient block mass", minimum))
    print(f"Four-step minimum mass is at least {minimum}/{SCALE**4} on all 162 ternary units")
