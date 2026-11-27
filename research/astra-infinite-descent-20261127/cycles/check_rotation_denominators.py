"""Arbitrary-clock rotation denominator certificates from actual common block clocks."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
from check_six_rotations import rows as chained_rows
from check_near_circuit import LOW,HIGH,plus,scaled,sub,cube_max


def rows(s,wrapped,alpha,signs):
    # The exact common division clock is an additional coordinate for each arc.
    dim=8*s+2
    cols=[tuple(F(j==i) for j in range(dim)) for i in range(dim)]
    one=cols[0]
    ts=cols[1:s+1]
    U=cols[s+2:2*s+2];V=cols[2*s+2:3*s+2]
    u=cols[3*s+2:4*s+2];v=cols[4*s+2:5*s+2]
    B=cols[5*s+2:6*s+2];E=cols[6*s+2:7*s+2]
    A=cols[7*s+2:8*s+2]
    L=[sub(ts[i],ts[i-1]) for i in range(s)]
    L[0]=plus(L[0],one)
    original=chained_rows(s,wrapped,alpha)
    keep=('half_','time_','prefix_','step_','end_','low_','extra_')
    result={n: (*a,*((F(0),)*s)) for n,a in original.items() if n.startswith(keep)}
    for i in range(s):
        l=scaled(alpha,L[i])
        left=sub(plus(l,U[i-1]),plus(U[i],u[i]))
        right=sub(plus(l,V[i-1]),plus(V[i],v[i]))
        result[f'left_clock_{i}']=sub(A[i],left)
        result[f'right_clock_{i}']=sub(A[i],right)
        result[f'duration_{i}']=sub(A[i],L[i])
        result[f'start_cap_{i}']=sub(plus(U[i-1],V[i-1]),plus(B[i-1],A[i]))
        if signs[i]!='*':
            hi,lo,highclock=(U,V,left) if signs[i]=='L' else (V,U,right)
            result[f'orient_{i}']=sub(hi[i-1],lo[i-1])
            result[f'upper_clock_{i}']=sub(highclock,A[i])
            result[f'separation_{i}']=sub(hi[i-1],A[i])
        for size in range(1,s+1):
            ids=[(i-k)%s for k in range(size)]
            costs=[plus(u[j],v[j],B[j]) for j in ids[1:]]
            upper=plus(U[i],V[i],E[i],*costs)
            lower=plus(A[(i+1)%s],scaled(alpha,plus(*(L[j] for j in ids))))
            result[f'chain_{i}_{size}']=sub(upper,lower)
    return result


def leaves(tree,signs):
    if 'weights' in tree:
        yield signs,tree['weights']
        return
    i=tree['branch']
    if not 0<=i<len(signs) or signs[i]!='*':
        raise ValueError('bad orientation split')
    for side in ('L','R'):
        yield from leaves(tree[side],signs[:i]+side+signs[i+1:])


def error_cost(label):
    if label.startswith('prefix_'):
        return int(label.rsplit('_',1)[1])+2
    if label.startswith('step_'):
        return 2
    if label.startswith('upper_clock_'):
        return 1
    return 0


def main():
    cert=json.loads(Path(__file__).with_name('rotation_denominator_duals.json').read_text())
    if not 2**15849<3**10000<2**15850:
        raise ValueError('slope')
    cases=[]
    for s in range(2,7):
        for w in range(s+1):
            tested=[]
            for signs,weights in leaves(cert[f'{s},{w}'],'*'*s):
                if not weights or not all(type(v)==int and v>0 for v in weights.values()):
                    raise ValueError('weights')
                vals=[]
                for alpha in (LOW,HIGH):
                    rs=rows(s,w,alpha,signs)
                    row=plus(*(scaled(v,rs[k]) for k,v in weights.items()))
                    vals.append(cube_max(row)/sum(weights.values()))
                m=max(vals)
                tax=F(sum(v*error_cost(k) for k,v in weights.items()),sum(weights.values()))
                charged=m+tax/F(4096)
                if charged>=0:
                    raise ValueError((s,w,signs,m))
                tested.append(dict(higher_sides=signs,normalized_upper=str(m),error_weight=str(tax),charged_upper=str(charged)))
            cases.append(dict(mismatches=s,wrapped=w,leaves=tested))
    print(json.dumps(cases,indent=2))


if __name__=='__main__':main()
