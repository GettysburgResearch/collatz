#!/usr/bin/env python3
"""Integer-interval checks of the direct energy dissipation inequality."""
from __future__ import annotations
import argparse, copy, hashlib, json
from pathlib import Path

BITS=128
UNIT=1<<BITS
TRACE=1<<60
EXPECTED='968f78afceb00b006320e8ef6d851bbfbbeb246ab2a92a24dd85885942979a1e'

def need(ok: bool,message: str) -> None:
    if not ok: raise ValueError(message)

def up(n: int,d: int) -> int: return (n+d-1)//d

def check_table(rows: list[dict]) -> int:
    for q,(r,s) in enumerate(zip(rows,rows[1:])):
        need(r['q']==q and s['q']==q+1,'clock inventory')
        loss=r['E'][0]-s['E'][1]
        need(loss>0,'positive certified loss')
        need(16384*loss**2*r['D'][0]*TRACE**2>=441*r['E'][1]**5,
             'certified all-source dissipation')
    return len(rows)-1

def bank(limit: int,clock: int) -> dict:
    state=list(range(1,limit+1,2)); valuations=[0]*len(state)
    count=0; rows=[]
    for q in range(clock+1):
        ehi=dlow=losslow=0
        for k,t in enumerate(state):
            den=(1<<(2*valuations[k]))*t*t
            num=(9**q)*UNIT
            ehi+=up(num,den)
            dlow+=(81**q)*UNIT//((1<<(4*valuations[k]))*t*t)
            losslow+=num*(6*t+1)//(den*(3*t+1)**2)
        need(16384*losslow**2*dlow*UNIT**2>=441*ehi**5,
             'finite-bank dissipation')
        rows.append([q,ehi,dlow,losslow])
        if q<clock:
            for k,t in enumerate(state):
                t=(3*t+1)//2; valuations[k]+=1; count+=1
                while t%2==0:
                    t//=2; valuations[k]+=1; count+=1
                state[k]=t
    return {'source_clock_entries':len(state)*(clock+1),'shortcut_steps':count,
            'rows_sha256':hashlib.sha256(json.dumps(rows,separators=(',',':')).encode()).hexdigest(),
            'inequalities':len(rows)}

def main() -> None:
    p=argparse.ArgumentParser(); p.add_argument('evidence',type=Path)
    p.add_argument('--output',type=Path,required=True); a=p.parse_args()
    raw=a.evidence.read_bytes(); need(hashlib.sha256(raw).hexdigest()==EXPECTED,'frozen evidence hash')
    d=json.loads(raw); checks=check_table(d['traces']); tested=bank(4095,80)
    bads=[]
    for key in ('D','E'):
        b=copy.deepcopy(d['traces'])
        if key=='D': b[0]['D'][0]=0
        else: b[0]['E'][1]*=100
        bads.append(b)
    b=copy.deepcopy(d['traces']); b[1]['E'][1]=b[0]['E'][0]; bads.append(b)
    b=copy.deepcopy(d['traces']); b[3]['q']+=1; bads.append(b)
    b=copy.deepcopy(d['traces']); b[-1]['E'][1]*=100; bads.append(b)
    for b in bads:
        try: check_table(b)
        except ValueError: pass
        else: raise ValueError('corruption accepted')
    out={'ok':True,'all_source_consecutive_pairs':checks,'finite_bank':tested,
         'direct_corruptions_rejected':len(bads),'evidence_sha256':EXPECTED,
         'status':'finite checks of proved inequality; reciprocal-moment divergence remains OPEN'}
    a.output.write_text(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n')
    print(json.dumps(out,sort_keys=True))

if __name__=='__main__': main()
