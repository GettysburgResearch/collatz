"""Certify finite ternary and physical native collision moments."""
import json
from collections import Counter
from math import comb


BITS = 120
SCALE = 1 << BITS


def ceiling(n, d):
    return -(-n // d)


def next_level(lower, upper, terms=40):
    m = len(lower)
    output_lower = [0] * (3 * m)
    output_upper = [0] * (3 * m)
    # All exponents with the same parity form one geometric tail; the
    # predecessor indices obey i -> 4i+1 modulo the preceding modulus.
    tail = ceiling(4 * max(upper), 3 * 4 ** terms)
    for target in range(3 * m):
        if target % 3 == 0:
            continue
        initial_a = 1 if target % 3 == 2 else 2
        index = (((1 << initial_a) * target - 1) // 3) % m
        low = 0
        high = tail
        for j in range(terms):
            low += lower[index] >> (2 * j)
            high += ceiling(upper[index], 1 << (2 * j))
            index = (4 * index + 1) % m
        output_lower[target] = low >> initial_a
        output_upper[target] = ceiling(high, 1 << initial_a)
    if not sum(output_lower) <= SCALE <= sum(output_upper):
        raise ValueError("probability normalization failed")
    return output_lower, output_upper


def check_tables():
    lower = upper = [SCALE]
    result = []
    for depth in range(12):
        modulus = len(lower)
        low = modulus * sum(x*x for x in lower) // SCALE
        high = ceiling(modulus * sum(x*x for x in upper), SCALE)
        if high > 16 * (depth+1)**2 * SCALE:
            raise ValueError("ternary collision bound failed")
        result.append([low, high])
        if depth < 11:
            lower, upper = next_level(lower, upper)
    return result


def check_sources():
    total = 0
    energies = []
    for k in range(17):
        population = Counter()
        fibers = Counter()
        intercept_sum = 0
        for x in range(1 << k, 2 << k):
            n = x
            p = 0
            # The residue represents the composed affine translation modulo
            # 3^p. Raw powers of 2 are units, including the even terminal.
            shift = 0
            modulus = 1
            for _ in range(k):
                if n % 2:
                    p += 1
                    modulus *= 3
                    shift = 3 * shift + 1
                    n = (3 * n + 1) // 2
                else:
                    n //= 2
                if modulus > 1:
                    shift = (shift * ((modulus + 1) // 2)) % modulus
            if n < modulus or (n - 2 * modulus) * (2 ** p) >= 3 ** p:
                raise ValueError("ordinary lift left predicted range")
            if n % modulus != shift:
                raise ValueError("modular affine translation mismatch")
            population[p] += 1
            fibers[p, n] += 1
            intercept_sum += (n << k) - 3**p * x
            total += 1
        if any(population[p] != comb(k, p) for p in range(k + 1)):
            raise ValueError("native odd-count fibers failed")
        energy = sum(3**p * m*m for (p, _), m in fibers.items())
        if 4 * intercept_sum != k * 4**k or 2 * energy > (2+k) * 4**k:
            raise ValueError("ordinary shell collision or offset identity failed")
        energies.append(energy)
    return total, energies


if __name__ == "__main__":
    count, energies = check_sources()
    result = {"fraction_bits": BITS, "ternary_collision_intervals": check_tables(),
              "ordinary_sources_checked": count,
              "ordinary_collision_numerators_denominator_4k": energies}
    print(json.dumps(result, indent=2))
