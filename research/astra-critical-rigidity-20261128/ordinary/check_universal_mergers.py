"""Exact native-word cover and independent replay of physical rational merger lifts."""

from itertools import combinations
from math import gcd
import json


LENGTH, GRADE, MODULUS, LIMIT = 14, 9, 19683, 38740
BASE = ("", "D", "UDOODE", "UDOODEO", "UDOOD", "UUUDOOEODDDE",
        "UDOODO", "UDOODOOUD", "UUUDOOODDDE", "UDOODOO",
        "UUUDOOEODDD", "UUDUUODUDODOODEODE")
PARITIES = {"U": (0, 1), "D": (1, 0), "E": (0, 0), "O": (1, 1)}


def require(value, message):
    if not value:
        raise ValueError(message)


def certificate():
    rows = []
    for pos in combinations(range(LENGTH), GRADE):
        offset = sum((1 << t) * 3**(GRADE - i - 1) for i, t in enumerate(pos))
        mask = sum(1 << t for t in pos)
        rows.append((offset, mask))
    witnesses = [None] * MODULUS
    for c, w in rows:
        for b, v in rows:
            delta = c - b
            residue = delta % MODULUS
            old = witnesses[residue]
            if old is None or abs(delta) < abs(old[0]):
                witnesses[residue] = (delta, w, v)
    require(all(x is not None for x in witnesses), "an affine residue has no representative")
    require(max(abs(x[0]) for x in witnesses) == LIMIT, "incorrect smallest cutoff")

    # Generate native offsets a second way, by composing odd/even branches.
    offsets = []
    for mask in range(1 << LENGTH):
        if mask.bit_count() != GRADE:
            continue
        c = 0
        for t in range(LENGTH):
            if mask & (1 << t):
                c = 3*c + (1 << t)
        offsets.append(c)
    require(len(offsets) == len(set(offsets)) == 2002, "unexpected offset multiplicity")
    require(sorted(offsets) == sorted(c for c, w in rows), "offset constructions disagree")
    bits = sum(1 << c for c in offsets)
    check_bounds = {}
    for bound in (LIMIT-1, LIMIT):
        differences = 0
        interval = (1 << (2*bound+1)) - 1
        for reference in offsets:
            shift = reference-bound
            local = bits >> shift if shift >= 0 else bits << -shift
            differences |= local & interval
        # Bit i here means that signed difference i-bound occurs.
        residue_mask = (1 << MODULUS) - 1
        folded = 0
        while differences:
            folded |= differences & residue_mask
            differences >>= MODULUS
        missing = sorted((r-bound) % MODULUS for r in range(MODULUS)
                         if not (folded >> r) & 1)
        require(missing == [r for r, record in enumerate(witnesses) if abs(record[0]) > bound],
                "interval-bitset and word-pair residue covers disagree")
        check_bounds[str(bound)] = missing
    return witnesses, {"words": len(rows), "residues": MODULUS, "missing": check_bounds}


def transition(state, letter):
    j, a = state
    lo, hi = PARITIES[letter]
    require((lo-a) % 2 == hi, "incompatible native parity pair")
    if letter == "U":
        return j+1, (3*a-1)//2
    if letter == "D":
        require(j >= 1, "negative level in base certificate")
        return j-1, (a+3**(j-1))//2
    if letter == "E":
        return j, a//2
    return j, (3*a+3**j-1)//2


def native(n, d):
    return (3*n+d)//2 if n & 1 else n//2


def sign_seed():
    a, b = 7, 21
    path = []
    for t in range(11):
        path.append((a % 2, b % 2))
        a, b = native(a, 1), native(b, 1)
    require((a, b) == (1, 2), "incorrect negative translation seed states")
    require(tuple(map(sum, zip(*path))) == (5, 4), "incorrect negative seed grades")
    return path


def translation(target, cover):
    require(target != 0, "constructive recursion expects nonzero translation")
    positive = target > 0
    a = abs(target)
    blocks = []
    while a >= 12:
        d, w, v = cover[((1 << LENGTH)*a) % MODULUS]
        num = (1 << LENGTH)*a-d
        require(num % MODULUS == 0 and 0 < num//MODULUS < a, "inverse block did not contract")
        blocks.append([((w >> t) & 1, (v >> t) & 1) for t in range(LENGTH)])
        a = num//MODULUS
    steps = [PARITIES[ch] for ch in BASE[a]]
    for block in reversed(blocks):
        steps.extend(block)
    if positive:
        return [(1, 1)] + steps
    # At s=7 the reversed arms have translation +1, and U recovers (1,1).
    return sign_seed() + [(h, l) for l, h in [PARITIES["U"]] + steps]


def entry_words(j, a, cover):
    reverse = []
    while j:
        e = next(e for e in range(1, 7) if (2**e*a) % 9 == 2)
        b = (2**e*a+1)//3
        require(b % 2 and b % 3 and b*a > 0, "wrong modular predecessor")
        reverse.append([PARITIES["U"]] + [PARITIES["E"]]*(e-1))
        j, a = j-1, b
    path = translation(a, cover)
    for block in reversed(reverse):
        path.extend(block)
    return path


def replay(znum, q, j, cover, trailing):
    require(q > 0 and q % 2 and gcd(znum, q) == gcd(znum*q, 3) == 1, "inadmissible center")
    require(pow(3, j, q) == 1 % q, "invalid prime-to-three slope order")
    target_a = ((3**j-1)*znum)//q
    path = entry_words(j, target_a, cover)
    t = len(path)
    cg, ch = 0, 0
    g, h = 0, 0
    for i, (l, u) in enumerate(path):
        if l:
            cg, g = 3*cg + (1 << i), g+1
        if u:
            ch, h = 3*ch + (1 << i), h+1
    require(h+1-g == j, "physical slope gap disagrees")
    require(3**j*cg-ch == (1 << t)*target_a, "physical translations disagree")
    numerator = (1 << t)*znum - q*cg
    denominator = q*3**g
    modulus = 1 << (t+trailing)
    source = numerator*pow(denominator, -1, modulus) % modulus
    if source*denominator == numerator:
        source += modulus
    require(source > 0 and source & 1 and source*denominator != numerator, "wrong ordinary lift")
    ra, rb = numerator, 3*numerator
    a, b = source, 3*source
    min_merge = None
    later_grade = 0
    for i in range(t+trailing+1):
        require(a != b and a > 0 and b > 0, "physical lift merged or lost positivity")
        if i < t+trailing:
            require((a % 2, b % 2) == (ra % 2, rb % 2), "physical and rational parities disagree")
        if ra == rb and min_merge is None:
            min_merge = i
        if i < t:
            require((ra % 2, rb % 2) == path[i], "wrong itinerary on constructed source")
        if i == t:
            require(ra == rb == znum*(denominator//q), "rational state failed to equal target")
        if t <= i < t+trailing:
            require(ra == rb, "rational future diverged")
            later_grade += ra % 2 + rb % 2
        if i < t+trailing:
            ra, rb = native(ra, denominator), native(rb, denominator)
            a, b = native(a, 1), native(b, 1)
    record = {"center": [znum, q], "level": j, "entry_clock": t, "entry_grades": [g, h],
              "first_rational_merger": min_merge, "ordinary_source_bits": source.bit_length(),
              "unmerged_ordinary_clock": t+trailing, "combined_future_grade": later_grade}
    return record


def main():
    cover, report = certificate()
    for a, path in enumerate(BASE[1:], 1):
        state = (1, 1)
        for letter in path:
            state = transition(state, letter)
        require(state == (0, a), "base certificate failed")
    report["base_paths"] = list(BASE[1:])
    rows = []
    for length in (3, 4, 5, 6, 7, 8, 9, 10):
        q = (1 << length)-3
        j = next(n for n in range(1,q+1) if pow(3,n,q) == 1)
        row = replay(1, q, j, cover, 20*length)
        require(row["combined_future_grade"] == 40, "one-odd cycle has incorrect grade")
        rows.append(row)
    report["one_odd_cycles"] = rows
    report["signed_centers"] = [replay(u, q, j, cover, 127)
                                for u, q, j in ((-1, 1, 1), (-2, 5, 4), (23, 7, 6), (5, 1, 3))]
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
