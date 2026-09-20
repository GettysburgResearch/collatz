#!/usr/bin/env python3
"""Exact reconstruction of the preceding in-chat anchored-return packet.
No external dependencies. Full outcomes are procedure outcomes, not convergence counts.
"""
import argparse
import hashlib
import json
from pathlib import Path


def need(ok, message):
    if not ok:
        raise ValueError(message)


def val(n):
    need(type(n) is int and n > 0, 'valuation domain')
    return (n & -n).bit_length() - 1


def step(n):
    need(type(n) is int and n > 0, 'positive integer required')
    return (3*n+1)//2 if n & 1 else n//2


def walk(n, length):
    w = ''
    for _ in range(length):
        w += str(n & 1)
        n = step(n)
    return n, w


def finish(D):
    s = val(D+1)
    z = 3**s * ((D+1) >> s)
    if z % 4 == 3:
        return ('MERGE', (3*z-1)//4, s+2)
    need(z > 1 and z % 4 == 1, 'positive H return')
    return ('RETURN', (z-1)//4, s+2)


def prior(C):
    if C % 2 == 0:
        v = val(3*C-2)
        if v < 3 or v % 2 == 0:
            return None
        k = (v-3)//2
        D = (3**(k+1)*((3*C-2) >> v)+1)//2
        pre = 2*k+4
    else:
        v = val(3*C-1)
        if v < 4 or v % 2:
            return None
        k = (v-4)//2
        D = (3**(k+2)*((3*C-1) >> v)+1)//2
        pre = 2*k+5
    status, out, length = finish(D)
    return status, out, pre+length, 'VL'


def bridge_a(C):
    if C % 8 != 7:
        return None
    v = (C+1)//8
    a = val(9*v-1)
    if a % 2 == 0:
        return None
    k = (a-1)//2
    E = (3**(k+1)*((9*v-1) >> a)+1)//2
    if E <= 1:
        return None
    b = val(E-1)
    if b % 2 == 0:
        return None
    ell = (b-1)//2
    F = (3**(ell+1)*((E-1) >> b)+1)//2
    status, out, length = finish(F)
    return status, out, 2*k+2*ell+7+length, 'AR-A'


def bridge_b(C):
    if C % 32 != 31:
        return None
    v = (C+1)//32
    Y = 243*v
    if Y % 4 != 1:
        return None
    q = (Y-5)//4
    length = 7
    if q % 2:
        if q <= 1 or val(q-1) % 2:
            return None
        s = val(q-1)//2
        q = (3**s*((q-1) >> (2*s)))+1
        length += 2*s
    need(q > 0 and q % 2 == 0, 'even adjacent parameter')
    vq = val(q)
    if vq == 2:
        return 'MERGE', (3*(q//4)+1)//2, length+3, 'AR-B'
    if vq >= 3:
        return 'RETURN', q//8, length+3, 'AR-B'
    D = (3*q+2)//4
    status, out, extra = finish(D)
    return status, out, length+2+extra, 'AR-B'


def transition(C, extended=True):
    need(type(C) is int and C > 0, 'C domain')
    for f in ([prior, bridge_a, bridge_b] if extended else [prior]):
        ans = f(C)
        if ans is not None:
            status, out, length, tag = ans
            a, _ = walk(9*C+2, length)
            b, _ = walk(C, length)
            target = (out, out) if status == 'MERGE' else (out, 9*out+2)
            need((a,b) == target, ('transition', C, ans, a, b))
            return ans
    return None


def classify(C, extended=True, budget=1000):
    original = C
    length = 0
    tags = []
    for _ in range(budget):
        tr = transition(C, extended)
        if tr is None:
            return {'C': original, 'status': 'OUTSIDE', 'last': C, 'length': length, 'tags': tags}
        status, out, inc, tag = tr
        length += inc
        tags.append(tag)
        if status == 'MERGE':
            a, wa = walk(9*original+2, length)
            b, wb = walk(original, length)
            need(a == b == out, ('original replay', original, length))
            return {'C': original, 'status': status, 'endpoint': out, 'length': length,
                    'words': [wa, wb], 'tags': tags}
        C = out
    return {'C': original, 'status': 'BUDGET', 'last': C, 'length': length, 'tags': tags}


def cylinder(A, B, M, word):
    """Replay the whole affine progression A*(M*t+B)+2 for H via arguments.
    More generally input is M*t+B; A unused except as a check label.
    Returns exact affine endpoint, rejecting any nonuniform parity.
    """
    for bit in word:
        p = int(bit)
        need(M % 2 == 0 and B % 2 == p, ('nonuniform parity', A, M, B, bit))
        if p:
            M, B = 3*M//2, (3*B+1)//2
        else:
            M, B = M//2, B//2
    return M, B


def tests():
    for D in range(2, 65537):
        if D % 4 == 0:
            E = D//4; out = (3*E-1,E)
        elif D % 4 == 2:
            E = (3*D+2)//4; out = (3*E-4,E)
        elif D % 4 == 3:
            Y = 9*(D+1)//4; out = (Y-5,Y-1)
        else:
            E = (3*D+1)//4; out = (9*E-10,E)
        need((walk(3*D-4,2)[0], walk(D,2)[0]) == out, ('R table',D))
    for M,B,L,W,V,E,F in [(512,439,9,'101000001','111001100',243,209),
                           (1024,735,10,'1011000001','1111100100',729,524)]:
        need(cylinder('H',9*B+2,9*M,W) == (E,F),'upper cylinder')
        need(cylinder('C',B,M,V) == (E,F),'lower cylinder')
        need(len(W) == len(V) == L,'word lengths')
    ladder = 0
    for r in range(2,34):
        for u in range(1,201,2):
            if 3**r*u % 4 != 3:
                continue
            n = 2**r*u-1
            for h in range(1,r//2+1):
                m = (n+1)//4**h-1
                C = (3**(r-2*h+1)*u-1)//4
                Hh = 9**h*C+(9**h-1)//4
                need(0 < 4**h*m < n, 'source bound')
                need(walk(n,r+2)[0] == Hh and walk(m,r-2*h+2)[0] == C, 'ladder')
                ladder += 1
    deep_a = 0
    for k in list(range(11))+[63]:
        for ell in list(range(15))+[64]:
            modulus = 2**(2*ell+3)
            b = ((1+2**(2*ell+2))*pow(3**(k+1),-1,modulus)) % modulus
            target = -pow(2**(2*k+1),-1,9) % 9
            b += modulus*((target-b)*pow(modulus,-1,9) % 9)
            v = (2**(2*k+1)*b+1)//9
            need(bridge_a(8*v-1) is not None, 'deep A guard')
            transition(8*v-1)
            deep_a += 1
    for s in list(range(1,40))+[64]:
        d = (-9*pow(4**(s+1),-1,243)) % 243
        if d % 2 == 0: d += 243
        v = (4**(s+1)*d+9)//243
        need(bridge_b(32*v-1) is not None, 'deep B guard')
        transition(32*v-1)
    lifted = 0
    for modulus,offset,minimum_r,length in [(2048,1757,9,9),(4096,2941,8,10)]:
        for r in range(minimum_r,minimum_r+20):
            u = offset*pow(3**(r-1),-1,modulus) % modulus
            u += modulus*((pow(2**r,-1,3)-u)*pow(modulus,-1,3) % 3)
            n=2**r*u-1; m=(n-3)//4
            C=(3**(r-1)*u-1)//4
            need(n % 3 == 0 and 0 < 4*m < n, 'lifted source')
            need(walk(n,r+2+length)[0] == walk(m,r+length)[0], 'lifted meeting')
            x=n
            for _ in range(r+2+length):
                x=step(x); need(x>n, 'all-states no descent')
            lifted += 1
    need(walk(333567,20)[0] == walk(83391,18)[0] == 507179, 'strict example')
    n=333567; vals=[]
    for _ in range(20):
        n=step(n); vals.append(n)
    need(min(vals) == 338119 and 333567 % 3 == 0,'strict example bound')
    for args in [(236031,18,59007,16,478505),(20530069503,34,1283129343,30,37500596075)]:
        n,L,m,J,y=args
        need(walk(n,L)[0] == walk(m,J)[0] == y, 'ladder example')
    return {'R_rows':65535,'ladder_cases':ladder,'symbolic_cylinders':2,'strict_examples':1,
            'additional_ladder_examples':2,'deep_A':deep_a,'deep_B':40,'lifted_no_descent':lifted}


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--limit',type=int,default=65536)
    p.add_argument('--full',type=Path)
    p.add_argument('--summary',type=Path)
    a=p.parse_args(); need(a.limit > 0,'limit')
    digest=hashlib.sha256(); counts={}; mergers={}
    stream=a.full.open('w',encoding='utf-8') if a.full else None
    try:
        for name,ext in [('baseline',False),('extended',True)]:
            counts[name]={'admitted':0,'MERGE':0,'OUTSIDE':0,'BUDGET':0,'merge_mod3_2':0}
            mergers[name]=set()
            for C in range(1,a.limit+1):
                counts[name]['admitted'] += transition(C,ext) is not None
                row=classify(C,ext); row['mode']=name
                counts[name][row['status']]+=1
                if row['status']=='MERGE':
                    mergers[name].add(C)
                    counts[name]['merge_mod3_2'] += C % 3 == 2
                line=json.dumps(row,sort_keys=True,separators=(',',':'))+'\n'
                digest.update(line.encode())
                if stream: stream.write(line)
    finally:
        if stream: stream.close()
    need(mergers['baseline'] <= mergers['extended'],'lost baseline successes')
    report={'status':'PROPOSED','limit':a.limit,'counts':counts,'added':len(mergers['extended']-mergers['baseline']),
            'rows_sha256':digest.hexdigest(),'tests':tests(),
            'scope':'exact bounded certificate-language replay; not global convergence or independent review'}
    text=json.dumps(report,sort_keys=True,indent=2)+'\n'
    if a.summary: a.summary.write_text(text,encoding='utf-8')
    print(text,end='')

if __name__=='__main__': main()
