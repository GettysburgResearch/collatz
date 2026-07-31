# Live repository review — wave 11

**Date:** 2026-08-01  
**Agent:** `gpt56-pro-03`  
**Scope:** full-PDF consequences, latest coefficient-crossing work, and fixed-support pulse closure  
**Status:** literature/strategy audit plus one new proposed native synthesis; no native status promotions

No positive-integer Collatz counterexample, nontrivial positive cycle, or unconditional resolution is claimed.

## Latest work inspected

This pass integrated:

- the complete Dubickas 2006/2008/2009 papers;
- Matveev 2000, Bugeaud 2002, and Chim 2025;
- PR #53 and PR #70 fixed-support pulse identities;
- PR #76/PR #79 least-counterexample and verified-floor inputs;
- PR #81/PR #83 first-coefficient-crossing and shifted-denominator work;
- PR #16/PR #67 centered `64 -> 81` work.

# 1. Fixed pulse supports are now closed through the exact density threshold

Wave 10 proved an all-repetition four-pulse exclusion. The broader finite-reduction theorem already showed that every fixed support with

\[
A\log2-\frac{s-1}{s}k\log3>0
\]

is decidable in principle, but it did not exclude all such supports.

`LIT-KTHM-0065` now combines the verified positive-cycle floor with the largest-gap pulse inequality, Matveev's source-audited logarithmic form, and complete continued fractions. Subject to the declared native pulse identity and verified-floor dependencies, it proves:

```text
P3=(1,2):
  every nontrivial positive-cycle lift with support 1..18 is excluded;

P11=(1,1,1,2,1,1,4):
  every positive-cycle lift with support 1..117 is excluded.
```

For `P3`, the only positive hits are the trivial all-2 representations of `n=1`. The first uncovered supports are exactly

```text
P3:  19;
P11: 118.
```

At those supports the largest-gap exponential rate changes sign, so the present proof genuinely stops rather than merely becoming computationally inconvenient.

# 2. Why the verified floor closes the formerly exceptional convergents

Let

\[
N_*=4\cdot3^{44}+2.
\]

Every odd member of a nontrivial positive cycle exceeds `N_*`. If the cycle has repeated-baseline parameters `(A,k,r)` and total pulse height `t`, then

\[
\Lambda=(Ar+t)\log2-kr\log3
\]

satisfies the exact product identity

\[
e^\Lambda
=
\prod_j\left(1+\frac1{3x_j}\right),
\]

and hence

\[
0<\Lambda<\frac{kr}{3N_*}.
\]

Writing a reduced candidate ratio as

\[
(r,t)=m(q,p)
\]

cancels the multiplier `m` and gives the primitive necessary inequality

\[
(Aq+p)\log2-kq\log3
<
\frac{kq}{3N_*}.
\]

This excludes precisely the short continued-fraction rows where the pulse-comparison estimate is too weak. The late convergents are excluded by the largest-gap pulse comparison. Neither method alone covers the complete list; their union does.

# 3. Exact certificate coverage

`LIT-X-0065` reconstructs every continued-fraction row with rational logarithm intervals and verifies two complementary methods.

```text
P3 upper convergents below the Matveev cutoff:
  verified-floor only:   3
  pulse-comparison only: 2
  both:                  7
  total:                12

P11 upper convergents below the Matveev cutoff:
  verified-floor only:   4
  pulse-comparison only: 5
  both:                  2
  total:                11
```

The generator and independent verifier agree on semantic digest

```text
c730cce495223542e2d15e424ca0ba94996c2d0382289baab3604344abe8b179
```

The exact artifact does not rerun the external `2^71` verification and does not rederive the native pulse cocycle from raw Collatz iteration.

# 4. Matveev notation correction

The numerical pulse cutoffs were valid, but an earlier source capsule mislabeled the bound

\[
B<kr+1
\]

as a bound on

\[
B^*=\max_i|b_i|.
\]

It is instead a bound on Matveev's weighted parameter `B` from equation `(1.3)`. With

\[
\alpha_1=2,
\quad
\alpha_2=3,
\quad
A_1=\log2,
\quad
A_2=\log3,
\]

one has

\[
B=\max\left\{
1,
(Ar+t)\frac{\log2}{\log3},
kr
\right\}<kr+1
\]

whenever `Lambda<log 3`. `LIT-KTHM-0060` has been corrected explicitly. The constants and frozen cutoff inequalities are unchanged.

# 5. The exact next cycle-side blocker

Support `19` for `P3` and support `118` for `P11` are not merely larger finite cases. The sign change

\[
A\log2-\frac{s-1}{s}k\log3<0
\]

means that one largest support gap no longer makes the pulse correction exponentially smaller than the denominator.

The next theorem must therefore use information not present in the one-gap argument. The most plausible exact routes are:

1. **multi-gap resultants:** combine several coordinate eliminants so that total separated gap length, not only the largest gap, controls the correction;
2. **fresh-prime incompatibility:** use Chim/Bugeaud to show fixed primes account for only logarithmic valuation, then find a denominator prime that cannot divide every pulse resultant;
3. **support-density rigidity:** prove that a positive cycle cannot distribute pulse support at or above the critical density over either negative baseline;
4. **mixed-baseline normal form:** show every near-negative positive cycle has a sparse description relative to one of finitely many baselines, then apply the closed fixed-support theorem.

No audited source currently supplies any of these final incompatibilities.

# 6. Relationship to the newest first-crossing work

PR #83 proves the universal shifted full-denominator equation for every non-descending first coefficient crossing:

\[
A_w=y(2^j-3^q)+d3^q,
\qquad
0\le d<j/3.
\]

It also reduces the exceptional language to polynomially many ordinary starts at each length, conditional only on an effective two-logarithm lower bound. Matveev now supplies that source dependency cleanly.

This creates a second possible use of the same arithmetic engine:

```text
cycle side:
  D divides one sparse pulse correction;

first-crossing side:
  one short displacement d solves a shifted full-denominator equation.
```

The two problems should share continued-fraction, resultant, and fresh-prime tooling. They are not logically identical: the cycle case has `d=0`, while the first-crossing case permits `0<d<j/3`.

# 7. Centered work after the full PDFs

The complete Dubickas papers now establish:

- the exact direct `81/64` nearest-integer constant;
- the stronger four-phase `3/2` lift;
- infinitely many visits to both signs of the centered error;
- the precise one-interval/Sturmian boundary.

They do not exclude the two-sided centered band of radius `1/81`. PR #16/PR #67 must still prove same-seed arithmetic cylinder nonstabilization, not merely real interval escape.

# Recommended next work

## Priority 1 — independent reconstruction of `LIT-KTHM-0065`

Review in this order:

```text
native distributed-pulse correction
 -> largest-gap rotation
 -> verified-floor product inequality
 -> all-r Legendre coverage
 -> Matveev weighted-B specialization
 -> exact convergent union
 -> trivial-hit classification.
```

## Priority 2 — support 19 and 118 fresh-prime/resultant attack

Freeze one critical support in each family and factor the denominator/resultant gcd structure. Record every prime that can divide all coordinate resultants. A genuinely new prime outside that set is a complete contradiction.

## Priority 3 — transfer the shifted-denominator equation into the same compiler

For PR #83, treat each short displacement `d<j/3` as an additional coefficient and attempt the same primitive-convergent plus fresh-prime reduction.

## Priority 4 — centered same-seed renewal

Use the full source constraints as side conditions, but prove a recurrence on the appended ordinary blocks `q_K`; another real limit-point estimate will not cross the extraction boundary.

# Bottom line

The pulse lane has moved from a few explicitly handled supports to the complete positive-rate fixed-support envelope:

\[
\boxed{
P_3:s\le18,
\qquad
P_{11}:s\le117.
}
\]

The new frontier is a true support-density phase transition. Crossing it requires a fresh arithmetic invariant, not more cap-box enumeration.