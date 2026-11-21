# Lean attack on global Collatz closure

**Checkpoint 1: the full theorem is OPEN.** Three concurrent attacks targeted
the missing global implication: paired reverse closure, an unbalanced
certificate normalizer, and inverse pressure. This packet contains the
completed Lean components and records precisely where each closing argument
still needs a theorem. It does not add a convergence axiom.

The map is the ordinary shortcut map on natural numbers:
\(T(n)=n/2\) for even \(n\), and \(T(n)=(3n+1)/2\) for odd \(n\).
The imported predicate `Basin n` means that an actual finite orbit reaches
one. The convergence problem concerns positive starting values.

## Arbitrary-length paired descent

For natural \(r,v,m,u\) satisfying

\[
3m=4^{r+1}v+2,\qquad 2u=3^rv+1,
\]

Lean proves

\[
T^{2r+3}(m)=u,\qquad
T^{2r+3}(3m-1)=3u-1,\qquad 0<u<m.
\]

Each arm has exactly \(r+1\) odd inputs. The displayed guards imply the
required positivity and parity. A reverse closure failure
`¬Basin m ∧ Basin (3*m-1)` therefore descends to the same failure at \(u\).
This treats every positive even valuation of \(3m-2\), with no bound on
the run parameter. The minimum in `not_minimal_failure` is taken over
**all positive reverse-failure bases**; the new base need not remain in the
\(27k+1\) progression of PR174's restricted open lemma.

Source: [Closure/PsiDescent.lean](lean/Closure/PsiDescent.lean), especially
`paired_descent`, `failure_descends`, and `not_minimal_failure`.

## Expanding returns and a finite ordinary budget

The proposed rule that every balanced paired return decreases is false.
For every natural \(t\), set

\[
m=2469887+4194304t,\qquad q=2816534+4782969t.
\]

Lean checks the exact 22-step return
\((m,3m-1)\longmapsto(q,3q-1)\), with 14 odd inputs on each arm and
\(q>m\). It also checks that this is the first positive balanced return
along these paths. These are entire ordinary integer cylinders, with
literal map evaluations, not just slope comparisons or completion points.

The positive continuation is also kernel-checked. Define
\(E(m)=588665m+6867833\). Any \(k\) consecutive returns of this cylinder
satisfy \(2^{22k}\mid E(m)\). Thus one fixed ordinary source cannot repeat
this expanding return indefinitely. If those \(k\) blocks are followed by
the paired contraction with parameter \(r\ge k\), Lean proves
\(8u\le3m+40\), hence \(u<m\) for \(m\ge9\), with the actual paths
and reverse-failure transfer included.

For example, it proves the whole 29-step descending cylinder
\(m=2469887+2^{29}t\) to \(u=594113+3^{17}t\), on both paired arms.
The [closure route note](closure/README.md) states the exact guard.
**Forcing a paying exit for every relevant source remains open.** Finite
escape from one expanding cylinder does not establish that global step.

## Exact correction synthesis with arbitrary budgets

[Descent/Correction.lean](lean/Descent/Correction.lean) supplies an exact
kernel for a possible total certificate compiler. For any positive exponent
word \(w\), an odd endpoint \(q\), and the usual affine correction \(B(w)\),

\[
2^{\sum w}q=3^{|w|}n+B(w)
\]

is equivalent to the word being an actual ordinary odd Collatz path from
\(n\) to \(q\). Every intermediate divisibility and exact parity guard is
derived, and the path is connected to exactly \(\sum w\) shortcut steps.
The endpoint-one specialization proves the existing `Basin` predicate.

The arbitrary-target equation permits both clock and odd rank to increase
or decrease. However, `head_budget_independent` and `prefix_budget_cancel`
show that changing those prospective budgets cannot change the next actual
odd exponent. The missing result is a **total successful choice of a legal
word**, not an algebraic identity for proposed budgets. This is a formal
implementation of correction principles already present in the repository,
with the new arbitrary-budget interface and explicit scope in the
[route note](descent/README.md).

## Inverse pressure and the missing global estimate

[Global/InversePressure.lean](lean/Global/InversePressure.lean) proves exact
finite-cutoff identities for the affine inverse branches and constructs
ordinary positive paths and reset families. It checks a failure of
pointwise contraction for every positive finite-period rational coefficient
times an integral power of degree 0 through 3. For every integral degree
at least 4, it proves a linear lower bound for all finite root-predecessor
pressure sums.

The attractive quadratic contraction under probability weights
\(15/16^a\) does not survive restoration of the fourth-Jacobian mass:
its factor changes from \(5/9\) to 3. The probability estimate alone
does not supply the required global negative-moment bound. Infinite sums,
real degrees, and mixed valuation weights have a separately stated written
proof boundary; they are not advertised as Lean theorems. See the
[inverse-pressure note](global/README.md).

## Reproduce the formal checkpoint

Use Lean 4.34.1; this project has no external package dependencies:

```sh
cd research/lean-global-target-20261121/lean
lake build
lake env lean -DwarningAsError=true CheckpointAudit.lean
```

Alternatively, run `check_lean.py` with `--lake` pointing to the desired
Lake executable and `--receipt` pointing outside the checkout. It records
the commands, source hashes, compiler identity and printed theorem axioms.
It rejects any audited dependency outside `propext`, `Classical.choice`,
and `Quot.sound`, and checks the imported file identities.

The audit also prints the type of the imported
`collatz_of_open_lemma` and the definition of its explicit `OpenLemma`
hypothesis. Checking that conditional implication does not discharge
the hypothesis.

The four imported Collatz modules are byte-identical to the pinned PR174
sources. [SOURCES.md](SOURCES.md) and
[upstream-files.json](upstream-files.json) record their provenance. Runtime
binaries and build caches are not committed. Execution records and publication
scope are kept in [the checkpoint report](../../reports/2026-11-21-lean-global-target/README.md).
