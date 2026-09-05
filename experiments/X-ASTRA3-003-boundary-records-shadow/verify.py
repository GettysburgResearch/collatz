#!/usr/bin/env python3
"""Independent physical reconstruction; imports no generator/repository module."""
import argparse
import copy
from fractions import Fraction
from hashlib import sha256
from math import isqrt
from pathlib import Path
import json

S = 2**80
SCHEMA = 'X-ASTRA3-003/v1'
SCOPE = 'finite exact interfaces and all-source finite-time enclosures; no Collatz proof'


def seal(x):
    return sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def step(x):
    if x % 2 == 0:
        return x//2
    return (x*3+1)//2


def vp(x,p):
    x = abs(x)
    if not x:
        raise ValueError('zero polynomial observation')
    q = p; answer = 0
    while x % q == 0:
        answer += 1; q *= p
    return answer


def root_ratio(num,den):
    # Reciprocal square-root formulation, followed by integer correction.
    v = num//isqrt(num*den)
    while v*v*den > num:
        v -= 1
    while (v+1)*(v+1)*den <= num:
        v += 1
    return v


def weight(n):
    v = root_ratio(S*S,n**3)
    return (v,v+1)


def lin(terms):
    lo=hi=0
    for c,(a,b) in terms:
        lo += c*(a if c>=0 else b)
        hi += c*(b if c>=0 else a)
    return lo,hi


def ap_sum(a,m):
    vals=[weight(a+j*m) for j in range(64)]
    z=a+64*m
    integral=root_ratio(4*S*S,m*m*z)
    return sum(x[0] for x in vals)+integral, sum(x[1] for x in vals)+integral+1+weight(z)[1]


def curvature(a,m,j):
    vals=[weight(a+t*m) for t in range(50)]
    terms=[]
    if j==0:
        terms.append((1,vals[0]))
    if j==2:
        terms.append((-1,vals[0]))
    for t in range(16):
        z=3*t
        if j==0:
            terms.extend([(1,vals[z]),(-1,vals[z+1]),(-1,vals[z+2]),(1,vals[z+3])])
        if j==1:
            terms.extend([(-1,vals[z]),(2,vals[z+1]),(-1,vals[z+2])])
        if j==2:
            terms.extend([(-1,vals[z+1]),(2,vals[z+2]),(-1,vals[z+3])])
    lo,hi=lin(terms); tail=max(0,vals[48][1]-vals[49][0])
    return (lo,hi+tail) if j==0 else (lo-tail,hi)


def ordinary_roots(k,H):
    m=2**k; out=[]
    for r in range(m):
        x=r; odd=0; lift=0
        for t in range(k+1):
            # x is the literal t-th iterate of the residue representative.
            lift=max(lift,((H-x)*2**t)//(m*3**odd)+1)
            if t<k:
                odd += x%2; x=step(x)
        out.append((r,r+m*lift))
    return out


def boundaries():
    output=[]; full_roots=[]; lifts=0
    for H in [64,4096]:
        for k in range(13):
            m=2**k; rows=ordinary_roots(k,H)
            Ms=[];Qs=[];Ds=[];Gs=[]; Bs=[[],[],[]];Vs=[];colors=[0,0,0]
            for r,a in rows:
                full_roots.append([H,k,r,a])
                j=next(j for j in range(3) if (a+j*m)%3==2)
                colors[j]+=1; Bs[j].append((1,weight(a)))
                if j==0:
                    Vs.extend([(1,weight(a)),(-1,weight(a+m))])
                Ms.append((1,ap_sum(a,m)));Ds.append((1,curvature(a,m,j)))
                b=a+j*m
                while b <= (3*H+1)//2:
                    Gs.append((1,weight(b))); b+=3*m
                Qs.append((1,ap_sum(b,3*m)))
                for n in [a,a+m,a+2*m,a+3*m]:
                    path=[n]
                    for _ in range(k):
                        path.append(step(path[-1]))
                    assert min(path)>H;lifts+=1
                if a>m:
                    y=a-m; low=y
                    for _ in range(k):
                        y=step(y);low=min(low,y)
                    assert low<=H
            mass=lin(Ms);qmass=lin(Qs);delta=lin(Ds);guard=lin(Gs)
            b0=lin(Bs[0]);b2=lin(Bs[2]);v0=lin(Vs)
            major=lin([(1,b0),(-1,b2),(1,v0),(-3,guard)])
            iq=lin([(1,mass),(1,delta),(-3,guard)])
            assert max(iq[0],3*qmass[0])<=min(iq[1],3*qmass[1])
            output.append(dict(H=H,k=k,colors=colors,M=list(mass),Q=list(qmass),
                defect3=list(delta),guard=list(guard),B0=list(b0),signed_majorant3=list(major),
                positive_certificate=400*b0[1]<=7*mass[0],
                root_certificate=200*major[1]<=7*mass[0],
                signed_certificate=200*delta[1]-600*guard[0]<=7*mass[0],
                direct_certificate=200*qmass[1]<=69*mass[0]))
    return dict(scale=S,ap_terms=64,curvature_terms=16,rows=output,
                cylinders=len(full_roots),physical_lifts=lifts,root_digest=seal(full_roots))


def records():
    paths=[];logs=[];positions=0
    starts=list(range(1,513))+[2**a-1 for a in range(3,16)]
    for n in starts:
        path=[n]
        while len(path)<=160:
            nxt=step(path[-1])
            if nxt in path:
                break
            path.append(nxt)
        assert len(set(path))==len(path)
        ordered=sorted(x for x in path if x%2)
        assert all((i+1)**40<=5**40*x**39 for i,x in enumerate(ordered))
        paths.append([n,path])
        for start in range(min(len(path),12)):
            x0=path[start];stop=start
            while stop<len(path) and path[stop]>=x0:
                stop+=1
            seg=path[start:stop];q=0;cs=[Fraction(1)];rec=[0]
            product=Fraction(1)
            for i,x in enumerate(seg[:-1],1):
                q+=x%2
                cs.append(Fraction(3**q,2**i))
                if cs[-1]<min(cs[:-1]):
                    rec.append(i)
                if x%2:
                    product*=Fraction(x*3+1,x*3)
                assert product==Fraction(seg[i],x0)/cs[-1]
                positions+=1
            cap=(x0*product).__floor__()
            assert len(rec)<=cap-x0+1
            assert all(x0<=seg[i]<=cap for i in rec)
            gaps=[rec[i+1]-rec[i] for i in range(len(rec)-1)]+[len(seg)-1-rec[-1]]
            assert max(gaps)>= (len(seg)-2+(cap-x0+1))//(cap-x0+1)
            for left,right in zip(rec,rec[1:]):
                assert all(cs[i]>=cs[left] for i in range(left,right))
                assert cs[right]<cs[left]
            logs.append([n,start,len(seg),cap,rec,product.numerator,product.denominator])
    core=[]
    for n in range(1,65):
        x=n;k=0
        while x!=1:
            x=step(x);k+=1
            assert k<1000
        core.append(k)
    return dict(source_count=len(starts),path_digest=seal(paths),records_digest=seal(logs),
                segments=len(logs),positions=positions,core=core,
                integer_inequalities=[8*3125**24<3456**24,200*11<69*32,200*65<69*192,3**200<2**317,
                                      317**6340<2**6023*117**2340*200**4000,
                                      8*177**2>500**2,463**2*65**3>250**2*98**3,49647<49650])


def polynomial(c,x):
    return sum(v*x**i for i,v in enumerate(c))


def prime_list(n):
    p=2;out=[]
    while n>1:
        if n%p==0:
            out.append(p)
            while n%p==0:
                n//=p
        p+=1
    return out


def dictionaries():
    return [dict(mod=8,features=[(2,[0,1]),(2,[1,1]),(3,[0,1]),(3,[1,1])]),
        dict(mod=35,features=[(2,[1,0,1]),(3,[0,1,1]),(5,[1,3]),(7,[-1,0,1])]),
        dict(mod=105,features=[(p,[-(3**a-2**a),2**(a+1)-3**a])
            for a in range(2,9) for p in [2,3,5,7]]+[(2,[1,1]),(3,[1,2])])]


def observations(n,dd):
    return [vp(polynomial(c,n),p) for p,c in dd['features']]+[n%dd['mod']]


def shadows():
    dicts=dictionaries();rows=[];packets=blocks=0
    for index,dd in enumerate(dicts):
        primes=sorted(set([2,3]+prime_list(dd['mod'])+[p for p,c in dd['features']]))
        a=2
        while True:
            if any(a%(p-1) for p in primes if p>3):
                a+=1;continue
            alpha=Fraction(3**a-2**a,2**(a+1)-3**a)
            if all(polynomial(c,alpha) for p,c in dd['features']):
                break
            a+=1
        powers={p:max([1,vp(dd['mod'],p)]+[
            vp(polynomial(c,alpha).numerator,p)+1 for pp,c in dd['features'] if pp==p]) for p in primes}
        for K in [1,2,4,8,16,32]:
            modulus=1
            for p,e in powers.items():
                modulus*=p**(e+((a+1)*K if p==2 else 0))
            residue=(alpha.numerator*pow(alpha.denominator,-1,modulus))%modulus
            n=modulus+residue;x=n;ends=[n];feat=observations(n,dd)
            for _ in range(K):
                # No closed-form packet formula used for physical replay.
                aa=bb=0;before=x
                while x%2:
                    x=step(x);aa+=1
                while x%2==0:
                    x=step(x);bb+=1
                assert aa==a and bb==1 and x>before
                assert observations(x,dd)==feat
                ends.append(x);packets+=1
            assert (x-alpha)*(2**((a+1)*K))==(n-alpha)*3**(a*K)
            assert x*2**((a+1)*K)>n*3**(a*K)
            for bound in [1,2,3]:
                t=0
                while t<max(0,K-3):
                    t+=1+(ends[t]//17)%bound;blocks+=1
                    assert observations(ends[t],dd)==feat
            rows.append(dict(dictionary=index,a=a,K=K,source=str(n),endpoint=str(x),
                             feature=feat,modulus=str(modulus)))
    return dict(dictionaries=dicts,rows=rows,packets=packets,adaptive_blocks=blocks,sha256=seal(rows))


def expected_report():
    payload=dict(schema=SCHEMA,scope=SCOPE,boundary=boundaries(),records=records(),shadows=shadows())
    # Normalize tuple/list representation through JSON just as an external reader.
    payload=json.loads(json.dumps(payload))
    return dict(payload=payload,sha256=seal(payload))


def validate(actual,expected):
    if not isinstance(actual,dict) or set(actual)!={'payload','sha256'}:
        raise ValueError('invalid envelope')
    if seal(actual['payload'])!=actual['sha256']:
        raise ValueError('hash mismatch')
    if actual!=expected:
        raise ValueError('independent reconstruction mismatch')


def self_test(expected):
    edits=[lambda p:p.update(scope='global Collatz proof'),
        lambda p:p['boundary'].update(cylinders=1),
        lambda p:p['boundary']['rows'][0]['M'].__setitem__(0,p['boundary']['rows'][0]['M'][0]+1),
        lambda p:p['boundary']['rows'][3].update(positive_certificate=True),
        lambda p:p['records'].update(positions=0),
        lambda p:p['shadows']['rows'][0].update(endpoint='1'),
        lambda p:p['shadows']['dictionaries'].pop(),
        lambda p:p['shadows']['rows'][6].update(a=2)]
    for edit in edits:
        bad=copy.deepcopy(expected);edit(bad['payload']);bad['sha256']=seal(bad['payload'])
        try:
            validate(bad,expected)
        except ValueError:
            pass
        else:
            raise AssertionError('resealed corruption accepted')
    return len(edits)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('report',type=Path)
    ap.add_argument('--self-test',action='store_true');args=ap.parse_args()
    expected=expected_report();validate(json.loads(args.report.read_text()),expected)
    print(expected['sha256']);print('independent physical reconstruction passed')
    if args.self_test:
        print('resealed corruptions rejected:',self_test(expected))

if __name__=='__main__':
    main()
