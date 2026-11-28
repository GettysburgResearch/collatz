"""Exact finite checks for the one-sided parity slice and its boundary flux."""

from functools import cache
from math import comb

FERMAT_PRIME = 65537
GENERATOR = 3


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def trajectory(start, steps):
    x = start
    word = []
    for _ in range(steps):
        bit = x % 2
        word.append(bit)
        x = (3 * x + 1) // 2 if bit else x // 2
    return x, word


def canonical_source(word):
    modulus = 2 ** len(word)
    odd_index = 0
    result = 0
    for position, bit in enumerate(word):
        if bit:
            odd_index += 1
            result -= 2**position * pow(3, -odd_index, modulus)
    return result % modulus


def chi(depth, frequency):
    order = 2**depth
    return pow(GENERATOR, (frequency % order) * ((FERMAT_PRIME - 1) // order),
               FERMAT_PRIME)


@cache
def character_polynomial(depth, z, frequency):
    if depth == 0:
        return 1
    modulus = 2**depth
    half = modulus // 2
    inverse = pow(3, -1, modulus)
    even = character_polynomial(depth - 1, z, frequency % half)
    odd = character_polynomial(depth - 1, z, (frequency * inverse) % half)
    return (even + z * chi(depth, -frequency * inverse) * odd) % FERMAT_PRIME


def check_characters(max_depth):
    require(pow(GENERATOR, 32768, FERMAT_PRIME) == FERMAT_PRIME - 1,
            "wrong primitive root")
    for depth in range(1, max_depth + 1):
        modulus = 2**depth
        weights = []
        for source in range(modulus):
            _, word = trajectory(source, depth)
            require(canonical_source(word) == source, "wrong positive inverse word")
            negative = source - modulus
            require(trajectory(negative, depth)[1] == word, "signed lift mismatch")
            weights.append(sum(word))
        for h in range(modulus):
            phases = [chi(depth, h * source) for source in range(modulus)]
            coefficients = [0] * (depth + 1)
            for q, phase in zip(weights, phases):
                coefficients[q] += phase
            for z in range(depth + 1):
                direct = sum(coefficient * z**q for q, coefficient in enumerate(coefficients))
                require(direct % FERMAT_PRIME == character_polynomial(depth, z, h),
                        "finite Fourier recurrence mismatch")
    print(f"All frequencies, weights and signed residue lifts through depth {max_depth}: pass")


def check_signed_windows(k):
    length = 5 * k
    width = 2**k
    modulus = 2**length
    threshold = (501 * length + 999) // 1000
    high = [r for r in range(modulus) if sum(trajectory(r, length)[1]) >= threshold]
    totals = [0, 0]
    for h in range(modulus):
        high_transform = sum(chi(length, h * r) for r in high)
        for i, sign in enumerate((1, -1)):
            window_transform = sum(chi(length, -sign * h * n) for n in range(1, width + 1))
            totals[i] += high_transform * window_transform
    inverse = pow(modulus, -1, FERMAT_PRIME)
    recovered = [v * inverse % FERMAT_PRIME for v in totals]
    observed = [sum(sum(trajectory(sign * n, length)[1]) >= threshold
                    for n in range(1, width + 1)) for sign in (1, -1)]
    require(recovered == observed, "signed window inversion mismatch")
    require(observed[1] == width, "reflected arc is not saturated")
    print(f"k={k} signed Fourier inversion gives positive/negative counts {recovered}")


def binomial_mass(size, index):
    return comb(size, index) if 0 <= index <= size else 0


def binomial_tail(size, cutoff):
    return sum(comb(size, index) for index in range(max(0, cutoff), size + 1))


def check_boundary_flux(k):
    length = 5 * k
    threshold = (501 * length + 999) // 1000
    width = 2**k
    words = [trajectory(n, length)[1] for n in range(1, width + 1)]
    counts = [0] * width
    previous = width * binomial_tail(length, threshold)
    for depth in range(length):
        unread = length - depth - 1
        signed_flux = sum((2 * word[depth] - 1)
                          * binomial_mass(unread, threshold - q - 1)
                          for word, q in zip(words, counts))
        counts = [q + word[depth] for q, word in zip(counts, words)]
        current = sum(binomial_tail(unread, threshold - q) for q in counts)
        require(2 * current - previous == signed_flux, "hybrid boundary flux mismatch")
        previous = current
    final = sum(q >= threshold for q in counts)
    require(previous == final, "wrong endpoint of physical interpolation")
    print(f"k={k}, all {length} hybrid layers and empirical endpoint: pass")


if __name__ == "__main__":
    check_characters(8)
    for scale in (1, 2):
        check_signed_windows(scale)
    for scale in (3, 6, 9):
        check_boundary_flux(scale)
