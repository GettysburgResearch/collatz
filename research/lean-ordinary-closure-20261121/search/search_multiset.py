#!/usr/bin/env python3
"""Exact affine comparison descent with a finite set of multipliers.

All weights are positive integers, and every query satisfies strict rank
descent for every nonnegative affine parameter.  Searches may be incomplete.
"""
from collections import deque,Counter
import argparse,json,time

def search(M,r,p,weights,cap=100000,height=100):
    root=weights[p]; bounds=(height*M,height*r)
    starts=((M,r),(p*M,p*r))
    reached=[{starts[0]:(None,None)},{starts[1]:(None,None)}]
    queues=[deque([starts[0]]),deque([starts[1]])]
    def smaller(q,a,b):return weights[q]*a<=root*M and weights[q]*b<root*r
    def neighbors(z):
        a,b=z
        yield 'D',(2*a,2*b)
        if a%2==0:
            if b%2==0:yield 'E',(a//2,b//2)
            else:yield 'O',(3*a//2,(3*b+1)//2)
        if a%3==0 and (2*b-1)%3==0 and 2*b-1>0:
            yield 'I',(2*a//3,(2*b-1)//3)
        for q in weights:
            if smaller(q,a,b):yield 'M'+str(q),(q*a,q*b)
            if a%q==0 and b%q==0 and smaller(q,a//q,b//q):
                yield 'V'+str(q),(a//q,b//q)
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
                    return {'cell':[M,r],'multiplier':p,'left':path(0,new),'right':path(1,new),'endpoint':list(new),'nodes':sum(map(len,reached))}
    return {'cell':[M,r],'multiplier':p,'unresolved':True,'nodes':sum(map(len,reached))}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--modulus',type=int,default=10080)
    ap.add_argument('--weights',default='3:8,5:5,7:5')
    ap.add_argument('--cap',type=int,default=100000);ap.add_argument('--height',type=int,default=100)
    ap.add_argument('--factors',default='')
    ap.add_argument('--output',required=True)
    args=ap.parse_args();start=time.monotonic();solved=[];levels=[]
    weights={int(q):int(w) for q,w in (x.split(':') for x in args.weights.split(','))}
    assert all(q>0 and w>0 for q,w in weights.items())
    frontier=[(args.modulus,r if r>1 else args.modulus+1,p) for p in weights for r in range(1,args.modulus,2)]
    for level,factor in enumerate([1]+[int(x) for x in args.factors.split(',') if x]):
        cells=[(M*factor,r+j*M,p) for M,r,p in frontier for j in range(factor)]
        frontier=[];counts=Counter()
        for M,r,p in cells:
            row=search(M,r,p,weights,args.cap,args.height)
            if row.get('unresolved',False):frontier.append((M,r,p))
            else:row['level']=level;solved.append(row);counts[p]+=1
        result={'level':level,'factor':factor,'tested':len(cells),'new_solved':sum(counts.values()),
                'solved_by_multiplier':dict(counts),'remaining':len(frontier),
                'remaining_by_multiplier':dict(Counter(p for M,r,p in frontier)),
                'remaining_density':{p:sum(2/M for M,r,q in frontier if p==q) for p in weights},
                'seconds':time.monotonic()-start}
        print(json.dumps(result),flush=True);levels.append(result)
        with open(args.output,'w') as f:json.dump({'status':'SEARCH ONLY; NO FULL PROOF' if frontier else 'COVER FOUND; REQUIRES INDEPENDENT CHECK',
            'weights':weights,'initial_modulus':args.modulus,'levels':levels,'solved':solved,'unresolved':frontier},f,indent=2)
        if not frontier:break

if __name__=='__main__':main()
