"""Replay exact finite controls for the canonical mask and period-vector arguments."""

from fractions import Fraction
from itertools import product
from math import gcd


def require(condition, description):
    if not condition:
        raise ValueError(description)


def affine(bits):
    intercept, multiplier = 0, 1
    for index, bit in enumerate(bits):
        if bit:
            intercept = 3 * intercept + (1 << index)
            multiplier *= 3
    return intercept, multiplier


def canonical(bits):
    intercept, multiplier = affine(bits)
    modulus = 1 << len(bits)
    return -intercept * pow(multiplier, -1, modulus) % modulus


def predecessor_masks(depth):
    classes = {}
    modulus = 3**depth
    for exponents in product((1, 2), repeat=depth):
        bits = tuple(bit for step in exponents for bit in (1,) + (0,) * (step - 1))
        intercept, _ = affine(bits)
        target = intercept * pow(1 << len(bits), -1, modulus) % modulus
        require(target not in classes, "different two-gap words have the same target")
        value, precision = target, modulus
        for exponent in reversed(exponents):
            allowed = [a for a in (1, 2) if ((1 << a) * value - 1) % 3 == 0]
            require(allowed == [exponent], "last inverse exponent is not forced")
            precision //= 3
            value = (((1 << exponent) * value - 1) // 3) % precision
        classes[target] = exponents
    return {r for r, w in classes.items() if (1, 1) not in zip(w, w[1:])}


def mask_and_carry_controls():
    fib_old, fib_new = 1, 1
    for depth in range(1, 12):
        fib_old, fib_new = fib_new, fib_new + fib_old
        require(len(predecessor_masks(depth)) == fib_new, "incorrect Fibonacci cardinal")
    tested = 0
    for macro_count in range(3, 9):
        for selection in product((0, 1), repeat=macro_count):
            blocks = [(1,) * (1 + bit) + (0,) for bit in selection]
            cuts = (0, 1, macro_count // 2 + 1, macro_count)
            chunks = [sum(blocks[i:j], ()) for i, j in zip(cuts, cuts[1:])]
            bits = sum(chunks, ())
            total = len(bits)
            start = prior_odd = raw = 0
            for piece in chunks:
                numerator, _ = affine(piece)
                prior_odd += sum(piece)
                modulus = 1 << (total - start)
                root_piece = -pow(3**prior_odd, -1, modulus) * numerator % modulus
                raw += (1 << start) * root_piece
                start += len(piece)
            residue = canonical(bits)
            carry, remainder = divmod(raw, 1 << total)
            require(carry < len(chunks) and remainder == residue, "raw carry mismatch")
            for depth in (1, 2, 4):
                modulus = 3**depth
                require((raw - carry * (1 << total) - residue) % modulus == 0,
                        "wrong canonical residue after the real carry")
            for length in range(1, total):
                require(canonical(bits[:length]) == residue % (1 << length),
                        "canonical source cylinders fail nesting")
            tested += 1
    return tested


def pf_controls():
    r = Fraction(4)
    powers = [1 + r + r**2, 1 + r, Fraction(1)]
    avoid_111 = {
        i: {0: (0, 1 / powers[i])} |
           ({1: (i + 1, r * powers[i + 1] / powers[i])} if i < 2 else {})
        for i in range(3)
    }
    s = Fraction(2, 5)
    factor = 1 + s**2 / (1 - s)
    avoid_101 = {
        0: {1: (0, 1 / factor), 0: (1, (factor - 1) / factor)},
        1: {0: (2, Fraction(1))},
        2: {1: (0, 1 - s), 0: (2, s)},
    }
    models = [
        (avoid_111, powers, powers[0], r * powers[0], (1, 1, 1)),
        (avoid_101, [factor, s / (1 - s), 1 / (1 - s)], 1 / s, 1 / (s * factor), (1, 0, 1)),
    ]
    paths = 0
    for model, function, eigenvalue, tilt, forbidden in models:
        for state, row in model.items():
            require(sum(prob for _, prob in row.values()) == 1, "row is not stochastic")
            for bit, (end, probability) in row.items():
                require(probability == tilt**bit * function[end] / (eigenvalue * function[state]),
                        "Perron transition discrepancy")
        for bits in product((0, 1), repeat=9):
            accepted = False
            for initial in model:
                vertex, probability = initial, Fraction(1)
                for bit in bits:
                    if bit not in model[vertex]:
                        break
                    vertex, step = model[vertex][bit]
                    probability *= step
                else:
                    accepted = True
                    want = tilt**sum(bits) * function[vertex] / (eigenvalue**len(bits) * function[initial])
                    require(probability == want, "full cylinder weight discrepancy")
                    paths += 1
            expected = all(bits[i:i+3] != forbidden for i in range(7))
            require(expected == accepted, "three-state presentation differs from forbidden word")
    return paths


def lattice_controls():
    count = 0
    rank_one = 0
    for denominator in (197, 503, 1009):
        for numerator in (37, 97, 131):
            p = Fraction(numerator, denominator)
            for bound in (7, 19, 45, 96, 171):
                for width in (Fraction(1, 299), Fraction(1, 97), Fraction(1, 31),
                              Fraction(1, 11), Fraction(1, 7), Fraction(1, 3)):
                    vectors = []
                    for n in range(1, bound + 1):
                        target = p * n
                        u = target.numerator // target.denominator
                        if 0 < target - u <= width:
                            vectors.append((n, u))
                    slopes = {Fraction(u, n) for n, u in vectors}
                    if len(slopes) > 1:
                        require(len(vectors) <= 2 * bound * width + 1, "rank-two area bound")
                    if len(slopes) == 1:
                        rank_one += 1
                        for cap in (1, 2, 5, 11):
                            require(sum(gcd(n, u) <= cap for n, u in vectors) <= cap,
                                    "primitive-ray content bound")
                    count += 1
    return count, rank_one


if __name__ == "__main__":
    words = mask_and_carry_controls()
    paths = pf_controls()
    strips, rays = lattice_controls()
    print(f"PASS: 11 ternary mask depths, {words} raw canonical lifts, {paths} Markov cylinders, "
          f"{strips} finite lattice strips ({rays} nonempty rank-one)")
