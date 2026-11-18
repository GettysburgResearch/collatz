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
