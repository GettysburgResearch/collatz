"""Independent finite reconstruction of the smooth abstract rank obstruction.

These populations are not asserted to be Collatz trajectories.
"""
import hashlib
import json


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def integer_root(value, degree):
    current = 1 << ((value.bit_length() + degree - 1) // degree)
    while True:
        following = ((degree - 1) * current + value // current ** (degree - 1)) // degree
        if following >= current:
            break
        current = following
    while current ** degree > value:
        current -= 1
    while (current + 1) ** degree <= value:
        current += 1
    require(current ** degree <= value < (current + 1) ** degree, 'root enclosure')
    return current


def retain(values):
    if len(values) <= 2:
        return list(values)
    groups = [[v for v in values if v % 3 == digit] for digit in range(3)]
    chosen = sorted(range(3), key=lambda d: (-len(groups[d]), d))[:2]
    return [3 * v + digit for digit in chosen
            for v in retain([n // 3 for n in groups[digit]])]


def code(number):
    total, place = 0, 1
    while number:
        number, bit = divmod(number, 2)
        total += bit * place
        place *= 3
    return total


def prefix_check(values):
    modulus, nodes, levels = 1, 0, 0
    diameter = max(values) - min(values)
    while modulus <= diameter:
        children = {}
        for n in values:
            children.setdefault(n % modulus, set()).add((n // modulus) % 3)
        require(all(len(c) <= 2 for c in children.values()), 'three children')
        nodes += len(children)
        levels += 1
        modulus *= 3
    return nodes, levels


def midpoint_check(values):
    tests = 0
    for depth in range(1, 9):
        modulus = 3 ** depth
        residues = {n % modulus for n in values}
        inv_two = (modulus + 1) // 2
        for left in residues:
            for right in residues:
                middle = (left + right) * inv_two % modulus
                require(middle not in residues or left == right == middle,
                        'nontrivial modular midpoint')
                tests += 1
    return tests


def main():
    records, node_count, midpoint_count, labels_count = [], 0, 0, 0
    for period in (4, 5, 7, 11, 17, 23, 32, 47, 67, 97, 137):
        base = 100 * period * period
        values = [integer_root((base ** period) * 2 ** j, period)
                  for j in range(period)]
        remaining = sorted(values)
        colors = {}
        color = 0
        while remaining:
            selected = set(retain(remaining))
            require(bool(selected) and selected <= set(remaining), 'partition')
            prefix_check(selected)
            for v in selected:
                colors[v] = color
            remaining = [v for v in remaining if v not in selected]
            color += 1
        power = (color - 1).bit_length()
        scale = 3 ** power
        x = [scale * v + code(colors[v]) for v in values]
        for mask_kind in range(3):
            lowbits = [2 if j == 0 or mask_kind == 0
                       or (j * (17 + mask_kind) + 3) % 11 < 5 else 1
                       for j in range(period)]
            labels = [12 * v + bit for v, bit in zip(x, lowbits)]
            extended = labels + [2 * labels[0], 2 * labels[1]]
            gaps = [extended[j + 1] - extended[j] for j in range(period + 1)]
            require(all(gaps[j + 1] > gaps[j] > 0 for j in range(period)),
                    'strict seam convexity')
            require(all(gaps[0] <= v < 2 * gaps[0] for v in gaps[:-1]), 'gap octave')
            require(all((n & -n) == bit and n % 3 != 0
                        for n, bit in zip(labels, lowbits)), 'eligibility')
            require(len({n // bit for n, bit in zip(labels, lowbits)}) == period,
                    'distinct odd parts')
            require(all(abs(n - 12 * scale * v) <= 12 * scale + 2
                        for n, v in zip(labels, values)), 'smooth floor error')
            nodes, levels = prefix_check(labels)
            node_count += nodes
            midpoint_count += midpoint_check(labels)
            labels_count += period
            records.append({'period': period, 'mask': mask_kind, 'colors': color,
                            'scale': scale, 'levels': levels,
                            'minimum_curvature': min(gaps[j+1]-gaps[j]
                                                     for j in range(period))})
    encoded = json.dumps(records, sort_keys=True, separators=(',', ':')).encode()
    print(json.dumps({'scope': 'abstract smooth ranks; no chronological Collatz recurrence',
                      'populations': len(records), 'labels': labels_count,
                      'occupied_prefixes': node_count, 'modular_midpoint_pairs': midpoint_count,
                      'records_sha256': hashlib.sha256(encoded).hexdigest(),
                      'records': records}, indent=2))


if __name__ == '__main__':
    main()
