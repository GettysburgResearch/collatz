"""Exact finite certificate for two adjacent reduced ramp cores at most 1000."""
from collections import Counter
from hashlib import sha256
from math import gcd
import json
CORE_LIMIT = 1000
EXPONENT_LIMIT = 10 ** 40
FIRST_BITS = 200
SECOND_BITS = 300
FINITE_CUTOFF = 510

def positive_discrete_log(target, bits, powers):
    """Least positive a such that 3^a = target mod 2^bits, or None."""
    target %= 1 << bits
    if target % 8 not in (1, 3):
        return None
    exponent = 0 if target % 8 == 1 else 1
    current = 1 if exponent == 0 else 3
    mask = (1 << bits) - 1
    for depth in range(3, bits):
        if current - target >> depth & 1:
            current = current * powers[depth - 2] & mask
            exponent += 1 << depth - 2
    if not (current == target and pow(3, exponent, mask + 1) == target):
        raise ValueError('Certificate failed: current == target and pow(3, exponent, mask + 1) == target')
    return exponent or 1 << bits - 2

def powers_of_three(bits):
    modulus = 1 << bits
    powers = [3]
    for _ in range(1, bits):
        powers.append(powers[-1] * powers[-1] % modulus)
    for depth in range(3, bits + 1):
        if not (powers[depth - 2] - 1) % (1 << depth) == 0:
            raise ValueError('Certificate failed: (powers[depth - 2] - 1) % (1 << depth) == 0')
        if not ((powers[depth - 2] - 1) % (1 << depth + 1) != 0 or depth == bits):
            raise ValueError('Certificate failed: (powers[depth - 2] - 1) % (1 << depth + 1) != 0 or depth == bits')
    return powers

def split_power(n, prime):
    exponent = 0
    while n % prime == 0:
        n //= prime
        exponent += 1
    return (exponent, n)

def next_step(n):
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2

def main():
    bases = [n for n in range(1, CORE_LIMIT + 1) if gcd(n, 6) == 1]
    power = powers_of_three(SECOND_BITS)
    for bits in range(3, 12):
        modulus = 1 << bits
        expected = {}
        for a in range(1, (modulus >> 2) + 1):
            expected[pow(3, a, modulus)] = a
        for target in range(1, modulus, 2):
            if not positive_discrete_log(target, bits, power) == expected.get(target):
                raise ValueError('Certificate failed: positive_discrete_log(target, bits, power) == expected.get(target)')
    first_admissible = []
    second_admissible = 0
    min_second = None
    for beta in bases:
        inv = pow(beta, -1, 1 << SECOND_BITS)
        first = positive_discrete_log(inv, FIRST_BITS, power)
        if first is not None:
            if not first > EXPONENT_LIMIT:
                raise ValueError('Certificate failed: first > EXPONENT_LIMIT')
            first_admissible.append(first)
        for f in range(1, FIRST_BITS):
            value = positive_discrete_log((1 - (1 << f)) * inv, SECOND_BITS, power)
            if value is not None:
                if not value > EXPONENT_LIMIT:
                    raise ValueError('Certificate failed: value > EXPONENT_LIMIT')
                second_admissible += 1
                min_second = value if min_second is None else min(min_second, value)
    rows = []
    largest_start = (0, 0, 0)
    max_steps = 0
    maxima_by_A = Counter()
    class_one = []
    physical_starts = 0
    for beta in bases:
        power_three = 1
        for A in range(1, FINITE_CUTOFF + 1):
            power_three *= 3
            f, successor = split_power(power_three * beta - 1, 2)
            sp, odd = split_power(successor + 1, 2)
            hp, beta_next = split_power(odd, 3)
            if beta_next > CORE_LIMIT:
                continue
            z = successor
            clock = 0
            while z != 1:
                z = next_step(z)
                clock += 1
                if not clock < 10000:
                    raise ValueError('Certificate failed: clock < 10000')
            if not 3 ** A * beta + 2 ** f - 1 == 2 ** (f + sp) * 3 ** hp * beta_next:
                raise ValueError('Certificate failed: 3 ** A * beta + 2 ** f - 1 == 2 ** (f + sp) * 3 ** hp * beta_next')
            rows.append((beta, A, f, sp, hp, beta_next, successor, clock))
            maxima_by_A[A] += 1
            if beta == 1 and beta_next == 1:
                class_one.append(A)
            for s in range(1, A + 1):
                h = A - s
                initial = 2 ** s * 3 ** h * beta - 1
                actual = initial
                for _ in range(s):
                    if not actual % 2 == 1:
                        raise ValueError('Certificate failed: actual % 2 == 1')
                    actual = next_step(actual)
                for _ in range(f):
                    if not actual % 2 == 0:
                        raise ValueError('Certificate failed: actual % 2 == 0')
                    actual = next_step(actual)
                if not actual == successor:
                    raise ValueError('Certificate failed: actual == successor')
                physical_starts += 1
                largest_start = max(largest_start, (initial, A, beta))
                max_steps = max(max_steps, s + f + clock)
    if not class_one == [1, 2, 4]:
        raise ValueError('Certificate failed: class_one == [1, 2, 4]')
    if not (len(rows) == 1094 and max((row[1] for row in rows)) == 12):
        raise ValueError('Certificate failed: len(rows) == 1094 and max((row[1] for row in rows)) == 12')
    print(json.dumps({'core_limit': CORE_LIMIT, 'global_exponent_limit': EXPONENT_LIMIT, 'first_bits': FIRST_BITS, 'second_bits': SECOND_BITS, 'reduced_bases': len(bases), 'first_solvable_classes': len(first_admissible), 'first_minimum_positive_exponent': min(first_admissible), 'second_solvable_classes': second_admissible, 'second_minimum_positive_exponent': min_second, 'finite_exponents_checked': FINITE_CUTOFF, 'transition_rows': len(rows), 'rows_by_A': dict(sorted(maxima_by_A.items())), 'core_one_to_core_one_exponents': class_one, 'physical_odd_starts': physical_starts, 'largest_start_with_A_and_beta': largest_start, 'largest_next_odd': max((row[6] for row in rows)), 'max_certified_shortcut_length_via_next_odd': max_steps, 'sorted_transition_rows_sha256': sha256(json.dumps(sorted(rows), separators=(',', ':')).encode()).hexdigest()}, indent=2))
if __name__ == '__main__':
    main()
