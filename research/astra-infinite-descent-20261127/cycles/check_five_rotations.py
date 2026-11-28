"""Exact Farkas certificates for up to five mismatches at an arbitrary odd rotation."""
from fractions import Fraction as F
from pathlib import Path
import json
from check_near_circuit import LOW,HIGH,plus,scaled,sub,cube_max


def rows(s, wrapped, alpha):
    # One constant, s chronological postcut times, lag, paired source heights, paired excesses.
    dim=5*s+2
    unit=[tuple(F(i==j) for i in range(dim)) for j in range(dim)]
    one,ts,r=unit[0],unit[1:s+1],unit[s+1]
    zero=scaled(0,one)
    beta=alpha-1
    U=unit[s+2:2*s+2]
    V=unit[2*s+2:3*s+2]
    u=unit[3*s+2:4*s+2]
    v=unit[4*s+2:5*s+2]
    time=ts+[sub(plus(ts[i],r),one if i>=s-wrapped else zero) for i in range(s)]
    state=U+V
    pay=u+v
    length=[sub(ts[i],ts[i-1]) if i else plus(sub(ts[i],ts[-1]),one) for i in range(s)]
    a=[sub(plus(scaled(alpha,length[i]),U[i-1]),plus(U[i],u[i])) for i in range(s)]
    result={'half_lag':sub(scaled(F(1,2),one),r)}
    for i in range(s):
        diff=sub(v[i],u[i])
        change=sub(sub(V[i-1],U[i-1]),sub(V[i],U[i]))
        result[f'diff_plus_{i}']=sub(diff,change)
        result[f'diff_minus_{i}']=sub(change,diff)
        result[f'native_{i}']=sub(a[i],length[i])
        base=sub(plus(U[i],V[i]),plus(a[(i+1)%s],scaled(alpha,length[i])))
        for name,cost in (('excess',plus(u[i],v[i])),('left',U[i]),('right',V[i])):
            result[f'cost_{name}_{i}']=plus(base,cost)
    rotated=list(range(2*s-wrapped,2*s))+list(range(s,2*s-wrapped))
    for track,ids in enumerate((list(range(s)),rotated)):
        paid=zero
        for j,i in enumerate(ids):
            prev=ids[j-1]
            dt=sub(time[i],time[prev] if j else zero)
            result[f'time_{track}_{j}']=dt
            paid=plus(paid,pay[i])
            result[f'prefix_{track}_{j}']=sub(scaled(beta,time[i]),plus(paid,state[i]))
            if j:
                result[f'step_{track}_{j}']=sub(plus(state[prev],scaled(beta,dt)),plus(state[i],pay[i]))
        result[f'end_{track}']=sub(one,time[ids[-1]])
    return result


def main():
    weights=json.loads(Path(__file__).with_name('five_rotation_duals.json').read_text())
    if not 2**15849<3**10000<2**15850:
        raise ValueError('slope bracket')
    records=[]
    for s in range(2,6):
        for wrapped in range(s+1):
            data=weights[f'{s},{wrapped}']
            if not data or not all(type(w)==int and w>0 for w in data.values()):
                raise ValueError('invalid Farkas weights')
            upper=[]
            for a in (LOW,HIGH):
                system=rows(s,wrapped,a)
                combination=plus(*(scaled(w,system[k]) for k,w in data.items()))
                upper.append(cube_max(combination)/sum(data.values()))
            mx=max(upper)
            if mx>=0:
                raise ValueError((s,wrapped,mx))
            records.append(dict(mismatches=s,wrap_count=wrapped,normalized_upper=str(mx),weights=data))
    print(json.dumps(records,indent=2))


if __name__=='__main__':
    main()
