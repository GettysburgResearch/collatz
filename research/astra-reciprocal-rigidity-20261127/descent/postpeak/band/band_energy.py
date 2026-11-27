"""Exact phase and four-copy energy certificates for merger-free bands.

A phase is represented by (A+B*q)/denominator, where q=1/(1-log_3(2))-2.
All ordering, alphabet assignments and reported inequality checks use integers.
"""
from collections import Counter
from functools import cache, cmp_to_key
from itertools import product
from math import log2


def require(condition, message):
    if not condition:
        raise ValueError(message)


@cache
def sign(a, b):
    # (1-alpha)*(a+b*q)=a-b+(2*b-a)*alpha, alpha=log_3(2).
    p, h = a-b, 2*b-a
    left = 3**max(p,0) << max(h,0)
    right = 3**max(-p,0) << max(-h,0)
    return (left>right)-(left<right)


def compare(x, y):
    return sign(x[0]-y[0], x[1]-y[1])


def reduce_phase(x, denominator):
    a,b = x
    # 0<q<1 gives two exact rational lower and upper bounds.
    lo=(a+min(0,b))//denominator
    hi=(a+max(0,b))//denominator+1
    while hi-lo>1:
        mid=(hi+lo)//2
        if sign(a-mid*denominator,b)>=0:
            lo=mid
        else:
            hi=mid
    return a-lo*denominator,b


def phase_types(length, numerator, denominator):
    # R=2^(numerator/denominator), in [81/16,6).
    den=denominator
    cut_a=(den,-den)
    cut_b=(numerator-2*den,numerator-2*den)
    require(compare(cut_a,cut_b)<0 and compare(cut_b,(den,0))<0,
            'the requested radius falls outside the supported alphabet range')
    points={(0,0),(den,0)}
    for i in range(length):
        for a,b in [(0,0),cut_a,cut_b]:
            points.add(reduce_phase((a,b-i*den),den))
    ordered=sorted(points,key=cmp_to_key(compare))
    words=set()
    for left,right in zip(ordered,ordered[1:]):
        # The midpoint has denominator 2*den. Rotate it group by group.
        ra,rb=left[0]+right[0],left[1]+right[1]
        w=[]
        for i in range(length):
            if compare((ra,rb),(2*cut_a[0],2*cut_a[1]))<0:
                w.append(2)
            elif compare((ra,rb),(2*cut_b[0],2*cut_b[1]))<0:
                w.append(3)
            else:
                w.append(4)
            rb+=2*den
            if compare((ra,rb),(2*den,0))>=0:
                ra-=2*den
        words.add(tuple(w))
    return words


@cache
def matrix(kind):
    length=2 if kind==2 else 3
    slots=tuple(range(1,3)) if kind==4 else tuple(range(length))
    rows=[]
    for flags in range(16):
        dest=Counter()
        for a,b in product(slots,repeat=2):
            for c,d in {(a,b),(b,a)}:
                v=(a,b,c,d)
                if any((flags & (1<<i)) and slot==0 for i,slot in enumerate(v)):
                    continue
                new=sum(1<<i for i,slot in enumerate(v) if slot==length-1)
                dest[new]+=1
        rows.append(list(dest.items()))
    return rows


def energy(word):
    counts={0:1}
    for kind in word:
        new=Counter()
        mat=matrix(kind)
        for state,num in counts.items():
            for dest,ways in mat[state]:
                new[dest]+=ways*num
        counts=new
    return sum(counts.values())


def check(length, numerator, denominator, rho_num=None, rho_den=None):
    words=phase_types(length,numerator,denominator)
    top=0.0
    for w in words:
        e=energy(w)
        t=sum(2 if k==2 else 3 for k in w)
        if rho_num is not None:
            require(e**rho_den < 2**(rho_num*t),
                    ('failed energy bound',length,numerator,denominator,w,e,t))
        top=max(top,log2(e)/t)
    print('groups',length,'log2(radius)',f'{numerator}/{denominator}',
          'phase words',len(words),'display max ratio',f'{top:.9f}',
          'checked cap',f'{rho_num}/{rho_den}' if rho_num is not None else 'none',flush=True)


if __name__=='__main__':
    import sys
    if len(sys.argv)>1:
        check(*(int(a) for a in sys.argv[1:]))
    else:
        check(32,5,2,992,1000)
        check(220,51,20,997,1000)
