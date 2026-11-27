"""Independent maximum-gain census by one dynamic program on the full finite orbit DAG."""
from collections import Counter,deque
from hashlib import sha256
import json


def demand(ok,tag):
    if not ok:raise ArithmeticError(tag)


def step(x):
    v=3*x+1;e=(v&-v).bit_length()-1
    return v>>e,e


def evaluate(B):
    nxt={1:(1,2)};depth={1:0}
    for seed in range(1,B+1,2):
        x=seed;fresh=[];seen=set()
        while x not in depth:
            demand(x not in seen,'new cycle during definitive finite graph discovery')
            seen.add(x);fresh.append(x);nxt[x]=step(x);x=nxt[x][0]
        for v in reversed(fresh):
            depth[v]=depth[nxt[v][0]]+1
    full=sum(depth[v]+1 for v in range(1,B+1,2))
    indeg=Counter()
    for x,(y,e) in nxt.items():
        if x!=1:indeg[y]+=1
    frontier=deque(x for x in depth if not indeg[x])
    # Store rational gain 3^k/2^a and least original source attaining it.
    best={x:(1,0,x) for x in range(1,B+1,2)}
    count=0
    while frontier:
        x=frontier.popleft();count+=1
        if x==1:continue
        y,e=nxt[x];t,a,v=best[x]
        cand=(3*t,a+e,v)
        if y in best:
            tt,aa,vv=best[y]
            le=cand[0]<<aa;ri=tt<<cand[1]
            if le>ri or (le==ri and v<vv):best[y]=cand
        else:best[y]=cand
        indeg[y]-=1
        if indeg[y]==0:frontier.append(y)
    demand(count==len(depth)==len(best),'complete acyclic graph evaluation')
    rows={x:(n,1<<a,v) for x,(n,a,v) in best.items() if B*n>=x<<a}
    digest=sha256()
    for x,(n,d,v) in sorted(rows.items()):
        demand(v*n<=x*d<=B*n,'source bound and superlevel')
        if x%3==0:demand((n,d,v)==(1,1,x),'no nonempty unit ancestor')
        digest.update(f'{x} {n} {d} {v}\n'.encode('ascii'))
    mx=max(rows)
    return dict(bound=B,full_DAG_nodes=len(depth),visits=full,targets=len(rows),above_bound=sum(x>B for x in rows),
                largest=mx,argmax_source=rows[mx][2],full_output_hash=digest.hexdigest())


if __name__=='__main__':
    print(json.dumps([evaluate(B) for B in (1,31,511,4095,65535)],indent=2,sort_keys=True))
