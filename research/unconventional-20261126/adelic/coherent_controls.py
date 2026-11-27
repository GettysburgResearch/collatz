"""Certified all-physical-phase separation for the coherent-switch construction."""

from fractions import Fraction
from hashlib import sha256
from math import gcd
import json


def check(condition, message):
    if not condition:
        raise AssertionError(message)


def numerator(word):
    value = 0
    for j, bit in enumerate(word):
        if bit:
            value = 3 * value + (1 << j)
    return value


def block_word(length, grade, modulus, target):
    """Choose a fixed-grade, width-eight-block word with the requested residue."""
    initial, deltas = [], []
    for j in range(0, length, 8):
        end = min(j + 8, length)
        before = j * grade // length
        q = end * grade // length - before
        if end - j == 8 and 0 < q < 8:
            initial.extend([1, 0] + [1] * (q - 1) + [0] * (7 - q))
            delta = pow(2, j, modulus) * pow(3, grade - before - 1, modulus) % modulus
            deltas.append((j, delta))
        else:
            initial.extend([1] * q + [0] * (end - j - q))
    if modulus == 1:
        return initial, 0
    wanted = (target - numerator(initial)) % modulus
    previous = {0: None}
    used = 0
    for j, delta in deltas:
        if wanted in previous:
            break
        used += 1
        for old in tuple(previous):
            new = (old + delta) % modulus
            if new not in previous:
                previous[new] = (old, j)
    check(wanted in previous, "available explicit patch did not hit the target")
    while wanted:
        wanted, j = previous[wanted]
        initial[j:j + 2] = [0, 1]
    check(numerator(initial) % modulus == target % modulus, "patched carry")
    return initial, used


def trial(m, q, length, grade, r, t, primes, require_spacing=True):
    check(gcd(m, q) == 1 and m > 2 * length, "global clock and grade")
    A, B = 3**q, 1 << m
    D = B - A
    n = m * r * t
    local = 1
    for prime in primes:
        power = prime
        while (pow(2, n, power) - pow(3, q * r * t, power)) % power == 0:
            local *= prime
            power *= prime
    wtarget = (3**(grade - 1) - (1 << (length - 1))) * pow(4, -1, local) % local
    inner, wp = block_word(length - 2, grade - 1, local, wtarget)
    U, V = [1] + inner + [0], [0] + inner + [1]
    inc = numerator(V) - numerator(U)
    check(inc == 4 * numerator(inner) + (1 << (length - 1)) - 3**(grade - 1), "coherent gain")
    check(inc > 0 and inc % local == 0, "switch gain reduction")
    rest_grade = q - 2 * grade
    uucarry = numerator(U + U) * 3**rest_grade
    vtarget = -uucarry * pow(2**(2 * length), -1, local) % local
    tail, vp = block_word(m - 2 * length, rest_grade, local, vtarget)
    words = {}
    for e in range(2):
        for f in range(2):
            words[e, f] = (V if e else U) + (V if f else U) + tail
    c0 = numerator(words[0, 0])
    c1 = numerator(words[1, 0]) - c0
    c2 = numerator(words[0, 1]) - c0
    check(c0 % local == 0 and numerator(words[1, 1]) == c0 + c1 + c2, "four native maps")
    check(c1 * 2**length == c2 * 3**grade, "exact gain ratio")
    x = Fraction(c0, D) + Fraction(c1 * A**(r-1), B**r - A**r) + Fraction(c2 * A**(t-1), B**t - A**t)
    den = x.denominator
    check(den > 1 and all(den % prime for prime in primes), "reduced denominator and local sieve")
    check(den.bit_length() <= m * (r+t), "subperiod denominator bound")
    # The full native word is certified at all its phases by the cyclic affine
    # identity. Also verify arrow parity along every full reduced numerator lap.
    # The rational enclosures below certify real spacing without storing those numerators.
    scale = 1 << 96
    floor = x.numerator * scale // den
    ceil = -(-x.numerator * scale // den)
    start_lower, start_upper = floor, ceil
    lower = []
    max_width = 0
    state = x.numerator
    for j in range(r * t):
        for bit in words[int(j % r == 0), int(j % t == 0)]:
            lower.append(floor)
            max_width = max(max_width, ceil - floor)
            check(state & 1 == bit, "native parity")
            state = (3 * state + den) >> 1 if bit else state >> 1
            if bit:
                floor, ceil = (3 * floor + scale) // 2, (3 * ceil + scale + 1) // 2
            else:
                floor, ceil = floor // 2, (ceil + 1) // 2
    check(floor <= start_lower <= start_upper <= ceil and len(lower) == n, "outward enclosure closed")
    check(state == x.numerator, "actual reduced orbit closed")
    lower.sort()
    min_gap = min((b - a) for a, b in zip(lower, lower[1:])) - max_width
    if require_spacing:
        check(min_gap >= scale, "unit-spacing certificate failed")
    return dict(macro_clock=m, macro_grade=q, motif_clock=length, motif_grade=grade,
                tracks=[r,t], least_period=n, full_local_prime_power_product=local,
                tested_primes=primes, inner_patch_blocks=wp, remainder_patch_blocks=vp,
                phase_minimum_floor=lower[0] // scale,
                minimum_pairwise_gap_floor=min_gap // scale,
                certified_gap_millionths=min_gap * 1000000 // scale,
                outward_interval_fractional_bits=96, maximum_interval_width_scaled=max_width,
                evaluated_all_phases=len(lower), direct_native_integer_steps=n,
                reduced_denominator_bits=den.bit_length(),
                reduced_denominator_sha256=sha256(den.to_bytes((den.bit_length()+7)//8, 'big')).hexdigest())


if __name__ == '__main__':
    cases = [(485,306,170,107,3,5,[31]), (24727,15601,1054,665,5,7,[5,71])]
    print(json.dumps([trial(*case) for case in cases], indent=2, sort_keys=True))
