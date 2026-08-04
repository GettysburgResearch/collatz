# Residue-cylinder dichotomy packet

**Agent:** `gpt56-cylinder-01`  
**Issue:** `#31`  
**Namespace:** `97xx`  
**Status:** all native theorem-level claims are `PROPOSED`; experiments are exact finite checks only  
**Created:** 2026-07-22  
**Last updated:** 2026-07-22, full corrected-stage Evertse closure

## Headline

This packet proves side **A** of the ordinary-integer residue-cylinder dichotomy for two complete, fully quantified classes cut from PR #3's phase-`-34` tower system.

### Direct comparison class

`T-9702` treats one direct connector from height `t` to `2t`. Every infinite four-type directive has infinitely many nonzero initial residue blocks, and its unique `Z_2` completion is not a signed ordinary integer.

### Corrected composed 256-transition class

`T-9705` treats the genuinely supercritical chronological corrected stage, with arbitrary physically overlapping type words and one unbounded scale counter. For every infinite directive,

```text
a_k != 0 infinitely often,
the unique Z_2 completion is not in Z.
```

Thus no positive ordinary marked Collatz initialization realizes this complete stage architecture. The result is uniform over the full directive class, not a sampled or eventually periodic family.

No finite-prefix compatibility, entropy surplus, completed logarithm, or `Z_2` limit is counted as an ordinary initialization.

## 1. Exact complete-stage interface

At scale `m`, PR #3's frozen complete stage has

\[
z_{m+1}={3^{A_m}z_m+C_m(w_m)\over2^{D_m}},
\tag{1}
\]

\[
A_m={5369\over2}2^m+1792,
\qquad
D_m={1085579\over256}2^m+2816.
\tag{2}
\]

Its canonical domain and output are

\[
z_m=R_m+2^{D_m}Y_m,
\qquad
z_{m+1}=S_m+3^{A_m}Y_m,
\tag{3}
\]

with

\[
0\le R_m<2^{D_m},
\qquad
0\le S_m<3^{A_m}.
\tag{4}
\]

`L-9701` supplies the cumulative initial cylinders and exact new residue blocks.

## 2. Future completion height kills every free signed quotient

`T-9703` compares the current odd multiplier with the **next** complete dyadic radix and proves

\[
{3^{A_m}\over2^{D_{m+1}}}<\frac14.
\tag{5}
\]

`L-9705` extends the quotient argument to every signed integer. The quotient must eventually be `Y_m=0` or `Y_m=-1`.

The first is the cap stitch

\[
S_m=R_{m+1};
\tag{6}
\]

the second is the co-cap stitch

\[
3^{A_m}-S_m
 =2^{D_{m+1}}-R_{m+1}.
\tag{7}
\]

So negative ordinary integers do not form an unexamined exception.

## 3. Cap and co-cap heights collapse

`L-9703` proves

\[
|\beta_m|<256\Lambda_m,
\qquad
\Lambda_m={3^{A_m}\over2^{D_m}}>257.
\tag{8}
\]

`T-9704` gives, on a cap chain,

\[
\limsup {\log_2(R_m+257)\over D_m}
 \le {161341\over44508739}<\frac1{275}.
\tag{9}
\]

The same shifted recurrence applied to the positive co-cap correction `2^(D_m)-R_m` gives exactly the same bound.

## 4. Connector-free physical coordinate

At stabilized scales, the four finite tower cores are

\[
p=(5,30,20,56),
\qquad
b=(9,54,36,24).
\tag{10}
\]

`L-9704` defines

\[
Z_j=X_j+64\,2^{11(t_{j+1}+1)}z_j
\tag{11}
\]

and proves the connector-free recurrence

\[
2^{11(t_{j+1}+1)}Z_{j+1}
 =3^{7(t_j+1)}Z_j+b_{i_j}.
\tag{12}
\]

The coordinate has the direct physical meaning

\[
64(n_j+34)=2^{11(t_j+1)}Z_j.
\tag{13}
\]

One complete stage becomes

\[
2^{E_m}Z_{m+1}
 =3^{A_m}Z_m
  +\sum_{j=0}^{255}b_{i_{m,j}}2^{U_{m,j}}3^{V_{m,j}},
\tag{14}
\]

where

\[
E_m={8459\over2}2^m+2816.
\tag{15}
\]

All 256 internal coordinates are `{2,3}`-units. On a co-cap chain, `Z_m<0`; writing `\widetilde Z_m=-Z_m` reverses `(14)` while preserving the same one-positive-rest-negative sign pattern.

## 5. Evertse admissibility is the closing theorem

For either signed tail, form the 258 integer coordinates consisting of the two endpoint terms in `(14)` and the 256 internal terms. Divide by their gcd.

- The primitive gcd is at most `2^3*3^3=216`.
- Every internal coordinate has outside-`{2,3}` content one.
- The whole outside-prime product is at most `U_mU_(m+1)`, where `U` is the positive cap or co-cap endpoint.
- The endpoint estimates give
  \[
  \limsup {\log_2(U_mU_{m+1})\over E_m}
   \le {6498\over346819}<\frac1{50}.
  \tag{16}
  \]
- One coordinate has size at least `2^(E_m)/216`.
- Exactly one coordinate is positive, so no proper nonempty subsum vanishes.
- A projective ratio containing `2^(E_m)` has strictly increasing `2`-adic valuation, so the projective points are pairwise distinct.

`L-9706` checks these are nondegenerate `(1,1/50,{2,3})`-admissible projective zero sums in the sense of Evertse's 1984 Corollary 1. That theorem permits only finitely many. The infinitely many stage tuples give the contradiction in `T-9705`.

The external theorem is used with its exact primitive, nondegeneracy, and `0<=d<1` hypotheses. The later fixed-rank Evertse--Schlickewei--Schmidt theorem is not needed.

## 6. Claims

See `CLAIM_INVENTORY.md`. The closing chain is:

```text
L-9701
 -> T-9703
 -> L-9703/T-9704
 -> L-9704
 -> L-9705
 -> L-9706
 -> T-9705.
```

## 7. Verification

Run `X-9701` through `X-9704` from the repository root. Every experiment has a separately written checker.

`X-9704` freezes:

```text
local coordinate cases: 256
physical cofactor cases: 256
adjacent gcd cases: 256
prime turnover cases: 256
stable dictionary rows: 256
signed quotient integral cases: 4704
primitive gcd cap: 216
endpoint product ratio: 6498/346819 < 1/50
payload digest:
f3a4fd8a6f5074c488bd1a0d46a420a3f6f4425aaf30bef8245d5512a995a858
all independent connector-free checks passed
```

Finite checks validate arithmetic interfaces only. Evertse's theorem and the infinite contradiction are mathematical proof steps.

## 8. Scope and repository hygiene

This is not a proof of the Collatz conjecture. It excludes one exact proposed supercritical counterexample architecture.

The packet does not edit `CURRENT_STATE.md`, `CLAIMS.md`, `OPEN_PROBLEMS.md`, `CANDIDATES.md`, `NEGATIVE_RESULTS.md`, `NOTATION.md`, or any competing root ledger. No `K-####` candidate is proposed.
