"""Finite physical rows and exhaustive small powered-word descriptions."""

from collections import Counter
from functools import cache
from itertools import product
from math import comb, gcd
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def step(x):
    return (3 * x + 1) // 2 if x % 2 else x // 2


def path(source, *, clocks=None):
    value = source
    bits = []
    odd_values = []
    carry = 0
    while (value != 1 if clocks is None else len(bits) < clocks):
        parity = value % 2
        if parity:
            odd_values.append(value)
            carry = 3 * carry + (1 << len(bits))
        bits.append(parity)
        value = step(value)
        require(len(bits) <= 1000, 'fixture exceeded first-hit clock budget')
    require((1 << len(bits)) * value == 3 ** len(odd_values) * source + carry,
            'physical affine row')
    return tuple(bits), odd_values, carry, value


def outside(value, primes):
    require(value > 0, 'outside part requires positive input')
    for prime in primes:
        while value % prime == 0:
            value //= prime
    return value


def check_physical_rows():
    counts = Counter()
    for n in (1, 2, 3, 7, 9, 21, 27, 97):
        for k in range(1, 13):
            prefix_bits, pre_odds, pre_carry, x = path(n, clocks=k)
            p = len(pre_odds)
            if p:
                g0 = gcd((1 << k) * x, 3**p * n, pre_carry)
                require(n % g0 == 0 and x % 3, 'actual prefix content')
                counts['actual_prefixes_with_odds'] += 1
            words = set()
            for t in range(1, 19):
                m = n + (1 << k) * t
                lifted_bits, _, lifted_carry, y = path(m, clocks=k)
                require((lifted_bits, lifted_carry, y) ==
                        (prefix_bits, pre_carry, x + 3**p * t), 'common lift')
                bits, odds, carry, endpoint = path(y)
                h, length = len(odds), len(bits)
                require(bits not in words, 'two lifts with the same suffix')
                words.add(bits)
                require(endpoint == 1, 'wrong finite target')
                if not h:
                    counts['all_even_suffixes'] += 1
                    continue
                coords = (1 << length, 3**(p+h) * t, 3**h * x, carry)
                require(coords[0] == sum(coords[1:]), 'four-coordinate row')
                for mask in range(1, 15):
                    total = sum((a if i else -a) for i, a in enumerate(coords)
                                if mask & (1 << i))
                    require(total != 0, 'proper zero subsum')
                    counts['proper_subsums'] += 1
                g = gcd(*coords)
                require(t % g == 0 and g & (g-1) == 0, 'common content')
                counts['nontrivial_contents'] += int(g > 1)
                for primes in ((2, 3), (2, 3, 5, 7), (2, 3, 5, 7, 11, 13)):
                    primitive_product = 1
                    for a in coords:
                        primitive_product *= outside(a // g, primes)
                    require(primitive_product == outside(t, primes) *
                            outside(x, primes) * outside(carry, primes),
                            'primitive outside product')
                    require(coords[0] // g >= 3**(p+h) * outside(t, primes),
                            'primitive height gain')
                    counts['height_and_outside_checks'] += 1
                floor = min(odds)
                require(coords[0] * floor**h <= (3*floor+1)**h * y,
                        'minimum odd input inequality')
                counts['positive_literal_carries'] += 1
    return dict(sorted(counts.items()))


@cache
def root_cost(word):
    if not word:
        return 0
    best = len(word)
    for length in range(1, len(word) + 1):
        root = word[:length]
        end = 0
        while word.startswith(root, end):
            end += length
            best = min(best, length + root_cost(word[end:]))
    return best


def check_word_counts(limit=12):
    counts = Counter()
    words = []
    for length in range(limit + 1):
        for letters in product('01', repeat=length):
            word = ''.join(letters)
            cost = root_cost(word)
            words.append((length, cost))
            for end in range(length + 1):
                require(root_cost(word[:end]) <= 2 * cost, 'prefix truncation')
                counts['truncations'] += 1
    for length in range(limit + 1):
        for budget in range(length // 2 + 1):
            exact = sum(1 for size, cost in words if size <= length and cost <= budget)
            require(exact <= (budget+1)*4**budget*comb(length, budget),
                    'powered-root counting bound')
            counts['description_counts'] += 1
    counts['binary_words'] = len(words)
    counts['maximum_length'] = limit
    return dict(sorted(counts.items()))


if __name__ == '__main__':
    print(json.dumps({'physical': check_physical_rows(), 'words': check_word_counts()},
                     indent=2, sort_keys=True))
