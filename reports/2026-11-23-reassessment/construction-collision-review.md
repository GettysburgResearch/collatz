# Independent review: finite clocks and fixed-source repeat budgets

23 November 2026. Reviewer: `/root/source_construction`.

**Verdict: VERIFIED WITH FIXES at the narrow written claims below.** The
author repaired the later-window corollary during review. The deterministic
infinite-series core also passed an independent strict Lean build and an
audit of every authored theorem. No actual Collatz escape, collision upper,
universal source construction, or full Collatz theorem is established.

## Frozen inputs

Repository baseline: `c91b80a3156e640ad471cf30c47721145ae21eb1`.

| File | SHA-256 reviewed |
| --- | --- |
| `research/reassessment-20261123/collision/FINITE_CLOCK_AND_FIXED_SOURCE.md` | `45d7be3b4a5b3fbef2d9481120c38de635d3c52f4157856790ba99b20c7a762b` |
| `research/reassessment-20261123/collision/lean/FiniteClock.lean` | `dfce17c2af78df947ac865ed47832e3265d077be407cb928ccb68d9c3936c3f4` |
| `research/reassessment-20261123/collision/lean/FiniteClockAudit.lean` | `4d8d936a95131018e8bb392c07302aba6cfad62098efd04de53e9e7fa9260918` |

The source comparisons retain the pins in `collision-sources.json`. This
review reconstructs the new deductions, not all imported analytic claims
in the peer branches. For application to `FAST_EQUIVALENT_FLOW.md`, use its
ordinary state domain of positive odd integers prime to three and its
legal unit parents. The existence of the hypothetical component and its
positive harmonic flow remains an explicit, source-qualified hypothesis.

## 1. Universal finite-clock theorem

**Theorem 1, equations (3)--(7): VERIFIED on the stated graph.**

For a fixed ordinary source `n`, put `x_j=U^j(n)`. There is no change of
source or branch in this construction. The no-cycle assumption gives
injectivity of `j↦x_j`. The harmonic equation includes `nu(x_j)` as a
nonnegative incoming summand at `x_(j+1)`, so
`nu(x_j)>=nu(n)>0`. These two facts, separately, give

\[
\nu(n)\sum_j c(x_j)^{-1}
\le\sum_j\nu(x_j)c(x_j)^{-1}
\le\sum_{x\in E}\nu(x)c(x)^{-1}=M.
\]

Every sum is nonnegative; no conditional series rearrangement is used.
Injectivity is essential for the second inequality. Harmonicity alone
would not supply it on a cyclic component.

For the stated independent exponential holding times, Tonelli gives
`E_n T_infinity=sum_j 1/c(x_j)<=M/nu(n)`. Finite expectation of this
nonnegative extended random variable implies finite lifetime almost
surely. Finite positive rates ensure that no individual holding time
creates the explosion; infinitely many original successor jumps occur
before that lifetime. This proves the assertion for the minimal process
killed at its explosion time.

At each fixed target, the harmonic sum is finite and proves coordinatewise
balance. However, each starting state has survival probability tending
to zero. Bounded convergence under the countable probability `pi` proves
that the killed semigroup's total surviving mass tends to zero. This
argument does not require a finite average lifetime under `pi`.

The packet correctly distinguishes that minimal semigroup from a
conservative extension supplied with additional entrance behavior at
infinity. It does not claim that every extension with the same finite
rate matrix is impossible. The infinite mean activity in (7) follows
because one injective spine already has infinitely many flow values
bounded below by one positive number.

## 2. Exact finite-capacity spine flux

**Theorem 2, equations (9)--(10): VERIFIED.**

Let `v_j=nu(q_j)` increase to finite `C`. Acyclicity ensures that `q_0`
has no spine parent and that the only spine parent of `q_j`, for `j>=1`,
is `q_(j-1)`. The off-spine parent sets at distinct endpoint levels are
disjoint. Their flows are `v_0` and then `v_j-v_(j-1)`, with total `C`.
Since `pi(x)c(x)=nu(x)/M`, this gives
`integral Q(1_S) d pi=C/M` with absolute integrability.

For the finite cutoff `S_J`, incoming and outgoing flows are both `v_J`.
Thus its mean pointwise generator is zero and its absolute integral is
`2v_J/M`. The difference between the two generator expressions has
exactly two types of support: the exit at `q_J`, contributing `v_J/M`,
and off-spine parents entering after level `J`, contributing
`(C-v_J)/M`. Their sum is precisely `C/M` for every cutoff.

The indicators themselves converge in `L1(pi)` by bounded convergence.
This proves failure of convergence for these pointwise generator
expressions. It does not by itself establish or refute membership in a
closed generator domain. The corrected packet makes no such unstated
membership assumption. Its further contradiction for an invariant
extension explicitly requires both domain membership and agreement
with the displayed pointwise generator.

## 3. Actual word repeats and the corrected later-window scope

**Theorem 3, equations (15)--(16): VERIFIED.** The word is finite,
nonempty, and made of positive exact valuations. Its ordered full carry
is retained. All iterates in the proof are ordinary positive odd
integers, not residues or independently chosen finite realizers.

For the block endpoints `p_j`, the same complete affine identity applies
to every repeated block. Subtraction gives
`2^A delta_(j+1)=3^d delta_j`. After `k-1` steps,
`2^((k-1)A) delta_(k-1)=3^((k-1)d) delta_0`. The final difference is
even, so coprimality gives the additional factor two in
`2^((k-1)A+1) | delta_0`, including when that difference is negative.

If `delta_0=0`, the original source lies on an actual positive cycle;
the packet retains this alternative. Otherwise the displayed modulus
is at most `|delta_0|`. Iterating
`U(x)+1<=(3/2)(x+1)` gives the strict upper bound
`|delta_0|<(3/2)^d(p+1)` in either sign. Setting `k=2` and using `A>=d`
proves `p+1>2(4/3)^d`. Thus a fixed source which is not itself periodic
has a uniform finite bound on the length of a prefix square, even as
the template varies. This assertion does not exclude positive cycles.

**Equation (18): VERIFIED WITH FIXES.** The first submitted packet,
SHA-256 `f70688e3a3272f686d723b50ca6cb469d01ce69ffbe1e1679c4812bca9f5fbca`,
did not explicitly retain the no-cycle alternative for a later window.
That omission matters: start at `p_0=5`, take `i=1`, `d=2`, `k=2` and
`w=(2,2)`. Since `U(5)=1`, this is an actual later repeated word with
`A=4`, but the unqualified proposed inequality would read
`32<81/4`, which is false.

The reviewed corrected packet requires
`U^(i+d)(p_0) != U^i(p_0)`. Under precisely that condition, applying
Theorem 3 at the window's actual source and retaining
`U^i(p_0)+1<=(3/2)^i(p_0+1)` proves (18). The condition is automatic
on an escaping orbit. Being off-cycle initially does not imply it for
every later window; the corrected prose expressly preserves this
distinction.

## 4. Fixed-limit collision consumer

**Equation (21): VERIFIED as a conditional consequence of the supplied
finite consumer (20).** The source-box injection and its external
analytic consumers retain their original source-qualified scope.

Fix `m` before passing along `N_l→infinity`. If `pi_(N_l)` tends to one
fixed ternary law, its finite residue collision tends to that law's
collision. Writing `r_l=mathcal B_(N_l,m)/(N_l-m)`, (20) says

\[
\sqrt{\operatorname{Col}_{3^m}(\pi_{N_l})}
\le (1-m/N_l)\sqrt{r_l}+m/N_l.
\]

Taking a subsequence realizing the liminf proves
`Col_(3^m)(mu)<=liminf_l r_l`. Only after this step may the proposed
`m`-dependent bound be applied. This justifies the order stated in
(21); it does not prove its premise. The complete ordered carry and
literal source quotient remain in the boxes. Equal endpoint residues
are insufficient to invoke the exact-word repeat theorem.

## 5. Independent formal verification and remaining gap

Both Lean modules were compiled from the frozen source bytes into a
fresh reviewer output directory, with `autoImplicit=false` and
`warningAsError=true`. The compiler was Lean 4.34.1,
`5045d0056413266e57c625dcd7c365b10e377c52`; the reused mathlib dependency
objects were pinned at `d13f23b723b8a846827a245b89c10fc7d3f11612`.
Both compilations exited zero. Source hashes were checked before and
after compilation. Both authored theorems' axiom reports contain only
`propext`, `Classical.choice`, and `Quot.sound`.

Exact commands, paths, outputs and hashes are in
`construction-collision-lean-review.json` and the accompanying
`construction-collision-*-review.log` files. The formal scope is the
deterministic series bound; the stochastic process, finite-capacity
flux, and repeated-word arguments above are independently reconstructed
written mathematics.

The central collision obligation remains open: no bound on the
same-source effective box mass in (21) has been obtained, and no
mechanism has turned persistent cross-box collisions into exact word
repeats violating their actual source and preperiod budget. The
finite-clock result identifies a false stationarity inference and
its exact boundary flux. It does not supply a stationary replacement
law or an escape contradiction.
