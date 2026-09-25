#!/usr/bin/env python3
"""Standalone literal verification. Imports no generator or project module.

The universal all-source conclusion also uses the written product-loss/net
proof; this checker verifies its complete finite arithmetic input.
"""
from fractions import Fraction
import copy
import json
from pathlib import Path
import sys


def require(ok, message):
    if not ok:
        raise ValueError(message)


def integer(x, minimum=0):
    require(type(x) is int and x >= minimum,'integer/type constraint')


def frac(pair):
    require(type(pair) is list and len(pair)==2,'fraction shape')
    integer(pair[0]); integer(pair[1],1)
    return Fraction(*pair)


def advance(x, clock):
    integer(x,1); integer(clock)
    for _ in range(clock):
        if x & 1:
            x = (3*x+1)//2
        else:
            x //= 2
    return x


def gap(numbers):
    points = sorted({Fraction(n,2**(n.bit_length()-1)) for n in numbers})
    require(len(points)>0,'empty net')
    return max([points[i+1]/points[i] for i in range(len(points)-1)]+[2*points[0]/points[-1]])


def verify(payload):
    require(type(payload) is dict,'object')
    require(len(payload['universal_net_bounds'])==2,'universal inventory')
    require(len(payload['source_nets'])==6,'source inventory')
    for u, expected in zip(payload['universal_net_bounds'],[(Fraction(11,10),11,14),(Fraction(101,100),146,32)]):
        ratio,Q,M = frac(u['ratio']),u['Q'],u['M']
        require((ratio,Q,M)==expected,'exact universal experiment')
        G = gap([3**j for j in range(Q+1)])
        c = Fraction(5,8)*Fraction(4,5)**M
        require(frac(u['ideal_gap'])==G,'ideal gap')
        require(frac(u['product_loss_bound'])==c,'product loss')
        require(frac(u['perturbed_gap_bound'])==G/(1-c),'perturbed gap')
        require(G/(1-c)<ratio,'gap target')
        require(u['threshold_multiplier']==5*2**(4*(M+Q)),'universal threshold')
    edges=windows=0
    for row, source in zip(payload['source_nets'],[1,27,121,303,1311,2**127-1]):
        require(row['source']==source,'source inventory')
        nodes, clocks = row['nodes'],row['clocks']
        require(len(nodes)==513 and len(clocks)==512,'ladder inventory')
        for n in nodes:
            integer(n,2); require(n%3!=0,'ternary unit')
        require(nodes[0]<=5*source,'original-height bound')
        direction=row['seed_link']['direction']; clock=row['seed_link']['clock']
        if direction=='source_to_seed':
            require(advance(source,clock)==nodes[0],'source anchor')
        elif direction=='seed_to_source':
            require(advance(nodes[0],clock)==source,'reverse source anchor')
        else:
            raise ValueError('anchor direction')
        for i,k in enumerate(clocks):
            integer(k,2); require(k<=5,'inverse clock')
            y,z=nodes[i],nodes[i+1]
            require(4*z>=5*y and 3*z<=32*y,'growth')
            x=z
            for j in range(k):
                require(x%2==(1 if j==0 else 0),'physical word')
                x=(3*x+1)//2 if x&1 else x//2
            require(x==y,'inverse endpoint')
            edges+=1
        actual=gap(nodes)
        require(frac(row['max_circular_ratio'])==actual,'reported gap')
        require(frac(row['window_ratio'])==Fraction(101,100) and actual<Fraction(101,100),'1-percent net')
        require(row['threshold']==max(nodes),'threshold')
        require(len(row['windows'])==16,'window inventory')
        for hit in row['windows']:
            index,t,z,x=(hit[k] for k in ['index','doublings','root','left'])
            integer(index); require(index<len(nodes),'index')
            integer(t);integer(z,1);integer(x,1)
            require(x>=max(nodes),'height precondition')
            require(z==nodes[index]*2**t and x<=z and 100*z<=101*x,'window geometry')
            require(advance(z,t+sum(clocks[:index]))==nodes[0],'complete original-linked arm')
            windows+=1
    return {'literal_inverse_edges':edges,'literal_window_checks':windows,'universal_bounds':2,'source_nets':6}


def main():
    path=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).with_name('net_certificates.json')
    payload=json.loads(path.read_text())
    out=verify(payload)
    mutations=[]
    bad=copy.deepcopy(payload);bad['source_nets'][0]['nodes'][25]+=2;mutations.append(bad)
    bad=copy.deepcopy(payload);bad['source_nets'][1]['clocks'][10]+=1;mutations.append(bad)
    bad=copy.deepcopy(payload);bad['source_nets'][2]['windows'][0]['root']+=1;mutations.append(bad)
    bad=copy.deepcopy(payload);bad['universal_net_bounds'][1]['threshold_multiplier']-=1;mutations.append(bad)
    bad=copy.deepcopy(payload);bad['universal_net_bounds'][0]['ideal_gap']=[1,1];mutations.append(bad)
    bad=copy.deepcopy(payload);bad['source_nets'][0]['nodes'][0]=True;mutations.append(bad)
    rejected=0
    for bad in mutations:
        try:verify(bad)
        except ValueError:rejected+=1
    require(rejected==6,'mutation rejection')
    out['rejected_semantic_mutations']=rejected
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=='__main__':main()
