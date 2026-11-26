#!/usr/bin/env python3
"""Independent finite checks of switching cycles and actual ordinary resets.

No primary construction code is imported. Cycle carries are recovered from
composed rational affine maps. These checks do not prove an asymptotic bound.
"""

from fractions import Fraction
from math import gcd
import hashlib
import json


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def valuation_two(n):
    require(n > 0, "valuation input")
    return (n & -n).bit_length() - 1


def affine_cycle(gaps):
    multiplier, offset = Fraction(1), Fraction(0)
    for e in gaps:
        multiplier = 3 * multiplier / (1 << e)
        offset = (3 * offset + 1) / (1 << e)
    fixed = offset / (1 - multiplier)
    divisor = (1 << sum(gaps)) - 3 ** len(gaps)
    carry = fixed * divisor
    require(carry.denominator == 1, "nonintegral recovered carry")
    if divisor > 0:
        state, seen = fixed, set()
        for e in gaps:
            require(state > 0 and state.numerator % 2, "nonphysical odd phase")
            require(state not in seen, "repeated phase before full period")
            seen.add(state)
            lifted = 3 * state.numerator + state.denominator
            require(valuation_two(lifted) == e, "incorrect true valuation")
            state = (3 * state + 1) / (1 << e)
            require(state.denominator == fixed.denominator, "denominator changed")
        require(state == fixed, "cycle did not return")
    return carry.numerator, divisor > 0


def switching_controls():
    words = positive = comparisons = 0
    for period in range(11, 25):
        for total in range(3 * period // 2 + 1, 2 * period):
            dates = [(i * total + period - 1) // period for i in range(period + 1)]
            gaps = [b - a for a, b in zip(dates, dates[1:])]
            marker = next(i for i in range(period) if gaps[i - 1] == gaps[i] == 2)
            start = (marker - 1) % period
            gaps = gaps[start:] + gaps[:start]
            choices = [i for i in range(1, period)
                       if (gaps[i - 1], gaps[i]) == (1, 2)]
            gaps[0], gaps[1] = 3, 1
            moduli = [m for m in range(2, 2 * period - total + 1) if gcd(m, 6) == 1]
            if not moduli:
                continue
            attained = {m: set() for m in moduli}
            for mask in range(1 << len(choices)):
                changed = gaps.copy()
                for j, i in enumerate(choices):
                    if mask >> j & 1:
                        changed[i - 1], changed[i] = 2, 1
                require(sum(changed) == total and changed.count(3) == 1, "marker destroyed")
                carry, is_positive = affine_cycle(changed)
                words += 1
                positive += is_positive
                for modulus in moduli:
                    attained[modulus].add(carry % modulus)
            for modulus, residues in attained.items():
                require(residues == set(range(modulus)), "missing independent carry residue")
                comparisons += 1
    return {"rational_affine_words": words, "positive_primitive_cycles": positive,
            "complete_modular_images": comparisons}


def reset_controls():
    blocks = protected = 0
    for source in range(1, 20000, 2):
        y = source + 1
        t = valuation_two(y)
        odd = y >> t
        b = valuation_two(3 ** t * odd - 1)
        terminal = (3 ** t * odd - 1) >> b
        common = gcd(odd, terminal + 1)
        require(common == gcd(odd, (1 << b) - 1), "odd common divisor mismatch")
        require(terminal ** 5 * common ** 8 < y ** 8, "integer power bound failed")
        state = source
        for j in range(t):
            exponent = valuation_two(3 * state + 1)
            require(exponent == (1 if j + 1 < t else b + 1), "reset location mismatch")
            state = (3 * state + 1) >> exponent
        require(state == terminal, "incorrect complete-block endpoint")
        blocks += 1
        protected += terminal >= y
    examples = []
    for b in range(3, 104, 10):
        t = 1
        while 3 ** t <= 1 << (t + b):
            t += 1
        t += 1
        modulus = 1 << (b + 1)
        retained = (1 << b) - 1
        residue = ((1 << b) + 1) * pow(3 ** t * retained, -1, modulus) % modulus
        u = residue + modulus
        while u % 3 != pow(pow(2, t, 3), -1, 3):
            u += modulus
        odd = retained * u
        y = (1 << t) * odd
        numerator = 3 ** t * odd - 1
        require(valuation_two(numerator) == b, "sharp example reset exponent")
        terminal = numerator >> b
        require(terminal > y and (y - 1) % 3 == 0, "sharp example lost protected floor")
        require(gcd(odd, terminal + 1) == retained, "sharp example retained gcd")
        examples.append({"reset_extra_exponent": b, "block_steps": t,
                         "source_bits": (y - 1).bit_length(),
                         "retained_bits": retained.bit_length(),
                         "source_sha256": hashlib.sha256(str(y - 1).encode()).hexdigest()})
    return {"ordinary_blocks": blocks, "blocks_finishing_above_shifted_source": protected,
            "sharp_profile_examples": examples}


if __name__ == "__main__":
    print(json.dumps({"switching": switching_controls(), "resets": reset_controls(),
                      "scope": "finite interfaces and examples; no asymptotic theorem verification"}, indent=2))
