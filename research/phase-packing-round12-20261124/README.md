# Round 12: prefix escape, phase-conditioned entropy, and a finite rational phase classifier

**VERIFICATION STATUS — LEAN NOT CHECKED.** This is proposed written mathematics
and a finite exact Python replay. Lean, Lake, and Elan are absent from this session's
container; network access for installing the toolchain also failed. The eight Lean
declarations in PhasePacking.lean are candidate source only. No compilation,
kernel check, transitive axiom audit, or independent reviewer is claimed.
Round 11's Lean candidate is likewise not promoted to checked status.
Full Collatz remains open.

Parent PR182: dbe1860f7da36f2cc316b038d38a7fb8748dec2a.
Latest parallel work examined: #187 (099058f3f2602a48e109c964899f0a9a2a223338)
independently strengthens the automatic-script exclusion; #188
(beed685ab713923191ae40c9559bf7400298d2d3), SCALAR_COCYCLE.md,
derives an all-reset carry inequality and polynomial lower bound on canonical
drawup. The present packet does not duplicate either result. It combines the
carry inequality with the entire ordinary escape product and with phase-conditioned
carry counting, and develops a finite classifier of contracting rational phases.

## 1. Notation and actual-source hypotheses

Write q_i=U^i(q_0), a_i=v_2(3q_i+1), with q_0 positive and odd. Use the
actual scalar of PR182 round 10:

    h_i = sum_(k>=0) a_(i+k)/3^(k+1),
    h_(i+1)=3h_i-a_i,
    1/2<h_i<=1+log_2(q_i)/3.

The exact source is f94a2ae1caba9a1857feda892ee1779695eea9d2,
research/carry-tower-round10-20261123/ActualScalar.lean (prior checked
result, not recompiled here). Put c_i=ceil(h_i-1/2)-1, p_i=h_i-c_i
in (1/2,3/2], and b_i=3p_i-p_(i+1) in {1,2,3}. Thus c_i is a nonnegative
integer, and

    a_i+c_(i+1)=b_i+3c_i.

Let A_N=sum_(i<N)a_i, B_N=sum_(i<N)b_i, K_N=sum_(i<N)c_i,
ell=log_2(3), and P_N=3^N/2^B_N. Retaining the terminal carry gives

    A_N+c_N=B_N+2K_N+c_0.                                  (1)

The exact ordinary orbit equation is

    q_N=q_0 P_N 2^(c_N-c_0-2K_N) E_N,
    E_N=prod_(i<N)(1+1/(3q_i)).                            (2)

Neither P_N nor the c_i are a different probability law. Both belong to
the same original source. All asymptotic escape statements below assume
the actual orbit is not eventually periodic, equivalently is injective.

## 2. Entire-prefix expansion and canonical occupation bound (R12-1)

The following sharpened version of PR188 SC1 has optimal local exponent
gamma=log_3(4) (approximately 1.26186). For c,d nonnegative integers
with d<=3c+2,

    2^(d-3c) <= ((d+1)/(c+1))^gamma.                       (3)

If d<=c, use (c+1)/(d+1)<=c+1<=2^c and gamma<=2.
If c<=d<=3c, the left side is at most one and the right side is at
least one. For d=3c+1 the ratio is at least two; for d=3c+2 it
equals three. The last case is equality and proves local sharpness.
Applying (3) at each transition (since a_i>=1,b_i<=3), and multiplying,
gives

    2^(B_N-A_N) <= ((c_N+1)/(c_0+1))^gamma.                 (4)

For the bounded finite orbit tests we use the rational integer-power
version of SC1 at exponent 4/3 rather than evaluating gamma numerically.

The prior same-orbit count in PR182 at
a7fd3ac9e5bff7412858df23d776bb847e9c1371,
research/whole-repo-round3-20261123/GLOBAL_ORBIT_COUNT.md, eq. (1),
gives F(X)=#{i:q_i<=X}=O(X^theta/sqrt(1+log X)), where
theta=H_2(log_3(2))=0.949955527188... . This is a written theorem, not
a newly imported Lean result. For clarity the count follows by taking
m=floor(log_3(X/8)) and K=floor(log_2 X). At common odd clock m every
source below X with total binary clock A>=K maps injectively below X/2:
the full carry divided by 2^A is at most (3/2)^m-1. The remaining positive
gap words contribute at most X times the sum of
binom(A-1,m-1)2^(-A) for m<=A<K. This equals X/2^(K-1) times the
upper binomial tail at m in K-1 fair bits. Stirling and the geometric
tail bound give O(X^theta/sqrt(log X)); iterate the X/2 recurrence.
This uses forward invariance and injectivity of the whole actual orbit.

Consequently sum_i 1/q_i<infinity (by the dyadic decomposition or
Tonelli), so E_N is bounded by a finite constant E_* for this source.
Equations (2),(4) and c_N+1<3/2+log_2(q_N)/3 yield

    P_N >= C(q_0) q_N/(1+log q_N)^gamma                   (5)

with positive source-dependent C. This holds at EVERY clock, not just
for a maximizing interval. In particular:

    P_N -> infinity, equivalently ell*N-B_N -> +infinity.

This is stronger than the earlier lower bound on maximum canonical
drawup. A fixed source with a bounded subsequence of P_N must be
eventually periodic. If its scalar is irrational, that conclusion
would itself be impossible (a periodic gap tail has rational scalar).

Inverting (5) gives, for X>=2,

    #{i:P_i<=X} = O_q(X^theta (1+log X)^(gamma*theta-1/2)),
    sum_i P_i^(-s)<infinity for every s>theta.              (6)

For the inversion, x/(1+log x)^gamma is eventually increasing; its
value at a sufficiently large constant times X(1+log X)^gamma
exceeds X/C(q_0). Insert the resulting bound on q_i into F. For
the series assertion also one can use (5) and absorb its logarithmic
factor into q_i^(s-s') for theta<s'<s.

There is no proof here that every scalar has a bounded subsequence of
P_N. Low rational phases have exponentially growing P_N and pass
this necessary test. A cycle is not an injective infinite orbit and
is excluded from (5),(6).

## 3. Phase-conditioned carry entropy (R12-2)

This attack counts actual carries, not the whole unconstrained
positive-gap alphabet. The relation (1) and the logarithm of the
actual complete affine equation give

    2K_N = ell*N-B_N+log_2(q_0)+log_2(E_N)
             -log_2(q_N)-c_0+c_N
         <= ell*N-B_N+O_q(1)-(2/3)log_2(q_N).               (7)

Here c_N<1/2+log_2(q_N)/3, and E_N is bounded as above. Even the
elementary harmonic bound log E_N=O(log N) suffices for the
limiting average. Set

    beta=liminf B_N/N,
    delta=(ell-beta)/2,
    kappa=limsup_m log P_b(m)/m,

where P_b(m) is the number of distinct length-m factors in the
canonical b-word at any starting time. Necessarily beta<=ell and
limsup K_N/N<=delta. The canonical alphabet is finite; kappa<=log 3.
For a periodic or eventually periodic phase, kappa=0. For any
subexponential factor-complexity canonical sequence, kappa=0 too.

For t>=0 put F(t)=(1+t)log(1+t)-t log(t), F(0)=0, with natural logs.
It is continuous, strictly increasing and unbounded. Fix B>0 and eta>0
such that

    eta>delta,       B(kappa+F(eta))<log 3.                 (8)

Then on the SAME injective ordinary orbit,

    limsup_(N->infinity) (1/N) #{j<N:q_j<=N^B} <= delta/eta. (9)

Proof. Put m=floor(B log_3 N)+1. For j=m,...,N-1 consider the
length-m canonical word b_(j-m),...,b_(j-1), together with its
m+1 carries c_(j-m),...,c_j. This pair determines the exact actual
past gap word by the one-step recurrence. Sum the carry-window
costs over j; each c_i is counted at most m+1 times, so at most
(delta/eta+o(1))N windows have cost >eta(m+1).

For every remaining window the number of possible carry vectors is
binom(m+1+floor(eta(m+1)),m+1) <= exp((m+1)F(eta)).
This is stars-and-bars followed by the usual entropy bound on a
binomial coefficient (or optimize the generating series (1-z)^(-m-1)).
Multiply by P_b(m)<=exp((kappa+o(1))m). The exact past affine
identity 2^A q_j=3^m q_(j-m)+C fixes q_j modulo 3^m from that
actual gap word alone. Since 3^m>N^B, each word permits at most
one positive endpoint <=N^B, and injectivity prevents a second
occurrence of the same endpoint. Hence the number of low-cost
low-height endpoints is at most N^(B(kappa+F(eta))/log 3+o(1))=o(N).
The first m endpoints are o(N); (9) follows. No mixing, iid
assumption, or stationary-limit exchange is made.

Taking eta down to delta yields the height lower bound

    liminf_N log(max_(j<=N) q_j)/log N
        >= log(3)/(kappa+F(delta)),                         (10)

with infinite right side when both terms vanish. Indeed for any
strictly smaller B, choose eta>delta sufficiently close to delta;
(9) shows a positive fraction above N^B for all sufficiently large N.
For beta=ell and kappa=0 the stronger statement holds: for EVERY
fixed B>0, the proportion of indices below N^B tends to zero.

### Consequences for the actual surviving rational phases

For a fixed rational phase beta is its mean canonical gap, independent
of all carries and any finite initial prefix; kappa=0. The previous
general critical packing exponent is about 1.05268, whereas (10) gives:

| phase | beta | delta | necessary liminf height exponent |
|---|---:|---:|---:|
| scalar 7/8 (and 5/8) | 3/2 | 0.04248125... | 6.187403458... |
| scalar 729/1456 | 19/12 | 0.00081458... | 166.231906997... |

These bounds are conditional on an actual nonperiodic orbit having
the indicated phase. No assumption of critical *actual* average gap
is needed. The numbers follow from the exact expression in (10).
They are necessary conditions, not a universal height upper bound.

Moreover if beta=ell, kappa=0, equations (5),(9) force P_j>N^B for
a proportion tending to one among j<N, for every B>0: P_j<=N^B
would give q_j<=C N^B(1+log N)^gamma, hence q_j<=N^(B+epsilon)
eventually. Thus even an arbitrary polynomial upper bound for the
canonical prefix maximum on an unbounded subsequence is incompatible
with such an escaping low-complexity critical phase. This is a
stronger bridge than a fixed small drawup threshold, but it does
not force low complexity or critical canonical mean for arbitrary
actual scalars.

## 4. A finite global classifier and recognizer for contracting phases (R12-3)

Take a supplied rational candidate t for h(q). Propagate on the actual
map by t'=3t-a. Reject soundly when t<=1/2 or 3t>bl(q)+3, the
necessary rational guards from the actual scalar bound. If q=1,
accept exactly t=1. After at most r odd steps, where 3^r divides
the candidate denominator exactly, the reduced denominator is
coprime to three. The canonical p-phase then cycles with some
period L, with b_i in {1,2,3}. This argument covers the branch

    R=3^L/2^(sum_(i<L)b_i)<1,

i.e. beta>ell. All computations of R and the canonical phase are exact.

Use the carry coordinate Y_i=q_i/2^c_i. The candidate guards imply
3c_i<=bl(q_i)+1 and c_i<=bl(q_i)-1, hence

    Y_i>=1, 2^(3c_i)<=4q_i, q_i^2<=4Y_i^3.

The exact complete equations give

    Y_(i+1) = 3Y_i/2^(b_i+2c_i)+1/2^(b_i+3c_i)
            <= (3Y_i+1)/2^b_i.                             (11)

For this periodic canonical word let z_i be the unique positive
rational periodic solution

    z_(i+1)=(3z_i+1)/2^b_i,  z_L=z_0.

If the full clock is A and complete carry C, then
z_0=C/(2^A-3^L), and all z_i are computable. Let zmax=max z_i,
R_j=3^j/2^(sum_(i<j)b_i), Rmax=max_(0<=j<L)R_j.
Subtract the canonical equality from (11), retaining the signed
difference and positive multiplier, to obtain

    Y_(nL+j)-z_j <= R^n R_j (Y_0-z_0).                     (12)

The subscript zero now refers to the tail after clearing the ternary
denominator. Formula (12) applies to every prefix on which the guards
continue to pass, whether or not the candidate is the actual scalar.

### Finite recognition of a supplied rational equality

Let q be the ordinary source at the start of that tail. Choose n
so that R^n Rmax q<=1 (R<1 makes this a finite exact computation).
Unless a previous guard has already rejected, after nL odd steps
and at every subsequent guarded state, Y<=zmax+1. Put

    Q_burn=floor(sqrt(4(zmax+1)^3)).

Then the ordinary states are integers in [1,Q_burn]. Within the next
Q_burn+1 states either a guard fails or an actual ordinary state
repeats. On a repeat, the literal period has gap word w of length k,
and its exact scalar at that repeated state is

    charge(w)= (sum_(i<k) w_i 3^(k-1-i))/(3^k-1).

Compare the propagated candidate there to charge(w). Equality is
equivalent to the original equality by the exact scalar recurrence.
This gives a finite decision, not a semidecision, for every supplied
rational candidate whose eventual canonical phase is contracting.
The budget is r+nL+Q_burn+1, with n computed at the actual tail
source. For each fixed phase, the burn-in is O(log q) and the
post-burn budget is independent of q. Prior R8-G4 treats triadic
candidates and R10-P4 treats a single paid return; this handles
all successive carries at a contracting phase and does not
require any preverified convergence floor.

### Uniform complete cycle bound for a contracting phase

If an actual periodic orbit has this canonical phase, then Y and z
return after a common period. Equation (12), iterated by that period,
forces Y_i<=z_i at every phase: a positive Y_i-z_i would be strictly
contracted while returning unchanged. Therefore every such actual
ordinary cycle lies inside the explicit phase-dependent interval

    1<=q_i<=Q_cycle=floor(sqrt(4 zmax^3)).                   (13)

All candidate cycles are classified by the literal finite functional
graph on positive odd integers <=Q_cycle, deleting edges that exit
the interval; compute their actual scalar words to retain only those
with the designated phase. This is an exact finite classification
of the contracting branch of the scalar problem. It does not assert
that this graph never has nonstandard cycles for unbounded phases.

In particular, if the finite graph has only the ordinary fixed point
1, no nontriadic rational scalar with that phase can occur at any
positive source: a true candidate would eventually be periodic by
(12), and its cycle must satisfy (13). This also works on any actual
rational phase reached after an arbitrary finite prefix.

### Exact finite graph controls

For 1<=L<=200, choose the balanced word
b_i=floor((i+1)A/L)-floor(iA/L) with A=bitlength(3^L), so that
2^A>3^L and every b_i is 1 or 2. These are CANONICAL words, not
assumed actual gap words, and may have nontrivial integer carries.
Their Q_cycle bounds are computed exactly by integer arithmetic:

| L | Q_cycle |
|---:|---:|
| 1 | 2 |
| 3 | 40 |
| 5 | 560 |
| 17 | 5980 |
| 29 | 25848 |
| 41 | 140849 |
| 147 | 1904337 |
| 200 | 5019951 |

The largest bound in this test is 5019951. The confined graph on
all 2509976 positive odd vertices up to that bound has exactly the
one cycle {1}. This excludes nontriadic phases in this tested
balanced family by (13). The graph check does not assert convergence
of all starting values in the graph: some paths can exit it.
This finite family can also be handled using the older sufficiently
large verified floor; no priority or breakthrough for these small
denominators is claimed.

## 5. Verification and explicit remaining gaps

Executed phase_controls.py locally in normal Python and under -O,
with identical bytes; no asserts are used. Exact receipt is
CONTROLS.json. It covers 24,703 actual guarded edges and prefix
identities, 113,588 full past residue identities, 17,030 candidate
decisions (against known finite orbit scalar oracles), 87 contracting
phases of periods up to four, and the 200 balanced-word bounded
cycle computations including the complete finite graph.
The finite graph uses no arbitrary stopping-time cutoff. The
bounded oracle for the small actual trajectory tests uses a
10,000-step cap and fails explicitly if exhausted.

PhasePacking.lean contains eight proposed finite lemmas and eight
#print axioms commands for the next Lean-enabled replay. Its scope:
complete carry telescope, normalized ordinary edge, cubic height
guard, canonical difference and finite prefix, returning comparison,
and full past endpoint uniqueness. **None has been compiled; no
axiom audit was executed.** The infinite occupation, entropy argument
and finite recognizer consumers remain written proofs. No full
repository validator was run in this session. No workflow changes.

The principal remaining scalar issue is the LOW phase beta<=ell
or an arbitrary irrational phase. For the narrow 729/1456 phase
a nonperiodic ordinary realization must now have extraordinarily
large prefix heights, but no opposing universal height upper bound
is known. To close Collatz we still need a universal actual-source
arithmetic construction, or a contradiction to the combination of
carry entropy, canonical prefix drift and full congruence arithmetic.
Nonstandard cycles outside the contracting canonical branch also
remain open. Do not conflate the new finite phase decision with
universal scalar membership or Collatz convergence.

## Reproduction

    python -B phase_controls.py
    python -O -B phase_controls.py

Expected identical JSON receipt committed with the source.
For the later Pro audit, use the upstream pinned Lean 4.34.1 and
Mathlib d13f23b723b8a846827a245b89c10fc7d3f11612 in a suitable
Mathlib environment, run lake env lean -j1 -DwarningAsError=true
on PhasePacking.lean, inspect every #print axioms output, repair
any errors, and record the exact head, source hash, stdout and
exit status before assigning checked status. Do the same for
round 11's still-uncompiled RepetitionWindow.lean.
