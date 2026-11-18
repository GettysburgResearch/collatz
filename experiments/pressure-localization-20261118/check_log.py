"""Replay the signed log-slope sums by raw parity, with an exact loss test."""
import argparse
import json
from fractions import Fraction
from pathlib import Path


def states(source, clocks):
    n = source
    raw = 0
    for _ in range(clocks):
        yield n, raw
        n = (3 * n + 1) // 2
        raw += 1
        while n % 2 == 0:
            n //= 2
            raw += 1


def check_loss():
    # Stronger rational check: round H/E down before exponentiation.
    horizon = 50
    energy = [Fraction(0)] * horizon
    signed = [Fraction(0)] * horizon
    for source in range(1, 128, 2):
        for j, (n, raw) in enumerate(states(source, horizon)):
            weight = Fraction(3 ** (2 * j), (n << raw) ** 2)
            energy[j] += weight
            signed[j] += weight * ((3 ** j).bit_length() - 1 - raw)
    for j in range(horizon - 1):
        mean = signed[j] / energy[j]
        exponent = mean.numerator // mean.denominator
        majorant = Fraction(7, 288) * energy[j] ** 2 * Fraction(2) ** (-exponent)
        if energy[j] - energy[j + 1] < majorant:
            raise ValueError(f"rational loss test failed at {j}")


def check(receipt):
    cutoff = receipt["cutoff"]
    scale = 1 << receipt["fraction_bits"]
    clocks = sorted(row["clock_count"] for row in receipt["rows"])
    horizon = clocks[-1]
    energy = [0] * horizon
    signed = [0] * horizon
    powers = [3 ** j for j in range(horizon)]
    for source in range(1, cutoff + 1, 2):
        for j, (n, raw) in enumerate(states(source, horizon)):
            # At eight extra bits, truncation then shifting reproduces each
            # signed floor in the original precision, including negative hits.
            numerator = scale * 256 * powers[j] ** 2
            denominator = (n << raw) ** 2
            energy[j] += (numerator // denominator) >> 8
            signed[j] += ((numerator * (powers[j].bit_length() - 1 - raw))
                          // denominator) >> 8
    count = (cutoff + 1) // 2
    for row in receipt["rows"]:
        q = row["clock_count"]
        energy_low = sum(energy[:q])
        slope_sum = sum(signed[:q])
        energy_high = energy_low + q * count - (-q * scale // (2 * (cutoff + 1)))
        slope_low = slope_sum + (-q * ((cutoff - 1).bit_length() + 4) * scale // cutoff)
        slope_high = slope_sum + q * count - (-q * (q - 1) * scale // (4 * (cutoff + 1)))
        expected = [energy_low, energy_high, slope_low, slope_high]
        observed = [row[k] for k in ("energy_sum_lower", "energy_sum_upper",
                                     "slope_sum_lower", "slope_sum_upper")]
        if expected != observed:
            raise ValueError(f"log trace mismatch at {q}")
    check_loss()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("receipt", type=Path)
    args = parser.parse_args()
    check(json.loads(args.receipt.read_text()))
    print("Verified the signed trace and 49 strengthened finite-bank loss bounds")
