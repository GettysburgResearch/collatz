"""Exact adversarial checks for polynomial pullback and the signed difference bound."""

from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb, gcd
import json
import random


def require(condition, error):
    if not condition:
        raise ValueError(error)


def v3(x):
    if not x:
        raise ValueError("valuation of zero")
    n = x
    power = 0
    while n % 3 == 0:
        n //= 3
        power += 1
    return power


def eval_poly(coefficients, x):
    y = 0
    for c in reversed(coefficients):
        y = x * y + c
    return y


def best_binary(values):
    """Largest multiplicity captured by any two-child target, using actual residues."""
    distinct = Counter(values)
    if len(distinct) < 2:
        return sum(distinct.values())
    classes = [[], [], []]
    for x, count in distinct.items():
        e = x % 3
        classes[e].extend([(x - e) // 3] * count)
    counts = sorted((best_binary(group) for group in classes), reverse=True)
    return counts[0] + counts[1]


def certify_integer_scaled_input(coefficients, denom, offset, k):
    # Multiplication of all integral-at-three outputs by a 3-adic unit preserves
    # the exact equality/difference tree, so the prime-to-3 part can be dropped.
    d3 = 3**v3(denom)
    outputs = [eval_poly(coefficients, r) for r in range(offset, offset + 3**k)]
    integral_units = [z // d3 for z in outputs if z % d3 == 0]
    score = best_binary(integral_units)
    degree = len(coefficients) - 1
    require(score + (degree - 1) <= degree * 2**k, "pullback bound")
    return score


def exhaustive_polynomials():
    cases = 0
    positive_gain = 0
    for degree in range(1, 5):
        for nonconstant in product(range(-2, 3), repeat=degree):
            if nonconstant[-1] == 0:
                continue
            co = (0, *nonconstant)
            for k in (2, 3, 4):
                score = certify_integer_scaled_input(co, 1, 0, k)
                positive_gain += score > 2**k
                cases += 1
    rng = random.Random(177150)
    denominators = [1, 2, 3, 5, 9, 15, 27, 54, 81, 243]
    for _ in range(520):
        degree = rng.randint(1, 9)
        co = tuple(rng.randint(-52, 52) for _ in range(degree)) + (rng.choice([1, 9, 27, -3, -8]),)
        co = tuple((3**rng.randrange(4))*c for c in co)
        score = certify_integer_scaled_input(co, rng.choice(denominators), rng.randint(-500, 70), 5)
        positive_gain += score > 2**5
        cases += 1
    return cases, positive_gain


def ternary_digits_from_01(x, depth):
    for _ in range(depth):
        x, digit = divmod(x, 3)
        if digit == 2:
            return False
    return True


def frobenius_control():
    # Full inverse target condition restricted to six free trits. To make the set
    # hereditary at all later depths, keep only one integer representative
    # per output prefix before testing first-trit occupancy.
    good = {}
    for x in range(3**7):
        y = x**3 - x
        if ternary_digits_from_01(y // 3, 6):
            good.setdefault(y % (3**7), (x, y))
    occupied = {x % 3 for x, _ in good.values()}
    # Select one actual lift from every input first-trit, retaining the
    # literal target S=three times the finite 0/1 digit Cantor set.
    good_finite = {x for x in range(-15, 16) if (x**3 - x) in
                   {3 * sum(a * 3**j for j, a in enumerate(ds)) for ds in product((0, 1), repeat=6)}}
    require({x % 3 for x in good_finite} == {0, 1, 2}, "critical root ternary control")
    return {"sample_signed_inputs": sorted(good_finite),
            "one_representative_per_residue_classes": len(good), "first_trits_dedup": sorted(occupied)}


def translate_polynomial(coefficients, e, scale):
    return [scale**i * sum(coefficients[j] * comb(j, i) * e**(j-i)
                           for j in range(i, len(coefficients))) for i in range(len(coefficients))]


def primitive_at_three(coefficients):
    divisor = 3**min(v3(z) for z in coefficients if z)
    return [z // divisor for z in coefficients]


def certified_subtree(coefficients, depth):
    derivative = [i*coefficients[i] for i in range(1, len(coefficients))]
    active = [(0, primitive_at_three(derivative), len(derivative) - 1)]
    by_level = []
    isometries = 0
    for k in range(depth):
        require(sum(m for _, _, m in active) <= len(derivative)-1, "total root credit")
        by_level.append(len(active))
        refined = []
        for start, q, m in active:
            debit = 0
            for e in range(3):
                shifted = translate_polynomial(q, e, 1)
                root_order = next(i for i, a in enumerate(shifted) if a % 3)
                child_start = start + e * 3**k
                if root_order:
                    child = primitive_at_three([z*3**i for i,z in enumerate(shifted)])
                    require(max(i for i,z in enumerate(child) if z % 3) <= root_order, "child degree")
                    refined.append((child_start, child, root_order))
                    debit += root_order
                    continue
                local = translate_polynomial(coefficients, child_start, 3**(k+1))
                require(local[1] and all(not z or v3(z) > v3(local[1]) for z in local[2:]), "linear term")
                ys = [eval_poly(local, x) for x in range(8)]
                for x in range(8):
                    for y in range(x):
                        require(v3(ys[x] - ys[y]) == v3(local[1]) + v3(x-y), "distance")
                isometries += 1
            require(debit <= m, "multiplicity budget")
        active = refined
    return by_level, isometries


def credit_controls():
    rng = random.Random(901)
    polys = [(0, -1, 0, 1), (1, 0, 0, 81), (0, 0, 1), (0, 0, 0, 0, 0, 0, 1)]
    for _ in range(320):
        d = rng.randrange(2, 9)
        polys.append(tuple(rng.choice(range(-6, 7)) for _ in range(d)) + (rng.choice([1, 3, 9, -6]),))
    total = 0
    for co in polys:
        _, visits = certified_subtree(co, 9)
        total += visits
    return len(polys), total


def delta(values, m, stride=1):
    out = list(values)
    for _ in range(m):
        out = [y-x for x,y in zip(out, out[stride:])]
    return out


def convolution_check():
    rng = random.Random(7302)
    cases = 0
    for count in range(8, 34):
        values = [rng.randrange(-50, 51) for _ in range(count)]
        for m in range(2, 6):
            for t in range(1, 6):
                if m*t >= count:
                    continue
                d = delta(values, m)
                totals = d
                for _ in range(m):
                    totals = [sum(totals[i:i+t]) for i in range(len(totals)-t+1)]
                require(totals == delta(values, m, t), "block difference identity")
                cases += 1
    return cases


def mechanical_cycle(p, h):
    require(gcd(p,h) == 1 and p < h < 2*p and 2**h > 3**p, "positive mechanical cycle")
    exponents = [((i+1)*h)//p - (i*h)//p for i in range(p)]
    total = carry = 0
    for a in exponents:
        carry = 3*carry + 2**total
        total += a
    D = 2**h - 3**p
    q = D // gcd(carry, D)
    x = Fraction(carry, D)
    x0 = x
    by_rank = [None]*p
    for i,a in enumerate(exponents):
        r = (i*h) % p
        by_rank[r] = x
        require(x.denominator == q and x.numerator % 2 == 1, "closed native fraction")
        x = (3*x+1) / 2**a
    require(x == x0 and len(set(by_rank)) == p, "closed primitive integer numerators")
    return q, by_rank


def run_length(values):
    longest = current = 0
    for z in values:
        if z >= 0:
            current += 1
        else:
            current = 0
        longest = max(longest, current)
    return longest


def rational_controls():
    ans = []
    for p,h in ((5,8), (41,65), (306,485)):
        q, ranks = mechanical_cycle(p,h)
        raw = [int(z*q) for z in ranks]
        h2 = delta(raw,2)
        vals = [run_length(h2), run_length([-z for z in h2])]
        max_run = max(vals)
        t = (max_run-1)//2+1
        if t>=54:
            require(2 * 27 * max(raw) * 2**2 >= t**2, "complete denominator bound m=2")
        ans.append({"p":p,"h":h,"q_bits":q.bit_length(),"second_difference_sign_runs":vals})
    return ans


def colors_check():
    cases = 0
    for m in range(1, 15):
        for a,b,c in product(range(m+1), repeat=3):
            if a+b+c > m:
                continue
            colors = [j % (m+1) for j in range(a+b+c+3)]
            groups = [colors[:a+1],colors[a+1:a+b+2],colors[a+b+2:]]
            require(all(len(set(g)) == len(g) for g in groups), "child repeated color")
            require(max(Counter(colors).values()) <= 2, "color has three children")
            cases += 1
    return cases


def main():
    cases, gains = exhaustive_polynomials()
    polys, visits = credit_controls()
    return {"optimal_target_polynomials_and_intervals":cases,"nonlinear_over_linear_max_count":gains,
            "certified_derivative_trees":polys,"verified_scaled_isometry_children":visits,
            "frobenius_cubic":frobenius_control(),"finite_color_allocations":colors_check(),
            "finite_difference_windows":convolution_check(),"rational_cycles":rational_controls()}


if __name__ == "__main__":
    print(json.dumps(main(), indent=2, sort_keys=True))
