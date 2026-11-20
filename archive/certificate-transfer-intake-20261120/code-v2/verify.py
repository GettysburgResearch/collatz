import random, math, sys
sys.path.insert(0,'.')
from chain import step, P3
def T(n): return n//2 if n%2==0 else 3*n+1
def Ta(n): return n//2 if n%2==0 else (3*n+1)//2      # one halving per step
def orbit(n):
    o=[n]
    while n!=1: n=T(n); o.append(n)
    return o
def ij(n):
    i=j=0
    while n!=1:
        if n&1: n=3*n+1; i+=1
        else: n//=2; j+=1
    return i,j

# ---- 1. dictionary: k=4^a q -> (v , 6v+1), k=2*4^a q -> (6v+1 , 3v), v=3^(a+1) q
ok=True
for k in range(1,60001):
    e=0; q=k
    while q%2==0: q//=2; e+=1
    a=e//2; v=3**(a+1)*q
    ox=set(orbit(16*k+1)); oy=set(orbit(32*k+1))
    if e%2==0:
        if not (3*v+1 in ox and 6*v+1 in oy): ok=False; print("dict fail I",k); break
    else:
        if not (6*v+1 in ox and 9*v+1 in oy): ok=False; print("dict fail II",k); break
print("1. dictionary verified for k<=60000:",ok)

# ---- 2. integer k: chain absorption (bits of k then zeros)  <=>  D(k)=0
def chain_absorbs(k, extra=4000):
    X=9*k+1; Y=27*k+2; a,e=1,-1
    for n in range(extra):
        # driver parity: X if a>=0 else Y ; consistency check of relation
        if a>=0: assert Y==P3[a]*X+e
        else: assert X==P3[-a]*Y+e
        if (a,e)==(0,0): return True
        bit=(X if a>=0 else Y)&1
        a,e=step(a,e,bit); X=Ta(X); Y=Ta(Y)
        if X in (1,2) and Y in (1,2) and n>10 and (a,e)!=(0,0):
            # both in the cycle; relation is frozen up to period 2
            pass
    return (a,e)==(0,0)
bad=0
for k in range(1,6001):
    ix,jx=ij(16*k+1); iy,jy=ij(32*k+1)
    D=(2*iy-jy)-(2*ix-jx)+1
    if chain_absorbs(k)!=(D==0): bad+=1; print("mismatch",k,D)
print("2. chain-absorption <=> D(k)=0 for k<=6000, mismatches:",bad)

# ---- 3. explicit merge classes: both orbits reach a common affine form
def forms(a0,b0,nsteps):
    # orbit of a0*t+b0 as long as parity is forced (a even)
    out=[(a0,b0)]; a,b=a0,b0
    for _ in range(nsteps):
        if a%2: break
        if b%2==0: a,b=a//2,b//2
        else: a,b=3*a,3*b+1
        out.append((a,b))
    return out
for r,s in [(2,4),(6,5),(24,6),(30,6),(8,7),(105,7),(110,7)]:
    fx=forms(16*2**s,16*r+1,400); fy=forms(32*2**s,32*r+1,400)
    common=[f for f in fx if f in fy]
    f=common[0]; tx=fx.index(f); ty=fy.index(f)
    # brute-force check on many t
    good=all( (lambda t: orbit(16*(r+2**s*t)+1)[tx]==f[0]*t+f[1]==orbit(32*(r+2**s*t)+1)[ty])(t) for t in range(0,3000))
    print(f"3. k={r}+{2**s}t : 16k+1 after {tx} steps = 32k+1 after {ty} steps = {f[0]}t+{f[1]}   brute-force ok: {good}")
