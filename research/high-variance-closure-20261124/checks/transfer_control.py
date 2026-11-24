"""Exact finite checks of the endpoint fractions and inverse-weight identity."""
from fractions import Fraction


def require(ok):
    if not ok:
        raise ValueError("transfer identity failed")


def step(x):
    return (3*x+1)//2 if x % 2 else x//2


def path(m, k):
    slope = Fraction(1)
    product_weight = Fraction(1, m)
    x = m
    word = []
    for _ in range(k):
        odd = x % 2
        word.append(odd)
        if odd:
            product_weight *= Fraction(3*x, 3*x+1)
        slope *= Fraction(3**odd, 2)
        x = step(x)
    require(slope / x == product_weight)
    return tuple(word), x


def check(k):
    total = Fraction(0)
    words = set()
    for t in range(1, 2**k+1):
        w, r = path(t, k)
        d = 3**sum(w)
        require(1 <= r <= d and w not in words)
        words.add(w)
        for h in (1, 2, 7):
            require(path(t + h * 2**k, k) == (w, r + h*d))
        total += Fraction(r, d) - Fraction(t, 2**k)
    require(len(words) == 2**k)
    require(total / 2**k == (Fraction(2, 3)**k - Fraction(1, 2)**k) / 2)


if __name__ == "__main__":
    for k in range(13):
        check(k)
    print("8191 parity words at clocks 0 through 12; three lifts per word; exact mean and product identities")
