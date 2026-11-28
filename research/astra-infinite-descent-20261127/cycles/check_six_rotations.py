"""Exact certificates for six arbitrary-rotation mismatches, using consecutive arcs."""
from fractions import Fraction as F
from pathlib import Path
import json
from check_five_rotations import rows as local_rows
from check_near_circuit import LOW, HIGH, plus, scaled, sub, cube_max


def rows(s, wrapped, alpha):
    dimension = 7*s+2
    units = [tuple(F(i == j) for j in range(dimension)) for i in range(dimension)]
    one = units[0]
    times, left, right, u, v, low, extra = (
        units[1:s+1], units[s+2:2*s+2], units[2*s+2:3*s+2],
        units[3*s+2:4*s+2], units[4*s+2:5*s+2],
        units[5*s+2:6*s+2], units[6*s+2:7*s+2])
    length = [sub(times[i], times[i-1]) for i in range(s)]
    length[0] = plus(length[0], one)
    a = [sub(plus(scaled(alpha,length[i]),left[i-1]),plus(left[i],u[i])) for i in range(s)]
    result = {k: (*row, *((F(0),)*(2*s))) for k,row in local_rows(s,wrapped,alpha).items()}
    for i in range(s):
        excess = plus(u[i],v[i])
        result[f'low_left_{i}'] = sub(left[i],low[i])
        result[f'low_right_{i}'] = sub(right[i],low[i])
        result[f'extra_left_{i}'] = sub(left[i],extra[i])
        result[f'extra_right_{i}'] = sub(right[i],extra[i])
        result[f'extra_excess_{i}'] = sub(excess,extra[i])
        for size in range(2,s+1):
            ids = [(i-k)%s for k in range(size)]
            interior = [plus(u[j],v[j],low[j]) for j in ids[1:]]
            upper = plus(left[i],right[i],extra[i],*interior)
            lower = plus(a[(i+1)%s],scaled(alpha,plus(*(length[j] for j in ids))))
            result[f'chain_{i}_{size}'] = sub(upper,lower)
    return result


def main():
    s=6
    weights=json.loads(Path(__file__).with_name('six_rotation_duals.json').read_text())
    if not 2**15849<3**10000<2**15850:
        raise ValueError('slope bracket')
    records=[]
    for wrapped in range(s+1):
        data=weights[f'{s},{wrapped}']
        if not data or not all(type(w)==int and w>0 for w in data.values()):
            raise ValueError('invalid Farkas weights')
        upper=[]
        for alpha in (LOW,HIGH):
            system=rows(s,wrapped,alpha)
            combination=plus(*(scaled(w,system[k]) for k,w in data.items()))
            upper.append(cube_max(combination)/sum(data.values()))
        mx=max(upper)
        if mx>=-F(1,512):
            raise ValueError((s,wrapped,mx))
        records.append(dict(mismatches=s,wrap_count=wrapped,normalized_upper=str(mx),weights=data))
    print(json.dumps(records,indent=2))


if __name__=='__main__':
    main()
