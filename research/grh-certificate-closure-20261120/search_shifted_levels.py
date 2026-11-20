from heapq import heappop,heappush
from math import gcd
from pathlib import Path
import time,json
OUT=Path(__file__).parent

def norm(a,b):
    for p in (2,3):
        while a%p==b%p==0:a//=p;b//=p
    return a,b

def moves(a,b,J):
    if a%2==0 and b%2:
        for j in [1,*range(J,J+5)]:
            if j==1 and (a%3 or b%3==0):continue
            yield norm(3**j*a,3**j*b+1),('forward',j)
    for m in range(1,13):
        off=2**m*b-1
        if (a%9==0 and off%3==0 and off%9) or (a%3**J==0 and off%3**J==0):
            yield norm(2**m*a,off),('reverse',m)

def descend(M,r,J,deadline):
    q=[(M,r)];seen={(M,r):None};act={}
    for pop in range(500):
        if not q:return None,pop
        if time.monotonic()>deadline:raise TimeoutError
        a,b=heappop(q)
        for (c,d),tag in moves(a,b,J):
            if c<=0 or d<=0:raise ValueError('positive form')
            if c<M:
                path=[((c,d),tag)]; cur=(a,b)
                while seen[cur] is not None:
                    path.append((cur,act[cur]));cur=seen[cur]
                path.append((cur,None));path.reverse()
                return {'M':M,'r':r,'a':c,'b':d,'path':path},pop+1
            if c<=10000*M and (c,d) not in seen:
                seen[c,d]=(a,b);act[c,d]=tag;heappush(q,(c,d))
    return None,500

def run(J):
    start=time.monotonic();deadline=start+20
    active=[(162,r) for r in range(162) if gcd(r,6)==1]
    certs=[];uncovered=[];pops=0
    try:
        while active:
            M,r=active.pop(); ans,n=descend(M,r,J,deadline);pops+=n
            if ans:certs.append(ans)
            elif M<81*2**8:active.extend([(2*M,r),(2*M,r+M)])
            else:uncovered.append((M,r))
    except TimeoutError:pass
    result={'J':J,'scope':'bounded search only, no theorem for unsearched cells','seconds':round(time.monotonic()-start,2),'pops':pops,'certified_cells':len(certs),'uncovered_leaves':len(uncovered),'unsearched_cells':len(active),'uncovered_examples':uncovered[:20],'certificates':certs}
    (OUT/f'level-{J}.json').write_text(json.dumps(result,indent=2)+'\n')
    print({k:v for k,v in result.items() if k not in ['certificates','uncovered_examples']},flush=True)
for J in (7,8,9):run(J)
