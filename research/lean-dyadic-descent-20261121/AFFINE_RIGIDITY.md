# The affine translation in the regularity argument

**Status: finite and algebraic Lean theorems; not an ordinary convergence
theorem.** [AffineRigidity.lean](AffineRigidity.lean) checks the elementary
rigidity mechanism used by the written
[all-frequency approximation argument](LITERATURE_RIGIDITY_BRIDGE.md).
It does not formalize that argument's measure theory or its external
stationary-density and predecessor-population inputs.

## 1. A useful exact calculation

Let `G` be an additive abelian group, let `w` be a specified element, and
suppose multiplication by six is onto. Let `f:G->A` have an arbitrary
codomain. Assume the two exact identities

\[
 f(2x)=f(x),\qquad f(3x+w)=f(x).
 \tag{1}
\]

Two compositions give

\[
 f(6x+w)=f(x)=f(6x+2w).
 \tag{2}
\]

For any `y`, choose `x` with `6x=y-w`. Substitution in (2) yields

\[
 \boxed{f(y+w)=f(y).}
 \tag{3}
\]

This is `translation_invariant`; the exact composition is
`adjacent_affine_values`. No probability, limiting argument, or independence
assumption is involved. In particular, the translation is the same `w`
as in the original affine branch.

Iterating (3) gives `f(y+n*w)=f(y)` for every natural `n`, checked by
`translate_nsmul`. Two distinct conclusions are then available:

- If every element of `G` is a nonnegative multiple of `w`, then `f` is
  constant (`cyclic_affine_constant`).
- If `G` has a topology, the nonnegative multiples of `w` are dense, and
  `f` is continuous into a Hausdorff space, then `f` is constant
  (`continuous_affine_constant`). The proof uses equality of continuous
  functions on a dense set. No compactness assumption is needed for this
  algebraic consequence.

This calculation is standard affine-group reasoning. It is supplied as a
small checked interface for the present argument, not claimed as a new
general rigidity principle.

## 2. The averaging step needs its own proof

For permutations `p,q` of a finite set `I`, suppose a real function satisfies

\[
 2f(x)=f(p(x))+f(q(x)).
 \tag{4}
\]

It would be invalid to obtain each branch identity merely by treating the
two summands separately. The valid step is the complete quadratic energy:

\[
 \begin{aligned}
 \sum_x\bigl(f(p(x))-f(q(x))\bigr)^2
 &=2\sum_x f(p(x))^2+2\sum_x f(q(x))^2-4\sum_x f(x)^2\\
 &=0.
 \end{aligned}
 \tag{5}
\]

The first equality uses (4), and the second uses both permutations.
Nonnegativity forces every difference to vanish; (4) then gives
`f(p(x))=f(q(x))=f(x)`. This is
`finite_harmonic_invariant`.

Surjectivity of multiplication by six makes both `x -> 2x` and
`x -> 3x+w` onto. On a finite group these maps are permutations, so (5)
and (3) prove `finite_cyclic_harmonic_constant`. There is no uniform
spectral-gap or mixing-rate conclusion as the finite group changes.

## 3. Transfer from the actual shortcut-shaped branches

On the auxiliary groups of the written argument, multiplication by two
is an additive automorphism. Let `half` be its inverse, with
`2*half(x)=x`. The two branches are

\[
 F_0(x)=\operatorname{half}(x),\qquad
 F_1(x)=\operatorname{half}(3x+w).
 \tag{6}
\]

If `f(F_0(x))=f(x)` and `f(F_1(x))=f(x)`, applying the first identity to
`2x` and to `3x+w` proves (1). This is `shortcut_to_affine`. Therefore:

| Checked statement | Hypotheses retained | Conclusion |
|---|---|---|
| `shortcut_translation` | Genuine additive `half`, multiplication by six onto, exact invariance under both branches | `f(x+w)=f(x)` |
| `continuous_shortcut_constant` | The previous hypotheses, dense nonnegative multiples of `w`, continuity into a Hausdorff space | `f` is constant |
| `finite_shortcut_harmonic_constant` | Finite cyclic group, genuine `half`, multiplication by six onto, the harmonic equation for the exact branches in (6) | Every real harmonic function is constant |

The last statement first uses the finite energy lemma for `F_0,F_1`,
then transfers their separate invariances to (1).

Here `half` is **not natural-number division**. The ordinary positive
integers do not form an additive group on which multiplication by six
is onto. Applying this theorem directly to an arbitrary ordinary label
would discard an essential hypothesis.

## 4. Relation to the literature-inspired argument

The [written bridge](LITERATURE_RIGIDITY_BRIDGE.md) uses compact additive
groups with dual `Z[1/6]`, together with finite residue factors. This
permits arbitrary real frequencies while making division by two and
three genuine automorphisms. The affine translation in (3) is the
reason invariant functions on the auxiliary group cannot retain a
nonconstant continuous factor when the specified translation is dense.

The measurable argument needs additional steps: strict convexity in
`L^2`, invariance under almost-everywhere composition, continuity of
translations on `L^2`, a Bernoulli conditional-expectation argument,
and removal of the contracting ternary coordinate. Those steps are
written and independently reviewed; the present module proves the
finite and continuous interfaces above. It does not claim that a
continuous theorem alone handles arbitrary measurable functions.

The initial source of this research direction is the
[PR186 rigidity task](https://github.com/GettysburgResearch/collatz/blob/1a57a3bf3c83ba2fa87d3b2216cfaff970f7a493/literature/deep-machinery-20261122/06_agent_tasks.md),
combined with the earlier
[periodic-label proof](PROFINITE_LABEL_RIGIDITY.md). The new written
argument does not import a higher-rank rigidity theorem: the two affine
branches do not commute, and its required ergodicity is proved directly.
Its primary-source references and analytic dependency boundaries are
recorded alongside the proof.

## 5. Remaining ordinary-source obligation

The checked calculation does not manufacture a continuous or measurable
extension of an arbitrary ordinary component label. The written argument
obtains dominated limits of finite-density empirical measures, and then a
uniform obstruction to approximation. Constructing the corresponding
approximations for the actual basin of one remains open.

All twelve public statements in this module are covered by the fresh
source-bound replay and axiom inventory in the
[literature-round report](../../reports/2026-11-21-dyadic-descent/literature/README.md).
Only that executed receipt certifies the final source bytes; the written
analytic result is outside the Lean statement count.
