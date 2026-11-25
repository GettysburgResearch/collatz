"""Exact finite inverse tests for the locally integral rational-cycle construction."""
from fractions import Fraction
from functools import lru_cache
from itertools import product

from check_basin import K, cost_thresholds, norm

F = Fraction
LEFT, RIGHT = F(8,5), F(19,10)
ANCHOR = {-2,-1,0,1}


def check(condition, message):
    if not condition:
        raise ValueError(message)


@lru_cache(None)
def phase(i,z):
    return norm(z*F(3)**i)


def wrap(i,z):
    return 1 if 3*phase(i,z)<4 else 2


def history(i,z,octave):
    return [wrap(t,z)+octave(t)-octave(t+1) for t in range(i-K,i)]


def code(gaps):
    n = 0
    for gap in gaps:
        check(gap in (1,2), "legal gap")
        n = 2*n+gap-1
    return n


def affine_from_minimum(i):
    a,b = F(1),F(0)
    def gap(t):
        return wrap(t,F(1)) + int(t not in ANCHOR) - int(t+1 not in ANCHOR)
    if i < 0:
        for t in range(-1,i-1,-1):
            a,b = a*2**gap(t)/3, (b*2**gap(t)-1)/3
    else:
        for t in range(i):
            a,b = 3*a/2**gap(t), (3*b+1)/2**gap(t)
    return a,b


def terminal_residue(gaps,m):
    x = 0
    for a in gaps:
        x = (3*x+1)*pow(2,-a,m)%m
    return x


def matching_carries(k,A,e,target):
    """For a fixed total, find the largest compatible forward affine carry."""
    best = None
    m = 3**(k+e)
    required = pow(2,A,m)*target%m
    def visit(d,used,carry):
        nonlocal best
        if d == k:
            if used == A and carry%m == required:
                best = max(carry, best or 0)
            return
        for a in range(1,A-used-(k-d-1)+1):
            visit(d+1,used+a,3*carry + (1<<used))
    visit(0,0,0)
    return best


def main():
    vals, ix = cost_thresholds()
    # Within each ideal phase interval, all candidate marked positions
    # and all preceding wrap digits are constant. Enumerate every subchoice.
    cuts = sorted({F(1), F(2)} |
                  {norm(c*F(3)**i) for c in (F(1), LEFT, RIGHT)
                   for i in range(-K-2,K+2)})
    min_generic = F(100)
    tested = 0
    for lo,hi in zip(cuts,cuts[1:]):
        z = (lo+hi)/2
        free = [i for i in range(-K,1) if LEFT <= phase(i,z) < RIGHT]
        for bits in product((0,1),repeat=len(free)):
            pattern = dict(zip(free,bits))
            octave = lambda t: pattern.get(t,1)
            bound = vals[ix[code(history(0,z,octave))]]
            min_generic = min(min_generic,lo*2**octave(0)/bound)
            tested += 1
    check(min_generic >= F(8,5), "generic ancestor margin")
    anchor = lambda i: int(i not in ANCHOR)
    equalities = []
    strict = []
    for i in range(-2,K+2):
        past = history(i,F(1),anchor)
        slope,intercept = affine_from_minimum(i)
        check(slope == phase(i,F(1))*2**anchor(i), "anchored physical slope")
        threshold = vals[ix[code(past)]]
        check(slope >= threshold, "anchor leading coefficient")
        if slope > threshold:
            strict.append(slope/threshold)
            continue
        for e, floor, offset in ((1,F(2),F(1)),(0,F(3,4),F(1,4))):
            for k in range(1,K+1-e):
                target_power = floor*3**k/slope
                A = target_power.numerator.bit_length()-1
                if A<k or target_power != (1<<A):
                    continue
                m = 3**(k+e)
                res = terminal_residue(past[-(k+e):],m)
                carry = matching_carries(k,A,e,res)
                if carry is None:
                    continue
                y0 = ((1<<A)*intercept-carry)/3**k
                equalities.append((i,e,k,A,y0))
                check(y0 >= offset, "affine threshold")
    print(f"Depth {K}: {tested} generic interval-pattern pairs, margin {min_generic}, "
          f"strict anchor slack {min(strict)}, {len(equalities)} matched boundary totals.")
    print("Boundary totals (terminal time, extra ternary digit, depth, total, ancestor intercept):")
    for i,e,k,A,y0 in equalities:
        print(i,e,k,A,y0)
    check(bool(equalities), "nonvacuous affine boundary checks")
    physical_control(vals,ix)


def physical_control(vals,ix):
    from check import subset_sum
    p,h = 306,485
    D = 2**h-3**p
    Q = 929
    check(D%Q == 0 and D%(Q**2) != 0, "whole tested prime power")
    b = pow(h,-1,p)
    u = pow(2,(1-b*h)//p,Q)*pow(3,b,Q)%Q
    v = pow(u,-1,Q)
    weights = [pow(v,r,Q) for r in range(p)]
    fixed = {i*h%p for i in range(-2-2*K,2+2*K)}
    free = [r for r in range(p) if
            LEFT**p <= 2**r < RIGHT**p and r not in fixed]
    bits = [1]*p
    for i in ANCHOR:
        bits[i*h%p] = 0
    for i in subset_sum([weights[r] for r in free],
                        -sum((2-j)*w for j,w in zip(bits,weights))%Q,Q):
        bits[free[i]] = 0
    ranks = [i*h%p for i in range(p)]
    gaps,C,A = [],0,0
    for r in ranks:
        b,rn = divmod(r+h,p)
        a = b+bits[r]-bits[rn]
        check(a in (1,2), "literal gap")
        gaps.append(a)
        C = 3*C+2**A
        A += a
    s = F(C,D)
    check(A == h and C%Q == 0 and s.denominator>2**(p//10+1),"literal denominator")
    x = s
    odd, physical = [], []
    for a in gaps:
        check(x.numerator%2 == 1 and x.denominator == s.denominator,"odd phase")
        odd.append(x)
        physical.append(x)
        x = (3*x+1)/2
        if a==2:
            check(x.numerator%2==0, "intervening even phase")
            physical.append(x)
            x /= 2
    check(x == s and min(odd)==s and 3*s<max(odd)<4*s, "cycle and width")
    mant = [x/2**bits[r] for x,r in zip(odd,ranks)]
    sorted_ranks = {x:i for i,x in enumerate(sorted(mant))}
    check([sorted_ranks[x] for x in mant] == ranks, "dyadic ranks")
    ternary = [x if x<3*s else x/3 for x in physical]
    sorted_ranks = {x:i for i,x in enumerate(sorted(ternary))}
    check(all(s<=x<3*s for x in ternary) and
          [sorted_ranks[x] for x in ternary] == [-i*p%h for i in range(h)],
          "ternary ranks")
    delicate = 0
    for i,x in enumerate(odd):
        past = [gaps[(i+j)%p] for j in range(-K,0)]
        upper = vals[ix[code(past)]]
        if x >= (s+F(1,2))*upper + F(3,2)**K-1:
            continue
        for e,floor,off in ((1,F(2),F(1)),(0,F(3,4),F(1,4))):
            for k in range(1,K+1-e):
                z = floor*s+off
                m = 3**(k+e)
                target = terminal_residue(past[-(k+e):],m)
                a = k
                while 2**a*(x-(F(3,2)**k-1)) < z*3**k:
                    if 2**a*upper >= floor*3**k:
                        carry = matching_carries(k,a,e,target)
                        if carry is not None:
                            delicate += 1
                            check((2**a*x-carry)/3**k >= z, "actual ancestor")
                    a += 1
    print(f"Joint physical p={p}, h={h}, canceled factor {Q}, "
          f"reduced denominator bits {s.denominator.bit_length()}, "
          f"{delicate} matched finite-height boundary cases.")


if __name__ == "__main__":
    main()
