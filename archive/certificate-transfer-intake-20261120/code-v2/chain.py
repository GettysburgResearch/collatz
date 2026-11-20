# Markov chain on relations between the two orbits at equal halving counts.
#   a >= 0 :  Y = 3^a * X + e        a < 0 :  X = 3^|a| * Y + e
# driven by the parity of X (a>=0) / parity of Y (a<0), each a fair coin.
# start: X = 9k+1, Y = 27k+2 = 3X - 1  ->  (a,e) = (1,-1).  absorbing state (0,0) = orbits merged.
import sys, random
from collections import defaultdict
P3=[3**i for i in range(4000)]
def step(a,e,bit):
    """bit = parity of the driving variable (X if a>=0, Y if a<0). returns new (a,e)."""
    if a>=1 or a<=-1:
        m=abs(a); sg=1 if a>0 else -1
        if e%2==0:
            if bit==0: return (a, e//2)
            return (a, (3*e+1-P3[m])//2)
        else:
            # other variable has opposite parity
            if bit==0:   # driver even, other odd -> other gains an odd step
                return (sg*(m+1), (3*e+1)//2)
            else:        # driver odd, other even
                if m>=2: return (sg*(m-1), (e-P3[m-1])//2)
                # m==1 -> a becomes 0.  convention at a=0: Y = X + e0
                en=(e-1)//2            # driver' = other' + en... careful with sides
                # a=+1: Y=3X+e, X odd: X'=(3X+1)/2, Y'=Y/2 => Y' = X' + (e-1)/2
                # a=-1: X=3Y+e, Y odd: Y'=(3Y+1)/2, X'=X/2 => X' = Y' + (e-1)/2 => Y' = X' - (e-1)/2
                return (0, en if a>0 else -en)
    else:
        # a==0: Y = X + e, driver X
        if e%2==0:
            return (0, e//2) if bit==0 else (0, 3*e//2)
        else:
            if bit==0:  # X even, Y odd
                return (1, (3*e+1)//2)
            else:       # X odd, Y even: X' = 3Y' + (1-3e)/2
                return (-1, (1-3*e)//2)

def exact(smax):
    dist={(1,-1):1}
    out=[]
    for s in range(1,smax+1):
        nd=defaultdict(int)
        for (a,e),c in dist.items():
            if (a,e)==(0,0): nd[(0,0)]+=2*c; continue
            nd[step(a,e,0)]+=c; nd[step(a,e,1)]+=c
        dist=nd
        merged=dist.get((0,0),0)
        out.append((s,merged/2**s,len(dist)))
    return out

if __name__=="__main__":
    mode=sys.argv[1]
    if mode=="exact":
        for s,m,n in exact(int(sys.argv[2])):
            print(f"s={s:3d} merged={m:.10f} unmerged={1-m:.10f} states={n}")
    else:
        nsamp=int(sys.argv[2]); T=int(sys.argv[3]); random.seed(1)
        marks=[10,20,26,50,100,200,500,1000,2000,5000,10000,20000,50000,100000]
        marks=[m for m in marks if m<=T]
        absorbed_at=[]
        for _ in range(nsamp):
            a,e=1,-1; t=0; hit=None
            bits=random.getrandbits(T)
            while t<T:
                a,e=step(a,e,(bits>>t)&1); t+=1
                if a==0 and e==0: hit=t; break
            absorbed_at.append(hit)
        for m in marks:
            u=sum(1 for h in absorbed_at if h is None or h>m)/nsamp
            print(f"depth {m:6d}: unmerged fraction ~ {u:.4f}")
