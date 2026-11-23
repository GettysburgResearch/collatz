# The central step: canonical escape charge

**Collatz is not proved by this checkpoint.** The objective of this pass was
to remove the surviving ordinary escape contribution, or to obtain a total
source-to-target descent. The work below proves two global statements about
that contribution and attacks the missing arithmetic comparison directly.
The comparison and the universal descent remain open. Nontrivial periodic
cycles are a separate unresolved obligation in the analytic domain used here.

The source refresh covered metadata for all 122 open PRs and then concentrated on the
changed work in PR175, PR176, PR177, and PR185, together with PR183's existing
ordinary Wold decomposition and our previous contact construction. Exact
commit pins are in [SOURCES.json](SOURCES.json) and in each proof note.

## 1. New global result: the exact boundary at every moving cutoff

Let `nu` be the repository's source-qualified ordinary harmonic reference,
`d` its finite canonical immigration, and `R_M` the first `M` terms of the
inverse Green potential `R`. On a hypothetical escaping component, choose
an actual source `x`, write `q_k=U^k(x)`, let `C_C` be the limiting ordinary
capacity, and let `ell_x` be the actual integer clock normalized at `x`.
Define

\[
\Phi_x(s)=\sum_{\ell_x(n)>-s}d(n).
\]

The new proof retains each original source and obtains

\[
\sup_{M\ge0}\left|R_M(q_k)-\frac{\Phi_x(M-k)}{C_C}\right|\longrightarrow0.
\]

This is uniform over **all** cutoffs, including an adaptive cutoff selected
from the observed orbit. A corresponding global formula retains the entire
original finite measure `d`. Its adjacent clock offsets give the exact
finite-Green energy defect

\[
\boxed{\lim_{M\to\infty}\mathcal D(R-R_M)=E_{\rm sync},\qquad
E_{\rm sync}=\sum_{C\ \mathrm{escaping}}\frac1{C_C}
\sum_{r\in\mathbb Z}\left(\sum_{h_C(n)=r}d(n)\right)^2.}
\]

The same calculation gives
`lim D(R_M)=D(R)+E_sync`. Every source has positive canonical charge, so
`E_sync=0` holds exactly when there are no escaping components. The formula
computes the quantity a strong approximation argument would have to remove;
it does not establish that it is zero. The existing Wold interpretation is
credited to PR183. The new results are the uniform moving-cutoff profile and
its application to the canonical Green approximation defect.

**Evidence:** complete source-qualified written proof, independently reviewed.
The infinite theorem is not formalized in Lean.

[Proof and direct closing attack](CRITICAL_BOUNDARY.md) ·
[Independent review](REVIEW_BOUNDARY.md)

## 2. New global result: the actual centered stopping clock is controlled

The previous finite contact reference can control the actual inverse clock,
provided the forward clock is retained. At an actual first-contact endpoint
`z` reached backwards from `U^k(p)`, the exact identity is

\[
\tau-k=h_C(p)-h_C(z).
\]

One finite measure on the original source labels and contact endpoints makes
the positive tails of this centered clock uniformly small. Bounded stopping
then proves, for the unchanged original weights `w_n=n^-4` and their supplied
unit projection `p_n`,

\[
\lim_{R\to\infty}\sup_{k\ge0}
\sum_{n\ \mathrm{still\ retained}}w_n
\left(\frac{P^{k+R}V(U^kp_n)}{G(U^kp_n)}-1\right)=0.
\]

This uses the established monotone harmonicization `P^m V` decreasing to
`G`. It does not assume pointwise convergence of the finite densities `D_m`
at ordinary integers. The proof also identifies the exact remaining
oscillation if one tries to substitute those densities.

The closing implication was tested: the required total inverse depth grows
as `k+R`, whereas the existing whole-ancestor finite-density horizon is fixed
by the component's minimum. Raising that floor removes the original atom
and restores it as boundary immigration. The new clock control therefore
approaches the surviving canonical amplitude without proving that amplitude
small.

**Evidence:** complete source-qualified written proof, independently reviewed.

[Proof and arithmetic comparison test](STOPPED_MIXING.md) ·
[Independent review](REVIEW_STOPPED.md)

## 3. The direct arithmetic attempt

For every odd ternary unit, `B(n)=64n+21` is a distinct actual sibling:
`U(B(n))=U(n)`. A hypothetical escaping path has a persistent linear canonical
spike `G(q_k)>=eta*q_k`, while its total relative sibling current is summable.
In particular

\[
\mathcal L_G(n)=\sum_{j\ge1}64^{-j}\frac{G(B^j(n))}{G(n)}
\quad\hbox{satisfies}\quad
\sum_k\mathcal L_G(q_k)<\infty.
\]

A uniform lower bound

\[
\boxed{\mathcal L_G(n)\ge\frac{c_\eta}{\log(2+n)}
\quad\text{on sufficiently large ordinary points with }G(n)\ge\eta n}
\]

would contradict escape directly on the retained domain, since the ordinary forward height is at
most exponential in its clock. This comparison is **OPEN**. A fully finite
obstacle formulation in the proof note avoids assuming a limit for `D_m`.

The attempted direct transfer of a high-density inverse witness has a sharp
arithmetic cost. Copying a depth-`r` word to `B^j(n)` can be integral only
when `3^(r-1)` divides `j`. The first possible copy therefore costs a sibling
height factor `64^(3^(r-1))`. Repairing the valuation word at much lower cost
is the unresolved step. This obstruction to copying does not disprove an
adaptive repair. Finite isolated-density examples also do not refute the
required high-linear comparison.

The independent source-induction attack pursued a total target merger at
globally irreducible source certificates. It did not obtain one. Its negative
rational shadow test and adaptive carry calculations identify the exact
unproved return rather than adding that return as a hypothesis to a claimed
solution.

The exact shadow pair `x=-6005/2187`, `y=8x+19=-6487/2187` refutes one
proposed coefficient bridge: the source reaches 1 with gaps
`[2,2,2,2,2,2,1]` and every odd-prefix coefficient contracts, while the
target has an expanding coefficient at every positive shortcut clock and
enters the negative cycle `-7,-10,-5`. This is a rational-shadow certificate;
it does not give a complete positive integer realization of the source
conditions or a positive integer counterexample to Collatz.

[Universal-source attempt](UNIVERSAL_SOURCE.md) ·
[Independent review](REVIEW_SOURCE.md)

## 4. Lean scope and replay

The module [CentralCurrent.lean](lean/CentralCurrent.lean) checks the
actual sibling family for every ordinary unit and every sibling index,
the failure of identical-word lifting at every depth at least two, and the
finite original-source pair-clock identity underlying the two adjacent
boundary offsets. [RationalShadowTest.lean](lean/RationalShadowTest.lean)
checks the exact source gaps and target states of the shadow pair, the
source's complete contracting coefficient sequence, and the target's
expanding coefficient at every positive ordinary clock. Their public statements are listed in
[THEOREMS.json](THEOREMS.json). No infinite analytic theorem or missing
comparison is installed as a Lean axiom.

The replay builds the four pinned local dependencies, both new modules, and
a separate complete axiom audit in a fresh output directory. It uses the
repository's pinned Lean and Mathlib versions and treats warnings as errors:

```sh
python research/central-step-20261122/check_lean.py \
  --mathlib /path/to/pinned/mathlib4 \
  --lean /path/to/pinned/lean \
  --report-dir reports/2026-11-22-central-step
```

[Replay receipt](../../reports/2026-11-22-central-step/lean-check.json) ·
[Replay log](../../reports/2026-11-22-central-step/lean-build.log)

The next mathematical step is an actual arithmetic lower bound on the
persistent-spike sector, or a universal target return. The results above do
not supply either statement.
