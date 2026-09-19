#!/usr/bin/env python3
"""Exact bounded generator for AHR; standard library, no convergence oracle."""
import argparse
import hashlib
import json
from pathlib import Path

SCHEMA = 'collatz-ahr-002-v1'

def enc(x):
    return json.dumps(x, sort_keys=True, separators=(',', ':'), ensure_ascii=True).encode()

def digest(x):
    return hashlib.sha256(enc(x)).hexdigest()

def v2(n):
    if type(n) is not int or n <= 0:
        raise ValueError('valuation requires a positive integer')
    return (n & -n).bit_length()-1

def step(n):
    return (3*n+1)//2 if n & 1 else n//2

def replay(n, word):
    path=[n]
    for bit in word:
        if bit not in '01' or int(bit) != n%2:
            raise ValueError('nonphysical word')
        n=step(n)
        path.append(n)
    return path

def threshold(j):
    k=1
    while 3*9**(k+j) < 128*64**j*8**k:
        k+=1
    return k

def transition(c):
    r=v2(c+2)-1
    if r<3:
        return {'kind':'outside', 'r':r}
    b=(c+2)//2**(r+1)
    good=(3**r*b)%4==1
    return {'kind':'merge' if good else 'hard', 'r':r, 'b':b,
            'next':(3**r*b-1)//4 if good else (3**(r-1)*b-1)//4,
            'high':'0000'+'1'*(r-3)+('01' if good else '00'),
            'low':'0'+'1'*r+('00' if good else '01')}

def scan(c, budget):
    initial=c
    seq=[]
    for _ in range(budget):
        tr=transition(c)
        if tr['kind']=='outside':
            return [initial,'outside',seq,c]
        seq.append([tr['r'],tr['kind']])
        c=tr['next']
        if tr['kind']=='merge':
            return [initial,'merge',seq,c]
    return [initial,'budget',seq,c]

def cylinder(labels):
    if not labels or any(type(r) is not int or r<3 for r in labels):
        raise ValueError('nonempty labels >=3 required')
    c,M=0,1
    for i in reversed(range(len(labels))):
        r=labels[i]
        good=i==len(labels)-1
        b0=pow(3,r if good else r+1,4)
        d=2**(r+3)
        c0=2**(r+1)*b0-2
        if good:
            c,M=c0,d
        else:
            D0=(3**(r-1)*b0-1)//4
            t=(c-D0)*pow(3**(r-1),-1,M)%M
            c,M=c0+d*t,d*M
    return c,M

def source(k,h,labels,t):
    c2,M2=cylinder(labels)
    p=9**k
    eps=1 if k%2 else -1
    a0=(1+eps*p)*pow(2**(h+4),-1,3*p)%(3*p)
    M3=3**h*3*p
    c3=(3**h*a0-1)*pow(4,-1,M3)%M3
    c0=c2+M2*((c3-c2)*pow(M2,-1,M3)%M3)
    c=c0+M2*M3*t
    a=(4*c+1)//3**h
    u=(2**(h+4)*a-1)//p
    n=8**k*u-5
    return n,n//3-2,c,u,a

def family_case(k,h,labels,t):
    n,x,c,u,a=source(k,h,labels,t)
    entry=c
    F='110'*k+'0100'+'1'*h+'01'
    B='1'+'110'*(k-1)+'1110000'+'1'*(h-1)+'00'
    flip=False
    growing=0
    for i,r in enumerate(labels):
        tr=transition(c)
        if tr['r']!=r or tr['kind']!=('merge' if i==len(labels)-1 else 'hard'):
            raise ValueError('compiled cylinder mismatch')
        F+=tr['low'] if flip else tr['high']
        B+=tr['high'] if flip else tr['low']
        if tr['kind']=='hard':
            growing+=int(tr['next']>c)
            flip=not flip
        c=tr['next']
    p,q=replay(n,F),replay(x,B)
    if p[-1]!=q[-1] or len(F)!=len(B) or not (x>0 and 3*x<n):
        raise ValueError('invalid lower-source meeting')
    if k>=threshold(len(labels)) and min(p[1:])<=n:
        raise ValueError('uniform no-descent bound failed')
    return {'k':k,'h':h,'labels':list(labels),'t':t,'n':n,'x':x,'entry':entry,
            'u':u,'a':a,'word_n':F,'word_x':B,'clock':len(F),
            'endpoint':c,'min_forward':min(p[1:]),'growing_returns':growing}

def specifications():
    patterns=[(r,) for r in range(3,11)]
    patterns += [(r,s) for r in (3,8,9) for s in (3,4,7)]
    patterns += [(9,5,3),(3,4,5,8,3),(8,)*12+(4,), (3,9,4,8)*4+(3,)]
    cases=[(k,h,rs,t) for rs in patterns for k in (1,2,8,40,82)
           for h in (1,2,7) for t in (0,1)]
    cases += [(49,1,(3,),0),(82,1,(9,5,3),0),
              (threshold(13),3,(8,)*12+(4,),0),
              (threshold(17),2,(3,9,4,8)*4+(3,),0),
              (250,80,(3,7,8,9,4),1)]
    return patterns,cases

def first_one(n):
    path=[n]
    for _ in range(1000):
        if n==1:
            return path
        n=step(n);path.append(n)
    raise ValueError('control did not terminate within budget')

def ambient():
    rows=[]
    for k in range(1,7):
        for u in range(1,4096,2):
            n=8**k*u-5
            s=v2(9**k*u+1)
            if s<5:
                rows.append([k,u,n,'entry_guard',None]);continue
            h=s-4;a=(9**k*u+1)//2**s
            if 3**(h+1)*a%4==1:
                rows.append([k,u,n,'parent_good_exit',None]);continue
            c=(3**h*a-1)//4
            out=scan(c,8)
            rows.append([k,u,n,'new_'+out[1],out])
    return rows

def tally(rows,index):
    out={}
    for row in rows:
        out[row[index]]=out.get(row[index],0)+1
    return out

def build():
    patterns,specs=specifications()
    families=[family_case(*spec) for spec in specs]
    grid=[scan(c,8) for c in range(1,65537)]
    amb=ambient()
    cyl=[[list(rs),*cylinder(rs)] for rs in patterns]
    controls={str(n):first_one(n) for n in (3003,999,128,14)}
    summary={'schema':SCHEMA, 'family_count':len(families),
             'family_sha256':digest(families),
             'no_descent_bound_cases':sum(f['k']>=threshold(len(f['labels'])) for f in families),
             'growing_return_cases':sum(f['growing_returns']>0 for f in families),
             'grid_count':len(grid),'grid_counts':tally(grid,1),'grid_sha256':digest(grid),
             'ambient_count':len(amb),'ambient_counts':tally(amb,3),'ambient_sha256':digest(amb),
             'cylinders':cyl,'controls':controls,
             'thresholds':[[j,threshold(j)] for j in (1,2,3,8,13,17)],
             'examples':[families[specs.index(spec)] for spec in
                         [(1,1,(3,),0),(1,1,(9,5,3),0),(82,1,(9,5,3),0)]]}
    return summary,{'families':families,'grid':grid,'ambient':amb}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--check',type=Path)
    ap.add_argument('--output',type=Path)
    ap.add_argument('--full',type=Path)
    args=ap.parse_args()
    summary,full=build()
    envelope={'payload':summary,'sha256':digest(summary)}
    if args.check and enc(json.loads(args.check.read_text()))!=enc(envelope):
        raise SystemExit('canonical mismatch')
    if args.output:
        args.output.write_text(json.dumps(envelope,indent=2,sort_keys=True)+'\n')
    if args.full:
        args.full.write_text(json.dumps(full,separators=(',',':'),sort_keys=True)+'\n')
    print(json.dumps({'status':'PASS','sha256':envelope['sha256'],
                      'families':summary['family_count'],'grid':summary['grid_counts'],
                      'ambient':summary['ambient_counts']},sort_keys=True))

if __name__=='__main__':
    main()
