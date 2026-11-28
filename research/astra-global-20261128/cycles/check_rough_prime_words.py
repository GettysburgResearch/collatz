"""Exact finite controls for the rough reservoir and genuine consecutive tags."""

from collections import Counter
from fractions import Fraction
from itertools import product
from math import prod
import json


MODULUS = 16
UNITS = tuple(range(1, MODULUS, 2))


def require(statement, explanation):
    if not statement:
        raise ValueError(explanation)


def factors(n):
    result = []
    p = 2
    while p * p <= n:
        while n % p == 0:
            result.append(p)
            n //= p
        p += 1
    if n > 1:
        result.append(n)
    return result


def reservoir(box):
    odd = range(box[0] | 1, box[1] + 1, 2)
    rough = [n for n in odd if n % 3 and n % 5]
    mass = sum(Fraction(1, n) for n in rough)
    actual, majorant = Counter(), Counter()
    for n in odd:
        if n % 3:
            weight = Fraction(1, n) / mass
            majorant[n % MODULUS] += weight
            if n % 5:
                actual[n % MODULUS] += weight
    require(sum(actual.values()) == 1, "actual rough normalization")
    require(all(actual[a] <= majorant[a] for a in UNITS), "positive domination")
    return rough, actual, majorant


def multiply(left, right):
    out = Counter()
    for a in UNITS:
        for b in UNITS:
            out[a * b % MODULUS] += left[a] * right[b]
    return out


def phase(a, sign, frequency):
    for e, k in product(range(2), range(4)):
        if (-1)**e * 3**k % MODULUS == a:
            return (2 * e * sign + frequency * k) % 4
    raise ValueError("incomplete unit decomposition")


def transform(measure, sign, frequency):
    real = imag = Fraction(0)
    for a in UNITS:
        angle = phase(a, sign, frequency)
        real += (1, 0, -1, 0)[angle] * measure[a]
        imag += (0, 1, 0, -1)[angle] * measure[a]
    return real, imag


def gaussian_product(values):
    u, v = Fraction(1), Fraction(0)
    for x, y in values:
        u, v = u * x - v * y, u * y + v * x
    return u, v


def fourier_check(components):
    actual, upper = Counter({1: Fraction(1)}), Counter({1: Fraction(1)})
    for _, law, majorant in components:
        actual = multiply(actual, law)
        upper = multiply(upper, majorant)
    residual = Fraction(0)
    for sign, frequency in product(range(2), range(4)):
        joined = gaussian_product(
            transform(component[2], sign, frequency) for component in components
        )
        require(joined == transform(upper, sign, frequency), "multiplicative Fourier product")
        if (sign, frequency) != (0, 0):
            residual += abs(joined[0]) + abs(joined[1])
    constant_term = sum(upper.values()) / len(UNITS)
    ceiling = constant_term + residual / len(UNITS)
    for a in UNITS:
        require(actual[a] <= upper[a] <= ceiling, "cell majorant and Fourier upper")
    require(ceiling < sum(upper.values()), "Fourier upper improves the total mass")
    return len(UNITS), str((ceiling * 1000).__ceil__()) + "/1000"


VISIT = {1: 0, 5: 1, 85: 2}


def label(n):
    path = []
    while n not in VISIT:
        require(len(path) < 2000, "terminal label beyond finite control horizon")
        path.append(n)
        n = (3 * n + 1) // 2 if n % 2 else n // 2
    fate = VISIT[n]
    for x in path:
        VISIT[x] = fate
    return fate


def main():
    require(label(8) == label(128) == 0, "both marked roots exit to unmarked powers of two")
    components = [reservoir(interval) for interval in ((31, 49), (43, 65), (53, 81))]
    cells, fourier_cap = fourier_check(components)
    primes = [p for p in range(83, 138) if factors(p) == [p]]
    first_tags, last_tags = [p for p in primes if p <= 103], [p for p in primes if p >= 107]
    representations = Counter(prod(t) for t in product(*(c[0] for c in components)))
    terminal = Counter()
    directed = Counter()
    total_tuples = 0
    for earlier, ways in representations.items():
        for a, b in product(first_tags, last_tags):
            m = earlier * a * b
            factorization = factors(earlier) + [a, b]
            require(max(factorization[:-2]) < a < b, "true final exponent-one tags")
            require(ways <= 5 ** len(factorization), "ordered representation upper")
            terminal[m] += ways
            directed[label(earlier * a), label(m)] += ways
            total_tuples += ways
    require(len(terminal) == len(representations) * len(first_tags) * len(last_tags),
            "terminal product determines both genuine last tags")
    require(sum(terminal.values()) == total_tuples, "representation mass")
    require(directed[1, 2] > 0 and directed[2, 1] > 0, "both physical directed transitions")
    output = {
        "modulus": MODULUS,
        "exact_fourier_characters": cells,
        "certified_residue_probability_upper_rounded_up": fourier_cap,
        "preparatory_box_cardinalities": [len(c[0]) for c in components],
        "tag_box_cardinalities": [len(first_tags), len(last_tags)],
        "ordered_tuples": total_tuples,
        "distinct_true_band_products": len(terminal),
        "maximum_tuple_multiplicity": max(terminal.values()),
        "unweighted_5_to_85_tuples": directed[1, 2],
        "unweighted_85_to_5_tuples": directed[2, 1],
        "scope": "finite harmonic domination and Fourier algebra, tuple multiplicities, actual ordered prime tags and native visit labels"
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
