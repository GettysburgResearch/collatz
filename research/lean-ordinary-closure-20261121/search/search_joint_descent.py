#!/usr/bin/env python3
"""Search whole-cell paired descents under joint multiplier-3/5 induction.

No found finite cover is presumed complete. Every query is strictly below
the root's weighted source for every nonnegative affine parameter.
"""
from collections import deque
from fractions import Fraction
import argparse,json,time

def search(M,r,p,w3,w5,cap,height):
    weights={3:w3,5:w5}
    root=weights[p]
    bounds=(height*M,height*r)
    starts=((M,r),(p*M,p*r))
    reached=[{starts[0]:(None,None)},{starts[1]:(None,None)}]
    queues=[deque([starts[0]]),deque([starts[1]])]
    def smaller(q,a,b):
        # Weighted Nat rank q*a*t+q*b < root*(M*t+r), every t>=0.
        return weights[q]*a <= root*M and weights[q]*b < root*r
    def neighbors(z):
        a,b=z
        yield 'D',(2*a,2*b)
        if a%2==0:
            if b%2==0:yield 'E',(a//2,b//2)
            else:yield 'O',(3*a//2,(3*b+1)//2)
        if a%3==0 and (2*b-1)%3==0 and 2*b-1>0:
            yield 'I',(2*a//3,(2*b-1)//3)
        for q in (3,5):
            if smaller(q,a,b):yield 'M'+str(q),(q*a,q*b)
            if a%q==0 and b%q==0 and smaller(q,a//q,b//q):
                yield 'V'+str(q),(a//q,b//q)
    def path(side,z):
        out=[]
        while reached[side][z][0] is not None:
            prev,move=reached[side][z]
            out.append(move);z=prev
        return out[::-1]
    side=0
    while queues[0] and queues[1] and sum(map(len,reached))<cap:
        side=0 if len(queues[0])<=len(queues[1]) else 1
        z=queues[side].popleft()
        for move,new in neighbors(z):
            if new[0]<=0 or new[1]<=0 or new[0]>bounds[0] or new[1]>bounds[1]:continue
            if new not in reached[side]:
                reached[side][new]=(z,move);queues[side].append(new)
                if new in reached[1-side]:
                    return {'cell':[M,r],'multiplier':p,'left':path(0,new),'right':path(1,new),'endpoint':list(new),'nodes':sum(map(len,reached))}
    return {'cell':[M,r],'multiplier':p,'unresolved':True,'nodes':sum(map(len,reached))}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--modulus',type=int,default=120)
    ap.add_argument('--w3',type=int,default=8);ap.add_argument('--w5',type=int,default=5)
    ap.add_argument('--cap',type=int,default=15000);ap.add_argument('--height',type=int,default=40)
    args=ap.parse_args();rows=[];start=time.monotonic()
    for p in (3,5):
        for r in range(1,args.modulus,2):
            # n=1 is a separately known base. Its positive lifts use r=M+1.
            rr=r+args.modulus if r==1 else r
            rows.append(search(args.modulus,rr,p,args.w3,args.w5,args.cap,args.height))
    print(json.dumps({'status':'SEARCH ONLY; unresolved rows are not proofs',
        'weights':[args.w3,args.w5],'modulus':args.modulus,
        'solved':sum(not row.get('unresolved',False) for row in rows),
        'rows':rows,'seconds':time.monotonic()-start},indent=2))
if __name__=='__main__':main()
