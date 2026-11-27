"""Independent direct orbit replay of the listed signed-chart replacements."""
from pathlib import Path
from functools import lru_cache
from hashlib import sha256
import json

lane=Path("research/astra-full-proof-20261125/transport")
witness=json.loads((lane/"competitors.json").read_text())

def require(condition, reason):
    if not condition:
        raise ValueError(reason)

def tr(n, d=1):
    return (3*n+d)//2 if n&1 else n//2
@lru_cache(maxsize=None)
def info(gaps):
    R=len(gaps)+1
    q=0
    c=1
    for g in gaps:
        q+=g
        c=3*c+2**q
    d=3**(R+1)
    u=-c
    count=0
    for i in range(1600):
        if u in (-d,-5*d,-17*d):
            return R,d,c,i,count,-u//d
        count+=u&1
        u=tr(u,d)
    raise ArithmeticError(gaps)

@lru_cache(maxsize=None)
def walk(x,n):
    y=x
    o=0
    first=0 if x==1 else None
    for j in range(1,n+1):
        o+=y&1
        y=tr(y)
        if y==1 and first is None:
            first=j
    return y,o,first
total=0
covered=set()
for e,gaps in witness:
    R0,d0,c0,i0,q0,s0=info((e,))
    R,d,c,i,q,s=info(tuple(gaps))
    require(s0==s and R0==2, ("center", e, gaps))
    P,O={1:(1,1),5:(3,2),17:(11,7)}[s]
    dk, rem=divmod(q0-3-q+R+1,O)
    require(rem==0, ("rank", e, gaps))
    delta=i-i0+P*dk
    for H in range(1600,1600+2*486):
        if pow(2,H,d0)!=c0%d0 or pow(2,H+delta,d)!=c%d:
            continue
        z=((1<<H)-c0)//d0
        w=((1<<(H+delta))-c)//d
        require(0<w<z and w&1 and z&1, ("height and parity", e, H))
        k=(H-i0)//P
        low=walk(z,i0+P*k)[0]
        rival=walk(w,i+P*(k+dk))[0]
        require(low==rival, ("physical meeting", e, H))
        require(walk(3*w,H+delta)[:2]==(1,R), ("new upper certificate", e, H))
        require(walk(3*z,H)[:2]==(1,2), ("old upper certificate", e, H))
        covered.add((e,H%486))
        total+=1
print(json.dumps({"listed_chart_pairs":len(witness),"physical_checks":total,
    "distinct_rank_two_residue_pairs_covered":len(covered),"H_range":[1600,2571],
    "distinct_charts":info.cache_info().currsize,
    "witness_sha256":sha256((lane/"competitors.json").read_bytes()).hexdigest()}))
