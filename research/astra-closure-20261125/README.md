# Source-dependent closure attempt — 25 November 2026

**Collatz remains OPEN. No unconditional final Lean proof was obtained in this pass.**

The new positive arithmetic result is a literal 30-shortcut merger for an entire ordinary ternary residue class. It eliminates that class from an actual least-bad-triple configuration. It also defeats a rational-cycle family that had simultaneously passed all our shallower inverse-ancestor and local-denominator tests. The packet also proves a sharp count of ordinary sources failing every forward clock test, with the original clocks and supplied initial history retained, and develops a global Fourier criterion using the idempotent theorem.

[Final Lean proposal](FinalProposal.lean) · [Root reconstruction and scope](../../reports/astra-closure-20261125/ROOT_REVIEW.md) · [Literature inputs](LITERATURE.md)

## The actual ordinary merger

For every odd positive integer
\[
 s\equiv187605073\pmod{1162261467},\qquad1162261467=3^{19},
\]
there is a positive multiple of three \(y<2s+1\) such that
\[
                         T^{30}(y)=T(s).
\]
The proof supplies the complete affine family
\[
\begin{aligned}
 s&=187605073+2324522934t,\\
 y&=259975167+3221225472t,\qquad t\ge0.
\end{aligned}
\]
There are 19 odd departures along the 30-shortcut source path. Its exact parity cylinder lifts the finite seed calculation to every \(t\). The endpoint \(T(s)\) may be even; no extra odd-return assumption is needed.

Consequently, if \(3q=2s+1\) is the actual least bad positive multiple of three and its orbit component contains this \(s\), the certificate gives a smaller good multiple in the same component, a contradiction. Both the arithmetic family and this application are kernel-checked. The theorem uses the actual component hypothesis; a rational model with similar local inequalities does not supply it.

[NineteenMerger.lean](cycles/NineteenMerger.lean) · [FinalProposal.exclude_nineteen_residue](FinalProposal.lean) · [Merger derivation and remaining finite-window controls](cycles/MERGER.md)

## The full-proof endpoint

The final module uses the ordinary shortcut map and the resident exact merger checker. Its open premise is:

> At the actual least bad positive multiple \(3q\), supply a positive smaller multiple \(3v\), together with two finite clocks at which their ordinary trajectories meet.

The final theorem has the form

~~~lean
theorem final_lean_proposal (selector : Nat → Certificate)
    (coverage : ∀ q, FirstFailure q → check q (selector q) = true) :
    ∀ n, 0 < n → ∃ k, run k n = 1
~~~

The implication is proved, and the equivalence of the stated closure condition with Collatz is checked. **The selector and its universal coverage proof are not supplied.** This interface is an explicit integration endpoint, not a new solution or a way of replacing the missing argument with an axiom. The new merger excludes one infinite source family from that endpoint; it does not cover all remaining sources.

## What the competing closure attempts established

| Attempt | Result in this packet | Remaining pointwise step |
|---|---|---|
| Exact inverse-ancestor descent | The ordinary residue merger above; its genuine least-basin application | A mandatory merger for every remaining least source |
| Tower induction | For every two-arm deadline, cofinally many actual powers \(3^{3m+1}\) miss every earlier power through that deadline. Exponentially many maximum-weight prefixes have cofinal ordinary power realizations | A source-dependent exit or merger at the prescribed exponent |
| Whole-denominator arithmetic | A fixed finite prime set's **full varying prime powers** can be canceled on wide rational cycles while preserving both rotation orders and all stated depth-16/17 ancestor tests. The same family is subsequently ruled out by the 19-departure merger under true minimality | A proof treating all remaining ordinary words and their genuine basin information |
| Forward clock and inverse amplification | A sharp all-prefix row estimate, an injection bounding all failing visits to a fixed gate, and exact dependence of the last-crossing choices after merger | Exclude the fixed ordinary representative, rather than count all representatives of its cylinder |
| Exact orbit invariance | A rooted disagreement forces many incoming starts, with an actual delayed crossing. The mass is on predecessor basins, not on distinct disagreement vertices | Control their incoming multiplicities with the original source still fixed |
| Global Fourier rigidity | Bounded lower limit of the symmetric Fejér integral norms is equivalent, in the written proof, to full Collatz. The arithmetic implication from eventual periodicity is kernel-checked for arbitrary colors | Bound the sum of the exact dyadic norm overshoots for the actual convergence predicate |

[Descent proofs and ordinary realization](descent/README.md) · [Invariant-color attack](descent/ATTEMPT.md) · [Joint cycle theorem](cycles/JOINT.md) · [Finite inverse-language computation](cycles/BASIN.md) · [Forward-clock proof](escape/README.md)

## The global literature route

For the actual nonconvergence indicator \(b(n)\), set \(b(0)=0\) and
\[
 K_N(t)=\sum_{|k|<N}(1-|k|/N)b(|k|)e^{2\pi i kt}.
\]
A bounded subsequence of \(\|K_N\|_1\) gives a finite measure with these Boolean Fourier coefficients. The Cohen–Helson–Rudin idempotent theorem then gives eventual periodicity of the positive coefficient sequence. The new Lean theorem proves that every eventually periodic coloring preserved by both actual shortcut branches is constant on positive integers. Applied to the actual convergence predicate, this proves universal convergence.

The written analysis derives the exact nonnegative increment
\[
 \|K_{2N}\|_1-\|K_N\|_1
 =\int (|K_{2N}(t)-K_N(2t)|-|K_N(2t)|)_+\,dt.
\]
Summability along dyadic \(N\) is the open analytic requirement. The available adjacent-absorption estimate gives an improved ceiling \(O(\sqrt N/(\log N)^{1/8})\), which does not imply summability. An actual mark for visiting 5, with exactly one defective odd edge, has divergent norms despite that ceiling. This tests the use of exact invariance.

[Full Fourier argument](global/README.md) · [PeriodicColor.lean](global/PeriodicColor.lean) · [Independent review](../../reports/astra-closure-20261125/GLOBAL_REVIEW.md)

## Forward-clock results

For the forward criterion, write \(S_j\) for the total division exponent through \(j\) odd returns. On every complete ordinary row, the fraction failing
\[
                         2^{6S_j}>(j+1)3^{6j}
\]
at **every** \(j\le n\) is
\[
 \Theta\!\left(0.946504577\ldots^{\,n}
                  n^{-1.426994557\ldots}\right).
\]
The same exponent holds after fixing any one admissible initial gap history, with constants allowed to depend on that fixed history. It is a written theorem using Caravenna's conditioned lattice local limit theorem. It is not a theorem about the future parities of one fixed integer.

The Lean visit injection gives, on paper by counting its finite target rectangle, at most
\[
                  6g^2\left\lceil(N+1)^{1/6}\right\rceil
\]
original source/native-clock pairs reaching a fixed odd gate \(g\) at a failing clock through odd grade \(N\), including repeated cycle visits. The sharper all-prefix bound and exact merger dependence are proved in the accompanying note. None of these estimates assumes a renewal floor.

## Evidence and reproduction

The Lean replay builds eight new modules and two resident imports in an empty project object directory. It reuses the dependency cache for Mathlib at d13f23b723b8a846827a245b89c10fc7d3f11612 and Lean 4.34.1. All 36 public theorem declarations in the new modules, plus 18 resident declarations, are audited transitively. Their axiom lists contain only subsets of propext, Classical.choice and Quot.sound. The analytic row theorem, full rational-cycle construction and Fourier analysis remain written proofs.

~~~sh
python -B research/astra-closure-20261125/check_lean.py \
  --lean /path/to/lean-4.34.1/bin/lean \
  --mathlib /path/to/mathlib4 \
  --receipt /tmp/collatz-closure-lean.json

python -B research/astra-closure-20261125/check_controls.py \
  --receipt /tmp/collatz-closure-finite.json

python -B research/astra-closure-20261125/cycles/check_merger.py
python -B -O research/astra-closure-20261125/cycles/check_merger.py
~~~

[Lean receipt](../../reports/astra-closure-20261125/LEAN_REPLAY.json) · [Finite receipt](../../reports/astra-closure-20261125/FINITE_REPLAY.json) · [Merger replay](../../reports/astra-closure-20261125/MERGER_REPLAY.json) · [Independent analytic review](escape/DESCENT_REVIEW.md) · [Independent joint-cycle review](cycles/ESCAPE_REVIEW.md)

The finite programs check actual ordinary rows, exact signed polynomial switches, rational-cycle replay, all indicated inverse-ancestor guards, and an ideal finite-memory language. Their scope is distinct from the written asymptotics and universal convergence. The first failed root Lean integration, a tactic normalization timeout, is preserved separately; the revised integration compiled successfully.

## Current-source intake

The complete all-state PR inventory contains 168 entries. Mathematical intake focused on the current heads of PR192, PR195, PR197, PR206, PR207, PR208 and PR209, together with the resident proof interfaces. We used their newly developed source-dependent descents, all-shift cycle constraints, exact clock rows and 116-exponent coverage. The inventory is not a claim that every statement on every branch was re-proved. [Frozen intake](../../reports/astra-closure-20261125/INTAKE.json)

Late updates to PR192 at 07d494324c7ea440d45845d725f5cebad8a67124 and PR206 at 45a6a111321f947a8482c9e96e898435b57cee09 were read before publication. Their new single-orbit rational/Mahler representations and simultaneous tower-merger windows do not prove their respective universal premises. The across-start Fourier predicate is distinct from PR192's time series along one supplied orbit. [Late intake](../../reports/astra-closure-20261125/LATE_INTAKE.json) · [PR206 reconstruction](../../reports/astra-closure-20261125/LATE206_REVIEW.md)

The first unsupported universal inference is still SourceClosure. The packet supplies new exact certificates and tests combinations of the latest approaches, while preserving that boundary.
