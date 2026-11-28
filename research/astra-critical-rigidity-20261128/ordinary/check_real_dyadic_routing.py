"""Construct exact binary/real first preimages, then run the actual forward map."""
from collections import Counter
from fractions import Fraction
from itertools import product
import json
from check_line_shadow_structure import require
from check_reciprocal_landing import landed
from check_target_renewal import mapped


def route(N, w, lo, hi):
    require(N > 0 and N % 3 != 2 and 0 <= lo < hi, "invalid mark or open interval")
    left, right = mapped(w,lo,hi)
    z, v = (left+right)/2, (right-left)/2
    z_scaled, b = z, 0
    while z_scaled >= 2:
        z_scaled /= 2
        b += 1
    rho = Fraction(8,9)
    q = Fraction(2*N-1,3)
    k0, power = 0, Fraction(1)
    while 10*power >= v/2**b or power*q > z_scaled+8:
        k0 += 1
        power *= rho
    first, H = power*q, 0
    while first < z_scaled+8:
        first *= 2
        H += 1
    k = k0
    while first > z_scaled+8:
        first *= rho
        k += 1
    require(k-k0 <= 6 and 5 <= first-z_scaled <= 10, "uniform six-step scale")
    carry = first-z_scaled
    outer = []
    for _ in range(k):
        if 5 <= (carry-Fraction(5,9))/rho <= 10:
            outer.append(5)
        else:
            outer.append(10)
        carry = (carry-Fraction(outer[-1],9))/rho
        require(5 <= carry <= 10,"carry-cover preimage")
    reverse_bits = [1] + [0]*H
    for c in reversed(outer):
        reverse_bits.extend((0,1,1) if c == 5 else (1,1,0))
    reverse_bits.extend([0]*b)
    reverse_bits.extend(reversed(w))
    m, h = N, 0
    for bit in reverse_bits:
        m = 2*m-bit*3**h
        h += bit
        require(m > 0 and m % 3, "nonpositive or reduced-height failure inside route")
    require(h == sum(w)+2*k+1 and lo < Fraction(m,3**h) < hi,
            "unmet grade or open real source")
    native, result = landed(h,m)
    require(tuple(reversed(reverse_bits)) == native and native[:len(w)] == w
            and result == N, "wrong first integral mark or native word")
    return dict(clock=len(native), grade=h, prefix=len(w), adjust=k-k0,
                block5=outer.count(5),block10=outer.count(10))


def main():
    counts, extreme = Counter(), []
    for length in range(5):
        for w in product((0,1), repeat=length):
            for N in (1,3,4,6,10,37):
                for lo,hi in ((Fraction(),Fraction(1,2)),
                              (Fraction(53,7),Fraction(54,7))):
                    r = route(N,w,lo,hi)
                    counts["full_binary_word_mark_windows"] += 1
                    counts["low_carry_motifs"] += r["block5"]
                    counts["high_carry_motifs"] += r["block10"]
                    counts["true_native_dates"] += r["clock"]
    for N,w,lo,hi in ((3**67+1,(0,)*75,Fraction(0), Fraction(1,2**50)),
                      (1,(1,)*60,Fraction(72000),Fraction(72001)),
                      (3**80, (1,0,1,1)*13,Fraction(27)-Fraction(1,2**41),
                       Fraction(27)+Fraction(1,2**41))):
        r = route(N,w,lo,hi)
        extreme.append(r)
        counts["true_native_dates"] += r["clock"]
    require(counts["full_binary_word_mark_windows"] == 372 and counts["low_carry_motifs"]
            and counts["high_carry_motifs"], "missing physical coverage")
    print(json.dumps(dict(scope="Exact finite backwards constructions and genuine forward first landings",
                          counts=dict(counts), extreme_routes=extreme),indent=2,sort_keys=True))


if __name__ == "__main__":
    main()
