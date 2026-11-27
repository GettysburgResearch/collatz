"""Connected prime-to-six integer flow controls and their ordinary rational cycles."""
from fractions import Fraction
from hashlib import sha256
from math import gcd, lcm, prod
import json

from check_shifts import cycle, require


def core(n):
    for prime in (2, 3):
        while n % prime == 0:
            n //= prime
    return n


def valuation(n, p):
    exponent = 0
    while n % p == 0:
        exponent += 1
        n //= p
    return exponent


def schedule(grade, flip=False):
    length = (3 ** grade).bit_length()
    pairs, tail = divmod(grade, 2)
    free = 2 * grade - length
    require(1 <= free <= pairs, "free pair allocation")
    gaps = []
    pair_id = 0
    for j in range(pairs):
        if (j + 1) * free // pairs == j * free // pairs:
            gaps.extend((2, 2))
            continue
        coin = sha256(f"core-pair-{grade}-{pair_id}".encode()).digest()[0] & 1
        if flip and pair_id == 0:
            coin = 1 - coin
        gaps.extend((1, 2) if coin else (2, 1))
        pair_id += 1
    if tail:
        gaps.append(2)
    require(sum(gaps) == length and len(gaps) == grade, "clock count")
    clock = 0
    prefix_errors = [0]
    for i, gap in enumerate(gaps):
        clock += gap
        prefix_errors.append(grade * clock - (i + 1) * length)
    require(max(prefix_errors) - min(prefix_errors) < 4 * grade, "clock interval discrepancy")
    return gaps, free


def native(gaps):
    return tuple(b for a in gaps for b in [1] + [0] * (a - 1))


def distances(word):
    length = len(word)
    mask = (1 << length) - 1
    code = sum(x << j for j, x in enumerate(word))
    return [(code ^ (((code >> d) | (code << (length - d))) & mask)).bit_count()
            for d in range(1, length)]


def lap(gaps, z):
    for a in gaps:
        d = 2 ** a
        z = (3 * z + d - 1) // d
    return z


def positive_fix(gaps, length, grade):
    delta = 2 ** length - 3 ** grade
    maximum = -(-(16 * grade * 2 ** length) // delta)
    lo, hi = 1, maximum
    require(lap(gaps, lo) >= lo and lap(gaps, hi) <= hi, "failed bracket")
    if lap(gaps, lo) == lo:
        return lo, maximum
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if lap(gaps, mid) > mid:
            lo = mid
        else:
            hi = mid
    require(lap(gaps, hi) == hi, "integer monotone crossing failed")
    return hi, maximum


def best_defect(length, grade):
    # Compare every strictly smaller positive defect exactly, restricting its
    # ternary exponent to the largest b with 3^b < 2^a.
    b = 0
    for a in range(1, length):
        while 3 ** (b + 1) < 2 ** a:
            b += 1
        if 2 ** a * 3 ** grade < 2 ** length * 3 ** b:
            return False
    return True


def certificate(grade):
    a, free = schedule(grade)
    b, _ = schedule(grade, flip=True)
    w, v = native(a), native(b)
    length = len(w)
    require(sum(x != y for x, y in zip(w, v)) == 2, "adjacent flip")
    nw, qw = cycle(w)
    nv, qv = cycle(v)
    raw = 2 ** length - 3 ** grade
    require(lcm(qw, qv) == raw, "adjacent unit carry")
    if qw < qv:
        w, a, nw, qw = v, b, nv, qv
    require(qw * qw >= raw and qw > 1, "full rational denominator control")
    hd = min(distances(w))
    require(2 * (hd + 4) >= free, "low all-shift distance for selected orientation")
    z, maximum = positive_fix(a, length, grade)
    initial = z
    charges = []
    macro_states = []
    missed_commands = 0
    for gap in a:
        macro_states.append(z)
        for h in range(gap):
            command = int(h == 0)
            missed_commands += (command != int(z % 2 == 0))
            n = 3 ** command * z
            if n % 2:
                charges.append(n)
            z = (n + 1) // 2
    require(z == initial and max(macro_states) <= maximum, "closed bounded integer control")
    require(missed_commands > 0, "exponential denominator but ordinary branch lock")
    require(charges and all(n % 2 and n % 3 != 1 for n in charges), "charged residue")
    require(all(core(n + 1) == core(charges[(i + 1) % len(charges)])
                for i, n in enumerate(charges)), "disconnected prime flow")
    require(prod(Fraction(n + 1, n) for n in charges) == Fraction(2 ** length, 3 ** grade),
            "full integer prime holonomy")
    av = sum(valuation(n + 1, 2) for n in charges)
    bv = sum(valuation(n, 3) - valuation(n + 1, 3) for n in charges)
    require((av, bv) == (length, grade), "prime budget")
    require(min(charges) * raw >= 3 ** grade, "individual positive holonomy")
    sources = [core(n) for n in charges]
    best = best_defect(length, grade)
    if best:
        require(len(set(sources)) == len(charges), "repeated core at strictly best defect")
    ordered = sorted(nw)
    min_space = Fraction(min(b - a for a, b in zip(ordered, ordered[1:])), qw)
    real_min = Fraction(min(nw), qw)
    if best:
        require(min_space > 1, "record-defect spacing in this finite control")
    return dict(length=length, grade=grade, free_pairs=free, minimum_shift_distance=hd,
                rational_denominator_bits=qw.bit_length(), raw_denominator_bits=raw.bit_length(),
                ordinary_rational_min_floor=real_min.numerator // real_min.denominator,
                ordinary_min_pair_spacing_floor=min_space.numerator // min_space.denominator,
                integer_fixed_point=initial, least_charged_index=min(charges),
                greatest_charged_index=max(charges), charged_edges=len(charges),
                distinct_core_sources=len(set(sources)), failed_ordinary_commands=missed_commands,
                strict_best_positive_defect=best, macro_height_bound=maximum,
                macro_maximum=max(macro_states), core_maximum=max(sources))


def main():
    require([core(n) for n in (27, 28, 63, 64)] == [1, 7, 7, 1], "short control")
    require(Fraction(28, 27) * Fraction(64, 63) == Fraction(256, 243), "short holonomy")
    print(json.dumps([certificate(m) for m in (41, 53, 306, 665, 971)], indent=2))


if __name__ == "__main__":
    main()
