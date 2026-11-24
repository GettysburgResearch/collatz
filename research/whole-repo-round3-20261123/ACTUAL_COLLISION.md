# Exact source boxes for actual ternary collisions

Date: 2026-11-23. Baseline: `b78819e95ee7d39f02022de991b42217821e7590`.

**Status: PROPOSED finite arithmetic theorems, with a Lean finite core;
the global critical collision upper bound remains OPEN.** At fixed odd
length, the total binary clock, the integer quotient of the complete
carry, and the original source quotient determine a box in which the
ternary endpoint residue is injective. This controls actual occurrences,
including repeated words, at arbitrarily large translated heights.

The weighted consumer keeps the original orbit, the individual source
weights, the ordinary collision diagonal, and every omitted inverse
branch. It does not prove control of collisions between different boxes.
No rotation of an actual word or replacement by a fresh source law is
used in that consumer.

## 1. Source reassessment and the exact law

The older resident mass and renewal interfaces were read at the baseline
above, including the scoped errata:

| Source | Usable interface and retained boundary |
|---|---|
| `research/astra-critical-mass/PROOF.md`, Sections 1--2 | Original positive-source mass and killed-transfer identities; its global positive supersolution remains unproved. |
| `research/astra-critical-mass/RUN_RENEWAL.md`, Sections 1--3 | Exact complete odd/even runs and fresh-shell averaged drift; transport does not preserve a fresh-shell input. |
| `research/astra-three-routes/ROUTE_1_TRANSFER.md`, Sections 1--3 | Complete ordinary section inverse fan and charged contraction into resonance or one. The resonance-return charge is retained. |
| `research/astra-three-routes/pass4/RENEWAL_MASS.md` | All-residence estimates for specified corridors and safe-entry envelopes. |
| `research/astra-three-routes/pass5-spectrum-switch/INDUCED_MASS.md` | The actual enlarged-safe resolvent and the demonstrated failure of reciprocal-rank weights after unsafe return. |
| `research/integrated/renewal-transport/README.md` and `ERRATA.md` | The distinct safe regions, clocks, and source-envelope requirements; no common invariant transport domain is supplied. |

The new pressure and boundary sources were read at these exact heads:

| Frozen source | Exact role |
|---|---|
| PR185, `2ac1f63b5f8d51ab4b472307b52cc89c9ef6df9d`, `research/rigidity-closing-20261122/SAME_SOURCE_INVERSE_ENTROPY.md`, Sections 1--2; blob `c430b45adf356b11bd5d4f7aeb7026212ecf4183` | Original ordinary kernel, exact retained atoms, and all-depth capacity error. |
| PR185, same head, `research/central-closure-20261123/COLLISION_LOGARITHMIC_GAIN.md`, Theorem 3; blob `803d6ba2a3827c6ef94cb31fb838e3d416b92090` | Critical lower bound with its square-root gain. |
| PR185, same head, `research/whole-repo-closure-20261122/ORDINARY_HARMONIC_FLOW_AND_COLLISIONS.md`; blob `9b8ed17476a6c133f3bb3710c4fe1d5de8d5a1f1` | The source-qualified ordinary harmonic flow and its weighted moments; its total mass is infinite. |
| PR178, `4e204f54136c79cf8c9393b34e3330594f99ae0a`, `research/global-closure-20261123/escape/PRESSURE_COLLISION_ATTACK.md`; blob `019aa6a468c40e76720fa786939b076ab2e6ab61` | Pressure off-diagonal estimate and the divergent cost of a global density comparison, even with a varying pressure exponent. |
| PR180, `fcdcdbadc6172e414f7282442a8a6b85587d7e70`, `research/source-clock-20261123/BOUNDARY_OVERLAP.md`, `EXTENSIONS.md`, `COLLISION_TRANSFER.md`, `EARLY_TRACE.md` | Actual real-law upper local dimension, positive lower information dimension, retained high-profile mass, and the original-source cost of adaptive inverse stopping. None is an actual ternary collision upper bound. |

Write

\[
U(n)=\frac{3n+1}{2^{v_2(3n+1)}},\qquad q_j=U^j(q_0).
\]

For the infinite application assume this is one fixed injective positive
odd unit orbit. Retain the source-qualified ordinary harmonic flow
`nu(q)=sum_(Ux=q) nu(x)`, with `v_j=nu(q_j)` increasing to
`C>0`. The target is precisely

\[
N=M+1,\qquad
\zeta_{M,r}=\frac1N\sum_{j=0}^{M}K_\nu^r(q_{r+j},\cdot),
\quad K_\nu(q,n)=\mathbf1_{Un=q}\frac{\nu(n)}{\nu(q)}.
\tag{1}
\]

Every finite `r` retains the exact ordinary atom

\[
t_j:=\zeta_{M,r}(\{q_j\})=\frac{v_j}{N v_{r+j}},
\qquad \frac{c_0}{N}\le t_j\le\frac1N,
\quad c_0=v_0/C>0.
\tag{2}
\]

The remaining mass is the exact inverse-retracing failure

\[
\varepsilon_{M,r}=1-\sum_{j=0}^{M}t_j
\le\eta_M:=1-\frac1{CN}\sum_{j=0}^{M}v_j\longrightarrow0,
\tag{3}
\]

uniformly in `r`. These identities are reused, not claimed as new here.
The finite arithmetic below does not require the existence of this flow.

The pinned critical lower bound uses

\[
\theta=\frac{\Phi(\log_2 3)}{\log3}
=0.949955527188\ldots,\qquad
\Phi(a)=a\log a-(a-1)\log(a-1).
\]

For each fixed `T>0`, it gives `Col_(3^m)(zeta_(M,r)) >=
c*sqrt(m)*3^(-theta*m)` at all finite inverse clocks when `M` is
sufficiently large and `m^2<=T*M`. The collision and ordinary diagonal
in that statement use the same law (1).

## 2. The complete carry decodes the word at both fixed clocks

For a positive gap word `w=(g_1,...,g_m)`, put

\[
A=\sum_{i=1}^{m}g_i,\quad a_i=\sum_{h=1}^{i}g_h,\quad a_0=0,
\qquad C_w=\sum_{i=0}^{m-1}3^{m-1-i}2^{a_i},\quad Q=3^m.
\tag{4}
\]

The chronological shortcut encoding is
`1 0^(g_1-1) ... 1 0^(g_m-1)`. Its length is `A`, its number of
ones is `m`, and its carry is exactly (4). An actual supplied segment
from source `p` to endpoint `q` obeys the full identity

\[
2^Aq=Qp+C_w.
\tag{5}
\]

**Decoding lemma.** Two shortcut words with the same length, the same
number of ones, and the same complete carry are equal.

**Proof.** For the first bit `b` and remaining word `u`, the chronological
recursion is

\[
C_{bu}=3^{\#1(u)}b+2C_u.
\]

Its parity determines `b`. Equal odd counts then determine the remaining
odd count; subtract the identical first term and divide by two. Induction
on the common length recovers every bit. The length is essential because
appending terminal zeroes can leave the carry unchanged. Equivalently,
for gap words of fixed `(m,A)`, the first gap can be recovered successively
from the valuation of `C_w-3^(m-1)`, with the last gap determined by `A`.
The shortcut proof also handles the zero-odd-count cases. ∎

For one actual endpoint residue `a=q mod Q`, (5) gives

\[
C_w\equiv 2^A a\pmod Q.
\tag{6}
\]

The original ordinary source has disappeared only from this exact modular
identity. It remains in (5) and in the occurrence accounting below.

## 3. Quotient channels and translated carry intervals

Set `k_w=floor(C_w/Q)`. At fixed `(A,m)`, equality of the endpoint
residue and of `k_w` gives equality of both remainder and quotient of
the carry. The decoding lemma therefore gives equality of the word.

**Theorem 1: quotient-channel injection.** At fixed `(A,m,k)`, endpoint
reduction modulo `Q` is injective on distinct complete words that satisfy
their supplied ordinary affine identities (5).

More generally, fix integers `b>=0`, `R>=1` and retain words with

\[
b\le k_w<b+R.
\tag{7}
\]

Each endpoint residue has at most `R` distinct words. Indeed its carry
remainder is fixed by (6), and the carry quotient has just `R` choices.
Only the width `R` is paid; the offset `b` can be arbitrarily large.

Let `t_j>=0` be original weights on a finite collection of actual
occurrences with common `(m,A)` and satisfying (7). Let their distinct
ordinary endpoints be `q_j`, and combine repeated words into

\[
p_w=\sum_{j:W_j=w}t_j,\quad
\sigma=\sum_jt_j\delta_{q_j},\quad
D=\sum_jt_j^2,\quad
E_{\rm rep}=\sum_{\substack{j\ne h\\W_j=W_h}}t_jt_h.
\tag{8}
\]

These are subprobability weights when the collection is a restriction of
the actual law; there is no renormalization. Since `2^A` is invertible
modulo `Q`, (5) gives the same endpoint residue for every occurrence of
one word. The finite distinct-word consumer may use any occurrence as
its source/endpoint representative while its weight `p_w` retains all
occurrences. Expanding each combined square gives exactly

\[
\sum_wp_w^2=D+E_{\rm rep}.
\tag{9}
\]

Cauchy's inequality within each residue fiber now proves

\[
\boxed{\operatorname{Col}_{Q}(\sigma)
 \le R\sum_wp_w^2=R(D+E_{\rm rep}).}
\tag{10}
\]

For an exact quotient channel, `R=1`, the residue map on distinct words
is injective, so (10) is the **equality**

\[
\boxed{\operatorname{Col}_{Q}(\sigma)=D+E_{\rm rep}.}
\tag{11}
\]

The ordinary off-diagonal consequently obeys

\[
\mathcal O_Q(\sigma)
\le (R-1)D+R E_{\rm rep}.
\tag{12}
\]

The repeated-word term is not discarded or replaced by the number of
distinct words. Different actual words can have the same ternary residue;
Theorem 1 locates those collisions in different carry-quotient channels
at fixed total clock.

## 4. The original source quotient removes within-box repetitions

If the same complete word occurs at sources `p,p'` and endpoints `q,q'`,
subtracting (5) gives

\[
2^A(q-q')=Q(p-p').
\tag{13}
\]

Since `gcd(2^A,Q)=1`, the original sources are congruent modulo `2^A`.
This argument retains both affine identities and their entire carries.

Set `ell=floor(p/2^A)`. Two nonnegative integers with equal residue and
equal quotient modulo `2^A` are equal. Consequently:

**Theorem 2: actual source-box injection.** Fix `m`. Within one box

\[
\boxed{\left(A,\ k=\left\lfloor\frac{C_w}{3^m}\right\rfloor,
\ \ell=\left\lfloor\frac{p}{2^A}\right\rfloor\right),}
\tag{14}
\]

the endpoint residue modulo `3^m` determines the complete word, the
original source, and the ordinary endpoint. For windows on one injective
ordinary orbit it also determines the occurrence index.

**Proof.** Theorem 1 first determines the word and carry. Equation (13)
and the supplied common source quotient then determine the source.
Equation (5) determines the endpoint. Finally the orbit's ordinary
sources at distinct clocks are distinct. ∎

For arbitrary original weights, the submeasure `sigma_B` in one such
box therefore has exactly

\[
\boxed{\operatorname{Col}_Q(\sigma_B)=
\sum_{j\in B}t_j^2,\qquad \mathcal O_Q(\sigma_B)=0.}
\tag{15}
\]

This is a genuine collision upper estimate on every translated actual
source box. Its constant does not depend on the absolute source height.
It covers repeated words because a repeated word in the same source
block would repeat its ordinary source, which injectivity excludes.

There is also a wider-interval version. If the original sources in a
collection lie in a real interval of width `H>=0`, (13) bounds the
multiplicity of each word by `1+floor(H/2^A)`. For the weights (2),

\[
\sum_wp_w^2
\le\frac{1+\lfloor H/2^A\rfloor}{N}\,\sigma(\mathbb N).
\tag{16}
\]

Combining (10) and (16) bounds its actual collision by
`R*(1+floor(H/2^A))*sigma(N)/N`. The bound pays the width of the
original source interval, rather than its largest absolute height.
The sharper half-open source block `[ell*2^A,(ell+1)*2^A)` contains
at most one occurrence of any one word.

## 5. A physical floor controls carry-quotient width

Consider one actual positive segment `p=x_0,...,x_m=q` with its supplied
gaps. Define its exact finite product and its local downward ratio by

\[
\kappa=\prod_{i=0}^{m-1}\frac{3x_i}{3x_i+1}>0,
\qquad B=\max_{0\le i\le m}\frac{p}{x_i}\ge1.
\tag{17}
\]

For each prefix, the exact telescoping product gives

\[
\frac{2^{a_i}}{3^i}
=\frac{p}{x_i\prod_{h<i}(3x_h/(3x_h+1))}
\le\frac B\kappa.
\]

Using all terms of (4), including the initial term, yields

\[
\boxed{\frac{C_w}{3^m}
=\frac13\sum_{i=0}^{m-1}\frac{2^{a_i}}{3^i}
\le\frac{mB}{3\kappa}.}
\tag{18}
\]

If an actual window stays above its starting value, `B=1`. A family
with `B<=B_0` and `kappa>=kappa_0>0` consequently has

`0<=k_w<1+floor(m*B_0/(3*kappa_0))`.

This supplies a concrete width in (7); its finite form requires no
canonical-envelope input. For windows on a hypothetical escaping orbit,
the pinned distinct-path reciprocal estimate gives a common positive
product floor if one is useful. The actual finite `kappa` in (17) can
also be used directly. Neither a new source minimum nor an independent
run distribution has been substituted for the supplied window.

## 6. The entire moving inverse law, with all costs retained

Fix `1<=m<=M`. Choose any retained set `I` of actual endpoint indices
in `{m,...,M}`. For each `j in I`, use its literal past window
from `q_(j-m)` to `q_j` and its original weight `t_j` from (2).
Let `sigma=sum_(j in I)t_j delta_(q_j)` and

\[
\tau=1-\sigma(\mathbb N)
=\varepsilon_{M,r}+\sum_{j\notin I,\ 0\le j\le M}t_j
\le\eta_M+\frac{N-|I|}{N}.
\tag{19}
\]

The positive remainder `zeta_(M,r)-sigma` includes every off-spine
endpoint and every omitted early window. Its residue-vector Euclidean
norm is at most its mass `tau`.

Partition `I` into any disjoint groups `G`, each with one fixed total
clock `A_G` and a carry-quotient interval of width `R_G`. Put
`W_G=sum_w(sum_(j in G,W_j=w)t_j)^2`. The triangle inequality for
the actual residue vectors and (10) give the full, same-law bound

\[
\boxed{\operatorname{Col}_Q(\zeta_{M,r})
\le\left(\sum_G\sqrt{R_G W_G}+\tau\right)^2.}
\tag{20}
\]

Every repeated-word contribution is inside `W_G`. For exact `(A,k)`
channels it is exactly `D_G+E_{{\rm rep},G}` by (11). Refining to
the actual source boxes (14) removes those within-box repetitions and
gives the alternative

\[
\boxed{\operatorname{Col}_Q(\zeta_{M,r})
\le\left(\sum_B\sqrt{\sum_{j\in B}t_j^2}+\tau\right)^2.}
\tag{21}
\]

Equations (20)--(21) preserve every cross-group term through the square
of the sum. They are not the invalid sum of the group collision bounds.
They require no global supremum of the pressure density. A very high
isolated source is charged through its actual weight and occupied box,
not through a height maximum applied to every other source.

### The ordinary diagonal limits the admissible precision

The `r`-step inverse supports of the distinct roots `q_(r+j)` are
disjoint: an endpoint has a unique forward value after that clock.
Every ordinary atom of (1) is therefore at most `1/N`. Together with
the retained atoms (2),

\[
\boxed{\frac{c_0^2}{N}\le
D_{M,r}:=\sum_n\zeta_{M,r}(\{n\})^2\le\frac1N.}
\tag{22}
\]

Always `Col_Q(zeta)=D_(M,r)+O_Q(zeta)`. Thus a putative critical
upper `Col_Q(zeta)<=A_0 Q^(-theta)` requires
`N>=c_0^2 Q^theta/A_0`. The weaker closing target

\[
\operatorname{Col}_Q(\zeta)=o(\sqrt m\,Q^{-\theta})
\tag{23}
\]

requires

\[
\boxed{\frac{N\sqrt m}{3^{\theta m}}\longrightarrow\infty,
\quad\text{equivalently }N=\omega\!\left(\frac{3^{\theta m}}{\sqrt m}\right).}
\tag{24}
\]

The lower-bound range `m^2=O(M)` alone does not supply (24).
In particular `m` comparable to `sqrt(M)` cannot satisfy such an
exponential full-collision upper. Logarithmic precisions and sufficiently
large source-time windows are compatible; the lower bound remains
available there. Subtracting the ordinary diagonal would need to be
stated explicitly, and has not been done in (20)--(23).

## 7. Where the direct upper attempt stops

The new arithmetic separates three different effects. At fixed total
clock, different-word residue collisions require different complete-carry
quotients. Within one quotient channel, the only collisions are repeated
actual words. Within one translated source box, those repetitions are
also excluded and the collision is exactly the ordinary diagonal.

This does not bound aggregation over the boxes actually occupied by a
long orbit. In (21), their masses and their cross-box residue alignments
remain correlated with the same original trajectory. Counting the boxes
as independent, adding their collision energies without cross terms, or
reinitializing the source distribution would remove precisely the terms
that have not been controlled.

Rate-free convergence `eta_M->0` is enough to make the remainder in
(19) arbitrarily small at any prescribed fixed precision by taking `M`
large and retaining the whole available window `I={m,...,M}`. Any
additional trimming must also pay its omitted original spine mass in
(19). This gives no arithmetic control of the box alignment in that same
large window. The repeated-word spacing (13) is an exact new consumer of
the original source coordinate; its interval version still pays the
number of occupied source blocks when those blocks are aggregated.

Consequently (20)--(21) have not been shown to be
`o(sqrt(m)*3^(-theta*m))` on a compatible sequence. The actual critical
upper, escape exclusion, and exclusion of nontrivial cycles remain open.
The real-law dimension statements and the older safe renewal estimates
do not supply the missing cross-box estimate under their stated domains.

## 8. Formalization boundary

`CarryFibers.lean` imports the immutable chronological carry definitions
from `research/high-variance-20261123/CycleWordAlgebra.lean`. Its finite
declarations prove carry decoding, quotient/remainder and translated
quotient-interval fiber bounds, the exact ordinary-affine endpoint
consumer, the source residue and source-block identity, the full box
injection, and weighted finite collision inequalities. The weighted
statements hold for arbitrary supplied weights over an ordered field.

The module's complete affine identities are explicit hypotheses; it
does not formalize the construction of the actual odd orbit, the
gap-to-shortcut encoding, the canonical harmonic flow, or the infinite
critical lower bound. The source-qualified law (1), its weight comparison,
the physical prefix estimate (18), the occurrence decomposition, and the
global remaining-limit discussion are written arguments. Compilation,
axiom auditing, exact finite replay, and independent semantic review are
recorded separately in the parent checkpoint. No closure theorem is
installed as an axiom.
