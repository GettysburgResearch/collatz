# L-9876 -- Exponential padding isometries have infinite section depth

Claim ID: `L-9876`  
Title: Every phase-`-34` exponential padding-counter isometry requires unbounded synchronous state  
Status: `PROPOSED`  
Authoring agent: `gpt56-synthesis-01`  
Reviewing agents: none external  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: `L-9867`; `PR3/T-0028`  
Scope: the four fixed-core phase-`-34` padding-counter charts and their inverse address maps  
Related counterexample candidates: none

## Statement

Fix one of the four padding charts of `PR3/T-0028`.  Its recovery length is

\[
r\in\{2,3,4,5\},
\qquad
P=2^{r-1},
\tag{1}
\]

and, on one fixed finite-core class, its normalized counter map is

\[
\Omega(s)
=
\frac{\mu_*+3^{-g_*}(3^{-7P})^s}{2^{r+1}}
\colon\mathbf Z_2\longrightarrow\mathbf Z_2.
\tag{2}
\]

`PR3/T-0028` proves that (2) is a bijective 2-adic isometry.  Put

\[
\lambda=3^{-7P},
\qquad
c=3^{-g_*}.
\tag{3}
\]

For `k>=0`, let

\[
h_k=\Omega|_{0^k}
\tag{4}
\]

be the rooted-tree section at the length-`k` all-zero least-significant-first
prefix, in the sense of `L-9867`.  Define its two-point slope

\[
\kappa_k=h_k(1)-h_k(0).
\tag{5}
\]

Then:

### 1. Exact zero-spine section invariant

For every `k>=0`,

\[
\boxed{
\kappa_k
=
c\,\frac{\lambda^{2^k}-1}{2^{r+1+k}}
\in\mathbf Z_2^\times.
}
\tag{6}
\]

The slopes satisfy the exact recurrence

\[
\boxed{
\kappa_{k+1}
=
\kappa_k\frac{1+\lambda^{2^k}}2
}
\tag{7}
\]

and the sharp separation law

\[
\boxed{
\nu_2(\kappa_\ell-\kappa_k)=r+k
\qquad(0\le k<\ell).
}
\tag{8}
\]

### 2. Infinite sections and state lower bound

The sections

\[
h_0,h_1,h_2,\ldots
\tag{9}
\]

are pairwise distinct.  In particular,

\[
\boxed{
|\operatorname{Sec}(\Omega)|=\infty,
}
\tag{10}
\]

and the first `K+1` zero-spine sections already give `K+1` distinct residual
states.

By the finite-section criterion of `L-9867`, no deterministic synchronous
least-significant-first Mealy machine with a fixed finite state set realizes
the all-precision map `Omega`.

### 3. The inverse physical address map is also infinite-section

Let

\[
\mathcal A(w)=\Omega^{-1}(-w)
\tag{11}
\]

be the target-address isometry used in `L-9858`.  Then

\[
\boxed{
|\operatorname{Sec}(\Omega^{-1})|
=
|\operatorname{Sec}(\mathcal A)|
=\infty.
}
\tag{12}
\]

Thus neither the forward padding chart nor its inverse physical-address chart
is a bounded synchronous transducer.  Any bounded physical stage router must
obtain a genuine cancellation after composing scale-dependent components, or
must use an asynchronous/nonstationary mechanism; it cannot treat either
chart as a fixed finite-state component.

## Definitions

Binary words and rooted-tree sections are read least-significant bit first.
For an isometry `f:Z_2 -> Z_2` and a length-`k` word `p`, its section `f|_p`
is the unique isometry satisfying

\[
f([p]+2^kz)
=
F_k(p)+2^k(f|_p)(z),
\tag{13}
\]

where `F_k(p)` is the canonical output prefix modulo `2^k`.  By `L-9867`, a
2-adic isometry has a finite synchronous LSF Mealy realization exactly when
its set of sections is finite.

The expression `lambda^s` in (2) for `s in Z_2` is the usual analytic power.
Here `P` is even, so `lambda in 1+8Z_2` and the power is defined on all of
`Z_2`.  Only the ordinary inputs `s=0,2^k` are needed for the separating
invariant (6).

## Motivation

`L-9858` showed that finite residual corrections are isometric permutations,
and `L-9863` showed that every such map is bit-causal.  `L-9867` then isolated
the exact missing condition for bounded memory: finiteness of the complete
rooted-tree section family.

The present claim evaluates that condition for the actual exponential chart
of `PR3/T-0028`.  The result is negative in the strongest direct sense: even
the single all-zero branch exposes a new residual map at every depth.  This
does not refute a composed stage router, but it prevents a proof from silently
treating the padding-address permutation as one reusable finite lookup state.

## Proof

### Exact formula for the zero-spine sections

Let

\[
u_k
=
\frac{\Omega(0)-[\Omega(0)]_{2^k}}{2^k}
\in\mathbf Z_2.
\tag{14}
\]

Substituting `s=2^kz` into (2) and subtracting `Omega(0)` gives

\[
\Omega(2^kz)-\Omega(0)
=
c\frac{\lambda^{2^kz}-1}{2^{r+1}}.
\tag{15}
\]

Comparing (15) with the canonical section identity (13) at `p=0^k` yields

\[
\boxed{
h_k(z)
=
u_k
+c\frac{\lambda^{2^kz}-1}{2^{r+1+k}}.
}
\tag{16}
\]

Taking the difference between `z=1` and `z=0` proves (6) as an identity in
`Q_2`.  Its integrality can also be read from section existence; its exact
valuation follows directly from LTE.  Indeed,

\[
\begin{aligned}
\nu_2(\lambda^{2^k}-1)
&=\nu_2(3^{7P2^k}-1)\\
&=\nu_2(3-1)+\nu_2(3+1)+\nu_2(7P2^k)-1\\
&=1+2+(r-1+k)-1\\
&=r+1+k.
\end{aligned}
\tag{17}
\]

Since `c` is odd in `Z_2`, equation (17) makes every `kappa_k` an odd unit.

### Recurrence and exact pairwise separation

Factor the numerator at the next depth:

\[
\begin{aligned}
\kappa_{k+1}
&=c\frac{\lambda^{2^{k+1}}-1}{2^{r+2+k}}\\
&=c\frac{(\lambda^{2^k}-1)(\lambda^{2^k}+1)}{2^{r+2+k}}\\
&=\kappa_k\frac{1+\lambda^{2^k}}2.
\end{aligned}
\tag{18}
\]

This proves (7).  Subtracting `kappa_k` and using (17) gives

\[
\kappa_{k+1}-\kappa_k
=
\kappa_k\frac{\lambda^{2^k}-1}{2},
\tag{19}
\]

so

\[
\boxed{
\nu_2(\kappa_{k+1}-\kappa_k)=r+k.
}
\tag{20}
\]

For `ell>k`, telescope:

\[
\kappa_\ell-\kappa_k
=
\sum_{j=k}^{\ell-1}(\kappa_{j+1}-\kappa_j).
\tag{21}
\]

The summands in (21) have the strictly increasing valuations

\[
r+k,r+k+1,\ldots,r+\ell-1.
\tag{22}
\]

The nonarchimedean valuation of a sum with a unique least-valuation summand is
the valuation of that summand.  Equations (21)--(22) prove (8).

If two sections `h_k,h_ell` were equal, their values at `0` and `1` would
have the same difference, so `kappa_k=kappa_ell`.  This contradicts (8).
Hence the zero-spine sections are pairwise distinct, proving (9)--(10).  The
Mealy-machine conclusion is exactly `L-9867/(9)--(11)`.

### Inverse and signed target address

`L-9867/(13)--(14)` gives a bijection between the section sets of an isometry
and its inverse.  Therefore (10) implies

\[
|\operatorname{Sec}(\Omega^{-1})|=\infty.
\tag{23}
\]

Negation `n(w)=-w` has a two-state synchronous LSF realization: write
`-w` as the binary complement of `w` plus one, and let the state be the
single carry bit.  Hence `n` has finitely many sections.

Now \(\mathcal A=\Omega^{-1}\circ n\).  If `mathcal A` had finitely many
sections, then

\[
\Omega^{-1}=\mathcal A\circ n
\tag{24}
\]

would also have finitely many sections by the composition law of
`L-9867/(14)`, contradicting (23).  This proves (12) and completes the
claim. QED

## Dependency audit

- `PR3/T-0028` supplies the four chart parameters, the exponential formula
  (2), and the fact that `Omega` is a bijective isometry of `Z_2`.
- `L-9867` supplies canonical sections, the finite-state equivalence, and the
  inverse/composition laws for section sets.
- The explicit section formula, slope recurrence, LTE separation, and
  infinite-section conclusion are proved here.
- No completed logarithmic target, residual stabilization assumption, or
  computational search is used.

## Gap audit

- Infinite sections of `Omega` do not imply infinite sections of every
  scale-to-scale conjugate \(\Psi_1\circ T\circ\Psi_0^{-1}\).  Infinite
  components can cancel in a special composition.
- The result excludes one fixed synchronous one-input-bit/one-output-bit
  transducer.  It does not exclude asynchronous, variable-length, or
  explicitly scale-dependent control.
- A linear lower bound on exposed section states is not a lower bound on the
  amount of ordinary residual information available in a physical stage.
- The normalized corrections of `L-9858` are centered restrictions of the
  inverse address chart.  This claim does not assert that every such
  restriction separately has infinitely many sections.
- No finite or infinite address is proved to be an ordinary Collatz seed.

## Adversarial tests

- The canonical output term `u_k` in (16) depends on the wrapped prefix
  `[Omega(0)]_(2^k)`.  It cancels from `kappa_k`; dropping it from the full
  section rather than only from the difference would be incorrect.
- The denominator in (6) is `2^(r+1+k)`, not `2^(r+k)`.  LTE gives precisely
  the same valuation, so `kappa_k` is odd.
- Replacing `lambda=3^(-7P)` by `lambda=1` destroys (17) and collapses the
  invariant.  The nontrivial exponential base is essential.
- Consecutive inequality alone would not rule out a later repeated section.
  The telescoped valuation (8) proves pairwise separation for every `k<ell`.
- The constant `mu_*` plays no role in the slope invariant, but it remains
  essential to the integrality of the original chart (2).
- Infinite sections of the inverse follow from the exact inverse-section
  bijection, not from a general claim that inversion preserves arbitrary
  automata complexity.

## Remaining uncertainty

Can the complete physical scale update cancel the infinite exponential
section drift against the residual zipper and the next inverse chart?  The
separating invariant (8) is now a concrete quantity to track through that
conjugacy, but this claim does not perform the cancellation audit.

## Suggested next attack

For consecutive charts, write the physical update as

\[
\mathcal U_m
=
\mathcal A_{m+1}\circ T_m\circ\mathcal A_m^{-1}.
\]

Evaluate the two-point slope of its zero-prefix sections.  If the factor
`(1+lambda^(2^k))/2` survives after the odd-affine zipper normalization, (8)
proves unbounded state for the full update.  If it cancels, the cancellation
identity supplies the finite recurrence that the router program currently
lacks.
