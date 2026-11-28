"""Exact finite controls for the source-qualified entropy and clock transfers."""
from collections import Counter, defaultdict
from fractions import Fraction
from math import comb, log


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def inverse_unit(y, e):
    z, rem = divmod((1 << e) * y - 1, 3)
    return z if rem == 0 and z % 3 and z % 2 and z > 0 else None


def path_choices(y, length, cap):
    if length == 0:
        yield (), y
        return
    for e in range(1, cap + 1):
        z = inverse_unit(y, e)
        if z is not None:
            for rest, x in path_choices(z, length - 1, cap):
                yield (e,) + rest, x


def physical_tau(n):
    initial = n
    stop = 0
    while n != 1:
        n = (3*n + 1)//2 if n % 2 else n//2
        stop += 1
        require(stop < 10000, f"unresolved bounded fixture {initial}")
    return stop


def entropy(weights):
    return -sum(float(w) * log(float(w)) for w in weights if w)


def stationary_flow_fixture(depth):
    # Odd positive representatives give exactly the same windows as all lifts.
    modulus = 3**(depth + 1)
    lifts = 3**depth
    states = [s for s in range(modulus) if s % 3]
    plans = {}
    end_class = [Counter(), Counter()]
    for s in states:
        odd_rep = s if s % 2 else s + modulus
        options = [(w, z) for w, z in path_choices(odd_rep, depth, 6)
                   if 2*depth <= sum(w) <= 3*depth]
        if not options:
            options = [next(path_choices(odd_rep, depth, 6))]
        plans[s] = options
        for _, z in options:
            end_class[s % 3 - 1][z % 3] += Fraction(1, len(options)*lifts)
    p12, p21 = end_class[0][2], end_class[1][1]
    require(p12 + p21 > 0, 'class fixture requires an irreducible boundary')
    mix = {1: p21/(p12+p21), 2: p12/(p12+p21)}
    require(all(sum(row.values()) == 1 for row in end_class), 'class matrix mass')
    full_occ = Counter()
    full_arr = Counter()
    init = Counter()
    end = Counter()
    chooser_entropy = 0.
    total_cost = Fraction(0)
    for s, options in plans.items():
        prior = mix[s % 3]/lifts
        init[s] = prior
        chooser_entropy += float(prior) * log(len(options))
        for word, _ in options:
            total_cost += prior * Fraction(sum(word), len(options))
            weight = prior / (lifts*len(options))
            for extra in range(lifts):
                z = s + modulus*extra
                if z % 2 == 0:
                    z += modulus*lifts
                for e in word:
                    u = inverse_unit(z, e)
                    require(u is not None, 'stored plan departed its legal lift')
                    full_occ[z % modulus, e] += weight
                    full_arr[z % modulus, e, u % modulus] += weight
                    z = u
                end[z % modulus] += weight
    require(init == end, 'full stationary class mixture at block boundaries')
    require(sum(full_occ.values()) == depth, 'occupation mass')
    flow = {key: v/depth for key, v in full_occ.items() if v}
    mass = Counter()
    incoming = Counter()
    for (s,e), value in flow.items():
        mass[s] += value
        target = (((1 << e)*s-1)//3) % (modulus//3)
        for i in range(3):
            t = target + (modulus//3)*i
            require(full_arr[s,e,t] == value*depth/3, 'hidden trit failed to reset')
            incoming[t] += value/3
    require(mass == incoming, 'stationary occupation balance')
    require(sum(e*v for (_,e),v in flow.items()) == total_cost/depth, 'policy mean cost')
    h_local = sum(float(mass[s]) * entropy([v/mass[s] for (t,_),v in flow.items() if t == s])
                  for s in mass)
    require(h_local + 1e-12 >= chooser_entropy/depth, 'entropy of Markovized flow')
    return len(flow)


def composition_checks():
    checked = 0
    for h in range(1,7):
        counts = {0: 1}
        for b in range(1,11):
            nxt = defaultdict(int)
            for index,n in counts.items():
                for step in range(-h,h+1):
                    nxt[index+step] += n
            counts = nxt
            require(sum(counts.values()) == (2*h+1)**b, 'all zero-sum candidate words')
            require(counts[0] == max(counts.values()), 'central convolution maximum')
            # Chebyshev and interval count, deliberately using an integer bound
            radius = 1
            total = sum(counts.values())
            while 3*radius*radius < 4*b*h*(h+1):
                radius += 1
            require(4*sum(n for i,n in counts.items() if abs(i)<=radius)>=3*total,
                    'centered block window variance bound')
            require(4*(2*radius+1)*counts[0] >= 3*total, 'zero-sum count from maximality')
            checked += 1
    return checked


def row_checks():
    tested = 0
    for y in range(5,40,2):
        if y%3 == 0:
            continue
        for n in range(1,6):
            seen = set()
            totals = Counter()
            for w,x in path_choices(y,n,8):
                require(x not in seen, 'different fixed-depth words have different sources')
                seen.add(x)
                s = sum(w)
                totals[s] += 1
                a = Fraction(2**s,3**n)
                beta = y-Fraction(x,1)/a
                prefix = 0
                symbolic = Fraction(0)
                for j,e in enumerate(w):
                    prefix += e
                    symbolic += Fraction(3**j,2**prefix)
                require(beta == symbolic and beta>=0, 'bounded-real block composition')
                require(physical_tau(x) == s+physical_tau(y), 'true off-cycle first hit')
                tested += 1
            require(all(count <= comb(s-1,n-1) for s,count in totals.items()),
                    'total composition supply')
    require(physical_tau(41)==69 and physical_tau(27)==70, 'critical endpoint seed')
    require(physical_tau(1)!=2+physical_tau(1), 'cycle row is not a first arrival')
    return tested


def main():
    measures = [stationary_flow_fixture(k) for k in (1,2,3)]
    print('finite occupation nonzero state-action pairs', measures)
    print('exact centered convolution cases',composition_checks())
    print('true clock, affine offset and disjoint row words',row_checks())


if __name__ == '__main__':
    main()
