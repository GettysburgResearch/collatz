"""Enumerate exact adjacent carry solutions and audit the crossing ledgers."""

from collections import Counter, defaultdict
from fractions import Fraction


def check(condition, message):
    if not condition:
        raise ArithmeticError(message)


def audit(U, V, L, cu, cv, stats):
    p = len(U)
    D = 2**L-3**p
    check(cu-cv == D, "adjacent static equation")
    x, y = Fraction(cu,D), Fraction(cv,D)
    initial = x, y
    us, vs = set(U), set(V)
    M = sum(u != v for u,v in zip(U,V))
    H = len(us ^ vs)
    I = sum((u < V[i]) + (v < U[i]) for i in range(p) for u,v in zip(U[i:],V[i:]))
    levels, marks, offsets, slopes, sources = [], [], [], [], []
    g = h = inward_mass = double_mass = outward_mass = inward_count = 0
    exact_product = Fraction(1)
    for t in range(L):
        a, b = int(t in us), int(t in vs)
        check(x.numerator % 2 == a and y.numerator % 2 == b, "period phases")
        j = abs(g-h)
        m = min(g,h)
        A = 3**(g-m)*y-3**(h-m)*x
        check(A.denominator == 1 and A, "integral nonzero determinant")
        A = int(A)
        m2 = min(g+a,h+b)
        c = a+b-(m2-m)
        B = b*3**(g+a-m2)-a*3**(h+b-m2)
        oldj = j
        g += a
        h += b
        x = (3**a*x+a)/2
        y = (3**b*y+b)/2
        next_A = 3**(g-m2)*y-3**(h-m2)*x
        check(2*next_A == 3**c*A+B, "normalized recurrence")
        exact_product *= abs(Fraction(3**c*A+B, 3**c*A))
        levels.append(oldj)
        slopes.append(c)
        offsets.append(B)
        sources.append(A)
        if B:
            marks.append(t)
            if a == b:
                double_mass += oldj
                check(abs(B) == 3**oldj-1 and c == 1, "double odd")
            elif abs(g-h) < oldj:
                inward_count += 1
                inward_mass += oldj
                check(abs(B) == 3**(oldj-1) and c == 0, "inward")
            else:
                outward_mass += oldj
                check(abs(B) == 1 and c == 1, "outward")
    check((x,y) == initial and g == h == sum(slopes) == p, "complete closed pair")
    check(exact_product == Fraction(2**L,3**p), "real product")
    check(I == inward_mass+double_mass and outward_mass == inward_mass-inward_count,
          "strict crossings and reflected level")
    check(M <= len(marks) <= 2*M and I <= min(M*(M+1)//2,M*max(levels)),
          "ordinal mismatch bounds")
    check(9**(H//2)*2**L <= 8**(H//2)*3**(p+I), "explicit real bound")
    for size in (1,2,3,4):
        for start in range(0,len(marks),size):
            group = marks[start:start+size]
            maximum = max(levels[t] for t in group)
            if len(group) < size:
                check(maximum <= size, "final incomplete packet")
            low = [t for t in group if abs(sources[t]) <= 3**(1+maximum)]
            if len(low) < 2:
                continue
            s,e = low[0],low[-1]
            partial = 3**sum(slopes[s:e])*sources[s]
            for v in range(s,e):
                remaining = sum(slopes[v+1:e])
                partial += 2**(v-s)*3**remaining*offsets[v]
                check(partial == 2**(v+1-s)*3**remaining*sources[v+1] and partial != 0,
                      "all strictly chronological cuts")
                stats["trimmed_chronological_cuts"] += 1
            stats["low_endpoint_packets"] += 1
    stats["adjacent_pairs"] += 1
    stats["negative_determinants"] += D < 0
    stats["positive_determinants"] += D > 0
    stats["rank_aligned_pairs_with_some_unequal_ranks"] += M < p
    stats["individual_ordered_crossings"] += I
    stats["largest_native_period_tested"] = max(stats["largest_native_period_tested"], L)


def words(length):
    # Construct each carry independently as a sum over its increasing calendar.
    for mask in range(1,1<<length):
        positions = tuple(i for i in range(length) if (mask >> i) & 1)
        carry = 0
        for i in positions:
            carry = 3*carry+(1<<i)
        yield positions,carry


def main():
    stats = Counter()
    for L in range(1,16):
        bygrade = defaultdict(dict)
        for w,c in words(L):
            bygrade[len(w)].setdefault(c,[]).append(w)
        for p, bycarry in bygrade.items():
            D = 2**L - 3**p
            for cu, upper in bycarry.items():
                cv = cu-D
                for U in upper:
                    for V in bycarry.get(cv,()):
                        audit(U,V,L,cu,cv,stats)
    for name in sorted(stats):
        if name != "negative_determinants":
            check(stats[name] > 0, name)
        print(f"{name}={stats[name]}")


if __name__ == "__main__":
    main()
