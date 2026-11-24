from fractions import Fraction as F
from itertools import product
from math import comb

# Rational interval for log(x); no floating-point enters the certificate.
def log_bounds(x, n=24):
    x = F(x)
    if x < 1:
        lo, hi = log_bounds(1/x, n)
        return -hi, -lo
    z = (x-1)/(x+1)
    s = 2*sum((z**(2*j+1)/F(2*j+1) for j in range(n)), F(0))
    return s, s + 2*z**(2*n+1)/(F(2*n+1)*(1-z*z))

def psi_bounds(c):
    lo1, hi1 = log_bounds(1+c)
    lo2, hi2 = log_bounds(c)
    return (1+c)*lo1-c*hi2, (1+c)*hi1-c*lo2

def require(x):
    if not x:
        raise AssertionError('exact arithmetic check failed')

# 3/2 < alpha < 317/200, and alpha > 15849/10000.
require(3**2 > 2**3 and 3**200 < 2**317)
require(3**10000 > 2**15849)
l3, u3 = log_bounds(3)
# The low-clock exponent is <= 1-308/317+Psi(13/24)/log(3) < 47/50.
require(psi_bounds(F(13,24))[1] < (F(308,317)-F(3,50))*l3)
# The existing critical exponent exceeds 47/50.
require(psi_bounds(F(5849,10000))[0] > F(47,50)*u3)

# Finite carry vectors; the last carry is recovered from phase, clock,
# first carry and the sum of the first m carries.
words = 0
for m in range(1,5):
    seen = {}
    for b in product(range(1,4), repeat=m):
        for k in product(range(3), repeat=m+1):
            g = tuple(b[i]+3*k[i]-k[i+1] for i in range(m))
            if min(g) < 1:
                continue
            A, B, S = sum(g), sum(b), sum(k[:-1])
            require(A+k[-1] == B+2*S+k[0])
            require(k[-1] == B+2*S+k[0]-A)
            if k[0] == 0 and b[0] == 1:
                require(k[1] == 0)
            key = (b,A,k[:-1])
            require(key not in seen or seen[key] == g)
            seen[key] = g
            words += 1

# Check the number of weak compositions of total at most s.
compositions = 0
for m in range(1,6):
    for s in range(8):
        count = sum(sum(v)<=s for v in product(range(s+1),repeat=m))
        require(count == comb(m+s,m))
        compositions += 1

print('Exact exponent inequalities: PASS (0.94 < critical; carry bound < 0.94)')
print('Legal finite carry-word cases:',words)
print('Weak-composition count cases:',compositions)
