"""Exact finite checks of the return equation, grouping and real differences."""

from fractions import Fraction


def valuation2(value):
    value = Fraction(value)
    def count(n):
        return (abs(n) & -abs(n)).bit_length() - 1
    return count(value.numerator) - count(value.denominator)


def orbit(start, steps):
    values = [start]
    odds = [0]
    for _ in range(steps):
        x = values[-1]
        e = x % 2
        values.append((3**e * x + e) // 2)
        odds.append(odds[-1] + e)
    return values, odds


def check_return(start, shift, length):
    xs, s = orbit(start, shift + length)
    y = xs[shift] - xs[0]
    terms = []
    for j in range(length):
        digit = xs[shift+j] % 2 - xs[j] % 2
        if digit:
            term = digit * Fraction((2*xs[j]+1)*2**j, 3**(s[shift+j+1]-s[shift]))
            assert valuation2(term) == j
            terms.append((j, term))
    residual = Fraction(y) + sum(value for _, value in terms)
    assert residual == Fraction(2**length, 3**(s[shift+length]-s[shift])) * (
        xs[shift+length] - xs[length])
    for i, (index, _) in enumerate(terms):
        for stop in range(i+1, min(i+4, len(terms))+1):
            assert valuation2(sum(value for _, value in terms[i:stop])) == index

    for l in range(0, length, 3):
        m = min(length, l+7)
        ml = Fraction(2**l, 3**s[l])
        mm = Fraction(2**m, 3**s[m])
        diff = mm*xs[m] - ml*xs[l]
        assert diff == sum((xs[j] % 2) * Fraction(2**j, 3**s[j+1]) for j in range(l, m))
        assert abs(diff/mm) <= (m-l)*Fraction(3, 2)**(m-l)
    return len(terms)


if __name__ == "__main__":
    hit_count = sum(check_return(x, q, 35) for x in range(1, 100) for q in range(1, 19))
    print(f"Verified 1782 return windows, including {hit_count} mismatch terms.")
