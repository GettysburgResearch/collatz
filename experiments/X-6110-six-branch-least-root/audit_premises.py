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
