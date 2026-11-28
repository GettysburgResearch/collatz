"""Count exact adjacent-to-adjacent Collatz cylinders by even grade.

Each returned row (c,h,s):N means N ordinary skeletons, each with
length generating function z**c / (1-z)**h and terminal sign s.
"""

from collections import Counter
from functools import cache
from math import comb


def skeleton_counts(evens):
    limit = 3**evens

    @cache
    def continuations(a, b, determinant):
        if a == b == evens and abs(determinant) == limit:
            return {(0, 0, 1 if determinant > 0 else -1): 1}
        counts = Counter()
        for left in (0, 1):
            right = (left + determinant) % 2
            next_a = a + left
            next_b = b + right
            if max(next_a, next_b) > evens:
                continue
            if determinant == 0 and left == right == 0:
                # All repetitions of this one self-loop are marked by h.
                continue
            numerator = 3 * determinant + right * 3**next_b - left * 3**next_a
            if numerator % 2:
                raise ArithmeticError("incompatible centered parity pair")
            following = numerator // 2
            if abs(following) > limit:
                continue
            for (steps, sites, sign), count in continuations(
                next_a, next_b, following
            ).items():
                counts[steps + 1, sites + int(determinant == 0), sign] += count
        return dict(counts)

    return continuations(0, 0, 1)


def coefficients(rows, time):
    result = Counter()
    for (minimum, sites, sign), count in rows.items():
        extra = time - minimum
        if extra < 0:
            continue
        choices = comb(extra + sites - 1, sites - 1) if sites else int(extra == 0)
        result[sign] += count * choices
    return result


def native_counts(time):
    counts = Counter()
    for start in range(2**time):
        x, y = start, start + 1
        a = b = 0
        for _ in range(time):
            if x % 2:
                x = (3*x + 1) // 2
            else:
                a += 1
                x //= 2
            if y % 2:
                y = (3*y + 1) // 2
            else:
                b += 1
                y //= 2
        if a == b and abs(y - x) == 1:
            counts[a, y - x] += 1
    return counts


def native_word(start, time):
    bits = []
    value = start
    for _ in range(time):
        bit = value % 2
        bits.append(str(bit))
        value = (value * (1 + 2*bit) + bit) // 2
    return "".join(bits), value


def check_inverse_rows():
    cases = (
        (64, -1, 6, "001101", "011000"),
        (32, 1, 5, "00011", "01000"),
    )
    checks = 0
    for time in range(9, 121):
        modulus = 3**(time - 4)
        for factor, shift, power, left, right in cases:
            root = (-shift * pow(factor, -1, modulus)) % modulus
            for lift in (0, 1, 7):
                target = root + lift * modulus
                x = 2**(time - power) * ((factor*target + shift) // modulus) - 2
                length = time - 1 - len(left)
                words = ("0" + "1"*length + left, "1" + "1"*length + right)
                if x <= 0 or native_word(x, time) != (words[0], target + 1):
                    raise ArithmeticError((time, lift, x, target, "first arm"))
                if native_word(x + 1, time) != (words[1], target):
                    raise ArithmeticError((time, lift, x, target, "second arm"))
                checks += 1
    return checks


def main():
    tables = {e: skeleton_counts(e) for e in range(9)}
    checks = 0
    for time in range(16):
        literal = native_counts(time)
        for e, rows in tables.items():
            predicted = coefficients(rows, time)
            for sign in (-1, 1):
                if predicted[sign] != literal[e, sign]:
                    raise ArithmeticError((time, e, sign, predicted, literal))
                checks += 1
    print(f"verified {checks} signed coefficients against all 65535 native residues")
    print(f"verified {check_inverse_rows()} exact two-arm inverses through clock 120")
    for e, rows in tables.items():
        counts = Counter()
        for (_, sites, _), count in rows.items():
            counts[sites] += count
        print(f"e={e} compressed skeletons by number of free runs {sorted(counts.items())}")
        if e <= 4:
            print(f"  exact terms {sorted(rows.items())}")


if __name__ == "__main__":
    main()
