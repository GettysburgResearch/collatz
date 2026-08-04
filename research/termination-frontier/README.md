# Termination and obstruction frontier

**Agent:** `gpt56-termination-01`
**Issue:** [#5](https://github.com/gfreund123/collatz/issues/5)
**Packet status:** targeted migration for review; not a canonical project ledger
**Last updated:** 2026-07-21

## What this packet is

This packet ports the high-signal conclusions of a preceding investigation of
Collatz termination methods. It is meant to stop collaborators from having to
reconstruct that investigation from chat history and to expose the few exact
interfaces where a new mechanism could advance it.

It does **not** contain:

- a proof that every Collatz orbit reaches 1;
- a positive integer with a divergent orbit or a nontrivial cycle;
- a terminating interpretation of the full Aaronson--Yolcu--Heule system;
- a claim that failure of a proof template is evidence for a counterexample;
- or a promotion of finite computation to an infinite assertion.

Two short arguments have been made self-contained in
[`CLAIM_INVENTORY.md`](CLAIM_INVENTORY.md). The other items below are
provenance records. They were reported as proved, checked, or computationally
certified in the prior workspace, but their frozen proofs, certificates, and
checker transcripts are not present in this branch. They therefore may not be
used as proved dependencies in this repository until imported and reviewed.

## Repository integration boundary

At the start of issue #5, `main` contained only this project's operating README
and `.gitkeep`. The canonical ledgers named by that README are being proposed in
PR #3, while issue #4 tracks a second, substantially larger migration. This
packet consequently:

- lives under an isolated `research/` directory;
- permanently reserves the `*-9000` identifiers used in this packet;
- does not edit `CURRENT_STATE.md`, `CLAIMS.md`, `OPEN_PROBLEMS.md`, or
  `NEGATIVE_RESULTS.md`;
- does not reuse low-numbered identifiers from either bootstrap effort; and
- asks an integrator to index or alias these stable identifiers after one
  bootstrap becomes canonical, without silently renumbering them.

## External baseline: the AYH rewrite system

The primary external dependency is Aaronson, Yolcu, and Heule, *An Automated
Approach to the Collatz Conjecture*, together with
[`emreyolcu/rewriting-collatz`](https://github.com/emreyolcu/rewriting-collatz).
The source file `rules/collatz-T.srs` has the following eleven rules:

```text
ad -> d
bd -> gd

ae -> ea
af -> eb
ag -> fa
be -> fb
bf -> ga
bg -> gb

ce -> cb
cf -> caa
cg -> cab
```

The six middle rules are the binary--ternary carry squares. If `a,b` denote
binary digits `0,1` and `e,f,g` denote ternary digits `0,1,2`, then each rule
rewrites the same number in the identity

$$
  3i+j=2j'+i',\qquad i,i'\in\{0,1\},\quad
  j,j'\in\{0,1,2\}.
$$

The boundary and preprocessing rules connect this local carry engine to the
accelerated Collatz map. The published reduction makes termination of the full
mixed-radix system equivalent to Collatz convergence. That reduction is cited
background here, not a new repository theorem: its complete proof is not
reproduced in this port.

The published computational frontier was also taken as background rather than
rerun: proper subsystems admit generated termination certificates, while the
full eleven-rule system remains the unresolved case. Targeted dependency-pair
inspection in the prior session localized the difficulty to the boundary-coupled
carry core; merely eliminating obviously noncanonical suffixes did not solve it.

## Results inventory from the prior workspace

The table deliberately separates the status reported in the prior workspace
from the admissible status of this port.

| Topic | Prior-work report | Repository admission/evidence class | Evidence needed before promotion |
| --- | --- | --- | --- |
| Periodic carry-cocycle rigidity | Exact theorem; adversarial audit reported accepted | unadmitted legacy lead; not a registered claim | Frozen theorem, full determinant proof, exact checker, independent repository review |
| Finite additive-processor obstruction | Derived from carry rigidity | unadmitted legacy lead; not a registered claim | Imported parent theorem and full implication proof |
| Nonnegative tropical top/DP obstruction | Exact all-dimension theorem; adversarial audit reported accepted | unadmitted legacy lead; not a registered claim | Exact extended-algebra semantics and complete coefficient-order proof |
| Natural matrix interpretation collapse results | Several exact no-go theorems and one surviving selector | unadmitted legacy lead; not a registered claim | Proofs for each eliminated extension class |
| Arctic critical-saturation analysis | Exact structural theorem plus bounded UNSAT runs | unadmitted legacy lead; not a registered claim | Frozen solver instances, certificates/logs, and independent checker |
| Canonical match-height obstruction | Exact unbounded family | `L-9001`, `PROPOSED` | Independent review |
| Least-component interval game | Exact finite-horizon theorem; adversarial audit reported accepted | unadmitted legacy lead; not a registered claim | Cone-invariance proof and checker |
| Cycle-sibling minimum correction | Exact logical refutation | `R-9001`, `PROPOSED` | Independent review |
| Positive rational cyclic-model family | Exact family reported; not integral | unadmitted legacy lead; not a registered claim | Exact mechanical-word parameterization and divisibility audit |
| Invariant-component generating function | Exact functional equations and analytic corollary reported | unadmitted legacy lead; not a registered claim | Full proof, hypotheses of the analytic theorem, endpoint conventions |

### Periodic carry-cocycle rigidity

The prior theorem can be frozen succinctly as follows for future import. On
`V = Z/mZ`, define digit edges

$$
 A_i(x)=2x+i\quad(i=0,1),\qquad
 E_j(x)=3x+j\quad(j=0,1,2).
$$

For every carry identity `3i+j=2j'+i'`, a real edge-weight cocycle was required
to satisfy the mixed-square equation

$$
 u_i(x)+v_j(A_i x)=v_{j'}(x)+u_{i'}(E_{j'}x).
$$

The reported classification was that every such periodic cocycle has the form

$$
 u_i(x)=\alpha+\phi(A_i x)-\phi(x),\qquad
 v_j(x)=\beta+\phi(E_j x)-\phi(x).
$$

Thus only one binary charge, one ternary charge, and a vertex coboundary remain.
The proof reportedly used a Poisson gauge, Fourier mixed paths, the Smith normal
form controlled by `|3^a-2^b|`, a lattice-shuffle recurrence, cyclic interval
autocorrelation, vanishing mixed traces, and Newton identities. The important
consequence was a no-go result for finite deterministic nonnegative additive
processors that weakly orient the carry core while making a marked leading pair
strict. The all-odd family from `2^K-1` to `3^K-1` eliminates the two charges;
bounded vertex potential then conflicts with repeated strict visibility.

This is a particularly valuable import target, but it is not admitted as a
theorem in this branch without the proof and checker.

### Tropical interpretation obstruction

The reported theorem concerns the specific nonnegative tropical extended
weakly-monotone algebra and all-coefficient strict order used in the AYH
relative-termination experiments, not every object called a tropical
interpretation. Weak monotonicity forces a zero-weight seed in the distinguished
row of every generator; composition propagates a zero seed to every nonempty
word. If a rule is weakly oriented, nonnegativity forces the corresponding
right-hand coefficient also to be zero. The all-coefficient strict comparison
then fails at `0 = 0`. In that template, no nonempty rule can be removed as
strict, regardless of dimension or coefficient bound.

Promotion requires importing the exact coefficient order and distinguished-row
conventions. The statement must not be generalized beyond that template.

### Natural matrix frontier

The prior analysis reported the following structural information.

- On an irreducible Perron-critical natural block with critical radius 5,
  integrality forces deterministic transitions and makes the affine carry gaps
  exact.
- Scalar periodic cohomology does not automatically lift to matrix-valued
  Frobenius extensions. A concrete `Z/5` self-extension
  `X_s = kappa_s (J-U_s)` produced endpoint-dependent polynomial terms.
- Block-sum projection still works on the Perron block; permutation target
  delimiter columns align automatically.
- The smallest surviving nonpermutation target had three states with maps

  ```text
  a = (0, 2, 1)       b = (1, 0, 2)
  e = (0, 0, 0)       f = (1, 1, 1)       g = (2, 2, 2)
  ```

  where a tuple records the image of states `0,1,2`.
- Direct affine return, a one-state intermediate selector path, dead transients,
  the first rational self-extension, and every depth of the canonical Toeplitz
  self-extension were reported to collapse by exact linear or block-flux
  arguments.

The first mechanism not covered by those collapses is a genuinely multi-state
intermediate selector block. This is recorded as open question `Q-9001`.

### Arctic frontier

With `P = max(A,B)` and `Q = max(E,F,G)`, the reported critical-saturation
theorem says that `PQ >= QP` together with equal tropical spectral radii makes
every edge on a `QP`-critical cycle exact. A separate transient-latch example
showed why spectral recurrence alone does not force a marked rule to be visible.

Two exact bounded searches were reported:

```text
dimension 2, rule weight 4, natural weight 1: UNSAT
  1887 variables, 9234 clauses

dimension 3, rule weight 5, natural weight 2: UNSAT
  7695 variables, 44195 clauses
```

The solver inputs and logs are not in this branch, so these figures are
historical provenance, not admitted experiment records. A support-only audit
was satisfiable; its smallest skeleton had a dead escape edge. The unresolved
mechanism is therefore a core-specific interacting transient return, recorded
as `Q-9002`.

### Canonical match bounds

`L-9001` supplies a complete short derivation showing unbounded standard match
height already on canonical strings, using only `ae -> ea`. It rules out an
ordinary finite global match bound. It does not rule out relative, contextual,
semantic, or otherwise strengthened match-bound methods.

### Least-component interval game

The reported finite-horizon theorem is precise. Given arbitrary `R,K >= 1`, CRT
produces a positive odd integer

$$
 m\equiv-1\pmod {2^{R+1}},\qquad m\equiv0\pmod {3^K}.
$$

For `Q(x)=(3x+1)/2`, the first `R` odd-only exponents are all 1 and

$$
 Q^j(m)+1=(3/2)^j(m+1),
$$

so this forward segment is strictly increasing. For each `0 <= j <= R`, every
valid inverse word `P_a(y)=(2^a y-1)/3` of length at most `K+j` from `Q^j(m)`
was shown to stay at least `m`. The proof reportedly uses the dyadic cone
`z_d=(3/2)^d-1`, invariant under every valid inverse branch.

This blocks fixed-horizon least-component arguments whose required witness is a
value below `m` inside the inspected forward/inverse window. It does not block
every method that uses local information, does not construct a compatible
infinite orbit, and must not be extended beyond the stated finite horizon.

### Cycles, siblings, and integrality

`R-9001` records the basic logical correction: membership in a weak component
only bounds a vertex below by the least member of the whole component, not by
the least vertex of its cycle.

Even after granting the stronger, generally unjustified cycle-minimum bound, the
prior workspace reported an infinite continued-fraction family of positive
rational cyclic models satisfying the tested sibling, product, logarithmic, and
reciprocal inequalities. The family began with eight exponent-1 entries, then
6, followed by mechanical 1/2 digits and a final 2. Its full parameterization is
not available here, so it remains provenance only. More importantly, rational
cyclic models are not integer Collatz cycles: the divisibility conditions in

$$
 x_i=\frac{B_i}{2^{\sum a_j}-3^\ell}
$$

are essential. This tested package therefore admits rational false positives.
The result redirected the cycle program toward Cramer-style integrality and
divisibility rather than further use of that same real-inequality package.

### Invariant components

For a component indicator `s_n`, the prior analysis derived

$$
 s_{2m}=s_m,\qquad s_{2m+1}=s_{3m+2}.
$$

Writing `F(z)=sum s_n z^n` and using Cartier operators gave

$$
 \Lambda_{2,0}F=F,\qquad \Lambda_{2,1}F=\Lambda_{3,2}F,
$$

and

$$
 F(z)=F(z^2)+z(\Lambda_{3,2}F)(z^2).
$$

The reported corollary was that every finite-valued rational solution is
constant and, via Pólya--Carlson, every nonempty proper invariant-component
indicator has the unit circle as a natural boundary. This does not exclude such
a component; it rules out rational, algebraic, and D-finite ordinary generating
functions (and hence unary finite-state/eventually periodic descriptions). It
does not rule out automatic descriptions in general. The proof and analytic
hypotheses must be imported before this becomes a repository theorem.

## Relationship to counterexample construction

These are method-specific constraints, not probabilistic evidence for or
against Collatz. Their constructive value is in narrowing what a credible
counterexample certificate would have to contain:

1. A finite-state additive carry potential is unlikely to certify the needed
   infinite behavior; the periodic cocycle theorem should be imported and
   tested against any such proposal.
2. Bounded residue or inverse-tree windows can be adversarially realized by CRT
   without yielding an infinite orbit. A candidate assembled from finite
   prefixes must separately prove infinite compatibility and positivity.
3. The tested sibling/product/logarithmic/reciprocal inequality package admits
   rational false positives. Exact integrality and divisibility are an
   indispensable additional layer.
4. A proper invariant component, if used to host a counterexample, cannot have
   a rational, algebraic, or D-finite ordinary generating function under the
   reported theorem.
5. In the AYH termination direction, the identified uneliminated mechanisms are
   richer stateful return paths, not a larger blind sweep over already-collapsed
   scalar templates.

## Exact next interfaces

The packet recommends only attacks that cross a presently identified boundary:

- **`Q-9001`: multi-state natural selector.** Classify a selector path with an
  intermediate block of at least two genuinely interacting states. Either
  produce an independently checkable interpretation or extend the block-flux
  obstruction to this case.
- **`Q-9002`: arctic transient return.** Prove or refute that a transient
  strongly connected return interacting with the critical core can carry strict
  marked visibility. Support-only or dead-edge models do not answer this.
- **Proof import.** Recover the periodic carry-cocycle proof and its small exact
  checker first; it is the broadest reusable obstruction in the packet.
- **Counterexample-side transfer.** Test proposed symbolic collision amplifiers
  for the two recurring gaps: finite-prefix compatibility and integer
  divisibility. Do not substitute a finite automaton or a rational cyclic model
  for either proof.

## Review order

1. [`CLAIM_INVENTORY.md`](CLAIM_INVENTORY.md) for the two self-contained claims
   and the two open questions.
2. This file's status boundary and result inventory.
3. The session report under `reports/gpt56-termination-01/` for integration and
   provenance details.
