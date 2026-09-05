#!/usr/bin/env python3
"""Cold finite verifier: does not import the generator or repository modules.

Implementation independence is not independent mathematical review.
"""
from __future__ import annotations
import argparse
from collections import deque
from fractions import Fraction as F
import hashlib
import itertools
import json
from math import isqrt
from pathlib import Path

Q=2**96
N=65536


def require(ok: bool, why: str) -> None:
    if not ok:raise ValueError(why)


def sha(obj: object) -> str:
    return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def step(n: int) -> int:
    return n//2 if n%2==0 else (3*n+1)//2


def root_weight(n: int, exponent:int=3) -> int:
    # Reciprocal via a square root of the denominator, then certify both endpoints.
    D=n**exponent
    den=isqrt(D*Q*Q)
    x=Q*Q//den
    while x*x*D>Q*Q:x-=1
    while (x+1)*(x+1)*D<=Q*Q:x+=1
    require(x*x*D<=Q*Q<(x+1)*(x+1)*D,'bad root enclosure')
    return x


def ceilf(x:F) -> int:
    return -(-x.numerator//x.denominator)


def reconstruct_bases() -> list[list[int]]:
    weights=[root_weight(i) for i in range(1,N+1)]
    principal=F(2,isqrt(N))-F(1,2*N*isqrt(N))
    peano=F(3,16*N*N*isqrt(N))
    z=[sum(weights)+(Q*principal).__floor__(),sum(weights)+N+ceilf(Q*(principal+peano))]
    m=N+1+(2-(N+1))%3
    w1,w3,w5=[root_weight(m,e) for e in (1,3,5)]
    low=F(2*w1,3)+F(w3,2)
    high=F(2*(w1+1),3)+F(w3+1,2)
    residue=[sum(weights[1::3])+low.__floor__(),
             sum(weights[1::3])+len(weights[1::3])+ceilf(high)+ceilf(F(9*(w5+1),16))]
    return [z,residue]


def verify_mass(c:dict) -> None:
    require(c['scale']==Q and c['zeta_cutoff']==N,'changed mass precision/scope')
    base=reconstruct_bases()
    require(c['base_mass_scaled']==base,'base mass interval mismatch')
    require([(x['H'],x['K']) for x in c['mass']]==[(1,40),(64,36)],'mass coverage changed')
    for packet in c['mass']:
        H,K=packet['H'],packet['K']
        eligible=(3*H+1)//2+1
        first=eligible+(2-eligible)%3
        require(packet['eligible_min']==first,'wrong killed odd-inverse boundary')
        reached=set(range(1,H+1))
        queue=deque((i,0) for i in range(1,H+1))
        counts=[0]*(K+1); sums=[0]*(K+1); ecounts=[0]*(K+1); esums=[0]*(K+1)
        while queue:
            x,d=queue.popleft()
            w=root_weight(x)
            counts[d]+=1;sums[d]+=w
            if x>=eligible and x%3==2:ecounts[d]+=1;esums[d]+=w
            if d==K:continue
            pre=[2*x]
            t=2*x-1
            if t%3==0 and t//3>0:pre.append(t//3)
            for u in pre:
                require(step(u)==x,'inverse graph not physical')
                if u not in reached:
                    reached.add(u);queue.append((u,d+1))
        deleted=list(range(2,eligible,3))
        es=sum(root_weight(y) for y in deleted);ec=len(deleted)
        S=C=0
        require(len(packet['rows'])==K+1,'missing horizon')
        for k,row in enumerate(packet['rows']):
            S+=sums[k];C+=counts[k];es+=esums[k];ec+=ecounts[k]
            expect={'k':k,'hit_count':C,'new_hit_count':counts[k],
                    'M_scaled':[base[0][0]-S-C,base[0][1]-S],
                    'Q_scaled':[base[1][0]-es-ec,base[1][1]-es]}
            require(row==expect,f'mass row H={H},k={k} differs')
            require(expect['M_scaled'][0]>0 and expect['Q_scaled'][0]>0,'nonpositive interval')
            if H==64:
                require(200*expect['Q_scaled'][1] <=69*expect['M_scaled'][0],'working bias ceiling failed')
    rows=c['mass'][1]['rows']
    first=next(r['k'] for r in rows if 3*r['Q_scaled'][0]>r['M_scaled'][1])
    require(first==c['H64_naive_one_third_first_certified_failure'],'uniformity refutation changed')
    require(c['H64_69_over_200_checked_through']==36,'asymptotic scope inflation')
    require(8*177**2>500**2 and 463**2*65**3>250**2*98**3,'radical certificate failed')
    require(F(177,500)+F(69,200)*F(463,250)<F(993,1000),'contraction constant failed')
    longest=0
    for seed in range(1,65):
        x=seed
        for k in range(1001):
            if x==1:break
            x=step(x)
        require(x==1,'floor was not verified')
        longest=max(longest,k)
    require(longest==c['floor64_max_hitting_time'],'floor certificate changed')
    b=c['critical_bias'];B=b['scale'];a=b['two_power'][0];d=b['three_power'][0]
    require(b['gamma']==[901,1000] and B==10**9,'critical bias scope changed')
    require(b['two_power']==[a,a+1] and b['three_power']==[d,d+1],'bad critical brackets')
    require(a**1000<2**901*B**1000<(a+1)**1000,'2-power bracket failed')
    require(d**1000<3**901*B**1000<(d+1)**1000,'3-power bracket failed')
    require(b['bounds']==[[a-B,d+1],[a+1-B,d]],'kappa division failed')


def verify_echo(c:dict) -> None:
    hashed=hashlib.sha256();hits=0
    for n in range(1,257):
        for d in range(1,129):
            x,y=n,n+d;t=q=0
            while x%2==y%2:
                q+=x%2
                x,y=step(x),step(y);t+=1
            require(t==(d & -d).bit_length()-1,'first disagreement isometry failed')
            P=2**t;C=3**q;A=P*x-C*n
            z=step(y)
            flag=int(x%2==1 and (2*P-C)*n>C*d+A)
            if x%2:require(bool(flag)==(z<n),'echo descent inequality failed')
            hits+=flag;hashed.update(f'{n},{d},{t},{z},{flag}\n'.encode())
    expect={'n_max':256,'d_max':128,'cases':32768,'certified_descents':hits,'sha256':hashed.hexdigest()}
    require(c['echo']==expect,'echo coverage or data mismatch')


def rational_step(x:F) -> F:
    require(x.denominator%2==1,'not a 2-adic integral rational')
    return (3*x+1)/2 if x.numerator%2 else x/2


def verify_crossing(c:dict) -> None:
    require(c['crossing_sieve']['max_depth']==21,'crossing scope changed')
    levels={};records=[];rejected_examples=[]
    for j in range(1,22):
        P=2**j;q=0
        while 3**(q+1)<P:q+=1
        if 3**q<2**(j-1):continue
        position_sets=[()] if q==0 else ((0,)+rest for rest in itertools.combinations(range(1,j-1),q-1))
        for pos in position_sets:
            word=''.join('1' if i in pos else '0' for i in range(j))
            ones=0;good=True
            for k,ch in enumerate(word,1):
                ones+=int(ch)
                if k<j and 3**ones<2**k:good=False;break
            if not good:continue
            require(ones==q,'wrong first-crossing weight')
            Q3=3**q;A=sum(3**(q-i-1)*2**p for i,p in enumerate(pos));D=P-Q3
            cell=levels.setdefault(str(j),dict(words=0,positive_displacements=0,echo_rejected=0,integral_positive_displacements=0))
            cell['words']+=1
            for d in range(1,(A-1)//P+1):
                rn=A-P*d;r=F(rn,D);t=(d & -d).bit_length()-1
                x=r
                for ch in word:
                    require((x.numerator%2)==int(ch),'formal rational parity mismatch')
                    x=rational_step(x)
                require(x==r+d,'formal endpoint mismatch')
                z=r+d
                for _ in range(t+1):z=rational_step(z)
                reject=int(z<r)
                cell['positive_displacements']+=1;cell['echo_rejected']+=reject
                cell['integral_positive_displacements']+=int(r.denominator==1)
                records.append((word,d,f'{word},{d},{rn},{D},{t},{reject}\n'))
                if reject:
                    rejected_examples.append((word,d,{'word':word,'d':d,'source':[r.numerator,r.denominator],
                        'lookahead':t+1,'next':[z.numerator,z.denominator]}))
    hashed=hashlib.sha256()
    for _,_,text in sorted(records):hashed.update(text.encode())
    require(levels==c['crossing_sieve']['levels'],'first-crossing coverage mismatch')
    require(hashed.hexdigest()==c['crossing_sieve']['sha256'],'crossing transcript mismatch')
    require([v for _,_,v in sorted(rejected_examples)[:8]]==c['crossing_sieve']['examples'],'echo examples mismatch')


def verify_carry_and_macro(c:dict) -> None:
    rules={'ae':'ea','af':'eb','ag':'fa','be':'fb','bf':'ga','bg':'gb'}
    digits={'a':(2,0),'b':(2,1),'e':(3,0),'f':(3,1),'g':(3,2)}
    hashed=hashlib.sha256();total=swaps=0
    for length in range(7):
        for a in itertools.product('abefg',repeat=length):
            start=''.join(a);w=start;steps=0
            value=0
            for ch in w:value=digits[ch][0]*value+digits[ch][1]
            binary=sum(ch in 'ab' for ch in w);ternary=length-binary
            n=value;out=[]
            for _ in range(binary):out.append('ab'[n%2]);n//=2
            for _ in range(ternary):out.append('efg'[n%3]);n//=3
            canonical=''.join(reversed(out));require(n==0,'mixed-radix overflow')
            while True:
                possible=[i for i in range(length-1) if w[i:i+2] in rules]
                if not possible:break
                i=possible[-1]
                w=w[:i]+rules[w[i:i+2]]+w[i+2:];steps+=1
            require(w==canonical,'normal form not canonical')
            inv=sum(start[i] in 'ab' and start[k] in 'efg' for i in range(length) for k in range(i+1,length))
            require(steps==inv,'carry measure failed')
            total+=1;swaps+=steps;hashed.update(f'{start}:{w}:{steps}\n'.encode())
    require(c['carry']==dict(max_length=6,words=total,swaps=swaps,sha256=hashed.hexdigest()),'carry coverage mismatch')
    hashed=hashlib.sha256();longest=0
    for n in range(1,32768,2):
        a=(n+1 & -(n+1)).bit_length()-1;u=(n+1)>>a
        top=3**a*u-1;b=(top & -top).bit_length()-1;m=top>>b
        x=n
        for i in range(a+b):
            require(x%2==(i<a),'macro branch sequence wrong')
            x=step(x)
        require(x==m and m%2==1,'macro endpoint wrong')
        longest=max(longest,a+b);hashed.update(f'{n},{a},{u},{b},{m}\n'.encode())
    require(c['macro']==dict(odd_sources=16384,max_source=32767,max_macro_steps=longest,sha256=hashed.hexdigest()),'macro coverage mismatch')


def verify_ranks(c:dict) -> None:
    configurations={
        'log':[],
        'negative-dyadic-minus-one':[[2,-1,1,-1]],
        'negative-dyadic-plus-one':[[2,1,1,-1]],
        'positive-dyadic-minus-one':[[2,-1,1,1]],
        'positive-ternary-minus-one':[[3,-1,1,1]],
        'negative-ternary-minus-one':[[3,-1,1,-1]],
    }
    def vp(x:int,p:int)->int:
        require(x!=0,'singular rank input');x=abs(x);a=0
        while x%p==0:x//=p;a+=1
        return a
    def exp_rank(n:int,terms:list)->F:
        ans=F(n)
        for p,num,den,power in terms:
            v=vp(den*n-num,p)-vp(den,p)
            ans*=F(p)**(power*v)
        return ans
    records=c['rank_witnesses'];pairs=set()
    require(len(records)==18,'rank witness coverage changed')
    for r in records:
        name=r['candidate'];ell=r['block']
        require(name in configurations and ell in (1,2,4),'unknown rank test')
        require(r['terms']==configurations[name],'rank formula changed')
        pair=(name,ell);require(pair not in pairs,'duplicate rank test');pairs.add(pair)
        x=r['source'];y=x
        for _ in range(ell):y=step(y)
        require(y==r['endpoint'] and x>1_000_000,'rank endpoint/floor changed')
        require(exp_rank(y,r['terms'])>exp_rank(x,r['terms']),'not a rank obstruction')


    macro_records=c['macro_rank_witnesses']
    require(len(macro_records)==6,'macro-rank coverage changed')
    used=set()
    for r in macro_records:
        name=r['candidate']
        require(name in configurations and name not in used,'duplicate macro rank')
        used.add(name)
        require(r['terms']==configurations[name],'macro rank formula changed')
        n=r['source'];x=n;odd=even=0
        require(n>1_000_000 and n%2==1,'macro rank source floor/parity')
        while x%2:x=step(x);odd+=1
        while not x%2:x=step(x);even+=1
        require((x,odd,even)==(r['endpoint'],r['a'],r['b']),'macro rank replay failed')
        require(exp_rank(x,r['terms'])>exp_rank(n,r['terms']),'not a macro rank obstruction')


def verify(payload:dict)->None:
    require(set(payload)=={'certificate','sha256'},'unexpected envelope fields')
    c=payload['certificate']
    require(payload['sha256']==sha(c),'digest mismatch')
    require(c['schema']=='astra-three-routes-v1','schema mismatch')
    require(c['status']=='FINITE_CERTIFICATE_NOT_COLLATZ_PROOF','false theorem status')
    require(c['scope']=={'all_positive_sources':True,'all_times':False,'independent_mathematical_review':False},'scope inflation')
    verify_mass(c);verify_echo(c);verify_crossing(c);verify_carry_and_macro(c);verify_ranks(c)


def main()->None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('certificate',type=Path)
    args=parser.parse_args()
    data=json.loads(args.certificate.read_text())
    verify(data)
    print('PASS independent implementation:',data['sha256'])

if __name__=='__main__':main()
