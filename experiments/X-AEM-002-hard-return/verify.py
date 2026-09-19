#!/usr/bin/env python3
"""Independent AHR reconstruction: forward cylinder lifting and CRT in u.
Imports neither generator nor repository modules. No assertions for checks.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path


def require(ok, message):
    if not ok:
        raise ValueError(message)

def enc(x):
    return json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=True).encode()

def sha(x):
    return hashlib.sha256(enc(x)).hexdigest()

def valuation(n):
    require(type(n) is int and n>0,'positive integer required')
    e=0
    while n%2==0:
        e+=1;n//=2
    return e

def orbit(n,length):
    require(type(n) is int and n>0,'invalid source type/value')
    require(type(length) is int and length>=0,'invalid clock')
    path=[n];bits=[]
    P,D,A=1,1,0
    for _ in range(length):
        b=n%2;bits.append(str(b))
        if b:
            A=3*A+D;P*=3;n=(3*n+1)//2
        else:
            n//=2
        D*=2;path.append(n)
    require(P*path[0]+A==D*n,'independent affine endpoint mismatch')
    return path,''.join(bits)

def validate_meeting(n,m,wn,wm):
    require(type(n) is int and type(m) is int and 0<m<n,'source order/type')
    p,w=orbit(n,len(wn));q,z=orbit(m,len(wm))
    require(w==wn and z==wm,'physical parities')
    require(p[-1]==q[-1],'meeting endpoint')
    return p,q

def bound(j):
    k=0
    while True:
        k+=1
        if 3*9**(k+j)>=128*64**j*8**k:
            return k

def primitive(c):
    r=valuation(c+2)-1
    if r<3:
        return r,'outside',c
    a,wa=orbit(9*c+2,r+3);b,wb=orbit(c,r+3)
    quotient=(c+2)//2**(r+1)
    good=pow(3,r,4)*(quotient%4)%4==1
    left='0000'+'1'*(r-3)+('01' if good else '00')
    right='0'+'1'*r+('00' if good else '01')
    require(wa==left and wb==right,'primitive parity template')
    require(min(a+b)*64>=9*c,'primitive state bound')
    if good:
        require(a[-1]==b[-1],'primitive merge')
        return r,'merge',a[-1]
    require(b[-1]==9*a[-1]+2,'swapped return')
    require((a[-1]<c)==(r<=7),'growth classification')
    return r,'hard',a[-1]

def run_scan(c,budget):
    original=c;labels=[]
    for _ in range(budget):
        r,kind,z=primitive(c)
        if kind=='outside':
            return [original,'outside',labels,c]
        labels.append([r,kind]);c=z
        if kind=='merge':
            return [original,'merge',labels,c]
    return [original,'budget',labels,c]

def compile_forward(labels):
    # Current parameter = (A*C+B)/2^s. Add each guard by one congruence.
    A,B,s,residue=1,0,0,0
    for i,r in enumerate(labels):
        good=i+1==len(labels)
        b0=1 if (r+(0 if good else 1))%2==0 else 3
        local=2**(r+1)*b0-2
        modulus=2**(s+r+3)
        new=(2**s*local-B)*pow(A,-1,modulus)%modulus
        require(new%2**s==residue,'incompatible refined guard')
        residue=new
        if not good:
            p=3**(r-1)
            A,B=p*A,p*B+(2*p-2**(r+1))*2**s
        s+=r+3
    require(0<residue<2**s,'canonical cylinder representative')
    for t in (0,1,17):
        row=run_scan(residue+2**s*t,len(labels))
        require(row[1]=='merge' and [v[0] for v in row[2]]==list(labels),
                'cylinder physical sample')
    return residue,2**s

def input_via_u(k,h,labels,t):
    c,M=compile_forward(labels)
    N=M*2**(h+6)
    rhs=2**(h+6)*c+2**(h+4)-3**h
    u0=rhs*pow(3**(h+2*k),-1,N)%N
    eps=1 if k%2 else -1
    u=u0+N*((eps-u0)*pow(N,-1,3)%3)+3*N*t
    require(u>0 and u%2==1,'positive odd quotient')
    n=2**(3*k)*u-5
    z=9**k*u+1
    require(n%12==3 and valuation(z)==h+4,'original exact guards')
    a=z//2**(h+4)
    require(3**(h+1)*a%4==3,'complementary rather than parent-good exit')
    C=(3**h*a-1)//4
    require(4*C+1==3**h*a and C%M==c,'entry equation')
    return n,n//3-2,C,u,a

def check_case(k,h,labels,t):
    n,x,C,u,a=input_via_u(k,h,labels,t)
    entry=C;growth=0
    for i,wanted in enumerate(labels):
        r,kind,z=primitive(C)
        require(r==wanted and kind==('merge' if i==len(labels)-1 else 'hard'),
                'actual itinerary')
        if kind=='hard' and z>C:
            growth+=1
        C=z
    clock=3*k+h+6+sum(r+3 for r in labels)
    p,wn=orbit(n,clock);q,wx=orbit(x,clock)
    require(0<x and 3*x<n,'exact one-third source order')
    require(p[-1]==q[-1]==C,'original-source collision')
    # Reconstruct the entry states independently from literal raw trajectories.
    en,_=orbit(n,3*k+h+6);ex,_=orbit(x,3*k+h+6)
    require(en[-1]==9*entry+2 and ex[-1]==entry,'entry arms/clocks')
    if k>=bound(len(labels)):
        require(min(p[1:])>n,'all displayed forward states above source')
    return {'k':k,'h':h,'labels':list(labels),'t':t,'n':n,'x':x,'entry':entry,
            'u':u,'a':a,'word_n':wn,'word_x':wx,'clock':clock,
            'endpoint':C,'min_forward':min(p[1:]),'growing_returns':growth}

def first_one(n):
    out=[n]
    for _ in range(1000):
        if n==1:
            return out
        n=(n//2 if n%2==0 else (3*n+1)//2);out.append(n)
    raise ValueError('control cap')

def counts(rows,index):
    d={}
    for v in rows:
        d[v[index]]=d.get(v[index],0)+1
    return d

def reconstruct():
    patterns=[(r,) for r in range(3,11)]
    patterns.extend((r,s) for r in (3,8,9) for s in (3,4,7))
    patterns.extend(((9,5,3),(3,4,5,8,3),(8,)*12+(4,),(3,9,4,8)*4+(3,)))
    specs=[(k,h,rs,t) for rs in patterns for k in (1,2,8,40,82)
           for h in (1,2,7) for t in (0,1)]
    specs.extend(((49,1,(3,),0),(82,1,(9,5,3),0),
                  (bound(13),3,(8,)*12+(4,),0),
                  (bound(17),2,(3,9,4,8)*4+(3,),0),
                  (250,80,(3,7,8,9,4),1)))
    families=[check_case(*s) for s in specs]
    grid=[run_scan(c,8) for c in range(1,65537)]
    ambient=[]
    for k in range(1,7):
        for u in range(1,4096,2):
            n=2**(3*k)*u-5;z=9**k*u+1;s=valuation(z)
            if s<5:
                ambient.append([k,u,n,'entry_guard',None]);continue
            h=s-4;a=z//2**s
            if pow(3,h+1,4)*(a%4)%4==1:
                ambient.append([k,u,n,'parent_good_exit',None]);continue
            C=(3**h*a-1)//4
            row=run_scan(C,8)
            ambient.append([k,u,n,'new_'+row[1],row])
    controls={str(n):first_one(n) for n in (3003,999,128,14)}
    require(len(controls['3003'])==30 and len(controls['999'])==35,'phase-control times')
    require((len(controls['128'])-len(controls['14']))%2==1,'second phase control')
    summary={'schema':'collatz-ahr-002-v1','family_count':len(families),
             'family_sha256':sha(families),
             'no_descent_bound_cases':sum(f['k']>=bound(len(f['labels'])) for f in families),
             'growing_return_cases':sum(f['growing_returns']>0 for f in families),
             'grid_count':len(grid),'grid_counts':counts(grid,1),'grid_sha256':sha(grid),
             'ambient_count':len(ambient),'ambient_counts':counts(ambient,3),
             'ambient_sha256':sha(ambient),
             'cylinders':[[list(rs),*compile_forward(rs)] for rs in patterns],
             'controls':controls,'thresholds':[[j,bound(j)] for j in (1,2,3,8,13,17)],
             'examples':[families[specs.index(s)] for s in
                         ((1,1,(3,),0),(1,1,(9,5,3),0),(82,1,(9,5,3),0))]}
    return {'payload':summary,'sha256':sha(summary)}

def validate(candidate,expected):
    require(type(candidate) is dict and set(candidate)=={'payload','sha256'},'envelope keys')
    require(candidate['sha256']==sha(candidate['payload']),'digest mismatch')
    require(enc(candidate)==enc(expected),'typed independent reconstruction mismatch')

def self_test(expected):
    cases=[]
    def mutated(path,value):
        c=copy.deepcopy(expected);obj=c['payload']
        for part in path[:-1]:
            obj=obj[part]
        obj[path[-1]]=value;c['sha256']=sha(c['payload']);cases.append(c)
    mutated(['family_count'],634)
    mutated(['family_count'],635.0)
    mutated(['examples',0,'k'],True)
    mutated(['examples',0,'n'],149812)
    mutated(['examples',0,'x'],149811)
    mutated(['examples',0,'endpoint'],1)
    mutated(['examples',0,'clock'],15)
    mutated(['examples',0,'word_n'],'0')
    mutated(['examples',0,'word_x'],'1')
    mutated(['examples',2,'min_forward'],0)
    mutated(['grid_counts','merge'],2115)
    mutated(['ambient_counts','new_merge'],12)
    mutated(['cylinders',0,1],47)
    mutated(['thresholds',0,1],48)
    mutated(['controls','3003'],[3003,1])
    mutated(['family_sha256'],'0'*64)
    for c in cases:
        try:
            validate(c,expected)
        except ValueError:
            continue
        raise ValueError('resealed mutation accepted')
    bad=[(7,11,'11','1'),(3,1,'0','1'),(True,1,'',''),(7,3,'','')]
    for args in bad:
        try:
            validate_meeting(*args)
        except ValueError:
            continue
        raise ValueError('bad direct witness accepted')
    # A deliberately truncated certificate must be unfinished, not successful.
    c,_=compile_forward([8]*12+[4])
    require(run_scan(c,0)[1]=='budget' and run_scan(c,8)[1]=='budget','budget distinction')
    require(run_scan(89,8)[1]=='outside','outside-language distinction')
    return len(cases),len(bad)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('artifact',type=Path)
    ap.add_argument('--self-test',action='store_true')
    args=ap.parse_args()
    expected=reconstruct()
    validate(json.loads(args.artifact.read_text()),expected)
    mutations,bad=self_test(expected) if args.self_test else (0,0)
    print(json.dumps({'status':'PASS','sha256':expected['sha256'],
                      'resealed_rejected':mutations,'direct_rejected':bad},sort_keys=True))

if __name__=='__main__':
    main()
