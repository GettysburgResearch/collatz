# Cross-direction lemma forge: wave six

Date: 2026-07-22  
Authoring lane: `gpt56-synthesis-01`  
Status: theorem-level claims remain `PROPOSED` pending external repository review

## Scope

Wave six closes the overnight lemma forge with six claims, `L-9862` through
`L-9867`.  It advances four live boundaries rather than opening a new
counterexample construction:

1. the first Padé residue-state refinement and the exact four-step block
   operator behind a possible induction;
2. a live order-statistic recursion for the actual survivor minimum and
   successor;
3. an exact fractional converse to the set-valued Hall packing cuts; and
4. the precise distinction between triangular 2-adic correction maps and
   bounded-state correction grammars.

No claim in this wave constructs an ordinary Collatz counterexample or
promotes any branch theorem.

## Executive summary

- `L-9862` crosses the first Padé state boundary.  Height `72` forces the
  residue modulus from sixteen to thirty-two channels; the old quotient has
  a defect of exact order `64`.  A universal thirty-two-channel certificate
  gives `lambda_32=72`, slack eight, and excludes every dyadic target at
  actual remainder `s=32`.
- `L-9864` groups four q-Pascal steps into one exact five-branch operator.
  Its Boolean branch gains are `(0,3,2,3,0)`, its parity swaps are explicit,
  and its scalar residual obeys an order-eight product congruence which is
  sharp already at `n=1`.  The missing all-layer input is now one endpoint
  relation, not an unspecified finite table.
- `L-9865` turns the survivor width lift into an exact 64-bucket stable merge.
  Each output bucket has exactly two source lists, and its first two entries
  come from at most four old labeled candidates.  This selects the actual
  nontrivial minimum/successor pair before applying signed-fiber isolation.
- `L-9866` proves that all set-valued Hall no-outlet cuts are sufficient for
  the corresponding finite fractional transportation problem.  The largest
  cut overload is exactly the unroutable mass; tight cuts form a lattice and
  are impermeable.  The ergodic corollary is only a stochastic kernel, not a
  deterministic residue or integer selector.
- `L-9863` proves that every 2-adic isometry has a unique LSF-triangular
  Boolean normal form, closed under composition and inverse.  Its finite
  reductions are rooted-binary-tree automorphisms of order
  `2^(2^Q-1)`.
- `L-9867` proves the exact bounded-memory criterion: an isometry has a finite
  synchronous LSF Mealy realization if and only if it has finitely many
  rooted-tree sections, and the minimal state count equals the number of
  sections.  A square-mask XOR isometry is triangular but has unboundedly many
  sections, so causality alone is strictly weaker than finite state.

## Padé: the first refinement boundary

The residue-sum closure theorem `L-9859` says that a modulus `M` closes
through height `H` exactly when

\[
4\,2^{\nu_2(M)}>H.
\]

At the decisive height `H=72`, this forces `M=32`.  The old `M=16` quotient
fails at exact order `64`:

\[
\operatorname{ord}_X(1+Q^{-64})=64,
\qquad
Q^{-128}=1\pmod {X^{73}}.
\]

`L-9862` also generalizes the twisted-pair realization.  Whenever the
`M`-channel state closes, `M/2` parity pairs close under

\[
\begin{aligned}
\mathbf E_{n+1,j}
&=\mathbf E_{n,j}+C_HQ^{n-4j}\mathbf O_{n,j+1},\\
\mathbf O_{n+1,j}
&=\mathbf O_{n,j}+C_HQ^{n-4j}\mathbf E_{n,j+1}.
\end{aligned}
\]

The complete universal phase calculation at `s=32` leaves the coefficient
window

\[
([X^{64}]F_{32,c},\ldots,[X^{72}]F_{32,c})
=(0,0,0,0,0,0,0,0,1)
\]

for every `c in Z_2`.  Hence

\[
\lambda_{32}=72,
\qquad
B_{32}=64,
\qquad
\delta_{32}=8.
\]

Together with the preceding finite certificates, all dyadic targets are
nonexceptional for

\[
s=4,8,12,16,20,24,28,32.
\]

This remains a finite-layer theorem.  Thirty-two-channel minimality is among
residue-sum quotient states, and no all-layer order formula follows.

## Padé: an exact four-step operator

`L-9864` packages the normalized size summands in

\[
P_n(Y)=\sum_v\mathscr S_{n,v}Y^v.
\]

Four q-Pascal steps give the exact identity

\[
P_{n+4}(Y)
=\sum_{k=0}^{4}
C^kQ^{nk-3\binom k2}{4\brack k}_Q
Y^kP_n(Q^{-4k}Y).
\]

In characteristic two,

\[
{4\brack1}_Q={4\brack3}_Q=X^3,
\qquad
{4\brack2}_Q=X^2(1+X+X^2),
\]

so the five branch gains are exactly `(0,3,2,3,0)`.  Even branches preserve
the parity pair and odd branches swap it.  The last endpoint coefficient
differs from one at exact order two, making the unresolved endpoint
cancellation visible.

At the scalar readout, the two possible degree-seven errors cancel in
characteristic two:

\[
F_{n+4,c}-F_{4,c+n}F_{n,c}\in X^8\mathbf F_2[[X]].
\]

The bound is sharp uniformly in `c` at `n=1`, where the difference is
`X^8 modulo X^9`.  For `n>=1`,

\[
F_{n+4,c}\equiv X^6F_{n,c}\pmod {X^8}.
\]

This congruence is absolute rather than relative to the already large order
of `F_n`; it does not propagate the known augmentation orders.  A normalized
relation between the endpoint twists `j` and `j+4` is still required.

## Survivor geometry: selecting the live pair

`L-9865` writes every depth-`n` survivor representative as an old lower
coordinate plus one new base-64 bucket.  For an old word `epsilon` and new
bit `b`,

\[
\alpha_{n+1}(\varepsilon,b)
=\alpha_n(\varepsilon)
+64^n[D_n(\varepsilon)+be_n]_{64},
\]

where

\[
e_n=[17^{-n}]_{64}\in\{1,49,33,17\}
\]

is four-periodic.  The reduction brackets retain the genuine new-bit wrap.
The two excluded constant extensions both land in bucket zero, but their
two siblings remain live candidates.

For every output bucket `t`, the bit-zero source has `D_n=t` and the bit-one
source has `D_n=t-e_n`.  The complete bucket is their stable merge in old
ordinary order.  Therefore its first two entries lie among the first two of
each source—at most four labeled candidates.  The global minimum lies in the
least occupied bucket; its successor is either the second element of that
bucket or the first element of the next occupied bucket.

The theorem also keeps the two wraps needed by the signed-fiber lane.  A
translated point acquires the bucket digit

\[
B_N^a(c)
=[A_N+D_N(c)+\chi_N^a(c)]_{64},
\]

where `chi` is the lower-width ordinary carry, and the oriented gap contains
the old endpoint wrap as

\[
g_{N+1}
=g_N+64^N[B_N^b-B_N^a-w_N]_{64}.
\]

Once the selected labels are known, they are consecutive after removing
`0,1`, so the isolation inequalities of `L-9847` apply to the actual pair.
The remaining problem is to propagate all 64 pairs of source heads without
re-enumerating exponentially many old words.

## Packing: Hall cuts are exactly fractionally sufficient

Let each allowed residue pattern `S` have demand `mu_S` and each residue `a`
have capacity `c_a`.  `L-9866` proves that nonnegative allocations supported
on `a in S`, with every row demand met and every column capacity respected,
exist exactly when

\[
\sum_{S\subseteq B}\mu_S
\le
\sum_{a\in B}c_a
\qquad(B\subseteq Q).
\]

The explicit pattern-to-residue flow network gives the deficiency formula

\[
v_{\max}
=d-\max_{B\subseteq Q}\bigl(\mu(B)-c(B)\bigr).
\]

Thus the largest Hall overload is exactly the unroutable fractional mass.
Every tight cut is saturated solely by patterns contained in it; crossing
patterns send no mass into it.  Tight cuts are closed under union and
intersection because the Hall slack is a nonnegative submodular function.

For the ergodic decoder of `L-9860`, the theorem produces a measurable
patternwise probability kernel whose weighted aggregate load in residue `a`
is at most `M_a/q`.  It does not purify that kernel, select residues along one
orbit, match times to integers, respect moving thresholds, or couple
different moduli.

## Collision charts: triangularity versus finite state

`L-9863` proves that an isometry `f:Z_2 -> Z_2` is equivalent to a unique
triangular digit system

\[
y_i=x_i+\phi_i(x_0,\ldots,x_{i-1}).
\]

Composition and inverse remain triangular.  At precision `Q`, these maps are
exactly the automorphisms of the depth-`Q` rooted binary tree, with

\[
|G_Q|=2^{2^Q-1},
\qquad
|\ker(G_{Q+1}\to G_Q)|=2^{2^Q}.
\]

Consequently, any genuinely isometric conjugated zipper update emits one
output bit after the corresponding input prefix is known.  The extension
count proves that this causal form alone places no uniform restriction on
future truth tables.

`L-9867` isolates the exact missing condition.  If `f|_p` denotes the
normalized tail map after prefix `p`, then

\[
f\text{ has a finite synchronous LSF Mealy realization}
\quad\Longleftrightarrow\quad
\{f|_p:p\text{ finite}\}\text{ is finite}.
\]

The minimal number of states is exactly the number of distinct sections.
Sections obey

\[
(g\circ f)|_p=(g|_{F(p)})\circ(f|_p),
\qquad
(f^{-1})|_{F(p)}=(f|_p)^{-1},
\]

so finite-section isometries form a group and chart-conjugacy state bounds
factor into their components.

The separation is strict.  Digitwise XOR by a binary mask `a` has section
set equal to the shift orbit of `a`.  Taking `a_i=1` exactly at square
indices gives a perfectly triangular isometry with a new section at every
depth.  The collision frontier is therefore finite-section closure of the
physical chart maps, not triangularity itself.

## Explicit non-results

- No nontrivial ordinary orbit, cycle, divergent seed, sanctuary, or
  `K-####` counterexample candidate is claimed.
- Padé target nonvanishing is finite through `s=32`; neither `L-9862` nor the
  four-step operator proves an all-layer order formula or the transverse
  residual-to-specialization-gcd transfer.
- The survivor selector is exact for one width lift but does not give a
  bounded-state recursion for all bucket heads, a positive gap bound, or
  infinitely many renewals.
- Fractional Hall feasibility is not deterministic phase selection, integer
  matching, temporal compatibility, or cross-modulus coherence.
- Triangularity is causal, not finite-state.  The collision charts still need
  a proof that the actual scale transition is isometric on its stated domain
  and that its full section family is uniformly finite.
- Every claim remains `PROPOSED`; same-session adversarial reconstruction is
  not external repository review.

## Internal audit record

- `L-9862`: the thirty-two-channel transition was independently reproduced
  across all 128 phase residues.  Both the Boolean state and a separate
  `q^128` group-ring calculation returned masks `0x100/0x000`; the closure
  boundary, order, slack, and target comparison were rederived.
- `L-9863`: both directions of the triangular theorem, inverse/composition
  laws, wreath convention, group counts, restriction fibers, and zero-leaf
  stabilizer were independently reconstructed; all depth-three maps were
  exhaustively checked.
- `L-9864`: the five-branch block, Gaussian factors, parity action, endpoint
  filtration, and order-eight cancellation were independently derived.  A
  separate bit-packed test covered multiple heights and phases; the root
  audit proved the uniform `n=1` sharpness formula symbolically.
- `L-9865`: inverse-unit lifts, periodic new digit, trivial exclusions,
  stable merges, translated carries, and both wraps were independently
  derived.  Exact enumerations through depth seven and 50,000 randomized
  translated-gap cases passed.
- `L-9866`: the min-cut sign, canonical cut reduction, family-cut converse,
  tight-cut impermeability/lattice, and stochastic-kernel scope were checked
  independently.  One implicit neighborhood inclusion was made explicit.
- `L-9867`: section surjectivity, prefix normalization, Mealy minimality,
  group laws, and the XOR counterexample were independently audited.  The
  surjectivity proof and canonical one-bit prefix identity were made explicit.
- All six claim files were checked for required proof/audit sections, exact
  display pairing, unique equation tags, local references, and embedded
  controls.

## Highest-leverage next actions

1. Normalize the Padé twisted-pair state by the forced baseline and identify
   an invariant relating the two endpoint twists `j` and `j+4` in `L-9864`.
2. Propagate the two source heads per survivor bucket under a second width
   lift; either close a finite selector state or construct a survivor-specific
   family forcing unbounded head depth.
3. Compute symbolic rooted-tree sections of the actual residual-address
   connector maps and close them under the composition rules of `L-9867`.
4. Apply the tight-cut lattice of `L-9866` to a concrete new H return, then
   locate the first obstruction that is genuinely deterministic or dynamic
   rather than fractional.
5. Preserve the independent automatic-width frontier: fixed-width absorption
   is decidable, but no theorem yet bounds the last unabsorbed width.

## Files added in wave six

- `research/cross-direction-lemmas/claims/L-9862-pade-dyadic-first-state-refinement.md`
- `research/cross-direction-lemmas/claims/L-9863-triangular-normal-form-2adic-isometries.md`
- `research/cross-direction-lemmas/claims/L-9864-pade-dyadic-four-step-block.md`
- `research/cross-direction-lemmas/claims/L-9865-survivor-bucket-order-statistics.md`
- `research/cross-direction-lemmas/claims/L-9866-fractional-hall-residue-allocation.md`
- `research/cross-direction-lemmas/claims/L-9867-finite-section-isometry-transducers.md`
- this report

The packet `research/cross-direction-lemmas/README.md`, `CLAIMS.md`, and
`VERIFICATION.md` index the audited proposed statements and preserve every
remaining ordinary-section, bounded-memory, and global-induction boundary.
