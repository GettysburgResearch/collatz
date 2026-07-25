"""X-6200 step 3: a closed-form model for the coverage deficit, tested against the data.

A backward step is either  n -> 2n  (always available) or  n -> (2n-1)/3  (available iff
n = 2 mod 3, density 1/3), multiplying the value by 2 and by ~2/3 respectively.  So a depth-d
tree path with b rare steps ends near

        2^(d-b) * (2/3)^b  =  2^d * 3^(-b),

and the number of such paths is about C(d,b) 3^(-b)  (choose which b steps take the rare
branch, each available with density 1/3).  Summing over b gives (4/3)^d, the branching factor.

A node is <= X iff 2^d 3^(-b) <= X, i.e. b >= b_min(d) = (d - log2 X)/log2 3.  Hence

        coverage(d, X)  ~  sum_{b >= b_min(d)}  C(d,b) 3^(-b) .

This file tests that prediction against the exact measurement.
"""
import math
from math import comb, log2

X = 10**8
L = log2(X)
L3 = log2(3)

rows = [l.split() for l in open('results/coverage_1e8_fine.txt') if not l.startswith('#')]
data = dict((int(r[0]), int(r[1])) for r in rows)


def predict(d):
    bmin = max(0.0, (d - L)/L3)
    b0 = math.ceil(bmin - 1e-12)
    return sum(comb(d, b) * 3.0**(-b) for b in range(b0, d+1))


print(f"X = {X:,},  log2 X = {L:.2f},  b_min(d) = (d - {L:.2f})/{L3:.4f}\n")
# coverage(d) is CUMULATIVE, so the model must be summed over depths too.
cum, model = 0.0, {}
for d in range(0, max(data)+1):
    cum += predict(d)
    model[d] = cum
norm = data[24]/model[24]            # ONE constant, fitted once, at d = 24

print(f"cumulative model, normalised once at d = 24 (factor {norm:.4f})\n")
print(f"{'d':>5} {'measured':>13} {'model':>14} {'model/meas':>11} {'coverage as X^e':>16}")
for d in (16, 24, 32, 40, 48, 56, 64, 80, 100, 120, 160, 300, 592):
    if d not in data:
        continue
    m = data[d]
    print(f"{d:>5} {m:>13,} {model[d]*norm:>14,.0f} {model[d]*norm/m:>11.3f}"
          f" {math.log(m)/math.log(X):>16.3f}")

print("""
VERDICT: the model tracks the measurement to within 10% while coverage is below about X^0.66,
and then over-predicts, saturating at 4.67x too high -- it claims 4.7*10^8 nodes below 10^8,
which is impossible.  So the first-order value estimate 2^d 3^(-b) UNDERSTATES the escape: many
more tree nodes leave [1,X] than it predicts.  The deficit is real and is not captured by the
leading-order random-walk picture.  Domain of validity: coverage <~ X^0.66.""")
