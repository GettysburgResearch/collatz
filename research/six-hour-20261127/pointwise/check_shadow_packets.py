"""Exact finite interfaces for moving shadow packets, endpoint ranks and decoder lifts."""
from collections import Counter
from fractions import Fraction
from functools import reduce
from itertools import combinations, product
from math import gcd, lcm, prod
import json
import random


def need(ok, why):
    if not ok:
        raise ArithmeticError(why)


def vp(x,p):
    need(x!=0,'valuation of zero')
    n=0
    while x%p==0:
        x//=p
        n+=1
    return n


def rough(x):
    x=abs(x)
    return x//(2**vp(x,2)*3**vp(x,3))


def offset(w):
    c=0
    s=0
    for e in w:
        c=3*c+(1<<s)
        s+=e
    return c,s


def lift(w,y=None):
    c,total=offset(w)
    q=3**len(w)
    if y is None:
        y=c*pow(1<<total,-1,q)%q
        if y%2==0:
            y+=q
    end=y
    result=[y]
    for e in reversed(w):
        a=(1<<e)*y-1
        need(a%3==0,'positive last-letter division')
        y=a//3
        need(y>0 and y%2==1 and vp(3*y+1,2)==e,'physical backwards edge')
        result.append(y)
    need((1<<total)*end==3**len(w)*y+c,'affine product')
    return list(reversed(result))


def packets():
    rng=random.Random(27943)
    counts=Counter()
    for test in range(720):
        m=rng.randint(1,5)
        # Adjacent shadow pieces deliberately share a boundary in part of the sample.
        w=[]
        units=[]
        phases=[]
        previous=None
        h=1
        for j in range(m):
            left=len(w)
            if j and rng.randrange(6)==0:
                w.append(rng.randint(1,5))
                units.append((left,left+1,None,None))
                previous=None
                continue
            t=previous if previous is not None and rng.randrange(2)==0 else Fraction(
                rng.randint(-19,19),rng.choice((1,2,4,5,7,8,10,11,16)))
            a=t
            for i in range(rng.randint(1,5)):
                h=max(h,abs(t.numerator),t.denominator)
                e=rng.randint(1,4)
                w.append(e)
                t=(3*t-1)/(1<<e)
            h=max(h,abs(t.numerator),t.denominator)
            units.append((left,len(w),a,t))
            previous=t
            phases.extend((a,t))
        c,e=offset(w)
        odd=( (1<<e)-c )*pow(3**len(w),-1,1<<(e+1))%(1<<(e+1))
        x=odd+(1<<(e+1))*(10**14*h+1)
        xs=[x]
        for gap in w:
            z=3*xs[-1]+1
            need(vp(z,2)==gap,'ordinary packet word')
            xs.append(z>>gap)
        need(min(xs)>4*m*(h+1),'high packet')
        C=lcm(*(t.denominator for t in phases))
        maxcoef=2*(h+1)**(2*m+1)
        need(C<=h**(2*m) and C%3!=0,'denominator clearing')
        counts['even_clearings']+=C%2==0
        counts['nontrivial_prime_to_six_clearings']+=rough(C)>1
        root=C*(1<<e)*(xs[-1]+1)
        total=C*3**len(w)*(xs[0]+1)
        terms=[]
        s=[0]
        for gap in w:
            s.append(s[-1]+gap)
        for i,j,a,b in units:
            if a is None:
                left,right=2,-1
            else:
                left,right=1-a,b-1
                ua=a.denominator*xs[i]+a.numerator
                ub=b.denominator*xs[j]+b.numerator
                require_rank=vp(ua,3)+(j-i)
                need(vp(ub,3)==require_rank,'endpoint ternary transport')
                need((1<<(j-i+vp(ub,2)))*3**vp(ua,3)<=h*(xs[i]+1),'dual endpoint clock')
                counts['checked_shadow_clocks']+=1
            for n,coef in ((i,left),(j,right)):
                cc=C*coef
                need(cc==int(cc) and abs(cc)<=maxcoef,'bounded cleared coefficient')
                if not cc:
                    continue
                tri=len(w)-n-int(a is None and n==i)
                term=int(cc)*(1<<s[n])*3**tri
                terms.append((term,int(cc),s[n],tri))
                need(abs(term)*(xs[n]+1)<=root*(h+1),'root dominance ratio')
        need(root+sum(t[0] for t in terms)==total,'compressed total')
        need(2*sum(abs(t[0]) for t in terms)<root,'strong dominance')
        while True:
            cut=None
            for length in range(1,len(terms)+1):
                cut=next((s for s in combinations(range(len(terms)),length)
                          if sum(terms[i][0] for i in s)==0),None)
                if cut is not None:
                    break
            if cut is None:
                break
            terms=[t for i,t in enumerate(terms) if i not in cut]
            counts['deleted_zero_subsums']+=1
        if not terms:
            need(all(e==1 for e in w),'empty pruned vector')
            counts['all_one_packets']+=1
            continue
        vector=[root,*[t[0] for t in terms]]
        g=reduce(gcd,vector)
        hu=vp(g,2)
        hv=vp(g,3)
        Hprime=root//g
        need(Hprime*maxcoef*(xs[0]+1)>=1<<e,'primitive height lower bound')
        for value,coef,p,q in terms:
            block=(1<<max(p-hu,0))*3**max(q-hv,0)
            need((value//g)%block==0 and 0<abs((value//g)//block)<=maxcoef,'clamped positions')
        Q=Fraction(prod(abs(z//g) for z in vector),1)
        Q/=2**sum(vp(z//g,2) for z in vector)
        Q/=3**(vp(total//g,3)+sum(vp(z//g,3) for z in vector[1:]))
        expected=Fraction(rough(root)*prod(rough(t[1]) for t in terms),rough(g)**len(vector))
        expected*=Fraction(3)**(-len(w)-vp(xs[0]+1,3)+vp(xs[-1]+1,3))
        need(Q==expected and Q*3**len(w)<=C*(xs[-1]+1)*maxcoef**(2*m),
             'primitive two-place product')
        counts['nontrivial_rough_scalings']+=rough(g)>1
        counts['primitive_packets']+=1
    return dict(sorted(counts.items()))


def decoder():
    count=Counter()
    for blocks in range(1,9):
        d=3*blocks
        endings=set()
        starts=set()
        for bits in product((0,1),repeat=blocks):
            w=[e for bit in bits for e in (1,1+bit,1)]
            xs=lift(w)
            need(max(xs)==xs[-1]<2*3**d,'least representative coverage')
            y=xs[-1]%(3**d)
            for left in range(d,0,-1):
                e=2 if y%3==1 else 1
                need(e==w[left-1],'one-digit inverse predictor')
                y=((1<<e)*y-1)//3%(3**(left-1))
            end=xs[-1]%(3**d)
            need(end not in endings,'distinct depth-d cylinders')
            endings.add(end)
            c,e=offset(w)
            root=((1<<e)-c)*pow(3**d,-1,1<<(e+1))%(1<<(e+1))
            need(root<=xs[0] and (xs[0]-root)%(1<<(e+1))==0,'least source')
            starts.add(root)
            for i in range(0,d+1,3):
                need(all(2*sum(w[i:i+j])<=3*j for j in range(1,d-i+1)),'future cap')
                need(all(2*sum(w[i-j:i])<=3*j for j in range(1,i+1)),'past cap')
                count['two_sided_finite_boundaries']+=1
            actual=Fraction(3**d,(1<<e)*xs[-1])
            attenuation=prod((Fraction(3*x,3*x+1) for x in xs[:-1]),start=Fraction(1))
            need(actual==attenuation/xs[0],'single-word harmonic charge')
            if blocks<=3:
                mod=3**(d+1)
                r=(3*xs[-1]+1)%mod
                power=next(h for h in range(2,2*3**d+1,2) if pow(2,h,mod)==r)
                y=((1<<power)-1)//3
                xl=lift(w,y)
                need(vp(3*xl[-1]+1,2)==power and (3*xl[-1]+1)>>power==1,'terminating lift')
                count['terminating_realizations']+=1
            count['principal_realizations']+=1
        need(len(starts)==2**blocks,'distinct least starts')
        for bound in (1,2,5,13,29):
            need(sum(x<=bound for x in starts)<=bound,'small-source union')
    return dict(sorted(count.items()))


if __name__=='__main__':
    print(json.dumps({'packets':packets(),'decoder':decoder()},sort_keys=True,indent=2))
