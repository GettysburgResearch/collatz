"""Exact commutator, coset and macro-arrangement controls."""

from collections import Counter
from fractions import Fraction
from functools import cache
from itertools import combinations, product
from math import comb, gcd


def check(ok, description):
    if not ok:
        raise AssertionError(description)


def affine(bits):
    odd_positions = [i for i, bit in enumerate(bits) if bit == "1"]
    return sum(2 ** t * 3 ** j for j, t in enumerate(reversed(odd_positions)))


def swap(a, b):
    return ((3 ** a.count("1") - 2 ** len(a)) * affine(b)
            + (2 ** len(b) - 3 ** b.count("1")) * affine(a))


def arrangements(counts):
    if not any(counts):
        yield ()
        return
    for i, count in enumerate(counts):
        if count:
            rest = list(counts)
            rest[i] -= 1
            for after in arrangements(tuple(rest)):
                yield (i,) + after


def primitive(word):
    return all(word[r:] + word[:r] != word for r in range(1, len(word)))


def totals(blocks, counts):
    n = sum(len(a) * k for a, k in zip(blocks, counts))
    u = sum(a.count("1") * k for a, k in zip(blocks, counts))
    return n, u, abs(2 ** n - 3 ** u)


def model_histogram(determinant, divisor, cstar):
    return Counter(gcd(t, determinant) for t in range(cstar % divisor, determinant, divisor))


def controls(blocks, counts, check_parsing=False):
    h = gcd(*(abs(swap(a, b)) for a, b in combinations(blocks, 2)))
    n, u, determinant = totals(blocks, counts)
    h_d = gcd(h, determinant)
    raw = Counter()
    gcd_hist = Counter()
    global_diff = 0
    cstar = affine("".join(a * k for a, k in zip(blocks, counts)))
    for letters in arrangements(counts):
        word = "".join(blocks[i] for i in letters)
        numerator = affine(word)
        global_diff = gcd(global_diff, abs(numerator - cstar))
        check(numerator == cstar if not h else (numerator - cstar) % h == 0,
              "wrong commutator coset")
        raw[numerator] += 1
        gcd_hist[gcd(numerator, determinant)] += 1
        if check_parsing:
            check(primitive(word) == primitive(letters), "binary and macro primitivity disagree")
        for j in range(len(letters)-1):
            a, b = blocks[letters[j]], blocks[letters[j+1]]
            before = "".join(blocks[i] for i in letters[:j])
            after = "".join(blocks[i] for i in letters[j+2:])
            expected = 2 ** len(before) * 3 ** after.count("1") * swap(a, b)
            check(affine(before + b + a + after) - numerator == expected, "swap identity")
    # At any modulus prime to 6, the swap gcd gives the exact generated subgroup.
    for mod in (5, 7, 11, 25, 35, 49, 55, 77, 125, 385):
        check(gcd(mod, global_diff) == gcd(mod, h), "excess generated coset")
    if determinant <= 2_000_000:
        model = model_histogram(determinant, h_d, cstar)
        for q in range(1, min(determinant, 1000) + 1):
            if determinant % q:
                continue
            h_q = gcd(q, h)
            expected = Fraction(h_q, q) if cstar % h_q == 0 else Fraction(0)
            observed = Fraction(sum(count for t, count in model.items() if t % q == 0),
                                model.total())
            check(expected == observed, "marginal of uniform coset model")
    return h, h_d, cstar, gcd_hist, len(raw)


def residue_counts(blocks, counts, mod):
    @cache
    def visit(remaining):
        if not any(remaining):
            return Counter({0: 1})
        n = sum(len(a) * k for a, k in zip(blocks, remaining))
        answer = Counter()
        for j, k in enumerate(remaining):
            if not k:
                continue
            prev = list(remaining)
            prev[j] -= 1
            a = blocks[j]
            for value, count in visit(tuple(prev)).items():
                endpoint = (3 ** a.count("1") * value + 2 ** (n-len(a)) * affine(a)) % mod
                answer[endpoint] += count
        return answer

    return visit(tuple(counts))


def main():
    small = ["".join(w) for ell in range(1, 5) for w in product("01", repeat=ell)]
    for a, b in product(small, repeat=2):
        check(swap(a, b) == affine(b+a) - affine(a+b), "pair formula")
        check((swap(a, b) == 0) == (a+b == b+a), "commuting words")
    print("pair identities and commuting tests", len(small) ** 2)
    for blocks, counts in (
            (("10", "110"), (4, 8)), (("1", "000"), (6, 3)),
            (("10", "1010"), (4, 2)), (("1", "0", "10"), (2, 3, 2)),
            (("00", "01", "110"), (2, 3, 2))):
        h, h_d, cstar, histogram, nraw = controls(blocks, counts, blocks == ("10", "110"))
        if blocks == ("1", "000"):
            check(h == h_d == 7 and all(t % 7 == 0 for t in histogram), "seven obstruction")
        if blocks == ("10", "1010"):
            check(h == 0 and nraw == 1, "commuting stratum")
        if blocks == ("1", "0", "10"):
            check(nraw < histogram.total(), "nonunique binary parsing control")
        print("stratum", blocks, counts, "H", h, "h_D", h_d, "roots",
              histogram.total(), "binary words", nraw, "gcd bins", len(histogram))
    for blocks, counts, mod in ((("10", "110"), (12, 28), 77),
                                (("1", "000"), (24, 18), 49),
                                (("1", "000"), (25, 17), 77)):
        counts_mod = residue_counts(blocks, counts, mod)
        h = gcd(swap(*blocks), mod)
        cstar = affine("".join(a * k for a, k in zip(blocks, counts)))
        mass = counts_mod.total()
        check(mass == comb(sum(counts), counts[0]), "type size")
        check(all((r-cstar) % h == 0 for r in counts_mod), "DP coset")
        delta = max(abs(Fraction(counts_mod[r], mass)
                        - (Fraction(h, mod) if (r-cstar) % h == 0 else 0))
                    for r in range(mod))
        print("macro slice", counts, "mod", mod, "coset", cstar % h, "mod", h,
              "maximum point error", delta)


if __name__ == "__main__":
    main()
