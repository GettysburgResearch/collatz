#!/usr/bin/env python3
"""Standalone exact checker: literal paths, integer phase order, Fenwick ranks.
Imports neither run.py nor a graph/max-flow library. No floating-point verdicts.
"""
from __future__ import annotations
import argparse
import copy
from fractions import Fraction
from functools import cmp_to_key
import hashlib
import json
from pathlib import Path


def require(condition, message):
    if not condition:
        raise ValueError(message)


def integer(x, low=0, high=100000):
    require(type(x) is int and low <= x <= high, 'integer domain')
    return x


def unhex(s):
    require(type(s) is str and 1 <= len(s) <= 100000 and
            all(c in '0123456789abcdef' for c in s), 'hex domain')
    n = int(s,16)
    require(format(n,'x') == s, 'noncanonical hex')
    return n


def physical(n,p):
    require(n > 0, 'nonpositive state')
    return (p*n+1)//2 if n & 1 else n//2


def distinct_keys(pairs):
    result = {}
    for key,value in pairs:
        require(key not in result, 'duplicate JSON key')
        result[key] = value
    return result


def decode_ladder(data, source, p, depth):
    require(set(data) == {'source','forward','seed_path','clocks'}, 'ladder schema')
    require(unhex(data['source']) == source, 'wrong immutable source')
    forward,seed = [[unhex(s) for s in data[k]] for k in ('forward','seed_path')]
    require(forward and seed and forward[0] == source and forward[-1] == seed[-1], 'anchor paths')
    expected = [source]
    if source % p == 0:
        while expected[-1] % 2 == 0:
            expected.append(physical(expected[-1],p))
        expected.append(physical(expected[-1],p))
    require(forward == expected, 'forward anchor recipe')
    y = forward[-1]
    expected_seed = ([5,8,4,2,1] if p == 3 else [3,8,4,2,1]) if y == 1 else [y]
    require(seed == expected_seed, 'seed anchor recipe')
    peak = max(forward+seed)
    steps = 0
    for path in (forward,seed):
        for a,b in zip(path,path[1:]):
            require(physical(a,p) == b, 'illegal original path')
            steps += 1
    y = seed[0]
    require(y >= 2 and y % p != 0, 'nonunit seed')
    nodes = [source,y]
    require(type(data['clocks']) is list and len(data['clocks']) == depth, 'clock inventory')
    for clock in data['clocks']:
        k = integer(clock,2 if p == 3 else 3,5 if p == 3 else 10)
        for j in range(2 if p == 3 else 3,k):
            u = y*2**j-1
            require(u % p != 0 or (u//p) % p == 0, 'noncanonical inverse choice')
        numerator = y*2**k-1
        require(numerator % p == 0, 'inverse integrality')
        z = numerator//p
        require(z > 0 and z & 1 and z % p != 0 and 4*z >= 5*y, 'inverse domain')
        n = z
        for _ in range(k):
            peak = max(peak,n)
            n = physical(n,p)
            steps += 1
        require(n == y, 'inverse physical endpoint')
        peak = max(peak,n)
        y = z
        nodes.append(y)
    return nodes,peak,steps


class Ranks:
    def __init__(self,n):
        self.tree = [0]*(n+1)
    def insert(self,i):
        i += 1
        while i < len(self.tree):
            self.tree[i] += 1
            i += i & -i
    def before(self,i):
        total = 0
        while i:
            total += self.tree[i]
            i -= i & -i
        return total
    def select(self,rank):
        # Return zero-based position of the rank-th active entry, rank starts at 1.
        pos = 0
        bit = 1 << (len(self.tree).bit_length()-1)
        while bit:
            nxt = pos+bit
            if nxt < len(self.tree) and self.tree[nxt] < rank:
                rank -= self.tree[nxt]
                pos = nxt
            bit >>= 1
        return pos


def order(a,b):
    x = a << (b.bit_length()-1)
    y = b << (a.bit_length()-1)
    return (x > y)-(x < y)


def ray_profile(nodes0,nodes1,k):
    # One canonical odd numerator determines a dyadic phase uniquely.
    rays = {}
    for color,nodes in enumerate((nodes0,nodes1)):
        for n in nodes:
            odd = n//(n & -n)
            h = n.bit_length()-1
            if odd in rays:
                require(rays[odd][1] == color, 'opposite-ray collision')
                rays[odd] = min(h,rays[odd][0]),color
            else:
                rays[odd] = h,color
    ordered = sorted(rays,key=cmp_to_key(order))
    positions = {n:i for i,n in enumerate(ordered)}
    colors = [rays[n][1] for n in ordered]
    ranks = Ranks(len(ordered))
    count = 0
    births = {}
    for odd,(h,color) in sorted(rays.items(),key=lambda item:(item[1][0],positions[item[0]])):
        require(h <= k, 'ray outside shell cutoff')
        i = positions[odd]
        delta = 0
        if count:
            before = ranks.before(i)
            left = ranks.select(before if before else count)
            right = ranks.select(before+1 if before < count else 1)
            delta = int(colors[left] != color)+int(color != colors[right])-int(colors[left] != colors[right])
        require(delta in (0,2), 'circle birth parity')
        if delta:
            births[h] = births.get(h,0)+delta//2
        ranks.insert(i)
        count += 1
    return births


def check(row):
    require(type(row) is dict and row.get('schema') == 'two-ladder-capacity-v1', 'schema')
    p = integer(row['multiplier'],3,5)
    require(p in (3,5), 'multiplier')
    source = unhex(row['source'])
    require(source > 0, 'source domain')
    depth = integer(row['depth'],0,16384)
    require(type(row['ladders']) is list and len(row['ladders']) == 2, 'ladder count')
    n0,p0,s0 = decode_ladder(row['ladders'][0],1,p,depth)
    n1,p1,s1 = decode_ladder(row['ladders'][1],source,p,depth)
    common = {'schema','multiplier','source','depth','ladders','status'}
    if row['status'] == 'CONVERGENCE':
        require(set(row) == common | {'collision','path'}, 'convergence fields')
        require(len(row['collision']) == 2, 'collision pair')
        a,b = [unhex(s) for s in row['collision']]
        require(a in n0 and b in n1 and a//(a & -a) == b//(b & -b), 'false collision')
        seq = [unhex(s) for s in row['path']]
        require(seq and seq[0] == source and seq[-1] == 1, 'convergence endpoints')
        for a,b in zip(seq,seq[1:]):
            require(physical(a,p) == b, 'convergence physical step')
        return dict(inverse_and_anchor_steps=s0+s1, convergence_steps=len(seq)-1,
                    rational_shells=0, ray_nodes=len(n0)+len(n1))
    require(row['status'] == 'CAPACITY_LOWER_CERTIFICATE', 'unsupported status')
    require(set(row) == common | {'last_shell','ambient_height_exponent','physical_peak',
                                'births','capacity','last_alternations'}, 'capacity fields')
    k = integer(row['last_shell'])
    h = integer(row['ambient_height_exponent'],1)
    peak = max(p0,p1,2 if p == 3 else 8)
    require(unhex(row['physical_peak']) == peak, 'physical peak mismatch')
    require(h == max(k+1,(peak-1).bit_length()), 'ambient height containment')
    births = ray_profile(n0,n1,k)
    require(type(row['births']) is list, 'birth schema')
    supplied = []
    for pair in row['births']:
        require(type(pair) is list and len(pair) == 2, 'birth pair')
        supplied.append([integer(pair[0],0,k),integer(pair[1],1,32772)])
    require(supplied == [[j,births[j]] for j in sorted(births)], 'wrong birth inventory')
    alternations = 0
    energy = Fraction(0)
    for j in range(k+1):
        alternations += 2*births.get(j,0)
        energy += Fraction(alternations,(j+1)**2)
    require(type(row['capacity']) is list and len(row['capacity']) == 2, 'capacity pair')
    numerator,denominator = [unhex(s) for s in row['capacity']]
    require(numerator == energy.numerator and denominator == energy.denominator, 'nonexact capacity')
    require(integer(row['last_alternations']) == alternations, 'last alternations')
    return dict(inverse_and_anchor_steps=s0+s1, convergence_steps=0,
                rational_shells=k+1, ray_nodes=len(n0)+len(n1))


def self_test(rows):
    exemplar = next(r for r in rows if r['status'] == 'CAPACITY_LOWER_CERTIFICATE'
                    and r['depth'] >= 4)
    changes = []
    x=copy.deepcopy(exemplar); x['ladders'][1]['clocks'][0]+=1; changes.append(x)
    x=copy.deepcopy(exemplar); x['ladders'][1]['clocks'][0]=True; changes.append(x)
    x=copy.deepcopy(exemplar); x['ladders'][1]['clocks'].pop(); changes.append(x)
    x=copy.deepcopy(exemplar); x['ladders'][1]['forward'][0]='1'; changes.append(x)
    x=copy.deepcopy(exemplar); x['births'][0][1]+=1; changes.append(x)
    x=copy.deepcopy(exemplar); x['births'].pop(); changes.append(x)
    x=copy.deepcopy(exemplar); x['births'].append(x['births'][0]); changes.append(x)
    x=copy.deepcopy(exemplar); x['capacity'][0]=format(unhex(x['capacity'][0])+1,'x'); changes.append(x)
    x=copy.deepcopy(exemplar); x['ambient_height_exponent']-=1; changes.append(x)
    x=copy.deepcopy(exemplar); x['physical_peak']='1'; changes.append(x)
    x=copy.deepcopy(exemplar); x['last_shell']=0; changes.append(x)
    x=copy.deepcopy(exemplar); x['source']='0'+x['source']; changes.append(x)
    x=copy.deepcopy(exemplar); x['status']='NONCONVERGENCE'; changes.append(x)
    x=copy.deepcopy(exemplar); x['ladders'][1]=copy.deepcopy(x['ladders'][0]); x['source']='1'; changes.append(x)
    for x in changes:
        try:
            check(x)
        except (ValueError,KeyError,IndexError,TypeError):
            pass
        else:
            raise ValueError('semantic mutation accepted')
    try:
        json.loads('{"a":0,"a":1}',object_pairs_hook=distinct_keys)
    except ValueError:
        pass
    else:
        raise ValueError('duplicate JSON key accepted')
    return len(changes)+1


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('path',type=Path)
    parser.add_argument('--self-test',action='store_true')
    parser.add_argument('--corpus',action='store_true')
    args=parser.parse_args()
    rows=json.loads(args.path.read_text(encoding='utf-8'),object_pairs_hook=distinct_keys)
    if args.corpus:
        expected=[(p,n,d) for p,n in ((3,7),(3,27),(3,97),(3,871),(3,2**61-1),(5,13),(5,17))
                  for d in (0,4,16,64,256,1024)]
        expected += [(3,1,0),(3,2,0),(3,5,4),(5,3,4),(5,8,0)]
        require([(r['multiplier'],unhex(r['source']),r['depth']) for r in rows] == expected,
                'experiment inventory does not match')
    counts=[check(row) for row in rows]
    totals={key:sum(c[key] for c in counts) for key in counts[0]}
    totals.update(status='PASS', cases=len(rows),
                  rejected_mutations=self_test(rows) if args.self_test else 0,
                  sha256=hashlib.sha256(args.path.read_bytes()).hexdigest())
    print(json.dumps(totals,sort_keys=True,indent=2))

if __name__ == '__main__':
    main()
