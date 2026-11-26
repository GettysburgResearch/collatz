"""Reconstruct the finite binary-logarithm and merger controls from integers.

This independently checks finite certificates. The unbounded parameter theorem
is a separate Lean argument; this program never pretends to iterate its huge
ordinary perfect powers.
"""
from pathlib import Path
import hashlib
import json
import re


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def advance(x):
    return (3 * x + 1) // 2 if x % 2 else x // 2


def trajectory(x, clocks):
    odd = 0
    for _ in range(clocks):
        odd += x % 2
        x = advance(x)
    return x, odd


def run(data_path):
    source = data_path.read_text()
    values = {}
    for name in ('K', 'seedB', 'seedU', 'a', 'a0'):
        match = re.search(r'^def ' + name + r' : Nat := ([0-9]+)$', source, re.M)
        require(match is not None, 'missing literal ' + name)
        values[name] = int(match.group(1))
    k = values['K']
    modulus = 1 << k
    derivative = ((3 ** 162 - 1) // 8) % modulus
    for n in range(2955):
        derivative = (derivative + (1 << (n + 2)) * derivative * derivative) % modulus
    require(derivative == values['seedB'], 'normalized derivative mismatch')
    unit = (derivative * pow(3 ** 58, -1, modulus)) % modulus
    require(unit == values['seedU'], 'logarithmic unit mismatch')
    require(unit % 2 == 1, 'unit must be odd')

    a, a0 = values['a'], values['a0']
    require(3 ** 52 * a == 1 + (1 << 119) * a0, 'anchor division')
    require(0 < a < (1 << 119), 'anchor representative')
    require(trajectory(a - 1, 119) == (1 + a0, 52), 'lower anchor')
    require(trajectory(3 ** 63 * a - 1, 119) == (1 + 3 ** 71 * a0, 60), 'upper anchor')

    left, right = 1 + unit, 1 + 3 ** 71 * unit
    p, q = 0, 0
    first_equal = None
    first_counted = None
    for clock in range(k + 1):
        if left == right:
            if first_equal is None:
                first_equal = clock
            if p == q + 71 and first_counted is None:
                first_counted = clock
        if clock == k:
            break
        p += left % 2
        q += right % 2
        left = advance(left)
        right = advance(right)
    require(left == right and p == q + 71, 'compensated finite merger')
    require(first_counted == k, 'reported first counted clock')

    odd_high = trajectory(3 ** 173 - 1, 1143)
    odd_low = trajectory(3 ** 131 - 1, 1143)
    require(odd_high[0] == odd_low[0], 'odd-base anchor merger')
    require(173 + odd_high[1] == 131 + odd_low[1], 'odd-base augmented grades')

    tested_bases = [1, 2, 3, 4, 5, 6, 7, 9, 10, 12, 15, 17, 27, 81, 243]
    exponent = 1 << 2956
    for base in tested_bases:
        odd_part = base
        valuation = 0
        while odd_part % 2 == 0:
            odd_part //= 2
            valuation += 1
        if valuation == 0:
            require(pow(base, exponent, modulus) == 1, 'odd-base congruence')
        else:
            r = valuation * (exponent // 2)
            require((pow(3, r, modulus) * pow(odd_part, exponent, modulus)) % modulus == 1,
                    'even-base normalized congruence')

    return {
        'scope': 'finite arithmetic and modular controls only',
        'data_sha256': hashlib.sha256(data_path.read_bytes()).hexdigest(),
        'precision_bits': k,
        'derivative_squarings': 2955,
        'first_equal_clock': first_equal,
        'first_counted_clock': first_counted,
        'terminal_bit_length': left.bit_length(),
        'odd_counts': [p, q],
        'odd_base_anchor_clocks': 1143,
        'odd_base_augmented_grade': 173 + odd_high[1],
        'perfect_power_congruence_control_bases': tested_bases,
        'ordinary_unbounded_family_replayed': False,
    }


if __name__ == '__main__':
    import sys
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_name('LogTowerData.lean')
    print(json.dumps(run(path), sort_keys=True, indent=2))
