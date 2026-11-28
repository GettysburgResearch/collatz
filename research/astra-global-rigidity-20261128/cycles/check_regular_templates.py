"""Replay the centered affine identities used for trajectory templates."""
from fractions import Fraction
from itertools import combinations
from math import prod
import json


def require(flag, message):
    if not flag:
        raise ValueError(message)


def affine(bits):
    carry = 0
    scale = 1
    multiplier = 1
    for bit in bits:
        if bit:
            carry = 3*carry + scale
            multiplier *= 3
        scale *= 2
    return scale, multiplier, carry


def primitive(bits):
    for d in range(1, len(bits)+1):
        if len(bits) % d == 0 and bits[:d] * (len(bits)//d) == bits:
            return bits[:d], len(bits)//d
    raise ValueError("empty block")


def check():
    totals = {k: 0 for k in ("templates", "powered_blocks", "actual_center_returns",
                              "nonzero_two_power_divisors", "nonzero_signed_ratios",
                              "negative_jumps", "positive_jumps", "zero_jumps")}
    for n in list(range(1, 100)) + [(1 << b)-1 for b in range(7, 14)]:
        states = [n]
        bits = []
        for _ in range(14):
            x = states[-1]
            bit = x % 2
            bits.append(bit)
            states.append((3*x+1)//2 if bit else x//2)
        for stops in combinations(range(1, 14), 2):
            boundaries = (0, *stops, 14)
            blocks = []
            for i, j in zip(boundaries, boundaries[1:]):
                base, power = primitive(bits[i:j])
                scale, mult, carry = affine(base)
                require(carry <= 3**len(base)-scale, "word carry height")
                center = Fraction(carry, scale-mult)
                x, y = states[i], states[j]
                require(scale**power*(y-center) == mult**power*(x-center),
                        "powered word center identity")
                if x == center:
                    require(states[i+len(base)] == x, "ordinary center return")
                    totals["actual_center_returns"] += 1
                else:
                    v = (scale-mult)*x-carry
                    require(v % scale**power == 0, "noncenter two-power divisor")
                    totals["nonzero_two_power_divisors"] += 1
                blocks.append((i, j, center, abs(scale-mult)))
                totals["powered_blocks"] += 1
            den = prod(d for _, _, _, d in blocks)
            q = sum(bits)
            c0 = blocks[0][2]
            x0 = 3**q*den*(n-c0)
            jumps = []
            for b, ((i,j,c,_), (_,_,newc,_)) in enumerate(zip(blocks, blocks[1:])):
                xi = den*(c-newc)*(1 << j)*3**(q-sum(bits[:j]))
                require(xi.denominator == 1, "integral jump")
                totals["negative_jumps" if xi<0 else "positive_jumps" if xi>0 else "zero_jumps"] += 1
                if x0 and c != states[j] and all(states[qend] != ctr for _,qend,ctr,_ in blocks[:b]):
                    ratio = abs(c-newc)/abs(states[j]-c)
                    for prv, nxt in zip(blocks[:b],blocks[1:b+1]):
                        a = states[prv[1]]
                        ratio *= abs((a-nxt[2])/(a-prv[2]))
                    require(abs(xi/x0) == ratio, "exact normalized jump")
                    totals["nonzero_signed_ratios"] += int(xi != 0)
                jumps.append(xi)
            marked = x0 + sum(jumps)
            require(marked == (1 << 14)*den*(states[-1]-blocks[-1][2]), "final marked form")
            require(marked.denominator == 1 and marked % (1 << 14) == 0, "common clock divisor")
            totals["templates"] += 1
    return totals


if __name__ == "__main__":
    print(json.dumps(check(), indent=2))
