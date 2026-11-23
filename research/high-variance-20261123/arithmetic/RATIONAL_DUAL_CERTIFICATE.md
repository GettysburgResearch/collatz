# A global rational-dual attack, with an effective certificate

## Result and remaining obligation

This attack tries to replace a hard ordinary inverse-word choice by the
entire complementary parity trajectory. Its useful output is a
**terminating, quantitatively bounded decision procedure for a proposed
rational parity dual of any positive integer**. A correct rational dual
also supplies an explicit bound for entering a cycle. The proof uses
ordinary integers throughout, including a signed numerator and its fixed
odd denominator; it does not extract an ordinary integer from a compact
2-adic limit.

It does **not** prove that a rational dual exists for every positive
integer, and it does not exclude nontrivial positive integer cycles.
Those are the unresolved closing obligations. In particular, no Collatz
theorem is claimed here.

Monks and Yazinski's *The autoconjugacy of the 3x+1 function*, Discrete
Mathematics 275 (2004), 219–236, defines the parity-complementing
autoconjugacy `Ω`. Their Theorem 2.1 already proves that
`Ω(Z_{>0}) ⊆ Q_odd` is equivalent to absence of divergent positive integer
orbits. Their Theorem 2.5 excludes self-conjugate integer cycles. The
qualitative rationality reduction is therefore **published prior work**.
The present packet independently proves the explicit signed-numerator
product estimates, finite rejection certificates, and quantitative
decision procedure below; it makes no priority claim for these
refinements. [Author's full paper](https://monks.scranton.edu/files/pubs/AutoConjV13.pdf),
[published article](https://doi.org/10.1016/S0012-365X(03)00125-0).

## 1. Complete scope of the attempted merger

Use the shortcut map

\[
 T(n)=\begin{cases}n/2&n\equiv0\pmod2,\\(3n+1)/2&n\equiv1\pmod2.
 \end{cases}
\]

The previous whole-word reservoir retains every alternative source clock
`m` and odd count `h`. If `N=T^k(t)`, an ordinary smaller source exists
precisely when some full correction

\[
 C'\in\left\{\sum_{j=0}^{h-1}3^{h-1-j}2^{d_j}:
       0\le d_0<\cdots<d_{h-1}<m\right\}
\]

satisfies

\[
 C'\equiv2^mN\pmod{3^h},\qquad
 0<2^mN-C'<3^ht.                                      \tag{1}
\]

This is the exact ordinary source language, not its convex hull. A real
point in the interval in (1), or an arbitrary point of the congruence
lattice, need not be a correction of a binary word. This attack did not
establish the missing intersection for arbitrary `t`.

The alternative explored here keeps a *whole infinite* complementary
parity trajectory and then asks whether its 2-adic realization has a
finite rational description. The arithmetic certificate below verifies
that description effectively if one is proposed; it does not assume its
existence.

## 2. Why a positive ordinary dual cannot be the universal source

Suppose two positive integer trajectories `x_i,y_i` have opposite parity
at each of the starting states `0,…,k−1`. Put `P_i=x_i y_i`. If `z_i` is
the odd member, direct calculation gives

\[
 \frac{P_{i+1}}{P_i}=\frac{3+1/z_i}{4}\le1.              \tag{2}
\]

If `z_i≥3`, the factor is at most `5/6`. The factor can equal one only
when `z_i=1`. If opposite parity also holds at the next state, either
the pair is `(1,2)` or `(2,1)`, or the next odd member is at least three.
Moreover, the only positive opposite-parity predecessor of either of
those two exceptional pairs is the other exceptional pair. Therefore,
outside these exceptional pairs,

\[
 x_k y_k\le x_0y_0(5/6)^{\lfloor k/2\rfloor}.           \tag{3}
\]

In particular the only eternally complementary positive integer pairs
are `(1,2)` and `(2,1)`. Any positive ordinary witnesses to `k` bits of
the complementary code of a fixed `n≥3` obey

\[
 y_0\ge\frac1n(6/5)^{\lfloor k/2\rfloor}.              \tag{4}
\]

This is an all-length height obstruction, not a bounded search. It also
holds for convergent sources: `Ω(3)=−4/9`, as in the published paper.
Thus positive ordinary dual extraction is the wrong universal
construction. Signed rational duals are the remaining possibility.

## 3. Signed rational numerator dynamics

Fix a positive odd integer `d`. A rational number `y=w/d` has the same
2-adic parity as its integer numerator `w`, and its numerator evolves by

\[
 T_d(w)=\begin{cases}w/2&w\text{ even},\\(3w+d)/2&w\text{ odd}.
 \end{cases}                                             \tag{5}
\]

The denominator need not be reduced. Let `x_0=n>0`, `w_0=a∈Z`, and use
the actual trajectories `x_{i+1}=T(x_i)`, `w_{i+1}=T_d(w_i)`. A proposed
rational dual is correct exactly when

\[
 x_i\not\equiv w_i\pmod2\quad\hbox{for every }i\ge0.       \tag{6}
\]

All statements below are applied only while the parity tests have
passed. The state with `x=1` and the state with `w=0` are handled
separately in Section 6, before any product logarithm. Before `x=1`, an
odd positive `x` is at least three.

### 3.1 Negative numerator phase

For `w<0`, write `v=−w>0` and `P=xv`. If the next numerator remains
negative, then

\[
 \frac{P'}P=
 \begin{cases}
 (3+1/x)/4\le5/6,&x\text{ odd},\ v\text{ even},\\
 (3-d/v)/4<3/4,&x\text{ even},\ v\text{ odd}.
 \end{cases}                                             \tag{7}
\]

The second factor is positive because this paragraph assumes that the
next numerator remains negative. Since `P` is a positive integer, a
negative phase starting with `P_-=n|a|` lasts at most

\[
 N_-=1+\left\lfloor\frac{\log P_-}{\log(6/5)}\right\rfloor \tag{8}
\]

steps before a parity failure, `x=1`, a zero numerator, or a positive
numerator occurs.

A negative-to-positive crossing can expand the absolute product, and
must be charged. Such a crossing has `x` even and `w=−v` odd, and

\[
 \frac{x'w'}{xv}=\frac{d/v-3}{4}<\frac d4.               \tag{9}
\]

Consequently the initial positive-phase product satisfies
`P_+≤dP_-`. There is at most one such crossing because (5) preserves
positivity. This crossing is charged separately from the positive
small-state visits below.

### 3.2 Positive numerator phase

Now let `w>0` and `P=xw`. Define

\[
 q_d=\frac{2d+3}{2d+4}<1,\qquad R_d=\frac{d+3}{4}\ge1.
                                                               \tag{10}
\]

If `w>d`, then

\[
 P'\le q_dP.                                           \tag{11}
\]

Indeed an odd `x≥3` gives factor at most `5/6≤q_d`. Otherwise `w` is
odd, and `w>d` implies `w≥d+2`, so its factor is
`(3+d/w)/4≤(3+d/(d+2))/4=q_d`.

If `1≤w≤d`, then

\[
 P'\le R_dP.                                           \tag{12}
\]

For even `x` this follows from `w≥1`; for odd `x≥3` the factor is at
most `5/6≤R_d`.

The important resource is the **number of distinct small numerators**,
not the total number of visits to an assumed compact set. Before the
first repeat of a small numerator there are at most `d` departures from
states in `{1,…,d}`. Every other departure contracts the same integer
product.

## 4. An explicit first-event bound

Start a positive phase with product `P_+`. Set

\[
 B=d+1+\left\lfloor
       \frac{\log(P_+R_d^d)}{\log(1/q_d)}
       \right\rfloor.                                  \tag{13}
\]

Within `B` transitions, at least one of the following has occurred:

1. A parity test fails.
2. `x=1`.
3. A small numerator `w∈{1,…,d}` repeats.

For if none occurred, among the first `B` departures at most `d` would
be small-state departures. Equations (11)–(12), with `R_d≥1>q_d`, give

\[
 1\le P_B\le P_+R_d^d q_d^{B-d}<1,                     \tag{14}
\]

a contradiction. For an exact implementation, one can choose any
integer `B>d` satisfying the strict rational inequality in (14);
floating-point logarithms are not needed.

Through this first-event state, using only the preceding departures,

\[
 x_i\le P_i\le P_+R_d^d.                              \tag{15}
\]

For a negative starting numerator, use (8) first and the conservative
bound `P_+≤dn|a|` in (13). Thus the negative crossing is paid for once,
in addition to at most `d` positive small-state departures. A zero
crossing invokes the separate zero rule below.

## 5. A repeated small numerator yields a finite certificate

Suppose parity has been checked at every state `0,…,j`, and

\[
 i<j,\qquad 1\le w_i=w_j\le d.                        \tag{16}
\]

The two numerator tails are identical because (5) is deterministic.
There are two cases.

**Equal integer states.** If `x_i=x_j`, the full pair state repeats.
Its intervening parity tests have already passed, so (6) holds forever.
The proposed rational dual is accepted with an actual finite prefix and
cycle certificate.

**Unequal integer states.** Put

\[
 r=v_2(x_i-x_j),                                      \tag{17}
\]

where the valuation is of the nonzero integer difference. Two ordinary
integer trajectories whose starting difference has valuation `r` have
the same first `r` parity bits and different parity at offset `r`:
while the bits agree, each map divides the difference by two and
multiplies it by an odd factor. This proves the assertion by induction.

Because the `w` tail repeats with period `j−i`, and parity has passed
through state `j`, this mismatch forces the **first** parity failure of
the pair at state

\[
 j+r.                                                \tag{18}
\]

For completeness, agreement of the two `x` tails before offset `r`
propagates already verified opposite parity to every state from `j` to
`j+r−1`, by induction using the earlier state a period behind. At offset
`r`, the earlier state `i+r` is already valid and the two integer
parities differ, while the numerator parities agree. The terminal
parity test at `j+r` therefore fails. The checker below actually
replays through and tests this terminal state; it does not infer an
infinite itinerary from a long finite prefix.

Equation (15) additionally bounds this extra clock by
`r≤floor(log_2 M)` for `M=ceil(P_+R_d^d)` whenever the difference is
nonzero. The concrete valuation (17) is sharper and requires no real
arithmetic.

## 6. The small exceptional states are decidable too

**`x=1`.** Its true complementary rational is `2`, so the correct
numerator is `2d`. If `w=2d`, accept the pair cycle
`(1,2d)→(2,d)→(1,2d)`. If `w≠2d`, compare the two `T_d` trajectories
from `w` and `2d`. The first parity discrepancy occurs exactly after

\[
 v_2(w-2d)                                          \tag{19}
\]

steps, by the same difference argument. The pair therefore fails at
that terminal state, which is included in the replay.

**`w=0`.** The numerator stays zero. Complementarity would require the
positive integer trajectory to remain odd forever. Its exact initial
odd-run length is `v_2(x+1)`, because during that run

\[
 T^r(x)+1=3^r(x+1)/2^r.
\]

Thus the parity test fails exactly at offset `v_2(x+1)`. This rule also
covers an initial zero numerator and a crossing such as `−1/3→0`.
No logarithm of the zero product is taken.

The routine tests parity first, so an even `x` paired with zero is
rejected immediately. If both exceptional rules could apply, either
rule gives a valid finite rejection certificate unless the standard
positive pair has already been accepted.

## 7. What this proves, and the attempted closing step

Equations (7)–(19) give an unconditional algorithm which, for every
`n>0`, `a∈Z`, and odd positive `d`, **terminates** and decides whether
`a/d=Ω(n)`. Its accepted output contains a literal paired cycle. Its
rejected output contains a literal first parity mismatch, with the
terminal index checked.

For a genuine rational dual there can be no rejection. The product
argument and first-event bound therefore force the positive integer
orbit to become periodic, with explicit bounds depending on the
proposed numerator and denominator. This is an effective certificate
version of the published rationality reduction.

The full proof attempt was to produce such a rational dual directly
from an ordinary source, then use the same full-denominator arithmetic
as the cycle lane to eliminate every nonstandard cycle. The product
argument does the verification and quantitative compactness work, but
the proposed rational construction is missing. Finite complementary
prefixes always have 2-adic realizers; (4) shows why positive integer
prefix realizers cannot simply be stabilized. Allowing rational
denominators fixes that explicit obstruction but does not provide a
uniform or source-dependent denominator bound. In particular, running
this decider over all rational candidates is only a semidecision
procedure for a fixed positive source: absent a rationality theorem,
there is no proof that any candidate will be accepted.

Even an accepted dual only gives a finite cycle. A nontrivial positive
integer cycle, if one exists, would also have a rational complementary
dual; the procedure correctly accepts it. The cycle lane's full
denominator obstruction must still be solved for arbitrary words.

## 8. Other global route tested: addition of component sources

Let `μ(n)` be the least positive ordinary integer in the full weak
Collatz component of `n` (allowing arbitrary clocks on both sides).
Then `μ(T(n))=μ(n)` and `μ(2n)=μ(n)`. If `μ` were subadditive, binary
expansion would give `μ(n)≤popcount(n)`, so a nontrivial component
minimum `t>1` would satisfy `t=μ(t)≤popcount(t)<t`.

This criterion alone is not progress on subadditivity. The attempted
whole-source compiler produces a precise extra dynamic. When
`z=x+y+c` and `x,y,c,z` have the same parity, commutation of the affine
branches requires

\[
 c' =\begin{cases}c/2&c\text{ even},\\(3c-1)/2&c\text{ odd}.
 \end{cases}                                           \tag{20}
\]

The odd identity follows by subtracting `T(x)+T(y)` from `T(z)`.
This is the `3c−1` map, not a proven decreasing carry. For example its
positive orbit `5→7→10→5` is a literal carry cycle. Arbitrary changes of
source clocks still have to pay for this carry and preserve the target
resource in (1). No rule proving universal component subadditivity was
obtained. The rational-dual method above was the subsequent global
attack, rather than an asserted solution of this unproved compiler.

## 9. Reproduction and verification scope

`check_rational_dual.py` implements the finite certificate procedure
with integer and rational arithmetic. It verifies the four local
product inequalities actually used, replays every rejection through its
first failing state, and validates each accepted paired cycle. It also
checks proposed duals obtained by reversing explicitly terminated
orbits, altered candidates with a prescribed long matching prefix,
and signed small grids including zero crossings. These computations
validate the implementation and examples; the all-input termination
argument is Sections 3–6.

`rational-dual-check.json` records the actual deterministic run. No Lean
claim is attached to this arithmetic note. The companion cycle lane
contains the packet's separately audited Lean theorem.

Predecessor interface: [previous full-word attempt](../../whole-repo-synthesis-20261122/arithmetic/WHOLE_WORD_MERGER_ATTEMPT.md).
