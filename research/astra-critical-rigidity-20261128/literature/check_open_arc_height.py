"""Finite exact controls for the original-source affine and local-product identities."""
from fractions import Fraction
from functools import reduce
from itertools import product
from math import gcd, lcm
import json


def require(ok, message):
    if not ok:
        raise ValueError(message)


def step(x):
    bit = x.numerator % 2
    require(x.denominator % 2 == 1, "physical denominator must be odd")
    return ((3 * x + 1) if bit else x) / 2, bit


def affine(word):
    multiplier, offset, divisor = 1, 0, 1
    for bit in word:
        if bit:
            multiplier, offset = 3 * multiplier, 3 * offset + divisor
        divisor *= 2
    return multiplier, offset, divisor


def v_p(value, p):
    require(value > 0, "valuation of nonpositive integer")
    exponent = 0
    while value % p == 0:
        value //= p
        exponent += 1
    return exponent


def norm(x, p):
    if x == 0:
        return Fraction(0)
    return Fraction(p) ** (v_p(x.denominator, p) - v_p(abs(x.numerator), p))


def local_product(x):
    return abs(x) * norm(x, 2) * norm(x, 3)


def physical(x, length):
    path, bits = [x], []
    for _ in range(length):
        x, bit = step(x)
        path.append(x)
        bits.append(bit)
    return path, bits


def minimum_realizers(depth):
    minima, words = {}, {}
    for n in range(1, 2**depth + 1):
        _, bits = physical(Fraction(n), depth)
        word = tuple(bits)
        require(word not in words, "parity permutation")
        words[word] = n
        mult, carry, divisor = affine(word)
        least = (-carry * pow(mult, -1, divisor)) % divisor or divisor
        require(least == n, "least positive parity realizer")
        runs = 1 + sum(a != b for a, b in zip(word, word[1:]))
        minima[runs] = min(n, minima.get(runs, n))
    require(words[(0,) * depth] == 2**depth, "all-even endpoint")
    require(words[(1,) * depth] == 2**depth - 1, "all-odd endpoint")
    return {str(k): min(n for runs, n in minima.items() if runs <= k)
            for k in range(1, 5)}


def arc_case(A, q, lengths, center_refs):
    x0 = Fraction(A, q)
    require(x0.numerator == A and x0.denominator == q, "reduced input")
    D = sum(lengths)
    path, bits = physical(x0, D)
    U = Fraction(1)
    time = 0
    terms = []
    refs = []
    hits = 0
    for i, d in enumerate(lengths):
        word = bits[time:time + d]
        mult, carry, div = affine(word)
        x, y = path[time], path[time + d]
        require(div * y == mult * x + carry, "physical affine segment")
        if center_refs:
            u = Fraction(carry, div - mult)
        else:
            # These references include even and odd denominators.
            u = Fraction((A + 5 * i) % 23 - 11, 2 + ((q + i) % 5))
        v = (mult * u + carry) / div
        refs.append((u, v))
        if x == u:
            hits += 1
        h = lcm(u.denominator, v.denominator)
        residual = h * q * (x - u)
        require(residual.denominator == 1 and residual.numerator % div == 0,
                "complete dyadic residual")
        require(U * (x - u) == U * Fraction(div, mult) * (y - v),
                "individual reference transport")
        if i == 0:
            terms.append(A - q * u)
        else:
            terms.append(q * (refs[i - 1][1] - u) * U)
        U *= Fraction(div, mult)
        time += d
    rhs = U * q * (path[-1] - refs[-1][1])
    require(sum(terms) == rhs, "signed original-source telescope")
    require(norm(rhs, 2) <= Fraction(1, 2**D) *
            max(1, norm(refs[-1][1], 2)), "terminal precision")
    if hits or rhs == 0:
        return hits
    vector = [terms[0]] + [z for z in terms[1:] if z]
    # Scale to primitive integers, and verify the exact change in the product
    # of independent local forms, including every prime outside {2,3}.
    clearing = lcm(*(x.denominator for x in vector))
    common = reduce(gcd, (abs(int(x * clearing)) for x in vector))
    scale = Fraction(clearing, common)
    primitive = [x * scale for x in vector]
    require(all(z.denominator == 1 for z in primitive), "primitive integrality")
    require(reduce(gcd, (abs(int(z)) for z in primitive)) == 1, "primitive gcd")

    def form_product(values):
        result = abs(values[0]) * norm(values[0], 3) * norm(sum(values), 2)
        for z in values[1:]:
            result *= local_product(z)
        return result

    require(form_product(primitive) == local_product(scale)**len(vector) *
            form_product(vector), "three-place primitive scaling")
    return hits


def primitive(word):
    size = len(word)
    return all(size % d or word != word[:d] * (size // d)
               for d in range(1, size))


def rational_cycles(max_length):
    count = odd_cases = 0
    for size in range(2, max_length + 1):
        for word in product((0, 1), repeat=size):
            if not primitive(word):
                continue
            mult, carry, div = affine(word)
            if mult >= div or not carry:
                continue
            x = Fraction(carry, div - mult)
            path, bits = physical(x, size)
            require(tuple(bits) == word and path[-1] == x, "cycle replay")
            require(gcd(x.denominator, 6) == 1, "full cycle denominator")
            require(all(v.denominator == x.denominator for v in path),
                    "physical denominator at every rotation")
            if word[0]:
                odd_cases += 1
            count += 1
    return count, odd_cases


def main():
    ledger_checks, hits, custom = 0, 0, 0
    for q in (1, 5, 7, 11, 25, 35, 41):
        for A in range(1, 88, 3):
            if gcd(A, q) != 1:
                continue
            for lengths in ((1,), (3, 5), (4, 2, 3), (1, 1, 2, 6), (11, 3, 2)):
                for use_centers in (True, False):
                    count = arc_case(A, q, lengths, use_centers)
                    hits += count
                    custom += not use_centers
                    ledger_checks += 1
    # Exact template return. It is essential to exclude this hypothesis.
    path, bits = physical(Fraction(1), 100)
    require(bits == [1, 0] * 50 and path[-1] == 1, "trivial-cycle control")
    cycles, odd = rational_cycles(10)
    print(json.dumps({
        "arcs_cases": ledger_checks,
        "custom_reference_cases": custom,
        "center_or_reference_hits": hits,
        "depth_12_smallest_seeds_for_at_most_k_runs": minimum_realizers(12),
        "primitive_positive_rational_cycle_words_to_length_10": cycles,
        "of_those_starting_odd": odd,
        "sharp_sources_length_12": [4095, 4096],
        "trivial_cycle_control_steps": 100,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
