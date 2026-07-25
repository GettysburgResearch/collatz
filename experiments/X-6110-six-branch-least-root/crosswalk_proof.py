# Exact certificate for T-6101: each digit a_i <-> the parity word W_i = (110)^(5-i) 1010 (110)^i.
P=3**12; Q=2**19
A=[7*3**(2*i)*2**(15-3*i) for i in range(6)]
invP=pow(P,-1,Q)

def word_affine(w):
    """T^L(n) = (alpha*n + beta)/2^L on the unique class r mod 2^L realising parity word w."""
    alpha, beta, t = 1, 0, 0
    r = 0; mod = 1                      # residue class of n mod 2^t forced so far
    for ch in w:
        b = int(ch)
        # current value is (alpha*n+beta)/2^t ; its parity must be b
        # (alpha*n+beta)/2^t = m ; need m = b mod 2  ->  alpha*n + beta = b*2^t mod 2^(t+1)
        need = (b*pow(2,t) - beta) * pow(alpha, -1, 2**(t+1)) % 2**(t+1)
        r, mod = need, 2**(t+1)
        if b: alpha, beta = 3*alpha, 3*beta + 2**t
        t += 1
    return alpha, beta, t, r, mod

print("i |  W_i                 | alpha | beta=kappa_i | 35765+6a_i | class r_i mod 2^19 | (6x-5) for x=-a_i/P mod 2^19")
allok=True
for i,a in enumerate(A):
    W = "110"*(5-i) + "1010" + "110"*i
    alpha,beta,t,r,mod = word_affine(W)
    x = (-a*invP)%Q
    n = (6*x-5) % Q
    ok = (alpha==P and t==19 and mod==Q and beta==35765+6*a and r==n)
    allok &= ok
    print(f"{i} | {W} | {alpha} | {beta:>10} | {35765+6*a:>10} | {r:>7} | {n:>7}  ok={ok}")
print("\nALL SIX BRANCH CERTIFICATES VALID:", allok)
print("ones in each W_i:", [("110"*(5-i)+"1010"+"110"*i).count('1') for i in range(6)])
print("number of length-19 parity words with 12 ones starting '1' = C(18,11) =", __import__('math').comb(18,11))
print("digit density of the six-branch chart : 6/2^19 =", 6/2**19)
print("digit density of the FULL (12,19) chart: 31824/2^19 =", 31824/2**19)
