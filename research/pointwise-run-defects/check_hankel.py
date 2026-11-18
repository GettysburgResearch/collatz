"""Check finite recurrence, exponent and independent-divisor interfaces exactly."""

from fractions import Fraction


def determinant(rows):
    """Fraction-free elimination with row pivoting."""
    matrix = [row.copy() for row in rows]
    sign = 1
    previous = 1
    for i in range(len(matrix) - 1):
        pivot_row = next((j for j in range(i, len(matrix)) if matrix[j][i]), None)
        if pivot_row is None:
            return 0
        if pivot_row != i:
            matrix[i], matrix[pivot_row] = matrix[pivot_row], matrix[i]
            sign = -sign
        pivot = matrix[i][i]
        for row in matrix[i + 1:]:
            for j in range(i + 1, len(matrix)):
                numerator = pivot * row[j] - row[i] * matrix[i][j]
                quotient, remainder = divmod(numerator, previous)
                assert not remainder
                row[j] = quotient
        previous = pivot
    return sign * matrix[-1][-1]


def check_cyclotomic(q, channels, size):
    values = [11]
    for n in range(2 * size - 2):
        forcing = sum((i + 1) * (2 * i + 3) ** n for i in range(channels))
        values.append(2 * q ** n * values[-1] + forcing)
    hankel = determinant([values[i:i + size] for i in range(size)])
    assert hankel
    factors = {}
    divisor = 1
    for d in range(1, size + 1):
        factor = q ** d - 1
        for e, old_factor in factors.items():
            if d % e == 0:
                factor //= old_factor
        factors[d] = factor
        step = (channels + 2) * d
        order = sum((i + d) // step + i // step for i in range(size))
        divisor *= factor ** order
    assert divisor > 1 and hankel % divisor == 0


def check_forward_tail(channels):
    q = Fraction(27, 16)
    u = Fraction(9, 8)
    modes = [Fraction(3 ** i, 2 ** (2 * i)) for i in range(channels)]
    values = {0: Fraction(7, 5)}
    indices = range(-15, 18)
    for n in range(17):
        forcing = sum((i + 1) * v ** n for i, v in enumerate(modes))
        values[n + 1] = u * q ** n * values[n] + forcing
    for n in range(-1, -16, -1):
        forcing = sum((i + 1) * v ** n for i, v in enumerate(modes))
        values[n] = (values[n + 1] - forcing) / (u * q ** n)
    for r in range(1, 5):
        residuals = {
            n: values[n] - u ** r * q ** (r * n - r * (r + 1) // 2) * values[n - r]
            for n in indices if n - r in values
        }
        for t in range(r):
            for v in modes:
                residuals = {
                    n: value - v * q ** t * residuals[n - 1]
                    for n, value in residuals.items() if n - 1 in residuals
                }
        assert residuals and not any(residuals.values())


def main():
    for h in range(1, 5):
        split = Fraction(h, h + 1)
        integral = (split ** 2 / (2 * h) - (h + 1) * split ** 3 / (6 * h ** 2)
                    + (1 - split) / (2 * (h + 1)))
        old = Fraction(2 * h - 1, 6 * h ** 2)
        assert integral == Fraction(2 * h + 3, 6 * (h + 1) ** 2)
        assert integral - old == Fraction(1, 6 * h ** 2 * (h + 1) ** 2)
        check_forward_tail(h)
        for q in (3, 4, 5):
            for size in (10, 16):
                check_cyclotomic(q, h, size)
    assert 2 ** (65 * 688) > 3 ** (57 * 495) and 2 ** (65 * 43) < 3 ** (57 * 31)
    gamma_lower = sum(Fraction(1, (5 * m - 1) ** 2) + Fraction(1, (5 * m) ** 2)
                      for m in range(1, 11)) / 10
    new_cutoff = (Fraction(2, 3) - Fraction(9, 96) - gamma_lower) / (Fraction(2, 3) + Fraction(7, 54))
    assert new_cutoff < Fraction(701, 1000)
    assert 2 ** 10000 > 3 ** 6309 and 2 ** (10 * 688) < 3 ** (9 * 495)
    print("PASS 4 channel counts, 24 exact Hankel divisors, signed-index tails, threshold witnesses")


if __name__ == "__main__":
    main()
