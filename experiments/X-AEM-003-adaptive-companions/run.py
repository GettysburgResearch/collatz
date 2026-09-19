#!/usr/bin/env python3
"""AAC exact certificate generator. Finite budgets; no convergence oracle."""
import argparse
import hashlib
import json
from pathlib import Path

SCHEMA = 'collatz-aac-003-v1'

def enc(x):
    return json.dumps(x, sort_keys=True, separators=(',', ':'), ensure_ascii=True).encode()

def digest(x):
    return hashlib.sha256(enc(x)).hexdigest()

def val(n):
    if type(n) is not int or n <= 0:
        raise ValueError('positive exact integer required')
    return (n & -n).bit_length()-1

def step(n):
    return (3*n+1)//2 if n%2 else n//2

def replay(n, w):
    if type(n) is not int or n < 1 or type(w) is not str:
        raise ValueError('invalid path input')
    out=[n]
    for bit in w:
        if bit not in '01' or int(bit) != n%2:
            raise ValueError('nonphysical word')
        n=step(n); out.append(n)
    return out

def adjacent(q):
    """Return merge or (9D+2,D), never silently choose a future."""
    if q%2==0:
        e=val(q)
        if e==2:
            return 'merge',(3*(q//4)+1)//2,'100','001','even_v2_2'
        if e>=3:
            return 'hard',q//8,'101','000','even_v2_ge3'
        b=q//2; s=val(b+1); d=(b+1)//2**s
        B=3**s*d-1; good=B%4==2
        return ('merge' if good else 'hard', (3*B+2)//4 if good else B//4,
                '1'*(s+1)+('00' if good else '01'),
                '0'+'1'*s+('01' if good else '00'), 'even_run_'+str(s))
    if q%8==5:
        b=(q-1)//4; s=val(b+1); d=(b+1)//2**s
        good=3**(s+1)*d%4==1
        return ('merge' if good else 'hard',
                (3**(s+1)*d-1)//4 if good else (3**s*d-1)//4,
                '0'+'1'*(s+1)+('00' if good else '01'),
                '100'+'1'*(s-1)+('01' if good else '00'), 'odd5_run_'+str(s))
    raise ValueError('outside adjacent language')

def seed(v):
    """Three companion types; v=1 mod16 stays explicitly outside."""
    if type(v) is not int or v<1 or v%2==0:
        raise ValueError('positive odd seed required')
    if v%16==1:
        return None
    if v%4==3 or v%16==9:
        a=6; q=(9*v-7)//2; F='1100'; B='10'
        kind,c,f,b,label=adjacent(q)
    elif v%16==5:
        a=3; q=(9*v-13)//8; F='110000'; B='010'
        kind,c,f,b,label=adjacent(q)
    else:
        a=1; z=(v-5)//8; F='110000'; B='000'
        good=z%4==3
        kind='merge' if good else 'hard'
        c=(9*z+5)//4 if good else (3*z+1)//4
        f='00' if good else '01'; b='11' if good else '10'; label='one_eighth'
    return a,kind,c,F+f,B+b,label

def hard(c):
    r=val(c+2)-1
    if r<3:
        return None
    b=(c+2)//2**(r+1); good=3**r*b%4==1
    return ('merge' if good else 'hard',
            (3**r*b-1)//4 if good else (3**(r-1)*b-1)//4,
            '0000'+'1'*(r-3)+('01' if good else '00'),
            '0'+'1'*r+('00' if good else '01'), r)

def certificate(k,u,budget=8):
    if any(type(x) is not int for x in (k,u,budget)) or k<1 or u<1 or u%2==0 or budget<0:
        raise ValueError('invalid input')
    n=8**k*u-5; v=9**(k-1)*u; entry=seed(v)
    if entry is None:
        return {'k':k,'u':u,'n':n,'status':'outside_seed'}
    a,kind,c,F,B,label=entry
    m=a*8**(k-1)*u-5
    F='110'*(k-1)+F; B='110'*(k-1)+B
    seq=[]; flip=False
    if kind=='hard':
        kind='budget'
        for _ in range(budget):
            h=hard(c)
            if h is None:
                kind='outside_return'; break
            kind,c,f,b,r=h
            F+=b if flip else f; B+=f if flip else b
            seq.append([r,kind])
            if kind=='merge':
                break
            flip=not flip
            kind='budget'
    p,q=replay(n,F),replay(m,B)
    if not 0<m<n:
        raise ValueError('lost immutable root order')
    if kind=='merge' and not p[-1]==q[-1]==c:
        raise ValueError('invalid meeting')
    if kind!='merge':
        target=(c,9*c+2) if flip else (9*c+2,c)
        if (p[-1],q[-1]) != target:
            raise ValueError('invalid retained pair')
    return {'k':k,'u':u,'n':n,'m':m,'a':a,'status':kind,'seed_label':label,
            'sequence':seq,'word_n':F,'word_m':B,'clock_n':len(F),'clock_m':len(B),
            'end_n':p[-1],'end_m':q[-1],'min_forward':min(p[1:]),
            'new_direct':v%16==7}

def from_source(n,budget=8):
    if type(n) is not int or n<2:
        raise ValueError('source must be an exact integer >=2')
    r=val(n+5)
    if r<3 or r%3:
        return {'n':n,'status':'outside_burst'}
    return certificate(r//3,(n+5)//2**r,budget)

def cylinder(rs):
    c,M=0,1
    for i in range(len(rs)-1,-1,-1):
        r=rs[i]; good=i==len(rs)-1; b0=pow(3,r if good else r+1,4)
        d=2**(r+3); c0=2**(r+1)*b0-2
        if good:
            c,M=c0,d
        else:
            t=(c-(3**(r-1)*b0-1)//4)*pow(3**(r-1),-1,M)%M
            c,M=c0+d*t,d*M
    return c,M

def residue(kind,p):
    if kind=='direct':
        return 7,16
    if kind=='old_entry':
        return 7,32
    if kind=='new_h0':
        return 23,32
    if kind=='even_run':
        s=p; M=2**(s+4); d0=pow(3,s+1,4)
        return (3+2**(s+2)*d0)*pow(9,-1,M)%M,M
    if kind=='odd_run':
        s=p; M=2**(s+5); d0=pow(3,s+1,4)
        return (1+2**(s+3)*d0)*pow(9,-1,M)%M,M
    if kind=='three_eighth':
        s=p; M=2**(s+6); d0=pow(3,s+1,4)
        return (-3+2**(s+4)*d0)*pow(9,-1,M)%M,M
    if kind=='one_eighth':
        return 29,32
    if kind=='returns':
        c,M=cylinder(p)
        return (16*c+7)*pow(9,-1,16*M)%(16*M),16*M
    raise ValueError('unknown family')

def source(k,c,M,t):
    u0=c*pow(9**(k-1),-1,M)%M
    epsilon=1 if k%2 else 2
    u0+=M*((epsilon-u0)*pow(M,-1,3)%3)
    return u0+3*M*t

def specifications():
    cases=[]
    for kind in ('direct','old_entry','new_h0','one_eighth'):
        cases += [(kind,0,k,t) for k in range(1,33) for t in (0,1)]
    for kind in ('even_run','odd_run','three_eighth'):
        cases += [(kind,s,k,t) for s in range(1,33) for k in (1,2,15,40) for t in (0,1)]
    patterns=[(r,) for r in range(3,11)]+[(9,5,3),(8,)*12+(4,), (3,9,4,8)*4+(3,)]
    cases += [('returns',rs,k,t) for rs in patterns for k in (1,2,15,82) for t in (0,1)]
    cases += [('even_run',128,250,0),('odd_run',128,250,0),('returns',(8,)*20+(4,),250,0)]
    return cases

def counts(rows):
    c={}
    for row in rows:
        key=row['status']; c[key]=c.get(key,0)+1
    return c

def build():
    families=[]
    for kind,p,k,t in specifications():
        c,M=residue(kind,p);u=source(k,c,M,t)
        row=certificate(k,u,64)
        if row['status']!='merge' or row['n']%12!=3:
            raise ValueError('family failed')
        if row['new_direct'] and k>=15 and row['min_forward']<=row['n']:
            raise ValueError('uniform bound failed')
        families.append({'spec':[kind,p,k,t],'c':c,'modulus':M,'result':row})
    # Every input, including all misses, is retained in the deterministic full rows.
    grid=[certificate(k,u,8) for k in range(1,7) for u in range(1,8192,2)]
    fixtures=[certificate(k,u,64) for k,u in ((2,47),(15,7),(23,343),(1,131),(1,879))]
    budget_fixture=certificate(1,source(1,*residue('returns',(8,8,4)),0),1)
    summary={'schema':SCHEMA,'family_count':len(families),'family_sha256':digest(families),
             'grid_count':len(grid),'grid_counts':counts(grid),'grid_sha256':digest(grid),
             'family_types':{s:sum(f['spec'][0]==s for f in families)
                             for s in sorted({f['spec'][0] for f in families})},
             'direct_no_descent':sum(f['result']['new_direct'] and f['result']['k']>=15 for f in families),
             'grid_by_companion':{str(a):counts([r for r in grid if r.get('a')==a]) for a in (1,3,6)},
             'old_entry_in_grid':sum(val(9**r['k']*r['u']+1)>=5 for r in grid),
             'old_entry_all_direct':all(r.get('new_direct') and r['status']=='merge'
                                       for r in grid if val(9**r['k']*r['u']+1)>=5),
             'fixtures':fixtures,'budget_fixture':budget_fixture,
             'threshold':[15,3*9**14<16*8**14,3*9**15>=16*8**15]}
    return summary,{'families':families,'grid':grid}

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--check',type=Path);p.add_argument('--output',type=Path);p.add_argument('--full',type=Path)
    p.add_argument('--source',type=int);p.add_argument('--budget',type=int,default=8)
    a=p.parse_args()
    if a.source is not None:
        print(json.dumps(from_source(a.source,a.budget),sort_keys=True,indent=2));return
    summary,full=build();env={'payload':summary,'sha256':digest(summary)}
    if a.check and enc(json.loads(a.check.read_text()))!=enc(env):
        raise SystemExit('canonical mismatch')
    for target,value in ((a.output,env),(a.full,full)):
        if target:
            target.write_text(json.dumps(value,sort_keys=True,indent=2 if target==a.output else None)+'\n')
    print(json.dumps({'status':'PASS','sha256':env['sha256'],'families':len(full['families']),
                      'grid':summary['grid_counts']},sort_keys=True))

if __name__=='__main__':
    main()
