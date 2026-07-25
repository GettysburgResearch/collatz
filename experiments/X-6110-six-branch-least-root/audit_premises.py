"""Independent check of the two 'native ghost' examples supplied in the task brief.

Neither is used by any 61xx claim; this script exists so the premises are audited rather
than assumed.
"""
from fractions import Fraction as F


def T(x):
    """Shortcut Collatz on rationals with odd denominator; parity = parity of numerator."""
    return (3*x + 1)/2 if x.numerator % 2 else x/2


def affine(word):
    """T^L(n) = (alpha n + beta)/2^L on the class realising the parity word."""
    alpha, beta, t = 1, 0, 0
    for ch in word:
        if ch == '1':
            alpha, beta = 3*alpha, 3*beta + 2**t
        t += 1
    return alpha, beta, t


# --- claim 1: parity word (1110)^inf  ->  T^4(x) = (27x+19)/16, unique realisation -19/11
alpha, beta, t = affine("1110")
print(f"word 1110: T^4(x) = ({alpha}x + {beta})/2^{t}      claimed (27x+19)/16 : "
      f"{(alpha, beta, t) == (27, 19, 4)}")
x = F(beta, 2**t - alpha)   # (alpha x + beta)/2^t = x  =>  x = beta/(2^t - alpha)
print(f"fixed point x = {x}                        claimed -19/11      : {x == F(-19, 11)}")
orbit = [x]
for _ in range(4):
    orbit.append(T(orbit[-1]))
print(f"orbit: {' -> '.join(map(str, orbit))}")
print(f"closes after 4 steps: {orbit[0] == orbit[4]};  "
      f"claimed -19/11,-23/11,-29/11,-38/11 : "
      f"{orbit[:4] == [F(-19,11), F(-23,11), F(-29,11), F(-38,11)]}")
print(f"multiplier 27/16 = {27/16:.4f} > 1, so any positive realisation would grow: True")

# --- claim 2: H-subsystem ghost g_r = -2^(3r+2)/(3^(2r+1) - 2^(3r+2)); g_3 = -2048/139
print("\n(the H formula is negative exactly when 3^(2r+1) > 2^(3r+2), i.e. r >= 3;"
      " the brief restricts to r >= 3, and r = 2 is shown here only as the boundary)")
for r in (2, 3, 4):
    g = F(-2**(3*r+2), 3**(2*r+1) - 2**(3*r+2))
    print(f"g_{r} = {g}" + ("   claimed -2048/139 : %s" % (g == F(-2048, 139)) if r == 3 else ""))

# --- T-6140(A) consistency: the general cycle window, in the PHYSICAL coordinate n,
#     must contain the six-branch chart window T-6103(b) pushed forward by n = 6x-5.
from fractions import Fraction as Fr
L, k = 19, 12
den = 2**L - 3**k                      # = -7153
lo_gen = Fr(3**k - 2**k, den)
hi_gen = Fr(2**(L-k)*(3**k - 2**k), den)
A6 = [7*3**(2*i)*2**(15-3*i) for i in range(6)]
# chart-coordinate window of T-6103(b) ...
lo_chart, hi_chart = Fr(-A6[5], 7153), Fr(-A6[0], 7153)
# ... pushed to the physical coordinate
lo_phys, hi_phys = 6*lo_chart - 5, 6*hi_chart - 5
print("\nT-6140(A) vs T-6103(b) consistency (both in the physical coordinate n = 6x-5):")
print(f"  general (L,k)=(19,12) window : [{float(min(lo_gen,hi_gen)):.2f}, {float(max(lo_gen,hi_gen)):.2f}]")
print(f"  six-branch window pushed fwd : [{float(lo_phys):.2f}, {float(hi_phys):.2f}]")
print(f"  six-branch window is contained in the general one: "
      f"{min(lo_gen,hi_gen) <= lo_phys and hi_phys <= max(lo_gen,hi_gen)}")
# and the six-branch kappa_i are exactly the c_w of the general formula
print(f"  kappa_0 = 35765+6*a_0 = {35765+6*A6[0]}  equals c_w for word W_0 : "
      f"{35765+6*A6[0] == 1412021}   x_w = {Fr(1412021, den)} = {float(Fr(1412021,den)):.2f}")
