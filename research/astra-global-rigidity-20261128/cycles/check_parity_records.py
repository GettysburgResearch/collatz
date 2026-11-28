"""Integer controls for true parity records and their deterministic lifetime clock."""
from collections import Counter
from hashlib import sha256
import json


def require(ok, what):
    if not ok:
        raise ValueError(what)


def step(x):
    return (3*x+1)//2 if x%2 else x//2


def symbolic_controls(max_width=15):
    stack = [(0, 0, 0, 0, 0, 0)]
    total = weak = strict = 0
    weak_best, strict_best = {}, {}
    while stack:
        t, q, b, low, carry, prior_low = stack.pop()
        total += 1
        h = b-low
        require(carry*4**q <= (1<<t)*(1<<h)*(4**q-3**q), 'all-prefix reflected carry')
        if b == low:
            weak += 1
            key = t, q
            weak_best[key] = max(weak_best.get(key,0),carry)
        if b < prior_low:
            strict += 1
            require(2*carry*4**q <= (1<<t)*(4**q-3**q), 'strict record carry')
            key = t, q
            strict_best[key] = max(strict_best.get(key,0),carry)
        if t == max_width:
            continue
        for bit in (0,1):
            new_b = b+2*bit-1
            new_carry = 3*carry+(1<<t) if bit else carry
            stack.append((t+1,q+bit,new_b,min(low,new_b),new_carry,low))
    for data,factor in ((weak_best,1),(strict_best,2)):
        for (t,q),carry in data.items():
            require(factor*carry*4**q == (1<<t)*(4**q-3**q), 'optimality at fixed length/grade')
    return {'max_word_length': max_width, 'all_prefix_words': total, 'weak_records':weak,
            'strict_records':strict, 'weak_length_grade_maxima':len(weak_best),
            'strict_length_grade_maxima':len(strict_best)}


def physical_controls(limit=8192):
    counts=Counter()
    observations=sha256()
    worst=(0,1)
    for n in range(1,limit+1):
        cut=0
        while 4**cut < 4*n*n*3**cut:
            cut+=1
        y=n; t=q=low=first=carry=0
        # Finish the finite sample through 1 and two laps, independently of cut.
        while True:
            b=2*q-t
            if b<=low:
                require(y == (n*3**q+(1<<t)-1)//(1<<t),'weak physical ceil')
                if b<low:
                    require(y == (2*n*3**q+(1<<t))//(1<<(t+1)),'strict physical rounding')
                    require(3**(-b)*4**t < 4*n*n*3**t,'strict integer record horizon')
                    require(t<cut,'actual late record')
                    low=b; first=t; counts['physical_strict_records']+=1
            if t==cut:
                cap_low=low; cap_first=first
            if y == 1:
                # The future discrepancy is now b,b+1,b,b+1,... .
                break
            bit=y%2
            carry = 3*carry+(1<<t) if bit else carry
            y=step(y); q+=bit; t+=1
            require((1<<t)*y==3**q*n+carry,'observed numerator')
            require(t<5000,'unexpected control timeout')
        if t>=cut:
            require((low,first)==(cap_low,cap_first),'cut versus complete known orbit')
        else:
            require(first<cut or first==0,'early known terminating tail')
        if first>worst[0]: worst=first,n
        observations.update(f'{n},{low},{first},{cut},{t}\n'.encode())
        counts['physical_starts']+=1; counts['true_steps_to_first_one']+=t
        counts['globally_nonnegative_sources']+=int(low==0)
        counts['strictly_positive_after_start']+=int(n%2 and first==0 and all_positive(n))
    return {**counts,'largest_first_minimum_clock_and_source':worst,'transcript_sha256':observations.hexdigest()}


def all_positive(n):
    x=n; b=0
    while True:
        bit=x%2; x=step(x); b+=2*bit-1
        if b<=0: return False
        if x==1: return True


if __name__=='__main__':
    print(json.dumps({'scope':'Finite exhaustive correction optima and direct positive trajectory controls.',
                      'words':symbolic_controls(),'ordinary':physical_controls()},indent=2,sort_keys=True))
