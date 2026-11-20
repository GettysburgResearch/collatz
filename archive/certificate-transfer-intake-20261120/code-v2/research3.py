import sys, random, math
sys.path.insert(0,'.')
random.seed(5)
def T(n): return n//2 if n%2==0 else 3*n+1
def A(n): return n//2 if n%2==0 else (3*n+1)//2
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
def lam(n):
    i,j=ij(n); return 2*i-j
def merging(k, cap=10**7):
    """structural merge of 16k+1 and 32k+1: X_n==Y_n with equal tripling counts at some n"""
    X=9*k+1; Y=27*k+2; p=2; q=3; n=0
    while n<cap:
        if X==Y and p==q: return True
        if X in (1,2) and Y in (1,2): return False
        if X&1: X=(3*X+1)//2; p+=1
        else: X//=2
        if Y&1: Y=(3*Y+1)//2; q+=1
        else: Y//=2
        n+=1
    raise RuntimeError

print("== R3a: Lemma 5.1 (consecutive numbers) brute force ==")
bad=0; cnt=0
for Aodd in range(3,400001,2):
    m=Aodd+1; b=0
    while m%2==0: m//=2; b+=1
    u=m
    if u%4==(1 if b%2==0 else 3):
        cnt+=1
        target=(3**b*u-1)//2
        oa=orbit(Aodd); ob=orbit(Aodd-1)
        # same number of steps to the target, and target on both orbits
        if not (target in oa and target in ob and oa.index(target)==ob.index(target)): bad+=1
print(f"   odd A<=400001 satisfying the condition: {cnt} (share {cnt/200000:.4f}); failures: {bad}")

print("== R3b: Proposition 5.2 family (k=2q) brute force ==")
bad=0; cnt=0; tot=0
for q in range(1,200001,2):
    tot+=1
    m=9*q+1; b=0
    while m%2==0: m//=2; b+=1
    u=m
    if u%4==(1 if (b-1)%2==0 else 3):
        cnt+=1
        target=(3**(b+1)*u-1)//2
        o1=orbit(32*q+1); o2=orbit(64*q+1)
        if not(target in o1 and target in o2 and o2.index(target)==o1.index(target)+1): bad+=1
        if not merging(2*q): bad+=1
print(f"   odd q<=200001 in the family: {cnt} of {tot} (share {cnt/tot:.4f}); failures: {bad}")

print("== R3c: odd family k=16t+9, t even: X_4=81t+47, Y_4=81t+46 ==")
bad=0; cnt=0
for t in range(0,40000,2):
    k=16*t+9
    X=9*k+1; Y=27*k+2
    for _ in range(4): X=A(X); Y=A(Y)
    if (X,Y)!=(81*t+47,81*t+46): bad+=1
    m=81*t+48; b=0
    while m%2==0: m//=2; b+=1
    if m%4==(1 if b%2==0 else 3):
        cnt+=1
        if not merging(k): bad+=1
print(f"   t even < 40000 satisfying the Lemma 5.1 condition: {cnt}; failures: {bad}")

print("== R2: smallest k with D(k) = -1, -2, +1, +2 and their data ==")
found={}
k=1
while len(found)<4 and k<200000:
    D=lam(32*k+1)-lam(16*k+1)+1
    if D in (-1,-2,1,2) and D not in found:
        found[D]=k
    k+=1
for D,k0 in sorted(found.items()):
    ix,jx=ij(16*k0+1); iy,jy=ij(32*k0+1)
    print(f"   D={D:+d}: k0={k0}  16k0+1={16*k0+1} (triplings {ix}, halvings {jx}, level {2*ix-jx})   32k0+1={32*k0+1} (triplings {iy}, halvings {jy}, level {2*iy-jy})")

print("== R2b: local normal form check: n0+2^S m  and  2^(S+lam(n0)) m + 1 reach a common value ==")
bad=0
for _ in range(300):
    n0=random.randrange(1,5000); i,j=ij(n0); S=j+random.randrange(0,6); m=random.randrange(1,10**6)
    common=1+3**i*2**(S-j)*m
    o1=set(orbit(n0+2**S*m))
    L=S+2*i-j
    if L<0: continue
    o2=set(orbit(2**L*m+1))
    if not(common in o1 and common in o2): bad+=1
print("   failures:",bad)
