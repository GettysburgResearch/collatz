"""Replay signed occupation and denominator clearing with exact integer and rational arithmetic."""
from collections import Counter
from fractions import Fraction
import json

from check_line_shadow_structure import line, rational_step, require, step


def oriented(level, lower, upper):
    raw = line(level, lower, upper)
    return raw if level >= 0 else -raw


def potential(level, shift):
    return max(1, Fraction(abs(shift), 3**abs(level)), -shift)


def check_sources(counts):
    for source in range(1, 1024, 2):
        a, b = step(source), step(3*source)
        gap = 1
        grade = marked = 0
        for _ in range(100):
            low_bit, high_bit = a % 2, b % 2
            next_a, next_b = step(a), step(b)
            if next_a == next_b:
                break
            shift = oriented(gap, a, b)
            next_gap = gap + high_bit - low_bit
            next_shift = oriented(next_gap, next_a, next_b)
            before = potential(gap, shift)
            after = potential(next_gap, next_shift)
            require(shift and next_shift, "collapsed line")
            if low_bit or high_bit:
                require(after <= 2*before, "active signed potential bound")
            else:
                require(after <= before, "increasing common even potential")
            if not gap or shift < 0:
                marked += 1
                if not (low_bit or high_bit):
                    require(2*after == before, "missing marked unit decrease")
                    counts["marked_even"] += 1
                counts["negative_or_balanced"] += 1
            if gap and 0 < shift < 3**abs(gap):
                lo, hi = (a, b) if gap > 0 else (b, a)
                place = 3**abs(gap)
                require(0 < place*lo-hi == shift < place, "one-sided line")
                require((hi+place-1)//place == lo, "wrong ceil")
                for digits in range(1, abs(gap)+1):
                    if shift*3**digits >= place:
                        break
                    require((hi % place)//(place//3**digits) == 3**digits-1,
                            "high ternary digits")
                    counts["ternary_blocks"] += 1
            grade += low_bit+high_bit
            require(marked <= 2*grade, "signed occupation exceeds prefix bound")
            counts["native_steps"] += 1
            a, b, gap = next_a, next_b, next_gap
        counts["ordinary_sources"] += 1


def landing(h, d):
    require(h > 0 and d > 0 and d % 3, "unreduced or nonpositive input")
    start = d
    initial = h
    z = Fraction(d, 3**h)
    word = []
    while h:
        require(z == Fraction(d, 3**h) and z.denominator == 3**h, "lost reduced state")
        bit = d % 2
        word.append(bit)
        if bit:
            h -= 1
            d = (d+3**h)//2
        else:
            d //= 2
        z = rational_step(z)
        require(d <= max(start, 3**initial), "numerator envelope")
    require(sum(word) == initial and z == d and d > 0, "first integer landing")
    return word, d


def lifted(h, m, word, target, counts):
    modulus = 2**len(word)
    a = (m*pow(3**h, -1, modulus)) % modulus + (m+1)*modulus
    b = 3**h*a-m
    x = Fraction(m, 3**h)
    for bit in word:
        require(b and b%2 == 0 and a%2 == bit, "wrong lifted bit")
        require(a != b, "merged lift")
        require(3**h*a-b == 3**h*x, "moving integer affine line")
        a, b = step(a), step(b)
        x = rational_step(x)
        h -= bit
        counts["lifted_native_steps"] += 1
    require(h == 0 and a-b == target == x, "wrong ordinary landing line")


def check_landings(counts):
    rows = []
    for h in range(1, 8):
        best = 0
        samples = 0
        for m in range(1, 3**h+1):
            if not m%3:
                continue
            word, target = landing(h, m)
            best = max(best, len(word))
            samples += 1
            counts["native_rational_steps"] += len(word)
            counts["landing_one"] += target == 1
            counts["other_landing"] += target > 1
            if m <= 30 or m >= 3**h-6:
                lifted(h, m, word, target, counts)
                counts["ordinary_lifts"] += 1
        rows.append({"exponent": h, "tested": samples, "largest_time": best})
    counts["distinct_exact_exponents"] = len(rows)
    return rows


def main():
    counts = Counter()
    check_sources(counts)
    rows = check_landings(counts)
    for required in ("marked_even", "ternary_blocks", "landing_one", "other_landing", "ordinary_lifts"):
        require(counts[required] > 0, f"missing control {required}")
    print(json.dumps({"counts": dict(counts), "bounded_landings": rows}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
