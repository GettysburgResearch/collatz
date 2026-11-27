"""Exact controls for rank gaps of two physical odd rational cycles."""
from collections import Counter
from fractions import Fraction
from math import gcd
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def chart(word):
    p = len(word)
    h = sum(word)
    carry = 0
    clock = 0
    for exponent in word:
        carry = 3 * carry + 2**clock
        clock += exponent
    initial = Fraction(carry, 2**h - 3**p)
    current = initial
    sites = []
    for exponent in word:
        require(current > 0 and current.numerator % 2 == 1, "illegal rational site")
        sites.append(current)
        current = (3 * current + 1) / 2**exponent
    require(current == initial and len(set(sites)) == p, "nonprimitive orbit")
    s = min(sites)
    bands = []
    mantissas = []
    for x in sites:
        k = 0
        while x >= 2**(k+1) * s:
            k += 1
        require(k <= 2, "outside the three-band chart")
        bands.append(k)
        mantissas.append(x / 2**k)
    ordered = sorted(range(p), key=mantissas.__getitem__)
    denominator = s.denominator
    Z = [4 * denominator * mantissas[i] for i in ordered]
    require(all(z.denominator == 1 for z in Z), "uncleared mantissa")
    c = [denominator * 2**(2-bands[i]) for i in ordered]
    require(gcd(p, h) == 1, "nonprimitive rank rotation")
    return h, [int(z) for z in Z], c


def lifted(seq, r):
    laps, rank = divmod(r, len(seq))
    return seq[rank] * 2**laps


def control(word):
    h, Z, c = chart(word)
    p = len(Z)
    counts = Counter()
    for r in range(3*p):
        require(lifted(Z, r+h) == 3*lifted(Z, r) + lifted(c, r), "rank recursion")
    for t in range(1, p):
        G = [lifted(Z, r+t)-Z[r] for r in range(p)]
        J = [lifted(c, r+t)-c[r] for r in range(p)]
        for r in range(p):
            b, dest = divmod(r+h, p)
            require(G[r] > 0 and 2**b*G[dest] == 3*G[r]+J[r], "gap recurrence")
            counts["base_gap_edges"] += 1
            counts["input_cut_edges"] += (r+t >= p)
            counts["output_upper_endpoint_crosses_cut"] += (dest+t >= p)
        for length in range(1, min(10, p+2)):
            a = length // 2
            previous = {}
            for start in range(p):
                ranks = [(start+i*h) % p for i in range(length+1)]
                code = tuple(((r+h)//p, J[r]) for r in ranks[:-1])
                bm = sum(b for b, _ in code[:a])
                bp = sum(b for b, _ in code[a:])
                modulus = 3**a * 2**bp
                center = G[ranks[a]]
                if code in previous:
                    diff = center-previous[code]
                    require(diff % modulus == 0, "actual midpoint residue")
                    counts["repeated_word_pairs"] += 1
                    counts["nonzero_actual_differences"] += (diff != 0)
                previous[code] = center
                # Same integral affine recurrence on a translated test path.
                shifted = G[start] + 2**(bm+bp)
                for idx in range(a):
                    b, j = code[idx]
                    shifted, remainder = divmod(3*shifted+j, 2**b)
                    require(remainder == 0, "translated prefix legality")
                require(shifted-center == modulus, "sharp mixed-place product")
                for b, j in code[a:]:
                    shifted, remainder = divmod(3*shifted+j, 2**b)
                    require(remainder == 0, "translated suffix legality")
                require(shifted-G[ranks[-1]] == 3**length, "translated terminal difference")
                counts["tested_windows"] += 1
    return {"period": p, "clock": h, **dict(counts)}


if __name__ == "__main__":
    lhs = (6*82**82)**521
    rhs = 81**(81*521)*3**(82*42)
    require(lhs < rhs, "entropy threshold")
    words = ["11222", "12112212212212121212212121221221212121222"]
    print(json.dumps({
        "entropy_comparison_bit_lengths": [lhs.bit_length(), rhs.bit_length()],
        "physical_rational_examples": [control(list(map(int, word))) for word in words],
    }, indent=2))
