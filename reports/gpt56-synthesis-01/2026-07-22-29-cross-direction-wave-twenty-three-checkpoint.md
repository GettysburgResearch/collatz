# Cross-direction lemma forge -- wave twenty-three checkpoint

Date: 2026-07-22
Agent: `gpt56-synthesis-01`
Issue: #29
Branch: `agent/gpt56-synthesis-01/29-cross-direction-lemmas`
Status: four proposed structural reductions; no counterexample claimed

## Checkpoint reason

The user requested a near-term publication checkpoint.  New attacks were
frozen, each proof lane returned a bounded handoff, the actual files were
reviewed, and only completed claims were integrated.

The pre-checkpoint memory snapshot remained healthy:

```text
free physical memory: 8.99 GiB
total physical memory: 15.41 GiB
used: 41.6 percent
```

## Live reconciliation

- Main remained at `b40e5c44959b20842e6c064084c668f5243b6ebd`.
- Issue #9 was newly claimed on
  `agent/gpt56-cycle-01/9-compressed-cycle-synthesis`; that branch still
  pointed to main at the cutoff.  Its affine-monoid issue supplement was used
  as the cycle notation source.
- PR #11 remained at `7950713cbb6ba0af0a424806cc36ce01ad24cf9e`.
- PR #20 remained at `82ca2f932438a9fe0897704ba62959ca23ec830f`.
- PR #33 remained at `c9d62bce3e93f5785f72e4520bc576863d9379eb`.
- PR #38 remained at `5ad965771869a647102e22115ed56749dbe2e254`.
- Issue #27 supplied the spectral-support question; no separate implementation
  branch existed at the cutoff.

## Result 1 -- compressed cycles reduce to primitive necklaces

[`L-9904`](../../research/cross-direction-lemmas/claims/L-9904-compressed-cycle-primitive-root.md)
proves an exact search reduction for issue #9 and PR #11.

For a nonempty accelerated valuation word `w`, write

\[
 2^{A(w)}S^{|w|}(x)=3^{|w|}x+C(w),
 \qquad D(w)=2^{A(w)}-3^{|w|}.
\]

The divisibility condition

\[
 D(w)>0,\qquad D(w)\mid C(w)
\]

already forces the reconstructed start and every intermediate state to be
positive odd integers with exactly the prescribed valuations.  It is a
complete finite certificate, not merely a fixed-point equation.

If `w=v^s`, then one common geometric factor multiplies both `C` and `D`.
The reduced fixed point, exact orbit, and validity of the certificate are
therefore exactly those of `v`.  Cyclic rotations give the actual successive
odd starting states on the same cycle.  Up to start, genuine certificates are
admissible primitive necklaces.

The true parameters used in cycle bounds are those of the primitive root:

- odd length `|v|`;
- shortcut period `A(v)`; and
- local-minimum count `#{i:v_i>=2}`.

Powered grammar productions cannot inflate any of these.

## Result 2 -- bounded essential leaves survive unbounded nominal width

[`T-9834`](../../research/cross-direction-lemmas/claims/T-9834-bounded-essential-width-degeneracy-forest.md)
is the careful extension of `T-9831` toward PR #38 atom `ACL-N071`.

Every finite integer zero sum can be split recursively into
inclusion-minimal nondegenerate zero-sum leaves.  The ambient coordinate count
and number of leaves may grow.  If the following leaf data are uniform,
however,

- width at most `W`;
- coefficient alphabet;
- finite internal prime union;
- ordered endpoint mask; and
- a primitive endpoint-product exponent below one,

then fixed-dimension Evertse applies after leaf type binning.  The possible
primitive projective leaves form a finite alphabet.

More strongly, if one bounded leaf carries divergent primitive height from
the ambient stage, then that leaf cannot satisfy the subunit endpoint gate.
The raw sufficient certificate uses the *leaf's* normalization loss:

\[
 \Theta<d(1-\gamma),\qquad d<1.
\]

Forest shapes, repeated leaf types, raw scale multipliers, and symbolic forest
words need not be finite.  Six counterfamilies in the claim show why each
uniformity and height-carrying hypothesis is necessary.

## Result 3 -- exact functional-graph point-spectrum support

[`L-9905`](../../research/cross-direction-lemmas/claims/L-9905-functional-graph-point-spectrum-support.md)
resolves PR #38 atom `ACL-N054` for a faithful atomic operator and also marks
the remaining bridge to issue #27's nuclear program.

For a deterministic countable map, the atomic pushforward on
`ell^1(X,w)` is bounded exactly when

\[
 \sup_x{w(Tx)\over w(x)}<\infty.
\]

A completely invariant basin gives an isometric coordinate quotient.  Any
nonzero quotient point eigenvector restricts to one unaccounted functional
component, which contains either a nontrivial directed cycle or no cycle at
all.

For shortcut Collatz and `w_s(n)=(1+n)^(-s)`, `s>1`, the pushforward has norm
`2^s`.  Quotienting by the *entire* basin of `{1,2}`, a nonzero quotient is
equivalent to nonzero point spectrum: cycles give root-of-unity vectors, and
cycle-free components give exact bilateral-path eigenvectors for

\[
 1<|\lambda|<2^s.
\]

The one-sided orbit sum suggested in issue #27 has a boundary term and is not
an eigenvector.  A cycle-only quotient gives false positives, approximate
spectrum can survive on terminating finite chains, and smooth composition
eigenfunctions do not have atomic support content.  The faithful pushforward
is noncompact and hence nonnuclear, so a Fredholm implementation still needs
a proved support-preserving intertwiner back to this quotient.

## Result 4 -- the period-ten gcd is an adjacent half-core problem

[`T-9835`](../../research/cross-direction-lemmas/claims/T-9835-adjacent-schur-core-gcd-localization.md)
sharpens the open gcd in `T-9830`.

Let `G_n` be the prime-to-six base Schur core and let

\[
 \mathcal C_n
 =\prod_{j=1}^{n}(81^{9Sj}-64^{9Sj}).
\]

Exact base-Hankel factorization and

\[
 \varepsilon_{n,0}={\Delta_{n+1}\over\Delta_n}
\]

show that the prime-to-six part of the raw consecutive cross determinant is

\[
 \mathcal C_nG_{n+1}^2.
\]

Using both neighbors traps the evaluated numerator/denominator gcd by

\[
 \boxed{
 g_n\mid\mathcal C_n\gcd(G_n,G_{n+1})^2.}
\]

The cyclotomic step is only quadratic:

\[
 \log_2\mathcal C_n
 ={9S\log_2 81\over2}n(n+1)+O_S(1).
\]

Hence period-ten quadratic primitive height would require

\[
 \log_2\gcd(G_n,G_{n+1})
 \ge27S\log_2(3)n^3-O_{W,m}(n^2).
\]

At least half of the Schur core's cubic logarithmic mass must therefore be
shared across adjacent orders.  The next exact target is an adjacent-core
resultant/primitive-divisor upper bound or a proved factor accounting for
that mass.

## Review and validation

- `L-9904` was independently reconstructed after its exhaustive exact-word
  audit; one missing multiplication marker in the powered local-minimum count
  was corrected.
- `T-9834` received an independent H/Evertse cold review of leaf splitting,
  type freezing, normalization, marked height, and all six counterfamilies.
- `L-9905` received an integrating review of both operator norm criteria,
  quotient support, the bilateral Collatz construction, the approximate-
  spectrum counterexample, and noncompactness.
- `T-9835` received an independent full-file reconstruction of the Hankel
  factorization, Schur complement, two-order clearing, divisibility, and all
  cubic constants.
- Claim-ID uniqueness, metadata, local links, equation/fence balance,
  whitespace, and the exact staged publication scope are checked before the
  checkpoint commit.

## Boundary

No result in this packet produces a Collatz counterexample or proves the
conjecture.  In particular:

- primitive compressed cycles still have to be found or excluded;
- a physical growing-width stage must supply bounded leaves and a
  height-carrying leaf;
- no spectral excess or nuclear-to-atomic bridge is supplied; and
- no upper bound for the adjacent Schur-core gcd is proved.

All four entries remain `PROPOSED` pending repository-independent review.
