"""Integer controls for the two-A router, fixed-target carry test and menu guard."""

from collections import Counter
import json


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def word_at(x, clock):
    carry = 0
    positions = []
    for t in range(clock):
        if x % 2:
            positions.append(t)
            carry = 3 * carry + (1 << t)
            x = (3 * x + 1) // 2
        else:
            x //= 2
    return x, tuple(positions), carry


def decode(carry, powers, clock):
    """Recover strictly ordered odd positions, returning None for an invalid carry."""
    positions = []
    last = -1
    for coefficient in powers:
        if carry <= 0:
            return None
        two_power = carry & -carry
        t = two_power.bit_length() - 1
        if t <= last or t >= clock:
            return None
        positions.append(t)
        carry -= coefficient * two_power
        last = t
    return tuple(positions) if carry == 0 else None


def powers_for(grade):
    return tuple(3**i for i in reversed(range(grade)))


def check_router():
    clock = 119
    scale = 1 << clock
    choices = Counter()
    physical_pairs = 0
    for residue in range(1, 243):
        if residue % 3 == 0:
            continue
        viable = []
        coarse = []
        for t in range(6, 114):
            carry = 7 * (1 << t) + 63
            if (scale * residue - carry) % 81 == 0:
                coarse.append(t)
                if (scale * residue - carry) % 243:
                    viable.append(t)
        require(len(coarse) == 2 and coarse[1] - coarse[0] == 54, 'coarse exponent pair')
        require(bool(viable), 'missing unit cell')
        choices[len(viable)] += 1
        for t in viable:
            s = clock - t
            for quotient in (0, 2, 10):
                q = residue + 243 * (quotient + (1 - residue % 2))
                y = ((1 << s) * q - 7) // 9
                x = ((1 << t) * y - 7) // 9
                require(q > 0 and x > 0 and y > 0 and x % 6 in (1, 5) and y % 6 in (1, 5), 'positive unit inverse')
                require(81 * x + 7 * (1 << t) + 63 == scale * q, 'pair affine equation')
                for start, end, steps in ((x, y, t), (y, q, s)):
                    require(word_at(start, steps)[0:2] == (end, (0, 2)), 'physical source A block')
                    require(word_at(5 * start, steps)[0:2] == (5 * end, (0, 5)), 'physical companion A block')
                require(word_at(x, clock)[0:2] == (q, (0, 2, t, t + 2)), 'whole source word')
                require(word_at(5 * x, clock)[0:2] == (5 * q, (0, 5, t, t + 5)), 'whole companion word')
                physical_pairs += 1
    failures = []
    for shorter in (118,):
        for residue in range(1, 243):
            if residue % 3 and not any(
                ((1 << shorter) * residue - 7 * (1 << t) - 63) % 81 == 0
                and ((1 << shorter) * residue - 7 * (1 << t) - 63) % 243 != 0
                for t in range(6, shorter - 5)
            ):
                failures.append(residue)
    require(bool(failures), '118 should have an uncovered fine cell')
    return {'unit_residues': sum(choices.values()), 'good_splits_per_residue': dict(choices),
            'physical_pairs_at_119': physical_pairs, 'uncovered_residues_at_118': failures}


def check_carry_characterization():
    seen_words = completed_words = 0
    for clock in range(1, 15):
        for residue in range(1, 1 << (clock + 1), 2):
            x = residue if residue % 3 else residue + (1 << (clock + 1))
            y, first, carry = word_at(x, clock)
            if y % 2 == 0:
                continue
            companion, second, other_carry = word_at(5 * x, clock)
            powers = powers_for(len(first))
            require(decode(carry, powers, clock) == first, 'source carry inversion')
            prediction = decode(5 * carry, powers, clock)
            completed = (len(first) == len(second) and companion == 5 * y)
            require((prediction is not None) == completed, 'fivefold carry test versus literal pair')
            if completed:
                require(prediction == second and other_carry == 5 * carry, 'companion carry inversion')
                completed_words += 1
            seen_words += 1
    return {'max_clock': 14, 'all_odd_words_with_odd_sentinel': seen_words,
            'complete_paired_words': completed_words}


def check_menu():
    x, clock = 835, 10
    y, first, carry = word_at(x, clock)
    companion, second, other_carry = word_at(5 * x, clock)
    require((y, companion, first, second, carry, other_carry) ==
            (199, 991, (0, 1, 5, 6, 8), (0, 1, 2, 3, 6), 871, 259), 'menu fixture')
    require(companion - 5 * y == -4 and other_carry - 5 * carry == -(4 << clock),
            'ordinary and real state identities')
    return {'source': x, 'companion_source': 5 * x, 'clock': clock, 'both_grades': len(first),
            'source_endpoint': y, 'companion_endpoint': companion, 'source_carry': carry,
            'companion_carry': other_carry, 'relative_offset': companion - 5 * y}


def count_exact_row(q, grade, do_replay):
    clock = 2 * grade
    two = 1 << clock
    three = 3**grade
    powers = powers_for(grade)
    first = (two * q) % three
    one_arm = both_arms = 0
    for carry in range(first, two // 2 + 1, three):
        if carry % 2 == 0 or (two * q - carry) % (3 * three) == 0:
            continue
        first_positions = decode(carry, powers, clock)
        if first_positions is None:
            continue
        one_arm += 1
        second_positions = decode(5 * carry, powers, clock)
        if second_positions is None:
            continue
        both_arms += 1
        if do_replay:
            x = (two * q - carry) // three
            require(word_at(x, clock) == (q, first_positions, carry), 'fixed-row source replay')
            require(word_at(5 * x, clock) == (5 * q, second_positions, 5 * carry),
                    'fixed-row companion replay')
    if do_replay:
        replay_single = replay_pair = 0
        low = (two * q - two // 2 + three - 1) // three
        for x in range(max(1, low), two * q // three + 1):
            if x % 6 not in (1, 5):
                continue
            y, positions, _ = word_at(x, clock)
            if y == q and len(positions) == grade:
                replay_single += 1
                other, other_positions, _ = word_at(5 * x, clock)
                replay_pair += (other == 5 * q and len(other_positions) == grade)
        require((replay_single, replay_pair) == (one_arm, both_arms), 'complete physical scan')
    return [q, grade, one_arm, both_arms]


def main():
    controls = {'two_a': check_router(), 'finite_carry_identity': check_carry_characterization(),
                'menu_guard': check_menu()}
    controls['fixed_rows'] = {
        'columns': ['ordinary_q', 'p_at_clock_2p', 'bounded_unit_one_arm', 'bounded_unit_paired'],
        'physical_scan_through_grade': 24,
        'rows': [count_exact_row(q, p, p <= 24) for p in (12, 16, 20, 24, 28, 32, 36, 40)
                 for q in (1, 5, 7, 13)]}
    print(json.dumps(controls, indent=2))


if __name__ == '__main__':
    main()
