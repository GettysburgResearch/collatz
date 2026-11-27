"""Exact finite controls for affine elimination and the mechanical segment bound."""

from fractions import Fraction as Q
from math import gcd


def require(condition):
    if not condition:
        raise RuntimeError("arithmetic control failed")


def join(a, b):
    u, c = a
    v, d = b
    return v * u, v * c + d


def affine(word, maps):
    result = Q(1), Q(0)
    for bit in word:
        result = join(result, maps[int(bit)])
    return result


def comm(a, b):
    u, c = a
    v, d = b
    return (u - 1) * d - (v - 1) * c


def is_unit(x):
    def strip(k):
        for prime in (2, 3):
            while k and k % prime == 0:
                k //= prime
        return k
    return strip(abs(x.numerator)) == strip(x.denominator) == 1


def dictionaries(depth):
    layer = {("0", "1")}
    all_pairs = set(layer)
    for _ in range(depth):
        new = set()
        for a, b in layer:
            new.update(((b, a), (a, a + b), (a, b + a),
                        (a + b, b), (b + a, b)))
        layer = new - all_pairs
        all_pairs.update(layer)
    return sorted(all_pairs)


def bounded_factors(word):
    # Count cyclic factors at every relevant length, including wraparound.
    length = len(word)
    period = word + word
    for k in range(1, length + 1):
        require(len({period[i:i + k] for i in range(length)}) <= k + 1)


def affine_controls():
    physical = ((Q(1, 2), Q(0)), (Q(3, 2), Q(1, 2)))
    companion = ((Q(3, 2), Q(0)), (Q(3, 4), Q(1, 4)))
    dictionaries_checked = dictionaries(4)
    seeds = ["10", "00101101", "0011", "001", "110",
             "1010", "01010", "0001111"]
    cut_checks = exact_checks = 0
    for a, b in dictionaries_checked:
        bounded_factors(a)
        bounded_factors(b)
        require(abs(len(a)*b.count("1") - len(b)*a.count("1")) == 1)
        for maps in (physical, companion):
            left, right = affine(a, maps), affine(b, maps)
            u, c = left
            v, _ = right
            delta = comm(left, right)
            require(is_unit(delta))
            for w in seeds:
                expansion = "".join((a, b)[int(e)] for e in w)
                slope, carry = affine(expansion, maps)
                require((slope, carry) == affine(w, (left, right)))
                suffix = Q(1)
                s1 = Q(0)
                for bit in reversed(w):
                    if bit == "1":
                        s1 += suffix
                    suffix *= (u, v)[int(bit)]
                require((u - 1)*carry == c*(slope - 1) + delta*s1)
                raw = abs((slope - 1).numerator)
                phase = carry/(1 - slope)
                require(raw % phase.denominator == 0)
                removed = raw // phase.denominator
                predicted = gcd(raw, s1.numerator)
                require(predicted % removed == 0)
                require(gcd(raw, (u - 1).numerator) % (predicted // removed) == 0)
                if w == "10":
                    require(phase.denominator == raw)
                    exact_checks += 1
                if w == "00101101":
                    require(s1 == (u*v + 1)*(u*v*v + 1))
                cut_checks += 1
    w = "10"
    for expected in (Q(1), Q(-10), Q(37, 5)):
        slope, carry = affine(w, physical)
        require(carry/(1 - slope) == expected)
        w = "".join("01" if c == "1" else "1" for c in w)
    return len(dictionaries_checked), cut_checks, exact_checks


def exception_controls():
    # Symbolic restriction to XY = -1, by collecting the powers of X.
    seed = "011100110010"
    exponents = {}
    zeros = ones = 0
    for bit in reversed(seed):
        if bit == "1":
            key = zeros - ones
            exponents[key] = exponents.get(key, 0) + (-1)**ones
            ones += 1
        else:
            zeros += 1
    require(exponents == {0: -1, 1: 3, 2: -2})
    require(sum(c*Q(1, 2)**i for i, c in exponents.items()) == 0)
    require(sum(c*Q(3, 2)**i for i, c in exponents.items()) == -1)
    physical = ((Q(1, 2), Q(0)), (Q(3, 2), Q(1, 2)))
    for k in range(1, 41):
        blocks = physical[0], affine("0"*k + "1", physical)
        slope, carry = affine(seed, blocks)
        raw = abs((slope - 1).numerator)
        closed = carry/(1 - slope)
        removed = raw // closed.denominator
        require(removed % (3 + 2**(k + 2)) == 0)
    return 40


def physical_controls():
    """Test (4/3)^k ≤ 3(y+1)/2 with exact integers on injective paths."""
    checked = 0
    for start in range(1, 701):
        y = start
        seen = set()
        bits = ""
        while y not in seen and len(bits) < 80:
            seen.add(y)
            bits += str(y % 2)
            y = (3*y + 1)//2 if y % 2 else y//2
        for length in range(3, len(bits) + 1):
            k = (length - 1)//2
            words = [bits[i:i+k] for i in range(k + 2)]
            if len(set(words)) <= k + 1:
                require(2*4**k <= 3**(k + 1)*(start + 1))
                checked += 1
    return checked


if __name__ == "__main__":
    pairs, cuts, exact = affine_controls()
    segments = physical_controls()
    exceptions = exception_controls()
    print(f"{pairs} dictionaries; {cuts} affine/valuation checks; "
          f"{exact} exact seed-10 denominators; {segments} physical segments; "
          f"{exceptions} exceptional specializations")
