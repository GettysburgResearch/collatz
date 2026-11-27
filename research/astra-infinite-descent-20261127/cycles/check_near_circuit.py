"""Exact Farkas controls for the physical near-circuit rotation inequalities.

Variables after the constant are lag/p and the ordinary mismatch positions/p.
The constants and multipliers use fractions. Each certificate is bounded on the
full unit cube, so no floating point optimizer is required for the check.
"""
from fractions import Fraction as F
import json

LOW = F(15849, 10000)
HIGH = F(15850, 10000)
SLACK = F(1, 32)


def plus(*terms):
    return tuple(map(sum, zip(*terms)))


def neg(v):
    return tuple(-e for e in v)


def scaled(a, v):
    return tuple(a*e for e in v)


def sub(a, b):
    return plus(a, neg(b))


def rows(s, split, alpha):
    dim = s
    units = [tuple(F(i == j) for i in range(dim)) for j in range(dim)]
    one, shift, *ordinary = units
    zero = scaled(0, one)
    slack = scaled(SLACK, one)
    beta = alpha-1
    paired_giant = sub(one, shift)
    ends = ordinary[:split] + [paired_giant] + ordinary[split:] + [one]
    lengths = [sub(b,a) for a,b in zip([zero]+ends[:-1], ends)]
    out = [(f'length_{i}', length) for i,length in enumerate(lengths)]
    out.append(('shorter_lag', sub(scaled(F(1,2),one),shift)))
    after = []
    maximum = []
    for i, pos in enumerate(ends):
        if i == split:
            heights = (scaled(beta, pos), zero)
            high = heights[0]
        elif i == s-1:
            heights = (zero, scaled(beta, shift))
            high = heights[1]
        elif i < split:
            heights = (scaled(beta,pos), scaled(beta,plus(pos,shift)))
            high = heights[1]
        else:
            heights = (scaled(beta,pos), scaled(beta,sub(plus(pos,shift),one)))
            high = heights[0]
        after.append(heights)
        maximum.append(high)
    for i, length in enumerate(lengths):
        nxt = lengths[(i+1) % s]
        gap = sub(maximum[i], nxt)
        out.append((f'next_spacing_{i}', plus(gap, slack)))
        pressure = sub(plus(*after[i]),plus(scaled(alpha,length),nxt))
        out.append((f'combined_{i}',plus(pressure,slack)))
    return out


def cube_max(row):
    return row[0]+sum(max(0,a) for a in row[1:])


def verify(cert):
    if not (2**15849 < 3**10000 < 2**15850):
        raise ValueError('slope bracket')
    cases = []
    for s in range(2,6):
        for split in range(s-1):
            multipliers = cert[f'{s},{split}']
            if not multipliers or any(type(m) != int or m <= 0 for m in multipliers.values()):
                raise ValueError('nonnegative nonzero integer dual')
            maxima = []
            for a in (LOW, HIGH):
                system = dict(rows(s,split,a))
                total = plus(*(scaled(m,system[name]) for name,m in multipliers.items()))
                maxima.append(cube_max(total)/sum(multipliers.values()))
            bound = max(maxima)
            if bound >= 0:
                raise ValueError((s,split,'dual bound fails',bound))
            cases.append(dict(s=s,ordinary_before_paired_giant=split,
                              weights=multipliers,upper_bound=str(bound)))
    return cases


if __name__ == '__main__':
    from pathlib import Path
    filepath = Path(__file__).with_name('near_circuit_duals.json')
    print(json.dumps(verify(json.loads(filepath.read_text())),indent=2))
