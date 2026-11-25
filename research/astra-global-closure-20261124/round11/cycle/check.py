"""Exact local windows versus the full rational lap, with both lifts at the seam."""
from fractions import Fraction as F
from itertools import product
from math import ceil, comb, gcd
import json


def require(ok, message):
    if not ok:
        raise ValueError(message)


def lift(items, index):
    lap, rank = divmod(index, len(items))
    return items[rank] * 2**lap


def difference(items, r, v, m):
    return sum((-1)**(m-j) * comb(m, j) * lift(items, r+j*v) for j in range(m+1))


def rational_lap(h, letters):
    p = len(letters)
    D = 2**h - 3**p
    numerator = sum(3**(p-1-j) * lift(letters, j*h) for j in range(p))
    z = [None] * p
    z[0] = F(numerator, D)
    r = 0
    for _ in range(p):
        b, nxt = divmod(r+h, p)
        y = (3*z[r] + letters[r])/2**b
        require(z[nxt] in (None, y), "inconsistent lap")
        z[nxt], r = y, nxt
    require(r == 0 and None not in z, "rotation not primitive")
    return z, D, numerator


def parameters(p, h, maximum, q, a, m):
    offset = q*h-a*p
    v = abs(offset)
    require(v > 0, "zero offset")
    lam = F(3**q, 2**a) if offset > 0 else F(2**a, 3**q)
    D = 2**h - 3**p
    X = F(2 * maximum * p * 2**h, D)
    denominator = 2**a if offset > 0 else 3**q
    E = F(sum(3**(q-1-j) * maximum * 2**((p-1+m*v+j*h)//p)
              for j in range(q)), denominator)
    err = abs(lam-1)
    B = ceil(err**m * X + E*sum(2**j*err**(m-1-j) for j in range(m)))
    J = maximum * 2**((p-1+m*v)//p) * 2**m
    L, M = 0, 1
    while M <= 7*B+J:
        L, M = L+1, 3*M
    return v, B, J, L, M


def window_test(h, letters, data, m, rational=None):
    p = len(letters)
    v, B, J, L, M = data
    increments = [difference(letters, r, v, m) for r in range(p)]
    require(max(map(abs, increments)) <= J, "increment bound")
    residues = []
    for target in range(p):
        r = (target-L*h) % p
        value = 0
        for _ in range(L):
            b, nxt = divmod(r+h, p)
            value = (3*value + increments[r]) * pow(2**b, -1, M) % M
            r = nxt
        require(r == target, "wrong endpoint")
        residues.append((value+M//2) % M-M//2)
    for r in range(p):
        b, nxt = divmod(r+h, p)
        require((2**b*residues[nxt] - 3*residues[r]-increments[r]) % M == 0,
                "window overlap")
        if rational is not None:
            w = difference(rational, r, v, m)
            require(abs(w) <= B and gcd(w.denominator, M) == 1, "height or denominator")
            require((w.numerator-residues[r]*w.denominator) % M == 0, "decoded residue")
    return [r for r, value in enumerate(residues) if abs(value) > B]


def check_word(h, letters, pair, m, maximum=4):
    p = len(letters)
    z, D, numerator = rational_lap(h, letters)
    yes = numerator % D == 0
    require(yes == all(x.denominator == 1 for x in z), "rotated full divisibility")
    data = [parameters(p, h, maximum, q, a, m) for q, a in pair]
    require(pair[1][0]*data[0][0]+pair[0][0]*data[1][0] == p, "two-offset seam")
    bad = [window_test(h, letters, row, m, z) for row in data]
    require(yes == (not any(bad)), "local versus full denominator")
    return {"p": p, "h": h, "difference_order": m, "reduced_denominator": str(z[0].denominator),
            "intercept_scale": maximum//4, "filters": [{"offset": row[0], "bound": row[1],
            "depth": row[3], "failing_ranks": len(bad[i])} for i, row in enumerate(data)]}


def wide_mixed_control():
    p, h = 306, 485
    bands = [int(1 <= r <= 102 and r % 2 == 1) for r in range(p)]
    for r in (60, 239, 112):
        bands[r] = 1
    letters = [4 >> k for k in bands]
    z, _, _ = rational_lap(h, letters)
    odd = [z[r]/letters[r] for r in range(p)]
    s, top = min(odd), max(odd)
    require(s == z[0]/4 and all(z[i] < z[i+1] for i in range(p-1))
            and z[-1] < 2*z[0], "actual dyadic order")
    require(3*s < top < 4*s and (s.numerator-s.denominator) % 9 == 0, "wide floor")
    physical = []
    r = 0
    for _ in range(p):
        b, nxt = divmod(r+h, p)
        a = b+bands[r]-bands[nxt]
        require(a in (1, 2) and 2**a*odd[nxt] == 3*odd[r]+1, "physical edge")
        require(odd[r].numerator % 2 and gcd(odd[r].denominator, 6) == 1, "exact valuation")
        physical.append(odd[r])
        if a == 2:
            physical.append(2*odd[nxt])
        r = nxt
    def ternary(x):
        while x >= 3*s:
            x /= 3
        return x
    mantissas = [ternary(x) for x in physical]
    phases = sorted(range(h), key=lambda idx: mantissas[idx])
    require(len(set(mantissas)) == h and all((phases[(i-p) % h]-phases[i]) % h == 1
            for i in range(h)), "actual ternary rotation")
    mismatches = [sum(bands[(r+t) % p] != bands[r] for r in range(p)) for t in range(p)]
    require(83*min(mismatches[1:p//10+1]) > p and 747*min(mismatches[1:]) > p
            and 20*mismatches[h % p] > p, "round ten cutoffs")
    checked = check_word(h, letters, [(41, 65), (12, 19)], 3)
    return {"odd_width_strict_bounds": [3, 4], "minimum_mismatches": min(mismatches[1:]),
            "temporal_mismatches": mismatches[h % p], "ternary_ranks": len(phases),
            "reduced_denominator_bits": s.denominator.bit_length(), "local_check": checked}


def main():
    p, h = 5, 8
    small_pair = [(1, 1), (1, 2)]
    total = legal = integral = 0
    for tail in product(range(3), repeat=p-1):
        bands = (0,) + tail
        letters = [2**(2-k) for k in bands]
        is_legal = all((r+h)//p+bands[r]-bands[(r+h)%p] in (1, 2) for r in range(p))
        for m in (1, 3):
            out = check_word(h, letters, small_pair, m)
            if m == 1:
                total += 1
                legal += is_legal
                integral += out["reduced_denominator"] == "1"
    # One full-divisor word at (5,8) violates physical edge legality.
    forbidden = [4, 1, 2, 2, 2]
    full_inadmissible = check_word(8, forbidden, small_pair, 2)
    require(full_inadmissible["reduced_denominator"] == "1", "missing positive filter control")
    mixture = [4, 2, 4, 4, 4]
    example = check_word(8, mixture, small_pair, 2)
    mult = int(example["reduced_denominator"])
    cleared = check_word(8, [mult*c for c in mixture], small_pair, 2, 4*mult)
    p, h = 306, 485
    free_bits = [int(1 <= r <= 102 and r % 2 == 1) for r in range(p)]
    large = check_word(h, [4 >> k for k in free_bits], [(41, 65), (12, 19)], 3)
    require((pow(3, 7, 5), pow(3, 4, 5), pow(3, 1, 5)) == (2, 1, 3),
            "single-filter algebra control")
    return {"exhaustive_p5_h8": {"tested_words": total, "physically_legal": legal,
            "whole_divisor_words_without_legality_filter": integral, "orders_checked": [1, 3]},
            "nonphysical_full_divisor": full_inadmissible, "ordinary_intercept_rational": example,
            "scaled_intercept_integer": cleared, "rational_306": large, "wide_mixed": wide_mixed_control(),
            "single_filter_loss": {"modulus": 5, "S": 3, "p": 7, "offset": 4}}


if __name__ == "__main__":
    print(json.dumps(main(), indent=2))
