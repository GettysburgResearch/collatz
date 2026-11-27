"""Bounded exact checks of the signed-grade split and both future-state bounds.

The search window is a diagnostic. The clock and count lemmas cover unrestricted
positive input and follow from the proof and Lean module.
"""
from fractions import Fraction
import json


def need(ok, message):
    if not ok:
        raise ArithmeticError(message)


def physical(n, sign):
    return (3*n+sign)//2 if n%2 else n//2


def odd_step(n, sign):
    x=3*n+sign
    digits=(x&-x).bit_length()-1
    return x>>digits,digits


def first_mark(x, mark, cutoff):
    seen=set();q=0;d=0
    while q<=cutoff:
        if x==mark:return ('mark',q,d)
        if x in seen:return ('repeat',q,d)
        seen.add(x)
        x,e=odd_step(x,-1); q+=1;d+=e
    return ('open',q,d)


def check_split(m, a, D, b, full):
    c=(a<<D)-m
    need(c>0 and D<=full,('domain',a,m,D,c,b,full))
    x=c; y=m; q=0
    for d in range(D):
        need(x%2==y%2 and x+y==a*3**q*2**(D-d),('prefix',a,m,D,d))
        q+=x%2
        x=physical(x,1);y=physical(y,-1)
    need(x+y==a*3**q and q<=b,('split',a,m,D,q,b))
    odd=x
    while not odd%2:odd//=2
    v=c
    for _ in range(q):v,_=odd_step(v,1)
    need(v==odd and 1<=odd<=a*3**b,('ordinary future',a,m,D,odd))
    return q,odd,x%2


def test_a(a,b0,e0):
    counts={'mark':0,'repeat':0,'open':0};pairs=0;even_splits=0;greatest_D=0;greatest_lap=0
    for m in range(1,20000,2):
        status,b,d=first_mark(m,a,240);counts[status]+=1
        if status!='mark' or b%b0:continue
        lap=b//b0;D=d-e0*lap;c=a*2**max(0,D)-m
        if D<=0 or c<=0:continue
        _,_,parity=check_split(m,a,D,b,d)
        lam=Fraction(2**e0,3**b0)
        need(Fraction(m,2**D)<=a*(b+1)*lam**lap,('tail bound',a,m,D,b))
        pairs+=1;even_splits+=not parity;greatest_D=max(greatest_D,D);greatest_lap=max(greatest_lap,lap)
    return {'mark':a,'odd_period':b0,'period_divisions':e0,'input_cutoff':19999,'odd_clock_cap':240,
            'outcomes':counts,'genuine_grade_splits':pairs,'even_at_split':even_splits,
            'maximum_D':greatest_D,'maximum_lap_count':greatest_lap}


def main():
    for k in range(1,129):
        c=(4**k-1)//3;m=((25<<(2*k+1))+1)//3;D=2*k
        need(first_mark(m,17,7)==('mark',7,11+D) and c+m==(17<<D),'one-lap family')
        need(check_split(m,17,D,7,11+D)[:2]==(1,1),'true one-step future')
    powers=[3**28<2**45,2187**32>8*2048**32,2187**128>3**7*2048**128]
    need(all(powers),'exponent comparisons')
    rows=[test_a(1,1,1),test_a(5,2,3),test_a(17,7,11)]
    print(json.dumps({'grade_scans':rows,'one_lap_varying_D_family_instances':128,
                      'exact_exponent_comparisons':len(powers)},sort_keys=True,indent=2))


if __name__=='__main__':main()
