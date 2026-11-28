"""Both signed closure ranks and repetition lcm arithmetic on true trajectories."""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import product
from math import gcd, lcm, prod
import json

from check_mismatch_event_factors import factors, valuation_rank
from check_rotation_occupation import lifted, require


@lru_cache(maxsize=None)
def factor_row(n):
    return factors(n)


def lucas_boundaries(y, a, b, c, q, counts):
    common = gcd(y[0], c)
    normalized = [d//common for d in y]
    require(all(gcd(d, q*c) == common for d in y), "fixed repeated map gcd")
    require(all(b*y[i+1] == a*y[i]+q*c for i in range(len(y)-1)), "literal repeated affine law")
    V = [1]+[(b**h-a**h)//(b-a) for h in range(1, len(y))]
    surplus = prod(normalized)//lcm(*normalized)
    require(prod(V) % surplus == 0, "all repeated prime levels in the Lucas factorial")
    rank = valuation_rank([factor_row(d) for d in y])
    require(lcm(*y) <= max(y)**rank, "lcm versus original unscaled rank")
    counts["actual_repeated_boundary_systems"] += 1
    counts["repeated_systems_with_removed_nonunit_gcd"] += common > 1
    counts["repeated_systems_with_nonunit_lcm_surplus"] += surplus > 1


def signed_closure(n, bits, states, counts):
    t = len(bits)
    w = sum(bits)
    if not w:
        return
    det = 2**t-3**w
    numerator = 2**t*states[-1]-3**w*n
    value = Fraction(numerator, det)
    q = value.denominator
    y = value.numerator
    phases, odd_dates = [], []
    for i, b in enumerate(bits):
        require(y % 2 == b and gcd(y, q) == 1, "exact reduced rational shortcut cylinder")
        if b:
            odd_dates.append(i)
            phases.append(abs(y))
        y = (3*y+q)//2 if b else y//2
    require(y == value.numerator, "all displayed rational phases close")
    next_dates = odd_dates[1:]+[odd_dates[0]+t]
    edges = [j-i for i, j in zip(odd_dates, next_dates)]
    sign = 1 if det > 0 else -1
    require(all(2**edges[i]*phases[(i+1) % w] == 3*a+sign*q for i, a in enumerate(phases)),
            "signed reduced odd numerator law including cyclic seam")
    rank = valuation_rank([factor_row(a) for a in phases])
    rank_cost = rank*(rank+2)
    if sign == 1:
        require(q**w <= 2**(t+rank_cost*(2*t-w)), "positive complete rank inequality")
        counts["positive_signed_prefixes"] += 1
    else:
        circumference = Fraction(3**w*2**(t-w))
        for i, a in enumerate(phases):
            circumference *= max(Fraction(1), Fraction(a, phases[(i+1) % w]))
        require(prod(phases) <= circumference**rank_cost, "negative numerator height mass")
        require(circumference <= Fraction(3**(2*w)*2**t, 2**(2*w)),
                "negative whole-lap variation ledger")
        require(q**w < 3**w*prod(phases), "negative q versus actual phases")
        counts["negative_signed_prefixes"] += 1
    require(2**t <= n*4**w, "true positive source enforces odd count")
    counts["prefixes_at_ordinary_returns"] += states[-1] == n
    counts["nonreturn_prefixes_with_complete_cancellation"] += states[-1] != n and 1 < q < abs(det)
    if sign == 1 and 1 in states[:-1]:
        entrance = states.index(1)
        cuts = [(i, a) for i, a in zip(odd_dates, phases) if i >= entrance]
        if len(cuts) >= 3 and all(j-i == 2 for (i, _), (j, _) in zip(cuts, cuts[1:])):
            lucas_boundaries([a for _, a in cuts], 3, 4, 1, q, counts)


def main():
    counts = Counter()
    for n in (1, 2, 3, 5, 7, 9, 13, 17, 19, 25, 27, 31, 41, 65, 87):
        states, bits = [n], []
        for _ in range(29):
            x = states[-1]
            bits.append(x % 2)
            states.append((3*x+1)//2 if x % 2 else x//2)
            signed_closure(n, bits, states, counts)
    for size in (2, 3):
        for block in product((1, 2, 3), repeat=size):
            a, b = 3**size, 2**sum(block)
            if a == b:
                continue
            carry, total = 0, 0
            for v in block:
                carry = 3*carry+2**total
                total += v
            for end in product((1, 2, 3), repeat=2):
                word = block*3+end
                if any(word[h:]+word[:h] == word for h in range(1, len(word))):
                    continue
                cycle = lifted(word)
                if cycle is None:
                    continue
                q, nums = cycle
                boundaries = [nums[i*size] for i in range(4)]
                lucas_boundaries(boundaries, a, b, carry, q, counts)
    require(len(counts) == 7 and all(counts.values()), "both signs, reductions and prime reuse exercised")
    return counts


if __name__ == "__main__":
    print(json.dumps(main(), indent=2, sort_keys=True))
