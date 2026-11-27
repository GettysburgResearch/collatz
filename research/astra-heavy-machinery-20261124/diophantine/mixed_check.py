"""Compare the separated finite source-time shifts on ordinary integer witnesses."""
from fractions import Fraction


def test(condition, message):
    if not condition:
        raise ValueError(message)


def valuation(x):
    n = x.numerator
    test(n != 0 and x.denominator % 2 == 1, 'outside finite odd branch')
    return (abs(n) & -abs(n)).bit_length() - 1


def prefix(q, length):
    ans = []
    for _ in range(length):
        a = valuation(3 * q + 1)
        ans.append(a)
        q = Fraction(3 * q + 1, 2**a)
    return ans


def main():
    count = 0
    for J in range(1, 14):
        center = Fraction(2, 3)**J - 1
        for h in range(4):
            n_center = (center - 1) / 2 - h
            other = [(r, J if r > h else J - 1) for r in range(6) if r != h]
            expected = [prefix(center + 2 * (r - h), horizon) for r, horizon in other]
            max_clock = max(sum(gaps) for gaps in expected)
            for gap in range(max_clock + 5, max_clock + 10):
                target = gap + J - 2
                modulus = 2**(target + 1)
                near = n_center.numerator * pow(n_center.denominator, -1, modulus)
                n = (near + 2**target) % modulus + modulus
                test(prefix(2 * (n + h) + 1, J) == [1] * (J - 1) + [gap],
                     'chosen source does not separate')
                test([prefix(2 * (n + r) + 1, horizon) for r, horizon in other] == expected,
                     'competing row changed')
                count += 1
    print(f'{count} positive witnesses separate one time/source translate from five competitors')


if __name__ == '__main__':
    main()
