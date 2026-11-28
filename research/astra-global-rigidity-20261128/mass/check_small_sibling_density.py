"""Exact finite identities for signed columns and protected odd-map climbs."""

from fractions import Fraction


def check(ok, label):
    if not ok:
        raise RuntimeError(label)


def odd_step(x):
    z = 3 * x + 1
    return z // (z & -z), (z & -z).bit_length() - 1


def make_row(previous, skip_first_one=False):
    old_modulus = len(previous)
    modulus = 3 * old_modulus
    period = 2 * old_modulus
    denominator = 2**period - 1
    result = []
    for a in range(modulus):
        scaled = Fraction()
        twopower = 1
        for e in range(1, period + 1):
            twopower = (2 * twopower) % modulus
            z = (twopower * a - 1) % modulus
            if z % 3:
                continue
            scaled += 3 * (2**(period - e)) * previous[z // 3]
        full = scaled / denominator
        if skip_first_one and (2 * a - 1) % 3 == 0:
            full -= Fraction(3, 2) * previous[((2 * a - 1) // 3) % old_modulus]
        result.append(full)
    return result


def verify_columns():
    rows = [[Fraction(1)]]
    marked = [[]]
    for depth in range(1, 6):
        rows.append(make_row(rows[-1]))
        marked.append(make_row(rows[-2], skip_first_one=True))
        check(marked[-1][-1] == rows[-1][-4 % 3**depth] / 4, 'negative root')
        check(all(value >= 0 for value in marked[-1]), 'positive column')
        for q in range(1, depth + 1):
            projection = sum(marked[-1][3**q - 1::3**q])
            check(projection == 3**(depth - q) * marked[q][-1], 'coarse projection')


    # Remove exactly the all-one outward prefix, at any depth at least s.
    for s in range(1, len(rows)):
        bypass = []
        for depth, row in enumerate(rows):
            new_row = []
            for a, total in enumerate(row):
                remainder = total
                if depth >= s:
                    previous = a
                    for _ in range(s):
                        if (2 * previous - 1) % 3:
                            break
                        previous = (2 * previous - 1) // 3
                    else:
                        z = previous % len(rows[depth - s])
                        remainder -= Fraction(3, 2)**s * rows[depth - s][z]
                check(remainder >= 0, 'nonnegative bypass')
                new_row.append(remainder)
            bypass.append(new_row)
            at_minus_one = row[-1]
            if depth >= s:
                at_minus_one -= Fraction(3, 2)**s * rows[depth - s][-1]
                residual_sum = sum(
                    Fraction(3, 2)**(depth - i) * rows[i][-4 % 3**i] / 4
                    for i in range(depth - s + 1, depth + 1)
                )
                check(residual_sum == at_minus_one, 'signed residual telescoping')
            check(new_row[-1] == at_minus_one, 'early or complete bypass')
            for r in range(s, depth + 1):
                projection = sum(new_row[3**r - 1::3**r])
                expected = 3**(depth - r) * bypass[r][-1]
                check(projection == expected, 'long bypass projection')


def verify_climbs():
    for s in range(1, 8):
        for k in range(1, 11):
            for u in (1, 2, 5, 17):
                x = 2**(s + 1) * 3**(k + 1) * u - 1
                z = 2**k * (x + 1) // 3**k - 1
                check(z % 2 == 1 and z % 3 != 0, 'unit before climb')
                for _ in range(k):
                    z, e = odd_step(z)
                    check(e == 1, 'small ancestor gap')
                check(z == x, 'small ancestor arrival')
                sibling = 16 * x + 5
                check(odd_step(sibling) == (odd_step(x)[0], 5), 'true unit sibling')
                for i in range(1, s + 1):
                    z, e = odd_step(z)
                    expected = 2**(s + 1 - i) * 3**(k + 1 + i) * u - 1
                    check(e == 1 and z == expected, 'prescribed climb')
                    check((2 * z - 1) // 3 < z, 'landing parent guard')


if __name__ == '__main__':
    verify_columns()
    verify_climbs()
    print('Exact signed columns and bypass prefixes through depth 5; 280 ordinary climbs passed')
