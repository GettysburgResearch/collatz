# Exact finite harmonic flow tests with unrestricted positive masses

Let T be the ordinary shortcut map. Fix any finite modulus and any
finite list of the following functions, allowing separate coefficients
or indicator masks on its residue classes:

* real and imaginary parts of n^(s+it), with s,t real;
* log n;
* real Laplace samples z^n with fixed 0<z<1.

For arbitrarily high floors M there is a finitely supported positive
measure μ on distinct ordinary ternary units n≥M such that

    Σ_n μ(n) (f(T(n))−f(n)) = 0

for **all** the tests, although the full measure is not invariant.
In particular finite Mellin samples and real Laplace samples can hold
together with exact logarithmic winding. The weights are positive
real numbers. When the entire list has rational values they can be
taken to be positive integers, allowing multiplicity. This differs
from [the exact finite cyclotomic construction with unit weights](CYCLOTOMIC_MOMENTS.md).
Indeed a single exact real Laplace evaluation can encode the entire
flow for distinct sources with *unit* mass, as shown there.

## Closed residue paths and eventual monotonicity

Use the strongly connected ternary-unit graph modulo H=lcm(Q,6)
from the linked proof. Each finite edge path lifts to arbitrarily
large ordinary sources in an arithmetic progression. For clarity,
with 2^a exactly dividing H, choose a terminal binary residue for
the prescribed path, then undo each letter in the binary integers
by n=(2y−e)/3^e, e the prescribed parity. The edge congruences give
the required residues modulo 2^a at each step; the parity is automatic.
Select an ordinary source agreeing with this lift to precision a+l,
where l is the length of the path, and with the prescribed starting
odd-part residue modulo H/2^a. The Chinese remainder theorem gives the
progression, the correct binary itinerary and all the odd-part labels.
All intermediate states tend to infinity with the source.

Every residue r admits a finite closed path of slope greater than
one by going to −1, repeating its odd loop and returning. It also
admits a closed path of slope less than one via repeated 1→2→1
loops. Thus if V(T(n))≥V(n) for all sufficiently large ternary
units, and V restricted to r is eventually nondecreasing in n,
the contracting return forces V constant along r between its
terminal value λn+O(1) and n, with λ<1. These intervals along the
fixed source progression overlap and cover a tail. An eventually
nonincreasing restriction uses the expanding return instead. If all
residue restrictions are eventually monotone, the constants agree
by strong connectivity. This argument by itself treats a broad
class of real potentials but does not assume oscillatory Mellin
terms are monotone.

## Oscillatory terms

For a real linear combination V of the tests collect equal real
Mellin exponents σ. On residue r their contribution is n^σ A_r(g(log n)),
where g(u)=(t_1u,...,t_du) modulo 2π and A_r is continuous on the
compact torus subgroup G given by the closure of this one-parameter
group. Use the same G for all terms and normalized Haar measure.
Along any fixed unbounded arithmetic progression, g(log n)
has every point of G as a subsequential limit. The forward real
flow has dense tails in G by compactness and recurrence, and the
mesh of logarithms of successive terms of the progression tends
to zero. Write h_r=1/2 or 3/2 for the branch slope.

Assume V(T(n))−V(n)≥0 on the entire sufficiently large tail.
First consider a largest positive exponent σ with nonzero
coefficient. Divide by n^σ and take limits on each residue edge.
For all x∈G the limit inequality is

    h_r^σ A_s(x+g(log h_r))−A_r(x) ≥ 0.                              (1)

Translation invariance gives the same inequality for Haar means.
The expanding −1 and contracting 1-cycles force opposite signs
on their means, and paths −1→r→1 force all means to vanish.
Each nonnegative continuous difference in (1) then vanishes
identically. On the −1 loop, boundedness and h^σ≠1 force A_(-1)=0,
and connectivity gives A_r=0 everywhere. Repeat to eliminate all
positive exponents.

Next, the coefficients of log n must be nondecreasing across
all residue edges by dividing by log n, hence equal to a common c.
Let A_r now denote the exponent-zero coefficients, or zero if that
exponent is absent. At bounded order the limiting inequality is

    A_s(x+g(log h_r))−A_r(x)+c log h_r ≥ 0.

After Haar integration sum on the two opposite-slope loops. This
forces c=0; the remaining means are nondecreasing along every
edge, hence equal. Again the continuous differences vanish.
Each closed path now gives invariance of A_r under translation by
g of its log slope. Compare the closed path via −1 having one
extra odd loop to the same path without that loop. Similarly insert
one two-step 1-cycle on a closed path via 1. Thus A_r is invariant
under translations by g(log(3/2)) and g(log(3/4)). These two real
logarithms generate a dense subgroup of the real line, by the
multiplicative independence of 2 and 3. Their images generate
a dense subgroup of G. Continuity and connectivity force a single
constant, which may be subtracted from V.

For a remaining negative exponent σ, take the largest such one
and repeat (1); all real Laplace terms are negligible. The order
of the endpoint signs reverses, so use paths 1→r→−1 to set the
means to zero. Boundedness on the same −1 loop still applies
because h^σ≠1. After removal of the finite exponent list, only
finite sums of decaying real exponentials remain. On each residue
such a sum is eventually monotone, as is seen from its largest
base with nonzero coefficient. The closed-path argument above
makes it constant on the tail. Thus every nonnegative tested drift
under consideration vanishes eventually.

## Positive finite realizations

The spans of the real vectors d(n)=(f(T(n))−f(n))_f over all
ternary units n≥M eventually stabilize as M increases, by finite
dimension. Beyond stabilization, any functional that vanishes on
all sufficiently large n annihilates the full tail span. Thus,
for every such M, every functional nonnegative on the tail
vectors annihilates them all. Their finite positive cone equals
their span by [the finite-dimensional separation argument](CYCLOTOMIC_MOMENTS.md).
Include any even ternary unit n in [M,2M) with positive weight,
then compensate its vector by a finite nonnegative combination of
other tail vectors. The measure is not invariant because this
edge lands below M. When all vector coordinates are rational,
finite rational feasibility and clearing denominators give integer
weights. This reasoning does not assert unit weights or exact
pointwise flow of the supports.
