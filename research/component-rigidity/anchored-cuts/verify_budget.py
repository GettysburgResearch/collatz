#!/usr/bin/env python3
"""Replay stored compiler controls without importing the compiler/generator."""
from fractions import Fraction
import json
from pathlib import Path
import sys
from verify_certificates import check_cut, need


def main():
    path=Path(sys.argv[1]) if len(sys.argv)>1 else Path('budget_certificates.json')
    rows=json.loads(path.read_text(encoding='utf-8'))
    outcomes={}
    path_edges=0
    for row in rows:
        status=row['status']; outcomes[status]=outcomes.get(status,0)+1
        anchor=row['anchor']; a=row['multiplier']
        need(a in (3,5),'invalid map')
        if status=='CONVERGENCE':
            seq=row['path']
            need(seq[0]==anchor and seq[-1]==1,'path endpoints')
            need(all(1<=x<=row['height'] for x in seq),'path bounds')
            for x,y in zip(seq,seq[1:]):
                need(y==(x//2 if x%2==0 else (a*x+1)//2),'literal map step')
                path_edges+=1
        elif status=='ENERGY_BUDGET_EXCLUDED':
            c=row['certificate']; check_cut(c)
            need(c['anchor']==anchor and c['multiplier']==a and c['height']==row['height'],
                 'certificate metadata mismatch')
            need(Fraction(*c['capacity'])>Fraction(*row['budget']),'budget not exceeded')
        elif status=='UNRESOLVED_AT_RESOURCE_CAP':
            heights=row['inspected_heights']
            need(heights and all(h<=row['max_height'] for h in heights),'cap metadata')
            need(2*heights[-1]>row['max_height'],'cap not exhausted')
        else:
            raise ValueError('unrecognized compiler outcome')
    # A bounded nonzero dyadic invariant is not automatically T-invariant.
    h=2**12
    bits=[0]+[int(5*2**(n.bit_length()-1)<=4*n<6*2**(n.bit_length()-1)) for n in range(1,h+1)]
    need(all(bits[n]==bits[2*n] for n in range(1,h//2+1)),'dyadic control')
    for k in range(2,12):
        need(sum(bits[n]!=bits[n+1] for n in range(2**k,2**(k+1)))==2,'bounded variation control')
    need(bits[3]!=bits[5],'odd-equation failure control lost')
    need(outcomes=={'ENERGY_BUDGET_EXCLUDED':2,'CONVERGENCE':2,'UNRESOLVED_AT_RESOURCE_CAP':1},
         'stored control coverage changed')
    print(json.dumps(dict(status='PASS',controls=len(rows),outcomes=outcomes,
                          literal_convergence_edges=path_edges,
                          dyadic_only_countercontrol='PASS'),sort_keys=True,indent=2))

if __name__=='__main__':
    main()
