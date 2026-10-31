#!/usr/bin/env python3
"""Exact all-source trace enclosures and finite-bank regressions; no AI agents."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

BITS=96
SCALE=1<<BITS
OUT_BITS=60
OUT_SCALE=1<<OUT_BITS

def need(c: bool, message: str) -> None:
    if not c: raise ValueError(message)

def ceildiv(n: int, d: int) -> int:
    return (n+d-1)//d

def canonical(x: object) -> bytes:
    return (json.dumps(x,sort_keys=True,separators=(',',':'))+'\n').encode()

def interval(n: int,d: int) -> tuple[int,int]:
    return n*SCALE//d,ceildiv(n*SCALE,d)

def transition(lo: list[int], hi: list[int], power: int) -> tuple[list[int],list[int]]:
    m=len(lo); b=1<<power; rden=b*b; c=3**power; terms=32
    tail=ceildiv(max(hi),(rden-1)*rden**(terms-1))
    hl=[0]*m; hu=[0]*m
    for n in range(m):
        ix=n; den=1; low=0; high=tail
        for _ in range(terms):
            low+=lo[ix]//den; high+=ceildiv(hi[ix],den)
            ix=(4*ix+1)%m; den*=rden
        hl[n]=low; hu[n]=high
    a=[0]*(3*m); z=[0]*(3*m)
    for k in range(m):
        x=(4*k+1)%m; y=(2*k+1)%m
        a[3*k+1]=c*hl[x]//(b*b); z[3*k+1]=ceildiv(c*hu[x],b*b)
        a[3*k+2]=c*hl[y]//b; z[3*k+2]=ceildiv(c*hu[y],b)
    return a,z

def weights(m: int, terms: int) -> tuple[list[int],list[int]]:
    h=2*m; lo=[]; hi=[]
    for r in range(m):
        o=r if r%2 else r+m
        low=0; high=0
        for k in range(terms):
            a,b=interval(1,(o+h*k)**2); low+=a; high+=b
        # Integral comparison for the ENTIRE positive tail, k>=terms.
        low+=SCALE//(h*(o+h*terms))
        high+=ceildiv(SCALE,h*(o+h*(terms-1)))
        lo.append(low); hi.append(high)
    return lo,hi

def rounded(lo: int,hi: int,bits: int) -> list[int]:
    den=1<<(bits-OUT_BITS)
    return [max(0,lo//den-8),ceildiv(hi,den)+8]

def trace_row(q: int,z2: tuple[list[int],list[int]],z4: tuple[list[int],list[int]]) -> dict:
    m=len(z2[0]); terms=128 if q<=3 else 16
    wl,wu=weights(m,terms)
    e0=e1=d0=d1=s0=s1=0
    for a,b,c,d,l,h in zip(*z2,*z4,wl,wu):
        e0+=a*l; e1+=b*h; d0+=c*l; d1+=d*h
        s0+=a*a*l; s1+=b*b*h
    need(sum(z2[0])<=SCALE*m<=sum(z2[1]),'square mass law')
    need(sum(z4[0])*5**q<=SCALE*27**q<=sum(z4[1])*5**q,'fourth mass law')
    return {'q':q,'residues':m,'weight_head_terms':terms,
            'E':rounded(e0,e1,2*BITS),'D':rounded(d0,d1,2*BITS),
            'S':rounded(s0,s1,3*BITS)}

def bank(limit: int,clock: int) -> dict:
    rows=[{'q':q,'active':0,'Elo':0,'Ehi':0,'Dlo':0,'Dhi':0,'c2':0,'prefix_max':0}
          for q in range(clock+1)]
    raw=0
    for source in range(1,limit+1,2):
        n=source; total=0; seen=set(); active=True; peak=n
        for q,row in enumerate(rows):
            if n in seen: active=False
            seen.add(n); peak=max(peak,n); row['prefix_max']=max(row['prefix_max'],peak)
            l,h=interval(81**q,(1<<(4*total))*n*n)
            row['Dlo']+=l; row['Dhi']+=h
            if active:
                l,h=interval(9**q,(1<<(2*total))*n*n)
                row['Elo']+=l; row['Ehi']+=h; row['c2']+=l*l; row['active']+=1
            if q<clock:
                y=3*n+1; a=(y&-y).bit_length()-1
                total+=a; raw+=a; n=y>>a
    upper=0
    for row in rows:
        q=row['q']+1; e=row['Elo']; upper+=row['Dhi']
        need(4*row['c2']*SCALE>=e**3,'reciprocal envelope interpolation')
        need(e**3*q**3<=12*upper*SCALE**2,'elementary finite-bank coercivity')
        need(19**19*e**57*q**59<=236**19*16**40*upper**19*SCALE**38,
             'beta=19/20 finite-bank coercivity')
        row['tail_allowance']=[1,2*(limit+1)]
    return {'odd_source_limit':limit,'clock':clock,'sources':(limit+1)//2,
            'shortcut_steps':raw,'rows':rows}

def main() -> None:
    p=argparse.ArgumentParser(); p.add_argument('--output',type=Path,required=True)
    p.add_argument('--depth',type=int,default=10); p.add_argument('--limit',type=int,default=4095)
    p.add_argument('--clock',type=int,default=80); a=p.parse_args()
    need(0<=a.depth<=12,'depth must be 0..12'); need(a.limit>0 and a.limit%2==1,'odd cutoff')
    need(0<=a.clock<=200,'clock must be 0..200')
    z2=([SCALE],[SCALE]); z4=([SCALE],[SCALE]); traces=[]
    for q in range(a.depth+1):
        traces.append(trace_row(q,z2,z4))
        if q<a.depth: z2=transition(*z2,2); z4=transition(*z4,4)
    out={'schema':1,'status':'PROPOSED; no pointwise pressure-decay proof',
         'base':'41a408e5e617fb4e65142485f6f3ff3e6ef6c408',
         'density_bits':BITS,'trace_bits':OUT_BITS,'geometric_terms':32,
         'traces':traces,'bank':bank(a.limit,a.clock)}
    data=canonical(out); a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_bytes(data)
    print(json.dumps({'ok':True,'sha256':hashlib.sha256(data).hexdigest(),
        'bytes':len(data),'all_source_trace_depth':a.depth,
        'ternary_residue_entries_per_power':sum(r['residues'] for r in traces),
        'bank_source_clock_entries':out['bank']['sources']*(a.clock+1)},sort_keys=True))

if __name__=='__main__': main()
