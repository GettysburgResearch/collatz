#!/usr/bin/env python3
"""Exact finite controls for two explicit forced-divergence constructions.

The schedule's infinite chain-hitting property is proved in Markdown. This
program checks actual orbit membership and the literal finite branch rules.
"""
import hashlib
import json
from itertools import product


def require(condition, detail):
    if not condition:
        raise ValueError(detail)


def up(x):
    return (3*x+1)//2


def down(x):
    return (x+1)//2


def schedule(count):
    rows = []
    previous = 0
    for j in range(1, count+1):
        source = (j & -j).bit_length()
        threshold = max(8, 2*previous, 2**(j*j))
        value = source
        steps = 0
        while value <= threshold:
            value = up(value)
            steps += 1
        rows.append([j, source, steps, value])
        previous = value
    return rows


def band_by_exponents(x):
    base = 64
    while base <= x:
        if 4*x < 5*base:
            return True
        base *= 4
    return False


def band_by_binary(x):
    bits = bin(x)[2:]
    return len(bits) >= 7 and len(bits) % 2 == 1 and bits.startswith('100')


def step(x, gate):
    return down(x) if gate(x) else up(x)


def check_growth(x, gate):
    a = step(x, gate)
    b = step(a, gate)
    c = step(b, gate)
    require(sum(bool(gate(z)) for z in (x, a, b)) <= 1, (x, a, b, c))
    require(9*x <= 8*c, (x, a, b, c))
    return ''.join('D' if gate(z) else 'U' for z in (x, a, b))


def main():
    rows = schedule(32)
    holes = [r[3] for r in rows]
    for j, source, steps, h in rows:
        value = source
        for _ in range(steps):
            value = up(value)
        require(value == h, ('actual upward orbit', j))
        require(h > 2**(j*j) and h >= 8, ('threshold', j))
        require(h <= 2*down(h) and down(h) < h, ('first guard', j))
        require(h <= 2*up(down(h)) and up(down(h)) < h, ('second guard', j))
        require(down(h) not in holes and up(down(h)) not in holes, ('hole guards', j))
    for a, b in zip(holes, holes[1:]):
        require(2*a < b, ('spacing', a, b))

    # Every choice of downward departures among all holes that these first
    # three steps could visit. All future holes exceed the largest crop.
    maximum = 65536
    relevant = [h for h in holes if h <= 4*(maximum+1)]
    require(holes[len(relevant)] > 4*(maximum+1), 'source crop coverage')
    words = set()
    for bits in product((False, True), repeat=len(relevant)):
        chosen = {h for h, take in zip(relevant, bits) if take}
        for x in range(1, maximum+1):
            words.add(check_growth(x, chosen.__contains__))

    band_count = 0
    returns = {3: 0, 6: 0}
    for x in range(1, 1 << 18):
        require(band_by_binary(x) == band_by_exponents(x), ('binary classifier', x))
        if band_by_binary(x):
            band_count += 1
            require(not band_by_binary(down(x)), ('band down guard', x))
            require(not band_by_binary(up(down(x))), ('band up guard', x))
            base = 1 << (x.bit_length()-1)
            require(base <= x and 4*x < 5*base, ('actual band', x))
            value = down(x)
            duration = 1
            while not band_by_binary(value):
                require(duration < 6, ('return not found', x, value))
                value = up(value)
                duration += 1
            z2 = up(up(down(x)))
            expected = 3 if 4*z2 < 5*base else 6
            require(duration == expected, ('exact first return', x, duration, expected))
            next_base = base if duration == 3 else 4*base
            require(next_base <= value and 4*value < 5*next_base,
                    ('next hole band', x, value, next_base))
            returns[duration] += 1
        check_growth(x, band_by_binary)

    encoded = json.dumps(rows, separators=(',', ':')).encode()
    result = {
        'scope': 'Exact finite scheduler, binary classifier and three-step arithmetic controls; no infinite chain-hitting claim is inferred from enumeration.',
        'scheduler_rows': len(rows),
        'scheduler_sha256': hashlib.sha256(encoded).hexdigest(),
        'first_eight_scheduler_rows': rows[:8],
        'largest_hole_bits': holes[-1].bit_length(),
        'all_gate_subsets': 2**len(relevant),
        'starts_per_gate_subset': maximum,
        'three_step_branch_words': sorted(words),
        'binary_classifier_inputs': (1 << 18)-1,
        'automatic_holes_in_crop': band_count,
        'automatic_first_return_native_counts': returns,
        'success': True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
