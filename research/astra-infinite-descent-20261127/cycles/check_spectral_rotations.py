"""Exact finite Fourier support transfer and native two-marker rotations."""
from collections import Counter
from math import gcd
import json
from check_cycle_rotations import necklaces,rational_labels
from check_independent_clocks import mechanical
from check_spectral import active_orders,cyclotomic


def need(ok,label):
    if not ok:raise ValueError(label)


def check(word,stats,all_rows):
    result=rational_labels(word)
    if result is None:return
    lab,q,_=result
    h=len(word);idx=[i for i,v in enumerate(word) if v];p=len(idx)
    if p<2:return
    g=gcd(p,h);a=h//g;b=p//g
    rel=[i-idx[0] for i in idx]
    d=[i*a//b-rel[i] for i in range(p)]
    if any(len(set(d[k::b]))>2 for k in range(b)):return
    cols=[[1<<(max(d)-v) for v in d[k::b]] for k in range(b)]
    active=active_orders(cols,g);J=sum(len(cyclotomic(k))-1 for k in active)
    e=[(idx[(i+1)%p]-idx[i])%h for i in range(p)]
    if all_rows:
        for lag in range(1,p):
            diff=[e[(i+lag)%p]-e[i] for i in range(p)]
            need(sum(x!=0 for x in diff)*J>=g,'global physical support inequality')
            active_count=0
            for k in range(b):
                row=diff[k::b]
                if not any(row):continue
                active_count+=1
                modes=active_orders([row],g)
                need(set(modes)<=set(active),'native discrepancy DFT support')
                j=sum(len(cyclotomic(n))-1 for n in modes)
                need(j*sum(x!=0 for x in row)>=g,'exact finite uncertainty')
                stats['nonzero_native_discrepancy_rows']+=1
            dcount=sum(x!=0 for x in diff)
            need(dcount*J>=g*active_count,'summed active discrepancy columns')
            if lag%b==0:
                t=lag//b
                Jt=sum(len(cyclotomic(k))-1 for k in active if t%k)
                need(dcount*Jt>=g*active_count,'removed cell-lag frequencies')
                stats['proper_whole_cell_lags']+=1
            stats['all_rotation_checks']+=1
        stats['primitive_binary_column_cycles']+=1
    return q,e,g,J


def main():
    stats=Counter()
    for h in range(4,15):
        for word in necklaces(h):check(word,stats,True)
    examples=[]
    n,b=65,41
    for Q,P in ((5,7),(5,11),(7,11),(5,17)):
        base,markers=mechanical(n,b,[Q,P])
        full=[]
        for j in range(Q*P):
            cell=base.copy()
            for prime,mark in zip((Q,P),markers):
                if j%prime==0:cell[mark:mark+2]=[0,1]
            full.extend(cell)
        q,e,g,J=check(tuple(full),stats,False)
        p=len(e);bits=sum((x-1)<<i for i,x in enumerate(e))
        need(set(e)=={1,2},'native one-two exponents')
        mask=(1<<p)-1
        def hamming(lag):
            return (bits^(((bits>>lag)|(bits<<(p-lag)))&mask)).bit_count()
        need(J==Q+P-1 and g==Q*P,'exact active degree')
        sc=hamming(Q*b);need(sc==4*Q,'exact two-marker display distance')
        smin=min(hamming(lag) for lag in range(1,p))
        need(smin*J>=g,'every fixture lag')
        examples.append(dict(primes=[Q,P],odd_period=p,full_denominator_bits=q.bit_length(),
                             active_degree=J,minimum_mismatches=smin,displayed_mismatches=sc))
    print(json.dumps(dict(counts=stats,two_prime_examples=examples),sort_keys=True,indent=2))


if __name__=='__main__':main()
