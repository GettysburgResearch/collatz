# Exact algebraic rigidity is not a numerical stability theorem

**RB1--RB3: PROPOSED, self-audited.** This file supplies adversarial controls
and a separate stable-state corollary. It prevents replacing exact invariant
identities by tiny errors, finite numerical tests, or a limiting sequence of
growing programs.

## RB1. One polynomial variable already defeats a dimension-only defect gap

Let tau(n) be the first raw shortcut time to 1, interpreted as infinity if
no such time exists. For each integer K>=1 define

    f_K(n)=min(tau(n),K)/K.                           (1)

This is uniformly computable with K literal T steps, regardless of Collatz.
It is not a program that waits for an unproved eventual hit. For n>1,
tau(n)=1+tau(T(n)) with the usual infinity convention. The edge 1 -> 2
is handled separately. Consequently

    0<=f_K(n)<=1,
    sup_{n>0}|f_K(T(n))-f_K(n)|=1/K,
    f_K(1)=0,   f_K(2^K)=1.                          (2)

Equality in the defect bound is attained at n=1. The oscillation stays one.
Since T(n)>=n/2, n>=2^K implies T^j(n)>1 for j<K. Thus f_K(n)=1 for every
n>=M=2^K. Equation (1) is a finite table below M with a constant tail, not
a claim that all larger integers avoid 1 forever.

Fix ANY input base B. On the nodes j=0,...,M prescribe

    P_d(j)=min(B*j+d,M),  d=0,...,B-1,
    H(j)=f_K(j), 1<=j<=M;  H(0)=1.

Exact Lagrange/Newton interpolation supplies rational polynomials P_d,H
of degree at most M. Start with the single scalar state 0. An induction on
digits gives reachable state min(n,M), so the polynomial machine computes
f_K EXACTLY. The displayed min is used to SPECIFY the finite interpolation
table; the actual digit updates are the fixed polynomials, without runtime
comparisons. The program uses one state variable but growing degree and
coefficient complexity.

Therefore there is no positive lower bound on normalized global invariance
defect depending only on the state dimension: dimension one already has
oscillation one and defects tending to zero. This does not refute a bound
that also controls degrees, coefficients, conditioning or transition norms.
It does not contradict AR2, which assumes zero defect for one fixed program.

Capped hitting-time and near-invariance constructions are not new here;
PR142's NEAR_INVARIANTS.md and REGULARITY_BRIDGE.md are prior project work.
This pass adds the explicit one-variable POLYNOMIAL realization and its
consequence for the new algebraic rigidity class. No literature-priority
claim is made for the elementary capped-clock observation itself.

## RB2. The pointwise limit does not preserve finite description size

For each fixed n, f_K(n) tends to 0 if n reaches 1 and to 1 otherwise.
Its pointwise limit is thus the nonconvergence indicator. Equations (2)
alone do not make that limit a fixed polynomial digit machine. The degrees,
finite tables and potentially other program resources grow with K.

Even if Collatz holds, convergence of f_K to zero is not uniform in n:
sup_n f_K(n)=1 for every K. Conversely, no nonzero limiting value at a
fixed n is produced by this finite construction. Selecting n=2^K changes
the source with K and is not a fixed-source counterexample.

Finite specialization is similarly one-way. A modular violation disproves
exact invariance of a rational model. A constant modular reduction, even
for several chosen primes, proves no rational invariant identity. A quotient
that separates a supplied unequal pair is the missing guard in that shortcut.

## RB3. Stable compact digit-state classifiers are automatic

There is a complementary route beyond polynomial maps. Let a machine have
a compact metric state space X, continuous digit maps P_d:X -> X, and a
continuous scalar observation h. Assume the family of ALL finite digit
compositions is equicontinuous. Suppose every state reachable by a canonical
positive word satisfies either h<=-eta or h>=eta, for one fixed eta>0, and
use the sign as a Boolean output.

Then the source-indexed Boolean sequence is B-automatic. By uniform
continuity of h and equicontinuity of the composition family, there is
delta>0 such that two reachable states within delta have the same output
after EVERY finite suffix. Otherwise the h-values of such suffix states
would differ by at least 2eta. Define states equivalent when all their
future suffix outputs agree. This is a right congruence. Representatives
of distinct classes are delta-separated, and compactness permits only
finitely many such representatives. The finite quotient is a DFAO; one
extra initial state handles the first nonzero digit when needed.

A concrete sufficient condition is that every P_d is nonexpansive in one
common metric. On X contained in [0,1]^d with the sup norm, if h is L-Lipschitz,
a grid with side at most eta/L shows a safe bound of

    1+(1+ceil(L/eta))^d

behavior classes including the extra initial state, for L>0. The L=0 case
has constant output. The grid argument concerns reachable states; h's margin
need not hold at the unused initial state. Nonexpansiveness prevents suffixes
from magnifying the initial grid-cell diameter.

Combining this finite quotient with FD3, a globally Collatz-invariant
classifier of this stable compact kind is constant. With finitely many
source exceptions it has exactly the same base-dependent normal form.
This is a self-contained theoretical corollary, not an executed neural-network
census and not a theorem about arbitrary neural networks. Expansive maps,
absence of a uniform output margin, noncompact state, or unbounded memory
lie outside its hypotheses. Small numerical edge errors do not establish
equicontinuity, a margin, or exact invariance.

## Executed controls and first unsupported step

The producer checks the complete finite range containing every possible
defect of f_K for K=1,...,10. The complement n>=2M has both endpoint values
one by the analytic tail argument. It exports rational polynomial coefficients
for K=1,...,5, and the separate verifier evaluates them on every reachable
node. These bounded checks support the implementation; the all-K statement
is the proof above. No independent formal or mathematical review is claimed.

None of these results establishes a finite algebraic description or a stable
compact realization of the actual convergence indicator. That remains the
first unsupported step toward a full Collatz conclusion through this route.
