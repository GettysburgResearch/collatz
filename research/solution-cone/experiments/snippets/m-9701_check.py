
# M-9701.a: BM94 recursion == coefficient pullback F (shortcut T), exact Z[omega] arithmetic,
# plus 3n-1 control with the twisted identity. Deterministic, stdlib only.
N = 4000
def wmul(x, y):
    (a, b), (c, d) = x, y
    return (a*c - b*d, a*d + b*c - b*d)      # w^2 = -1 - w
W = [(1,0), (0,1), (-1,-1)]
def T(n): return n//2 if n%2==0 else (3*n+1)//2
def U(n): return n//2 if n%2==0 else (3*n-1)//2
import random
random.seed(97)
a = [random.randint(-9, 9) for _ in range(N+1)]
def run(mapT, n_range, twist, shift):
    rhs = {}
    for n in n_range:                          # f(z^6)
        c = rhs.get(6*n, (0,0)); rhs[6*n] = (c[0]+a[n], c[1])
    filt = {}
    for j in range(3):                         # (z^shift/3) sum_j w^(twist j) f(w^j z^2)
        for n in n_range:
            k = 2*n + shift
            coef = wmul(W[(twist*j)%3], wmul(W[(j*n)%3], (a[n],0)))
            c = filt.get(k, (0,0)); filt[k] = (c[0]+coef[0], c[1]+coef[1])
    for k, (x, y) in filt.items():
        assert x%3 == 0 and y%3 == 0
        c = rhs.get(k, (0,0)); rhs[k] = (c[0]+x//3, c[1]+y//3)
    checked = 0
    for m in n_range:                          # LHS: sum_m a_{T(m)} z^{3m}
        t = mapT(m)
        if t > N: continue
        assert rhs.get(3*m, (0,0)) == (a[t], 0), f"mismatch at m={m}"
        checked += 1
    for k, v in rhs.items():                   # fractional powers must cancel
        if k%3 != 0 and k <= 3*N:
            assert v == (0,0), f"nonvanishing non-integral exponent {k}"
    return checked
c1 = run(T, range(0, N+1), twist=1, shift=-1)  # BM94: 1/(3z), filter w^j
c2 = run(U, range(1, N+1), twist=2, shift=+1)  # 3n-1: z/3, filter w^{2j}
print("BM94 identity == pullback F (T):", c1, "coefficients OK")
print("3n-1 control identity == F_U:  ", c2, "coefficients OK")
