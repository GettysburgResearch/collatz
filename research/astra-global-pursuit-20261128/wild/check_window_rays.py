"""Exact ordinary controls for prescribed predecessor windows."""
from fractions import Fraction
import itertools
import json


def require(condition, detail):
    if not condition:
        raise RuntimeError(detail)


def shortcut(value):
    return (3 * value + 1) // 2 if value % 2 else value // 2


def fast_odd_step(value):
    numerator = 3 * value + 1
    return numerator // (numerator & -numerator)


def spine_step(value, period):
    modulus = 9 * (period // 2)
    exponent = next(e for e in range(3, 3 * period + 3)
                    if pow(2, e, modulus) * value % modulus == 4 % modulus)
    parent = ((value << exponent) - 1) // 3
    require(parent % (modulus // 3) == 1, "spine residue")
    require(fast_odd_step(parent) == value, "spine edge")
    require(parent * 3 >= 7 * value, "spine growth")
    return parent, exponent


def affine_data(word):
    carry = 0
    for step, digit in enumerate(word):
        if digit:
            carry = 3 * carry + (1 << step)
    return sum(word), carry


def checked_cells():
    counts = {"spine_edges": 0, "prescribed_paths": 0, "shortcut_edges": 0}
    for length in range(4):
        for word in itertools.product(range(2), repeat=length):
            odds, carry = affine_data(word)
            for k in range(2):
                modulus = 3 ** (odds + k)
                period = 2 * modulus
                for target in (1, 5, 7, 11):
                    value = target
                    spine_back = []
                    for depth in range(1, 5):
                        value, gap = spine_step(value, period)
                        if depth > 1:
                            require(gap % period == 2 % period, "fixed phase")
                        spine_back.insert(0, gap)
                        counts["spine_edges"] += 1
                        for residue in range(3 ** k):
                            endpoint_r = ((carry + 3 ** odds * residue)
                                          * pow(2, -length, modulus)) % modulus
                            lift = next(e for e in range(1, period + 1)
                                        if pow(2, e, 3 * modulus)
                                        == 3 * endpoint_r + 1)
                            for extra in (0, period):
                                exponent = lift + extra
                                z = ((value << exponent) - 1) // 3
                                numerator = (z << length) - carry
                                require(numerator % 3 ** odds == 0, "word integrality")
                                start = numerator // 3 ** odds
                                if start < 1:
                                    continue
                                require(start % 3 ** k == residue, "ordinary residue")
                                cur = start
                                for digit in word:
                                    require(cur % 2 == digit, "native word")
                                    cur = shortcut(cur)
                                require(cur == z, "native word endpoint")
                                for elapsed in [exponent] + spine_back:
                                    require(cur % 2 == 1, "odd node")
                                    for _ in range(elapsed):
                                        cur = shortcut(cur)
                                require(cur == target, "target endpoint")
                                counts["prescribed_paths"] += 1
                                counts["shortcut_edges"] += length + exponent + sum(spine_back)
    return counts


def checked_windows():
    # For empty prefix and J=0, P=2. Each selected rational p/q below
    # has gcd 1 and |q alpha-p|<1/q, certified without floating point.
    # These two properties alone suffice for the covering proof.
    witnesses = [Fraction(1, 5), Fraction(5, 24), Fraction(11, 53)]
    count = 0
    max_bits = 0
    for ratio in witnesses:
        p, q = ratio.numerator, ratio.denominator
        centre = q * (2 * q - 2 * p)
        require(2 ** (centre - 2) < 3 ** (q * q) < 2 ** (centre + 2),
                "rotation spacing")
        value, _ = spine_step(1, 2)
        spine = [value]
        for _ in range(2 * q):
            value, _ = spine_step(value, 2)
            spine.append(value)
        for lead in (72 * q, 72 * q + 3, 72 * q + 11):
            for high in (16, 19, 23, 27, 31):
                x = high << (lead - 4)
                found = False
                for value in spine[q:2 * q]:
                    # E even, so every source is an actual integer parent.
                    approx = x.bit_length() - value.bit_length()
                    for e in range(max(2, approx - 4), approx + 10):
                        if e % 2:
                            continue
                        n = ((value << e) - 1) // 3
                        if n >= x and n ** q <= (x ** q << 12):
                            require(fast_odd_step(n) == value, "window target")
                            found = True
                            break
                    if found:
                        break
                require(found, "window certificate")
                count += 1
                max_bits = max(max_bits, x.bit_length())
    return {"rotation_approximants": len(witnesses),
            "ordinary_translated_windows": count,
            "largest_test_location_bits": max_bits}


if __name__ == "__main__":
    print(json.dumps(checked_cells() | checked_windows(), indent=2, sort_keys=True))
