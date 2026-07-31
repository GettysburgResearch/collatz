# R-6801 — Almost-everywhere dynamics cannot prove every Collatz orbit

**Claim ID:** `R-6801`  
**Title:** Ensemble valuation laws, ergodicity, and probability-zero divergence do not imply pointwise Collatz convergence  
**Status:** **PROVED METHOD FIREWALL**  
**Authoring agent:** `gpt56-positive-entropy-01` (`GPT-5.6 Pro`)  
**Reviewing agents:** none yet  
**Created:** 2026-07-31  
**Last updated:** 2026-07-31  
**Issue:** #75  
**Dependencies:** elementary measure theory; standard quantifiers in Birkhoff and Borel--Cantelli  
**Scope:** claimed proof templates based on distribution across integers or Haar-almost-everywhere orbit genericity

## 1. Exact logical boundary

Let `(X,mu,T)` be a probability-preserving ergodic system and let `f` be integrable. Birkhoff's ergodic theorem gives

\[
\frac1N\sum_{k=0}^{N-1}f(T^kx)
\longrightarrow
\int_X f\,d\mu
\]

for `mu`-almost every `x`.

It does **not** give the convergence for every `x`.

Likewise, a Borel--Cantelli conclusion that an exceptional event has probability zero says that the exceptional set has measure zero. It does not say that the set is empty.

These quantifiers cannot be strengthened without a separate pointwise theorem.

## 2. Why the distinction is maximal for positive integers in `Z_2`

Embed the ordinary positive integers in the `2`-adic integers `Z_2`, equipped with normalized Haar measure.

The set

\[
\mathbf Z_{>0}\subset\mathbf Z_2
\]

is countable and therefore has Haar measure zero.

Consequently, an almost-everywhere theorem on `Z_2` is logically compatible with **every ordinary positive integer** lying in the exceptional null set. The theorem may still be extremely informative, but it supplies no pointwise assertion for one specified ordinary starting value without additional arithmetic input.

This is not a merely technical concern. The Collatz conjecture is exactly a universal statement over that countable exceptional candidate set.

## 3. Ensemble distributions are not orbit distributions

It is elementary that, across odd residue classes modulo powers of two,

\[
\Pr\bigl(v_2(3n+1)=r\bigr)=2^{-r}.
\]

This is a spatial distribution over integers or residue classes.

The pointwise statement

\[
\lim_{N\to\infty}
\frac1N\#\{0\le k<N:v_2(3n_k+1)=r\}
=2^{-r}
\]

for **every** Collatz trajectory is a different theorem. It is not implied by the spatial count.

Even a measure-preserving conjugacy of the `2`-adic Collatz map to a Bernoulli shift gives genericity only almost everywhere. Exceptional periodic and non-generic `2`-adic points remain, and a universal ordinary-integer proof must exclude the relevant exceptions arithmetically.

## 4. Audit of a current claimed proof

The February 2026 preprint

```text
David D. Zelenka,
The Collatz Conjecture Resolved: Funnel Density and the Impossibility of Divergence,
Zenodo 10.5281/zenodo.18626114
```

uses the following chain:

```text
geometric valuation density across integers
 -> trajectory genericity via ergodic theory
 -> divergence has probability zero
 -> divergence is impossible.
```

The final implication is invalid:

```text
measure zero != empty.
```

The public proof page states this inference explicitly as

```text
Probability 0 in deterministic system means IMPOSSIBLE
Measure-zero set of trajectories is empty.
```

That statement is false in measure theory.

Two additional independent gaps are visible in the published presentation:

1. Birkhoff genericity is asserted for every trajectory, whereas the theorem is almost-everywhere.
2. Uniqueness of the positive cycle is treated as an axiom supported by a bounded search and irrationality heuristic; excluding all nontrivial positive cycles is itself an open Collatz subproblem.

Thus this preprint does not establish the Collatz conjecture.

## 5. Relationship to current repository work

The repository's ordinary-extraction packets found the analogous discrete quantifier boundary:

```text
for every depth there exists a positive representative
    does not imply
there exists one positive representative for every depth.
```

`R-6801` is the measure-theoretic version:

```text
almost every 2-adic point is generic
    does not imply
this ordinary integer is generic.
```

Both failures arise from replacing a pointwise universal obligation with an aggregate statement.

`T-6801` and `T-6802` deliberately avoid this error. Their entropy bounds are proved for one fixed ordinary orbit from exact parity-factor divisibility and physical height, with no random-model transfer.

## 6. Current literature disposition

- Angeltveit's 2026 work is a rigorous finite verification algorithm and supplies exact descent sieves; it does not claim pointwise genericity.
- Rozier--Terracol's 2026 journal result analyzes paradoxical finite sequences and their relation to Collatz without claiming global closure.
- Chang's March 2026 map-balance theorem explicitly separates map-level balance from the still-open orbit-level residue-visitation problem.
- Tong Niu's May 2026 note was withdrawn after overlap with Rozier--Terracol and made no Collatz-resolution claim.
- Motimba's July 2026 hut manuscript claims a complete induction proof but is an unreviewed working paper; this packet does not accept or reject it without a line-by-line reconstruction of the full manuscript.

## 7. What a valid probabilistic-to-pointwise bridge would need

A successful proof must add a genuinely pointwise ingredient, for example:

1. a deterministic discrepancy bound for every ordinary orbit;
2. an arithmetic theorem excluding every non-generic `2`-adic orbit from the ordinary positive section;
3. a decreasing well-founded rank verified on every physical transition;
4. a finite certificate that covers all exceptional residue paths;
5. or an ordinary least-root theorem proving the exceptional cylinders escape to infinity.

Without such a bridge, probability and ergodic arguments remain almost-all results.

## 8. Scope boundary

This firewall does not refute probabilistic heuristics, almost-all theorems, or their value in designing deterministic invariants. It refutes only the universal inference from measure-one behavior to every positive integer.

No proof or disproof of Collatz follows from `R-6801` alone.
