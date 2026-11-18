"""Replay ordinary words used in the rational-phase avoidance construction."""

from math import gcd
from random import Random


def unit_square_root_ten(depth):
    root = 1
    modulus = 3
    for _ in range(1, depth):
        root, = [candidate for candidate in (root, root + modulus, root + 2*modulus)
                 if (candidate*candidate - 10) % (3*modulus) == 0]
        modulus *= 3
    return root


def word_to_target(target, depth):
    inverse_letters = []
    for _ in range(depth):
        exponent = next(a for a in range(1, 5)
                        if ((1 << a)*target - 1) % 3 == 0
                        and (((1 << a)*target - 1)//3) % 3 != 0)
        target = ((1 << exponent)*target - 1)//3
        inverse_letters.append(exponent)
    return list(reversed(inverse_letters))


def ordinary_replay(letters, q):
    total = 0
    bonus = 0
    for exponent in letters:
        bonus = 3*bonus + (1 << total)
        total += exponent
    modulus_two = 1 << (total + 1)
    modulus_three = 3**q
    dyadic = ((1 << total) - bonus) * pow(3**len(letters), -1, modulus_two)
    multiplier = ((dyadic + 1) * pow(modulus_three, -1, modulus_two)) % modulus_two
    period = modulus_two * modulus_three
    start = period + ((multiplier*modulus_three - 1) % period)
    source = (1 << q)*((start + 1)//modulus_three) - 1
    assert start % modulus_three == modulus_three - 1
    assert ((source + 1)*modulus_three >> q) - 1 == start

    states = [start]
    applied = 0
    three_power = modulus_three
    for exponent in letters:
        numerator = 3*states[-1] + 1
        assert numerator & -numerator == 1 << exponent
        states.append(numerator >> exponent)
        applied += exponent
        three_power *= 3
        offset_numerator = (states[-1] << (q + applied)) - three_power*source
        assert offset_numerator << (q//4) >= (modulus_three - (1 << q)) << applied
    return states


def check_arrival_at_one(last, expected_odd, expected_shortcut):
    current = last
    shortcut_steps = 0
    for _ in range(expected_odd):
        assert current > 1
        numerator = 3*current + 1
        exponent = (numerator & -numerator).bit_length() - 1
        current = numerator >> exponent
        shortcut_steps += exponent
    assert current == 1 and shortcut_steps == expected_shortcut
    print(f'From the {last.bit_length()}-bit endpoint, reached 1 in '
          f'{expected_odd} odd steps ({shortcut_steps} shortcut steps).')


def main():
    q = 2048
    depth = q//32
    alpha = unit_square_root_ten(depth + 1)
    prescribed = word_to_target(alpha, depth)
    terminal = ordinary_replay(prescribed, q)[-1]
    assert (terminal - alpha) % (3**depth) == 0
    check_arrival_at_one(terminal, 8280, 16473)

    cutoff, precision = 64, 22
    modulus = 3**precision
    forbidden = {a * pow(b, -1, modulus) % modulus
                 for b in range(1, cutoff + 1) if b % 3
                 for a in range(-cutoff, cutoff + 1) if a % 3 and gcd(a, b) == 1}
    rng = Random(20261118)
    for attempt in range(1, 1001):
        word = [rng.choice((1, 2)) for _ in range(2*depth)]
        odd_power = 1
        binary_power = 1
        for a in word[depth:]:
            odd_power *= 3
            binary_power <<= a
            if odd_power < binary_power:
                break
        else:
            states = ordinary_replay(word, q)[depth:]
            if all(y % modulus not in forbidden for y in states):
                assert min(states) == states[0]
                print(f'Checked prescribed irrational target modulo 3^{depth}.')
                print(f'Checked {len(states)} consecutive ordinary states, {len(forbidden)} '
                      f'rational residues, and exact incoming offset bounds (fixture {attempt}).')
                check_arrival_at_one(states[-1], 8035, 16186)
                return
    raise AssertionError('fixture search exhausted')


if __name__ == '__main__':
    main()
