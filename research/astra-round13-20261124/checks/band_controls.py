"""Ordinary synchronized first-merger and exact defect checks."""
import json
from fractions import Fraction


def step(n):
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def orbit(n, t):
    for _ in range(t):
        n = step(n)
    return n


def accepts(b, budget):
    for depth in range(budget + 1):
        if b % 4 == 2:
            return True
        if depth == budget:
            return False
        if b % 2:
            b = 3 * (b // 2) + 2
        elif b % 64 == 56:
            b = 9 * (b // 64) + 8
        else:
            return False


def marked(n):
    d = n.bit_length() - 1
    return n > 0 and n % 2 == 1 and (d+1)*(n-2**d) <= 70*2**d


def check():
    checked = 0
    largest_source = 0
    for k in (0, 1, 2, 7, 31, 97):
        for depth in range(8):
            modulus = 2 ** (6 * depth + 2)
            target = 2 * 64**depth + 63
            base = (target * pow(55 * 3**k, -1, modulus)) % modulus
            for index in (0, 1, 11):
                u = base + index * modulus
                source = 2 ** (k + 1) * u - 1
                partner = 2**k * u - 1
                b = 3**k * u - 1
                first, second = b, 3*b+2
                if source != 2*partner+1 or min(partner, u) <= 0:
                    raise ValueError("invalid arm")
                if orbit(partner, k) != b or orbit(source, k+1) != second:
                    raise ValueError("missing prefix")
                defect = 55*b - 8
                if (defect // 64**depth) % 4 != 2 or defect % 64**depth:
                    raise ValueError("wrong defect")
                for clock in range(6*depth+2):
                    if first == second:
                        raise ValueError("premature synchronous merger")
                    if clock % 6 == 0 and clock < 6*depth:
                        if (min(first, second) % 64 != 56 or max(first, second) != 3*min(first, second)+2):
                            raise ValueError("missing return")
                    first, second = step(first), step(second)
                if first != second:
                    raise ValueError("terminal merger missing")
                largest_source = max(source, largest_source)
                checked += 1
    finite_densities = []
    for r in range(3):
        modulus = 2 ** (6*r+2)
        count = sum(accepts(b, r) for b in range(modulus))
        observed = Fraction(count, modulus)
        expected = sum(Fraction(1, 4)*Fraction(33, 64)**i for i in range(r+1))
        if observed != expected:
            raise ValueError("mixed script cylinder count")
        finite_densities.append(str(observed))
    for k in range(11, 100, 8):
        n = 2**(2*k+1) + 2**k - 1
        b = 3**(k-1)*(2**(k+1)+1)-1
        if not marked(n) or n%3 or accepts(b, 3):
            raise ValueError("uncovered marked family")
    for k in (0,1,7):
        L = 3
        modulus = 2**(6*L+2)
        u = (63+2*64**L)*pow(55*3**k,-1,modulus) % modulus + 2**80
        n = 2**(k+1)*u-1
        x = (n-1)//2
        y = x//(x & -x)
        if not (marked(n) and marked(y) and y<n and accepts(3**k*u-1,L)):
            raise ValueError("marked induction transport")
    print(json.dumps(dict(verified_sources=checked, max_source=str(largest_source),
                          max_rising_clock=98, max_return_depth=7,
                          mixed_script_densities=finite_densities)))


if __name__ == "__main__":
    check()
