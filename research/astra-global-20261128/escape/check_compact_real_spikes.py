"""Exact finite controls for nested small-offset exit families and native leaves."""
from fractions import Fraction
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def residue(value, modulus):
    return value.numerator * pow(value.denominator, -1, modulus) % modulus


def affine_step(gain, offset, exponent):
    next_gain = gain * Fraction(3, 2**exponent)
    return next_gain, offset + next_gain / 3


def balanced_gaps(depth):
    totals = [(3**i - 1).bit_length() for i in range(depth + 1)]
    return [b - a for a, b in zip(totals, totals[1:])]


def affine_word(word):
    gain, offset = Fraction(1), Fraction(0)
    for exponent in word:
        gain, offset = affine_step(gain, offset, exponent)
    return gain, offset


def odd_step(n):
    z = 3*n + 1
    return z // (z & -z)


def inverse(n, e):
    num = 2**e*n - 1
    require(num % 3 == 0, 'num % 3 == 0')
    x = num // 3
    require(x > 0 and x % 2 and odd_step(x) == n, 'x > 0 and x % 2 and odd_step(x) == n')
    return x


def log_two_mod_three(target, precision):
    exponent = 0 if target % 3 == 1 else 1
    period = 2
    for depth in range(2, precision + 1):
        modulus = 3**depth
        exponent = next(k for k in range(exponent, exponent + 3*period, period)
                        if pow(2, k, modulus) == target % modulus)
        period *= 3
    return exponent, period


def nested_control():
    # Small two-layer model. The second family enforces every new low trit.
    families = [(5, 1), (0, 64)]
    first_exp, first_depth = families[0]
    first_word = [first_exp, *balanced_gaps(first_depth)]
    first_mod = 3**len(first_word)
    first_address = residue(affine_word(first_word)[1], first_mod)
    beta_mod = residue(affine_word(balanced_gaps(first_depth))[1], first_mod)
    second_exp = next(e for e in range(first_exp+1, first_exp+1+2*first_mod)
                      if (2**e*first_address-1-3*beta_mod) % first_mod == 0)
    families[1] = (second_exp, families[1][1])
    final_word = [second_exp, *balanced_gaps(families[1][1])]
    final_mod = 3**len(final_word)
    final_address = residue(affine_word(final_word)[1], final_mod)
    require(final_address % first_mod == first_address, 'final_address % first_mod == first_address')
    y = final_address + final_mod*(1 if final_address % 2 == 0 else 2)
    require(y > final_mod and y % 2 and y % 3, 'y > final_mod and y % 2 and y % 3')
    exit_words = []
    sum_weights = []
    max_offset = Fraction(0)
    for first, length in families:
        word = [first]
        x = inverse(y, first)
        total_weight = Fraction(0)
        for e in balanced_gaps(length):
            require(x > y, 'x > y')
            f = next(f for f in range(3, 15) if f != e and
                     (2**f*x - 1) % 9 in (3, 6))
            z = inverse(x, f)
            require(z > y and z % 3, 'z > y and z % 3')
            candidate = tuple([*word, f])
            slope, intercept = affine_word(candidate)
            require(y == slope*z + intercept, 'y == slope*z + intercept')
            max_offset = max(max_offset, intercept)
            total_weight += slope
            w = z
            for _ in candidate:
                require(w > y, 'w > y')
                w = odd_step(w)
            require(w == y, 'w == y')
            exit_words.append(candidate)
            x = inverse(x, e)
            word.append(e)
        require(total_weight > Fraction(1, 100), "each family carries positive weight above the calibration floor")
        sum_weights.append(str(total_weight))
    first_budget = Fraction(3*families[0][1], 2**families[0][0])
    second_budget = Fraction(3*families[1][1], 2**families[1][0])
    require(first_budget == second_budget, "the two imposed offset budgets agree")
    require(max_offset < Fraction(1, 16), "every actual exit respects the strict real cap")
    require(len(set(exit_words)) == len(exit_words), "exit words are distinct")
    require(all(w[:len(v)] != v for w in exit_words for v in exit_words if w != v),
            "no exit extends another exit")
    root_checks = 0
    for m in (1, 5, 7, 11, 17, 19, 101):
        modulus = 3*final_mod
        target = (1+3*final_address)*pow(m,-1,modulus) % modulus
        e, period = log_two_mod_three(target, len(final_word)+1)
        require(pow(2, e+period, modulus)*m % modulus == 1+3*final_address, 'pow(2, e+period, modulus)*m % modulus == 1+3*final_address')
        root_checks += 1
    return {'target': str(y), 'first_exponents': [x[0] for x in families],
            'balanced_lengths': [x[1] for x in families], 'exits': len(exit_words),
            'family_weights': sum_weights, 'largest_intercept': str(max_offset),
            'direct_parent_residue_checks': root_checks}


def finite_cap_control():
    tested, remapped, cycles = 0, 0, 0
    for x in range(1, 5000, 2):
        path = [x]
        for _ in range(25):
            path.append(odd_step(path[-1]))
        gain = Fraction(1)
        for n, (a, y) in enumerate(zip(path, path[1:]), 1):
            v = 3*a + 1
            gain *= Fraction(3, v & -v)
            offset = y-gain*x
            require(offset > 0 and 3*offset >= gain, 'offset > 0 and 3*offset >= gain')
            M = y // (12*(1+offset))
            if M >= 1:
                require(all(w > M for w in path[:n+1]), 'all(w > M for w in path[:n+1])')
            if x % 3 == 0:
                promoted = 4*x+1
                require(odd_step(promoted) == path[1], 'odd_step(promoted) == path[1]')
                require(y-gain*promoted/4 == offset-gain/4, 'y-gain*promoted/4 == offset-gain/4')
                remapped += 1
            if y in path[:n]:
                k = path[:n].index(y)
                survived = Fraction(1)
                for z in path[k:n]:
                    survived *= Fraction(3*z,3*z+1)
                earlier = Fraction(1)
                for z in path[:k]:
                    earlier *= Fraction(3*z,3*z+1)
                require(offset == y*(1-survived)+survived*y*(1-earlier), 'offset == y*(1-survived)+survived*y*(1-earlier)')
                cycles += 1
            tested += 1
    return {'native_segments': tested, 'nonunit_promotions': remapped,
            'repeated_target_splits': cycles}


if __name__ == '__main__':
    print(json.dumps({'nested': nested_control(), 'native': finite_cap_control()},
                     sort_keys=True, indent=2))
