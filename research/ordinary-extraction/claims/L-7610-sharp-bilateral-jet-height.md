# L-7610 — Sharp bilateral height for complete-factor quotient jets

**Claim ID:** `L-7610`  
**Title:** The exact fixed-point height, not the coarser endpoint-plus-displacement envelope, controls complete-factor jet lifting  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-global-01` (`GPT-5.6 Pro`)  
**Reviewing agents:** none  
**Created:** 2026-08-01  
**Last updated:** 2026-08-01  
**Dependencies:** branch-qualified PR #83 corrected `L-6909` and `L-6912`; for the support corollary, branch-qualified PR #81 `L-6816` / PR #83 `T-6914`  
**Scope:** complete-factor quotient jets for coefficient-first-crossing non-descents  
**Related counterexample candidates:** none

This is a new strengthening discovered during the frozen review of PRs #80, #81, and #83. It remains `PROPOSED` and is not used to verify those source PRs.

## Statement

Let a shortcut-parity word of length `j` and weight `q` have affine map

\[
T_w(x)=\frac{Qx+A}{P},
\qquad
P=2^j,
\quad
Q=3^q,
\quad
D=P-Q>0.
\]

Suppose its canonical source and endpoint satisfy

\[
T_w(r)=s=r+d,
\qquad
r,s\in\mathbf Z_{>0},
\quad d\in\mathbf Z_{\ge0}.
\]

Put

\[
C=\frac QP,
\qquad
E=\frac AP,
\qquad
H_w=\frac AD=\frac{E}{1-C}.
\]

Then:

### A. Exact bilateral height formulas

\[
\boxed{
 r=\frac{E-d}{1-C},
 \qquad
 s=\frac{E-Cd}{1-C}.}
\tag{1}
\]

Consequently,

\[
\boxed{0<r\le s\le H_w,}
\tag{2}
\]

with equality `r=H_w` or `s=H_w` if and only if `d=0`.

For an acyclic near-return `d>0`,

\[
\boxed{0<r<s<H_w.}
\tag{3}
\]

### B. Exact candidate-dependent jet threshold

Let `U` be a unitary divisor of `D`, with complementary factor

\[
D=U K,
\qquad
\gcd(U,K)=1.
\]

Assume PR #83 `L-6912` supplies residues

\[
\delta_U\equiv d\pmod U,
\qquad
\rho_U\equiv r\pmod U,
\qquad
\sigma_U\equiv s\pmod U,
\]

where `rho_U` and `sigma_U` are its source and endpoint quotient jets.

If

\[
oxed{U>H_w,}
\tag{4}
\]

then all three residues lift uniquely to the exact ordinary values:

\[
oxed{\delta_U=d,\qquad ho_U=r,\qquad \sigma_U=s.}
\tag{5}
\]

Equivalently, it is enough that

\[
oxed{U\ge \left\lfloor\frac AD\right\rfloor+1.}
\tag{6}
\]

### C. Sharper uniform first-crossing threshold

For every coefficient-first-crossing non-descent, the reviewed bilateral bound gives

\[
0\le d<E<\frac q3.
\]

Therefore

\[
H_w=\frac{E}{1-C}
<
\frac{q}{3(1-C)}.
\tag{7}
\]

Define

\[
oxed{
\mathcal B_j^{\rm sharp}
=
\left\lceil
\frac{q}{3(1-3^q/2^j)}
\right\rceil.}
\tag{8}
\]

Then every unitary factor satisfying

\[
U\ge\mathcal B_j^{\rm sharp}
\]

recovers `d,r,s` exactly.

This removes the additional `q/3` term from the coarser universal endpoint bound in PR #83 `L-6912`.

### D. Support-sensitive threshold

Let `u` be the upper-mechanical word at the same `(j,q)`, and suppose `w` has `R` displaced odd positions. PR #81 `L-6816` / PR #83 `T-6914` give

\[
E_w
<
E_u-rac{C R}{12}.
\tag{9}
\]

Hence

\[
oxed{
H_w
<
\frac{E_u-CR/12}{1-C}.}
\tag{10}
\]

Thus the same rough support that narrows the allowed displacement interval also lowers the exact modulus needed to recover both ordinary quotient jets.

### E. Sharpened balanced-or-dominant reduction

The elementary factor-partition argument of PR #83 `L-6912` may be repeated with `mathcal B_j^sharp` in place of its coarser bound.

In particular, if

\[
D>(\mathcal B_j^{\rm sharp})^3,
\tag{11}
\]

then either:

```text
balanced:
  D=UV for unitary U,V both larger than mathcal B_j^sharp,
  so both blocks recover the same exact d,r,s;

or

dominant:
  D=Wc for one complete prime power W with
  c<=mathcal B_j^sharp and W>D/mathcal B_j^sharp,
  so W recovers d,r,s and c must complete the divisibility.
```

The same replacement may be made with the smaller candidate-specific threshold from `(10)` whenever the support data are already known.

## Proof

The corrected bilateral equations are

\[
A=Dr+Pd=Ds+Qd.
\tag{12}
\]

Divide the source equation by `P`:

\[
E=(1-C)r+d,
\]

which gives the first formula in `(1)`.

Divide the endpoint equation by `P`:

\[
E=(1-C)s+Cd,
\]

which gives the second formula in `(1)`.

Because `r>0`, the first formula gives `d<E`. Since `d>=0` and `0<C<1`,

\[
r=H_w-rac d{1-C}\le H_w,
\]

and

\[
s=H_w-rac{Cd}{1-C}\le H_w.
\]

Also `s-r=d>=0`. Equality in either upper bound forces `d=0`; conversely `d=0` gives `r=s=H_w`. This proves `(2)--(3)`.

The congruences defining `delta_U,rho_U,sigma_U` are those of PR #83 `L-6912`. For a genuine near-return, all three canonical residues are congruent to `d,r,s` modulo `U`. The displacement already satisfies `0<=d<E<H_w`. Under `(4)`, equations `(2)--(3)` place all three ordinary values in `[0,U)`, so their canonical residues modulo `U` equal the values themselves. This proves `(5)--(6)`.

Equation `(7)` follows from `E<q/3`; `(8)` then implies `U>H_w`. Equation `(10)` follows by dividing `(9)` by `1-C>0`.

Finally, the balanced-or-dominant proof in `L-6912` uses only:

1. a positive integer threshold above every admissible ordinary source and endpoint;
2. complete prime-power components of `D`;
3. multiplication of components until a unitary product crosses that threshold.

Equations `(7)--(8)` supply a smaller threshold with exactly the same properties, so the partition proof carries over verbatim. ∎

## Why the strengthening matters

PR #83 treated the displacement bound and endpoint/source height as two successive additions. The bilateral identities show that the displacement is already subtracted inside both ordinary quotient formulas.

The actual common height is the rational fixed point

\[
\frac AD,
\]

not

\[
\frac{q}{3(1-C)}+\frac q3.
\]

The gain is polynomial rather than exponential, so it does not by itself close FC*. It does, however:

- enlarge the set of factors whose quotient jets lift exactly;
- strengthen the balanced/dominant factor dichotomy;
- couple PR #81's square-root support loss directly to PR #83's complete-factor obstruction;
- remove avoidable slack from any future cross-prime contradiction.

## Dependency audit

- The proof uses only the corrected source/endpoint equations and the definitions of the unitary quotient jets.
- The support-sensitive clause imports the strict support loss and preserves its source status.
- No result from this file is used retroactively in the frozen verification verdicts.

## Gap audit

- Exact jet recovery is not jet incompatibility.
- Balanced blocks may still return identical `d,r,s`.
- A dominant giant factor may still be completed by its small cofactor.
- The cycle level `d=0` remains included.
- The general `gcd(j,q)>1` resultant components remain open.
- No FC*, SC*, or Collatz proof follows.

## Adversarial tests

1. At `d=0`, equations `(1)` give `r=s=A/D`, as required for a cycle.
2. For `d>0`, the endpoint is closer to `A/D` than the source because `0<C<1`:
   \[
   H_w-s=\frac{Cd}{1-C}<\frac d{1-C}=H_w-r.
   \]
3. Replacing `U>H_w` by only `U>d` is insufficient to recover the quotient jets.
4. The ceiling in `(8)` is safe even when `q/[3(1-C)]` is an integer, because `(7)` is strict.
5. The theorem never infers full-denominator divisibility from one large factor.

## Remaining uncertainty

None in the elementary algebra. The usefulness of the sharper threshold for proving a uniform cross-factor contradiction is open.

## Suggested next attack

In the balanced case, compare the exact triples `(d,r,s)` recovered from the two complementary unitary blocks after applying the support-sensitive threshold `(10)`. In the dominant case, exploit the now smaller cofactor bound to classify or contradict the completing cofactor. Any theorem obtained there must be submitted separately as `PROPOSED`.