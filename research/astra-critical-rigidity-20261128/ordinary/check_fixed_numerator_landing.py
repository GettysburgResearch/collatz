"""Replay centered landing identities, fast cylinders and exact first-landing counts."""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb, gcd
import json

from check_line_shadow_structure import rational_step, require


def affine(word):
    g = carry = 0
    for i, odd in enumerate(word):
        if odd:
            carry = 3 * carry + 2**i
            g += 1
    return g, carry


def landing(n, m, q):
    z = Fraction(m, q * 3**n)
    x = [z]
    bits = []
    while z.denominator % 3 == 0:
        bits.append(z.numerator % 2)
        z = rational_step(z)
        x.append(z)
    require(z.denominator == q and sum(bits) == n, "wrong exact landing denominator")
    return x, tuple(bits)


def powered_pieces(word):
    start = 0
    while start < len(word):
        best = (1, 1)
        for b in range(1, min(6, len(word) - start) + 1):
            w = word[start:start + b]
            end = start + b
            while word[end:end + b] == w:
                end += b
            if end - start > best[0]:
                best = end - start, b
        span, b = best
        yield start, start + span, word[start:start + b]
        start += span


def centered_checks(n, m, q, counts):
    states, bits = landing(n, m, q)
    clock = len(bits)
    centers = []
    pieces = list(powered_pieces(bits))
    tail = Fraction(0)
    for start, end, w in pieces:
        g, carry = affine(w)
        c = Fraction(carry, 2**len(w) - 3**g)
        centers.append(c)
        h = n - sum(bits[:start])
        remaining = n - sum(bits[:end])
        u = states[start].numerator
        v = states[end].numerator
        shifted_entry = c.denominator * u - c.numerator * q * 3**h
        shifted_end = c.denominator * v - c.numerator * q * 3**remaining
        require(shifted_entry and shifted_entry == 2**(end - start) * shifted_end,
                "centered word equation")
        _, before = affine(bits[:start])
        combined = c.denominator * m + q * 3**h * (c.denominator * before - c.numerator * 2**start)
        require(combined == 2**start * shifted_entry and combined % 2**end == 0
                and combined % 3 != 0, "original-numerator block divisibility")
        suffix = Fraction(3**remaining, 2**(clock - end))
        slope = Fraction(3**(h - remaining), 2**(end - start))
        tail += c * (1 - slope) * suffix
        counts["powered_pieces"] += 1
        counts["nonconstant_repeated_pieces"] += len(set(w)) == 2 and end - start >= 2 * len(w)
        counts["positive_center"] += c > 0
        counts["negative_center"] += c < 0
        counts["zero_center"] += c == 0
        counts["negative_shifted_entries"] += shifted_entry < 0
    terminal = states[-1].numerator
    require(terminal == Fraction(m, 2**clock) + q * tail, "forward center telescoping")
    shifted = m + q * 3**n
    for t, (z, bit) in enumerate(zip(states, bits)):
        h = n - sum(bits[:t])
        require(shifted == 2**t * (z.numerator + q * 3**h), "wrong odd-background prefix")
        if not bit:
            shifted += q * 3**h * 2**t
            counts["even_insertions"] += 1
    require(shifted == 2**clock * (terminal + q), "shifted terminal identity")
    counts["full_landing_words"] += 1
    counts["native_dates"] += clock


def source_class(word, n):
    mod = 2**len(word)
    state = 0
    for bit in reversed(word):
        state = (2 * state - bit) * (pow(3, -1, mod) if bit else 1) % mod
    return (state * 3**n) % mod


def fast_cylinders(counts):
    sharp = []
    for n in range(1, 10):
        grid = [(m, len(landing(n, m, 1)[1])) for m in range(1, 3**n) if m % 3]
        observed = Counter(t for _, t in grid)
        minima = {}
        for E in range(5):
            t = n + E
            mod = 2**t
            residues = set()
            smallest = 3 * mod + 1
            full_count = 0
            for evens in combinations(range(t - 1), E):
                word = [1] * t
                for i in evens:
                    word[i] = 0
                r = source_class(word, n)
                require(r not in residues, "colliding fast-word cylinders")
                residues.add(r)
                first = next(x for x in (r, r + mod, r + 2*mod, r + 3*mod) if x > 0 and x % 3)
                require(first <= 3 * mod and list(landing(n, first, 1)[1]) == word,
                        "witness misses exact first-landing word")
                smallest = min(smallest, first)
                grid_end = 3**n - 1
                representatives = [x for x in (r, r + mod, r + 2*mod) if x % 3]
                count = sum(max(0, 1 + (grid_end - x) // (3 * mod)) for x in representatives)
                full_count += count
                require(abs(Fraction(count) - Fraction(2 * 3**(n - 1), mod)) <= 2,
                        "grid class error")
                counts["prescribed_fast_cylinders"] += 1
            require(len(residues) == comb(t - 1, n - 1) and full_count == observed[t],
                    "word counts disagree with direct complete grid")
            if smallest < 3**n:
                require(smallest == min(m for m, exact in grid if exact == t),
                        "wrong first fast numerator")
            minima[str(E)] = smallest
        counts["full_grid_sources"] += len(grid)
        sharp.append({"n": n, "minimum_by_excess": minima})
    return sharp


def main():
    counts = Counter()
    for n in range(1, 9):
        for q in (1, 5, 7, 35):
            for m in range(1, 48):
                if gcd(m, 3*q) == 1:
                    centered_checks(n, m, q, counts)
    minima = fast_cylinders(counts)
    for key in ("nonconstant_repeated_pieces", "positive_center", "negative_center",
                "zero_center", "negative_shifted_entries"):
        require(counts[key] > 0, f"missing {key} control")
    print(json.dumps({"counts": dict(counts), "fast_sources": minima}, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
