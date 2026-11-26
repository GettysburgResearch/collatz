"""Independent replay of the finite data in the period-four wall argument.

The universal statement is proved in Lean. This script separately reconstructs
the ordinary merger bank, the binary rotation, and the signed-rational control.
It never uses Python assertions, so optimization cannot disable its checks.
"""
from pathlib import Path
import ast
import hashlib
import json
import re
from fractions import Fraction


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def run(x, clocks, denominator=1):
    odd = 0
    for _ in range(clocks):
        if x % 2:
            odd += 1
            x = (3 * x + denominator) // 2
        else:
            x //= 2
    return x, odd


def cycle(x, denominator):
    seen, values = {}, []
    while x not in seen:
        require(len(values) < 1000, 'control did not enter its finite cycle')
        seen[x] = len(values)
        values.append(x)
        x = run(x, 1, denominator)[0]
    return set(values[seen[x]:])


def check_reset_tree(path):
    source = path.read_text()
    rows = re.findall(r'private def row([0-9]+) : Certificate :=(.*?)\n\nset_option', source, re.S)
    require([int(r) for r, _ in rows] == list(range(16)), 'missing reset tree row')
    leaves, maximum_depth, maximum_blocks = 0, 0, 0
    exempt_mass = Fraction(0)

    def parse(tokens, pos):
        token = tokens[pos]
        if token == '.exempt':
            return ('exempt',), pos + 1
        if token == '.pair':
            return ('pair', int(tokens[pos + 1]), int(tokens[pos + 2])), pos + 3
        require(token == '.branch', 'unknown certificate token')
        left, pos = parse(tokens, pos + 1)
        right, pos = parse(tokens, pos)
        return ('branch', left, right), pos

    def verify(tree, h, residue):
        nonlocal leaves, maximum_depth, maximum_blocks, exempt_mass
        require(0 <= residue < 2 ** h, 'invalid binary representative')
        if tree[0] == 'branch':
            return verify(tree[1], h + 1, residue) + verify(tree[2], h + 1, residue + 2 ** h)
        leaves += 1
        maximum_depth = max(maximum_depth, h)
        mass = Fraction(1, 2 ** h)
        if tree[0] == 'exempt':
            require(h >= 4 and residue % 16 == 11, 'invalid exempt class')
            exempt_mass += mass
            return mass
        _, left, right = tree
        require(left <= 81 and right <= 81, 'reset block limit')
        maximum_blocks = max(maximum_blocks, left, right)
        block = lambda k: 16 ** k * residue + 11 * (16 ** k - 1) // 15
        require(run(block(left), h + 4 * left) == run(block(right) + 1, h + 4 * right),
                'reset leaf endpoint or odd grade differs')
        return mass

    mass = Fraction(0)
    for row, text in rows:
        tokens = re.findall(r'\.branch|\.pair|\.exempt|[0-9]+', text)
        tree, consumed = parse(tokens, 0)
        require(consumed == len(tokens), 'unconsumed certificate data')
        row_mass = verify(tree, 4, int(row))
        require(row_mass == Fraction(1, 16), 'incomplete row cover')
        mass += row_mass
    require(mass == 1 and exempt_mass == Fraction(1, 16), 'incomplete full source cover')
    return {'source_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
            'leaves_including_exempt': leaves, 'maximum_binary_depth': maximum_depth,
            'maximum_block_count': maximum_blocks, 'covered_mass': '15/16',
            'exempt_class': '11 modulo 16'}


def check(wheel_path):
    source = wheel_path.read_text()
    bank_text = source.split('private def bank', 1)[1].split('def residue', 1)[0]
    banks = [ast.literal_eval(s) for s in re.findall(r'\[[0-9,]+\]', bank_text)]
    require(len(banks) == 3 and all(len(b) == 16 for b in banks), 'bank dimensions')
    multiplier = [1, 3, 9, 9]
    offset = [3, 5, 8, 8]
    maximum_first_clock = [0, 0, 0, 0]
    for phase in range(4):
        bank = banks[min(phase, 2)]
        for residue, x in enumerate(bank):
            require(0 <= x < 16384 and x % 16 == residue, 'bank residue')
            y = multiplier[phase] * x + offset[phase]
            a, p = run(x, 14)
            b, q = run(y, 14)
            require(a == b and 3 ** p == multiplier[phase] * 3 ** q, 'counted bank merger')
            first = next(k for k in range(15)
                         if run(x, k)[0] == run(y, k)[0]
                         and 3 ** run(x, k)[1] == multiplier[phase] * 3 ** run(y, k)[1])
            maximum_first_clock[phase] = max(maximum_first_clock[phase], first)

    orbit = [pow(3 ** 12, j, 16384) for j in range(1024)]
    require(len(set(orbit)) == 1024 and set(orbit) == set(range(1, 16384, 16)),
            'binary wheel does not cover its complete unit class')
    for j in range(10):
        require(pow(531441, 1 << j, 1 << (5 + j)) == 1 + (1 << (4 + j)),
                'binary wheel lifting bit')

    left_cycle, right_cycle = {3, 12, 6}, {57, 93, 147, 228, 114}
    require(left_cycle.isdisjoint(right_cycle), 'signed cycles overlap')
    for x in [-11, -7, -14, -13]:
        require(cycle(x, 15) == left_cycle, 'left signed shadow')
        require(cycle(x + 15, 15) == right_cycle, 'right signed shadow')
    require(run(-11, 8, 15)[0] == 12 and run(4, 8, 15)[0] == 57, 'shadow entries')
    require(run(12, 36, 15) == (12, 12), 'left shadow lap')
    require(run(57, 20, 15) == (57, 12), 'right shadow lap')

    samples = []
    biases = [12, 6, 3, 12]
    grades = [5, 5, 5, 6]
    for n in [0, 1, 2, 7, 11, 27, 113, 65547]:
        q, v = 15 * n + 11, 0
        while q % 2 == 0:
            q //= 2
            v += 1
        s, i0 = v % 4, v + 1
        a = 3 ** (grades[s] + 12 * i0) * q
        x0 = (a + biases[s]) // 15
        r = banks[min(s, 2)][x0 % 16]
        target = (15 * r - biases[s]) % 16384
        j = next(j for j in range(1024) if orbit[j] * a % 16384 == target)
        i = i0 + j
        k_left, k_right = (8 + 36 * i + s - v) // 4, (8 + 20 * i + s - v) // 4
        block = lambda k: 16 ** k * n + 11 * (16 ** k - 1) // 15
        left = run(block(k_left), 8 + 36 * i + s + 14)[0]
        right = run(block(k_right) + 1, 8 + 20 * i + s + 14)[0]
        require(left == right, 'ordinary unequal-depth endpoints do not merge')
        require(max(k_left, k_right) <= 9 * (v + 1024) + 3, 'block bound')
        samples.append({'n': n, 'valuation': v, 'blocks': [k_left, k_right],
                        'terminal_bits': left.bit_length()})
    return {
        'scope': 'finite merger bank, signed rational control, and ordinary sample replays',
        'source_sha256': hashlib.sha256(wheel_path.read_bytes()).hexdigest(),
        'bank_rows': 64,
        'maximum_first_counted_clocks_by_phase': maximum_first_clock,
        'wheel_size': len(orbit),
        'left_signed_cycle_numerators': sorted(left_cycle),
        'right_signed_cycle_numerators': sorted(right_cycle),
        'ordinary_samples': samples,
        'reset_tree': check_reset_tree(wheel_path.with_name('WallRuns81.lean')),
        'unbounded_ordinary_theorem_replayed': False,
    }


if __name__ == '__main__':
    import sys
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_name('WallWheel.lean')
    print(json.dumps(check(path), sort_keys=True, indent=2))
