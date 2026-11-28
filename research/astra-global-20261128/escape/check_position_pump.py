#!/usr/bin/env python3
"""Check literal ordinary Collatz digit balances and interior division states."""

from collections import Counter, defaultdict
from fractions import Fraction
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent


def require(ok, message):
    if not ok:
        raise ValueError(message)


def trits(n):
    digits = []
    while n:
        n, digit = divmod(n, 3)
        digits.append(digit)
    return tuple(reversed(digits))


def windows(digits, r):
    framed = (-1,) * r + digits + (-2,) * r
    return enumerate(tuple(framed[i:i + 2 * r + 1]) for i in range(len(digits)))


def arc(n, digits, j, r):
    # Half-prefix remainders and quotient tails come from whole integer division.
    prefix = 0
    for digit in digits[:j]:
        prefix = 3 * prefix + digit
    quotient, carry = divmod(prefix, 2)
    modulus = 3 ** (2 * r)
    return n % 2, carry, prefix % modulus, quotient % modulus, digits[j]


def expanded_rows(seed, extra):
    radius, length, layer = seed['radius'], seed['length'], seed['layer']
    counts = [Counter() for _ in range(length)]
    initial = Counter()
    modulus = 3 ** (2 * radius)
    for n, count in seed['rows']:
        digits, weight = trits(n), int(count)
        initial[(n % 2, 0, 0, 0)] += weight
        for j in range(length):
            counts[j][arc(n, digits, j, radius)] += weight
    layers = counts[:layer + 1] + [counts[layer]] * extra + counts[layer + 1:]
    paths = {state: [(0, weight)] for state, weight in initial.items()}
    for j, arcs in enumerate(layers):
        next_paths = defaultdict(list)
        for (e, carry, prefix_tail, quotient_tail, digit), multiplicity in sorted(arcs.items()):
            arrivals = paths[e, carry, prefix_tail, quotient_tail]
            q, new_carry = divmod(3 * carry + digit, 2)
            end = (e, new_carry, (3 * prefix_tail + digit) % modulus,
                   (3 * quotient_tail + q) % modulus)
            while multiplicity:
                require(bool(arrivals), ('outgoing flow exceeds arrivals', j, end))
                prefix, available = arrivals.pop()
                flow = min(available, multiplicity)
                next_paths[end].append((3 * prefix + digit, flow))
                multiplicity -= flow
                if available > flow:
                    arrivals.append((prefix, available - flow))
        require(all(not bucket for bucket in paths.values()), ('unspent arrivals', j))
        paths = next_paths
    rows = Counter()
    for (e, carry, _, _), bucket in paths.items():
        require(carry == e, 'terminal parity tag')
        for n, weight in bucket:
            require(n % 2 == e, 'literal reconstructed parity')
            rows[n] += weight
    return list(rows.items())


def inspect(seed, check_repetitions=True):
    r, length, layer = seed['radius'], seed['length'], seed['layer']
    require(2 * r + 1 <= layer and layer + 1 < length - 1, 'interior layers')
    window_balance = Counter()
    interior = [Counter(), Counter()]
    total = odd = 0
    seen = set()
    for n, count in seed['rows']:
        weight = int(count)
        require(n > 0 and n % 3 and n not in seen and weight > 0, ('source', n))
        seen.add(n)
        e = n % 2
        m = (3 * n + 1) // 2 if e else n // 2
        x, y = trits(n), trits(m)
        require(len(x) == len(y) == length, ('length', n))
        require(x[0] == 2 - e, ('top branch', n))
        for cell in windows(x, r):
            window_balance[cell] -= weight
        for cell in windows(y, r):
            window_balance[cell] += weight
        for side in range(2):
            interior[side][arc(n, x, layer + side, r)] += weight
        total += weight
        odd += e * weight
    require(all(v == 0 for v in window_balance.values()), 'literal window balance')
    require(interior[0] == interior[1], 'repeated interior arcs')
    require(84 * odd > 53 * total and 3 ** 53 > 2 ** 84, 'supercritical odd fraction')
    answer = {'width': 2 * r + 1, 'digits': length, 'repeated_layer': layer,
            'sources': len(seen), 'smallest': min(seen), 'largest': max(seen),
            'total_weight': str(total), 'odd_weight': str(odd),
            'odd_fraction': str(Fraction(odd, total)),
            'position_window_cells': len(window_balance),
            'positive_repeated_arcs': len(interior[0])}
    if check_repetitions:
        larger = []
        for extra in (1, 2):
            rows = expanded_rows(seed, extra)
            expanded = dict(seed, length=length + extra, rows=rows)
            checked = inspect(expanded, check_repetitions=False)
            require(checked['odd_weight'] == answer['odd_weight'] and
                    checked['total_weight'] == answer['total_weight'], 'pumped parity totals')
            larger.append({'digits': length + extra, 'sources': checked['sources'],
                           'position_window_cells': checked['position_window_cells']})
        answer['literal_reconstructions'] = larger
    return answer


def main():
    seeds = json.loads((HERE / 'position_pump_seeds.json').read_text())
    print(json.dumps({'seeds': [inspect(seed) for seed in seeds]}, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
