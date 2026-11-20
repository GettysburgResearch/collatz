import sys, random, math
sys.path.insert(0,'.')
from chain import step, P3
from collections import defaultdict
random.seed(11)
def A(n): return n//2 if n%2==0 else (3*n+1)//2
def ij(n):
    i=j=0
    while n!=1:
        if n&1: n=3*n+1; i+=1
        else: n//=2; j+=1
    return i,j
def lam(n):
    i,j=ij(n); return 2*i-j

def exact_from(a0,e0,smax):
    dist={(a0,e0):1}; out=[]
    for s in range(1,smax+1):
        nd=defaultdict(int)
        for (a,e),c in dist.items():
            if (a,e)==(0,0): nd[(0,0)]+=2*c; continue
            nd[step(a,e,0)]+=c; nd[step(a,e,1)]+=c
        dist=nd; out.append(dist.get((0,0),0)/2**s)
    return out
def mc_from(a0,e0,nsamp,T,marks):
    hits=[]
    for _ in range(nsamp):
        a,e=a0,e0; bits=random.getrandbits(T); hit=None
        for t in range(T):
            a,e=step(a,e,(bits>>t)&1)
            if a==0 and e==0: hit=t+1; break
        hits.append(hit)
    return [sum(1 for h in hits if h is None or h>m)/nsamp for m in marks]

print("== R1/R7: other starting relations: unmerged share after s bits ==")
marks=[10,100,1000,5000]
for (a0,e0,name) in [(0,1,"n , n+1"),(0,7,"n , n+7"),(0,-100,"n , n-100"),(1,-1,"n , 3n-1  (ours)"),(2,5,"n , 9n+5"),(4,1001,"n , 81n+1001")]:
    ex=exact_from(a0,e0,22)
    u=mc_from(a0,e0,1500,5000,marks)
    print(f"{name:22s} exact unmerged at s=10: {1-ex[9]:.4f}, s=22: {1-ex[21]:.4f} | MC unmerged at {marks}: {u}")

print("== R1b: random B-bit n: do n and n+1 have equal (triplings,halvings)? ==")
for B in [30,100,300,1000,3000]:
    N=400; eq=0
    for _ in range(N):
        n=random.getrandbits(B)|(1<<(B-1))
        if ij(n)==ij(n+1): eq+=1
    print(f"B={B:5d}: equal for {eq/N:.3f} of sampled n")
