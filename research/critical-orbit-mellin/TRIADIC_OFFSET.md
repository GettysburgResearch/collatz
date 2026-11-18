# The raw translated offset cone at each fixed triadic rational phase

**Proposed, source-qualified.** For each fixed u=m/3^k in [0,1), use
the nonnegative raw cone S_Q^u of the [affine coarea formula](OFFSET_COAREA.md).
Every positive ordinary orbit is eventually periodic if and only if

    liminf_(Q→∞) S_Q^u([theta,1])/Q = 0 for every 0<theta<1.

In the eventual-periodic direction the limits are zero. A single
escaping orbit forces a positive lower limit at every one of these
phases for one common threshold, with constants allowed to depend
on k. This result includes the raw arithmetic phase u=0.

Write P=2·3^Q. Translating by uP preserves the odd grid and all
congruences modulo 3^(Q-k). Thus the first N=Q-k reverse steps at
the translated target t are an actual positive odd path ending
backwards at x, with t=Jx+F. The remaining k reverse exponents
need not be legal there. Their slope-sum over all possibilities
is 3^k and their offsets are at most C_k=(3/2)^k-1. Their final
distortion at t is F/t+(J/t)F_tail, where J/t<=1/x.

If the genuine prefix is simple, the [uniform reciprocal packing and
physical cone criterion](HARMONIC_OFFSET_CONE.md) shows that avoiding
all vertices <=R makes F/t uniformly small as R grows. It also gives
C_k/x<=C_k/R. Thus for fixed theta any marked simple prefix visits
a bounded state. If all orbits eventually cycle, their targets lie
in a fixed finite set. The sum over all such prefixes and extensions
is O_(theta,k)(1) by the pointwise bounds on g_N(t).

A nonsimple prefix ends on an ordinary odd cycle C of period d<=N.
Let p_C be the density of its basin, with sum over cycles at most one.
At any t on C a first-hit layer of fixed depth contributes at most
K p_C to the slope-sum divided by t for an absolute K. Indeed
J/t<=1/x. The nonperiodic unit first-hit sources are an antichain,
whose pairwise disjoint predecessor basins each have density >=c/x
and all lie inside the basin of C. Nonunits at a nonzero depth
inject via x→4x+1 into the same first-hit layer of units, with loss
at most five in reciprocal weights. There is at most one periodic
source at that depth, itself a unit with 1/x<=p_C/c. Depth zero
uses the same individual bound. This refines the [ordinary first-hit
estimate](../native-pressure-20261118/ORDINARY-DENSITIES.md) by retaining
the enclosing basin mass. Appending full laps costs a multiplier <1,
hence g_N(t)/t<=K(1+N/d)p_C. Summed over all d targets on C and divided
by Q this costs at most 2K p_C. For each fixed cycle the contribution
tends to zero by the pointwise boundedness of g_N(t). Dominated
convergence over the cycles, including the fixed suffix factor 3^k,
makes the entire normalized repeated-prefix contribution vanish.

Conversely fix an escaping odd unit n and y_j=U^j(n). Retain
M=Q-k-1 genuine reverse steps at y_j through n, terminating at a
unit x; restrict to 1<=j<M. Shifting back the target to its unshifted
class t_w=y_j-uP modulo P changes this final ancestor by a multiple
of three: explicitly the shift is -2^(A+1)3m, up to multiples of
3^(k+1), where A is the total retained valuation. Thus the required
starting class for the remaining k+1 inverse letters is still a
ternary unit. It admits a continuation with every exponent at most
six: at a unit residue choose an exponent giving an integral unit
parent, using that 2 generates the units modulo 9, and continue
one digit at a time (equivalently lift the starting class to an odd
positive unit and work at that lift). Its slope is bounded below by
(3/64)^(k+1). The completed word at phase u has target y_j itself,
since 0<y_j<P for all j<=Q at sufficiently large Q.

The genuine prefix contributes F/y_j>=1/(3n+1) for j>=1, and completion
only increases the offset. Provided x>C_(k+1), the total offset remains
below y_j since the truncated comparison is F+Jx=y_j. For all large
M-j this lower bound on x is automatic: each of the finitely many
small states reaching the nonperiodic n has a unique depth to n.
Unit ancestors supply at least one fifth of g_(M-j)(n): replacing
any nonunit x by 4x+1 retains its odd successor and divides its slope
by four, injectively, when M-j>=1. Distinct completed words are
counted separately, with disjoint targets as j varies. Consequently
the lower bound divided by Q is at least a fixed positive constant
times the Cesàro mean of g_l(n), since the slope from n to y_j
divided by y_j is bounded below by the simple-path correction product.
The canonical fixed-root mean is positive, proving the converse.

## One compact null carrier for every triadic phase

If an escaping unit n exists, there is a single compact Lebesgue-null set
E inside (0,1) such that liminf_Q S_Q^u(E)/Q>0 at **every** triadic
rational u. At almost every real u one has S_Q^u(E)=0 at every depth,
by exact coarea and countability of the depths.

Indeed let K_n denote the compact null carrier of corrections from
ordinary unit ancestors x to n, as in the [arithmetic zero-phase
argument](OFFSET_COAREA.md), and let L_j be the correction from n
to y_j=U^j(n). For j>=1 these give a compact countable set of values
after adjoining their finite limit L_infty, with positive infimum.
For the above shifted construction now require
x>2^(k+2)(1+C_(k+1)). This still removes only finitely many retained
depths M-j for each fixed k. Let B range over offsets of the finitely
many length-(k+1) suffixes of exponents at most six. The set
of numbers -log₂(1-B/x) for positive integers x satisfying this
bound, ranging over every k>=0, is countable and compact after
adjoining zero. At fixed k its only possible new accumulation point
is zero, and as k increases its largest allowed value tends to zero.
Call the resulting countable compact set D.

The final shifted distortion equals 1-2^(-v), where
v=L(x,n)+L_j-log₂(1-B/x), since the unshifted retained prefix
has reciprocal correction product Jx/y_j=2^(-L(x,n)-L_j).
Take E to be the image of K_n+{L_j,L_infty : j>=1}+D under this
map, using the nonnegative carrier K_n. The sum is a compact
countable union of translates of a null set and hence is null.
Its positive lower endpoint and finite upper endpoint give the
claimed interior bounds. The same linear lower count now lies
inside E simultaneously in the stated phase-by-phase sense.

## All-depth maximal estimate at almost every real phase

For fixed 0<theta<1 and every 1<p<2, the raw cone has a uniform
moment over the translated grid:

    sup_Q ||S_Q^u([theta,1])||_(L^p(du)) < infinity.

Consequently for every real a>1/p,

    || sup_(Q>=1) Q^(-a) S_Q^u([theta,1]) ||_p < infinity.

In particular, simultaneously for every theta>0 and epsilon>0 at
almost every phase, the whole sequence satisfies
S_Q^u([theta,1])=o(Q^(1/2+epsilon)). The fixed triadic rational
equivalence above is a separate pointwise statement.

Here is the moment argument. Under the iid geometric exponent
probabilities, the word probability is J_w/3^Q. Its ternary residue
law at depth Q has Haar-normalized mass function g_Q on Z/3^Q.
This is exactly the conditional expectation onto the depth-Q cylinders
of the infinite ternary density, since every further term is a multiple
of 3^Q in Z_3. For every p_0<2, p_0>=1, one therefore has uniform
L^(p_0) bounds from the unrestricted density theorem. The norms of
finite group functions below use uniform probability. [El Jaouhari's
moment results and additional estimates, paper 9 v2](https://rstation.ai/problems/collatz/papers/9/v2)

Let h_B be the depth-Q density restricted to F_w in [B,2B), for
dyadic B ranging over all positive scales. For B>=1 it is at most
g_Q pointwise, and its L¹ norm is O(B^(-1/2)). Indeed for
J=3·2^(-a) one has E J=1 and E sqrt(J)<1 by strict concavity.
The square root of F_w=(1/3)sum_(i<=Q) product_(h<=i) J_h is bounded
by the sum of the square roots, so E sqrt(F_w) is bounded uniformly.
Choose p<p_0<2. Interpolating L¹ with L^(p_0) gives
||h_B||_p=O(B^(-delta)) for some delta>0.

For B<1 the first exponent satisfies 2^(-a_1)<=F_w<2B.
Conditional on any prescribed first exponent a, the ternary
residue map from depth Q-1 to depth Q is
z -> 2^(-a)(1+3z); it is a bijection onto one residue class modulo
three. The pushed density therefore has L^p norm exactly
3^(1-1/p)||g_(Q-1)||_p. The sum of the eligible first-letter
probabilities is O(B), giving ||h_B||_p=O(B).

For uniform u the shifted odd representatives can be written as
t=v+2j, 0<v<=2, 0<=j<3^Q. Independently of uniform v, their
original residue labels have a uniform cyclic displacement on
Z/3^Q: decompose the translation Pu into its integer multiple of
two and its remainder. Conditional on the remainder, identifying
the new smallest positive representative changes the cyclic index
only by a fixed carry. Since F_w/t lies in [theta,1], only
B<=t<=2B/theta matters for this band, and 1/t<=1/B. For any such
j its total possible coefficient mass is h_B at the corresponding
original label because 3^Q times the word probability equals J_w.
For B>=1 there are O_theta(B) such labels, and Minkowski over the
cyclic displacement bounds the band norm by O_theta(||h_B||_p).
For B<theta/2 there is only j=0, and the permissible v have
probability O_theta(B). The band norm is then at most
O_theta(B^(1/p-1)||h_B||_p)=O_theta(B^(1/p)). The intervening
dyadic scales theta/2<=B<1 are finite. Both infinite tails are
summable in norm, proving the uniform estimate.

Finally the pth power of the stated maximal function is bounded by
the sum of Q^(-ap) times the pth powers, an integrable series when
ap>1. Its terms tend to zero almost everywhere. Taking p arbitrarily
close to two and using a countable cofinal family of thresholds and
exponents proves the stated simultaneous all-depth conclusion.

## A residual exceptional set for neighborhoods of the null carrier

Assume an escaping orbit exists and take its common compact null E.
There is a dense countable intersection of open sets of phases such
that, for every open neighborhood O of E in (0,1) and every a<1,

    limsup_Q S_Q^u(O)/Q^a = infinity.

This countable intersection has Lebesgue measure zero by the preceding
maximal estimate (use any fixed neighborhood bounded away from zero
and 1/2<a<1). In particular it contains irrational phases. It handles
all neighborhoods by taking a countable nested neighborhood basis of
the compact E and all exponents by taking a sequence increasing to one.

For a fixed neighborhood, exponent and positive integers M,N, every
triadic phase admits a finite word subsum exceeding M Q^a at some
Q>=N, using its linear lower bound on the common carrier. The words
may be chosen from the preceding construction, with translated
targets strictly between zero and P. Their distortions lie in E,
inside the open neighborhood, and each summand varies continuously
near this phase while the finite list stays marked. Thus the union
of all such witnessing open neighborhoods of phases is open and
dense. Intersecting these open sets proves the assertion by Baire's
theorem. One can further require S_Q^u(E)=0 at *every* depth:
for any fixed word the inverse image of compact nowhere dense E
under its distortion map is nowhere dense after closure, since the
map is strictly monotone and continuous off its one wrapping point.
Countably many words and depths thus exclude only a meagre set.
