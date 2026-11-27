"""Integer controls for cyclic clock differences and their complete denominator.

Run identically with python -B or python -O -B. No sampled case proves an
asymptotic estimate or substitutes for its external Diophantine input.
"""

from collections import Counter
from hashlib import sha256
from itertools import accumulate, product
from math import gcd
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def clocks(gaps):
    return [0, *accumulate(gaps)]


def carry_and_divisor(gaps):
    p = len(gaps)
    dates = clocks(gaps)
    a = dates[-1]
    numerator = sum((3 ** (p - 1 - i)) << dates[i] for i in range(p))
    divisor = 2**a - 3**p
    require(divisor > 0, "positive word required")
    return numerator, divisor


def direct_replay(gaps, carry, determinant):
    common = gcd(carry, determinant)
    reduced = determinant // common
    first = carry // common
    point = first
    seen = set()
    for gap in gaps:
        require(point % 2 == 1 and gcd(point, reduced) == 1, "nonprimitive odd phase")
        seen.add(point)
        offset = 3 * point + reduced
        require(offset % (1 << gap) == 0 and (offset >> gap) % 2 == 1, "odd gap")
        point = offset >> gap
    require(point == first, "failed cyclic replay")
    return len(seen)


def cut(gaps, v, u, windows):
    p = len(gaps)
    exceptional = [i for i, clock in enumerate(windows) if clock != u]
    spacings = [(i - exceptional[j - 1]) % p or p for j, i in enumerate(exceptional)]
    height = max(spacings)
    origin = exceptional[spacings.index(height)]
    rotated = gaps[origin:] + gaps[:origin]
    cut_rows = sorted((i - origin) % p for i in exceptional)
    require(cut_rows[0] == 0 and cut_rows[-1] == p - height, "largest cyclic gap")
    dts = clocks(rotated + rotated)
    b0 = dts[v]
    m0 = min(b0, u)
    result = 0
    valuations = []
    for i in cut_rows:
        b = dts[i + v] - dts[i]
        valuation = dts[i] + min(u, b) - m0
        sign = 1 if u > b else -1
        core = ((1 << abs(u - b)) - 1) * sign
        integer = (3 ** (p - height - i)) * (core << valuation)
        result += integer
        valuations.append(valuation)
    require(valuations[0] == 0 and all(x < y for x, y in zip(valuations, valuations[1:])),
            "dyadic valuations must strictly rise")
    require(result % 2 == 1, "cut residual must be odd")
    return height, result, cut_rows, dts


def check_one(word, v, u, windows, carry, determinant, counts):
    p = len(word)
    a = sum(word)
    common = gcd(determinant, carry)
    m = sum(j != u for j in windows)
    require(0 < m <= p, "nonempty exception support")
    h, residual, rows, dts = cut(word, v, u, windows)
    require(residual % common == 0, "complete gcd divides signed integer residual")
    spread_values = [p * dts[i] - a * i for i in range(p)]
    wp = max(spread_values) - min(spread_values)
    separation = abs(p * u - a * v)
    power_exponent = a * (p - h) + wp + separation
    require(pow(abs(residual), p) <= pow(m, p) * 2**power_exponent,
            "exact integer form of the m-term size bound")

    # Check the cyclic congruence independently in chronological order,
    # without rotating or extracting the head valuation.
    if determinant > 1:
        inverse_three = pow(3, -1, determinant)
        dates = clocks(word)
        left = (pow(2, u, determinant) * pow(inverse_three, v, determinant) - 1)
        left *= pow(inverse_three, p - 1, determinant) * carry
        right = sum((pow(2, u, determinant) - pow(2, b, determinant))
                    * pow(2, dates[i], determinant) * pow(inverse_three, i + v, determinant)
                    for i, b in enumerate(windows) if b != u)
        require((left - right) % determinant == 0, "cyclic difference modulo determinant")

    counts["windows"] += 1
    counts["one_sided" if u in (min(windows), max(windows)) else "mixed"] += 1
    counts["nonresonant" if separation else "resonant"] += 1
    counts["coprime_window" if gcd(a, p) == 1 else "noncoprime_window"] += 1
    counts["negative_residual" if residual < 0 else "positive_residual"] += 1
    if m == 1:
        counts["single_exception"] += 1
        require(separation == abs(windows[next(i for i, c in enumerate(windows) if c != u)] - u),
                "single difference")
        require((2**separation - 1) % common == 0 and 2**separation - 1 < determinant,
                "all-period exclusion at one exceptional window")


def is_primitive(word):
    p = len(word)
    return all(any(word[i] != word[(i + j) % p] for i in range(p)) for j in range(1, p))


def small_words():
    counts = Counter()
    for p in range(2, 9):
        for word in product((1, 2, 3), repeat=p):
            if 2**sum(word) <= 3**p or not is_primitive(word):
                continue
            if word != min(word[i:] + word[:i] for i in range(p)):
                continue
            carry, determinant = carry_and_divisor(word)
            require(direct_replay(word, carry, determinant) == p, "least rational period")
            counts["primitive_rational_cycles"] += 1
            twice_dates = clocks(word + word)
            a = twice_dates[p]
            g = gcd(a, p)
            s = p // g
            for v in range(1, p):
                windows = [twice_dates[i + v] - twice_dates[i] for i in range(p)]
                if len(set(windows)) > 1:
                    for u in sorted(set(windows)):
                        check_one(word, v, u, windows, carry, determinant, counts)
                if s >= 2 and gcd(v, p) == 1 and (a // g * v + 1) % s == 0:
                    k = [twice_dates[i] - ((a * i + p - 1) // p) for i in range(p)]
                    jumps = sum(k[i] != k[(i + v) % p] for i in range(p))
                    u = (a // g * v + 1) // s
                    require(sum(b != u for b in windows) <= jumps + g, "seams and jumps")
                    require(max(k) - min(k) <= (max(1, jumps) - 1) * ((a+p-1)//p - 1),
                            "level graph range")
                    counts["unit_lift_checks"] += 1
    return dict(sorted(counts.items()))


def two_switch(q, r, a, b):
    n = q * r
    bits = []
    block_carries = {}
    for j in range(n):
        labels = (int(j % q == 0), int(j % r == 0))
        block = sum(([1-bit, bit] for bit in labels), []) + [1]*(a-2) + [0]*(b-a-2)
        bits.extend(block)
        carry = 0
        for time, bit in enumerate(block):
            if bit:
                carry = 3 * carry + 2**time
        block_carries[labels] = carry
    dates = [i for i, bit in enumerate(bits) if bit]
    gaps = tuple(dates[j+1]-dates[j] for j in range(len(dates)-1)) + (len(bits)-dates[-1]+dates[0],)
    carry, determinant = carry_and_divisor(gaps)
    period = direct_replay(gaps, carry, determinant)
    require(period == a * n, "two-switch least period")
    low = block_carries[0,0]
    left = block_carries[1,0]-low
    right = block_carries[0,1]-low
    require(block_carries[1,1] == low + left + right, "two independent carry changes")
    p0 = 3**a
    q0 = 2**b
    common_block = q0 - p0
    phi_q = (q0**q - p0**q) // common_block
    phi_r = (q0**r - p0**r) // common_block
    require(gcd(phi_q, phi_r) == 1, "distinct prime block factors")
    require((low, left, right) ==
            (23*3**(a-2) - 4*2**a, 3**(a-1), 4*3**(a-2)), "symbolic block offsets")
    numerator = low * phi_q * phi_r + left * p0**(q-1) * phi_r + right * p0**(r-1) * phi_q
    require(gcd(numerator, phi_q * phi_r) == 1, "whole nontrivial prime factors survive")
    base_numerator = q*r*low + r*left + q*right
    binary_residual = (23*q*r+3*r+4*q) * 2**b - (36*q*r) * 2**a
    require((9*base_numerator - binary_residual) % common_block == 0,
            "width-zero residual modulo the reduced block clock")
    require(gcd(common_block, numerator) == gcd(common_block, binary_residual),
            "exact base-factor gcd")
    predicted = common_block * phi_q * phi_r // gcd(common_block, binary_residual)
    reduced = determinant // gcd(determinant, carry)
    require(reduced == predicted and reduced > 1, "exact two-switch denominator")

    lag_blocks = r * pow(r, -1, q)
    lag = a * lag_blocks
    width = b * lag_blocks
    doubled_dates = clocks(gaps + gaps)
    exceptional = [i for i in range(period) if doubled_dates[i+lag] - doubled_dates[i] != width]
    spacings = [(i - exceptional[j-1]) % period for j, i in enumerate(exceptional)]
    require(len(exceptional) == 2*r and max(spacings) == a*(q-1),
            "fixed-support resonant sharpness")
    exceptions = sum(gap != 1 for gap in gaps)
    require(0 < exceptions <= 3*n, "growing one-sided test")
    magnitude = reduced.to_bytes((reduced.bit_length()+7)//8, "big")
    dts = clocks(gaps)
    discrepancy = [period*dts[i] - len(bits)*i for i in range(period)]
    return {"q":q,"r":r,"a":a,"b":b,"native_period":len(bits),"odd_period":period,
            "clock_gcd":gcd(len(bits),period),
            "resonant_exception_count":len(exceptional),"resonant_largest_spacing":max(spacings),
            "predicted_limit_numerator":q+r-1,"predicted_limit_denominator":q*r,"exceptions_at_unit_lag":exceptions,
            "discrepancy_span_times_odd_period":max(discrepancy)-min(discrepancy),
            "whole_denominator_bits":determinant.bit_length(), "reduced_denominator_bits":reduced.bit_length(),
            "reduced_denominator_sha256_unsigned_big_endian":sha256(magnitude).hexdigest()}


def main():
    return {"compact":small_words(), "two_switch":[two_switch(5,7,41,65),two_switch(5,11,41,65)]}


if __name__ == "__main__":
    print(json.dumps(main(), sort_keys=True, indent=2))
