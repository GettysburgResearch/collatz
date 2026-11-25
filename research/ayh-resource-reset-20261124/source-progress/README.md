# Ordinary source progress beyond the expanding prefix

**Collatz remains open.** This continuation proves new pointwise cases of the existing Lean proposal, including source-dependent exclusions in the residual rank-three Mersenne row. It also proves cofinal progressing families at unbounded exact upper ranks and transfers the selected many-clock graph problem to one common finite binary grid. The universal residual proposition remains an explicit, unproved argument.

Use the shortcut map $T(n)=n/2$ for even $n$ and $(3n+1)/2$ for odd $n$. Write $C(n)$ when its actual finite ordinary orbit reaches 1. A reverse defect is a positive $z\equiv17\pmod{48}$ with $C(3z)$ and not $C(z)$. The preceding [bounded return theorem](../closing-proposal/QuantitativeReturn.lean) proves that every positive nonbasin input $n$ gives a reverse defect at most $2^{40}n$. At a least reverse defect $z$, a same-component ordinary value $0<n<z/2^{40}$ is therefore impossible.

## 1. Two ordinary checkpoints and new proved exclusions

The preceding rank-three analysis isolates

$$j=97+162m,\qquad 81z+527=1024\,2^j,$$

with $M_j=2^j-1$ the first nonbasin Mersenne number if this $z$ is a least reverse defect. This uses the actual quantitative return and the earlier forty-offset certificate; it does not assume all smaller ordinary integers converge.

The new [two-checkpoint theorem](MersenneTwoCheckpoints.lean) follows two smaller directed queries through their full ordinary expanding runs. It forces both

$$3^q-5\quad\text{and}\quad 2^r3^s-17$$

outside the basin, where

$$q=67+108m,\quad k=\lfloor(j-1)/11\rfloor,\quad r=(j-1)\bmod11,\quad s=3+7k.$$

Both exponents $q,s$ are smaller than $j$. The clocks depend on the supplied source: the first checkpoint consumes $3(33+54m)$ steps from $12\,2^j-5$, and the second consumes $11k$ steps from $27\,2^{j-1}-17$. These are exact positive ordinary identities.

If **$m\equiv3\pmod{16}$**, then $3^q\equiv139\pmod{256}$. Eight further steps from $3^q-5$ and eight from $3^{q+2}-1$ meet. But $0<q+2<j$, and the latter input lies on the earlier $M_{q+2}$. This contradicts the least-defect configuration. [MersenneProgressCases.lean](MersenneProgressCases.lean) combines the new merger with the previous quantitative return and first-index theorem. There is no analytic or density premise in this kernel exclusion.

Since 16 is coprime to $3^{10}$, this removes one-sixteenth of **each** of the 58,049 classes outside the preceding ternary census. It is not a complete exclusion of the Mersenne row.

### Density-one exclusion with an inherited input

Compare $x_m=3^{67+108m}-5$ with $x_m+4=3^{67+108m}-1$. The second input lies on the earlier $M_q$. Under PR146's pinned symbolic fixed-gap estimate, all but

$$O\!\left(M/\sqrt{\log(2M)}\right)$$

parameters in any interval of $M$ parameters have an actual same-clock merger by $\lfloor\log_2M\rfloor$ additional steps. The same bound holds inside every fixed odd-stride progression, including every earlier ternary class. The order of $3^{108D}$ modulo $2^h$ is $2^{h-4}$ for odd $D$, so the transfer loses only a fixed factor from the full binary residue count.

This is a **source-qualified written consequence**, not a new Lean probability theorem. It provides finite certificates for a density-one set of parameters and leaves an exceptional prescribed parameter unresolved. [Proof and upstream source](TWO_CHECKPOINT_RESCUE.md#fixed-gap-four-removes-a-density-one-set-of-indices).

### The second checkpoint supplies a different mechanism

On the ordinary exponent cylinder $3^q\equiv-53\pmod{2^{288}}$, the second checkpoint meets an earlier Mersenne orbit within at most 285 additional steps. Higher-precision subsets of that cylinder can force the first checkpoint to miss **every** $3^a-1$, $a\ge1$, through any prescribed finite deadline. Both assertions concern the same supplied ordinary source, with sufficiently large parameter.

[MersenneRescueWords.lean](MersenneRescueWords.lean) checks all eleven literal merger rows. [MersenneRescueCylinder.lean](MersenneRescueCylinder.lean) proves the complete attachment and ordinary meeting for **every** $m=m_0+2^{284}t$, with the explicit $m_0$ in that file. Its finite modular-power evaluator is proved correct in Lean. The identification of this explicit progression with the displayed congruence and the arbitrary-deadline obstruction retain written proof scope. The progression intersects every earlier ternary class.

The exponents satisfy $22s+14r=21q+3$. Simultaneous 2-adic limiting coefficients on a fixed $r$ row therefore obey

$$3^{14r}y^{22}=27x^{21}.$$

If $x$ is a negative rational, $y$ cannot be rational, by the signs of the two rational sides. The exponent identity and rational sign assertion are kernel theorems; passage to a 2-adic limit is a written continuity argument. Irrational limiting configurations are not excluded. [Full checkpoint packet](TWO_CHECKPOINT_RESCUE.md).

## 2. Every finite lower word extends to genuine progress

Fix any $q\ge2$, any binary word $W$ of length $a$, any exact upper odd rank $R\ge q+44+2a$, and any source bound $L$. There are ordinary $z\ge L$ and odd $t>0$ such that

$$z\equiv17\pmod{48},\qquad81z+271=2^{q+7}t,$$

and the **first** hit of $3z$ uses exactly $R$ odd inputs. On the lower arm $T^7z=2^qt-1$, the next $q$ inputs are odd, one halving follows, and the next $a$ inputs have word $W$. The constructed continuation gives

$$n=T^{2q+48+2a}z>0,\qquad2^{40}n<z,\qquad C(n)\Longleftrightarrow C(z).$$

The entire existence statement, first-hit qualification, exact rank and contraction are proved in [PositiveWordDescent.lean](PositiveWordDescent.lean), `dense_progress`. It constructs a single positive ordinary source for each supplied tuple, without substituting a 2-adic completion.

The reusable pointwise theorem `delayed_tail_drop` needs no upper-hit assumption: any supplied source satisfying the affine equation, with any $a$ intervening steps and then $q+40+a$ even inputs, has the required contraction. [SourceProgressCases.lean](SourceProgressCases.lean) converts this into the existing `SourceProgress` and excludes it at a least reverse defect.

Every finite post-ascent word also occurs at every upper rank above its forced prefix count. Thus an adverse finite lower prefix is compatible with actual upper convergence. Progressing members in every finite cylinder do **not** imply progress at an arbitrary fixed member. The old $t=1$ rank-three family does not pass the immediate even-tail test. [Proof and exact quantifiers](WORD_REALIZATION.md).

## 3. One joint grid retains the original source population

At clock $h$, label a base site by $(T^h x,p_h(x))$, including its terminal value and odd count. Under a common lift,

$$T^i(2^hK+x)=2^{h-i}3^{p_i(x)}K+T^ix\qquad(0\le i\le h).$$

Equal labels give a physical meeting at $h$ on **every** lift. Away from at most $M^2(h+1)^2$ explicit exceptional lifts of $M$ sites, the finite graph components equal the label fibres. The inclusion, exception count and original-parent occupancy bound are kernel theorems in [LiftedLattice.lean](LiftedLattice.lean).

For the pinned PR197 coordinates, one event on $m\bmod2^D$ retains the same seed choice and all clocks in the slab. At $h=\lfloor d/3\rfloor$ the incomplete-period error is exponentially small. Under the preceding source-qualified inputs, a counterexample forces this joint grid event to have mass $\gg d^{-3}$ on infinitely many rows. The opposing $o(d^{-3})$ upper is open.

A single-clock estimate cannot supply it. For every odd stride and a window of $2^r$ sites, the complete-grid mean fractional deficiency is at least $c\sqrt{r/h}$. The prescribed-pair upper gives only $O((\log d/d)^{1/4})$ in the present stride range. Shared future bits prevent multiplying these marginal probabilities across clocks. [Source census, inequalities and boundaries](GRID_TRANSFER.md).

## 4. Exact boundary of the fixed-word search

The calibrated signed potential bounds every reflected path to 17, including arbitrarily many cycle turns. Together with ternary divisibility it makes the uniform affine query graph finite **without bounding word lengths**. On the residual exponent progression there are exactly two admissible query sources, and no further query from their successor states. On the other rank-three Mersenne progression there are none.

This classifies fixed finite words legal on every sufficiently large member of a whole progression. The new checkpoints use clocks that grow with the supplied exponent and lie beyond that restriction. [All-clock quotient](UNIFORM_MERSENNE_QUOTIENT.md); [kernel potential](SignedSeventeenPotential.lean).

## Final Lean proposal and evidence

[FinalProgressProposal.lean](FinalProgressProposal.lean) proves

```lean
collatz_from_residual (residual : ResidualExclusion) : UniversalConvergence
```

It chooses an actual least reverse defect and dispatches the established proved cases. `ResidualExclusion` must eliminate every remaining least defect with a genuine higher-rank upper hit. **That proposition is not proved.** The final equivalence records its exact strength; a passing conditional theorem is not a proof of Collatz.

The [execution report](../../../reports/ayh-resource-reset-20261124/source-progress/README.md) distinguishes the fresh full kernel build, explicit axiom audits, exact replays, independent reconstructions and source-qualified analytic statements. [Source ledger](SOURCES.json). Run [check_lean.sh](check_lean.sh) inside the pinned Lean 4.34.1 / Mathlib environment to rebuild all local dependencies and new modules.
