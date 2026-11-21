# Finite coefficient-strip escape on ordinary Collatz paths

## Status and exact result

`CoefficientCounting.lean` and `CoefficientPeaks.lean` have passed Lean 4.34.1
with `-DwarningAsError=true`, against the packet's pinned Mathlib dependencies.
Their printed principal theorem closures contain only `propext`,
`Classical.choice`, and `Quot.sound`. No additional axiom, `sorry`, native
evaluation trust, or probabilistic assumption is used.

For the shortcut Collatz map, put

\[
x_t=T^t(n),\qquad q_t=\#\{i<t:x_i\text{ is odd}\},\qquad
C_t=\frac{3^{q_t}}{2^t}.
\]

For every natural source `n` and positive integer `B`, define

\[
k=70(\lfloor\log_2 B\rfloor+3),\quad M=2^k,\quad N=n+M+1,
\]

\[
H=6B^2(n+N)+1=6B^2(2n+M+1)+1.
\]

**Theorem `finite_coefficient_exit`.** There is a clock `t <= H` such that

\[
\boxed{3^{q_t}<2^t\quad\text{or}\quad B2^t<3^{q_t}.}
\]

Thus an actual ordinary path cannot keep every coefficient in the closed
strip `[1,B]` through this displayed finite horizon. The witness is necessarily
positive because `C_0=1` and `B>=1`. The formal statement includes source zero;
the positive ordinary sources required by Collatz are a direct specialization.

The theorem has no assumed absence of cycles, no injectivity premise, and no
infinite-orbit premise. All coefficient comparisons in the Lean statements are
natural-number inequalities.

The auxiliary theorem `escapeClock_polynomial` proves the entirely explicit
bound

\[
\boxed{H\le 12B^2n+6\cdot2^{210}B^{72}+6B^2+1.}
\]

The constants are coarse. The purpose is a transparent finite certificate,
not a practical computation cutoff or an optimized exponent.

## Exact counting, followed by ordinary dynamics

### 1. One finite parity period

`CoefficientCounting.parity_weight_sum` proves

\[
\sum_{0\le r<2^k}2^{q_k(r)}=3^k.
\]

The induction pairs `r` with `r+2^k`. Their first `k` odd counts agree, and
their `k`-step endpoints differ by the odd integer `3^(q_k(r))`. Their next
parities therefore differ, so the two next-step weights sum to three times
the old weight. This is an exact identity across all ordinary residue classes;
it makes no claim that successive parities on a fixed orbit are independent.

For the selected `k`, let the resistant residues be

\[
R_B=\{0\le r<2^k:2^k\le B3^{q_k(r)}\}.
\]

The fixed inequalities

\[
2\cdot3^{42}\le2^{70},\qquad
2\cdot3^{70}\le2^{112}
\]

and the exact moment imply

\[
4B\,\#R_B\le2^k.
\]

Here, writing `b=floor(log2 B)+3`, every resistant residue has at least
`42b` odd inputs. Its moment contribution is at least `2^(42b)`, while
`4B<=2^b` supplies the required final margin.

The formal `packing` theorem consequently says: if `N` distinct ordinary
values lie in `[0,X]` and all satisfy the resistant coefficient inequality,
then

\[
\boxed{4BN\le X+2^k.}
\]

The quotient-residue injection counts the final partial period explicitly;
the `2^k` boundary cost remains in the conclusion.

### 2. Both affine-correction inequalities are retained

Suppose provisionally that `1<=C_t<=B` for every `t<=H`. Direct induction
on the actual shortcut recurrence gives

\[
2^t x_t\le3^{q_t}(n+t),
\]

\[
3^{q_t}(3Bn+q_t)\le3B\,2^t x_t.
\]

At an odd step, the exact identity is `2*x_(t+1)=3*x_t+1`; at an even step
it is `2*x_(t+1)=x_t`. The lower coefficient bound pays the new correction
in the first inequality. The upper coefficient bound pays the new correction
in the second. In particular, the positive affine correction is never erased
when reasoning about repetition or coefficient stopping.

It follows that

\[
x_t\le B(n+t),\qquad 3Bn+q_t\le3Bx_t.
\]

Also `2^t<=3^(q_t)<=4^(q_t)` gives `t<=2q_t`. Therefore

\[
\boxed{t\le6Bx_t\qquad(t\le H).}
\]

### 3. Finite injectivity is proved

If `x_i=x_j` for `i<j<N`, determinism reduces every later clock to a
strictly smaller clock until it falls below `j`. Thus every later state is
bounded by the maximum of the first `j` states, which is at most `B(n+N)`.
Applying the preceding clock bound at `H` would give

\[
H\le6Bx_H\le6B^2(n+N),
\]

contrary to the definition of `H`. Hence the first `N` states are distinct.
Only the provisional coefficient strip through `H` is used. The deterministic
consequence of a repeated pair is proved separately, with no coefficient
assumption after `H`.

### 4. The actual shifted prefixes are resistant

For every `j<N`, the chosen parameters ensure `j+k<=H`. Exact odd-count
addition and the strip bounds give

\[
\frac{3^{q_k(x_j)}}{2^k}=\frac{C_{j+k}}{C_j}\ge\frac1B.
\]

The Lean proof uses the equivalent multiplied integer inequality. Thus all
`N` distinct states satisfy the counting theorem with `X=B(n+N)`, giving

\[
4BN\le B(n+N)+M.
\]

But `N=n+M+1` and `B>=1` imply `Bn+M<BN`, contradicting that packing
inequality. This proves the finite exit alternative.

## Relation to existing repository work

This result does **not** claim to discover qualitative coefficient escape.
The prior sources already establish or propose stronger asymptotic statements
in their stated scopes:

- The accepted
  [integrated coefficient-stopping reference at checkpoint 65ee193](https://github.com/GettysburgResearch/collatz/blob/65ee193029bc04f5ee1b9ca25b6b96d6f1055695/research/integrated/coefficient-stopping/README.md)
  proves that an all-supercritical positive ordinary orbit diverges and records
  the equivalence between `SC*` and universal finite coefficient stopping.
- [PR92's ORBIT_MELLIN.md at 7bb6d36](https://github.com/GettysburgResearch/collatz/blob/7bb6d36d3bc37dd09b52aa9a23c8e33973032359/research/astra-three-routes/pass2/ORBIT_MELLIN.md)
  derives full `C_t -> infinity` for a nonperiodic positive ordinary orbit
  from orbit sparsity and a bounded correction product. That source explicitly
  disclaims priority for qualitative reciprocal summability and coefficient
  escape. Its orbitwise conclusions do not transfer automatically to inverse
  basins with merging sources.
- [PR92's FINITE_RECORDS.md at the same pin](https://github.com/GettysburgResearch/collatz/blob/7bb6d36d3bc37dd09b52aa9a23c8e33973032359/research/astra-three-routes/pass3/FINITE_RECORDS.md)
  gives finite simple-path distortion budgets and a finite descent-or-repetition
  consequence from supplied coefficient-stopping certificates on a near-source
  window. That note marks its statements as proposed pending independent review
  and keeps `SC*` and cycle exclusion open.

The contribution here is a fully finite, elementary integer proof checked by
Lean, together with one explicit uniform escape horizon. It does not import
those analytic or infinite-path arguments, and it derives the finite
injectivity needed for its counting step.

## What remains open

`supercritical_peak` specializes the main theorem to a supplied ordinary path
whose every prefix coefficient is at least one. It gives, for each positive
`B`, a coefficient peak above `B` by `escapeClock n B`.

This necessary peak growth is compatible with an all-supercritical divergent
orbit. The theorem does not eliminate the upper-exit branch and therefore does
not prove `SC*`. It also does not identify a coefficient crossing below one
with an ordinary strict descent: the affine correction must still be paid,
as the existing offset certificates and first-crossing program require.

No statement here proves universal convergence, rules out every positive
cycle, or turns the earlier selected dyadic exponent blocks into coverage of
every forced mark. The result supplies a verified finite interface for the
coefficient-stopping program outside the recent dyadic-band cluster.

## Verification pins

- `CoefficientCounting.lean` SHA-256:
  `070d4f0f0da69130b04033b8aac169fd1e9f763c3435ff78448ba1dbe232e51e`.
- `CoefficientPeaks.lean` SHA-256:
  `34c522620ab742bd728db2d2ebf958b131a981fb5edd9d7c9ad160ee28d50db9`.
- Mathlib revision: `d13f23b723b8a846827a245b89c10fc7d3f11612`.
- Lean: `4.34.1`; development runs used one worker and warnings as errors.
- The packet's root replay and audit receipt records the final publication gate.
