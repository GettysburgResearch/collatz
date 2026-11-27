"""Steer a fixed positive 3-unit into any ternary class by an ordinary inverse word."""

from dataclasses import dataclass
from math import isqrt


def log_two(unit, precision):
    """Return the canonical log base 2 of a 3-unit modulo 3^precision."""
    if precision < 1 or unit % 3 == 0:
        raise ValueError("expected positive precision and a ternary unit")
    residue = 0 if unit % 3 == 1 else 1
    period = 2
    modulus = 3
    for _ in range(1, precision):
        modulus *= 3
        for digit in range(3):
            trial = residue + digit * period
            if pow(2, trial, modulus) == unit % modulus:
                residue = trial
                break
        else:
            raise ArithmeticError("discrete logarithm lift failed")
        period *= 3
    return residue


@dataclass(frozen=True)
class InverseWord:
    odd_exponents: tuple
    final_doublings: int

    @property
    def clock(self):
        return sum(self.odd_exponents) + self.final_doublings

    def residue(self, source, modulus):
        """Evaluate the physical word modulo a target modulus without giant powers."""
        current_modulus = modulus * 3 ** len(self.odd_exponents)
        value = source % current_modulus
        for exponent in self.odd_exponents:
            if exponent < 1:
                raise ValueError("an inverse odd stage needs a positive exponent")
            numerator = (pow(2, exponent, current_modulus) * value - 1) % current_modulus
            if numerator % 3:
                raise ArithmeticError("illegal odd inverse")
            value = numerator // 3
            current_modulus //= 3
        return value * pow(2, self.final_doublings, current_modulus) % current_modulus

    def ordinary(self, source):
        value = source
        for exponent in self.odd_exponents:
            numerator = (value << exponent) - 1
            if exponent < 1 or numerator % 3:
                raise ArithmeticError("illegal odd inverse")
            value = numerator // 3
        return value << self.final_doublings


def corrected_word(source, target, precision, stages, floor_log=0):
    """Steer a fixed unit into a unit class. floor_log ensures clock >= floor_log."""
    if min(source, precision, stages) < 1 or source % 3 == 0 or target % 3 == 0:
        raise ValueError("expected a positive 3-unit source, unit target and positive sizes")
    total_precision = precision + stages
    coarse = (total_precision + 1) // 2
    fine = total_precision - coarse
    coarse_modulus = 3 ** coarse
    fine_modulus = 3 ** fine
    modulus = coarse_modulus * fine_modulus
    period = 2 * (coarse_modulus // 3)
    # A radix of valuation exactly one, large enough for all fine digits.
    radix = 3 ** ((fine + stages) // (stages + 1))
    if radix % 9 == 0:
        radix += 3
    if radix < 3:
        radix = 3
    scale = target * pow(radix // 3, -stages, coarse_modulus) % coarse_modulus
    desired = [scale * pow(source, -1, coarse_modulus)]
    desired.extend(scale * pow(radix // 3, i, coarse_modulus) * (1 - radix)
                   for i in range(stages))
    residuals = [log_two(value, coarse) for value in desired]
    cumulative = [0] * (stages + 1)
    cumulative[-1] = residuals[-1]
    for i in range(stages - 1, -1, -1):
        gap = (residuals[i] - cumulative[i + 1] - 1) % period + 1
        cumulative[i] = cumulative[i + 1] + gap
    if cumulative[0] < floor_log:
        cumulative[0] += period * ((floor_log - cumulative[0] + period - 1) // period)
    offset = sum(3 ** i * pow(2, cumulative[i + 1], modulus) for i in range(stages))
    baseline = (source * pow(2, cumulative[0], modulus) - offset) % modulus
    error = (3 ** stages * target - baseline) % modulus
    if error % coarse_modulus:
        raise ArithmeticError("incorrect coarse congruence")
    linear_unit = (pow(2, period, modulus) - 1) // coarse_modulus
    correction = error // coarse_modulus * pow(linear_unit * scale, -1, fine_modulus)
    correction %= fine_modulus
    digits = []
    for _ in range(stages + 1):
        correction, digit = divmod(correction, radix)
        digits.append(digit)
    if correction:
        raise ArithmeticError("insufficient radix capacity")
    exponents = tuple(cumulative[i] - cumulative[i + 1] + period * digits[i]
                      for i in range(stages))
    result = InverseWord(exponents, cumulative[-1] + period * digits[-1])
    if result.residue(source, 3 ** precision) != target % (3 ** precision):
        raise ArithmeticError("portal verification failed")
    return result


def odd_word(source, target, precision, stages=None, floor_log=0):
    """Any target class, including a multiple of 3, with an odd ordinary entrance."""
    if stages is None:
        stages = max(1, isqrt(precision + 1))
    modulus = 3 ** (precision + 1)
    intermediate = (3 * target + 1) * pow(2, -1, modulus) % modulus
    word = corrected_word(source, intermediate, precision + 1, stages, floor_log)
    return InverseWord(word.odd_exponents + (word.final_doublings + 1,), 0)
