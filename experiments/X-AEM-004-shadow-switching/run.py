#!/usr/bin/env python3
"""Exact source certificates; switching shadows is not a universal selector."""
import argparse
import hashlib
import json
from pathlib import Path

SCHEMA = 'collatz-aes-004-v1'
PARENT = '1d4dfc103055648def3db73860778a383a91ea3c'

def enc(x):
    return json.dumps(x, sort_keys=True, separators=(',', ':'), ensure_ascii=True).encode()

def digest(x):
    return hashlib.sha256(enc(x)).hexdigest()

def pos(n):
    if type(n) is not int or n < 1:
        raise ValueError('positive exact integer required')
    return n

def val(n):
    pos(n)
    return (n & -n).bit_length()-1

def step(n):
    return (3*n+1)//2 if n%2 else n//2

def replay(n, w):
    pos(n)
    if type(w) is not str:
        raise ValueError('word must be text')
    out = [n]
    for bit in w:
        if bit not in '01' or int(bit) != n%2:
            raise ValueError('nonphysical word')
        n = step(n)
        out.append(n)
    return out

def finish(n, m, F, B, kind, c, flip=False, budget=8):
    """Retain immutable sources and each arm's clock through old H returns."""
    if type(budget) is not int or budget < 0 or not 0 < m < n:
        raise ValueError('budget or source order')
    seq = []
    if kind == 'hard':
        kind = 'budget'
        for _ in range(budget):
            r = val(c+2)-1
            if r < 3:
                kind = 'outside_return'
                break
            b = (c+2)//2**(r+1)
            good = 3**r*b%4 == 1
            f = '0000'+'1'*(r-3)+('01' if good else '00')
            z = '0'+'1'*r+('00' if good else '01')
            F += z if flip else f
            B += f if flip else z
            c = (3**r*b-1)//4 if good else (3**(r-1)*b-1)//4
            seq.append([r, 'merge' if good else 'hard'])
            if good:
                kind = 'merge'
                break
            flip = not flip
    p, q = replay(n, F), replay(m, B)
    target = (c, c) if kind == 'merge' else ((c, 9*c+2) if flip else (9*c+2, c))
    if (p[-1], q[-1]) != target:
        raise ValueError('retained pair or meeting mismatch')
    return {'n':n, 'm':m, 'status':kind, 'word_n':F, 'word_m':B,
            'clock_n':len(F), 'clock_m':len(B), 'end_n':p[-1], 'end_m':q[-1],
            'min_forward':min(p[1:]), 'returns':seq}

def adjacent(q):
    """Credited AAC adjacent exits: finite entry, not always a merger."""
    pos(q)
    if q%2 == 0:
        e = val(q)
        if e == 2:
            return 'merge', (3*(q//4)+1)//2, '100', '001'
        if e >= 3:
            return 'hard', q//8, '101', '000'
        b = q//2; s = val(b+1); d = (b+1)//2**s; B = 3**s*d-1
        good = B%4 == 2
        return ('merge' if good else 'hard', (3*B+2)//4 if good else B//4,
                '1'*(s+1)+('00' if good else '01'),
                '0'+'1'*s+('01' if good else '00'))
    if q%8 == 5:
        b = (q-1)//4; s = val(b+1); d = (b+1)//2**s
        good = 3**(s+1)*d%4 == 1
        return ('merge' if good else 'hard', (3**(s+1)*d-1)//4 if good else (3**s*d-1)//4,
                '0'+'1'*(s+1)+('00' if good else '01'),
                '100'+'1'*(s-1)+('01' if good else '00'))
    raise ValueError('outside adjacent domain')

def old_entry(k, u):
    """Standalone restatement of AAC seed selection, unchanged on this domain."""
    v = 9**(k-1)*u; n = 8**k*u-5; pre = '110'*(k-1)
    if v%16 == 1:
        return None
    if v%4 == 3 or v%16 == 9:
        m = (3*n-5)//4; q = (9*v-7)//2; F, B = pre+'1100', pre+'10'
        kind,c,f,b = adjacent(q)
    elif v%16 == 5:
        m = (3*n-25)//8; q = (9*v-13)//8; F, B = pre+'110000', pre+'010'
        kind,c,f,b = adjacent(q)
    else:
        m = (n-35)//8; z = (v-5)//8; F, B = pre+'110000', pre+'000'
        good = z%4 == 3
        kind,c,f,b = ('merge' if good else 'hard', (9*z+5)//4 if good else (3*z+1)//4,
                       '00' if good else '01', '11' if good else '10')
    return m,F+f,B+b,kind,c,False

def old_result(k, u, budget=8):
    n = 8**k*u-5; entry = old_entry(k,u)
    if entry is None:
        return {'n':n,'status':'outside_seed'}
    return finish(n,*entry,budget=budget)

def switched_entry(k, u):
    n = 8**k*u-5; v = 9**(k-1)*u
    if v <= 1 or v%16 != 1:
        raise ValueError('not a nontrivial missing seed')
    t = val(v-1); w = (v-1)//2**t
    if t%2:
        s = (t-1)//2; m = (3*n-5)//4; flip = False
        F = '110'*(k-1)+'1100'+'01'*s
        B = '110'*(k-1)+'10'+'10'*s
        label = 'same_center'
    else:
        s = (t-2)//2; m = 4**k*u-1; flip = True
        F = '110'*k+'00'+'10'*s
        B = '1'*(2*k)+'00'+'01'*s
        label = 'odd_spine'
    q = 3**(s+2)*w+1
    p,z = replay(n,F),replay(m,B)
    expected = (q,q+1) if flip else (q+1,q)
    if q%2 or (p[-1],z[-1]) != expected:
        raise ValueError('even adjacent entry failed')
    kind,c,f,b = adjacent(q)
    F += b if flip else f; B += f if flip else b
    meta = {'entry':label,'t':t,'s':s,'w':w,'adjacent_q':q}
    return (m,F,B,kind,c,flip),meta

def certificate(k, u, budget=8):
    pos(k);pos(u)
    if u%2 == 0 or type(budget) is not int or budget < 0:
        raise ValueError('odd parameter and nonnegative exact budget required')
    n = 8**k*u-5; v = 9**(k-1)*u
    meta = {'k':k,'u':u}
    if v == 1:
        row = finish(n,1,'11000','','merge',1,budget=budget)
        meta['entry'] = 'core3'
    elif v%32 == 13:
        m = 4**k*u-1; c = (3*9**k*u+1)//32
        row = finish(n,m,'110'*k+'00001','1'*(2*k)+'00100','merge',c,budget=budget)
        meta['entry'] = 'gap4_direct'
    elif v%16 == 1:
        entry, details = switched_entry(k,u)
        row = finish(n,*entry,budget=budget); meta.update(details)
    else:
        row = finish(n,*old_entry(k,u),budget=budget)
        meta['entry'] = 'retained_AAC'
    row.update(meta)
    return row

def from_source(n, budget=8):
    pos(n)
    if n < 2:
        raise ValueError('source must be at least two')
    e = val(n+5)
    if e < 3 or e%3:
        return {'n':n,'status':'outside_burst'}
    return certificate(e//3,(n+5)//2**e,budget)

def source(k, residue, modulus, j=0):
    """Solve in u; the independent verifier instead solves in the odd quotient."""
    u = residue*pow(9**(k-1),-1,modulus)%modulus
    epsilon = 1 if k%2 else 2
    u += modulus*((epsilon-u)*pow(modulus,-1,3)%3)
    return u+3*modulus*j

def direct_source(k,t,j=0):
    s = (t-1)//2 if t%2 else (t-2)//2
    d = 3*pow(3**(s+2),-1,8)%8
    return source(k,1+2**t*d,2**(t+3),j)

def cylinder(rs):
    c,M = 0,1
    for i in range(len(rs)-1,-1,-1):
        r = rs[i]
        if type(r) is not int or r < 3:
            raise ValueError('invalid label')
        good = i == len(rs)-1; b0 = pow(3,r if good else r+1,4)
        d = 2**(r+3); c0 = 2**(r+1)*b0-2
        if good:
            c,M = c0,d
        else:
            c,M = c0+d*((c-(3**(r-1)*b0-1)//4)*pow(3**(r-1),-1,M)%M),d*M
    return c,M

def return_source(k,t,rs,j=0):
    s = (t-1)//2 if t%2 else (t-2)//2
    c,M = cylinder(rs)
    # q=8C forces an H return; pull the exact itinerary back to w and then u.
    W = 8*M
    w0 = (8*c-1)*pow(3**(s+2),-1,W)%W
    return source(k,1+2**t*w0,2**t*W,j)

def general_case(c,w,k,u):
    """General negative-period to odd-spine certificate, under an explicit gap guard."""
    if any(type(x) is not int or x < 1 for x in (c,k,u)) or type(w) is not str or not w:
        raise ValueError('invalid general source')
    if c <= 1 or (c-1)&(c-2):
        raise ValueError('c-1 must be a power of two')
    z = -c
    for bit in w:
        if bit not in '01' or z%2 != int(bit):
            raise ValueError('negative word not physical')
        z = step(z)
    if z != -c:
        raise ValueError('not a periodic centre')
    L=len(w);q=w.count('1');d=val(c-1)
    n=2**(L*k)*u-c;m=2**(q*k)*u-1;Y=3**(q*k)*u
    if not 0<m<n or (Y-c)%(2**d) or (Y-c)//2**d%8!=4:
        raise ValueError('gap or immutable source guard')
    E=(3*(Y-c)+2**(d+2))//2**(d+3)
    row=finish(n,m,w*k+'0'*d+'001','1'*(q*k)+'0'*d+'100','merge',E)
    row.update({'centre':c,'period':w,'k':k,'u':u,'gap_exponent':d})
    odds = 0; positive_prefixes = True
    for i, bit in enumerate(w, 1):
        odds += int(bit)
        positive_prefixes &= 3**odds > 2**i
    if positive_prefixes and 3**(q*k) >= 2**(L*k+d+2) and row['min_forward'] <= n:
        raise ValueError('general forward-arm bound')
    if 2**((L-q)*k) > c and 2**((L-q)*k)*m >= n:
        raise ValueError('general source-size bound')
    return row

def general_source(c,w,k,j=0):
    d=val(c-1);L=len(w);q=w.count('1');M=2**(d+3)
    u0=(c+2**(d+2))*pow(3**(q*k),-1,M)%M
    eps=c*pow(2**(L*k),-1,3)%3
    u0+=M*((eps-u0)*pow(M,-1,3)%3)
    return u0+3*M*j

def threshold(t):
    s=(t-1)//2 if t%2 else (t-2)//2;k=1
    while 3**s*9**k < 2**(t+2)*8**k:
        k+=1
    return k

def specs():
    rows=[['direct',k,t,j] for k in (1,2,3,15,26,40) for t in range(4,41) for j in (0,1)]
    patterns=[[r] for r in range(3,11)]+[[9,5,3],[8]*12+[4],[3,9,4,8]*4+[3]]
    rows += [['returns',k,t,rs,j] for k in (1,3,26) for t in (4,5,10,11) for rs in patterns for j in (0,1)]
    rows += [['direct',200,128,0],['direct',200,129,0],['returns',200,128,[8]*20+[4],0]]
    return rows

def family(spec):
    kind,k,t=spec[:3]
    u=direct_source(k,t,spec[3]) if kind=='direct' else return_source(k,t,spec[3],spec[4])
    row=certificate(k,u,64)
    if row['status']!='merge' or row['n']%12!=3 or row.get('t')!=t:
        raise ValueError('new family failed')
    if kind=='direct' and k>=threshold(t) and row['min_forward']<=row['n']:
        raise ValueError('forward-arm lower bound failed')
    if row['entry']=='odd_spine' and k>=3 and 2**k*row['m']>=row['n']:
        raise ValueError('spine size bound failed')
    return {'spec':spec,'result':row}

def counts(rows,key='status'):
    c={}
    for r in rows:
        v=r[key];c[v]=c.get(v,0)+1
    return c

def summarize(families,general,grid,old,fixtures,budget_case):
    compare={}
    for a,b in zip(old,grid):
        key=a['status']+' -> '+b['status'];compare[key]=compare.get(key,0)+1
    return {'schema':SCHEMA,'parent':PARENT,'family_count':len(families),'family_sha256':digest(families),
            'general_count':len(general),'general_sha256':digest(general),
            'grid_count':len(grid),'grid_counts':counts(grid),'grid_sha256':digest(grid),
            'parent_grid_counts':counts(old),'comparison':compare,
            'old_mergers_preserved':all(b['status']=='merge' for a,b in zip(old,grid) if a['status']=='merge'),
            'new_entry_counts':counts(grid,'entry'),
            'direct_no_descent':sum(x['spec'][0]=='direct' and x['result']['min_forward']>x['result']['n'] for x in families),
            'odd_spine_rows':sum(x['result']['entry']=='odd_spine' for x in families),
            'thresholds':[[t,threshold(t)] for t in range(4,17)],
            'fixtures':fixtures,'budget_fixture':budget_case}

def build():
    families=[family(s) for s in specs()]
    general=[general_case(c,w,k,general_source(c,w,k,j))
             for c,w in ((5,'110'),(17,'11110111000')) for k in (*range(1,25),32,64,128) for j in (0,1)]
    grid=[certificate(k,u,8) for k in range(1,7) for u in range(1,8192,2)]
    old=[old_result(k,u,8) for k in range(1,7) for u in range(1,8192,2)]
    fixtures=[certificate(k,u,64) for k,u in ((1,1),(1,13),(1,17),(1,33),(2,47),
              (26,direct_source(26,4)),(23,direct_source(23,5)))]
    budget_case=certificate(3,return_source(3,4,[8,8,4]),1)
    full={'families':families,'general':general,'grid':grid,'parent_grid':old}
    return summarize(families,general,grid,old,fixtures,budget_case),full

def main():
    p=argparse.ArgumentParser();p.add_argument('--check',type=Path);p.add_argument('--output',type=Path)
    p.add_argument('--full',type=Path);p.add_argument('--source',type=int);p.add_argument('--budget',type=int,default=8)
    a=p.parse_args()
    if a.source is not None:
        print(json.dumps(from_source(a.source,a.budget),sort_keys=True,indent=2));return
    payload,full=build();envelope={'payload':payload,'sha256':digest(payload)}
    if a.check and enc(json.loads(a.check.read_text()))!=enc(envelope):
        raise SystemExit('canonical mismatch')
    for target,value in ((a.output,envelope),(a.full,full)):
        if target:
            target.parent.mkdir(parents=True,exist_ok=True)
            target.write_text(json.dumps(value,sort_keys=True,indent=2 if target==a.output else None)+'\n')
    print(json.dumps({'status':'PASS','sha256':envelope['sha256'],'families':len(full['families']),
                      'grid':payload['grid_counts'],'comparison':payload['comparison']},sort_keys=True))
if __name__=='__main__':
    main()
