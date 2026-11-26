"""Exact finite controls for physical affine rows and prime-adic closing matches."""

import itertools
import json
import math
from fractions import Fraction


def require(condition, description):
    if not condition:
        raise AssertionError(description)


def shortcut(q):
    return (3 * q + 1) // 2 if q % 2 else q // 2


def form(bits):
    carry = 0
    odd_count = 0
    for j, bit in enumerate(bits):
        if bit:
            carry = 3 * carry + 2**j
            odd_count += 1
    return len(bits), odd_count, carry


def closure(row):
    length, count, carry = row
    return Fraction(carry, 2**length - 3**count)


def floor_log(n, base):
    if base == 2:
        return n.bit_length() - 1
    k = 0
    while n >= base:
        k += 1
        n //= base
    return k


def prime_part(x, p):
    require(x, "nonzero valuation input")
    x = abs(x)
    power = 1
    while x % p == 0:
        power *= p
        x //= p
    return power


def population_certificate():
    length = 1536
    clock = (3**length).bit_length() - 1
    require(clock == 2434, "block clock")
    count = math.comb(clock - 1, length - 1) // length
    require(count**50 > 3**(47 * length), "integer binomial lower bound")
    require(2**100 > 3**63, "binary entropy exponent")
    return {"block_length": length, "total_clock": clock,
            "rotation_lower_bound_bits": count.bit_length(),
            "count_exceeds_three_power_47L_over_50": True}


def words():
    tested = 0
    equal = 0
    one_zero = 0
    for length in range(1, 13):
        for bits in itertools.product((0, 1), repeat=length):
            s, p, carry = form(bits)
            bound = 2**(s - p) * (3**p - 2**p)
            require(carry <= bound, "carry envelope")
            require((carry == bound) == (tuple(sorted(bits)) == bits), "carry extremizers")
            phase = closure((s, p, carry))
            require(2**s * phase == 3**p * phase + carry, "rational closure")
            tested += 1
            if p == length - 1 and length > 1:
                r = length - 1 - bits.index(0)
                require(phase + 1 == Fraction(2**(length-r-1) * 3**r, 2**length - 3**p), "single-even identity")
                require(phase.denominator == abs(2**length - 3**p), "single-even denominator")
                one_zero += 1
            equal += carry == bound
    return {"words": tested, "carry_envelope_equalities": equal, "one_zero": one_zero}


def path(seed, length):
    states = [seed]
    for _ in range(length):
        states.append(shortcut(states[-1]))
    return states


def windows():
    rows = 0
    endpoint_pairs = 0
    zero_shifts = 0
    directed_nonzero = 0
    centers = ((1, -1, -1), (5, -3, 17), (7, 13, -5), (1, 0, 0))
    for seed in itertools.chain(range(1, 600, 2), (2**25 - 1, 3**35 - 2)):
        states = path(seed, 112)
        bits = [q % 2 for q in states[:-1]]
        for j in range(0, 101, 4):
            for length in (1, 3, 5, 9):
                s, p, carry = form(bits[j : j + length])
                x, y = states[j], states[j + length]
                require(2**s * y == 3**p * x + carry, "physical row")
                phase = closure((s, p, carry))
                earlier = phase.denominator * x - phase.numerator
                later = phase.denominator * y - phase.numerator
                require(earlier % 2**s == 0, "initial dyadic match")
                require(later % 3**p == 0, "terminal ternary match")
                require(earlier // 2**s == later // 3**p, "transported closure quotient")
                endpoint_pairs += 1
                for d, a, b in centers:
                    A, B = d * x - a, d * y - b
                    U, V = 2**s * B, 3**p * A
                    E = d * carry + 3**p * a - 2**s * b
                    require(U - V == E, "shifted carry")
                    if E == 0:
                        require(A % 2**s == B % 3**p == 0, "zero carry divisibility")
                        require(A // 2**s == B // 3**p, "zero carry quotient")
                        zero_shifts += 1
                    if A and B:
                        require(prime_part(U, 2) * prime_part(V, 3) == (
                            2**s * 3**p * prime_part(B, 2) * prime_part(A, 3)
                        ), "directed prime parts")
                        directed_nonzero += 1
                    rows += 1
    return {"shifted_rows": rows, "closing_endpoint_pairs": endpoint_pairs,
            "exact_zero_shifts": zero_shifts, "nonzero_directed_pairs": directed_nonzero}


def neighbor_closings():
    tested = 0
    equal_phases = 0
    sample = None
    seeds = list(range(1, 700, 2)) + [2**k - 1 for k in (24, 48, 80, 120, 180)]
    for seed in seeds:
        states = path(seed, max(180, 5 * seed.bit_length()))
        bits = [q % 2 for q in states[:-1]]
        odd_times = [j for j, bit in enumerate(bits) if bit]
        for i, j in enumerate(odd_times):
            q = states[j]
            b, h = floor_log(q, 3), floor_log(q, 2)
            if not (0 < b <= i and h > 0 and j + h < len(states)):
                continue
            left = closure(form(bits[odd_times[i - b] : j]))
            right = closure(form(bits[j : j + h]))
            common = math.lcm(left.denominator, right.denominator)
            U, V = common * (q - right), common * (q - left)
            require(U.denominator == V.denominator == 1, "integral centered pair")
            require(U.numerator % 2**h == V.numerator % 3**b == 0, "bilateral local match")
            require(U - V == common * (left - right), "difference of closures")
            require(math.gcd(common, 6) == 1, "closing common denominator")
            if left == right:
                require(U.numerator % (2**h * 3**b) == 0, "coincident phases")
                equal_phases += 1
            tested += 1
            if left == -1 and q + 1 == 2 * 3**b:
                case = {"odd_center": q, "past_odd_count": b, "future_bits": h,
                        "past_denominator": left.denominator,
                        "future_denominator": right.denominator}
                if sample is None or q > sample["odd_center"]:
                    sample = case
    require(sample is not None and sample["past_odd_count"] == 179, "long rise example")
    return {"windows": tested, "equal_phase_windows": equal_phases, "fixed_rise_example": sample}


if __name__ == "__main__":
    print(json.dumps({"population_certificate": population_certificate(), "word_controls": words(), "path_controls": windows(),
                      "forced_closings": neighbor_closings()}, indent=2))
