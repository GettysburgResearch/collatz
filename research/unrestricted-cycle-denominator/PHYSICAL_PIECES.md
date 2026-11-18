# A primitive circular list of long physical pieces

Fix any modulus Q≥1. There exist cyclic lists of distinct positive
ordinary ternary units n_0,...,n_(L−1) with these simultaneous
properties, writing c=log₂3, K for their odd count and δ=L−cK:

* gcd(L,K)=1, 0<δ≍_Q 1/L, all heights are comparable to L²,
  and the gap between distinct heights is at least a constant times L.
* Every successor is correct modulo Q. For all but o(L) edges
  one has the exact integer equality T(n_i)=n_(i+1).
  The maximum absolute error on the other edges can be bounded by
  any prescribed function of L tending to infinity, on a suitable
  sequence of lengths. At least one edge is incorrect.
* The first ordinary moment balances exactly: Σ_i T(n_i)=Σ_i n_i.
  The ordinary winding residual is O_Q(2^h/L³), where h is the
  slowly increasing number of letters per physical piece below.

This separate construction imposes order on individual ordinary
steps. Higher exact cyclotomic jets and superpolynomial winding
accuracy were obtained on a [different family](WINDING_PRECISION.md).

## A coprime positive-drift schedule with an integral local model

Let M be the lcm of p−1 over primes p≥5 dividing Q (use M=1 for an
empty set). There are infinitely many coprime pairs (L,K)≡(1,0)
modulo M with δ positive and comparable to 1/L. To verify this,
write C_i=(p_i,q_i) for convergent columns of c, taking those with
p_i−q_i c>0. The unimodular adjacent columns give a solution modulo
M to u C_i−v C_(i−1)≡(1,0). Choose 1≤v≤M in its residue class,
and choose u>2v in its prescribed class coprime to v. At primes
common to M and v the prescribed u is already a unit, since the
target vector is primitive. At the remaining prime factors of v
specify u≡1 and apply the Chinese remainder theorem. Both coefficients
may be bounded in terms of M alone. Put (L,K)=u C_i−v C_(i−1).
The errors add with the same sign and the previous error is comparable
to 1/q_i, as in the [winding note](WINDING_PRECISION.md). This proves
the claim. In particular D=2^L−3^K is coprime to 6Q, since D≡1
at the prime factors of Q at least five.

For the cyclic mechanical schedule take the letters
floor((j+1)K/L)−floor(jK/L). Its rotations are all the intercepts
t/L for 0≤t<L in this floor formula. In any contiguous segment of
length l≤L its odd count differs from lK/L by less than one.
Consequently its homogeneous multiplier 3^w/2^l is bounded above
and below by absolute positive constants for large L. The full
affine translation is a sum of K half-suffix multipliers, hence
comparable to L. The unique positive rational fixed points x_i
at all the phases are therefore comparable to L/(1−3^K/2^L),
which is comparable to L². Their denominators divide D, so
they define unambiguous integer residues at every prime of 6Q.
In particular they realize their 2-adic parity schedules; for the
first bit this follows by reducing the fixed-point numerator modulo
two, and rotations give the rest. They are ternary units since one
odd step produces a unit and every subsequent step preserves units.

Consecutive intercepts t/L and (t+1)/L for 0≤t<L−1 change precisely
one interior prefix floor, at an index 1≤p<L. Thus one adjacent
01 changes to 10, uniformly in this direction, and all other letters
agree. The absolute affine numerator difference is
2^(p−1)3^(suffix odd count), since the pair numerators differ by
one. This is comparable to 2^L by the balanced prefix bound and
3^K≍2^L. The rational initial values at these consecutive intercepts
are monotone, separated by a quantity comparable to 2^L/D≍L.
All distinct phases are therefore separated by at least c_Q L.
Moreover they cannot form an ordinary cycle: if integral, every
numerator would be divisible by D whereas this adjacent difference
is coprime to D>1. The use of mechanical words as extrema for
rational cycles is classical. [Halbeisen and Hungerbühler](https://people.math.ethz.ch/~halorenz/publications/pdf/collatz.pdf)

## Rounding at the joins and balancing their total error

Write Q'=lcm(Q,3). First fix h, cut into floor(L/h) blocks of
length h and at most one shorter terminal block. At each starting
phase x choose an integer lift n≡x modulo 2^h Q' with
n−x=2^h Q' β, |β|≤1/2. Iterate the ordinary map inside that
block. Its letters agree with the reference, and each state
difference equals the starting difference times the homogeneous
multiplier through the prefix. The errors at every phase are
O_Q(2^h), and every discrepancy at a join is an integer multiple
of Q'. The same remains true if each β is shifted by a bounded
integer.

For the full blocks the two odd counts are a=floor(hK/L) and a+1.
The error in their combined end-minus-start displacement, in units
of Q', is the sum of (3^w−2^h)β over blocks of count w. A short
block of length l contributes 2^(h−l)(3^w−2^l)β. The reference
displacements of all blocks sum to zero. For each of the two full
classes alter β at individual entries by 0 or ±1 so that its class
sum has absolute value at most 1/2. This is possible because
the original sum has absolute value at most half its class size.
The resulting total displacement divided by Q' is an integer of
size O(2^h), including the possible short block. The coefficient
bound for that block follows from its bounded multiplier.

The two integers d_0=3^a−2^h and d_1=3^(a+1)−2^h are odd and
coprime: d_1−3d_0=2^(h+1). Any integer y of size O(2^h) can be
written d_0 u+d_1 v=y with |u|,|v|=O(2^h). Choose u a smallest
absolute residue modulo |d_1|, then bound v by
|d_0|/2+|y|/|d_1|. For fixed h each full class has a positive
limiting fraction: its upper class fraction tends to the fractional
part of h/c, strictly between zero and one, by counting the total
ones over the full blocks. Thus for sufficiently large L the
negative residual is cancellable by further shifts ±1 spread over
distinct blocks of each class. All β remain bounded by 5/2 and
the sum of all physical end-minus-start displacements is exactly
zero. This is the asserted first moment, with the last true output
of each block included in the displacement even when it differs
from the next chosen lift.

Take h successively larger and choose L at each stage so large
that the preceding counts suffice, 2^h=o(L), and the prescribed
diverging error bound dominates the constant times 2^h. The
reference gaps imply distinctness, with gaps still comparable
from below to L. Only the O(L/h+1) joins can fail. At one of
them equality must fail, since the full mechanical parity word
has no ordinary realization. Also the lifted set is not invariant
even under a different permutation: its spacing is much larger
than any join error. Finally the derivative of log(1+1/(3x)) on
this shell is O_Q(L^(−4)), which gives the winding error by summing
the lifted phase errors over the odd states.
