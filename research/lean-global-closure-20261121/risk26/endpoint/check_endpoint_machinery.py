"""Exact finite controls for the endpoint machinery notes.

These check finite identities and adversarial constructions. They do not
test an infinite Collatz claim or a probabilistic almost-sure theorem.
"""

from fractions import Fraction
from itertools import product
from math import prod
import json


def require(condition, label):
    if not condition:
        raise RuntimeError(label)


def vp(n, prime):
    require(n != 0, "valuation of zero")
    n = abs(n)
    v = 0
    while n % prime == 0:
        n //= prime
        v += 1
    return v


def carry(word):
    a = 0
    result = 0
    for g in word:
        result = 3 * result + 2**a
        a += g
    return a, result


def crt(a, modulus_a, b, modulus_b):
    return a + modulus_a * (
        (b - a) * pow(modulus_a, -1, modulus_b) % modulus_b
    )


def critical_word(d):
    totals = [(3**i).bit_length() - 1 for i in range(d + 1)]
    return tuple(totals[i + 1] - totals[i] for i in range(d))


def ordinary_collision(word, m):
    d = len(word)
    a, c = carry(word)
    delta = 2**a - 3**d
    mod2, mod3 = 2 ** (a + 2), 3 ** (m + 1)
    r2 = (c + 2 ** (a + 1)) * pow(delta, -1, mod2) % mod2
    r3 = (c + 3**m) * pow(delta, -1, mod3) % mod3
    source = crt(r2, mod2, r3, mod3)
    if source == 0:
        source += mod2 * mod3
    states = [source]
    for g in word:
        numerator = 3 * states[-1] + 1
        require(vp(numerator, 2) == g, "incorrect physical valuation")
        states.append(numerator // 2**g)
    endpoint = states[-1]
    require(2**a * endpoint == 3**d * source + c, "full carry")
    require(vp(source - endpoint, 2) == 1, "exact binary collision depth")
    require(vp(source - endpoint, 3) == m, "exact ternary collision depth")
    require(source % 2 == endpoint % 2 == 1, "ordinary odd endpoints")
    require(source % 3 != 0 and endpoint % 3 != 0, "ordinary unit endpoints")

    linear = source * (2**a - 3**d) - c
    real_product = (2**a) * (3**d) * c
    binary_product = Fraction(1, 2 ** (a + vp(linear, 2)))
    ternary_product = Fraction(1, 3 ** (d + vp(linear, 3)))
    actual_product = real_product * binary_product * ternary_product
    expected_product = Fraction(c, 2 ** (a + 1) * 3**m)
    require(actual_product == expected_product, "S-adic product identity")
    require(
        Fraction(1, 6 * 3**m) <= actual_product
        <= Fraction(d, 3 * 3**m),
        "critical subspace-product bracket",
    )
    return source, endpoint, a, c


def check_collision_controls():
    cases = 0
    last = None
    for d in list(range(1, 41)) + [64, 100, 200]:
        word = critical_word(d)
        require(all(g in (1, 2) for g in word), "critical gap alphabet")
        a, c = carry(word)
        require(2**a <= 3**d < 2 ** (a + 1), "exact critical total")
        require(3 ** (d - 1) <= c and 3 * c <= d * 3**d,
                "complete balanced carry")
        for m in [1, 2, 3, max(1, d.bit_length() - 1)]:
            last = ordinary_collision(word, m)
            cases += 1
    return {"ordinary_CRT_collisions": cases,
            "largest_source_bits": last[0].bit_length()}


def check_repeat_factorization():
    # Rational geometric weights and rational t make the finite tensor
    # identity exact. t stands for 2**s in the written proof.
    p, r, t = Fraction(2, 3), Fraction(1, 3), Fraction(3, 2)
    alphabet = range(1, 6)
    cases = 0
    for d in range(1, 5):
        for k in range(2, 7):
            direct = sum(
                (prod(p * r ** (g - 1) for g in w) ** k)
                * t ** ((k - 1) * sum(w))
                for w in product(alphabet, repeat=d)
            )
            single = sum((p * r ** (g - 1)) ** k * t ** ((k - 1) * g)
                         for g in alphabet)
            ratio = r**k * t ** (k - 1)
            closed = p**k * t ** (k - 1) * (1 - ratio**5) / (1 - ratio)
            require(single == closed, "finite geometric moment")
            require(direct == single**d, "all-template repeat factorization")
            cases += 1
    return {"exact_repeat_moment_factorizations": cases}


def odd_orbit(n, horizon):
    result = []
    seen = set()
    while n not in seen and len(result) < horizon:
        seen.add(n)
        result.append(n)
        v = vp(3 * n + 1, 2)
        n = (3 * n + 1) // 2**v
    return result


def check_sieve_controls():
    cases = 0
    for source in [7, 27, 31, 97, 871, 6171]:
        states = odd_orbit(source, 20)
        n = len(states)
        require(n > 1, "nontrivial distinct finite orbit")
        differences = [abs(states[i] - states[j])
                       for i in range(n) for j in range(i)]
        discriminant = prod(differences)
        weighted_divisor = 1
        for prime in [2, 3]:
            valuation_sum = sum(vp(d, prime) for d in differences)
            residue_pair_count = 0
            modulus = prime
            while modulus <= max(differences):
                residue_pair_count += sum(d % modulus == 0 for d in differences)
                modulus *= prime
            require(valuation_sum == residue_pair_count,
                    "prime-power diagonal-corrected collision identity")
            weighted_divisor *= prime**valuation_sum
        require(discriminant % weighted_divisor == 0, "sieve product divisibility")
        diameter = max(states) - min(states)
        require(discriminant <= diameter ** (n * (n - 1) // 2),
                "sieve actual-height upper bound")
        cases += 1
    return {"same_source_sieve_controls": cases}


def main():
    # Exact brackets used to prove lambda_2(s_*)<1.
    require(3**2 > 2**3, "ell > 3/2")
    require(3**5 < 2**8, "ell < 8/5")
    result = {"status": "PASS", **check_collision_controls(),
              **check_repeat_factorization(), **check_sieve_controls()}
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
