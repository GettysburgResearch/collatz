#!/usr/bin/env python3
"""Exact affine-shadow synthesis. Proposed mathematics; not a Collatz solver.

No external packages. Every generated word is checked on its full progression.
The compiler refines a parameter progression; it does not change a fixed input
and pretend that the input now satisfies the new guard.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


def need(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def integer(x: Any, name: str, minimum: int | None = None) -> int:
    need(type(x) is int, name + ' must be an integer (not bool/float)')
    need(minimum is None or x >= minimum, name + ' is out of range')
    return x


def v2(x: int) -> int:
    integer(x, 'valuation input', 1)
    return (x & -x).bit_length()-1


def core(x: int) -> int:
    integer(x, 'slope', 1)
    for p in (2, 3):
        while x % p == 0:
            x //= p
    return x


def T(x: int) -> int:
    return (3*x+1)//2 if x & 1 else x//2


def word_data(word: str) -> tuple[int, int, int]:
    q = a = 0
    for j, bit in enumerate(word):
        need(bit in '01', 'bad parity bit')
        if bit == '1':
            q += 1
            a = 3*a+(1 << j)
    return len(word), q, a


def residue(word: str) -> int:
    length, odds, correction = word_data(word)
    modulus = 1 << length
    return (-correction*pow(3**odds, -1, modulus)) % modulus


def gap_words(gap: int) -> tuple[str, str]:
    """Credited fixed-gap compiler: upper word, lower word; iterative."""
    integer(gap, 'gap', 1)
    f: list[str] = []
    g: list[str] = []
    while gap > 1:
        if gap % 2 == 0:
            f.append('0'); g.append('0'); gap //= 2
        elif gap % 4 == 1:
            f.append('01'); g.append('10'); gap = (3*gap+1)//4
        else:
            f.append('10'); g.append('01'); gap = (3*gap-1)//4
    return ''.join(f)+'100', ''.join(g)+'001'


def compile_type(d: int, b: int) -> dict[str, Any]:
    """All d>=0, b in Z; X=3**d*y+b. No signed-orbit stopping premise."""
    integer(d, 'exponent', 0); integer(b, 'intercept')
    original_d, original_b = d, b
    f: list[str] = []; g: list[str] = []; moves: list[str] = []
    complexity = abs(b)+3**d
    bits = complexity.bit_length()
    bound = d*(bits+2)+6*bits+3
    while d:
        if b == 0:
            # Both sources odd: introduce a nonzero intercept, without d change.
            f.append('1'); g.append('1'); moves.append('kick')
            b = (1-3**d)//2
        elif b % 2 == 0:
            f.append('0'); g.append('0'); moves.append('halve')
            b //= 2
        else:
            f.append('0'); g.append('1'); moves.append('lower_exponent')
            d -= 1
            b = (b-3**d)//2
        need(len(f) <= bound, 'type compiler exceeded proved bound')
    if b:
        upper, lower = gap_words(abs(b))
        f.append(upper if b > 0 else lower)
        g.append(lower if b > 0 else upper)
    fw, gw = ''.join(f), ''.join(g)
    length = len(fw)
    need(length == len(gw) and length <= bound, 'clock/bound mismatch')
    r, modulus = residue(gw), 1 << length
    a = 3**original_d
    lower_limit = max(1, -((original_b-1)//a))
    base = r + modulus*max(0, (lower_limit-r+modulus-1)//modulus)
    qf, af = word_data(fw)[1:]; qg, ag = word_data(gw)[1:]
    need(qg == qf+original_d and 3**qf*original_b+af == ag,
         'affine endpoint identity failed')
    need((a*r+original_b-residue(fw)) % modulus == 0,
         'incompatible physical cylinders')
    return dict(d=original_d, b=original_b, status='gate', residue=r,
                modulus=modulus, base=base, words=[fw, gw], bound=bound,
                moves=moves, final_gap=b)


def apply_word(form: list[int], word: str) -> list[int]:
    """Whole integer progression: no sampling of branch legality."""
    a, b = form
    for bit in word:
        need(a % 2 == 0 and b % 2 == int(bit), 'nonuniform parity')
        if bit == '1':
            a, b = 3*a, 3*b+1
        a //= 2; b //= 2
    return [a, b]


def compile_family(forms: list[list[int]], ap: list[int] | None = None) -> dict[str, Any]:
    """Uniform merger inside ANY input progression t=a (mod M).

    Output words apply simultaneously to A_i*t+B_i at t=base+modulus*j.
    An incompatible slope core is a no-uniform-word result, not nonconvergence.
    """
    need(type(forms) is list and len(forms) >= 2, 'need at least two affines')
    for row in forms:
        need(type(row) is list and len(row) == 2, 'bad affine form')
        integer(row[0], 'slope', 1); integer(row[1], 'intercept')
    ap = [0, 1] if ap is None else ap
    need(type(ap) is list and len(ap) == 2, 'bad progression')
    a0, m0 = integer(ap[0], 'residue', 0), integer(ap[1], 'modulus', 1)
    need(a0 < m0, 'residue must be canonical')
    cores = [core(a) for a, _ in forms]
    if len(set(cores)) != 1:
        return dict(forms=forms, ap=ap, status='incompatible_slopes', cores=cores)
    current = [[a*m0, a*a0+b] for a, b in forms]
    words = ['' for _ in forms]
    parameter_base, parameter_modulus = a0, m0

    def advance(indices: list[int], word: str) -> None:
        for index in indices:
            current[index] = apply_word(current[index], word)
            words[index] += word

    def normalize(indices: list[int]) -> None:
        while current[indices[0]][0] % 2 == 0:
            bit = str(current[indices[0]][1] % 2)
            advance(indices, bit)

    for i in range(1, len(forms)):
        cohort = list(range(i))
        normalize(cohort); normalize([i])
        upper, lower = (0, i) if current[0][0] >= current[i][0] else (i, 0)
        quotient, remainder = divmod(current[upper][0], current[lower][0])
        need(remainder == 0, 'nonintegral normalized slope ratio')
        d = 0
        while quotient > 1 and quotient % 3 == 0:
            quotient //= 3; d += 1
        need(quotient == 1, 'normalized slopes are not a power of three')
        b = current[upper][1]-3**d*current[lower][1]
        gate = compile_type(d, b)
        modulus = gate['modulus']
        a, c = current[lower]
        shift = ((gate['residue']-c)*pow(a, -1, modulus)) % modulus
        parameter_base += parameter_modulus*shift
        parameter_modulus *= modulus
        current = [[a*modulus, a*shift+b] for a, b in current]
        fw, gw = gate['words']
        advance([i] if upper == i else cohort, fw)
        advance(cohort if upper == i else [i], gw)
        need(all(current[j] == current[0] for j in range(i+1)), 'cohort mismatch')
    threshold = max([0]+[-((b-1)//a) for a, b in forms])
    base = parameter_base+parameter_modulus*max(
        0, (threshold-parameter_base+parameter_modulus-1)//parameter_modulus)
    endpoints = [apply_word([a*parameter_modulus, a*base+b], w)
                 for (a, b), w in zip(forms, words)]
    need(all(e == endpoints[0] for e in endpoints), 'final affine mismatch')
    need(endpoints[0][0] > 0 and endpoints[0][1] > 0, 'nonpositive output')
    return dict(forms=forms, ap=ap, status='gate', cores=cores, base=base,
                modulus=parameter_modulus, words=words, endpoint=endpoints[0])


def first_entry(n: int) -> dict[str, Any]:
    integer(n, 'source', 2)
    if n % 2 == 0:
        return dict(n=n, m=n//2, words=['0',''], outcome='merge', states=[n//2,n//2])
    r = v2(n+1); u = (n+1) >> r; m = (n-1)//2
    b = 3**(r-1)*u-1
    if b % 4 == 2:
        return dict(n=n, m=m, words=['1'*r+'00','1'*(r-1)+'01'],
                    outcome='merge', states=[(3*b+2)//4]*2)
    c = b//4
    return dict(n=n, m=m, words=['1'*r+'01','1'*(r-1)+'00'],
                outcome='H', states=[9*c+2,c])


def hard_trace(c: int, budget: int = 64) -> dict[str, Any]:
    integer(c, 'H parameter', 1); integer(budget, 'budget', 0)
    start = c; clock = 0; rows = []
    for _ in range(budget):
        r = v2(c+2)-1
        if r < 3:
            return dict(start=start, outcome='escape', rows=rows, c=c, clock=clock)
        b = (c+2) >> (r+1)
        if (3**r*b) % 4 == 1:
            rows.append([c,r,'merge',(3**r*b-1)//4])
            return dict(start=start, outcome='merge', rows=rows,
                        clock=clock+r+3)
        target = (3**(r-1)*b-1)//4
        rows.append([c,r,'hard',target]); c=target; clock+=r+3
    return dict(start=start, outcome='budget', rows=rows, c=c, clock=clock)


def valuation_trace(c: int, budget: int = 64) -> dict[str, Any]:
    """Credited #125 two-bridge return language; original orientation retained."""
    integer(c, 'C', 1); integer(budget, 'budget', 0)
    start=c; clock=0; rows=[]
    for _ in range(budget):
        va=v2(3*c-2); vb=v2(3*c-1)
        if va>=3 and va%2==1:
            label='A'; k=(va-3)//2; b=(3*c-2)//2**va
            d=(3**(k+1)*b+1)//2
            f='00'+'01'*k+'00'; g='01'+'10'*k+'11'
        elif vb>=4 and vb%2==0:
            label='B'; k=(vb-4)//2; b=(3*c-1)//2**vb
            d=(3**(k+2)*b+1)//2
            f='100'+'01'*k+'00'; g='110'+'10'*k+'11'
        else:
            return dict(start=start,outcome='escape',rows=rows,c=c,clock=clock)
        s=v2(d+1); zz=3**s*((d+1)//2**s)
        if zz%4==3:
            out=(3*zz-1)//4; kind='merge'
            f+='1'*s+'01'; g+='1'*s+'00'
        else:
            out=(zz-1)//4; kind='hard'
            f+='1'*s+'00'; g+='1'*s+'01'
        need(c>=14 and len(f)==len(g) and len(f)>=6,'support/clock guard')
        rows.append(dict(c=c,label=label,k=k,s=s,out=out,kind=kind,words=[f,g]))
        clock+=len(f)
        if kind=='merge': return dict(start=start,outcome='merge',rows=rows,clock=clock)
        c=out
    return dict(start=start,outcome='budget',rows=rows,c=c,clock=clock)


def hitting_time(n: int, budget: int = 4096) -> int | None:
    for i in range(budget+1):
        if n == 1: return i
        n = T(n)
    return None


def records() -> list[dict[str, Any]]:
    rows = []
    for d in range(13):
        for b in range(-64,65):
            rows.append(dict(kind='type', value=compile_type(d,b)))
    for d in [1,2,7,17,33,64]:
        for b in [0, 2**128, -(2**128), 3**d, 1-3**d, 3**(d+5)+2]:
            rows.append(dict(kind='type', value=compile_type(d,b)))
    # Exhaustive small slopes: include no-uniform conclusions, never call them divergence.
    for a in range(1,19):
        for c in range(1,19):
            for offset in [-3, 0, 7]:
                ap = [(a+c) % 12, 12]
                rows.append(dict(kind='family', value=compile_family([[a,offset],[c,1-offset]],ap)))
    examples = [([[1,0],[9,2]],[0,1]), ([[1,0],[9,2]],[1,2]),
                ([[8,-5],[4,-1],[3,-5]],[0,1]),
                ([[8,-5],[4,-1],[3,-5]],[7,24]),
                ([[5,1],[1,1]],[0,1]),
                ([[5,1],[30,-19],[90,7],[180,0]],[17,40]),
                ([[1,1],[1,2],[1,3],[1,4]],[0,1]),
                ([[3**18,7],[2**22,-17],[2**8*3**9,29]],[123,1009]),
                ([[2**40,-2**120],[3**30,2**90+7]],[137,512])]
    for forms, ap in examples:
        rows.append(dict(kind='example', value=compile_family(forms,ap)))
    for q in range(1,33):
        forms=[[2**(q%6), -q], [3**(q%7),q+1],
               [2**(q%4)*3**(q%5),1-q*q]]
        rows.append(dict(kind='family', value=compile_family(forms,[q%(2*q+1),2*q+1])))
    for n in range(2,4097):
        entry=first_entry(n)
        if entry['outcome']=='H':
            trace=hard_trace(entry['states'][1])
            sigma=hitting_time(entry['m'])
            need(sigma is not None, 'finite test companion did not reach core')
            initial=len(entry['words'][1])
            hard=sum(item[2]=='hard' for item in trace['rows'])
            bound=(max(0,sigma-initial)+5)//6
            need(hard<=bound, 'companion-clock bound failed')
            vl=valuation_trace(entry['states'][1])
            vl_hard=sum(row['kind']=='hard' for row in vl['rows'])
            need(vl_hard<=bound,'extended companion-clock bound failed')
            entry.update(trace=trace, valuation_trace=vl, companion_sigma=sigma, hard_bound=bound)
        rows.append(dict(kind='entry', value=entry))
    # Infinite-claim adversaries: these are finite, exactly replayed phase controls.
    for n,m in [(2,1),(7,3),(3003,999),(11,17)]:
        rows.append(dict(kind='core_control', value=dict(n=n,m=m,
                      sigma_n=hitting_time(n),sigma_m=hitting_time(m))))
    return rows


def canonical(data: Any) -> bytes:
    return json.dumps(data, sort_keys=True, separators=(',',':'), ensure_ascii=True).encode()


def summary(rows: list[dict[str,Any]]) -> dict[str,Any]:
    counts={}
    for row in rows:
        key=row['kind']+':'+row['value'].get('status',row['value'].get('outcome','control'))
        counts[key]=counts.get(key,0)+1
    types=[r['value'] for r in rows if r['kind']=='type']
    return dict(schema='ACS-1', counts=counts, rows=len(rows),
                rows_sha256=hashlib.sha256(canonical(rows)).hexdigest(),
                max_type_length=max(len(r['words'][0]) for r in types),
                scope='finite reconstruction only; no all-input convergence claim')


def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--full', '--output', dest='output', type=Path)
    parser.add_argument('--check',type=Path)
    parser.add_argument('--family', help='JSON list [[A,B],...]')
    parser.add_argument('--ap', help='JSON [residue,modulus]', default='[0,1]')
    args=parser.parse_args()
    if args.family is not None:
        print(json.dumps(compile_family(json.loads(args.family),json.loads(args.ap)),sort_keys=True))
        return
    rows=records(); result=dict(summary=summary(rows),rows=rows)
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n',encoding='utf-8')
    if args.check:
        expected=json.loads(args.check.read_text(encoding='utf-8'))
        need(canonical(result['summary'])==canonical(expected),'canonical summary differs')
    print(json.dumps(result['summary'],sort_keys=True))

if __name__=='__main__':
    main()
