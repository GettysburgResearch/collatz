#!/usr/bin/env python3
"""Finite K-decreasing proof language with physical two-arm certificates."""
from __future__ import annotations
from dataclasses import dataclass
from functools import lru_cache
import argparse
import json
from pathlib import Path


def require(ok: bool, reason: object) -> None:
    if not ok:
        raise RuntimeError(str(reason))


def valuation(n: int) -> int:
    require(n > 0, ('valuation domain',n))
    return (n & -n).bit_length()-1


def rank(n: int) -> int:
    require(n>0 and n&1, ('rank domain',n))
    return n.bit_count()*(n.bit_count()-1)//2+valuation(n+1)


def odd_step(n: int) -> tuple[int,int]:
    require(n>1 and n&1, ('odd domain',n))
    a=valuation(3*n+1)
    return (3*n+1)>>a,a


def credit(n: int) -> int:
    d=1<<(n.bit_count()-1)
    left,right,b=d,n+1-d,0
    while left<right:
        left*=4;right*=3;b+=1
    return b


@dataclass(frozen=True)
class Edge:
    target: int
    kind: str
    left: int
    right: int
    odd_cost: int


@lru_cache(maxsize=None)
def forward(n: int) -> tuple[Edge,...]:
    if n==1:
        return ()
    result=[]
    m,clock=n,0
    for j in range(1,credit(n)+2):
        q,a=odd_step(m)
        clock+=a
        if rank(q)<rank(m):
            result.append(Edge(q,'first-good',clock,0,j))
            break
        m=q
    else:
        raise RuntimeError(('first-good theorem failed',n))
    r=valuation(n+1)
    core=(n+1)>>r
    for j in range(1,r):
        core*=3
        q=(core<<(r-j))-1
        if rank(q)<rank(n):
            result.append(Edge(q,'forced-run',j,0,j))
    return tuple(dict.fromkeys(result))


def transverse(n: int) -> tuple[Edge,...]:
    if n<=1 or n%8!=5:
        return ()
    m=(n-1)//4
    # U(1)=1 is an arithmetic identity, but the physical orbit is killed at 1.
    if m==1:
        return (Edge(1,'unwrap-terminal',3,0,1),)
    a=valuation(3*m+1)
    return (Edge(m,'unwrap',a+2,a,2),)



def braids(n: int) -> tuple[Edge,...]:
    """True two-arm joins, not assumed to be proper ancestors."""
    if n<=1:
        return ()
    result=[]
    base_clock=valuation(3*n+1)
    y=n
    for q in range(1,4):
        y=4*y+1
        for a in range(1,5):
            numerator=(y<<a)-1
            if numerator%3:
                continue
            m=numerator//3
            require(m>1 and m&1,('braid source',n,q,a,m))
            result.append(Edge(m,f'braid-{q}-{a}',base_clock,a+base_clock+2*q,3))
    return tuple(result)

def ancestors(n: int) -> tuple[Edge,...]:
    if n<=1:
        return ()
    result=[]
    # A finite test menu. The ancestor-normalization theorem is not limited to it.
    for a in range(1,13):
        numerator=(n<<a)-1
        if numerator%3:
            continue
        m=numerator//3
        if m>1 and m&1:
            result.append(Edge(m,'ancestor',0,a,1))
    return tuple(result)


class Search:
    def __init__(self, mode: str, budgeted: bool):
        require(mode in ('forward','ancestors','transverse','braid','both'),mode)
        self.mode,self.budgeted=mode,budgeted
        self.status={1:True}
        self.chosen={}
        self.expanded=0

    def edges(self,n: int) -> tuple[Edge,...]:
        pool=list(forward(n))
        if self.mode in ('transverse','braid','both'):
            pool.extend(transverse(n))
        if self.mode in ('braid','both'):
            pool.extend(braids(n))
        if self.mode in ('ancestors','both'):
            pool.extend(ancestors(n))
        return tuple(e for e in pool if rank(n)-rank(e.target)>=(e.odd_cost if self.budgeted else 1))

    def solve(self,n: int) -> bool:
        if n in self.status:
            return self.status[n]
        stack=[[n,self.edges(n),0]]
        self.expanded+=1
        while stack:
            source,edges,i=stack[-1]
            if i==len(edges):
                self.status[source]=False
                stack.pop()
                continue
            edge=edges[i]
            if edge.target not in self.status:
                require(rank(edge.target)<rank(source),'rank cycle')
                stack.append([edge.target,self.edges(edge.target),0])
                self.expanded+=1
            elif self.status[edge.target]:
                self.status[source]=True
                self.chosen[source]=edge
                stack.pop()
            else:
                stack[-1][2]+=1
        return self.status[n]

    def certificate(self,n: int) -> list[tuple[int,Edge]]:
        require(self.solve(n),('no certificate',n))
        result=[]
        while n!=1:
            edge=self.chosen[n]
            result.append((n,edge))
            n=edge.target
        return result


def trace(n: int,k: int) -> tuple[int,int]:
    odd=0
    for _ in range(k):
        require(n>1,('postterminal clock',n,k))
        if n&1:
            n=(3*n+1)//2;odd+=1
        else:
            n//=2
    return n,odd


def check_certificate(n: int, search: Search) -> dict:
    original=n
    signed_clock=0
    odd_work=0
    kinds=[]
    for source,edge in search.certificate(n):
        left,lc=trace(source,edge.left)
        right,rc=trace(edge.target,edge.right)
        require(left==right,('physical join',source,edge))
        require(lc+rc==edge.odd_cost,('odd cost',source,edge))
        require(rank(source)-rank(edge.target)>=(edge.odd_cost if search.budgeted else 1),('admission',source,edge))
        signed_clock+=edge.left-edge.right
        odd_work+=edge.odd_cost
        kinds.append(edge.kind)
    require(signed_clock>=0 and trace(original,signed_clock)[0]==1,('composed clock',original,signed_clock))
    if search.budgeted:
        require(odd_work<=rank(original)-1,('budget',original,odd_work))
    return {'source':original,'shortcut_stopping_time':signed_clock,'odd_arm_work':odd_work,'kinds':kinds}


def separating_families() -> dict:
    checked=0
    examples=[]
    max_bits=0
    for h in range(3,33):
        a=(4**h-1)//3
        for r in (h+1,h+7,10000+h):
            m=(a<<r)-1
            for q in sorted({1,h-2}):
                n=4**q*m+(4**q-1)//3
                end=(3**h*a<<(r-h))-1
                require(not [e for e in forward(n) if rank(e.target)<rank(n)],('old language unexpectedly advances',h,r,q))
                require(rank(m)<rank(n) and rank(end)==rank(m)-h,('family rank',h,r,q))
                require(trace(n,h+2*q)[0]==end and trace(m,h)[0]==end,('family clocks',h,r,q))
                require(rank(n)-rank(m)>=2 and rank(n)-rank(end)>=h+2,('family budget',h,r,q))
                max_bits=max(max_bits,n.bit_length())
                checked+=1
                if h<=4 and r==h+1 and q==1:
                    examples.append({'h':h,'r':r,'q':q,'source':n,'witness':m,'endpoint':end,
                                     'source_rank':rank(n),'witness_rank':rank(m),'endpoint_rank':rank(end),
                                     'source_shortcut_clock':h+2*q,'witness_shortcut_clock':h})
    return {'checked':checked,'maximum_source_bitlength':max_bits,'examples':examples}


def run(count: int) -> dict:
    result={'status':'PROPOSED proof language; EMPIRICAL finite census; Collatz unresolved',
            'seed_domain':f'odd positive n <= {2*count-1}', 'families':separating_families(), 'census':{}}
    for budgeted in (False,True):
        searches={mode:Search(mode,budgeted) for mode in ('forward','ancestors','transverse','braid','both')}
        success={mode:set() for mode in searches}
        for n in range(1,2*count,2):
            for mode,search in searches.items():
                if search.solve(n):
                    success[mode].add(n)
        require(success['ancestors']==success['forward'],'ancestor normalization census')
        new=sorted(success['braid']-success['forward'])
        require(success['forward']<=success['transverse'],'extension lost source')
        certs=[check_certificate(n,searches['braid']) for n in new[:12]]
        verified=0
        for mode,search in searches.items():
            for n in success[mode]:
                check_certificate(n,search)
                verified+=1
        result['census']['budgeted' if budgeted else 'strict']={
            'proved':{mode:len(s) for mode,s in success.items()},
            'new_braid_successes':new,'new_unwrap_successes':sorted(success['transverse']-success['forward']),'example_certificates':certs,
            'successful_certificates_replayed':verified,
            'expanded_nodes':{mode:s.expanded for mode,s in searches.items()},
            'first_unresolved':{mode:[n for n in range(1,2*count,2) if n not in s][:20] for mode,s in success.items()}}
    return result


def main() -> None:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--count',type=int,default=4096)
    p.add_argument('--output',type=Path)
    a=p.parse_args()
    require(a.count>=1,'count must be positive')
    text=json.dumps(run(a.count),sort_keys=True,indent=2)+'\n'
    if a.output:a.output.write_text(text,encoding='utf-8')
    else:print(text,end='')

if __name__=='__main__':main()
