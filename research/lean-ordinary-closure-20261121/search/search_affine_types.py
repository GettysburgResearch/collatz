#!/usr/bin/env python3
"""Joint strict induction for globally quantified affine comparisons.

Kinds map u to a pair A*u+B, C*u+D.  Query application solves either arm
for a positive integer affine u, then replaces it by the other arm.  Every
query has strictly smaller weight(kind)*u for all affine parameters t>=0.
Unlike homogeneous-only search this tests EVERY positive residue, because
the psi kind has no even-source normalization.
"""
from collections import deque,Counter
from math import gcd
import argparse,json,time

TYPES={'3':(1,0,3,0),'5':(1,0,5,0),'psi':(1,0,2,-1)}

def search(M,r,p,weights,cap=100000,height=100,types=TYPES,rank_modulus=1,lower=None):
    root=weights[p][r%rank_modulus] if isinstance(weights[p],list) else weights[p]
    assert M%rank_modulus==0
    bounds=(height*M,height*r)
    A,B,C,D=types[p]
    starts=((A*M,A*r+B),(C*M,C*r+D))
    reached=[{starts[0]:(None,None)},{starts[1]:(None,None)}]
    if starts[0]==starts[1]:return {'cell':[M,r],'kind':p,'left':[],'right':[],'endpoint':list(starts[0]),'nodes':2}
    queues=[deque([starts[0]]),deque([starts[1]])]
    def smaller(q,a,b):
        if lower is not None:return b>0 and lower(a,b,M,r,q,p)
        if isinstance(weights[q],list):
            g=gcd(a,rank_modulus)
            w=max(weights[q][j] for j in range(b%g,rank_modulus,g))
        else:w=weights[q]
        return b>0 and w*a<=root*M and w*b<root*r
    def neighbors(z):
        a,b=z
        yield 'D',(2*a,2*b)
        if a%2==0:
            if b%2==0:yield 'E',(a//2,b//2)
            else:yield 'O',(3*a//2,(3*b+1)//2)
        if a%3==0 and (2*b-1)%3==0 and 2*b-1>0:
            yield 'I',(2*a//3,(2*b-1)//3)
        for q in weights:
            A,B,C,D=types[q]
            if a%A==0 and (b-B)%A==0 and smaller(q,a//A,(b-B)//A):
                yield '+'+q,(C*(a//A),C*((b-B)//A)+D)
            if a%C==0 and (b-D)%C==0 and smaller(q,a//C,(b-D)//C):
                yield '-'+q,(A*(a//C),A*((b-D)//C)+B)
    def path(side,z):
        out=[]
        while reached[side][z][0] is not None:
            prev,move=reached[side][z]
            out.append(move);z=prev
        return out[::-1]
    while queues[0] and queues[1] and sum(map(len,reached))<cap:
        side=0 if len(queues[0])<=len(queues[1]) else 1
        z=queues[side].popleft()
        for move,new in neighbors(z):
            if min(new)<=0 or new[0]>bounds[0] or new[1]>bounds[1]:continue
            if new not in reached[side]:
                reached[side][new]=(z,move);queues[side].append(new)
                if new in reached[1-side]:
                    return {'cell':[M,r],'kind':p,'left':path(0,new),'right':path(1,new),'endpoint':list(new),'nodes':sum(map(len,reached))}
    return {'cell':[M,r],'kind':p,'unresolved':True,'nodes':sum(map(len,reached))}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--modulus',type=int,default=1440)
    ap.add_argument('--weights',default='3:8,5:5,psi:5')
    ap.add_argument('--rank-modulus',type=int,default=1)
    ap.add_argument('--cap',type=int,default=100000);ap.add_argument('--height',type=int,default=100)
    ap.add_argument('--factors',default='')
    ap.add_argument('--output',required=True)
    args=ap.parse_args();start=time.monotonic();solved=[];levels=[]
    weights={q:([int(v) for v in w.split('/')] if '/' in w else int(w)) for q,w in (x.split(':') for x in args.weights.split(','))}
    assert all(all(v>0 for v in w) if isinstance(w,list) else w>0 for w in weights.values())
    assert all(len(w)==args.rank_modulus if isinstance(w,list) else True for w in weights.values())
    frontier=[(args.modulus,r if r>1 else args.modulus+1,p) for p in weights for r in range(1,args.modulus+1)]
    for level,factor in enumerate([1]+[int(x) for x in args.factors.split(',') if x]):
        cells=[(M*factor,r+j*M,p) for M,r,p in frontier for j in range(factor)]
        frontier=[];counts=Counter()
        for M,r,p in cells:
            row=search(M,r,p,weights,args.cap,args.height,rank_modulus=args.rank_modulus)
            if row.get('unresolved',False):frontier.append((M,r,p))
            else:row['level']=level;solved.append(row);counts[p]+=1
        result={'level':level,'factor':factor,'tested':len(cells),'new_solved':sum(counts.values()),
                'solved_by_kind':dict(counts),'remaining':len(frontier),
                'remaining_by_kind':dict(Counter(p for M,r,p in frontier)),
                'remaining_density':{p:sum(1/M for M,r,q in frontier if p==q) for p in weights},
                'seconds':time.monotonic()-start}
        print(json.dumps(result),flush=True);levels.append(result)
        with open(args.output,'w') as f:json.dump({'status':'SEARCH ONLY; NO FULL PROOF' if frontier else 'COVER FOUND; REQUIRES INDEPENDENT CHECK',
            'types':TYPES,'weights':weights,'rank_modulus':args.rank_modulus,'initial_modulus':args.modulus,'levels':levels,'solved':solved,'unresolved':frontier},f,indent=2)
        if not frontier:break

if __name__=='__main__':main()
