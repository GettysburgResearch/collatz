"""Replay ordinary Collatz paths and small exact covering histograms."""

from collections import Counter
from itertools import product
from math import isqrt
import json

from portal import odd_word, corrected_word
from returns import census


def require(test, description):
    if not test:
        raise ArithmeticError(description)


def walk(value, clock):
    odd = 0
    peak = value
    for _ in range(clock):
        if value % 2:
            odd += 1
            value = (3 * value + 1) // 2
        else:
            value //= 2
        peak = max(peak, value)
    return value, odd, peak


def radix_cases():
    ordinary = 0
    modular = 0
    for precision in range(1, 9):
        modulus = 3 ** precision
        for stages in range(1, 5):
            for source in [1, 2, 4, 5, 19, 49, 64, 121]:
                for target in range(min(modulus, 50)):
                    word = odd_word(source, target, precision, stages)
                    require(word.residue(source, modulus) == target,
                            "radix terminal residue")
                    modular += 1
                    if word.clock > 600:
                        continue
                    value = word.ordinary(source)
                    endpoint, odd, peak = walk(value, word.clock)
                    require(value % 2 == 1 and value % modulus == target,
                            "ordinary residue or parity")
                    require(endpoint == source and odd == stages + 1,
                            "ordinary endpoint or odd count")
                    require(peak <= source << word.clock, "ordinary height bound")
                    ordinary += 1
    return {"modular": modular, "full_ordinary": ordinary}


def exact_histogram(source, precision, stages, width):
    modulus = 3 ** (precision + stages)
    weights = [source] + [-3 ** i for i in range(stages)]
    counts = Counter({0: 1})
    for i, weight in enumerate(weights):
        offset = (stages - i) * width
        atoms = Counter(weight * pow(2, offset + j, modulus) % modulus
                        for j in range(width))
        updated = Counter()
        for old, multiplicity in counts.items():
            for atom, copies in atoms.items():
                updated[(old + atom) % modulus] += multiplicity * copies
        counts = updated
    fiber = [counts[3 ** stages * a] for a in range(3 ** precision)]
    zeros = sum(value == 0 for value in fiber)
    require(sum(counts.values()) == width ** (stages + 1), "histogram mass")
    if width ** (stages + 1) <= 20000:
        direct = Counter()
        for values in product(range(width), repeat=stages + 1):
            h = [(stages - i) * width + v for i, v in enumerate(values)]
            value = source
            for e, f in zip(h, h[1:]):
                scaled = (value << (e-f)) - 1
                if scaled % 3:
                    break
                value = scaled // 3
            else:
                direct[(value << h[-1]) % 3 ** precision] += 1
        require(fiber == [direct[a] for a in range(3 ** precision)],
                "direct physical enumeration")
    return {"source": source, "precision": precision, "stages": stages,
            "window": width, "missing": zeros, "min": min(fiber), "max": max(fiber)}


def large_examples():
    rows = []
    for precision in (8, 24, 64, 152):
        # The actual PR192 dyadic terminal constraint forces
        # 517727 * Y = 203816 modulo 3^precision.
        target = 203816 * pow(517727, -1, 3 ** precision) % (3 ** precision)
        for source in [1, 17, 101]:
            word = corrected_word(source, target, precision, max(1, isqrt(precision)))
            require(word.residue(source, 3 ** precision) == target, "large target")
            rows.append({"q": source, "precision": precision,
                         "grade": len(word.odd_exponents), "clock": word.clock})
    return rows


def paired_cases():
    cases = 0
    for k in range(4, 18):
        for u in range(1, 28, 2):
            X = (3 ** k * u + 1) // 2
            Y = 4 + 4 ** (k+1) * u
            low, low_grade, _ = walk(Y, 2*k+3)
            high, high_grade, _ = walk(3*Y-1, 2*k+3)
            require((low, high, low_grade, high_grade) == (X, 3*X-1, k, k),
                    "full ternary cusp")
            cases += 1
    for X, Y, h, p in [(8, 927, 72, 41), (1, 1, 2, 1), (2, 6, 5, 2)]:
        low, lp, _ = walk(Y, h)
        high, hp, _ = walk(3*Y-1, h)
        require((low, high, lp, hp) == (X, 3*X-1, p, p), "paired fixture")
    rows = census(14)
    # Independent ordinary enumeration at *every* possible clock for grades 1-4.
    for row in rows[:4]:
        p = row["grade"]
        total = 0
        for h in range(1, row["max_clock"]+1):
            for r in range(2 ** h):
                # Translate the zero representative to keep both arms ordinary positive.
                y = r + 2 ** h
                x, lp, _ = walk(y, h)
                if lp != p:
                    continue
                v, hp, _ = walk(3*y-1, h)
                total += int(hp == p and v == 3*x-1)
        require(total == row["all"], "direct binary prefix check")
    return {"cusp_full_ordinary": cases, "exact_return_census": rows}


def main():
    histograms = [exact_histogram(q, L, r, h) for q, L, r, h in
                  [(1, 2, 2, 2), (1, 3, 2, 8), (5, 3, 2, 8),
                   (7, 3, 2, 8), (17, 4, 3, 12), (121, 6, 4, 16)]]
    require(histograms[0]["missing"] > 0, "negative narrow-window control")
    print(json.dumps({"radix": radix_cases(), "histograms": histograms,
                      "large_modular_only": large_examples(), "paired": paired_cases()}, indent=2))


if __name__ == "__main__":
    main()
