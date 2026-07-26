# L-8702 — Exact centered height-renewal atlas

**Claim ID:** `L-8702`  
**Type:** lemma  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-sol-02`  
**Reviewing agents:** none  
**Issue:** #40  
**Created:** 2026-07-26  
**Last updated:** 2026-07-26  
**Dependencies:** `D-8701`, `L-8701`  
**Scope:** positive ordinary paths of the exact centered forced-tail recurrence

## Statement

Let \(H\ge 1\), let \(B_0\) be a positive integer with

\[
\frac H{64}\le B_0<H,
\]

and suppose binary controls \(e_j\in\{0,1\}\) make

\[
64B_{j+1}=81B_j+e_j-e_{j+1}
\tag{1}
\]

integral for as long as the path is considered.

1. If the path remains legal for 18 steps, then \(B_j\ge H\) for some
   \(j\le18\). Hence every first height crossing of a legal path occurs at a
   unique time \(1\le t\le18\), and at that crossing
   \[
   H\le B_t<64H.
   \]
   A path may instead fail at a forbidden low residue before crossing.

2. Fix \(t\ge1\) and a word \(e_0\ldots e_t\). Define
   \[
   D_j=\sum_{i=0}^{j-1}
   81^{j-1-i}64^i(e_i-e_{i+1}),\qquad D_0=0,
   \tag{2}
   \]
   \[
   r=\bigl[-81^{-t}D_t\bigr]_{64^t},\qquad 0\le r<64^t,
   \tag{3}
   \]
   and
   \[
   c_j=\frac{81^jr+D_j}{64^j}.
   \tag{4}
   \]
   Then every \(c_j\) is an integer, and all integer initial values with this
   itinerary have the exact affine form
   \[
   \boxed{B_0=r+64^tQ,\qquad
   B_j=c_j+81^j64^{t-j}Q.}
   \tag{5}
   \]

3. Put
   \[
   L=\max\left\{
   \frac{H-64r}{64^{t+1}},
   \frac{H-c_t}{81^t}
   \right\}
   \tag{6}
   \]
   and
   \[
   U=\min\left(
   \left\{
   \frac{H-c_j}{81^j64^{t-j}}:0\le j<t
   \right\}
   \cup
   \left\{
   \frac{64H-c_t}{81^t}
   \right\}
   \right).
   \tag{7}
   \]
   The word realizes a first crossing at time \(t\) exactly for
   \[
   \boxed{Q\in\mathbb Z\cap[L,U)
   =\{\lceil L\rceil,\ldots,\lceil U\rceil-1\}.}
   \tag{8}
   \]
   These nonempty charts are pairwise disjoint as initialized states
   \((B_0,e_0)\), and their union is exactly the set of initialized states in
   the band whose legal forced tail reaches the next height before failing.

## Proof

### Iteration, residue, and affine charts

Induction in `(1)` gives

\[
64^jB_j=81^jB_0+D_j.
\tag{9}
\]

At \(j=t\), integrality therefore requires

\[
81^tB_0+D_t\equiv0\pmod {64^t}.
\]

Since \(81\) is invertible modulo \(64^t\), this is equivalent to
\(B_0\equiv r\pmod {64^t}\), proving the first formula in `(5)`.

For \(j\le t\), split the defining sum at \(j\):

\[
D_t=81^{t-j}D_j+64^jE
\]

for an integer \(E\). The terminal congruence then implies

\[
81^{t-j}(81^jr+D_j)\equiv0\pmod {64^j}.
\]

Again \(81\) is invertible modulo \(64^j\), so \(c_j\) in `(4)` is integral.
Substitution in `(9)` proves the second formula in `(5)`.

The lower band inequality and terminal crossing inequality give the two lower
bounds in `(6)`. The inequalities \(B_j<H\) for \(0\le j<t\) and
\(B_t<64H\) give the upper bounds in `(7)`. All affine coefficients of \(Q\)
are positive, so their intersection is exactly `[L,U)`. For any real \(U\)
and integer \(Q\), \(Q<U\) is equivalent to \(Q<\lceil U\rceil\), proving
`(8)`.

An integer solution of `(1)` has at most one next digit: two distinct choices
would differ by \(1\), which cannot be divisible by \(64\). Conversely, every
integer \(Q\) in `(8)` gives positive integral states satisfying `(1)` and the
first-crossing inequalities. Thus the charts form the asserted deterministic
partition. This is a partition of crossing survivors, not of all states in
the initial band.

### Universal 18-step bound

Expanding `(2)` by controls gives, for \(j\ge1\),

\[
D_j=
81^{j-1}e_0
-17\sum_{i=1}^{j-1}
81^{j-1-i}64^{i-1}e_i
-64^{j-1}e_j.
\tag{10}
\]

All coefficients after the first are nonpositive. Their sum is
\(-81^{j-1}\), attained by \(e_0=0\) and \(e_1=\cdots=e_j=1\). Hence

\[
D_j\ge-81^{j-1}.
\tag{11}
\]

If \(H\ge11\), `(9)` and `(11)` imply

\[
B_{18}\ge
\frac{81^{18}H/64-81^{17}}{64^{18}}\ge H,
\tag{12}
\]

where the last inequality is the exact integer comparison

\[
11(81^{18}-64^{19})-64\cdot81^{17}
=1551116294402118154433498457982123>0.
\]

If \(1\le H<11\), inspect the three positive branches from `D-8701`.
Their increments are \(17Q\) with \(Q\ge1\), \(17Q+4\), and \(17Q+13\).
Thus every positive legal step increases \(B\) by at least \(4\), and 18
legal steps give \(B_{18}\ge B_0+72>H\). This proves the uniform bound.

Finally, at a first crossing,

\[
B_t=\frac{81B_{t-1}+e_{t-1}-e_t}{64}
<\frac{81H+1}{64}<64H,
\]

which proves the stated upper height bound.

## Computational corroboration

`X-8703` enumerates all \(2^{20}-4=1048572\) words for \(1\le t\le18\)
at the canonical height \(H=64^{18}\), independently reconstructs every
formula and interval, and stores aggregate digests plus boundary certificates.
The finite enumeration is classified `EMPIRICAL`; it is not used in the
proof above.

## Dependency audit

- `D-8701` supplies the exact recurrence and the three legal branch formulas.
- `L-8701` supplies the already-proved branchwise strict monotonicity. The
  proof above also repeats the exact increments needed for the uniform bound.
- No asymptotic, probabilistic, or external theorem is used.

## Gap audit

- The recurrence is partial. The lemma explicitly permits failure before a
  crossing and does not claim that the atlas covers every band state.
- A finite crossing chart is not an infinite path and does not discharge the
  ordinary top-boundary obligation in `Q-8701`.
- The canonical computation fixes one height. The identities and 18-step
  bound, not its numerical counts, are uniform in \(H\).
- No translation to a physical Collatz initialization is asserted.

## Adversarial tests

`test_renewal.py` checks direct recurrence replay, negative and exact
floor/ceiling boundaries, first-crossing inequalities, both pieces of the
18-step proof, a brute-force small-band partition, deterministic regeneration,
and digest tamper resistance. `verify.py` imports no builder code and
recomputes the complete canonical atlas.

## Remaining uncertainty

The lemma has not received independent human or agent review, so its repository
status remains `PROPOSED`. It does not decide whether any chart can renew
indefinitely along one ordinary initialized path.

## Suggested next attack

Compose consecutive height charts while retaining the exact transported
quotient and residue, then test whether every attempted infinite composition
must hit an empty interval. Any positive construction must preserve one
ordinary seed across all renewals; choosing a new existential \(Q\) at each
height would repeat the fixed-modulus ghost error of `R-8701`.
