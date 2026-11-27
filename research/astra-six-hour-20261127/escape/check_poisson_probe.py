"""Check the binary Poisson formula against signed integer orbit sums.

The seed is exp(4*pi*i*(u-a))*sinc((u-a)/2)^4. The Fourier density is the
fourfold convolution of the uniform density on [-1/4,1/4], translated by 2.
Each numerical column is independently truncated under the stated bounds.
"""

import itertools
import math

import numpy as np


def multiplier(k, x):
    clock = 0
    for _ in range(k):
        z = 3 * x + 1
        gap = (z & -z).bit_length() - 1
        x = z >> gap
        clock += gap
    return 3**k / 2**clock


def sources(k, d):
    """Enumerate fixed-total words via their forward proper prefix sums."""
    q = 3**k
    modulus = 2 ** (d + 1)
    inverse = pow(q, -1, modulus)
    for cuts in itertools.combinations(range(1, d), k - 1):
        starts = (0, *cuts)
        carry = sum(3 ** (k - j - 1) * 2**n for j, n in enumerate(starts))
        x = ((2**d - carry) * inverse) % modulus
        z = x
        for n, end in zip(starts, (*cuts, d)):
            value = 3 * z + 1
            gap = (value & -value).bit_length() - 1
            if gap != end - n:
                raise ArithmeticError("binary source failed actual gap replay")
            z = value >> gap
        yield x


def density(x):
    # Reflect about the center to avoid cancellation near the right endpoint.
    u = 1 - np.abs(x)
    return (8 / 3) * (np.maximum(u, 0) ** 3 - 4 * np.maximum(u - 0.5, 0) ** 3)


def frequency_row(k, a, t):
    q = 3**k
    total = 0j
    d = k
    while t * 2**d < 16 * q:
        modulus = 2 ** (d + 1)
        indicator = np.zeros(modulus)
        for x in sources(k, d):
            if indicator[x]:
                raise ArithmeticError("different words share a binary source")
            indicator[x] = 1
        normalized = np.fft.ifft(indicator)
        ell = np.arange(modulus, 3 * modulus + 1)
        xi = ell / modulus
        factors = density(xi - 2) * np.exp(-math.pi * t * ell / q)
        factors = factors * np.exp(-2j * math.pi * a * xi)
        # The normalized inverse FFT supplies 1/modulus, while (6) uses
        # pi/2 * 2^(-d), hence the remaining factor is pi.
        total += math.pi * np.sum(normalized[ell % modulus] * factors)
        d += 1
    # Each width-d row has at most 2*modulus+1 modes of density <=2.
    # In (6) each individual coefficient-sum has absolute value <=2^d.
    # The ratio of successive first-omitted bounds is <=2*exp(-32*pi).
    tail = 12 * math.pi * 2**d * math.exp(-2 * math.pi * t * 2**d / q)
    return total, tail


def ordinary_row(k, a, t, limit):
    total = 0j
    for x in range(-limit + 1, limit, 2):
        width = t / multiplier(k, x)
        numerator = math.exp(-2 * math.pi * width) * math.expm1(-math.pi * width) ** 4
        total += numerator / (math.pi**3 * (x - a + 1j * width) ** 4)
    # Sum both signed tails over all integers, using |numerator| <= 1.
    tail = 2 / (3 * math.pi**3 * (limit - abs(a)) ** 3)
    return total, tail


def main():
    print("depth\tsource\twidth\treal\timaginary\tabsolute_difference\ttruncation_bound")
    for k in range(1, 6):
        for a, t in [(-1, 0.75), (1, 0.75), (3, 1.0), (27, 1.0)]:
            lhs, err1 = frequency_row(k, a, t)
            rhs, err2 = ordinary_row(k, a, t, 2048)
            err = abs(lhs - rhs)
            if err > err1 + err2 + 2e-13:
                raise ArithmeticError(f"Poisson disagreement at {k=} {a=} {t=}: {err}")
            print(f"{k}\t{a}\t{t}\t{lhs.real:.11g}\t{lhs.imag:.11g}\t{err:.3e}\t{err1 + err2:.3e}")


if __name__ == "__main__":
    main()
