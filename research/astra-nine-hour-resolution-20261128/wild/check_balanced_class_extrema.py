from fractions import Fraction


def walk(n, t):
    q = 0
    for _ in range(t):
        odd = n % 2
        q += odd
        n = (3 * n + 1) // 2 if odd else n // 2
    return n, q


def check():
    cases = 0
    for n in range(1, 101):
        for t in range(1, 9):
            y, q = walk(n, t)
            lift = 1 if q == 0 else 2 * 3 ** (q - 1)
            real = Fraction((1 << t) * y, 3**q)
            u = (1 << lift) * n + ((1 << lift) - 1) * (real - n)
            assert u.denominator == 1
            assert (u.numerator - n) % (1 << t) == 0
            after, grade = walk(u.numerator, t)
            assert after == (1 << lift) * y and grade == q
            assert after >> lift == y
            cases += 1
    print(f"{cases} exact prefix lifts")


if __name__ == "__main__":
    check()
