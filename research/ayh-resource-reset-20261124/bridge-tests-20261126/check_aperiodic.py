"""Independent finite replay of APERIODIC_HORIZONS.md, not its infinite proof."""
from math import isqrt
import json

def step(n):
    return (3*n+1)//2 if n%2 else n//2

def check(n, depth, zeros, clock):
    left, right = set(), set()
    m = n
    for j in range(depth+1):
        x, y = m, m+1
        for _ in range(clock(j)+1):
            left.add(x)
            right.add(y)
            x, y = step(x), step(y)
        m = 2*m + int(j+1 not in zeros)
    if not left.isdisjoint(right):
        raise ValueError('actual ordinary opposite-endpoint meeting')
    return [len(left),len(right)]

results=[]
for H in [0,1,3,7,16,32]:
    zeros={2*((2*H+4)*k+isqrt(2*k*k)) for k in range(1,1202)}
    sizes=check((1<<(5*H+5))-1,1200,zeros,lambda j:H)
    results.append(dict(kind='fixed_horizon',H=H,depth=1200,sizes=sizes))
for N in [128,256,1024]:
    zeros={N<<k for k in range(20)}
    sizes=check((1<<N)-1,3000,zeros,lambda j:(N+j)//128)
    results.append(dict(kind='fixed_root_growing_clocks',N=N,depth=3000,sizes=sizes))
if results[5]['sizes'] != [37369,1489] or results[6]['sizes'] != [39576,3038]:
    raise ValueError('independent sizes differ from reported controls')
print(json.dumps(results,indent=2))
