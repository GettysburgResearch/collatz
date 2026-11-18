# Uncovered length with arbitrarily many decreasing powers

**Proposed, source-qualified and effective.** In a primitive nontrivial
positive ordinary shortcut cycle of length L, choose k disjoint cyclic
powered factors, each of exponent at least two. Let d count the uncovered
positions. If at most one chosen factor increases, then

    d + log₂(L+1) >= max(L/(4000(k+1)), L^(10/153)/4000),
    d >= 2^(-34) L^(10/153).                                       (1)

The number of decreasing factors and the number of gaps are unrestricted.
More generally, fix a minimum exponent e>=2 and a bound r on the number
of increasing factors. With c=log₂3, gamma=c-1, set

    B=1/(1-c/e),  K=(1+gamma B)^r,
    mu=1-gamma(e+K-1)/(e(e-1)c).

Whenever mu>0 one has, uniformly in k, the roots, and their exponents,

    d+log₂(L+1) >= C_(e,r) max(L/(k+1), L^(10/153)),                 (2)

with an effectively computable positive constant. This includes each
exponent/count pair in the [table for complete tours](MULTIPLE_INCREASING_POWERS.md).
The positive power in (1) consequently holds even for an incomplete
cover fragmented into an unbounded number of disjoint descending pieces.

## Sweeping over the uncovered positions

Use ordinary height H(x)=log₂(x+1), least phase m, Z=log₂(2m+2) and
s=log₂(L+1). The [single-rise proof](ONE_INCREASING_POWER.md)
supplies the physical sign, the entry bound on each powered length
ew<=B H(entry) (with the same bound for any actual exponent >=e),
Z<=16s and a total additive logarithmic correction at most s.
Every uncovered step changes H by at most one. A complete sweep
starting at a boundary of height J therefore has maximum boundary
height at most K(J+d). In fact every individual increase amplifies
H by at most 1+gamma B, every decrease lowers it, and one may charge
all the additive gap lengths before the r amplifications.

If m is in a gap, the next boundary has height <=Z+d. If it is in
an increasing power, its entry height is at most (1+1/(e-c))Z,
by applying the single-rise first-copy bound to this factor alone.
If m is in the last copy of a descending factor of actual exponent b,
root width v and odd count p, use its exit height J. The same local
brackets still give J<=gamma p+Z and bcp<=v+J. Its entry height is
at most K(J+d) by sweeping around from its exit. Thus

    b(v-cp) <= (K-1)J+Kd+s,
    b(b-1)c p <= (b+K-1)J+Kd+s.

Since (b+K-1)/(b(b-1)) decreases in b>=e, this yields

    mu J <= Z+gamma(Kd+s)/(e(e-1)c).

Consequently in all three cases one can take J=O_(e,r)(d+s) and
all boundary heights and individual powered lengths are O_(e,r)(d+s).
If there are no powered factors the result is immediate.

Let P be the sum of increasing powered lengths, W the largest root
width and D the sum of b(v-cp) over the decreases. Then P,W=O_(e,r)(d+s),
since there are at most r increases. The sum of the homogeneous gains
over all the gaps is at most gamma d, even when their number grows.
The total logarithmic correction gives D<=gamma(P+d)+s.
For each descending root w>ch, the [Rhin estimate used for complete
tours](ONE_INCREASING_POWER.md) gives w/(w-ch)<=w^(14.3), also for w=1.
Summing the descending lengths therefore gives

    L <= d+P+D W^(14.3) = O_(e,r)((d+s)^(15.3)).

Alternatively L<=d+k max(powered length). These prove (2).

## Constants for at most one increase

At e=2, r=1 one has B<5, K<4 and mu>1/10, using 19/12<c<485/306.
At the exit of a minimum-containing decrease we accordingly have
J<=10Z+8d+2s<=164s+8d. This bound also covers the gap and rising
cases. Every boundary height is thus <=656(d+s), and each length,
P and W are <=3280(d+s). The deficit satisfies D<=2000(d+s) since
gamma<3/5. With T=d+s>=1, the bounds

    L <= d+3280 kT,     L <= 3281T+2000T(3280T)^(14.3) <= (4000T)^(15.3)

give the first line of (1). For L>=2^512, L^(10/153)>=8000 log₂(L+1):
this holds at 2^512 and the ratio is increasing thereafter. Thus
d>=L^(10/153)/8000 on this range. For smaller L one has
L^(10/153)<2^34 and d>=1 by the [effective exclusion of complete
one-rise covers](ONE_INCREASING_POWER.md) (which uses Barina's
verified initial range). This proves the second line for all L.
