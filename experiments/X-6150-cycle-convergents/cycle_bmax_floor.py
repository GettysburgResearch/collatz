"""min{ j : Bmax(j) >= B } from the continued fraction of log2(3), for B = 2^71.

A positive cycle with minimum m: T^L(m) >= m for all L, and 2^q > 3^k, so there is a first
L0 <= q with 3^(k_L0) < 2^L0.  Below L0 the word is above the line, so it qualifies for
Bmax(L0), and T^L0(m) >= m gives m <= Bmax(L0).  Hence Bmax(L0) >= m >= B and q >= L0.

Bmax(j) = (1/3) G(k) r/(1-r) <= (1/3) k r/(1-r)  since every term of G is <= 1.  The upper
bound is what a floor needs, and it is exactly T-6141(b)'s  m <= k 2^q/(3(2^q - 3^k)).
"""
from fractions import Fraction

# --- log2(3) to 360 bits, by fixed-point squaring (integers only) -------------------------
BITS = 400
y = (3 << BITS) // 2
bits = []
for _ in range(BITS - 40):
    y = (y * y) >> BITS
    if y >= (2 << BITS):
        bits.append(1); y >>= 1
    else:
        bits.append(0)
L23 = Fraction((1 << len(bits)) + int(''.join(map(str, bits)), 2), 1 << len(bits))
ERR = Fraction(1, 1 << (len(bits) - 8))      # generous bound on |L23 - log2 3|

a, b, cf = L23.numerator, L23.denominator, []
while b and len(cf) < 34:
    cf.append(a // b); a, b = b, a % b

conv, h1, h0, k1, k0 = [], 1, 0, 0, 1
for t in cf:
    h1, h0 = t * h1 + h0, h1
    k1, k0 = t * k1 + k0, k1
    conv.append((h1, k1))

# --- one-sided best approximations from below: delta = p - q*log2 3 > 0 --------------------
LIM = 5 * 10**11
cands = set()
for i, (p, q) in enumerate(conv):
    if p - q * L23 > 0 and p <= LIM:
        cands.add((p, q))
    # intermediate fractions p_i + t*p_{i+1}
    if i + 1 < len(conv):
        p2, q2 = conv[i + 1]
        t = 1
        while p + t * p2 <= LIM:
            pp, qq = p + t * p2, q + t * q2
            if pp - qq * L23 > 0:
                cands.add((pp, qq))
            t += 1
            if t > 200: break
# multiples of the best ones (delta scales, Bmax stays flat, but include for completeness)
base = sorted(cands)
for p, q in base:
    g = 2
    while g * p <= LIM and g <= 60:
        cands.add((g * p, g * q)); g += 1
top = [x for x in base if x[0] > 10**7][:40]
for p1, q1 in top:                       # sums among the large generators
    for p2, q2 in top:
        if p1 + p2 <= LIM:
            cands.add((p1 + p2, q1 + q2))

LN2 = Fraction(6931471805599453, 10**16)
rows = []
for p, q in sorted(cands):
    d = p - q * L23                      # = delta_j, exact up to ERR*q
    if d <= 0:
        continue
    # Bmax(j) <= k/(3(1-2^-delta)),  1-2^-delta >= delta*ln2 - (delta*ln2)^2/2
    x = d * LN2
    onemr_lo = x - x * x / 2
    if onemr_lo <= 0:
        continue
    rows.append((p, q, float(d), float(Fraction(q, 3) / onemr_lo)))

rows.sort()
B = 2**71
run, best = 0.0, None
records = []
for p, q, d, ub in rows:
    if ub > run:
        run = ub; records.append((p, q, d, ub))
        if best is None and ub >= B:
            best = (p, q, d, ub)

print("records of the upper bound on Bmax (one-sided best approximations only):")
print("%14s %14s %12s %14s" % ("j", "k", "delta", "Bmax <= "))
for p, q, d, ub in records[-10:]:
    print("%14d %14d %12.4e %14.6e" % (p, q, d, ub))
print()
print("B = 2^71 = %.6e" % B)
if best:
    p, q, d, ub = best
    print("first j with Bmax(j) >= B : j = %d  (k = %d, delta = %.4e, bound %.6e)" % (p, q, d, ub))
    print()
    print("=> every positive cycle has  q >= L0 >= %d  shortcut steps" % p)
    print("   T-6141(g) best route at B = 2^71 :   q >= 1.0377e11")
    print("   ratio: %.4f" % (p / 1.0377e11))
else:
    print("no candidate reached B within j <= %d" % LIM)

allowed = sorted(p for p, q, d, ub in rows if ub >= B and p <= 2 * 10**12)
print()
print("candidates examined:", len(rows))
print("allowed periods q <= 2e12 :", allowed, " count:", len(allowed))
print("primitive:", [a for a in allowed if not any(a % b == 0 and b < a for b in allowed)])
