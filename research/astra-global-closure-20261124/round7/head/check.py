"""Independently replay the three complete affine tables in UnitTripling.lean."""

from collections import Counter
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
import re


RULES = {
    'h': (2, 0, 1, 0), 'D': (1, 0, 2, 0),
    't': (2, 1, 3, 2), 'i': (3, 2, 2, 1),
    'a': (9, 3, 3, 1), 'b': (9, 6, 3, 2),
    'A': (3, 1, 9, 3), 'B': (3, 2, 9, 6),
}
SPECS = {'up': (40, 144, 'hDtiab'), 'down': (172, 186624, 'hDtiAB'),
         'both': (33, 864, 'hDtiabAB')}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def parse_tables(source):
    body = source.split('private def route : Mode → Nat → Nat → String\n', 1)[1]
    body = body.split('  | _, _, _ => ""\n', 1)[0]
    tables = {mode: {} for mode in SPECS}
    group = None
    for line in body.splitlines():
        row = re.fullmatch(r'  \| \.(up|down|both), (\d+), b => match b with', line)
        if row:
            require(group is None, 'unterminated table group')
            group = row[1], int(row[2])
        elif line == '    | _ => ""':
            require(group is not None, 'misplaced end of group')
            group = None
        else:
            row = re.fullmatch(r'    \| (\d+) => "([a-zA-Z]+)"', line)
            require(row and group, f'bad affine certificate syntax {line!r}')
            mode, modulus = group
            key = modulus, int(row[1])
            require(key not in tables[mode], f'duplicate {mode} row {key}')
            tables[mode][key] = row[2]
    require(group is None, 'incomplete final group')
    return tables


def replay(mode, table):
    leaf_count, period, letters = SPECS[mode]
    require(len(table) == leaf_count, 'row count changed')
    require(math.lcm(*(a for a, _ in table)) == period, 'period changed')
    cover = bytearray(period)
    counts = Counter()
    test_count = 0
    max_unit = Fraction(0)
    max_end = Fraction(0)
    max_word = 0
    test_parities = set()
    for (modulus, base), word in sorted(table.items()):
        require(set(word) <= set(letters), f'illegal direction in {mode} {word}')
        if mode == 'both':
            require(modulus % 2 == 0 and base % 2 == 1 and 1 <= base < modulus,
                    f'odd source skipped in row {(modulus, base)}')
        else:
            require(2 <= base <= modulus + 1, f'first positive source above 1 skipped: {base}')
        start = base % modulus
        require(not any(cover[start::modulus]), 'overlapping source classes')
        cover[start::modulus] = bytes([1]) * (period // modulus)
        a, b = modulus, base
        max_word = max(max_word, len(word))
        for letter in word:
            i, j, k, l = RULES[letter]
            c, ca = divmod(a, i)
            d, db = divmod(b, i)
            require(ca == 0 and db == j, f'bad {mode} {modulus} {base} at {letter}')
            src_a, src_b = a, b
            a, b = k*c, k*d+l
            require(a > 0 and b > 0, 'nonpositive intermediate affine row')
            if letter in 'abAB':
                u, v = (src_a, src_b) if letter.isupper() else (a, b)
                require(u % 3 == 0 and v % 3 != 0, 'query lacks unit condition')
                max_unit = max(max_unit, Fraction(u, modulus), Fraction(v, base))
                test_parities.add((u % 2, v % 2))
                test_count += 1
        if mode == 'both':
            require((a, b) == (3*modulus, 3*base), 'tripling endpoint mismatch')
        else:
            require(a <= modulus and 0 < b < base, 'strict descent failed')
        max_end = max(max_end, Fraction(a, modulus), Fraction(b, base))
        counts[modulus] += 1
    cover_ok = all(cover[1::2]) and not any(cover[::2]) if mode == 'both' else all(cover)
    require(cover_ok, 'incomplete integer coverage')
    require(test_parities == {(0, 1)}, 'a queried unit is not forced odd')
    return {'leaves': len(table), 'full_modulus': period, 'leaves_by_modulus': dict(counts),
            'distinct_words': len(set(table.values())), 'longest_word': max_word,
            'total_letters': sum(map(len, table.values())), 'unit_query_positions': test_count,
            'maximum_unit_to_source_ratio': str(max_unit),
            'maximum_endpoint_to_source_ratio': str(max_end),
            'query_slope_base_parities': sorted(test_parities)}


def step(n):
    return (3*n+1)//2 if n % 2 else n//2


def iterate(n, clocks):
    for _ in range(clocks):
        n = step(n)
    return n


def prefix_bank(source):
    table_text = source.split('private def bank : List Prefix := [', 1)[1].split(']', 1)[0]
    bank = [tuple(map(int, row)) for row in re.findall(r'⟨(\d+),(\d+),(\d+),(\d+),(\d+)⟩',
                                                       table_text)]
    require(len(bank) == len(set(bank)) == 6, 'incorrect prefix bank')
    for h, base, p, g, y in bank:
        lo, hi, p_count, q_count = base, 3*base, 0, 0
        for _ in range(h):
            p_count += lo % 2
            q_count += hi % 2
            lo, hi = step(lo), step(hi)
        require((p_count, 1+q_count-p_count, lo, hi) == (p, g, y, 3**g*y-1),
                'ordinary prefix trace')
        require(base % 2 == 1 and 1 <= g <= min(3, h) and h <= 23, 'prefix ranges')
        require(52488 % (2**g * 3**(p+1)) == 0, 'invalid lifting stride')
    return bank


def select(q, bank):
    for index, (h, base, p, g, y) in enumerate(bank):
        dyadic, remainder = divmod(q, 2**g)
        t, residue = divmod(dyadic-y, 3**p)
        u = base + 2**h * t
        if remainder == residue == 0 and t >= 0 and u % 3:
            return index, u, h, g
    raise ValueError(f'no physical prefix accepts {q}')


def bank_controls(bank):
    count = Counter()
    for i in range(243):
        base = 136 + 216*i
        index = select(base, bank)[0]
        count[index] += 1
        for extension in (0, 1, 29):
            q = base + extension*52488
            j, u, h, g = select(q, bank)
            # Extra small-base constraints may allow an earlier word at a later
            # lift, but the original word must still accept as well.
            require(select(q, [bank[index]])[0] == 0, 'inconsistent cell lift')
            require(j <= index and u % 2 == 1 and u % 3 != 0 and u > 0, 'word domain')
            require(iterate(u, h) == q//2**g and iterate(3*u, h)+1 == 3**g*(q//2**g),
                    'ordinary affine lift')
    require([count[j] for j in range(6)] == [162, 54, 18, 6, 2, 1], 'cell coverage')
    max_slope = max(Fraction(2**h, 2**g*3**p) for h, _, p, g, _ in bank)
    require(max_slope == Fraction(2**20, 729), 'unit height coefficient')
    return {'prefixes': len(bank), 'positive_cell_modulus': 52488, 'cells': 243,
            'newly_covered': [count[j] for j in range(6)], 'ordinary_lifts_replayed': 3*243,
            'largest_unit_slope_in_Q': str(max_slope)}


def ray_projection(v, bank):
    power = 3*v+1
    m = (power & -power).bit_length()-1
    a = power >> m
    require(v % 2 == 1 and v % 9 == 2 and a % 2 == 1 and m >= 1, 'original source')
    z = 3**(m+1)*a-1
    require(iterate(v, m) == a and iterate(9*v+2, m) == z, 'original pair')
    if (z+1) % 4 == 3:
        index, u, h, g = select(4*power, bank)
        d = m+2-g
        right = 3**(m+2)*a-1
        require(d >= 0 and iterate(u, h+d) == a and iterate(3*u, h+d) == right,
                'upward exact pair')
        require(iterate(z, 2) == iterate(right, 2), 'upward meeting')
        require(u < 24000*v, 'size bound')
        return str(index)
    require(iterate(3*v, m) == 3**m*a-1 and iterate(3**m*a-1, 2) == iterate(z, 2),
            'downward meeting')
    return 'identity'


def ordinary_controls(bank):
    # A first arrival in the lower arm does not pay for the upper one.
    clocks = 0
    for m in range(4, 301, 2):
        if m % 3 == 0:
            continue
        x = (2**m-1)//3
        require(x % 3 != 0 and step(x) == 2**(m-1), 'lower clock / unit')
        require(iterate(x, m) == 1 and iterate(3*x, m) == 3**m-1, 'first-hit mismatch')
        clocks += 1
    for j in range(1, 61):
        power = 2**(18*j)
        n, u, v = (power-1)//3, (16*power-7)//9, (32*power-23)//9
        require(n % 18 == 9 and u % 3 == v % 3 == 1, 'fixed ray residues')
        require(iterate(u, 3) == 2*power and iterate(3*u, 4) == 3*power-1,
                'first old-ray query')
        require(iterate(v, 4) == 2*power-1 and iterate(3*v, 6) == 3*power//2-1,
                'second old-ray query')
    sources = list(range(11, 18012, 18))
    sources.extend((2**(18*j-2)-1)//3 for j in range(1, 61))
    branches = Counter(ray_projection(v, bank) for v in sources)
    return {'first_hit_family_exponents': clocks, 'old_18j_ray_exponents': 60,
            'original_odd_sources_replayed': len(sources), 'selected_branches': dict(branches)}


def main():
    here = Path(__file__).resolve().parent
    source = (here/'UnitTripling.lean').read_text()
    tables = parse_tables(source)
    lift = here/'OddUnitLift.lean'
    bank = prefix_bank(lift.read_text())
    report = {'tables': {mode: replay(mode, rows) for mode, rows in tables.items()},
              'six_prefixes': bank_controls(bank), 'ordinary_examples': ordinary_controls(bank),
              'odd_unit_lift_sha256': hashlib.sha256(lift.read_bytes()).hexdigest(),
              'lean_sha256': hashlib.sha256((here/'UnitTripling.lean').read_bytes()).hexdigest(),
              'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
