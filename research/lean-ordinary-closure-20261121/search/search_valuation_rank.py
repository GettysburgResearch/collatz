#!/usr/bin/env python3
"""Explore the genuine Nat rank mu(n)=n*2^v2(n), for the psi comparison.

A whole-cell lower bound on root valuation and an exact upper valuation
on query sources certify the inequality. Proportional forms are handled
exactly even when their valuations are unbounded on the cell.
"""
from search_affine_types import search
from collections import Counter
import argparse,json,time

def v2(n):
    assert n>0
    return (n&-n).bit_length()-1

def rank_guard(power=1,base=2):
    assert power>0 and base>0
    def lower(a,b,M,r,q,p):
        assert q==p=='psi'
        if b<=0:return False
        if base==1:return a<=M and b<r
        if a*r==b*M:
            d=v2(a)-v2(M)
            return a**power*base**d<M**power if d>=0 else a**power<M**power*base**(-d)
        va,vb=v2(a),v2(b)
        if va<=vb:return False
        rootlower=min(v2(M),v2(r))
        wq=base**vb;wp=base**rootlower
        # Every binomial coefficient of query_rank(t) is at most its root
        # counterpart, and the constant term is strictly smaller.  This is
        # an exact sufficient polynomial inequality for EVERY t>=0.
        if wq*b**power>=wp*r**power:return False
        return all(wq*a**j*b**(power-j)<=wp*M**j*r**(power-j) for j in range(1,power+1))
    return lower

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--modulus',type=int,default=1440)
    ap.add_argument('--power',type=int,default=1);ap.add_argument('--base',type=int,default=2)
    ap.add_argument('--height',type=int,default=100);ap.add_argument('--cap',type=int,default=100000)
    ap.add_argument('--factors',default='2,2,3,2')
    ap.add_argument('--output',required=True)
    args=ap.parse_args();start=time.monotonic();solved=[];levels=[]
    frontier=[(args.modulus,r if r>1 else args.modulus+1) for r in range(1,args.modulus+1)]
    for level,factor in enumerate([1]+[int(x) for x in args.factors.split(',') if x]):
        cells=[(M*factor,r+j*M) for M,r in frontier for j in range(factor)]
        frontier=[]
        for M,r in cells:
            row=search(M,r,'psi',{'psi':1},lower=rank_guard(args.power,args.base),height=args.height,cap=args.cap)
            if row.get('unresolved',False):frontier.append((M,r))
            else:row['level']=level;solved.append(row)
        result={'level':level,'factor':factor,'tested':len(cells),'new_solved':len(cells)-len(frontier),
                'remaining':len(frontier),'remaining_density':sum(1/M for M,r in frontier),
                'remaining_root_v2_lower':dict(Counter(min(v2(M),v2(r)) for M,r in frontier)),
                'seconds':time.monotonic()-start}
        print(json.dumps(result),flush=True);levels.append(result)
        with open(args.output,'w') as f:json.dump({'status':'SEARCH ONLY; NO FULL PROOF' if frontier else 'COVER FOUND; REQUIRES INDEPENDENT CHECK',
            'rank':{'formula':'n^power*base^v2(n)','power':args.power,'base':args.base},'initial_modulus':args.modulus,'levels':levels,'solved':solved,'unresolved':frontier},f,indent=2)
        if not frontier:break

if __name__=='__main__':main()
