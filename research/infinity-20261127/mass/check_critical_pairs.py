"""Construct and replay common-middle translations on the actual critical rational census."""
import hashlib
import json
import random
from fractions import Fraction as F


def demand(condition, message):
    if not condition:
        raise RuntimeError(message)


DIGITS = (65, 73, 85, 103)
BLOCKS = {65: (1, 1, 1, 2), 73: (1, 1, 2, 1),
          85: (1, 2, 1, 1), 103: (2, 1, 1, 1)}
ILO, IHI = F(65, 49), F(103, 49)


def bits_for(gaps):
    bits = []
    for e in gaps:
        bits.extend([1]+[0]*(e-1))
    return bits


def offset(bits):
    c, dyad = 0, 1
    for bit in bits:
        if bit:
            c = 3*c + dyad
        dyad *= 2
    return c


def floor_log3(j):
    return (3**j).bit_length()-1


def head(J, r, x, s, endpoint, h):
    # Three to five shared unit gaps suffice in these rows.
    normalized = (s * (endpoint-F(1, 2**(h+1))) - x - (1-F(2,3)**r))/F(2,3)**r
    balanced = []
    swaps = []
    base, ratio = F(0), F(1)
    dyad, triad = 1, 1
    for M in range(J - 2 - r):
        if M % 4 == (J - 2 - r) % 4:
            center = base + F(5,9)*ratio
            inner = ratio*F(4,9)
            if center + inner*IHI >= normalized:
                gaps = balanced.copy()
                for i, drop in swaps:
                    if center + inner*ILO <= normalized:
                        break
                    gaps[i-1:i+1] = [1,2]
                    center -= drop
                if center + inner*ILO <= normalized <= center + inner*IHI:
                    break
        triad *= 3
        next_dyad = 1 << (triad.bit_length()-1)
        e = (next_dyad//dyad).bit_length()-1
        if balanced and balanced[-1] == 2 and e == 1:
            swaps.append((M, ratio/6))
        balanced.append(e)
        base += ratio/3
        ratio = F(next_dyad, triad)
        dyad = next_dyad
    else:
        raise RuntimeError("could not bracket residual with balanced carry")
    rem = (normalized-center)/inner
    L = (J-2-r-M)//4
    suffix = []
    for _ in range(L):
        digit = next(c for c in DIGITS if ILO <= (81*rem-c)/32 <= IHI)
        rem = (81*rem-digit)/32
        suffix.extend(BLOCKS[digit])
    bits = bits_for([1]*r + gaps + [1,1] + suffix)
    demand(sum(bits) == J and ILO <= rem <= IHI, "head grade")
    got = F(offset(bits), 3**J)
    residual = s*(endpoint-F(1,2**(h+1))) - x - got
    demand(residual == F(2**len(bits),3**J)*rem, "carry residual")
    return bits, {"M":M, "L":L}


def bridge(l, tag):
    m = floor_log3(l)
    bits = [1]*l + [0]*(m-l)
    rng = random.Random(tag)
    # A cyclic rotation at the slope-l/m minimum gives a passing local bridge.
    for _ in range(100):
        rng.shuffle(bits)
        height, minimum, pos = 0, 0, 0
        for i, b in enumerate(bits, 1):
            height += m*b-l
            if height < minimum:
                minimum, pos = height, i
        word = bits[pos:]+bits[:pos]
        if offset(word) <= 100*3**l:
            return word
    raise RuntimeError("no marked bridge")


def short_digest(a):
    raw = abs(a).to_bytes((abs(a).bit_length()+7)//8, "big")
    return hashlib.sha256(raw).hexdigest()[:16]


def physical(K, bits, y, h):
    n = len(bits)
    den = 3**K
    a = 2**n*y - offset(bits)
    demand(a % 3 != 0 and a % 2 == 1 and 2**n <= 2*a < 13*2**n, "six-lift interval/reduction")
    v, pow2, pow3, clear = a, 1, 1, None
    for j, expected in enumerate(bits, 1):
        odd = v % 2
        demand(odd == expected, "recorded bit disagrees with actual rational step")
        if odd:
            demand(den > 1, "unexpected ordinary odd step")
            den //= 3
            v = (v+den)//2
            pow3 *= 3
        else:
            v //= 2
        pow2 *= 2
        demand(v > 0 and (den == 1 or v % 3 != 0), "positivity/reduction")
        demand(pow3 >= pow2, "physical prefix gate")
        if den == 1 and clear is None:
            clear = j
            demand(v == y << h, "first-clearance landing")
    demand(clear == n-h and v == y, "final actual ordinary endpoint")
    return a


def measure_phase(K, sstar):
    n = floor_log3(K-1)+1
    return abs(F(2**n,3**K)-sstar)


def packet(J, initial_K, r, x, targets, phase_search):
    n0 = floor_log3(initial_K-1)+1
    s0 = F(1,2) if phase_search else F(2**n0,3**initial_K)
    builds = [head(J,r,x,s0,y,h) for y,h in targets]
    P = max(len(bits) for bits,_ in builds)
    heads = [bits+[0]*(P-len(bits)) for bits,_ in builds]
    demand(all(bits[:r] == [1]*r and sum(bits) == J for bits in heads), "common physical head")
    coeff = [y-F(1, 2**(h+1)) for y,h in targets]
    head_diff = offset(heads[1])-offset(heads[0])
    c = coeff[1]-coeff[0]
    sstar = F(head_diff,3**J)/c
    demand(F(1,3)<sstar<F(2,3), "interior tuning phase")
    K = min(range(initial_K,initial_K+1024), key=lambda k:measure_phase(k,sstar)) if phase_search else initial_K
    D = 3**K
    n = floor_log3(K-1)+1
    l = K-J-1
    m = floor_log3(l)
    # Select several actual positive passing bridges, then apply the same two heads to each.
    diffs, records, seen = set(), [], set()
    predicted = c*2**n - 3**(K-J)*head_diff
    demand(predicted.denominator == 1 and predicted and predicted % 2**r == 0, "translation identity/divisibility")
    for tag in (119,234,453,987,1575):
        w = bridge(l,tag)
        nums = []
        for u,(y,h) in zip(heads,targets):
            z = n-h-1-P-m
            demand(z>=0, "clock reserve")
            full = u+w+[0]*z+[1]+[0]*h
            nums.append(physical(K,full,y,h))
        a,b = nums
        demand(a not in seen, "duplicate freely varied middle")
        seen.add(a)
        diffs.add(b-a)
        demand(F(b-a,D) == c*(F(2**n,D)-sstar), "phase identity")
        demand(all(abs(F(v,D)-x)<F(1,10) for v in nums), "both real starts near prescribed center")
        records.append([short_digest(a),short_digest(b)])
    demand(diffs == {int(predicted)}, "translation depends on shared middle")
    delta = abs(int(predicted))
    if not phase_search:
        demand(delta*2**100<D, "insufficient near-source accuracy")
    return {"K":K,"n":n,"J":J,"P":P,"middle_length":m,"r":r,
            "heads":[info for _,info in builds], "targets":[y for y,_ in targets],
            "phase_search":phase_search, "translation_digest":short_digest(delta),
            "real_distance_bits_floor":(D//delta).bit_length()-1,
            "dyadic_agreement_bits":(delta & -delta).bit_length()-1,
            "paired_source_digests":records}


def visit_five(s):
    seen = set()
    while s not in seen and s != 1:
        seen.add(s)
        s = (3*s+1)//2 if s%2 else s//2
    demand(s == 1, "control target did not converge")
    return 5 in seen


def main():
    for c, w in BLOCKS.items():
        demand(offset(bits_for(w)) == c and len(bits_for(w)) == 5, "refinement digit")
    demand(all(F(a,81)+F(32,81)*IHI >= F(b,81)+F(32,81)*ILO
               for a,b in zip(DIGITS,DIGITS[1:])), "digit gap")
    demand(not visit_five(113) and visit_five(509), "finite defect control")
    rows = [
        packet(1000,1871,3,F(5,4),[(17,1),(51,0)],False),
        packet(1200,1780,3,F(5,4),[(17,1),(51,0)],True),
        packet(4600,5101,3,F(5,4),[(113,1),(509,1)],True),
    ]
    print(json.dumps(rows, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
