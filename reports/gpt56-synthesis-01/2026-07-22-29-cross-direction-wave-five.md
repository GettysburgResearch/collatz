# Cross-direction lemma forge: wave five

Date: 2026-07-22  
Authoring lane: `gpt56-synthesis-01`  
Status: theorem-level claims remain `PROPOSED` pending external repository review

## Scope

Wave five followed the exact frontiers left by wave four rather than opening
new completion-only constructions. It produced nine claims, `L-9853` through
`L-9861`, in four connected themes:

1. a rigorous obstruction to naive survivor-gap averaging;
2. arithmetic refinements of integer packing, from fixed residues to partial
   set-valued decoders;
3. a finite ordinary separator for automatic horizontal-root absorption; and
4. a characteristic-two Padé state theory that settles actual dyadic
   remainders through `s=28` while proving exactly why small channel summaries
   do not close.

The collision/padding lane also advances from one residual XOR bit to an exact
finite correction isometry at every precision.

## Executive summary

- `L-9853` refutes the hoped-for uniform maximum-gap contraction for a long
  zero run. The legal powers-of-`81` twist group contains examples whose
  normalized maximum gap approaches one and whose pointed isolation radius is
  exponentially larger than the average gap.
- `L-9854` proves the elementary but strong sparse-residue slope bound
  `MrC>=q`. Applied to the raw H graph, exact valuation nine and decoder
  distinctness contradict its slope with a margin `1024` versus less than
  `189/128`.
- `L-9855` resolves the unique-ergodic packing theorem by decoded residue
  phase: each arithmetic progression receives its own sharp capacity bound.
- `L-9860` extends this to partial set-valued decoders. Every residue cut `B`
  must absorb all phase demand whose entire allowed set lies inside `B`,
  yielding the exact Hall-type no-outlet inequalities.
- `L-9857` gives every fixed-width automatic horizontal root a finite Moore
  presentation and an explicit ordinary-input separator from the finite core.
  Fixed-width absorption is decidable, but the separator horizon grows as
  `2^(Theta(3^k))`.
- `L-9858` proves that residual quotients and physical address corrections are
  related by a pointed bijective 2-adic isometry. At precision `Q`, the map is
  a permutation of all `Q`-bit words and requires exactly `Q` bits of
  residual-dependent information on a full odd-affine zipper cylinder.
- `L-9856`, `L-9859`, and `L-9861` prove exact Padé augmentation orders at
  `s=12,16,20,24,28`, extending `L-9848`'s `s=4,8` result. Every dyadic target
  is therefore nonexceptional in the first seven nonzero actual remainder
  layers.
- `L-9859` also proves the exact residue-channel closure criterion
  `4*2^(nu_2(M))>H`. At height `38`, sixteen residue sums are minimal among
  residue-sum quotient states. `L-9861` gives an equivalent eight-pair twisted
  realization below height `64`, while proving that the untwisted even/odd
  readout itself is not closed.

## Survivor geometry: multiplicity does not regularize order

`L-9847` made a long common zero run look promising: `r` zero coordinates
produce `2^r` exact common translations. A natural next conjecture was that
their pointed gaps should be at most a constant multiple of the average
`64^N/2^r`.

`L-9853` derives both exact lifts of that translation set. Adding a zero-run
coordinate gives a disjoint binary set lift, while increasing the ambient
width gives a 64-bucket order recurrence whose bucket digit includes both an
inverse-unit digit and a subset-sum carry.

The twist group is exact:

\[
\langle81\rangle
=\{a\bmod64^N:a\equiv1\pmod {16}\},
\qquad
\operatorname{ord}_{64^N}(81)=2^{6N-4}.
\]

This permits a starting depth for which the run weights become the ordinary
positive sequence

\[
64^k81^{r-k-1},
\qquad 0\le k<r.
\]

With no wrap, every subset sum lies in the interval

\[
0\le x\le D_r=\frac{81^r-64^r}{17},
\]

so the wrap gap has length at least `64^N-D_r`. Its normalized supremum over
ambient widths is one. At the least width where the wrap gap exceeds the
smallest weight, zero has pointed radius `64^(r-1)` and

\[
\frac{\operatorname{rad}(0)}{64^N/2^r}
>
\frac{17}{4096}\left(\frac{128}{81}\right)^r.
\]

Thus no uniform average-scale pointed-gap estimate can depend only on run
length and multiplicity. The construction does not show that zero is selected
by the actual minimum/successor pair, and extra zero coordinates may fill the
gap. The live theorem must couple the full signed difference to the actual
ordinary-order selector.

## Three levels of arithmetic packing

### Coarse sparse support

`L-9854` begins with no ergodic hypothesis. If an eventually positive integer
sequence has multiplicity at most `M`, satisfies `N_n<=Cn+O(1)`, and occupies
only `r` classes modulo `q`, counting available integers gives

\[
C\ge\frac{q}{Mr}.
\]

Exact valuation `v` is the single class `2^v modulo 2^(v+1)`, so the required
slope is at least `2^(v+1)/M`. A hypothetical ordinary point on the raw H
graph would give pairwise distinct endpoints of exact valuation nine and
upper slope below `189/128`; the required slope is `1024`. This independently
excludes every signed ordinary point without the close drift-integral
comparison used in `L-9850`.

### Deterministic phase residues

`L-9855` retains the normalized-growth and unique-ergodic setting of `L-9851`
and assumes a finite residue decoder `rho(x) modulo q`. If `E_a` is the phase
fiber decoded to `a`, then the exact small-value demand in that fiber is

\[
\frac ym\int_{E_a}R^{-1}\,d\nu,
\]

while its arithmetic progression has capacity `My/q`. Therefore

\[
\frac qm\int_{E_a}R^{-1}\,d\nu\le M
\]

for every residue separately, and the corresponding inequality holds for
every union of decoder fibers. Summing all residues recovers `L-9851`; a
constant decoder strengthens it by the full factor `q`.

### Partial, set-valued decoders

`L-9860` handles the common situation where a finite carry analysis leaves a
nonempty allowed set `D(x)` rather than one residue. For each cut `B`, only
the no-outlet phase region

\[
H_B=\{x:D(x)\subseteq B\}
\]

is forced to consume capacity inside `B`. With residue-dependent endpoint
multiplicities `M_a`, the sharp necessary cut is

\[
\frac1m\int_{H_B}R^{-1}\,d\nu
\le
\frac1q\sum_{a\in B}M_a.
\]

These are exactly the saturated finite Hall-family cuts. Singleton allowed
sets recover `L-9855`. Replacing `D(x) subseteq B` by the tempting event
`D(x) intersects B` is false even for a one-point system with modulus two.
A multiplicity-weighted residue multiset attains equality, proving the
coefficient sharp. The cuts remain necessary, not sufficient matching or
orbit-construction conditions.

## Automatic components: finite fixed-width absorption testing

`L-9857` uses the horizontal staying/escape graph of `L-9849`. A formal copy
of the `L_k=2*3^(k-1)` horizontal phases, disjointly adjoined to the fixed
section-closed core `F`, is a Moore presentation of every width-`k` root. Its
state count is at most `|F|+L_k`; absorbed aliases only reduce the actual
kernel.

Comparing this presentation with the core automaton gives a product with

\[
D_k=|\mathcal F|\bigl(|\mathcal F|+L_k\bigr)
\]

pairs. If a root differs from a core state, a shortest least-significant-first
distinguishing word has length at most `D_k-1`. It cannot end in zero because
`E_0q(0)=q(0)`, so it is the canonical binary expansion of an ordinary
integer. Consequently

\[
x_{h,k,j}\in\mathcal F
\iff
\exists f\in\mathcal F\ 
x_{h,k,j}(n)=f(n)
\quad(0\le n<2^{D_k}).
\]

An unabsorbed root needs at most `|F|` witness inputs, one per core state.
Evaluation of each witness is exact: follow staying bits until the first
padded-digit mismatch, then evaluate the corresponding escape decoration on
the unread high quotient.

This closes equality at every supplied width. It gives no width-independent
separator and no termination certificate for the eventual-absorption
quantifier.

## Collision/padding: the full finite correction isometry

Let `Omega` be the connector isometry and

\[
\mathcal A(w)=\Omega^{-1}(-w).
\]

`L-9858` first proves the exact distance identity

\[
\nu_2(\mathcal A(h)-\mathcal A(V))=\nu_2(h-V).
\]

If `h=V+2^H d`, normalize the address displacement by

\[
\Psi_{H,V}(d)
=\frac{\mathcal A(V+2^Hd)-\mathcal A(V)}{2^H}.
\]

The restriction of a bijective isometry to a dyadic ball is onto the
corresponding address ball, so `Psi_(H,V)` is itself a pointed bijective
isometry of `Z_2`. Its first bit is `d mod2`, recovering the XOR law of
`L-9852`; at every precision `Q`, its reduction is a permutation of
`Z/2^Q Z`.

On a compatible odd-affine zipper cylinder, the quotient parameter `t` is
conjugated through another bijective isometry. Every `Q`-bit correction word
therefore occurs exactly once modulo `2^Q`. Any deterministic rule whose only
residual-dependent channel factors through a finite state must have at least
`2^Q` states to output all corrections, and the raw `Q` quotient bits suffice
via the finite permutation.

This is an exact information theorem, not a bounded streaming rewrite. The
finite permutation may change with chart and scale, and compatibility,
stage caps, intermediate physical crossings, and ordinary realization remain
open.

## Padé: exact layers and the first state-minimality theorem

### Remainders twelve and sixteen

`L-9856` places the universal 2-adic phase bits in a finite Boolean ring and
propagates the q-Pascal coefficient state. Grouping by subset size modulo four
gives complete Hasse tables. After the forced baselines, their columnwise XOR
has first units

\[
\lambda_{12}=20,
\qquad
\lambda_{16}=32,
\]

with slacks `3` and `4`. Both are below every eligible dyadic target cost.

### Exact residue-state closure and remainder twenty

`L-9859` studies the q-Pascal transition on arbitrary finitely supported size
states. Projection to sums by `v modulo M` induces a closed transition through
height `H` exactly when

\[
Q^{-4M}=1\pmod {X^{H+1}}
\iff
4\,2^{\nu_2(M)}>H.
\]

The necessity witness is the kernel state `e_0+e_M`; its next projection
contains the nonzero defect `1+Q^(-4M)`. Thus, at height `38`, sixteen channels
are minimal among residue-sum quotient states. The exact sixteen-channel
transition gives

\[
\lambda_{20}=38,
\qquad
\delta_{20}=5.
\]

Minimality is deliberately restricted to residue-sum projections; a
different richer compression is not excluded.

### Remainders twenty-four and twenty-eight

Below height `64`, the same sixteen-channel state remains exact. `L-9861`
rewrites it as eight twisted even/odd pairs and derives their closed
cross-recurrence. Compact paired certificates give

\[
\lambda_{24}=46,
\qquad
\lambda_{28}=52,
\]

with slacks `6` and `7`. The raw untwisted even/odd pair is not itself closed:
the quotient criterion detects its defect already at augmentation order
eight. The pairing explains the finite tables without claiming an induction.

Combining `L-9848`, `L-9856`, `L-9859`, and `L-9861`, every target residual is
nonzero for

\[
s=4,8,12,16,20,24,28.
\]

The uniform order formula remains conjectural, as do all later layers and the
separate residual-to-specialization-gcd transfer.

## Explicit non-results

- No nontrivial ordinary Collatz orbit, divergent seed, cycle, sanctuary, or
  `K-####` candidate is claimed.
- The exceptional survivor gaps do not identify an actual successor edge.
- Sparse, deterministic, and Hall packing inequalities are necessary screens;
  passing them does not select compatible residues or construct endpoints.
- Fixed-width automatic absorption is finite, but eventual absorption over all
  widths remains undecided.
- The correction isometry supplies finite lookup sufficiency, not a bounded
  local scale-to-scale residual grammar.
- Padé nonvanishing is proved only through `s=28`; the all-layer augmentation
  order and noncyclotomic/specialization gcd sectors remain open.
- Sixteen-channel minimality is only among residue-sum quotient states, and
  the paired finite certificates are not a two-channel induction.

## Internal audit record

- The `81` twist subgroup, discrete-log solvability, no-wrap subset sums,
  adjacent pointed gaps, and exponential ratio in `L-9853` were independently
  reconstructed.
- The sparse-residue counting inequality was checked with signed initial H
  endpoints and eventual positivity. The phase-residue and Hall indicators
  were checked for null boundaries and every factor of `q` and `M`.
- The formal automatic Moore presentation, LSF word composition, shortest
  product path, canonical last bit, decoration evaluation, and absorbed-state
  aliasing were independently audited.
- The connector ball-surjectivity argument, correction sign, canonical wrap,
  finite permutation, odd-affine conjugacy, and exact information-channel
  hypothesis were independently audited.
- Every Padé q-Pascal exponent and forced baseline was re-derived. Independent
  Boolean-ring propagation reproduced the universal tables for `s=12,16,20,
  24,28`; kernel witnesses separately checked each claimed nonclosure.
- All claim files were checked for required audit sections, sequential unique
  equation tags, exact display pairing, local link targets, and embedded
  control characters.

## Highest-leverage next actions

1. Couple the survivor translation fiber to the actual minimum/successor
   selector; `L-9853` shows that multiplicity-only gap estimates cannot work.
2. Apply the Hall cuts of `L-9860` to the first H return with a genuinely
   partial low-residue decoder, before spending effort on a full selector.
3. Symbolically refine the automatic root/core product relation through the
   width lift, seeking a width-independent quotient or an explicit invariant
   that prevents one.
4. Conjugate consecutive collision-chart correction permutations and test
   whether their least-significant-bit update is triangular.
5. At Padé layer `s=32`, account for the first augmentation-height boundary
   that forces a thirty-two-channel residue state; seek a normalized channel
   invariant rather than only another finite table.

## Files added in wave five

- `research/cross-direction-lemmas/claims/L-9853-zero-run-translation-gap-obstruction.md`
- `research/cross-direction-lemmas/claims/L-9854-sparse-residue-linear-packing.md`
- `research/cross-direction-lemmas/claims/L-9855-phase-residue-ergodic-packing.md`
- `research/cross-direction-lemmas/claims/L-9856-pade-dyadic-four-residue-transition.md`
- `research/cross-direction-lemmas/claims/L-9857-finite-ordinary-absorption-separator.md`
- `research/cross-direction-lemmas/claims/L-9858-residual-address-correction-isometry.md`
- `research/cross-direction-lemmas/claims/L-9859-pade-dyadic-minimal-residue-state.md`
- `research/cross-direction-lemmas/claims/L-9860-hall-set-valued-residue-packing.md`
- `research/cross-direction-lemmas/claims/L-9861-pade-dyadic-paired-channel-layers.md`
- this report

The packet `research/cross-direction-lemmas/README.md`, `CLAIMS.md`, and
`VERIFICATION.md` index the theorem statements and preserve all dependency and
counterexample boundaries.
