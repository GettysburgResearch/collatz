# L-9846 — Necessary signature of an ordinary raw-return fiber

Claim ID: `L-9846`  
Title: Any ordinary point on the raw-return invariant fiber has linear real growth and Sturmian low residues  
Status: `PROPOSED`  
Authoring agent: `gpt56-synthesis-01-h`  
Reviewing agents: `gpt56-synthesis-01`  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: `L-9841`, `L-9843`, `L-9845`  
Scope: necessary arithmetic and real-growth signatures of a hypothetical ordinary raw-return endpoint  
Related counterexample candidates: none

## Definitions

Use the raw phase system of `L-9841` and `L-9845`:

\[
\mathcal I=\left(1,\frac98\right],
\qquad
R_{n+1}=P(R_n),
\qquad
r_n=r(R_n)\in\{6,7\},
\tag{1}
\]

where `r_n=7` on `1<R_n<=xi^(-1)` and `r_n=6` on the complementary
half-open branch. Put

\[
\ell=\log(9/8),
\qquad
\rho=\frac{\log(1/\xi)}{\ell},
\qquad
x_n=\frac{\log R_n}{\ell}\in(0,1].
\tag{2}
\]

Let `alpha:I->Z_2` be the unique invariant endpoint graph of `L-9845`.
Assume, conditionally, that for one phase

\[
\boxed{N_0=\alpha(R_0)\in\mathbb Z_{\ge0},}
\qquad
N_n=\alpha(R_n).
\tag{3}
\]

Use `b_r=(7/16)(1+mu_r)`, `L=9/8`, and `sigma=L xi`, and define the exact
cocycle bounds of `L-9843` by

\[
c_-=min\!\left(\frac{b_7}{L},\frac{b_6}{\sigma}\right),
\qquad
c_+=\max\!\left(\frac{b_7}{\sigma},b_6\right).
\tag{4}
\]

## Statement

### 1. Integral macro orbit with fixed valuation

Every graph iterate is an ordinary positive integer and satisfies

\[
\boxed{
N_{n+1}=F_{r_n}(N_n),
\qquad
N_n\in\mathbb Z_{>0},
\qquad
\nu_2(N_n)=9
\quad(n\ge0).
}
\tag{5}
\]

Thus an ordinary graph point produces one infinite integral orbit at the raw
macro checkpoints; there is no further branch choice.

### 2. Exact linear real-growth signature

Put `w_0=N_0/R_0`. For every `n>=1`,

\[
\boxed{
w_0+nc_-
\le\frac{N_n}{R_n}
<w_0+nc_+.
}
\tag{6}
\]

Equivalently,

\[
\boxed{
R_n(w_0+nc_-)
\le N_n
<R_n(w_0+nc_+),
}
\tag{7}
\]

and, since `1<R_n<=L`,

\[
\boxed{
w_0+nc_-<N_n<L(w_0+nc_+).
}
\tag{8}
\]

The phase-normalized growth has the exact every-orbit limit

\[
\boxed{
\lim_{n\to\infty}\frac{N_n}{nR_n}
=\overline\phi
=\frac{103271}{944784\log(9/8)}.
}
\tag{9}
\]

### 3. Sturmian residue signature

At every macro checkpoint,

\[
\boxed{
N_n\equiv
\begin{cases}
\mathtt{0x0B6EB200}\pmod{2^{32}},&r_n=7,\\
\mathtt{0x8B6EB200}\pmod{2^{32}},&r_n=6.
\end{cases}
}
\tag{10}
\]

Consequently the two-symbol residue sequence is exactly the Sturmian branch
coding, merely with its letters renamed. In particular it is aperiodic, has
factor complexity `p(m)=m+1`, and the first residue has exact count

\[
\boxed{
\#\{0\le j<n:
N_j\equiv\mathtt{0x0B6EB200}\pmod{2^{32}}\}
=n\rho+x_n-x_0.
}
\tag{11}
\]

Hence its limiting frequencies are `rho` and `1-rho`, with discrepancy
strictly smaller than one.

### 4. Necessary-signature boundary

Equations (5)--(11) are necessary consequences of the conditional assumption
(3). They neither prove that an ordinary graph point exists nor rule one out.
They concern exact raw macro checkpoints, not every intermediate Collatz
iterate, and residue-word aperiodicity is not by itself a theorem of 2-adic
irrationality.

## Proof

The ordinary-integer criterion `L-9845/(28)--(31)` applied at `R_0` proves
that every forward graph iterate is integral. Its valuation theorem gives
`nu_2(N_n)=9` at every phase; since (3) is nonnegative and exact valuation
nine excludes zero, all `N_n` are positive. This proves (5).

The macro map of `L-9845` is the real affine return of `L-9843`, because its
exact coefficients satisfy

\[
\frac{\mathcal V_r}{\mathcal U_r}=a_r,
\qquad
\frac{\mathcal B_r}{\mathcal U_r}
=\frac7{16}(1+\mu_r)=b_r.
\tag{12}
\]

Therefore `w_n=N_n/R_n` obeys

\[
w_{n+1}=w_n+\phi(R_n),
\qquad
c_-\le\phi(R_n)<c_+.
\tag{13}
\]

Summation proves (6), and multiplication by `R_n` proves (7)--(8).
The every-orbit mean theorem `L-9843/(17)` gives
`(w_n-w_0)/n -> bar(phi)`; the fixed term `w_0/n` vanishes, proving (9).

Finally, graph invariance writes
`N_n=G_(r_n)(N_(n+1))`. The separated-cylinder decoder `L-9845/(34)--(35)`
therefore gives (10). The underlying branch word is the Sturmian coding of
the irrational phase rotation. Relabeling its two letters preserves
aperiodicity and factor complexity, while `L-9845/(22)` is exactly (11).
This completes the proof. ∎

## Motivation

`L-9843` and `L-9845` describe the same raw return in opposite completions:
the real normalized endpoint drifts linearly, while inverse 2-adic contraction
selects one compatible endpoint. Their combination gives a falsifiable
signature for any hypothetical ordinary intersection: linear phase-normalized
growth, fixed valuation nine, and a prescribed aperiodic low-residue stream.

## Dependency audit

- `L-9841` supplies the irrational phase rotation and Sturmian branch coding.
- `L-9843` supplies the exact cocycle bounds and every-orbit mean drift.
- `L-9845` supplies graph invariance, ordinary integrality, valuation nine,
  and the modulo-`2^32` branch decoder.
- No new existence, rationality, or physical-intermediate-orbit assertion is
  imported.

## Gap audit

- The hypothesis (3) is not established.
- Linear growth at macro checkpoints is compatible with fixed 2-adic
  valuation and is not a contradiction.
- A Sturmian sequence of renormalized residues need not be a literal block
  decomposition of the binary expansion of `N_0`.
- Macro integrality does not by itself certify every physical first-crossing
  or intermediate Collatz condition.

## Adversarial tests

- The limit is `N_n/(nR_n)`, not necessarily `N_n/n`; the phase `R_n` does
  not converge.
- The residue `0x0B6EB200` labels branch `7`, so its frequency is `rho`.
- Exact valuation nine gives only the common congruence `512 mod 1024`; the
  bit-31 separation is needed to recover the branch.
- The result is conditional even though every conclusion after (3) is exact.

## Remaining uncertainty

`L-9850` supersedes the conditional ordinary-point gap for this architecture:
it combines the signature above with integer packing to prove
`alpha(I) intersection Z` is empty. Thus no ordinary macro orbit realizes
(5)--(11). The conditional signature remains useful for diagnosing other
return systems, but is no longer a live possibility for this raw return.

## Suggested next attack

Generalize the `L-9850` packing argument. For another uniquely ergodic return,
compare its mean normalized drift with `integral R^(-1) dnu`; a coefficient
above one, together with a recursive decoder that prevents repeated ordinary
endpoints, gives the same exclusion without any rational-address converse.
