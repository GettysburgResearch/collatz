#!/usr/bin/env python3
"""Independent reconstruction of C3S1--C3S3; no author imports."""
import json


def need(ok, message):
    if not ok:
        raise ValueError(message)


def v(n, p):
    need(n > 0, "positive valuation input required")
    out = 0
    while n % p == 0:
        n //= p
        out += 1
    return out


def T(n):
    need(n > 0, "positive ordinary input required")
    return (3*n+1)//2 if n % 2 else n//2


def walk(n, clocks):
    path = [n]
    for _ in range(clocks):
        n = T(n)
        path.append(n)
    return path


def ternary_log2(target, m):
    e = 0 if target % 3 == 1 else 1
    need(pow(2, e, 3) == target % 3, "nonunit ternary target")
    period = 2
    for level in range(2, m+1):
        modulus = 3**level
        hits = [e+d*period for d in range(3)
                if pow(2, e+d*period, modulus) == target % modulus]
        need(len(hits) == 1, "nonunique exponent lift")
        e = hits[0]
        period *= 3
    return e, period


def S(a, e):
    need(e >= 1 and e % 2, "odd exponent required")
    return 2**(a+e+9)-687*3**a-81*176106*3**(a+(e-1)//2)


def comparison():
    need(S(4, 81) == 5759691404070374176388879671, "large-rank base")
    need(S(3, 81) == 5221070572784472125193957821, "small-rank base")
    need(2**5 > 3**3 and 4 > 3, "a-increment comparison induction")
    for a in range(1, 3):
        need(S(a+1, 81)*2**a < S(a, 81)*2**(a+1), "normalized small-rank order")
    checks = 0
    for a in range(4, 10):
        e0 = 3**a
        need(S(a, e0) > 0, "a-induction example")
        for d in range(5):
            e = e0+2*d
            P0, E = 2**(a+e+9), 687*3**a
            need(S(a, e+2) == 3*S(a, e)+P0+2*E, "e-increment identity")
            checks += 1
        need(2**(2*e0+1) > 3**(e0+1), "a-induction multiplier")
        checks += 1
    return checks


def complete_small_classes():
    expected = [(1, 21, 162), (2, 315, 486), (3, 837, 1458)]
    for a, e0, period in expected:
        modulus = 3**(a+4)
        target = (42*3**a*pow(2**a, -1, modulus)-1) % modulus
        hits = [e for e in range(1, period+1) if pow(2, e, modulus) == target]
        need(hits == [e0], "incomplete or incorrect small exponent progression")
        need(ternary_log2(target, a+4) == (e0, period), "discrete-log cross-check")
    return expected


def literal_cases():
    pairs = [(1, 21), (1, 183), (2, 315), (2, 801), (3, 837)]
    a = 4
    modulus = 3**(a+4)
    target = (42*3**a*pow(2**a, -1, modulus)-1) % modulus
    e, _ = ternary_log2(target, a+4)
    pairs.append((a, e))
    total_clocks = 0
    for a, e in pairs:
        numerator = 2**a*(2**e+1)
        need(numerator % 3**a == 0, "source integrality")
        z = numerator//3**a-1
        need(z > 1 and z % 81 == 41 and v(e, 3) == a, "source class and terminal valuation")
        h = (4*z-2)//81
        need(h > 0 and h % 4 == 2, "eligible upper index")
        X, Y = 128*h+1, 64*h+1
        P = 3**((e-1)//2)
        clocks = a+e+9
        upper = walk(X, clocks)
        lower = walk(Y, clocks)
        need(upper[-1] == 1 and 1 not in upper[:-1], "exact upper first hit")
        need(sum(n % 2 for n in upper[:-1]) == a+4, "exact upper odd rank")
        need(lower[7] == 2*z+1 and lower[7+a] == 2**(e+1)+1, "lower checkpoints")
        need(all(n % 2 for n in lower[7:7+a]), "lower forced odd run")
        need(lower[-1] == T(P), "same-clock residual merger")
        exact = 2**(a+e+9)+2**(a+9)-687*3**a-81*176106*3**(a+(e-1)//2)
        need(81*3**a*(X-176106*P) == exact, "least-source comparison identity")
        if (a, e) != (1, 21):
            need(176106*P < X, "least-source interval guard")
        total_clocks += clocks
    exception = walk(3**10, 89)
    need(exception[-1] == 1 and 1 not in exception[:-1]
         and sum(n % 2 for n in exception[:-1]) == 46
         and max(exception) == 1135052, "finite exception certificate")
    return len(pairs), total_clocks


def compressed_cylinders():
    expected = [116073, 380781, 2431215, 63433935, 633234915]
    rows = []
    for H in range(11):
        L, a = H+6, H+4
        m = 2*L-1
        modulus = 3**m
        target = (-1+3**(a+1)*pow(2**(a+1), -1, modulus)) % modulus
        e, period = ternary_log2(target, m)
        if H < len(expected):
            need(e == expected[H], "compressed example changed")
        need(e % 2 and v(e, 3) == a and e >= 3**a, "compressed terminal exponent")
        residue_num = (pow(2, a, modulus)*(pow(2, e, modulus)+1)) % modulus
        need(residue_num % 3**a == 0, "compressed quotient integrality")
        z3 = (residue_num//3**a-1) % 3**(L+1)
        need((2*z3-1) % 3**(L+1) == 0, "compressed ternary z class")
        z2 = (pow(2, a, 2**L)*(pow(2, e, 2**L)+1)*pow(3**a, -1, 2**L)-1) % 2**L
        need((z2+1) % 2**a == 0, "compressed binary z class")
        N2 = (4*z2+1)*pow(3, -1, 2**L) % 2**L
        need(N2 == 2**L-1, "compressed binary N class")
        need((4*z3-2) % 3**(L+1) == 0, "compressed ternary N class")
        rows.append([H, a, e, period])
    return rows


def general_blocks():
    cases = solved = 0
    for z in range(41, 20000, 162):
        a = v(z+1, 2)
        q = (z+1)//2**a
        e = v(3**a*q-1, 2)
        w = (3**a*q-1)//2**e
        target = 2*z+1
        middle = walk(target, a)[-1]
        need(middle == 2**(e+1)*w+1, "general block removal")
        if e % 2:
            R = 3**((e-1)//2)*w
            need(walk(target, a+e+2)[-1] == T(R), "odd block residual")
            solved += int(e == 1)
        else:
            R = 2*3**(e//2)*w+1
            need(walk(target, a+e)[-1] == R, "even block residual")
        cases += 1
    return cases, solved


def rank_six_family():
    need(pow(2, 486, 729) == 1 and pow(2, 243, 729) != 1
         and pow(2, 162, 729) != 1, "complete exponent order modulo 729")
    residues = [A for A in range(486) if pow(2, A+3, 729) == 380]
    need(residues == [340], "rank-six exponent progression")
    need(729*3**5 > 4096*2**5 and 3 > 2,
         "same-clock strict-height comparison induction")
    clocks = 0
    for j in range(4):
        A = 340+486*j
        e = A+1
        need((2**(A+3)-11) % 9 == 0, "rank-six z integrality")
        z = (2**(A+3)-11)//9
        need(z % 81 == 41, "rank-six c=3 domain")
        w = (2**A-1)//3
        need(3*z+1 == 8*w and v(3*z+1, 2) == 3,
             "first known odd gap is not three")
        need(3*w+1 == 2**A, "second known odd gap")
        X = (512*z-175)//81
        Y = (X+1)//2
        need(729*X == 2048*2**e-7207, "rank-six upper parameterization")
        need(X % 128 == 1 and ((X-1)//128) % 4 == 2,
             "rank-six upper eligibility")
        upper = walk(X, A+12)
        need(upper[-1] == 1 and 1 not in upper[:-1]
             and sum(n % 2 for n in upper[:-1]) == 6,
             "rank-six exact first-hit certificate")
        lower = walk(Y, A+12)
        need(lower[7] == 2*z+1 and lower[10] == 2**e-1,
             "rank-six lower Mersenne checkpoint")
        need(lower[-1] == (3**e-1)//2 and lower[-1] > X,
             "rank-six same-clock lower height")
        need(all(n > 1 for n in lower), "early lower rank-six arrival")
        clocks += A+12
    return len(residues), 4, clocks


def main():
    recurrences = comparison()
    small = complete_small_classes()
    literal, clocks = literal_cases()
    cylinders = compressed_cylinders()
    blocks, solved = general_blocks()
    residues, rank_six_cases, rank_six_clocks = rank_six_family()
    print(json.dumps({
        "scope": "independent exact controls for conditional C3S1--C3S2 and the remaining C3S3 family; not all c=3 convergence",
        "author_implementation_imported": False,
        "small_exponent_classes": small,
        "comparison_recurrence_controls": recurrences,
        "literal_single_run_cases": literal,
        "literal_upper_clocks": clocks,
        "compressed_cylinder_examples": cylinders,
        "general_block_controls": blocks,
        "directly_solved_first_blocks": solved,
        "rank_six_exponent_classes": residues,
        "rank_six_literal_cases": rank_six_cases,
        "rank_six_upper_clocks": rank_six_clocks,
    }, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
