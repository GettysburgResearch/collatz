"""Exact checks for the compact odd-slope pair update and multiplicative sampling."""
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import product
import json
from pathlib import Path


def require(test, reason):
    if not test:
        raise ValueError(reason)


def odd_unit_mod(q, modulus):
    return (q.numerator * pow(q.denominator, -1, modulus)) % modulus


def raw_step(s, offset, alpha, bit, precision):
    modulus = 1 << precision
    other = (offset + bit) % 2
    height = s + other - bit
    slope = odd_unit_mod(alpha, modulus) * pow(3, height, modulus)
    numerator = (3 ** other * offset + other - bit * slope) % modulus
    require(numerator % 2 == 0, 'raw offset is dyadically integral')
    return height, numerator // 2, other


def run_word(s, offset, alpha, word, precision):
    for k, bit in enumerate(word):
        s, offset, _ = raw_step(s, offset, alpha, bit, precision - k)
    return s, offset


def modular_checks():
    alphas = [Fraction(a, b) for a, b in ((1, 1), (5, 1), (7, 1), (17, 1), (11, 17), (-1, 1))]
    haar_rows = high_bits = 0
    for alpha in alphas:
        for p in range(1, 6):
            mod = 1 << p
            for bit in (0, 1):
                image = Counter()
                for s, offset in product(range(2 * mod), repeat=2):
                    h, d, _ = raw_step(s, offset, alpha, bit, p + 1)
                    image[(h % mod, d)] += 1
                require(len(image) == mod ** 2 and set(image.values()) == {4}, 'individual Haar branch')
                haar_rows += (2 * mod) ** 2
        for n, v in product(range(3, 7), range(1, 4)):
            delta = 1 << (n + v - 3)
            for s, d, bits in product((-3, 0, 2), (-2, 0, 3), product((0, 1), repeat=n)):
                p, q = run_word(s, d, alpha, bits, n + v)
                r, z = run_word(s + delta, d, alpha, bits, n + v)
                require(r - p == delta, 'level shift along one literal word')
                require((z - q) % (1 << v) == bits[0] * (1 << (v - 1)), 'exact high-bit sign')
                high_bits += 1
    return {'haar_branch_source_rows': haar_rows, 'high_bit_word_comparisons': high_bits}


def next_integer(z):
    return (3*z + 1)//2 if z % 2 else z//2


def integer_checks():
    rows = overlaps = 0
    for lower, upper, offset1, offset2 in [(1,5,0,0),(3,11,7,-5),(17,25,-11,13),(3,9,0,0)]:
        alpha = Fraction(upper, lower)
        d = offset2 - alpha * offset1
        for x in range(3, 2051):
            a = lower * x + offset1
            b = upper * x + offset2
            h = 0
            z = odd_unit_mod(d, 1 << 13)
            for k in range(12):
                h, z, actual = raw_step(h, z, alpha, a % 2, 13-k)
                require(actual == b % 2, 'raw word must follow both true integer arms')
                a, b = next_integer(a), next_integer(b)
                residual = b - alpha * Fraction(3) ** h * a
                require(z == odd_unit_mod(residual, 1 << (12-k)), 'true residual in complete precision')
                rows += 1
                overlaps += a == b and alpha * Fraction(3) ** h != 1
    return {'true_integer_pair_steps': rows, 'actual_unequal_slope_coincidences': overlaps}


def valuation(z):
    return (z & -z).bit_length()-1


def sampling_checks():
    periods = dyadic_atoms = even_prefixes = 0
    for a, m, c in product((3,5,7,9,11,17,25), (1,4), (0,2)):
        v, d = valuation(m), valuation(a*a-1)
        for depth in range(v+d, 13):
            mod = 1 << depth
            period = 1 << (depth - v - d + 1)
            observed = {(c + m * pow(a,n,mod)) % mod for n in range(period)}
            expected = {z for z in range(mod) if (z-(c+m)) % (1 << (v+d)) == 0 or
                        (z-(c+m*a)) % (1 << (v+d)) == 0}
            require(observed == expected and len(observed) == period, 'exact tower permutation')
            periods += 1
        for r in range(1,9):
            mod = 1 << (r+2)
            matches = [h for h in range(1 << r) if a*pow(3,h,mod)%mod == 1]
            require(len(matches) == int(a % 8 in (1,3)), 'absorbing-level residue class')
            dyadic_atoms += 1
    for a,c,t in product((2,4,6,10),(0,1,5,7),range(2,12)):
        n = t+1
        x, base = c+a**n, c
        for k in range(t):
            require(x % 2 == base % 2, 'large even tower fixed-shift word')
            x, base = next_integer(x), next_integer(base)
            even_prefixes += 1
    return {'complete_odd_tower_periods':periods,'absorbing_residue_checks':dyadic_atoms,
            'deterministic_even_tower_departures':even_prefixes}


if __name__ == '__main__':
    results = {'finite_scope':'exact compact raw branch, Fourier high-bit and physical source identities; limiting laws require the written proof',
               'source_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
               'modular':modular_checks(),'physical':integer_checks(),'sampling':sampling_checks()}
    print(json.dumps(results, indent=2, sort_keys=True))
