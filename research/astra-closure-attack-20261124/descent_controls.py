"""Exact checks for the two-clock shadow theorem and its finite-coverage wall."""
from fractions import Fraction
from itertools import combinations, product

DEN = 2**18
NUM = 251349
OFFSET = {'F': -75565, 6: -75565, 5: -141101, 4: -149293, 3: -158509,
          2: -168877, 1: -246077, 0: -332927}
GAPS = {'F': (2, 1), 6: (1, 2), 5: (2, 1), 4: (2, 1), 3: (2, 1),
        2: (1, 2), 1: (1, 2), 0: (2, 3)}
L = (2, 1)
P = (1, 4)


def check(truth, label):
    if not truth:
        raise ArithmeticError(label)


def physical_lift(word):
    """Smallest positive representative for a finite list of block gaps."""
    q, modulus = 1, 2
    for a in reversed([a for block in word for a in block]):
        modulus <<= a
        q = ((2**a * q - 1) * pow(3, -1, modulus)) % modulus
    return q, modulus


def edge(q, gap):
    n = 3*q + 1
    check(n > 0 and (n & -n) == 2**gap, "exact physical valuation")
    return n >> gap


def residues():
    powers = [Fraction(9, 8)**j / 4 for j in range(8)]
    sums = {sum(parts, Fraction()) for k in range(3) for parts in combinations(powers, k)
            if sum(parts, Fraction()) <= Fraction(14, 23)}
    check(len(sums) == 13, "complete finite list of error offsets")
    for c, s in product((5, 7, 11, 19), sums):
        d = ((115+c+9*s)/166).denominator
        check(d & (d-1), "putative dyadic universal slope")
    return 4*len(sums)


def finite_inputs():
    tested = states = outside = 0
    for prefix in product((L, P), repeat=14):
        marks = [i for i, word in enumerate(prefix) if word == P]
        if any(b-a <= 6 for a, b in zip(marks, marks[1:])):
            continue
        # The extra true edges allow us to recover dyadic integrality of each
        # reported boundary without guessing an infinite ordinary continuation.
        words = prefix + (L,)*13 + (P,) + (L,)*7
        q0, modulus = physical_lift(words)
        for start in (q0, q0+modulus):
            q = start
            outside += int((q+7) % 83 != 0)
            for i in range(len(prefix)):
                nearest = next((j-i for j in range(i, len(words)) if words[j] == P), 99)
                state = nearest if nearest <= 6 else 'F'
                y, rem = divmod(NUM*q + OFFSET[state], DEN)
                check(rem == 0 and 0 < y < q, "ordinary strictly smaller boundary")
                first, second = GAPS[state]
                y1 = edge(y, first)
                y2 = edge(y1, second)
                ordinary_mid = edge(q, words[i][0])
                ordinary_next = edge(ordinary_mid, words[i][1])
                if words[i] == L:
                    if GAPS[state] == L:
                        check(y1 < ordinary_mid, "synchronous smaller intermediate")
                    else:
                        u = q
                        for a, b in words[i:i+nearest+1]:
                            u = edge(edge(u, a), b)
                        check(u < ordinary_mid, "smaller actual source past paid block")
                nxt_dist = next((j-i-1 for j in range(i+1, len(words)) if words[j] == P), 99)
                nxt = nxt_dist if nxt_dist <= 6 else 'F'
                check(DEN*y2 == NUM*ordinary_next + OFFSET[nxt], "literal shadow transport")
                q = ordinary_next
                states += 1
            tested += 1
    return tested, states, outside


def table():
    for state, v in OFFSET.items():
        original = P if state == 0 else L
        next_states = (6, 'F') if state == 0 or state == 'F' else (state-1,)
        for ns in next_states:
            c, cp = 3 + 2**original[0], 3 + 2**GAPS[state][0]
            check((2**sum(original))*OFFSET[ns] == 9*v + DEN*cp - NUM*c, "table clock")
    check(Fraction(NUM, DEN)*83 == 84 - sum(Fraction(9,8)**k for k in (1, 2, 6)),
          "dyadic slope synthesis")
    check(Fraction(9,8)**6 < Fraction(21,10), "strict future bound")


def close_pair():
    # A cluster can be locally contracting above the actual source minimum.
    words = (L,)*30 + (P,P)
    q, _ = physical_lift(words)
    n = edge(q, 2)
    path = [q]
    for a, b in words:
        path.append(edge(path[-1], a))
        path.append(edge(path[-1], b))
    check(n == path[1] and all(x > n for x in path[2:]), "no earlier minimum recovery")
    return n, path[-1]


def triple_payments():
    count = 0
    for leading in range(65):
        words = (L,)*leading + (P,)*3
        least, modulus = physical_lift(words)
        for seed in (least, least+modulus):
            x, y = seed, (seed-7)//2
            check(0 < y < seed and 4*y < 3*seed+1, "strict half-source comparison")
            for a, b in words:
                x = edge(edge(x, a), b)
            for _ in range(3*leading+14):
                y = (3*y+1)//2 if y%2 else y//2
            check(y == x, "asynchronous triple-paid merger")
            count += 1
    return count


def main():
    table()
    candidates = residues()
    tests, states, outside = finite_inputs()
    n, end = close_pair()
    triples = triple_payments()
    print(f"ordinary finite paths={tests}; compared block boundaries={states}; "
          f"starting values outside 83 guard={outside}; rejected dyadic candidates={candidates}; "
          f"asynchronous triple-paid mergers={triples}")
    print(f"L^30 PP non-recovery control: starting intermediate={n}; final boundary={end}")


if __name__ == '__main__':
    main()
