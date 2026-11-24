"""Exact finite certificate for the paired inverse fifth-power lower bound."""

from collections import Counter
import json


CLOCK_LIMIT = 27
GRADE_LIMIT = 8
PADDING_LIMIT = 400
MODULUS = 81
SCALE = 2**20
UNIT_RESIDUES = [r for r in range(MODULUS) if r % 3]
POTENTIAL = dict(zip(UNIT_RESIDUES, [
    289, 332, 381, 100, 846, 300, 115, 558, 279, 391, 332, 343, 445, 132,
    641, 423, 337, 321, 449, 272, 592, 184, 394, 359, 194, 511, 152, 252,
    406, 736, 486, 243, 320, 387, 368, 294, 237, 516, 313, 169, 708, 353,
    211, 278, 256, 206, 413, 616, 242, 222, 587, 211, 200, 174,
], strict=True))


def shortcut(x):
    return (3*x+1)//2 if x % 2 else x//2


def records():
    """First equal-grade ratio-five return on each surviving binary cylinder."""
    stack = [(1, 1, 2, 8, 1, 1)]
    while stack:
        h, r, a, b, p, k = stack.pop()
        if p == k and b == 5*a:
            yield h, r, p, (2**h)*a - (3**p)*r
            continue
        if h == CLOCK_LIMIT:
            continue
        for bit in (0, 1):
            y = a + (3**p)*bit
            z = b + 5*(3**k)*bit
            pp, kk = p+y%2, k+z%2
            if max(pp, kk) <= GRADE_LIMIT:
                stack.append((h+1, r+bit*2**h, shortcut(y), shortcut(z), pp, kk))


def replay_record(h, r, p, carry):
    for lift in (0, 1, 2):
        x = r+lift*2**h
        y, z, grade_y, grade_z = x, 5*x, 0, 0
        for t in range(1, h+1):
            grade_y += y % 2
            grade_z += z % 2
            y, z = shortcut(y), shortcut(z)
            if (y*5 == z and grade_y == grade_z) != (t == h):
                raise ValueError("incorrect first return")
        if grade_y != p or 2**h*y-3**p*x != carry:
            raise ValueError("incorrect affine carry")


def weight(n, e):
    """floor(SCALE * (n / 2**e)**(1/5)), using only integers."""
    target = SCALE**5*n >> e
    lo, hi = 0, SCALE+1
    if hi**5 <= target:
        raise ValueError("invalid root bracket")
    while hi-lo > 1:
        mid = (lo+hi)//2
        if mid**5 <= target:
            lo = mid
        else:
            hi = mid
    return lo


def certificate():
    bank = list(records())
    for record in bank:
        replay_record(*record)
    totals = {}
    for p in range(1, GRADE_LIMIT+1):
        n = 3**p
        modulus = MODULUS*n
        aggregate = [0]*modulus
        totals[p] = aggregate
        # For a child congruent to v modulo 81, the parent has exactly
        # one residue (C+n*v)*2**(-e) modulo 81*n.
        for e in range(n.bit_length()+1, PADDING_LIMIT+1):
            w = weight(n, e)
            if not w:
                break
            inv = pow(2, -e, modulus)
            favors = [(n*v*inv % modulus, w*POTENTIAL[v]) for v in UNIT_RESIDUES]
            for h, _, grade, carry in bank:
                if grade != p or h > e:
                    continue
                base = carry*inv % modulus
                for delta, contribution in favors:
                    aggregate[(base+delta) % modulus] += contribution
    min_margin = None
    min_residue = None
    nclasses = 0
    for q in range(MODULUS*3**GRADE_LIMIT):
        if q % 3 == 0:
            continue
        nclasses += 1
        score = sum(table[q % len(table)] for table in totals.values())
        margin = score-SCALE*POTENTIAL[q % MODULUS]
        if min_margin is None or margin < min_margin:
            min_margin, min_residue = margin, q
    if min_margin <= 0:
        raise ValueError("uniform positive margin failed")
    return {
        "branch_records": len(bank),
        "by_grade": dict(sorted(Counter(r[2] for r in bank).items())),
        "maximum_carry": max(r[3] for r in bank),
        "literal_first_return_replays": 3*len(bank),
        "parent_unit_classes": nclasses,
        "scale": SCALE,
        "minimum_integer_margin": min_margin,
        "minimum_margin_residue": min_residue,
    }


if __name__ == "__main__":
    print(json.dumps(certificate(), indent=2))
