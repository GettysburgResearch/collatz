"""Exact bounded controls for both written proofs. Run with Python 3."""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import comb
import json


def require(condition, label):
    if not condition:
        raise RuntimeError(label)


def rotations(word):
    return [word[i:] + word[:i] for i in range(len(word))]


def carry(word, companion=False):
    scale = slope = 1
    offset = 0
    for bit in word:
        mult = 3 if companion or bit else 1
        offset = mult * offset + bit * scale
        slope *= mult
        scale *= 2 ** (1 + bit) if companion else 2
    return scale, slope, offset


def period(word, companion=False):
    scale, slope, offset = carry(word, companion)
    return Fraction(offset, scale - slope)


def odd_gaps(word):
    positions = [i for i, bit in enumerate(word) if bit]
    require(positions[0] == 0, "minimum must be odd")
    return tuple(y - x for x, y in zip(positions, positions[1:] + [len(word)]))


def repeated_word(word, length):
    return (word * (1 + length // len(word)))[-length:]


def check_cycles():
    counts = defaultdict(int)
    for length in range(2, 13):
        groups = defaultdict(list)
        companions = defaultdict(list)
        for word in product((0, 1), repeat=length):
            weight = sum(word)
            if not 0 < weight < length:
                continue
            cuts = rotations(word)
            if word != min(cuts):
                continue
            phases = [period(cut) for cut in cuts]
            d = phases[0].denominator
            require(all(y.denominator == d for y in phases), "physical denominator")
            j = min(range(length), key=lambda i: abs(phases[i]))
            groups[weight].append((d, abs(phases[j].numerator), cuts[j]))
            counts["positive" if phases[j] > 0 else "negative"] += 1
            ws = [period(cut, True) for cut in cuts]
            cm = min(range(length), key=lambda i: abs(ws[i]))
            companions[weight].append((ws[cm].denominator, abs(ws[cm].numerator), cuts[cm]))
            if 2 ** (length + weight) < 3 ** length:
                continue
            den = ws[0].denominator
            require(all(y >= 1 and y.denominator == den for y in ws),
                    "positive companion/min")
            if len(set(cuts)) == length:
                require(len(set(ws)) == length, "primitive companion")
            bound = 4
            k = 0
            while 3 ** k <= 2 * bound * den:
                k += 1
            seen = {}
            for i, y in enumerate(ws):
                if y > bound:
                    continue
                past = repeated_word(cuts[i], k)
                source = ws[(i - k) % length]
                scale, slope, offset = carry(past, True)
                require(scale*y == slope*source + offset, "periodic past clock")
                require(scale*bound >= 3**k, "restricted suffix weight")
                residue = (den * offset * pow(scale, -1, 3**k)) % (3**k)
                require(y * den == residue, "ternary history decoder")
                require(seen.setdefault(past, y) == y, "bounded endpoint uniqueness")
                counts["bounded_companion_phases"] += 1
            counts["positive_companion_necklaces"] += 1

        for weight, rows in companions.items():
            for k in range(1, length + weight + 1):
                codes = set()
                for d, minimum, word in rows:
                    if minimum > 2**k:
                        continue
                    clock = 0
                    for j, bit in enumerate(word, 1):
                        clock += 1 + bit
                        if clock >= k:
                            break
                    key = (d, word[:j])
                    require(key not in codes, "companion stopping-prefix minimum")
                    codes.add(key)
                    require(0 <= clock-k <= 1, "binary clock overshoot")
                    counts["companion_stopping_codes"] += 1
            for r in range(length + 1):
                codes = set()
                for d, minimum, word in rows:
                    if minimum > 3**r:
                        continue
                    key = (d, word[length-r:])
                    require(key not in codes, "companion ternary minimum")
                    codes.add(key)
                    counts["companion_ternary_codes"] += 1

        for weight, rows in groups.items():
            for k in range(length + 1):
                codes = set()
                choices = sum(comb(k, h) for h in range(k+1)
                              if 0 <= weight-h <= length-k)
                total_at_d = defaultdict(int)
                for d, minimum, word in rows:
                    if minimum > 2**k:
                        continue
                    key = (d, word[:k])
                    require(key not in codes, "minimum from physical prefix")
                    codes.add(key)
                    total_at_d[d] += 1
                    counts["dyadic_minimum_codes"] += 1
                require(all(n <= choices for n in total_at_d.values()), "prefix count")
            for r in range(weight + 1):
                codes = set()
                for d, minimum, word in rows:
                    if minimum > 3**r:
                        continue
                    gaps = odd_gaps(word)
                    suffix = gaps[len(gaps)-r:]
                    key = (d, suffix)
                    require(key not in codes, "minimum from physical past")
                    codes.add(key)
                    counts["ternary_minimum_codes"] += 1
    return counts


def shortcut(x):
    return (3*x+1)//2 if x % 2 else x//2


def exact_companion(n):
    states = []
    while n != 1:
        require(len(states) < 2000, "physical fixture time limit")
        states.append(n)
        n = shortcut(n)
    result = Fraction(9)
    for x in reversed(states):
        bit = x % 2
        result = bit + Fraction(2**(1+bit), 3)*result
    return result


def valuation_two(x):
    n = abs(x.numerator)
    d = x.denominator
    return (n & -n).bit_length() - (d & -d).bit_length()


def check_agreements():
    count = 0
    for n in range(1, 161):
        expected = exact_companion(n)
        for b in [1, 3, 5, 21, 45, 143]:
            for v in [8, 23, 50]:
                candidate = expected + Fraction((-1)**n * 2**v, b)
                actual = -expected / 3
                trial = -candidate / 3
                x = n
                clock = 0
                while v - clock >= 2:
                    bit = x % 2
                    require(trial.denominator % 2 == 1, "dyadic trial denominator")
                    residue = (trial.numerator*pow(trial.denominator, -1, 4)) % 4
                    require(residue == 1 if bit else residue % 2 == 0, "trial branch")
                    trial = (3*trial+bit)/2**(1+bit)
                    actual = (3*actual+bit)/2**(1+bit)
                    clock += 1+bit
                    require(valuation_two(actual-trial) == v-clock, "exact bit agreement")
                    x = shortcut(x)
                    count += 1
    return count


if __name__ == "__main__":
    result = check_cycles()
    result["trial_steps"] = check_agreements()
    print(json.dumps(result, sort_keys=True))
