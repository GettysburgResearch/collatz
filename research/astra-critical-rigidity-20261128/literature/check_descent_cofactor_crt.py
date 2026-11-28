"""Independent coordinating CRT construction and exact Fraction replay."""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import gcd, isqrt, prod
import json

PRIMES = (2, 3, 5, 7, 11)
CONSTANT = 30 * prod(2 * p for p in PRIMES if p not in (2, 3))


def require(ok, message):
    if not ok:
        raise ValueError(message)


def join(a, modulus, b, other):
    require(gcd(modulus, other) == 1, "noncoprime CRT moduli")
    return a + modulus * ((b - a) * pow(modulus, -1, other) % other), modulus * other


def construct(word, n, q, counts):
    length, k = len(word), sum(word)
    Q = q * 3**n
    require(length > 0 and k <= n and (k < n or word[-1]), "word endpoint")
    require(Q >= CONSTANT * 2**length * (k + 1)**len(PRIMES), "precision hypothesis")
    carry, grade, marks = 0, 0, []
    for t, odd in enumerate(word):
        if odd:
            marks.append((t, grade, carry))
            carry = 3 * carry + 2**t
            grade += 1
    dyadic = 2**length
    b0 = -Q * carry * pow(3**k, -1, dyadic) % dyadic
    z, modulus = 0, 1
    for p in (3, 5) if q > 1 else (3,):
        allowed = next(r for r in range(p) if (b0 + dyadic * r) % p)
        z, modulus = join(z, modulus, allowed, p)
    for p in PRIMES:
        if p in (2, 3) or q % p == 0:
            continue
        power = p
        while power < 2 * (k + 1):
            power *= p
        forbidden = set()
        for t, g, c in marks:
            numerator = b0 + q * 3**(n - g) * c
            require(numerator % 2**t == 0, "prefix numerator integrality")
            u0 = numerator // 2**t
            forbidden.add(-u0 * pow(2**(length - t), -1, power) % power)
        allowed = next(r for r in range(power) if r not in forbidden)
        z, modulus = join(z, modulus, allowed, power)
    b0 += dyadic * z
    modulus *= dyadic
    lower = (Q + 1) // 2
    b = b0 + ((lower - b0 + modulus - 1) // modulus) * modulus
    require(lower <= b <= Q and gcd(b, Q) == 1, "bounded true reduced source")
    max_wait = wait = 0
    for odd in word:
        wait = 0 if odd else wait + 1
        max_wait = max(max_wait, wait)
    smooth_cap = prod(2 * p * (k + 1) for p in PRIMES if p not in (2, 3))
    x, h = Fraction(b, Q), n
    for odd in word:
        require(x > 0 and x.denominator == q * 3**h, "complete physical denominator")
        require(x.numerator % 2 == odd, "actual native parity")
        if odd:
            cofactor = x.numerator
            for p in PRIMES:
                while cofactor % p == 0:
                    cofactor //= p
            require(cofactor * 2**(max_wait + 1) * smooth_cap >= q * 3**h,
                    "cofactor inequality at actual marked level")
            x = (3 * x + 1) / 2
            h -= 1
            counts["marked_numerator_tests"] += 1
        else:
            x /= 2
        counts["true_fraction_steps"] += 1
    require(h == n - k and x.denominator == q * 3**h, "exact terminal level")
    counts["crt_witnesses"] += 1
    counts["maximum_source_denominator_bits"] = max(counts["maximum_source_denominator_bits"], Q.bit_length())
    counts["pure_three_sources" if q == 1 else "complete_moving_five_descents"] += 1


def spaced_word(length, k):
    dates = {(i + 1) * length // k - 1 for i in range(k)}
    require(len(dates) == k and length - 1 in dates, "spaced odd dates")
    return tuple(int(t in dates) for t in range(length))


def main():
    counts = Counter()
    for length in range(1, 9):
        for word in product((0, 1), repeat=length):
            n = max(1, sum(word))
            target = CONSTANT * 2**length * (sum(word) + 1)**len(PRIMES)
            while 3**n < target or n == sum(word):
                n += 1
            construct(word, n, 1, counts)
    for n in (100, 300, 1000):
        length = (3**n).bit_length() - 1 - (len(PRIMES) + 3) * (n + 1).bit_length()
        construct(spaced_word(length, isqrt(n)), n, 1, counts)
    for n, length in ((3, 30), (4, 50), (6, 90)):
        target_bits = (length + n + CONSTANT.bit_length())**2
        q = 5
        while q.bit_length() <= target_bits:
            q *= 5
        construct(spaced_word(length, n), n, q, counts)
    print(json.dumps(dict(counts), sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
