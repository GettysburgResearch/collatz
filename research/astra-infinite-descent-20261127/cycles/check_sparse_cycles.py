"""Exact finite controls for the sparse-carry and four-label pulse calculations."""
from fractions import Fraction
from itertools import combinations, product
import json
from math import gcd


def require(ok, msg):
    if not ok:
        raise ArithmeticError(msg)


def raw(word):
    carry = 0
    for date, odd in enumerate(word):
        carry = (3 if odd else 1) * carry + ((1 << date) if odd else 0)
    return carry


def fixed(word):
    return Fraction(raw(word), (1 << len(word)) - 3 ** sum(word))


def boundary(word):
    total = 0
    ones_left = sum(word)
    date = 0
    while date < len(word):
        if not word[date]:
            date += 1
            continue
        start = date
        p = ones_left
        while date < len(word) and word[date]:
            date += 1
            ones_left -= 1
        total += (1 << start) * 3**p - (1 << date) * 3**ones_left
    return total


def swap_controls():
    words = 0
    swaps = 0
    pairs = 0
    resonance = [0, 0, 0]
    for h in range(2, 13):
        for w in product((0, 1), repeat=h):
            p = sum(w)
            d = (1 << h) - 3**p
            if not (p and d > 0):
                continue
            words += 1
            require(raw(w) == boundary(w), 'run numerator')
            x = fixed(w)
            change = [i for i in range(h-1) if w[i] != w[i+1]]
            for i in change:
                z = list(w)
                z[i:i+2] = reversed(z[i:i+2])
                xp = fixed(z)
                require((xp-x).denominator == d, 'single edit')
                swaps += 1
            for i,j in combinations(change, 2):
                if j == i+1:
                    continue
                z = list(w)
                for t in (i,j):
                    z[t:t+2] = reversed(z[t:t+2])
                xp = fixed(z)
                a, b = j-i, sum(w[i:j])
                sigma = 1 if w[i] != w[j] else -1
                g = gcd(d, (1 << a) - sigma * 3**b)
                require((xp-x).denominator == d//g, 'double edit')
                if a*p == b*h:
                    common = gcd(h,p)
                    l = a // (h//common)
                    e = gcd(common,l)
                    u, v = 1 << (e*h//common), 3**(e*p//common)
                    if sigma == 1:
                        expected, slot = u-v, 0
                    elif (common//e)%2 == 0:
                        expected, slot = u+v, 1
                    else:
                        expected, slot = 1, 2
                    require(g == expected, 'full resonance formula')
                    resonance[slot] += 1
                pairs += 1
    for k in range(1, 9):
        for n in (2, 3, 7, 13, 91):
            require(fixed(([1]+[0]*(n-1))*k).denominator == 2**n-3,
                    'repeated one-run denominator')
            block = list((1,0)*n)
            block[:2] = [0,1]
            require(fixed(block*k).denominator == 4**n-3**n,
                    'sharp dispersed-edit denominator')
    for n in range(3, 101):
        w = []
        for e in (n, n+1, n, n-1):
            w.extend([1]+[0]*(e-1))
        t = 1 << n
        require(raw(w) == (t+3)*(2*t*t+9), 'primitive four-run numerator')
        require((t**4-81) == (t+3)*(t-3)*(t*t+9), 'four-run determinant')
        # Res(2T^2+9,(T-3)(T^2+9)) = 27 * 81.
        require(2187 % gcd(2*t*t+9,(t-3)*(t*t+9)) == 0, 'resultant')
    return dict(words=words, single_edits=swaps, disjoint_double_edits=pairs,
                resonant_opposite=resonance[0], resonant_equal_even=resonance[1],
                resonant_equal_odd=resonance[2], sharp_repeated_tests=80,
                primitive_four_run_tests=98)



def affine(word, x):
    return (3**sum(word)*x+raw(word))/(1<<len(word))


def powered_controls():
    motifs = [w for h in range(1,5) for w in product((0,1),repeat=h)]
    cases = matched = nonmatched = equal = 0
    for u,v in product(motifs,repeat=2):
        cu,cv = fixed(u),fixed(v)
        for n,m in ((1,1),(2,3),(5,2),(3,5)):
            h1,p1 = n*len(u), n*sum(u)
            h2,p2 = m*len(v), m*sum(v)
            d = (1<<(h1+h2))-3**(p1+p2)
            if d<=0 or p1+p2==0:
                continue
            x = fixed(u*n+v*m)
            y = Fraction(3**p2*((1<<h1)-3**p1),d)
            require(x-cv==(cu-cv)*y,'two centers')
            require(y.denominator==d//gcd(d,(1<<h1)-3**p1),'two-block binomial')
            if cu==cv:
                require(x==cv,'vanishing center difference')
                equal += 1
            if h1*p2==h2*p1:
                b = gcd(h1,p1)
                a0,b0 = h1//b,p1//b
                e = gcd(b,h2//a0)
                require(gcd(d,(1<<h1)-3**p1)==(1<<(a0*e))-3**(b0*e),
                        'complete equal-slope factor')
                matched += 1
            else:
                nonmatched += 1
            cases += 1
    from random import Random
    rng=Random(332155)
    chains=empty=residual=0
    for trial in range(1800):
        r = rng.randrange(1,6)
        us = [rng.choice(motifs) for _ in range(r)]
        vs = [rng.choice(motifs+[()]*20) for _ in range(r)]
        ns = [rng.randrange(1,8) for _ in range(r)]
        blocks = [u*n+v for u,v,n in zip(us,vs,ns)]
        w = sum(blocks,())
        h,p = len(w),sum(w)
        d = (1<<h)-3**p
        if d<=0 or not p:
            continue
        centers = [fixed(u) for u in us]
        defects = [affine(v,centers[i])-centers[(i+1)%r] for i,v in enumerate(vs)]
        val,clock,grade = Fraction(0),0,0
        for j,b in enumerate(blocks):
            val += defects[j-1]*(1<<clock)*3**(p-grade)
            clock+=len(b)
            grade+=sum(b)
        require(d*(fixed(w)-centers[0]-defects[-1])==val,'cyclic connector defect')
        if all(x==0 for x in defects):
            empty+=1
            require(fixed(w)==centers[0],'all center defects zero')
        else:
            residual+=1
        chains+=1
    for n in range(1,51):
        w=(1,1,0,0)*n+(1,0,1,0)*n
        require(fixed(w).denominator==7*(16**n+9**n),'sharp context-free family')
    return dict(two_block_cases=cases,equal_slopes=matched,
                different_slopes=nonmatched,equal_centers=equal,
                connector_chains=chains,zero_defect_chains=empty,
                nonzero_defect_chains=residual,sharp_context_free_cases=50)


def arc_controls():
    from random import Random
    rng = Random(479213)
    cases = edges = changing = neg = zero = same = 0
    worst = Fraction(0)
    for trial in range(2300):
        h = rng.randrange(2,45)
        w = tuple(rng.randrange(2) for _ in range(h))
        p = sum(w)
        if not p or (1<<h)<=3**p:
            continue
        if any(h%k==0 and w[:k]*(h//k)==w for k in range(1,h)):
            continue
        points = sorted(rng.sample(range(1,h),rng.randrange(1,min(h,9))))
        arcs = [w[a:b] for a,b in zip([0]+points,points+[h])]
        x=fixed(w)
        q=x.denominator
        refs = []
        for a in arcs:
            s=fixed(a)
            if trial%2:
                # Starting a nonfixed reference one dyadic cylinder away from
                # the center preserves the signed center denominator at the end.
                start=s + rng.choice((-2,-1,1,2))*(1<<len(a))
                end=affine(a,start)
            else:
                start=end=s
            if start==x:
                break
            require(start.denominator==end.denominator,'reference denominator')
            refs.append((x,start,end))
            x=affine(a,x)
        if len(refs)!=len(arcs):
            continue
        require(x==refs[0][0],'reference closed physical trace')
        delta=1-Fraction(3**p,1<<h)
        hs=max(max(abs(start.numerator),abs(end.numerator),start.denominator)
               for _,start,end in refs)
        m=min(entry[0] for entry in refs)
        require(delta*m<=2*len(arcs)*hs,'small boundary')
        cost=Fraction(0)
        prod=Fraction(1)
        for i,(a,(x,start,end)) in enumerate(zip(arcs,refs)):
            prev=refs[i-1][2]
            k=q*start.denominator*(x-start)/(1<<len(a))
            require(k.denominator==1 and k!=0,'integer separated dyadic gap')
            require(q*start.denominator*(affine(a,x)-end)==3**sum(a)*k,
                    'ternary shadow gap')
            prod *= (x-prev)/(x-start)
            cost += q*start.denominator*abs(start-prev)/(1<<len(a))
            changing += (start!=end)
            same += (start==prev)
            zero += (start==0)
            neg += (start<0)
        require(prod==1-delta,'signed product')
        require(delta<=cost,'weighted height variation')
        worst=max(worst,delta/cost)
        cases+=1
        edges+=len(arcs)
    return dict(partitions=cases,arcs=edges,changing_references=changing,
                matching_interfaces=same,zero_starts=zero,negative_starts=neg,
                largest_observed_fraction_of_bound=str(worst))


COEF = (-1, 3, -3, 1)
ONE = (1, 1, 1, 1)
MARKS = [ONE, (1,2,1,2), (1,1,1,2), (1,1,2,2), (1,1,2,1),
         ONE, (2,1,2,1), (2,1,1,1), (2,2,1,1), (1,2,1,1), ONE]
CLOCKS = (1,2,1,2,2)*2
PULSE = [0,0,1,2,1,0,0,-1,-2,-1,0]


def floor_date(i):
    # floor(17/100 + i log_2(3)); exact also for negative padded dates.
    r = Fraction(2**17)*Fraction(3)**(100*i)
    def pow_le(n):
        return Fraction(2)**n <= r
    n = r.numerator.bit_length() - r.denominator.bit_length()
    if not pow_le(n):
        n -= 1
    require(pow_le(n) and not pow_le(n+1), 'exact logarithmic floor')
    return n//100


def physical_pulse(pad, rank):
    count = 2*pad+10
    dates = [floor_date(i) for i in range(-pad, 11+pad)]
    letters = [y-x for x,y in zip(dates,dates[1:])]
    require(tuple(letters[pad:pad+10]) == CLOCKS, 'mechanical clock')
    masks = [ONE]*pad + MARKS + [ONE]*pad
    carries = [0]*4
    shift = 1
    for m, row in zip(letters, masks):
        carries = [3*c + shift*l for c,l in zip(carries,row)]
        shift <<= m
    dot = lambda row: sum(c*v for c,v in zip(COEF,row))
    require(dot(carries) == 0, 'pulse total')
    mod = 3**count
    res = [c*pow(shift, -1, mod) % mod for c in carries]
    mod2 = 2*mod
    res = [u if u%2 else u+mod for u in res]
    # Integer quadratic containing a row with zero third difference. Choose
    # a large positive scale compared with the CRT modulus and the test rank.
    target = [mod2*(rank**3 + j*rank**2 + j*j*rank) for j in range(3)]
    terminal = [t+v for t,v in zip(target,res)]
    terminal.append(terminal[0]-3*terminal[1]+3*terminal[2])
    require(all(y%mod2 == r for y,r in zip(terminal,res)), 'fourth terminal residue')
    rows = [terminal]
    for m, mask in reversed(list(zip(letters, masks))):
        new = []
        for y,l in zip(rows[-1],mask):
            z = (y << m) - l
            require(z>0 and z%3==0, 'positive integral predecessor')
            x = z//3
            require(x & -x == l, 'exact lowbit')
            new.append(x)
        rows.append(new)
    rows.reverse()
    oddrows = [[x//l for x,l in zip(row,mask)] for row,mask in zip(rows,masks)]
    for row in rows:
        a,b,c,d = row
        require(0 < b-a < c-b < d-c, 'increasing gaps')
    for current,following in zip(oddrows,oddrows[1:]):
        for x,y in zip(current,following):
            require(3*x+1 in (2*y,4*y), 'literal binary odd edge')
    odd = [x for row in oddrows for x in row]
    require(max(odd)<4*min(odd), 'narrow physical band')
    require([dot(r) for r in rows] == [0]*pad+PULSE+[0]*pad,'cubic pulse')
    return dict(padding=pad, odd_steps=count, largest_odd_bits=max(odd).bit_length(),
                distinct_physical_states=len(set(odd)))


if __name__ == '__main__':
    print(json.dumps({
        'scope': 'finite carry, adjacently edited cycles and ordinary four-path controls',
        'sparse': swap_controls(),
        'powered': powered_controls(),
        'arc_height': arc_controls(),
        'native_pulse': [physical_pulse(pad, 20000) for pad in (0,1,7,25,64)],
    }, indent=2, sort_keys=True))
