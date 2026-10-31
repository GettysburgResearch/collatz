#!/usr/bin/env python3
"""Separate cycle-sweep interval verifier and literal shortcut replay."""
from __future__ import annotations
import argparse, copy, hashlib, json
from pathlib import Path

B=128
UNIT=1<<B
TRACE=1<<60
BANK=1<<96

def check(ok: bool, message: str) -> None:
    if not ok: raise ValueError(message)

def up(n: int,d: int) -> int: return -((-n)//d)

def dumps(x: object) -> bytes:
    return (json.dumps(x,sort_keys=True,separators=(',',':'))+'\n').encode()

def unique(pairs: list) -> dict:
    out={}
    for k,v in pairs:
        if k in out: raise ValueError('duplicate JSON key')
        out[k]=v
    return out

def advance(low: list[int],high: list[int],s: int) -> tuple[list[int],list[int]]:
    # L(n)=4n+1 is one permutation cycle. No truncated-series producer code.
    m=len(low); den=1<<(2*s); c=3**s; order=[]; marked=bytearray(m); n=0
    for _ in range(m):
        check(not marked[n],'non-simple affine residue cycle')
        marked[n]=1; order.append(n); n=(4*n+1)%m
    check(n==0 and all(marked),'incomplete affine residue cycle')
    left=0; right=up(max(high)*den,den-1)
    hl=[0]*m; hh=[0]*m
    sweeps=max(2,up(B+64,2*s*m)+1)
    for _ in range(sweeps):
        for n in reversed(order):
            left=low[n]+left//den; right=high[n]+up(right,den)
            hl[n]=left; hh[n]=right
    a=[0]*(3*m); b=[0]*(3*m)
    for t in range(1,3*m):
        if t%3==0: continue
        v=4 if t%3==1 else 2
        n=((v*t-1)//3)%m; denominator=v**s
        a[t]=c*hl[n]//denominator; b[t]=up(c*hh[n],denominator)
    return a,b

def trace(q: int,square: tuple[list[int],list[int]],fourth: tuple[list[int],list[int]]) -> dict:
    m=3**q; head=128 if q<=3 else 16; h=2*m
    lows=[0,0,0]; highs=[0,0,0]
    for r in range(m):
        # Enumerate the unique odd representative without using the producer branch.
        odd=r+m if (r&1)==0 else r
        wl=sum(UNIT//((odd+h*k)**2) for k in range(head))
        wh=sum(up(UNIT,(odd+h*k)**2) for k in range(head))
        wl+=UNIT//(h*(odd+h*head)); wh+=up(UNIT,h*(odd+h*(head-1)))
        al,ah=square[0][r],square[1][r]
        dl,dh=fourth[0][r],fourth[1][r]
        for i,(l,u) in enumerate(((al,ah),(dl,dh),(al*al,ah*ah))):
            lows[i]+=l*wl; highs[i]+=u*wh
    ans={}
    for i,key in enumerate(('E','D','S')):
        shift=(3 if key=='S' else 2)*B-60
        ans[key]=[lows[i]>>shift,up(highs[i],1<<shift)]
    check(sum(square[0])<=m*UNIT<=sum(square[1]),'independent square mass')
    check(sum(fourth[0])*5**q<=27**q*UNIT<=sum(fourth[1])*5**q,'independent fourth mass')
    return {'q':q,'residues':m,'weight_head_terms':head,**ans}

def replay(limit: int,clock: int) -> dict:
    # Literal shortcut map: one odd T step, followed by individual halvings.
    nums=list(range(1,limit+1,2)); exponents=[0]*len(nums)
    seen=[set() for _ in nums]; live=[True]*len(nums); peaks=nums.copy()
    total_steps=0; rows=[]
    for j in range(clock+1):
        row={'q':j,'active':0,'Elo':0,'Ehi':0,'Dlo':0,'Dhi':0,'c2':0,'prefix_max':max(peaks)}
        for k,n in enumerate(nums):
            if n in seen[k]: live[k]=False
            seen[k].add(n)
            denominator=(2**(4*exponents[k]))*n*n; numerator=3**(4*j)*BANK
            row['Dlo']+=numerator//denominator; row['Dhi']+=up(numerator,denominator)
            if live[k]:
                denominator=(2**(2*exponents[k]))*n*n; numerator=3**(2*j)*BANK
                lo=numerator//denominator
                row['Elo']+=lo; row['Ehi']+=up(numerator,denominator)
                row['c2']+=lo*lo; row['active']+=1
        row['tail_allowance']=[1,2*(limit+1)]; rows.append(row)
        if j<clock:
            for k,n in enumerate(nums):
                n=(3*n+1)//2; exponents[k]+=1; total_steps+=1
                while n%2==0:
                    n//=2; exponents[k]+=1; total_steps+=1
                nums[k]=n; peaks[k]=max(peaks[k],n)
    cumulative=0
    for r in rows:
        e=r['Elo']; Q=r['q']+1; cumulative+=r['Dhi']
        check(4*r['c2']*BANK>=e**3,'envelope interpolation')
        check(Q**3*e**3<=12*cumulative*BANK**2,'elementary coercivity')
        check(Q**59*(19*e**3)**19<=16**40*(236*cumulative)**19*BANK**38,
              'packing coercivity')
    return {'odd_source_limit':limit,'clock':clock,'sources':len(nums),
            'shortcut_steps':total_steps,'rows':rows}

def validate(d: dict,oracle: dict) -> None:
    check(set(d)=={'schema','status','base','density_bits','trace_bits','geometric_terms','traces','bank'},'root schema')
    for key,value in (('schema',1),('density_bits',96),('trace_bits',60),('geometric_terms',32)):
        check(type(d[key]) is int and d[key]==value,'typed constant '+key)
    check(d['base']=='41a408e5e617fb4e65142485f6f3ff3e6ef6c408','source pin')
    check(d['status']=='PROPOSED; no pointwise pressure-decay proof','status')
    check(dumps(d['bank'])==dumps(oracle['bank']),'complete independent bank reconstruction')
    check(len(d['traces'])==len(oracle['traces']),'trace inventory')
    for a,b in zip(d['traces'],oracle['traces']):
        check(set(a)==set(b),'trace schema')
        for key in ('q','residues','weight_head_terms'):
            check(type(a[key]) is int and a[key]==b[key],'trace index')
        for key in ('E','D','S'):
            v=a[key]; w=b[key]
            check(isinstance(v,list) and len(v)==2 and all(type(z) is int for z in v),'interval type')
            check(0<=v[0]<=w[0]<=w[1]<=v[1],'independent interval not enclosed')
            check(w[0]-v[0]<=32 and v[1]-w[1]<=32,'unjustified interval widening')

def main() -> None:
    p=argparse.ArgumentParser(); p.add_argument('evidence',type=Path); p.add_argument('--output',type=Path,required=True)
    a=p.parse_args(); raw=a.evidence.read_bytes(); d=json.loads(raw,object_pairs_hook=unique)
    depth=len(d['traces'])-1; limit=d['bank']['odd_source_limit']; clock=d['bank']['clock']
    check(type(depth) is int and 0<=depth<=12,'depth'); check(type(limit) is int and 0<limit<=65535 and limit%2,'cutoff')
    check(type(clock) is int and 0<=clock<=200,'clock')
    z2=([UNIT],[UNIT]); z4=([UNIT],[UNIT]); rows=[]
    for q in range(depth+1):
        rows.append(trace(q,z2,z4))
        if q<depth: z2=advance(*z2,2); z4=advance(*z4,4)
    oracle={'traces':rows,'bank':replay(limit,clock)}; validate(d,oracle)
    corruptions=[]
    for key in ('E','D','S'):
        bad=copy.deepcopy(d); bad['traces'][-1][key][1]=0; corruptions.append(bad)
    bad=copy.deepcopy(d); bad['traces'][-1]['D'][0]-=100000; corruptions.append(bad)
    bad=copy.deepcopy(d); bad['traces'][-1]['residues']+=3; corruptions.append(bad)
    for key in ('Elo','Dlo','prefix_max','active'):
        bad=copy.deepcopy(d); bad['bank']['rows'][-1][key]+=1; corruptions.append(bad)
    bad=copy.deepcopy(d); bad['bank']['rows'][0]['active']=True; corruptions.append(bad)
    bad=copy.deepcopy(d); bad['bank']['rows'][-1]['tail_allowance'][1]+=2; corruptions.append(bad)
    bad=copy.deepcopy(d); bad['traces'].pop(); corruptions.append(bad)
    for bad in corruptions:
        try: validate(bad,oracle)
        except (ValueError,KeyError,TypeError): pass
        else: raise ValueError('semantic corruption accepted')
    try: json.loads('{"x":1,"x":2}',object_pairs_hook=unique)
    except ValueError: pass
    else: raise ValueError('duplicate JSON accepted')
    out={'ok':True,'evidence_sha256':hashlib.sha256(raw).hexdigest(),
         'method':'128-bit affine-cycle interval sweeps and literal shortcut replay; no producer imports',
         'all_source_trace_depth':depth,'residue_entries_per_power':sum(3**q for q in range(depth+1)),
         'bank_source_clock_entries':((limit+1)//2)*(clock+1),
         'raw_shortcut_steps':oracle['bank']['shortcut_steps'],
         'direct_corruptions_rejected':len(corruptions)+1}
    a.output.write_bytes(dumps(out)); print(json.dumps(out,sort_keys=True))

if __name__=='__main__': main()
