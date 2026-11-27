"""Direct exact replays for the weighted identities, cycles, and the convergent family."""
from fractions import Fraction
from itertools import product


def require(condition, message):
    if not condition:
        raise ValueError(message)


def step(x, d):
    total = 3 * x + d
    a = (total & -total).bit_length() - 1
    return total >> a, a


def finite_orbits():
    for d in (1, 3, 5, 7, 9):
        for x0 in range(1, 100, 2):
            x, f, correction = x0, 1, Fraction(x0)
            for j in range(40):
                y, a = step(x, d)
                next_f = f << (a - 1)
                require(2 * next_f * y == 3 * f * x + d * f, 'weighted step')
                require(Fraction(2, 3)**j * f * x == correction, 'product identity')
                correction *= 1 + Fraction(d, 3 * x)
                x, f = y, next_f


def cycle_denominators():
    count = 0
    for p in range(1, 6):
        for word in product(range(1, 5), repeat=p):
            prefix = [0]
            for a in word:
                prefix.append(prefix[-1] + a)
            full = 2**prefix[-1] - 3**p
            carry = sum(3**(p - 1 - j) * 2**prefix[j] for j in range(p))
            value = Fraction(carry, full)
            evaluation = sum(Fraction(2**prefix[j], 3**j) for j in range(p))
            evaluation /= 1 - Fraction(2**prefix[-1], 3**p)
            require(evaluation == -3 * value, 'complete denominator')
            q = value
            for a in word:
                q = (3 * q + 1) / 2**a
                require(q.numerator % 2 == q.denominator % 2 == 1, 'legal rational clock')
            require(q == value, 'rational cycle')
            count += 1
    return count


def convergent_family():
    for m in range(1, 8):
        b = 3**m + 1
        y = (2**b - 1) // 3
        require((y + 1) % 3**m == 0, 'integral inverse cylinder')
        q = 2**m * ((y + 1) // 3**m) - 1
        for _ in range(m):
            q, a = step(q, 1)
            require(a == 1, 'initial gap')
        require(q == y and step(q, 1) == (1, b), 'first differing gap')
        require(step(1, 1) == (1, 2), 'fixed point')


def source_rows():
    def pow2_part(x):
        return x & -x

    for n in range(100):
        r = pow2_part(3 * n + 1)
        s = pow2_part(3 * n + 2)
        require([pow2_part(6 * n + i) for i in (1, 4, 2, 5)] == [1, 2 * s, 2 * r, 1],
                'one-gap source kernel')
    for w in range(1, 32):
        for m in range(12):
            q = 2**(m + 1) * w - 1
            f = 1
            for _ in range(m + 1):
                q, a = step(q, 1)
                f <<= a - 1
            require(f == pow2_part(3**(m + 1) * w - 1), 'mixed decimation')


if __name__ == '__main__':
    finite_orbits()
    words = cycle_denominators()
    convergent_family()
    source_rows()
    print(f'250 rational starts x 40 steps, {words} full cycle words, 7 explicit convergent sources, 100 dyadic and 372 mixed rows passed')
