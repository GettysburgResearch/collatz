"""Finite controls for the arbitrary-subshift entropy extraction in O18."""
from collections import Counter, defaultdict
from math import log
from fractions import Fraction
import json


def require(value, message):
    if not value:
        raise RuntimeError(message)


def conditional(pairs):
    by=defaultdict(Counter)
    total=0
    for c,e in pairs:
        by[c][e]+=1
        total+=1
    return sum(v/total*log(sum(c.values())/v) for c in by.values() for v in c.values())


def residue(w):
    q=3**len(w)
    x=0
    for e in reversed(w):
        x=((3*x+1)*pow(2,-e,q))%q
    return x


def count_at(a,w):
    for e in w:
        t=(a<<e)-1
        if t%3:
            return False
        a=t//3
        require(a>0 and a%2==1,'ordinary branch sign/parity')
    return True


def extended_letter(word,j):
    return word[j] if 0<=j<len(word) else 1


def language(n):
    # The marked symbol 7 can recur only after an even number of other
    # symbols. There are minimal forbidden words at every odd spacing,
    # so this closed subshift is not of finite type.
    digits=(1,3,5,7)
    words=[((),None)]
    for _ in range(n):
        words=[(w+(d,),0 if d==7 else None if parity is None else 1-parity)
               for w,parity in words for d in digits if d!=7 or parity!=1]
    return [w for w,_ in words]


def main():
    # These are distinct X_0 in Q cap Z_3. In this two-point subshift
    # neither can code both maximizing words, even though the words have
    # a shared target cylinder and both are legal from ordinary target 5.
    fixed={1:Fraction(-1),3:Fraction(1,5)}
    pp=[x.numerator*pow(x.denominator,-1,3)%3 for x in fixed.values()]
    require(len(set(fixed.values()))==2 and len(set(pp))==1,'no common full code')
    require(all(count_at(5,(e,)) for e in fixed),'ordinary common endpoint')

    tests=strict=windows=0
    maxima=[]
    for n in range(1,9):
        good=language(n)
        groups=defaultdict(list)
        for w in good:
            groups[residue(w)].append(w)
        b,chosen=max(groups.items(),key=lambda z:len(z[1]))
        q=3**n
        a=b if b%2 else b+q
        require(all(count_at(a,w) for w in chosen),'ordinary maximizing fiber')
        require(len(chosen)*q>=len(good),'average-over-cylinders lower bound')
        maxima.append(len(chosen))
        for m in (1,2,3):
            for h in (1,2,3):
                law=[]
                for j in range(n):
                    local=[]
                    full=[]
                    given={}
                    for w in chosen:
                        past=tuple(extended_letter(w,t) for t in range(j-m,j))
                        xj=residue(tuple(extended_letter(w,t) for t in range(j,j+h)))
                        key=(past,xj)
                        local.append((key,w[j]))
                        full.append((w[:j],w[j]))
                        if m<=j<=n-h:
                            require(given.setdefault(w[:j],key)==key,
                                    'prefix fails to determine observed window')
                    if m<=j<=n-h:
                        gap=conditional(local)-conditional(full)
                        require(gap>=-2e-12,'interior conditional entropy direction')
                        strict+=int(gap>1e-7)
                        windows+=1
                    law.extend(local)
                require(log(len(chosen))<=n*conditional(law)+(m+h)*log(4)+2e-11,
                        'time-averaged localized Gibbs inequality')
                tests+=1
    print(json.dumps({'maximizing_fibers':maxima,'finite_subshift_tests':tests,
        'interior_window_tests':windows,'strict_conditioning_savings':strict,
        'common_full_state_counterexample_endpoints':['-1','1/5']},indent=2))


if __name__=='__main__':
    main()
