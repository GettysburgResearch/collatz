"""Finite reconstruction of the physical prefix, partial carries, and coding examples."""
from fractions import Fraction
from math import isqrt
import json


def require(ok, context):
    if not ok:
        raise ArithmeticError(context)


def orbit(start, count):
    states = [start]
    for _ in range(count):
        x = states[-1]
        states.append((3 * x + 1 if x % 2 else x) // 2)
    return states


def weighted(bits):
    result = []
    weight = 0
    for j, bit in enumerate(bits):
        weight += bit
        result.append(Fraction(bit * 2**j, 3**weight))
    return weight, result


def verify_pairs():
    checks = 0
    for start in range(1, 129):
        states = orbit(start, 48)
        bits = [x % 2 for x in states]
        for shift in (1, 2, 5, 11):
            for n in (1, 6, 12, 25, 33):
                p, left = weighted(bits[:n])
                r, right = weighted(bits[shift : shift + n])
                parts = [sum(y - x for x, y in zip(left[j::4], right[j::4]))
                         for j in range(4)]
                lhs = states[shift] - start + sum(parts)
                rhs = 2**n * (Fraction(states[shift+n], 3**r)
                              - Fraction(states[n], 3**p))
                require(lhs == rhs, (start, shift, n))
                require(lhs.numerator % 2**n == 0, ("dyadic", start, shift, n))
                for word, total in ((left, p), (right, r)):
                    carry = sum(word) * 3**total
                    require(0 <= carry <= 3**n-2**n, ("carry", carry, n))
                checks += 1
    return checks


def floor_rot(n, channel):
    # floor(n*(sqrt(2)-1) + channel/4), computed with integers.
    return (isqrt(32*n*n) + channel) // 4 - n


def rotation_rows():
    rows = []
    for q in (5, 29, 169, 985):
        # Positive-error convergents have q*theta just above an integer.
        words = []
        for n in range(2*q):
            label = [floor_rot(n+1, i)-floor_rot(n, i) for i in (0, 3)]
            words.append("11110" + "".join("110" if b else "10" for b in label))
        p = floor_rot(q, 0)
        changed = {j for i in (0, 3) for n in range(1, q)
                   if floor_rot(n+q, i)-floor_rot(n, i) != p
                   for j in (n-1, n)}
        begin = length = 0
        while begin < q:
            end = begin+1
            bad = begin in changed
            while end < q and (end in changed) == bad:
                end += 1
            a = "".join(words[begin:end])
            b = "".join(words[q+begin:q+end])
            require((len(a), a.count("1")) == (len(b), b.count("1")), (q, begin))
            if bad:
                length += len(a)
            else:
                require(a == b, ("outside", q, begin))
            begin = end
        rows.append(dict(symbol_shift=q, native_shift=sum(map(len,words[:q])),
                         charged_native_length=length))
    return rows


if __name__ == "__main__":
    print(json.dumps(dict(ordinary_pairs=verify_pairs(), rotation=rotation_rows()),
                     indent=2))
