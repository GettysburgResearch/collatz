#!/usr/bin/env python3
"""Check native shortcut blocks, lower carry codes, and delayed pencil ranks."""

from collections import defaultdict
import json
import sys

sys.dont_write_bytecode = True
from check_position_pencil import PRIME, reduce_vector


def branch(n, s):
    bits = []
    for _ in range(s):
        e = n % 2
        bits.append(e)
        n = (3 * n + 1) // 2 if e else n // 2
    return tuple(bits), n


def native_cases(s):
    m = 2 ** s
    visited = set()
    checks = 0
    for a in range(m):
        b, end = branch(a, s)
        h = sum(b)
        if b in visited or not 0 <= end < 3 ** h:
            raise ArithmeticError(('address', s, a))
        visited.add(b)
        for q in (0, 1, 2, 7, 31, 104729):
            found, y = branch(m*q+a, s)
            if found != b or y != 3**h*q+end:
                raise ArithmeticError(('native lift', s, a, q))
            for depth in (0,1,2,5):
                power = 3 ** depth
                for width in (1,3,5):
                    space = 3 ** width
                    literal = ((m*q+a)//power) % (m*space)
                    carry = (m*(q % power)+a)//power
                    encoded = m*((q//power) % space)+carry
                    if literal != encoded or not 0 <= carry < m:
                        raise ArithmeticError(('native carry',s,a,q,depth,width))
                    checks += 1
    return checks


def delayed_columns(s,width,lam):
    m, n = 2**s, 3**(width-1)
    low = 0
    while 3**(low+1) < m: low+=1
    high=low+1
    tags=[sum(branch(a,s)[0]) for a in range(m) if sum(branch(a,s)[0]) in (low,high)]
    window_row=len(tags)*m*n
    space=3*n
    for b,h in enumerate(tags):
        for w in range(m*space):
            d=defaultdict(int)
            d[b*m*n+w%(m*n)]+=1
            d[b*m*n+w//3]-=lam
            d[window_row+w%space]+=1
            if h<high:d[window_row+h*space+w//m]-=1
            else:d[window_row+(high-1)*space+w//m]-=lam
            yield d
    for i in range(high-1):
        for j in range(space):
            yield {window_row+i*space+j:-lam,window_row+(i+1)*space+j:1}


def delayed_case(s,width):
    m,n=2**s,3**(width-1)
    h=0
    while 3**(h+1)<m:h+=1
    tags=sum(sum(branch(a,s)[0]) in (h,h+1) for a in range(m))
    rows=tags*m*n+(h+1)*3*n
    ranks=[]
    for lam in (0,1,2,PRIME-1):
        pivots={}
        for column in delayed_columns(s,width,lam):
            v=reduce_vector(column,pivots)
            if v:pivots[min(v)]=v
        ranks.append(len(pivots))
    if ranks[1:] != [rows-n-tags,rows-n,rows-n]:
        raise ArithmeticError((s,width,rows,n,tags,ranks))
    return {'steps':s,'window':width,'tags':tags,'rows':rows,
            'ranks_mod_101_at_0_1_2_minus1':ranks}


def main():
    checks=sum(native_cases(s) for s in range(1,11))
    cases=[delayed_case(s,w) for s,w in ((1,3),(2,2),(2,3),(3,2),(3,3),(4,1),(4,2))]
    print(json.dumps({'native_quotient_arc_checks':checks,'delayed_pencils':cases},
                     indent=2,sort_keys=True))


if __name__ == '__main__':
    main()
