"""Exact finite controls for ordinary one-even excursions."""
from fractions import Fraction
from functools import lru_cache
from itertools import product
import json


def require(test, message):
    if not test:
        raise ArithmeticError(message)


def valuation(x, prime):
    count = 0
    while x % prime == 0:
        x //= prime
        count += 1
    return count


def step(x):
    return (3*x+1)//2 if x % 2 else x//2


def run(x, steps):
    for _ in range(steps):
        x = step(x)
    return x


def block(x):
    m = valuation(x+1, 2)
    a = (x+1) >> m
    r = 3**m*a
    return m, a, r


@lru_cache(None)
def residues(k):
    if not k:
        return {0}
    modulus = 3**k
    result = set()
    for m in range(1, min(k, 5)+1):
        for older in residues(k-m):
            # At the oldest (possibly truncated) block only the newest m trits matter.
            result.add(((3**m*(older+1)-2**m)*pow(2**(m+1), -1, modulus)) % modulus)
    return result


def cycle_word(length, final):
    qs = [3]
    coefficient = Fraction(27,16)
    for i in range(1, length):
        m = 1 if coefficient >= Fraction(4,3) else 2
        coefficient *= Fraction(3**m,2**(m+1))
        require(1 <= coefficient <= Fraction(27,16), 'balance')
        qs.append(m)
    word = [bit for m in qs for bit in [1]*m+[0]]
    return word + [1]*4+[0, 1 if final == 'cross' else 0]


def source(word, h):
    # Lift one parity bit at a time, updating a positive ordinary residue.
    x = 0
    for i,w in enumerate(word):
        if run(x,i)%2 != w:
            x += 2**i
    b = 2**len(word)
    mod = 3**(h+1)
    x += b*((3**h-x)*pow(b,-1,mod)%mod)
    return x + (10*len(word)+1)*b*mod


def concrete_checks():
    by_mode = dict(cross=0, merge=0)
    processed = 0
    first_brakes_paid = 0
    for q in range(1, 100001, 2):
        n = 3*q
        y = n
        seen = set()
        history = []
        while y <= 2*n:
            m,a,r = block(y)
            require(run(y,m) == r-1, 'ordinary run')
            if r%4 != 3:
                require(run((y-1)//2,m+1) == run(y,m+2), 'brake merge')
                if y==n and n%4==1:
                    require((n-1)//4<=q and run((n-1)//4,0)==run(n-1,2),'first lower')
                    first_brakes_paid+=1
                elif y==n:
                    h=valuation(n,3)
                    z=2**h*(n//3**h)-1
                    require(run(z,h)==n-1,'first backward merge')
                    if z%3==0:
                        require(0<z<n,'first smaller multiple')
                        first_brakes_paid+=1
                    elif h>=2:
                        require((2*z+1)%3==0 and 2*z+1<n,'first upper cost')
                        require(run(2*z+1,h+3)==run(z,h+2),'first upper merge')
                        first_brakes_paid+=1
                    else:
                        require(q%12==1,'first escape residue')
                break
            require(y not in seen, 'return before escape at a ternary root')
            seen.add(y)
            z = (r-1)//2
            require(run(y,m+1) == z and z%6 == 1, 'ordinary next')
            require(run(2*y+1,m+3) == run(y,m+2), 'upper partner')
            require(valuation(2*z+1,3)==m and (2**m*((2*z+1)//3**m)-1)==y,'unique inverse')
            if z<=2*n and (2*y+1>=n):
                require(m<=5,'bounded run')
            if m<=5:
                history.append(m)
            else:
                history.clear()
            for k in range(1,9):
                if sum(history) >= k:
                    require(z % (3**k) in residues(k),'composition cylinder')
            y=z
            processed+=1
    for length,h,mode in product((2,5,20,80),(1,2,7),('cross','merge')):
        word=cycle_word(length,mode)
        n=source(word,h)
        require(n%3==0 and valuation(n,3)==h,'CRT')
        y=n
        for _ in range(length):
            m,a,r=block(y)
            require(r%4==3, 'controlled prefix')
            y=(r-1)//2
            require(n<=y<2*n,'before crossing')
        m,a,r=block(y)
        if mode=='cross':
            require(m==4 and r%4==3 and (r-1)//2>2*n,'genuine crossing')
        else:
            require(m==4 and r%4==1 and (y-1)//2<n and (y-1)%6==0,'paying branch')
            require(run((y-1)//2,m+1)==run(y,m+2),'terminal merger')
        by_mode[mode]+=1
    size=[len(residues(k)) for k in range(13)]
    for k in range(1,13):
        require(size[k]==sum(size[max(0,k-5):k]), 'lossless ternary coding')
    return {'odd_q_through':99999,'ordinary_singleton_edges':processed,'first_brakes_paid':first_brakes_paid,
            'balanced_cases':by_mode,'ternary_residue_counts_k_0_to_12':size}


if __name__=='__main__':
    print(json.dumps(concrete_checks(),indent=2,sort_keys=True))
