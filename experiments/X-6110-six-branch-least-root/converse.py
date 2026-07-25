P=3**12; Q=2**19
A=[7*3**(2*i)*2**(15-3*i) for i in range(6)]; Aset=set(A)
invP=pow(P,-1,Q)
def T(n): return (3*n+1)//2 if n%2 else n//2
def parity(n,L):
    s=[];
    for _ in range(L): s.append(n%2); n=T(n)
    return "".join(map(str,s)), n
print("Test: x in the SHIFTED class x_i + 2^18 (chart-ILLEGAL) still has parity word W_i?")
for i,a in enumerate(A):
    xi=(-a*invP)%Q
    x = xi + (1<<18)                      # chart-illegal shift
    d = (-P*x)%Q
    n = 6*x-5
    W = "110"*(5-i)+"1010"+"110"*i
    p,nn = parity(n,19)
    print(f" i={i}: d(x) in A? {d in Aset:1}   parity==W_i? {p==W}   T^19(n)={nn}  n' odd? {nn%2}  n'=1 mod 6? {nn%6==1}")
print()
print("Test: n = 1 mod 6 whose parity word is W_i W_j  ==> is x legal for >=1 step?  (scan)")
bad=0; good=0
for x in range(1, 400000):
    n=6*x-5
    p,_=parity(n,38)
    for i in range(6):
        for j in range(6):
            if p == "110"*(5-i)+"1010"+"110"*i + "110"*(5-j)+"1010"+"110"*j:
                d=(-P*x)%Q
                if d==A[i]:
                    x2=(P*x+A[i])//Q
                    good += ((-P*x2)%Q == A[j])
                else: bad+=1
print(f"  pairs found: legal-and-matching={good}, parity-matched-but-chart-illegal={bad}")
