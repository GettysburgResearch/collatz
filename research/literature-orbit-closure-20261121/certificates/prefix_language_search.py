"""Exact finite binary-prefix deletion certificates, exploratory only.

T^H(2^H q+a) = T^(H-r)(2^(H-r)q+(a>>r))
is certified by equality of both the finite constant and odd-step count.
No finite computation is promoted to a universal cover.
"""
from collections import defaultdict
import json


def step(n):
    return (3*n+1)//2 if n & 1 else n//2


def history(n, h):
    out = [(n, 0)]
    p = 0
    for _ in range(h):
        p += n & 1
        n = step(n)
        out.append((n,p))
    return out


def search(H):
    hist = [history(n,H) for n in range(1<<H)]
    rules = []
    for r in range(1,H):
        for a in range(1,1<<H,2):
            b = a >> r
            if b & 1 and hist[a][H] == hist[b][H-r]:
                rules.append((r,a,b,H,hist[a][H]))
    # Collapse each residue rule whenever its sibling has the same deletion.
    by_r = defaultdict(set)
    for r,a,b,H,key in rules:
        by_r[r].add((H,a))
    for r, current in by_r.items():
        for h in range(H,r+1,-1):
            for a in range(1,1<<(h-1),2):
                if (h,a) in current and (h,a+(1<<(h-1))) in current:
                    current.remove((h,a))
                    current.remove((h,a+(1<<(h-1))))
                    current.add((h-1,a))
    out = [(r,h,a,a>>r,a% (1<<r)) for r,rs in by_r.items() for h,a in rs]
    out.sort(key=lambda x:(x[1],x[0],x[2]))
    return out


if __name__ == '__main__':
    H=14
    out=search(H)
    dest='/workspace/scratch/c6766c1207a3/collatz_work/literature_symbolic/prefix_language_rules.json'
    with open(dest,'w') as f:
        json.dump({'H':H, 'rules_r_h_a_b_c':out},f,indent=2)
    print(json.dumps({'H':H,'count':len(out),'first_rules':out[:80]},indent=2))
