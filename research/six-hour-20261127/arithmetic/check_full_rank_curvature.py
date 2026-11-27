"""Signed second differences, all local rank cells, and the final backward seam."""
from fractions import Fraction
from itertools import product
from math import gcd
import json

from check_anchor_carries import require


P, SHIFT = 1_000_003, 584_964
LOW, HIGH = Fraction(584962, 10**6), Fraction(584963, 10**6)


def clock(rank):
    return 1+int(rank % P+SHIFT >= P)


def coefficients(rank):
    rank %= P
    result = []
    for value in (rank, rank+1, rank+2):
        wrap, index = divmod(value, P)
        grades = 3 if index <= P-SHIFT else 2
        result.append(tuple((4 >> k)*(1 << wrap) for k in range(grades)))
    return result


def curvature_residue(c, h):
    left, middle, right = c
    return (h-left+2*middle-right) % gcd(2*left, 4*middle, 2*right) == 0


def advance(state, rank):
    c, h = state
    divisor = 1 << clock(rank)
    next_h, remainder = divmod(3*h+c[0]-2*c[1]+c[2], divisor)
    if remainder:
        return []
    next_choices = [tuple(d for d in pool if divisor*d in (2*x, 4*x))
                    for pool, x in zip(coefficients(rank+SHIFT), c)]
    return [(d, next_h) for d in product(*next_choices) if curvature_residue(d, next_h)]


def predecessors(state, rank):
    # 'rank' is the earlier rank.
    d, next_h = state
    divisor = 1 << clock(rank)
    earlier_choices = [tuple(x for x in pool if divisor*y in (2*x, 4*x))
                       for pool, y in zip(coefficients(rank), d)]
    result = set()
    for c in product(*earlier_choices):
        h, remainder = divmod(divisor*next_h-c[0]+2*c[1]-c[2], 3)
        if not remainder and curvature_residue(c, h) and (h or len(set(c)) > 1):
            result.add((c, h))
    return result


def calendar_check():
    # Any two distinct macroscopic cuts t*alpha, with the indices needed
    # by the local or 35-step tests, stay ordered after all mesh offsets.
    require(LOW < Fraction(SHIFT, P) < HIGH and Fraction(1, P) < Fraction(1, 10**6),
            "sample parameters")
    require(2**1584962 < 3**1000000 < 2**1584963, "limiting slope enclosure")
    for t in range(1, 41):
        a, b = t*LOW, t*HIGH
        floor = a.numerator//a.denominator
        require(floor+Fraction(1, 1000) < a <= b < floor+1-Fraction(1, 1000),
                "stable lifted rotation cuts")
    cuts = {(-j*SHIFT-i) % P for j in range(4) for i in range(3)}
    cuts = sorted(cuts)
    faces = []
    for start, stop in zip(cuts, cuts[1:]+[P]):
        faces.append(start)
        if start+1 < stop:
            faces.append(start+1)
    return faces


def local_exits(faces):
    negative = []
    positive_zeros = []
    for rank in faces:
        for c in product(*coefficients(rank)):
            # The largest possible absolute lowbit second difference is 14.
            # An exit to zero or across zero requires 3*abs(h) <= 14.
            for h in (-4, -3, -2, -1, 1, 2, 3, 4):
                if not curvature_residue(c, h):
                    continue
                for d, next_h in advance((c, h), rank):
                    if h < 0 <= next_h:
                        negative.append((rank, c, h, d, next_h))
                    if h > 0 and next_h == 0 and len(set(d)) > 1:
                        for f, after_h in advance((d, 0), rank+SHIFT):
                            if after_h > 0 or (after_h == 0 and len(set(f)) > 1):
                                positive_zeros.append((rank, c, d, f))
    expected = [(P-SHIFT-i, (4, 1, 4), -2, (4, 2, 8), 0) for i in (2, 1)]
    require(negative == expected and not positive_zeros, "all signed rank exits")
    return negative


def ordinary_lifts(faces):
    checked = 0
    witnessed = set()
    for rank in faces:
        divisor = 1 << clock(rank)
        choices = []
        for old, new in zip(coefficients(rank), coefficients(rank+SHIFT)):
            slot = []
            for c in old:
                for odd in range(1, 48, 2):
                    numerator = 3*odd+1
                    multiplier = numerator & -numerator
                    if odd % 3 and multiplier in (2, 4) and c*multiplier % divisor == 0:
                        d = c*multiplier//divisor
                        if d in new:
                            slot.append((c, c*odd, d, d*(numerator//multiplier)))
            choices.append(slot)
        for triple in product(*choices):
            c, labels, d, after = zip(*triple)
            h = labels[0]-2*labels[1]+labels[2]
            if not 0 < abs(h) <= 4:
                continue
            next_h = after[0]-2*after[1]+after[2]
            require(curvature_residue(c, h) and (d, next_h) in advance((c, h), rank),
                    "three literal ordinary source lifts")
            checked += 1
            if h < 0 <= next_h:
                witnessed.add(rank)
    require(checked > 100 and witnessed == {P-SHIFT-2, P-SHIFT-1},
            "both local negative exits have literal ordinary lifts")
    return checked


def check():
    faces = calendar_check()
    exits = local_exits(faces)
    # The second exit would put doubled lowbit 2 at rank zero, whose actual
    # doubled lowbit is 8. The first may be tested without any further cap.
    rank = exits[0][0]
    states = {(exits[0][1], exits[0][2])}
    counts, letters = [], []
    for _ in range(35):
        rank -= SHIFT
        letter = clock(rank)
        allowed = ((4, 2, 1) if letter == 1 else (4, 2))
        require(coefficients(rank) == [allowed]*3, "uniform earlier grade slots")
        letters.append(letter)
        states = set().union(*(predecessors(state, rank) for state in states))
        counts.append(len(states))
    require(all(counts[:-1]) and not states, "no backward seam survivor")
    require(18**72 < 2**23*17**68 and 3**12 > 2**19, "microscopic entropy threshold")
    return {"sample_period_shift": [P, SHIFT], "slope_bracket": [str(LOW), str(HIGH)],
            "local_integer_faces": faces, "negative_exits": exits,
            "nonnegative_sustained_positive_zero_entries": 0, "literal_ordinary_triples": ordinary_lifts(faces),
            "backward_letters": letters, "backward_counts": counts,
            "microscopic_mismatch_lower_limit_strictly_above": "1/18"}


if __name__ == "__main__":
    print(json.dumps(check(), indent=2))
