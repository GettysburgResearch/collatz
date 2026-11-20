# Checks for problem (2): E, the certificate map, explicit families, consequences.
def cert(x, extra_loops=0):
    """certificate (A_0..A_r) of an odd x reaching 1, via the odd-to-odd (Syracuse) orbit"""
    assert x%2==1
    A=[0]
    while x!=1:
        y=3*x+1; a=0
        while y%2==0: y//=2; a+=1
        A.append(A[-1]+a); x=y
    for _ in range(extra_loops): A.append(A[-1]+2)
    return A
def holds(x,A):
    r=len(A)-1
    return 3**r*x+sum(3**(r-1-j)*2**A[j] for j in range(r))==2**A[r] and all(A[i]<A[i+1] for i in range(r)) and A[0]==0
def odd_iterates(x,n):
    out=[x]
    for _ in range(n):
        y=3*x+1
        while y%2==0: y//=2
        x=y; out.append(x)
    return out

# 1. every odd x<4000 has a certificate, and extra loops keep it valid; even x never satisfy (1) with r>=1
print("1. certificates valid for odd x<4000:", all(holds(x,cert(x)) and holds(x,cert(x,3)) for x in range(1,4000,2)))

# 2. certificate map in the merging case
def w_certificate(x):
    """x in E, x=128m+1.  Try to build a certificate of w=(x+1)/2 from that of x by the merge rule."""
    w=(x+1)//2; A=cert(x); B=cert_prefix=[0]
    xo=odd_iterates(x,len(A)-1)
    # follow w's odd iterates and look for s with w_s == x_s and B_s == A_s - 1
    y=w; Bs=[0]
    for s in range(1,len(A)+60):
        t=3*y+1; a=0
        while t%2==0: t//=2; a+=1
        y=t; Bs.append(Bs[-1]+a)
        while len(A)<=s: A.append(A[-1]+2); xo.append(1)          # pad x with loops
        if y==xo[s] and Bs[s]==A[s]-1:
            return Bs[:s]+[A[i]-1 for i in range(s,len(A))], s
    return None, None
ok=True; nm=0
for m in range(1,20001):
    if m%4==0: continue
    x=128*m+1; B,s=w_certificate(x)
    if B is not None:
        nm+=1
        if not holds((x+1)//2,B): ok=False; print("map fails",x); break
print(f"2. merge rule (keep length, subtract 1 from the exponents after the merge): {nm} merging x with m<=20000, all output certificates valid: {ok}")
x=257; B,s=w_certificate(x); print("   example x=257:", cert(x), "->  w=129:", B, " merge after", s, "triplings")

# 3. explicit family in the class x = 257 mod 512
bad=0;cnt=0
for q in range(1,60001,2):
    t=27*q+1;b=0
    while t%2==0: t//=2;b+=1
    if t%4==(3 if b%2==0 else 1):      # u' = (-1)^(b+1) mod 4
        cnt+=1
        B,s=w_certificate(256*q+1)
        if B is None or not holds(128*q+1,B): bad+=1
print(f"3. family x=256q+1, 27q+1=2^b u', u'=(-1)^(b+1) mod 4: {cnt} cases (share {cnt/30000:.4f} of odd q), failures {bad}")

# 4. consequence: (2) twice on x_s gives 64q+1, tied to 3^(27s-2)
def orbit_contains(n,target,limit=10**6):
    for _ in range(limit):
        if n==target: return True
        if n==1: return False
        n=n//2 if n%2==0 else 3*n+1
    return False
for s in (1,2,3):
    q=(2**(54*s)-1)//81
    assert (2**(54*s)-1)%81==0 and q%2==1
    xs=256*q+1
    c1=holds(xs,[0,2,4,6,8+54*s])
    w1=(xs+1)//2; w2=(w1+1)//2
    c2=xs%512==257 and w1%512 in (129,385) and w2==64*q+1
    c3=orbit_contains(w2,27*q+1) and orbit_contains(9*q,3**(27*s-1)+1) and orbit_contains(3**(27*s-2),3**(27*s-1)+1)
    print(f"4. s={s}: explicit certificate (0,2,4,6,{8+54*s}) valid: {c1}; residues as required: {c2}; 64q+1 and 3^{27*s-2} share an orbit: {c3}; (3^{27*s-2} does reach 1: {orbit_contains(3**(27*s-2),1)})")

# 5. smallest open-type examples: w still running when x lands
def landing_w(x):
    w=(x+1)//2; p=j=0; t=x
    while t!=1:
        if t&1: t=3*t+1;p+=1
        else: t//=2;j+=1
    q=h=0; ww=w; reached=False
    while h<j-1:
        if ww==1: reached=True
        if ww&1: ww=3*ww+1;q+=1
        else: ww//=2;h+=1
    return p,j,q,ww,reached
out=[]
m=1
while len(out)<5:
    if m%4:
        x=128*m+1; p,j,q,ws,reached=landing_w(x)
        B,s=w_certificate(x)
        if B is None and not reached and ws not in (1,2,4): out.append((x,(x+1)//2,p,j,q,q-p,ws))
    m+=1
print("5. first open-type x: (x, w, triplings of x, halvings of x, triplings of w by then, lead, W*)")
for o in out: print("  ",o)
