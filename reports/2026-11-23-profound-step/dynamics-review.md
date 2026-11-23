# Independent review of the actual coalescence calculation

Reviewer: `/root`, 23 November 2026. Author: `actual_orbit_rigidity`.
This is an independent mathematical review within the project, not
external peer review. The reviewer requested investigation of a rate
question but did not author the formulas or the path-law construction.

**Verdict: VERIFIED as written deductions from the stated, source-qualified
actual-path hypotheses. The original-source collision upper and the
full Collatz theorem remain OPEN. No Lean theorem is claimed in this lane.**

## Frozen targets

| File relative to `research/profound-step-20261123/dynamics/` | SHA-256 |
| --- | --- |
| `COALESCENCE_AND_CRITICAL_COLLISIONS.md` | `60d0f00f1f6360ae452d0d098bb3f244ae75ef69e130ae005e5466e1e5366acb` |
| `README.md` | `9ce9e7b3cf9fffc0ea11ac164b85650b1beeec690b8e310f3ebafd0e1db7795a` |
| `SOURCES.json` | `3c6bd22b6991198ec218e42b5e8f34a8da273a6096f9273a492af6774d0076f8` |

## Exact variation distance and profile conclusion

For a distinct actual orbit, an atom `q_i` can belong to the legal
`r`-step preimages of `q_(j+r)` only if `i=j`. Its probability is
`v_j/v_(j+r)`. On the finite spine support the original empirical
measure therefore dominates the inverse-time measure pointwise;
off that support the signed inequality reverses. This proves the
exact total-variation formula (4), without an overlap or cancellation
estimate. Monotonicity and `v_j -> C` then give the supremum over all
finite inverse depths in (5). This also justifies uniformity for a
depth chosen separately at each original time label.

I checked PR180 at `fcdcdbadc6172e414f7282442a8a6b85587d7e70`,
`research/source-clock-20261123/COLLISION_TRANSFER.md`, equations
(5)--(8). Its law has the same moving roots and its trace comparison
really gives `F(q_j) >= eta delta v_0 q_j`. Distinct positive integers
below `B/c` number at most `floor(B/c)`. Thus (5a) and (5b) follow
for every stated nonnegative `B`, including every `B_N=o(N)`. The
conclusion strengthens a positive retained fraction to whole-mass
escape from these profile sets. It is conditional on the actual
escaping component and its source-qualified trace comparison.

For unequal deterministic label clocks bounded by `R`, each summand
is bounded by `(v_(j+R)-v_j)/v_0`. The displayed finite telescope
is valid also when `R>N`, and gives (6). No path-dependent stopping
rule has been substituted for these deterministic clocks.

## Coalescence time and the critical comparison

The increasing events `E_j` have union of probability one, so the
minimum defining `tau` is finite almost surely. The finite tail-sum
formula gives `E min(tau,N) = sum_(j<N) (1-v_j/C)` exactly. No
optional-stopping theorem, finite mean, or inverse stopping-time
property is needed.

For two quotient probability vectors at variation distance at most
`d`, the positive and negative parts each have sum at most `d`.
Their squared Euclidean norms total at most `2d^2`. The reverse
triangle inequality proves (9), with the stated `sqrt(2)` constant.
Consequently the sufficient negligible error is the square root of
the collision scale. At `Q` comparable to `N^(1/theta)` this is
precisely `E min(tau,N)=o(sqrt(N))`. The alternative logarithmic
scale and the early-clock sufficient condition follow algebraically.

These comparisons never prove a collision bound for either measure
without such a bound for the other. In particular, depth zero is
the original empirical law. The note retains this distinction.

## Fixed reweighting on the same component

For a positive unit target there are infinitely many legal unit
parents: admissible exponents occur in residue classes, with the
nonunit class omitted. Positivity of the supplied flow gives
`v_k>v_(k-1)` and hence positive mass for every `A_k`, `k>=1`.
The displayed mixture has a finite almost-everywhere integrable
density bounded below by one half. Its marginals define a positive
bounded harmonic flow. This holds because the event at a target
is the disjoint union of its actual parent events, and the future
of a parent is deterministic. The inverse ratios telescope.

The mixture's exact coalescence tail is (15). The optional uniform
fixed-basin sublinearity follows from the same integrable-density
truncation bound uniformly over all cylinder events, even when their
levels vary. The explicit logarithmic weights telescope to one,
and their tail gives (16) with the stated constant. The supremum
can be approximated by a finite inverse clock for each fixed `N`.

This is a conditional reweighting inside a hypothetical actual
escaping component. It does not construct such a component, show
a slow rate for the distinguished canonical flow, or give a lower
bound for the difference of collision probabilities.

## External analytic inputs and review boundary

I directly inspected the exact PR180 `EXTENSIONS.md`, equations
(E13)--(E15): they permit a fixed integrable, possibly unbounded
absolutely continuous path reweighting. I also inspected
`BOUNDARY_OVERLAP.md`, (21), and its following dimension argument.
It quantifies over every fixed reference measure; taking the new
boundary marginal as reference and using equivalence at each fixed
root gives the claimed upper-local-dimension transfer. The countable
root mixture and affine changes retain the source qualifications.
The universal almost-everywhere upper bound for a real probability
measure supplies the other inequality.

The newly constructed density is fixed once, rather than varying
with the resolution. Thus these particular regularity conclusions
survive the reweighting. This review verifies the conditional use
of the pinned analytic inputs, not their entire dependency trees.
It does not claim that every identity defining a canonical trace
construction survives the change of law.

I read Aldous--Fill, Chapter 12, Sections 12.1.1--12.1.2 and (12.3),
from the primary author text:
<https://www.stat.berkeley.edu/users/aldous/RWG/Book_Ralph/Ch12.S1.html>.
The citation supports the coupling methodology. No reversible-chain
or finite-state mixing theorem is imported into these countable
actual-orbit deductions.

No mathematical repair was required. The missing quantitative
property of the distinguished flow, or a direct original-source
residue-pair estimate, is correctly left unproved.
