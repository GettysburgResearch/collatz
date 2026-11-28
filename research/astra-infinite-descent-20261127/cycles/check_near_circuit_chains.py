"""Rational certificates for six to eight mismatch positions."""
from fractions import Fraction as F
from pathlib import Path
import json
from check_near_circuit import LOW,HIGH,plus,scaled,sub,cube_max


def chain_rows(s,split,alpha):
    vectors=[tuple(F(i==j) for i in range(s)) for j in range(s)]
    one,r,*ordinary=vectors
    zero=scaled(0,one)
    slack=scaled(F(1,128),one)
    beta=alpha-1
    times=ordinary[:split]+[sub(one,r)]+ordinary[split:]+[one]
    lengths=[sub(b,a) for a,b in zip([zero]+times[:-1],times)]
    out={f'length_{i}':l for i,l in enumerate(lengths)}
    out['shorter_lag']=sub(scaled(F(1,2),one),r)
    max_h,min_h=[],[]
    for i,t in enumerate(times):
        if i==split:
            hi,lo=scaled(beta,t),zero
        elif i==s-1:
            hi,lo=scaled(beta,r),zero
        elif i<split:
            hi,lo=scaled(beta,plus(t,r)),scaled(beta,t)
        else:
            hi,lo=scaled(beta,t),scaled(beta,sub(plus(t,r),one))
        max_h.append(hi)
        min_h.append(lo)
    for i,l in enumerate(lengths):
        next_l=lengths[(i+1)%s]
        out[f'next_spacing_{i}']=plus(sub(max_h[i],next_l),slack)
        out[f'combined_{i}']=plus(sub(plus(max_h[i],min_h[i]),plus(next_l,scaled(alpha,l))),slack)
        for count in range(2,s):
            ids=[(i+j)%s for j in range(count)]
            if any(j in (split,s-1) for j in ids[:-1]):
                continue
            end=ids[-1]
            budget=plus(max_h[end],*(min_h[j] for j in ids))
            demand=plus(scaled(alpha,plus(*(lengths[j] for j in ids))),lengths[(end+1)%s])
            out[f'chain_{i}_{count}']=plus(sub(budget,demand),slack)
    return out


def main():
    cert=json.loads(Path(__file__).with_name('near_circuit_chain_duals.json').read_text())
    if not 2**15849<3**10000<2**15850:
        raise ValueError('failed rational slope bracket')
    out=[]
    for s in range(6,9):
        for split in range(s-1):
            weights=cert[f'{s},{split}']
            if not weights or any(type(w)!=int or w<=0 for w in weights.values()):
                raise ValueError('invalid nonnegative dual')
            maxima=[]
            for a in (LOW,HIGH):
                rows=chain_rows(s,split,a)
                v=plus(*(scaled(w,rows[k]) for k,w in weights.items()))
                maxima.append(cube_max(v)/sum(weights.values()))
            result=max(maxima)
            if result>=-F(1,100):
                raise ValueError((s,split,result))
            out.append(dict(mismatches=s,ordinary_before_paired_giant=split,
                            weights=weights,normalized_upper=str(result)))
    print(json.dumps(out,indent=2))


if __name__=='__main__':
    main()
