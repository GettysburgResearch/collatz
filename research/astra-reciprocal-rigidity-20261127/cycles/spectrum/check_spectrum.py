"""Exact controls for the collective spectrum and mechanical-edit estimates."""
from collections import deque
from fractions import Fraction
from math import gcd


def require(test, message):
    if not test:
        raise ValueError(message)


def cyclic_word(mask, n):
    return tuple((mask >> i) & 1 for i in range(n))


def rotation_distance(bits, h):
    return sum(x != y for x, y in zip(bits, bits[h:]+bits[:h]))


def actual_cycle(bits):
    n = len(bits)
    u = sum(bits)
    D = 2**n-3**u
    if not u or D <= 0:
        return None
    Cw = 0
    for j, bit in enumerate(bits):
        if bit:
            Cw = 3*Cw + 2**j
    g = gcd(Cw, D)
    d = D//g
    first = Cw//g
    x = first
    states = []
    for bit in bits:
        require(x % 2 == bit, "physical parity")
        states.append(x)
        x = (3*x+d)//2 if bit else x//2
    require(x == first, "actual return")
    return d, states, Fraction(u*2**n, 3*D)


def diameter(n, steps):
    distances = {0: 0}
    pending = deque([0])
    while pending:
        x = pending.popleft()
        for step in steps:
            y = (x+step) % n
            if y not in distances:
                distances[y] = distances[x]+1
                pending.append(y)
    D = max(distances.values())
    require((D//3+1)*len(steps) <= len(distances), "disjoint geodesic balls")
    return D, set(distances)


def spectrum(bits, d, states):
    n = len(bits)
    dist = [rotation_distance(bits, h) for h in range(n)]
    checks = 0
    for k in set(dist[1:]):
        K = {h for h in range(n) if 0 < dist[h] <= k}
        require(K and K == {(-i) % n for i in K}, "symmetric shifts")
        diameter(n, K | {0, 1, n-1})
        D, H = diameter(n, K | {0})
        M = len(H)
        g = n//M
        require(H == set(range(0, n, g)), "actual subgroup")
        counts = [sum(bits[i::g]) for i in range(g)]
        errors = sum(min(s, M-s) for s in counts)
        require(sum(dist[h] for h in H) == 2*sum(s*(M-s) for s in counts), "coset average")
        require(errors*(len(K)+1) < 3*M*k, "majority approximation")
        require(max(dist[h] for h in H) <= D*k, "subadditive distance")
        start = states.index(min(states))
        x0 = d+states[start]
        for h in H:
            require(d+states[(start+h) % n] <= x0*3**(D*(k//2)), "Cayley height")
        checks += 1
    return checks


def mechanical(length, slope, intercept):
    return tuple(int((i+1)*slope+intercept) - int(i*slope+intercept)
                 for i in range(length))


def align(source, target):
    # The first argument supplies the mechanical input, the second the physical bits.
    a, b = len(source), len(target)
    costs = [list(range(b+1))]+[[i]+[0]*b for i in range(1, a+1)]
    for i in range(1, a+1):
        for j in range(1, b+1):
            costs[i][j] = min(costs[i-1][j]+1, costs[i][j-1]+1,
                              costs[i-1][j-1]+(source[i-1] != target[j-1]))
    columns = []
    i, j = a, b
    while i or j:
        if i and j and costs[i][j] == costs[i-1][j-1]+(source[i-1] != target[j-1]):
            columns.append((source[i-1], target[j-1]))
            i -= 1
            j -= 1
        elif i and costs[i][j] == costs[i-1][j]+1:
            columns.append((source[i-1], None))
            i -= 1
        else:
            columns.append((None, target[j-1]))
            j -= 1
    return tuple(reversed(columns)), costs[a][b]


def check_alignment(bits, d, states, C, slope, target):
    n = len(bits)
    source = target
    columns, E = align(source, bits)
    require(sum(x != y for x, y in columns) == E, "alignment cost")
    active = [j for j, (_,y) in enumerate(columns) if y is not None]
    Hn = max(abs(n*sum(bits[i:j])-(j-i)*sum(bits)) for i in range(n+1) for j in range(i,n+1))
    require(Hn < n*(E+2), "centered edit discrepancy")
    require(Fraction(max(states), d)**n <= C**n * 3**Hn, "exact physical height")
    q = (n-1)//(E+2)
    if not q:
        return
    clean = []
    for i in range(n-q+1):
        sub = columns[active[i]:active[i+q-1]+1]
        if all(x == y for x,y in sub):
            clean.append((bits[i:i+q], i))
    require(n-q+1-len(clean) <= E*q, "dirty window cover")
    factors = {word for word,_ in clean}
    require(len(factors) <= q+1 < len(clean), "clean factor collision")
    seen = {}
    for word, i in clean:
        if word in seen:
            diff = abs(states[i]-states[seen[word]])
            require(diff > 0 and diff % 2**q == 0, "native separation")
            break
        seen[word] = i
    require(2**q < d*(C+1)*3**(E+2), "finite logarithmic bound")
    require(0 <= slope <= 1, "slope")


def near_mechanical_controls():
    cycles = families = edits = 0
    for n in range(2, 13):
        for mask in range(1, 2**n):
            bits = cyclic_word(mask, n)
            rotations = {bits[h:]+bits[:h] for h in range(n)}
            if bits != min(rotations) or len(rotations) != n:
                continue
            physical = actual_cycle(bits)
            if physical is None:
                continue
            d, states, C = physical
            cycles += 1
            families += spectrum(bits,d,states)
            slopes = (Fraction(sum(bits), n), Fraction(5,8), Fraction((mask % 8),7))
            for j, slope in enumerate(slopes):
                length = max(0, n+(mask+j) % 7-3)
                target = mechanical(length, slope, Fraction(mask % 11, 11))
                check_alignment(bits,d,states,C,slope,target)
                edits += 1
    print("primitive rational necklaces", cycles, "subgroup cutoffs", families,
          "optimal alignments", edits)


def defect_family(g,v):
    a,b = 2**g, 3**v
    sign = 1 if a>b else -1
    ratio = Fraction(max(a,b), min(a,b))
    upper = 1
    while ratio**(2*upper) <= 27:
        upper *= 2
    lower = upper//2
    while upper-lower > 1:
        mid=(upper+lower)//2
        if ratio**(2*mid) <= 27:
            lower=mid
        else:
            upper=mid
    M=lower
    e=1 if sign==1 else 2
    n=g*M
    u=v*M+sign*e
    require(3**u < 2**n < 3**(u+1), "exact critical weight")
    normal=(1,)*v+(0,)*(g-v)
    changed=(1,)*(v+sign)+(0,)*(g-v-sign)
    bits=changed*e+normal*(M-e)
    d,states,_=actual_cycle(bits)
    require(len(set(states)) == n, "primitive physical cycle")
    mask=sum(bit << i for i,bit in enumerate(bits))
    modulus=(1 << n)-1
    for j in range(1, M):
        h=j*g
        rotated=((mask << h) & modulus) | (mask >> (n-h))
        require((rotated ^ mask).bit_count() <= 2*e, "all subgroup shifts")
    require((min(states)+d)*3**e > 2**((M-e-2)*g), "nearly full denominator")
    print("block",g,v,"rows",M,"period",n,"changed rows",e,
          "complete reduced denominator bit length",d.bit_length())


def cutoffs():
    a = Fraction(65,41)
    for T,b,expected in [(217000000000,39,369788),(2**100,101,894200757095011)]:
        L=11+Fraction(143,10)*b
        cost=lambda e:(e+2)*(L+a*(e+2))
        require(2*T <= 2**b and cost(expected-1)<T <= cost(expected),
                "mechanical cutoff certificate")
        print("minimum mechanical edits certified",expected,"at period floor",T)
        crossings = 522498 if b==39 else 1264590838166868
        height = 25+Fraction(286,10)*b
        area = lambda c: c*height+a*c*c/2
        require(area(crossings-2)<T<=area(crossings),"crossing certificate")
        print("minimum geometric grid crossings",crossings,"at period floor",T)


if __name__ == "__main__":
    cutoffs()
    near_mechanical_controls()
    for pair in [(5,3),(8,5),(19,12),(46,29),(65,41)]:
        defect_family(*pair)
