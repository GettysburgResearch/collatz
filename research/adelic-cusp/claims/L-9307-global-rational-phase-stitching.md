# L-9307 — Global rational diagonal and bilateral phase stitching

**Claim ID:** L-9307  
**Title:** The dyadic survivor product, triadic mirror product, and every CRT split use one contiguous reciprocal phase chain  
**Status:** PROPOSED  
**Authoring agent:** `gpt56-pro-04`  
**Reviewing agents:** none  
**Created:** 2026-07-21  
**Last updated:** 2026-07-21  
**Dependencies:** `L-9301`, `L-9305`, `T-9304`; elementary CRT and character reciprocity  
**Scope:** exact phase-level identification for the one-place and two-place EQ Fourier products  
**Related counterexample candidates:** none

## Statement

### 1. Universal circle reciprocity

Let `M,N >= 1` be coprime, let `a` be an integer, and let

\[
z\in\{0,1,\ldots,M-1\},
\qquad
q\in\{0,1,\ldots,N-1\}
\]

be the residues determined by

\[
Nz\equiv a\pmod M,
\qquad
Mq\equiv-a\pmod N.
\tag{1}
\]

Then

\[
\boxed{
\frac zM
\equiv
\frac qN+rac a{MN}
\pmod 1.
}
\tag{2}
\]

No size hypothesis on `a` is required.

### 2. One reciprocal phase chain

Fix `K >= 1` and an integer `h`. For

\[
0\le \ell<K,
\]

put

\[
M_\ell=64^{K-\ell},
\qquad
N_\ell=81^{\ell+1},
\tag{3}
\]

and define

\[
q_\ell(h)
\equiv
-17h\,M_\ell^{-1}
\pmod{N_\ell},
\qquad
0\le q_\ell(h)<N_\ell.
\tag{4}
\]

Write

\[
x_\ell(h)=\frac{q_\ell(h)}{N_\ell},
\qquad
\delta_\ell(h)=
\frac{17h}{M_\ell N_\ell}.
\tag{5}
\]

Let

\[
C(x)=|\cos(\pi x)|,
\]

viewed as a `1`-periodic function.

Define the dyadic survivor magnitude

\[
F^{(2)}_K(h)
=
\left|
\widehat\mu\!\left(\frac h{64^K}\right)
\right|
=
\frac{|S_K(h)|}{2^K},
\tag{6}
\]

and the triadic mirror magnitude

\[
F^{(3)}_K(h)
=
\left|
\widehat\nu\!\left(\frac h{81^K}\right)
\right|
=
\frac{|\widehat C_K(h)|}{2^K}.
\tag{7}
\]

Then the two products have the exact common indexing

\[
\boxed{
F^{(2)}_K(h)
=
\prod_{\ell=0}^{K-1}
C\bigl(x_\ell(h)+\delta_\ell(h)\bigr),
}
\tag{8}
\]

and

\[
\boxed{
F^{(3)}_K(h)
=
\prod_{\ell=0}^{K-1}
C\bigl(x_\ell(h)\bigr).
}
\tag{9}
\]

Thus the dyadic and triadic products differ only by the explicit circle shifts `delta_ell(h)` on the same reciprocal phase chain.

### 3. Every CRT split stitches the same chain

Let

\[
K=n+j,
\qquad
n,j\ge1,
\qquad
Q_{n,j}=64^n81^j.
\tag{10}
\]

Let

\[
u_{n,j}\equiv(81^j)^{-1}\pmod{64^n},
\qquad
v_{n,j}\equiv(64^n)^{-1}\pmod{81^j},
\tag{11}
\]

and let `G_(n,j)(h)` be the normalized CRT-product coefficient from `T-9304`.

The two local characters in `T-9304` are the local components of the **same global rational character**:

\[
\boxed{
\frac{hu_{n,j}}{64^n}
\equiv
\frac h{Q_{n,j}}
\pmod{\mathbb Z_2},
}
\tag{12}
\]

and

\[
\boxed{
\frac{hv_{n,j}}{81^j}
\equiv
\frac h{Q_{n,j}}
\pmod{\mathbb Z_3}.
}
\tag{13}
\]

Moreover, its absolute Fourier coefficient is obtained by cutting the chain `(4)` at `ell=j`:

\[
\boxed{
|G_{n,j}(h)|
=
\left[
\prod_{\ell=0}^{j-1}C\bigl(x_\ell(h)\bigr)
\right]
\left[
\prod_{\ell=j}^{K-1}
C\bigl(x_\ell(h)+\delta_\ell(h)\bigr)
\right].
}
\tag{14}
\]

The first `j` factors are supplied exactly by the triadic mirror; the final `n` factors are supplied by the dyadic survivor side through circle reciprocity. Changing the split changes only the location at which the explicit shifts begin. It does not create a second unrelated phase process.

## Definitions

The inverses in `(4)` are taken modulo `N_ell`. Equation `(4)` is the same reciprocal residue that appears in `L-9304`, but here its denominator includes the full triadic depth belonging to the relevant global rational character.

The phrase *global rational diagonal* means that the pair of local character classes in `(12)` and `(13)` is the image of one rational number

\[
r=\frac h{64^n81^j}
\]

in

\[
\mathbb Q_2/\mathbb Z_2
\times
\mathbb Q_3/\mathbb Z_3.
\]

The phrase *bilateral phase stitching* refers to the fact that the triadic factor supplies the low indices of one reciprocal chain and the dyadic factor supplies the high indices.

## Motivation

`T-9304` stationarized the CRT comparison transform as a product of one fixed `Z_2` transform and one fixed `Z_3` transform. It remained possible that the product offered genuinely independent spectral loss unavailable in the original one-place EQ product.

The present lemma shows that this is not the phase geometry. On the room-relevant rational diagonal, the two local factors are adjacent portions of one chain

\[
q_\ell(h)
\equiv
-17h\,64^{\ell-K}
\pmod{81^{\ell+1}}.
\]

The two-place formulation remains conceptually useful, especially for transfer operators and solenoid dynamics, but it does not automatically supply two independent sources of Fourier decay.

## Proof

### Universal circle reciprocity

From `(1)`, the integer

\[
Nz-a-Mq
\]

is divisible by `M`. It is also divisible by `N`, because

\[
Mq\equiv-a\pmod N.
\]

Since `gcd(M,N)=1`, there is an integer `r` such that

\[
Nz-a-Mq=rMN.
\]

Dividing by `MN` gives

\[
\frac zM-rac qN-rac a{MN}=r,
\]

which is `(2)`.

### Dyadic product

By `L-9301`, the `ell`-th absolute factor of `F^(2)_K(h)` is

\[
C\!\left(
\frac{z_\ell(h)}{M_\ell}
\right),
\]

where

\[
N_\ell z_\ell(h)
\equiv17h
\pmod{M_\ell}.
\]

Apply `(2)` with

\[
M=M_\ell,
\qquad
N=N_\ell,
\qquad
a=17h.
\]

The reciprocal residue is exactly `q_ell(h)`, so

\[
\frac{z_\ell(h)}{M_\ell}
\equiv
x_\ell(h)+\delta_\ell(h)
\pmod1.
\]

Since `C` is `1`-periodic, multiplying the factors proves `(8)`.

### Triadic product

By `L-9305`,

\[
F^{(3)}_K(h)
=
\prod_{i=1}^{K}
C\!\left(
-
\frac{17\,64^{-i}h}{81^{K-i+1}}
\right).
\]

Set

\[
\ell=K-i.
\]

Then

\[
81^{K-i+1}=81^{\ell+1}=N_\ell,
\qquad
64^{-i}=64^{-(K-\ell)}=M_\ell^{-1}\pmod{N_\ell}.
\]

The phase is therefore `x_ell(h)` up to sign and an integer. The function `C` is even and `1`-periodic, proving `(9)`.

### Global rational diagonal

Because

\[
81^j u_{n,j}-1
\]

is divisible by `64^n`,

\[
\frac{hu_{n,j}}{64^n}
-
\frac h{64^n81^j}
=
\frac{h(81^ju_{n,j}-1)}{64^n81^j}
\in\mathbb Z_2.
\]

This proves `(12)`. The proof of `(13)` is identical with `2` and `3` interchanged.

### Stitched product

Use the global character

\[
r=\frac h{Q_{n,j}}.
\]

For the triadic factor, the digit index `s`, with `0<=s<j`, contributes

\[
rc\lambda^s
=
-
\frac{17h}{64^{n+s+1}81^{j-s}}.
\]

Set

\[
\ell=j-s-1.
\]

Then

\[
64^{n+s+1}=64^{K-\ell}=M_\ell,
\qquad
81^{j-s}=81^{\ell+1}=N_\ell.
\]

Hence these are exactly the unshifted factors `C(x_ell(h))` for

\[
0\le\ell<j.
\]

For the dyadic factor, the digit index `t`, with `0<=t<n`, contributes

\[
rd\rho^t
=
rac{17h}{64^{n-t}81^{j+t+1}}.
\]

Set

\[
\ell=j+t.
\]

Again

\[
64^{n-t}=64^{K-\ell}=M_\ell,
\qquad
81^{j+t+1}=81^{\ell+1}=N_\ell.
\]

Applying circle reciprocity gives the shifted factors

\[
C\bigl(x_\ell(h)+\delta_\ell(h)\bigr)
\]

for

\[
j\le\ell<K.
\]

Combining the two ranges proves `(14)`. QED.

## Dependency audit

- `L-9301` supplies the fixed dyadic survivor product.
- `L-9305` supplies the fixed triadic mirror product.
- `T-9304` supplies the exact CRT product coefficient.
- The new content is the common global rational character and the exact reindexing of all factors into one reciprocal chain.
- No branch-qualified room-position theorem is used.
- No computation, external Fourier-decay theorem, or probabilistic independence assertion is used.

## Gap audit

- A shared phase chain does not prove that the chain has enough energy.
- The lemma concerns absolute Fourier factors. Complex coefficients also have explicit phases, but they are not needed for the discrepancy consequences developed in `T-9305`.
- The two-place viewpoint may still enable a new proof through dynamics or transfer operators even though the target is not weaker.
- The global rational diagonal is a very thin subset of the full product dual group; full-group moment factorization does not control it.
- Word-order conventions affect pathwise identifications but not the complete binary product or the absolute formulas above.

## Adversarial tests

1. At `h=0`, every factor equals `1`.
2. At `K=1`, the chain has one phase and `(8)`--`(9)` reduce to the elementary `64`/`81` reciprocity identity.
3. At the endpoint split `j=0` the stitched formula becomes the dyadic product; at `n=0` it becomes the triadic product. These endpoints can be included by declaring the corresponding empty product to be `1`.
4. Multiplying `h` by a power of `64` removes dyadic factors through the exact self-similarity of `L-9301`; the reciprocal chain records the same removal through trivial shifted phases.
5. Multiplying `h` by a power of `81` removes initial reciprocal levels as in `L-9304`; both the triadic and stitched products record the same valuation loss.

## Remaining uncertainty

The argument is complete-looking. Independent review should check the sign convention in the two local additive characters and the indexing at the split boundary `ell=j`. Absolute values are insensitive to simultaneous conjugation, but the indexing must still be exact.

## Suggested next attack

Use the `pi`-Lipschitz property of `C(x)` to compare all stitched products quantitatively. The geometric sum of the explicit shifts can be evaluated exactly, producing split-independent weighted discrepancy equivalence in `T-9305`.