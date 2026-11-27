"""Exact ordinary inverse-word certificates at the specified bounded canonical floor."""
import argparse
import json
from collections import Counter
from fractions import Fraction
from math import gcd


def source_residue(a, b, modulus, requested):
    """Solve a*z+b = requested modulo a power of three."""
    common = gcd(a, modulus)
    delta = requested - b
    if delta % common:
        return None
    modulus //= common
    if modulus == 1:
        return 0, 1
    return (delta // common * pow(a // common, -1, modulus)) % modulus, modulus


def below_linear(a, b, m, top, intercept, denominator):
    """Check strict inequality at and after the verified height cutoff."""
    slope = denominator * a - top * m
    return slope <= 0 and slope * (2 ** 71) + denominator * b < intercept * m


def verify_example(k, odd_class, n, word, kind, res, modulus, floor_rank):
    """Independently replay the exact odd maps at one CRT lift of this witness."""
    dyadic = 2 ** (k + 3)
    z0 = 1 + (2 ** k) * odd_class
    z0 += dyadic * (((res-z0) * pow(dyadic, -1, modulus)) % modulus)
    period = dyadic * modulus
    z = z0 + (1 + (2**71)//period) * period
    if z % 3 != 2 or (z-1) % (2**k) or (z-1)//2**k % 8 != odd_class:
        raise RuntimeError("incorrect original-source congruences")
    y = z
    for _ in range(n):
        if (3*y+1) % 8 != 4:
            raise RuntimeError("native forward exponent was not two")
        y = (3*y+1)//4
    for e in word:
        candidate, remainder = divmod((2**e)*y-1, 3)
        if remainder or candidate <= 0 or candidate % 2 == 0:
            raise RuntimeError("putative inverse word is not physical")
        y = candidate
    den, numer = 4**floor_rank, 3**floor_rank
    least_scaled = den + numer*(z-1)
    if kind == "canonical":
        ok = y % 48 == 17 and y < z
    elif kind == "absolute":
        ok = den*y < least_scaled
    else:
        ok = y%3 == 0 and den*y < 2*least_scaled+den
    if not ok:
        raise RuntimeError("floor witness did not contradict its claimed cut")


def run(k, depth, cap, trits, floor_rank):
    precision = 3 ** trits
    floor_den, floor_num = 4 ** floor_rank, 3 ** floor_rank
    odd_classes = (1, 3, 5, 7)
    # Only z=2 mod 3 is relevant. Each flag is a full class at precision trits.
    covered = [bytearray(precision // 3) for _ in odd_classes]
    stats = Counter()
    examples = []
    for n in range((k - 1) // 2 + 1):
        q16 = [(1 + 2 ** (k - 2*n) * 3 ** n * u) % 16 for u in odd_classes]
        forward_den = 4 ** n
        forward_num = 3 ** n
        frontier = [(0, 0, ())]
        for d in range(1, depth + 1):
            after = []
            term = 3 ** (d-1)
            ternary = 3 * term
            m = forward_den * ternary
            for old_e, old_c, word in frontier:
                e = 1
                while (1 << (old_e+e)) * forward_num <= cap * m:
                    total = old_e + e
                    binary = 1 << total
                    c = (old_c << e) + term
                    a = binary * forward_num
                    b = binary * (forward_den - forward_num) - forward_den * c
                    if a * (2 ** 71) + b <= 0:
                        raise RuntimeError("positivity guard needs a larger initial cutoff")
                    new_word = word + (e,)
                    e += 1
                    legal = source_residue(a, b, ternary, 0)
                    if legal is None or (legal[1] >= 3 and legal[0] % 3 != 2):
                        continue
                    if d < depth:
                        after.append((total, c, new_word))
                    stats["legal_nodes"] += 1
                    candidates = []
                    if below_linear(a, b, m, floor_num, floor_den-floor_num, floor_den):
                        candidates.append(("absolute", legal, range(4)))
                    if below_linear(a, b, m, 2*floor_num, 3*floor_den-2*floor_num, floor_den):
                        candidates.append(("triple", source_residue(a, b, 3*ternary, 0), range(4)))
                    if below_linear(a, b, m, 1, 0, 1):
                        mask = [i for i, x in enumerate(q16)
                                if ((binary*x-c)*pow(ternary, -1, 16)) % 16 == 1]
                        if mask:
                            candidates.append(("canonical", source_residue(a, b, 3*ternary, 2*m), mask))
                    for kind, congruence, mask in candidates:
                        if congruence is None:
                            continue
                        res, mod = congruence
                        if mod == 1:
                            res, mod = 2, 3
                        if mod > precision or res % 3 != 2:
                            continue
                        start, step = (res - 2)//3, mod//3
                        for i in mask:
                            flags = covered[i]
                            segment = flags[start::step]
                            if not segment or all(segment):
                                continue
                            verify_example(k, odd_classes[i], n, new_word, kind, res, mod, floor_rank)
                            new_count = len(segment) - sum(segment)
                            flags[start::step] = b'\1' * len(segment)
                            stats[kind] += new_count
                            if len(examples) < 12:
                                examples.append(dict(u_mod_8=odd_classes[i], n=n,
                                                     word=new_word, kind=kind,
                                                     z_modulus=mod, z_residue=res))
            frontier = after
    counts = [sum(flags) for flags in covered]
    return {"k": k, "minimum_v3": floor_rank, "classes_per_u": precision//3, "excluded_by_u": counts,
            "first_unexcluded_z_residues": [[3*i+2 for i,a in enumerate(flags) if not a][:4]
                                            for flags in covered],
            "stats": dict(stats), "sample_witnesses": examples}


def residue_three(value):
    return value.numerator * pow(value.denominator, -1, 3) % 3


def tilted_below(slope, virtual_value, threshold, at_two):
    return slope < threshold or (slope == threshold and virtual_value < at_two)


def virtual_control(k, floor_rank):
    """Exhaust all inverse words at the exceptional ternary datum z=2.

    Once four spare binary factors clear the forward denominator, only three
    small odd virtual integers could give a floor certificate. Each has an
    explicit forward orbit in {1,3,5}.
    """
    rho = Fraction(3, 4) ** floor_rank
    stats = Counter()
    for n in range((k-1)//2+1):
        scale = Fraction(3, 4)**n
        q16 = tuple((1+2**(k-2*n) * 3**n*u) % 16 for u in (1, 3, 5, 7))
        cutoff = 2*n+4

        def test(q, m, residues):
            if q <= 0:
                raise RuntimeError("the virtual control left the positive half-line")
            if tilted_below(m, q, rho, 1+rho):
                raise RuntimeError(f"virtual absolute-floor certificate at {n}, {q}, {m}")
            if residue_three(q) == 0 and tilted_below(m, q, 2*rho, 3+2*rho):
                raise RuntimeError(f"virtual triple-floor certificate at {n}, {q}, {m}")
            if (1 in residues and residue_three(q) == 2
                    and tilted_below(m, q, 1, 2)):
                raise RuntimeError(f"virtual canonical-floor certificate at {n}, {q}, {m}")

        def check_cleared(q, m):
            if q.denominator != 1 or q <= 0 or int(q) % 2 == 0:
                raise RuntimeError("binary clearing did not produce a positive odd integer")
            for source, multiplier in {1: [(1, 1), (5, Fraction(16, 3)),
                                             (3, Fraction(32, 9))],
                                       3: [(3, 1)],
                                       5: [(5, 1), (3, Fraction(2, 3))]}.get(int(q), []):
                test(Fraction(source), m*multiplier, [source % 16])
                stats["small_tail_tests"] += 1

        def explore(q, m, residues, clock):
            sign = residue_three(q)
            if sign == 0:
                return
            first = 1 if sign == 2 else 2
            e = first
            while True:
                factor = 2**e
                child = (factor*q-1)/3
                child_scale = factor*m/3
                child16 = tuple(((factor*x-1)*11) % 16 for x in residues)
                if clock+e >= cutoff:
                    check_cleared(child, child_scale)
                    stats["cleared_prefixes"] += 1
                    if child > 5:
                        break
                else:
                    test(child, child_scale, child16)
                    stats["short_prefixes"] += 1
                    explore(child, child_scale, child16, clock+e)
                e += 2

        explore(1+scale, scale, q16, 0)
    return dict(k=k, minimum_v3=floor_rank, **stats)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--depth", type=int, default=8)
    parser.add_argument("--trits", type=int, default=9)
    parser.add_argument("--cap", type=int, default=4)
    parser.add_argument("--k", type=int, nargs="+", default=[5, 7, 9, 11])
    parser.add_argument("--floor-rank", type=int, nargs="+", default=[2, 3, 4, 5])
    args = parser.parse_args()
    print(json.dumps({"depth": args.depth, "trits": args.trits, "ceiling_ratio": args.cap,
                      "virtual_controls": [virtual_control(k, r) for r in args.floor_rank
                                           for k in args.k if k <= 2*r+1],
                      "results": [run(k, args.depth, args.cap, args.trits, r) for r in args.floor_rank
                                  for k in args.k if k <= 2*r+1]},
                     indent=2))


if __name__ == "__main__":
    main()
