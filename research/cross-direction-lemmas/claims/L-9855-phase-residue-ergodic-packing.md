# L-9855 -- Phase-resolved residue packing over a uniquely ergodic base

Claim ID: `L-9855`  
Title: A finite residue decoder imposes one sharp packing inequality in every phase fiber  
Status: `PROPOSED`  
Authoring agent: `gpt56-synthesis-01`  
Reviewing agents: `gpt56-synthesis-01-h`  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: `L-9851`; `L-9845`, `L-9846`, and `L-9850` only for the raw-return comparison  
Scope: uniquely ergodic integer sequences equipped with a finite arithmetic residue decoder  
Related counterexample candidates: none

## Definitions

Use the setting of `L-9851`. Thus `X` is a compact metric space,
`P:X->X` is continuous and uniquely ergodic with invariant probability
measure `nu`,

\[
x_n=P^n(x_0),
\qquad
R:X\longrightarrow(0,\infty)
\tag{1}
\]

is continuous, and `(N_n)` is an integer sequence such that:

1. `N_n>0` for all sufficiently large `n`;
2. every positive integer occurs among the sufficiently late `N_n` at most
   `M` times; and
3. for some `m>0`,

   \[
   \frac{N_n}{nR(x_n)}\longrightarrow m.
   \tag{2}
   \]

Fix a modulus `q>=1`. Let

\[
\rho:X\longrightarrow\mathbb Z/q\mathbb Z
\tag{3}
\]

be a finite residue decoder. Write

\[
E_a=\rho^{-1}(a)
\qquad(a\in\mathbb Z/q\mathbb Z),
\tag{4}
\]

and assume each `E_a` is a Borel `nu`-continuity set:

\[
\nu(\partial E_a)=0.
\tag{5}
\]

The arithmetic decoding hypothesis is

\[
N_n\equiv\rho(x_n)\pmod q
\tag{6}
\]

for every sufficiently large `n`.

## Statement

### 1. Exact small-value density in each decoded residue

For `0<y<mR_min`, define

\[
A_{T,a}(y)
=\#\{1\le n\le T:x_n\in E_a,\ N_n\le yT\}.
\tag{7}
\]

Then

\[
\boxed{
\lim_{T\to\infty}\frac{A_{T,a}(y)}T
=\frac ym\int_{E_a}\frac1{R(x)}\,d\nu(x).
}
\tag{8}
\]

Thus the ordinary endpoint demand can be resolved not only by size but by the
exact residue class supplied by the phase decoder.

### 2. Fiberwise arithmetic packing inequalities

There are at most `yT/q+O(1)` positive integers at most `yT` in one residue
class modulo `q`. Hence

\[
\limsup_{T\to\infty}\frac{A_{T,a}(y)}T
\le\frac{My}{q}.
\tag{9}
\]

Comparison with (8) gives, for every residue `a`,

\[
\boxed{
\frac qm\int_{E_a}\frac1R\,d\nu\le M.
}
\tag{10}
\]

Equivalently, for every subset `B` of residues,

\[
\boxed{
\frac1m\int_{\rho^{-1}(B)}\frac1R\,d\nu
\le\frac{M|B|}{q}.
}
\tag{11}
\]

The inequalities are phase-resolved capacity constraints. A proposal fails
as soon as one collection of decoder fibers demands more small endpoints than
its corresponding arithmetic progressions contain, even if the unrestricted
total packing test passes.

### 3. Relation to unrestricted and coarse residue packing

Summing (10) over all `q` residues recovers exactly `L-9851/(8)`:

\[
\frac1m\int_X\frac1R\,d\nu\le M.
\tag{12}
\]

If the decoder is constant, say `rho(x)=a_0`, then (10) sharpens this by the
full modulus:

\[
\boxed{
\frac1m\int_X\frac1R\,d\nu\le\frac Mq.
}
\tag{13}
\]

In particular, if every endpoint has exact dyadic valuation `v`, use
`q=2^(v+1)` and the constant residue `2^v` to obtain

\[
\boxed{
\frac1m\int_X\frac1R\,d\nu\le\frac{M}{2^{v+1}}.
}
\tag{14}
\]

This is the ergodic, exact-density counterpart of the linear upper-slope
screen in `L-9854`. Neither theorem contains the other: the present result
uses a normalized-growth limit and can detect overcrowding in individual
phase fibers, whereas `L-9854` needs only a coarse linear upper bound.

### 4. Raw-return comparison

For the exact `{30,60,70}` raw H return, hypothetical ordinary endpoints have
exact valuation nine, the recursive decoder gives multiplicity `M=1`, and
`L-9850` computes

\[
\frac1{\overline\phi}\int_{\mathcal I}\frac1R\,d\nu
=\frac{16}{7(1+\mu_3^{-1})}>1.
\tag{15}
\]

The raw phase coordinate has one seam discontinuity on its compact circle, so
it is not literally covered by the continuous-`R` hypothesis above. However,
`L-9850` separately proves the required triangular threshold limit for every
raw phase by Weyl equidistribution. Applying the residue-capacity part of the
present proof to that already-audited limit, (14) requires the quantity in
(15) to be at most `2^(-10)`. This gives a residue-refined version of the
raw-return packing contradiction with a factor exceeding `1024`, rather than
the close unrestricted threshold in `L-9850`. The simpler slope argument of
`L-9854` avoids even the exact mean; the point here is the reusable
phase-resolved criterion.

## Proof

By `L-9851/(4)`, the pairs `(n/T,x_n)` have the triangular product
distribution `dt times dnu`. The indicator

\[
\mathbf1_{\{x\in E_a,\ mtR(x)\le y\}}
\tag{16}
\]

has product-null boundary: one part lies over `partial E_a`, which is
`nu`-null by (5), and the other lies on `mtR(x)=y`, whose time section has
Lebesgue measure zero for every `x`. The sandwich argument in
`L-9851/(10)--(12)` therefore applies with the additional factor
`1_(E_a)(x)`. Since `y<mR_min`, its inner time integral never saturates at
one, and

\[
\begin{aligned}
\lim_{T\to\infty}\frac{A_{T,a}(y)}T
&=\int_{E_a}\int_0^1
\mathbf1_{\{mtR(x)\le y\}}\,dt\,d\nu(x)\\
&=\frac ym\int_{E_a}\frac1{R(x)}\,d\nu(x).
\end{aligned}
\tag{17}
\]

This proves (8).

After deleting finitely many exceptional indices, (6) puts every term
counted by `A_(T,a)(y)` in the single ordinary progression `a modulo q`.
There are `yT/q+O(1)` positive members of that progression below `yT`, and
each is used at most `M` times. Thus

\[
A_{T,a}(y)\le\frac{MyT}{q}+O(1),
\tag{18}
\]

which proves (9). Comparing (8) and (9) and cancelling `y>0` proves (10).
Summing (10) over `a in B` proves (11); the fibers are disjoint and their
union is `rho^(-1)(B)`. Taking all residues proves (12), while a constant
decoder proves (13).

Finally, exact valuation `v` means

\[
N_n\equiv2^v\pmod {2^{v+1}},
\tag{19}
\]

so (14) is (13) at that modulus. Substitution of the exact raw-return data
from `L-9845`, `L-9846`, and `L-9850`, together with the separately proved
raw triangular limit just noted, proves (15) and its stated contradiction.
QED

## Motivation

`L-9851` compares the total forced density of small endpoints with the whole
positive integer lattice. A finite 2-adic decoder usually places different
phase regions into specific, much sparser arithmetic progressions. The
capacity comparison should therefore be performed in each decoded channel,
not only after forgetting the residues.

The theorem is a bridge between real ergodic drift and finite 2-adic state.
It turns any exact low-bit decoder into a quantitative obstruction that can be
tested before attempting an infinite carry construction.

## Dependency audit

- `L-9851` supplies triangular product equidistribution and the normalized-
  growth sandwich; the additional continuity-set indicator is checked here.
- The residue capacity estimate is elementary and includes the multiplicity
  factor explicitly.
- `L-9845` and `L-9846` supply valuation and decoder data only for the raw H
  comparison. `L-9850` supplies its already-audited exact integral and
  distinctness bound, as well as the Weyl argument needed at the phase seam;
  the abstract theorem does not depend on that claim.
- No independence between phase and residue is assumed: the decoder is an
  explicit function of phase.

## Gap audit

- The inequalities are necessary, not sufficient.
- A decoder with positive-measure boundary need not satisfy the triangular
  indicator limit under unique ergodicity without an additional hypothesis.
- The normalized-growth limit must hold along the full sequence; a limsup
  upper bound belongs instead to the coarser theorem `L-9854`.
- The multiplicity `M` must come from independent arithmetic structure.
- Passing every finite-modulus test does not construct an ordinary orbit or
  control intermediate H states.

## Adversarial tests

- The available capacity of one residue is `1/q` of the integer lattice, so
  the right side of (10) is `M`, while the equivalent integral bound has
  `M/q`; reversing this factor would weaken the theorem incorrectly.
- The event in (16) includes both the phase fiber and the moving size
  threshold. Phase frequencies alone do not prove (8).
- The cutoff `y<mR_min` is retained from `L-9851`; otherwise the time integral
  becomes `min(1,y/(mR(x)))`.
- Exact valuation `v` selects one class modulo `2^(v+1)`, not merely
  divisibility by `2^v`.
- The abstract theorem assumes continuous `R`; a null phase seam is not
  silently absorbed into that hypothesis. The half-open raw rotation is used
  only because `L-9850` independently proves its required threshold limit.

## Remaining uncertainty

For new return architectures, how large a modulus admits a stable decoder
whose fiber boundaries remain controlled, and what is the smallest true
endpoint multiplicity in each decoded channel? These arithmetic inputs may
be harder than the real drift calculation.

## Suggested next attack

Replace the deterministic decoder `rho(x)` by a finite set-valued decoder
`D(x)` when several residues remain possible. The correct necessary
conditions should be Hall-type inequalities comparing every collection of
phase states with the union of their allowed residue classes. Such a theorem
would quantify partial decoders before full branch separation is available.
