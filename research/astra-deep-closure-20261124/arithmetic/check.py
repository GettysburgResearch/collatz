"""Exact finite controls for physical Pell fibers and the independent Farey floor."""
from collections import defaultdict
from fractions import Fraction
from math import gcd, isqrt, prod


def require(ok, label):
    if not ok:
        raise ArithmeticError(label)


def factors(n):
    result = {}
    p = 2
    while p*p <= n:
        while n % p == 0:
            result[p] = result.get(p, 0)+1
            n //= p
        p = 3 if p == 2 else p+2
    if n > 1:
        result[n] = 1
    return result


def log_bounds(x, terms=64):
    z = (x-1)/(x+1)
    lower = sum(2*z**(2*j+1)/(2*j+1) for j in range(terms))
    tail = 2*z**(2*terms+1)/((2*terms+1)*(1-z*z))
    return lower, lower+tail


def period_control():
    l2, u2 = log_bounds(Fraction(2))
    l3, _ = log_bounds(Fraction(3))
    _, u3p = log_bounds(Fraction(3)+Fraction(1, 2**71))
    a, b, c, d = 103768467013, 65470613321, 10439860591, 6586818670
    require(Fraction(a, b) < l3/u2 and u3p/l2 < Fraction(c, d), 'log interval')
    require(b*c-a*d == 1 and b+d == 72057431991, 'Farey interval')
    require(2**31*31 < b+d and 2**32*32 < 137500000000, 'cycle rank cutoffs')


def fundamental(D):
    root = isqrt(D)
    m, d, a = 0, 1, root
    pprev, p, qprev, q = 1, a, 0, 1
    while p*p-D*q*q != 1:
        m = d*a-m
        d = (D-m*m)//d
        a = (root+m)//d
        pprev, p = p, a*p+pprev
        qprev, q = q, a*q+qprev
    return p, q


def rank(vectors):
    rows = {}
    for vector in vectors:
        row = {p: Fraction(v) for p, v in vector.items() if v}
        while row:
            p = min(row)
            if p not in rows:
                rows[p] = {q: v/row[p] for q, v in row.items()}
                break
            scale = row[p]
            for q, value in rows[p].items():
                v = row.get(q, 0)-scale*value
                if v:
                    row[q] = v
                else:
                    row.pop(q, None)
    return len(rows)


def ratios(values):
    base = factors(values[0])
    result = []
    for value in values[1:]:
        current = factors(value)
        result.append({p: current.get(p, 0)-base.get(p, 0)
                       for p in current.keys() | base.keys() if p != 2})
    return result


def check_pell():
    by_D = defaultdict(list)
    edges = 0
    sources = set(range(1, 12001, 2))
    for seed_D in (3, 15, 21, 33, 39, 51, 57, 69, 87, 93):
        u, v = fundamental(seed_D)
        X, V = u, v
        while X <= 6*10**10+1:
            if X % 12 == 7:
                sources.add((X-1)//6)
            X, V = u*X+seed_D*v*V, u*V+v*X
    for x in sorted(sources):
        if x % 3 == 0:
            continue
        q = (3*x+1) & -(3*x+1)
        y = (3*x+1)//q
        a = q.bit_length()-1
        D = 3*(2**(a % 2))*prod(p for p, e in (factors(x) | factors(y)).items() if e%2)
        X = 6*x+1
        V = isqrt((X*X-1)//D)
        require(gcd(x, y) == 1 and X*X-D*V*V == 1, 'odd edge to Pell')
        by_D[D].append((X, V, x, y))
        edges += 1
    repeats = 0
    order_tests = 0
    for D, records in by_D.items():
        u, v = fundamental(D)
        X, V, j = 1, 0, 0
        earlier = set()
        for idx, (target, coord, _, _) in enumerate(records):
            while X < target:
                if j:
                    earlier.update(factors(V//v))
                X, V = u*X+D*v*V, u*V+v*X
                j += 1
            require((X,V) == (target,coord), 'Pell power replay')
            if idx:
                require(j>2 and set(factors(V//v))-earlier-{2}, 'fresh odd divisor')
                order_tests += 1
        if len(records) > 1:
            repeats += 1
            vs = [v0 for _, v0, _, _ in records]
            xs = [x for _, _, x, _ in records]
            ys = [y for _, _, _, y in records]
            require(rank(ratios(vs)) == len(records)-1, 'full projected Pell rank')
            require(rank(ratios(xs+ys)) >= len(records)-1, 'physical rank covers fiber')
    require(repeats >= 2 and order_tests >= 3, 'nonvacuous fixed-discriminant tests')
    return edges, len(by_D), repeats, order_tests


def check_ratio_five():
    by_D = defaultdict(list)
    # Include solutions with multiple admissible indices at one discriminant.
    sources = set(range(1, 2001, 2))
    for D in range(2, 180):
        if any(e>1 for e in factors(D).values()):
            continue
        u, v = fundamental(D)
        X, V = u, v
        while X <= 5*10**9:
            if (2*X-3) % 30 == 15:
                sources.add((2*X-3)//15)
            X, V = u*X+D*v*V, u*V+v*X
    for x in sorted(sources):
        one, two = 3*x+1, 15*x+1
        q, t = one & -one, two & -two
        y, z = one//q, two//t
        X = (15*x+3)//2
        require(4*(X*X-1) == 5*q*t*y*z, 'coupled first odd steps')
        f = factors(y)
        for prime, power in factors(z).items():
            f[prime] = f.get(prime, 0)+power
        f[5] = f.get(5, 0)+1
        f[2] = q.bit_length()+t.bit_length()-4
        D = prod(p for p, exponent in f.items() if exponent%2)
        V = isqrt((X*X-1)//D)
        require(X*X-D*V*V == 1, 'coupled squareclass')
        by_D[D].append((X, V, y, z))
    extra = 0
    for records in by_D.values():
        if len(records)<2:
            continue
        xs = [factors(y) for _, _, y, _ in records]
        zs = [factors(z) for _, _, _, z in records]
        def vector(i):
            primes = xs[i].keys() | zs[i].keys() | xs[0].keys() | zs[0].keys()
            return {p: xs[i].get(p,0)+zs[i].get(p,0)-xs[0].get(p,0)-zs[0].get(p,0)
                    for p in primes if p != 2}
        require(rank([vector(i) for i in range(1,len(records))]) == len(records)-1,
                'independent paired products on a fixed discriminant')
        extra += len(records)-1
    require(extra>=2, 'nonvacuous coupled rank tests')
    return len(sources), extra


if __name__ == '__main__':
    period_control()
    edges, classes, repeats, fresh = check_pell()
    coupled, pivots = check_ratio_five()
    print(f'{coupled} coupled sources, {pivots} independent product pivots; '
          f'{edges} literal transitions, {classes} Pell discriminants, {repeats} '
          f'multi-index fibers, {fresh} fresh odd pivots; rational Farey and rank cutoffs passed')
