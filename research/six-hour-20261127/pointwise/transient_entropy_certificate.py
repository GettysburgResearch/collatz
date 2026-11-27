"""Integer replay of finite entropy, positive terminal lifts and the sparse birth model."""
from collections import Counter, defaultdict
from itertools import combinations, product
from math import comb, isqrt, prod
from hashlib import sha256
import json


def check(ok, label):
    if not ok:
        raise ValueError(label)


def step(x):
    return (3*x+1)//2 if x%2 else x//2


def powers(counts):
    return prod(count**count for count in counts if count)


def entropy_controls():
    trials = Counter()
    for source in range(3, 401):
        states, seen = [], set()
        x = source
        while x not in seen and len(states) < 140:
            states.append(x)
            seen.add(x)
            x = step(x)
        P = len(states)
        bits = [x%2 for x in states]
        for m in (5, 9, 13):
            if P < m:
                continue
            for left in (1, source, max(states)//2):
                A = [i for i in range(P-m+1) if left <= states[i] < left+(1<<m)]
                a = len(A)
                if not a:
                    continue
                windows = {tuple(bits[i:i+m]) for i in A}
                check(len(windows)==a, 'native physical dyadic injection')
                for h in (1,2,4):
                    rows = Counter((bits[i+j-h],bits[i+j]) for i in A for j in range(h,m))
                    denom = powers(rows.values())
                    numer = powers([sum(rows[u,v] for v in (0,1)) for u in (0,1)])
                    check(a**a*denom <= (1<<(h*a))*numer, 'finite full conditional entropy')
                    global_diff = sum(u!=v for u,v in zip(bits,bits[h:]))
                    check(rows[0,1]+rows[1,0] <= (m-h)*global_diff, 'linear boundary mismatch')
                    trials['conditional_pair_rows'] += 1
                for k in (1,2,3):
                    rows = Counter((tuple(bits[i+j-k:i+j]),bits[i+j]) for i in A for j in range(k,m))
                    marginals = Counter()
                    for (history,_),count in rows.items():
                        marginals[history] += count
                    check(a**a*powers(rows.values()) <= (1<<(k*a))*powers(marginals.values()),
                          'finite higher conditional entropy')
                    trials['higher_order_rows'] += 1
    return trials


def inverse_one_lift(bits):
    q = sum(bits)
    D = 0
    for j, bit in enumerate(bits):
        if bit: D = 3*D+(1<<j)
    mod = 3**q
    residue = D*pow(1<<len(bits),-1,mod)%mod if mod>1 else 0
    target = (1+3*residue)%(3*mod)
    power = 0
    for r in range(q):
        power += next(i*3**r for i in range(3) if pow(4,power+i*3**r,3**(r+2))==target%3**(r+2))
    if power==0: power=mod
    y = ((1<<(2*power))-1)//3
    check((3*y+1)==1<<(2*power), 'exit to one')
    x = y
    for bit in reversed(bits):
        x = (2*x-1)//3 if bit else 2*x
    for bit in bits:
        check(x>0 and x%2==bit,'positive incoming known-good lift')
        x=step(x)
    check(x==y, 'ends at prescribed pre-one state')
    return power


def generic_controls(number_blocks=4096):
    # B=2, K=64. The target ceil(log_3(2^t (1+t/K)^2)) is evaluated with integers.
    K=64
    m,y=1,1
    t=q=0
    three=1
    reference=defaultdict(int)
    flags=[]
    digest=sha256()
    for j in range(1,number_blocks+1):
        L=1+isqrt((j+1).bit_length()-1)
        target=(1<<(t+L))*(K+t+L)**2
        nextpower=three
        k=0
        while nextpower*K*K<target:
            nextpower*=3
            k+=1
        choices=list(combinations(range(L),k))
        key=(L,k)
        choice=choices[reference[key]%len(choices)]
        reference[key]+=1
        word=[int(i in choice) for i in range(L)]
        loose = three > (1<<(t+L)) and 0<k<L
        if not loose:
            word=[1]*k+[0]*(L-k)
        elif isqrt(j)**2==j:
            before=m
            first=1-y%2
            if word[0]!=first:
                pos=word.index(first)
                word[0],word[pos]=word[pos],word[0]
            flags.append((j,t))
        for i,bit in enumerate(word):
            if y%2!=bit:
                m+=1<<t
                y+=three
            if i==0 and loose and isqrt(j)**2==j:
                check(m==before+(1<<t),'square birth full modulus jump')
            y=step(y)
            three*=3**bit
            t+=1
            q+=bit
            digest.update(bytes([bit]))
            check(three>1<<t and 0<m<=1<<t,'critical gate and canonical positive seed')
        check(nextpower==three,'block total')
    return dict(B=2,K=K,number_blocks=number_blocks,shortcut_dates=t,ones=q,
                authorized_square_flips=len(flags),last_four_flips=flags[-4:],
                least_source_bit_length=m.bit_length(),word_sha256=digest.hexdigest())


def main():
    counts=entropy_controls()
    maximum=0
    for n in range(10):
        for bits in product((0,1),repeat=n):
            maximum=max(maximum,inverse_one_lift(bits))
            counts['all_shortcut_words_with_known_good_lift']+=1
    return dict(finite_physical=dict(counts),largest_half_exit_exponent=maximum,
                critical_shadow=generic_controls())

if __name__=='__main__':
    print(json.dumps(main(),indent=2,sort_keys=True))
