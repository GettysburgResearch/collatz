"""Reconstruct the complete ternary partition and its ordinary compensated paths."""
import json
import re
from collections import Counter
from fractions import Fraction
from pathlib import Path

from check_ternary_pump import delayed_class, power_class

ROOT = Path(__file__).resolve().parent
K = 2**106
ROOT_STEP = 3**16
ROOT_BASE = 95*pow(K, -1, ROOT_STEP) % ROOT_STEP


def require(ok, label):
    if not ok:
        raise ArithmeticError(label)


def trace(x, clocks):
    bits = []
    for _ in range(clocks):
        odd = x & 1
        bits.append(odd)
        x = (3*x+1)//2 if odd else x//2
    return x, bits


def tree_rows():
    """Parse only the explicit full-arity tree term in the Lean data file."""
    text = (ROOT/"ValuationCover.lean").read_text(encoding="utf-8")
    body = text.split("def trie : Tree :=", 1)[1].split("set_option", 1)[0]
    pat = re.compile(r"\s*(\(\.fork|\(\.leaf\s*⟨[0-9,]+⟩\)|\))")
    tokens = []
    while body.strip():
        match = pat.match(body)
        require(match is not None, "unrecognized certificate token")
        tokens.append(match[1])
        body = body[match.end():]
    stream = iter(tokens)

    def read(residue, depth):
        token = next(stream)
        if token == "(.fork":
            for digit in range(3):
                yield from read(residue+digit*3**depth, depth+1)
            require(next(stream) == ")", "fork arity")
        else:
            require(token.startswith("(.leaf"), "expected leaf")
            yield residue, depth, tuple(map(int, re.findall(r"\d+", token)))

    leaves = list(read(0, 0))
    require(next(stream, None) is None, "one complete tree")
    return leaves


def witness(row, N):
    rank, evens, constant, upper, odds, sign = row
    f = rank+evens
    delta = upper-f
    gain = odds+1-rank
    w, rem = divmod((N << f)-constant, 3**rank)
    require(rem == 0 and w > 0 and w % 48 == 17, "canonical normalization")
    lo, lower_bits = trace(w, f)
    hi, upper_bits = trace(3*w, upper)
    require((lo, sum(lower_bits)) == (N-1, rank), "ordinary lower run and grade")
    require(N % 2**delta == 0, "upper dyadic scale")
    require((hi, sum(upper_bits)) == (3**gain*(N >> delta)+sign-1, odds),
            "ordinary upper run and grade")
    # Each lower full-odd exponent is recovered from the actual trajectory.
    odd_times = [i for i, bit in enumerate(lower_bits) if bit]
    require(odd_times[0] == 0 and lo & 1, "lower odd endpoints")
    endpoints = odd_times[1:]+[f]
    word = [b-a for a, b in zip(odd_times, endpoints)]
    b = 1
    for r, exponent in enumerate(reversed(word)):
        b = (b << exponent)+3**r
    require(b == constant and sum(word) == f, "inverse word and affine intercept")
    return w, lo, hi, lower_bits, upper_bits


def main():
    leaves = tree_rows()
    heights = Counter()
    modes = Counter()
    ranks = Counter()
    upper_max = lower_max = gain_max = delta_max = 0
    mass = Fraction()
    min_gap = None
    for residue, h, row in leaves:
        rank, evens, constant, upper, odds, sign = row
        f, d, g = rank+evens, upper-rank-evens, odds+1-rank
        require(0 <= d <= 100 and g >= 0 and sign in (0, 1, 2), "paid chart grades")
        x, step = ROOT_BASE+ROOT_STEP*residue, ROOT_STEP*3**h
        require((K*x-95) % ROOT_STEP == 0 and 0 <= residue < 3**h, "root and leaf address")
        N = x << 100
        dw, rem = divmod(step << (100+f), 3**rank)
        require(rem == 0 and dw % 48 == 0, "ordinary source stride")
        w, lo, hi, lowbits, highbits = witness(row, N)
        w1, lo1, hi1, lowbits1, highbits1 = witness(row, (x+step) << 100)
        require((lowbits, highbits) == (lowbits1, highbits1), "both representative words")
        require(81*w+271 < 128*N and 81*dw <= 128*(step << 100), "strict source budget")
        require(dw == w1-w and dw % 2**f == 0 and 3*dw % 2**upper == 0,
                "transport of both parity words")
        require(lo1-lo == (dw >> f)*3**rank == step << 100, "lower compensated slope")
        require(hi1-hi == ((3*dw) >> upper)*3**odds == 3**g*(step << (100-d)),
                "upper compensated slope")
        if sign == 0:
            require(d-g >= 5, "earlier Mersenne with funded gap")
            min_gap = d-g if min_gap is None else min(min_gap, d-g)
        elif sign == 1:
            require(2**40*3**g < 2**173, "pure downward return")
        else:
            n, rem = divmod(173-d, 2)
            require(2**40*(2**rem*3**(g+n)+1) < 2**173, "positive turn floor")
        heights[h] += 1
        modes[sign-1] += 1
        ranks[rank] += 1
        mass += Fraction(1, 3**h)
        upper_max, lower_max = max(upper_max, upper), max(lower_max, f)
        delta_max, gain_max = max(delta_max, d), max(gain_max, g)
    require(mass == 1 and len(leaves) == 123, "disjoint exhaustive tree")
    j = power_class(95, 11)
    k = delayed_class(j, 11)
    m = 11+162*j
    N = 1 << m
    z, rem = divmod(128*N-271, 81)
    require(rem == 0 and (z+1) % 3**12 == 0, "literal ordinary hard parent")
    X = N >> 100
    q, rem = divmod(X-ROOT_BASE, ROOT_STEP)
    require(rem == 0, "literal trie coordinate")
    selected = [(v, h, row) for v, h, row in leaves if q % 3**h == v]
    require(len(selected) == 1, "unique actual parameter leaf")
    v, h, row = selected[0]
    w, lo, hi, _, _ = witness(row, N)
    require(0 < w < z and trace(z, 7)[0] == lo, "literal ordinary source and parent share M_m")
    # Both deep and shell families have the same ternary parameter measure in j and k.
    density = sum((Fraction(1, 3**(s-2)) for s in range(6, 16)), Fraction(1, 3**11))
    require(density == Fraction(1, 54)+Fraction(17, 18*3**11), "combined coverage")
    result = {"leaves": len(leaves), "root_X": ROOT_BASE, "root_step": ROOT_STEP,
              "sum_of_leaf_masses": [mass.numerator, mass.denominator],
              "leaves_by_ternary_depth": dict(sorted(heights.items())),
              "leaves_by_lower_odd_grade": dict(sorted(ranks.items())),
              "leaves_by_upper_signed_constant": dict(sorted(modes.items())),
              "maximum_lower_clock": lower_max, "maximum_upper_clock": upper_max,
              "maximum_delta": delta_max, "maximum_gain": gain_max, "minimum_negative_gap": min_gap,
              "d12_ball_address": {"modulus": 3**11, "j": j, "k": k},
              "combined_pump_and_ball_density": [density.numerator, density.denominator],
              "literal_ordinary_parent": {"m": m, "z_bit_length": z.bit_length(),
                  "w_bit_length": w.bit_length(), "upper_endpoint_bits": hi.bit_length(),
                  "trie_residue": v, "trie_depth": h, "row": list(row)}}
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
