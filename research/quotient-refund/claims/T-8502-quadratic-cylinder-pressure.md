# T-8502 — Linear refund has quadratic cylinder demand and a zero-dimensional completion set

**Claim ID:** `T-8502`  
**Status:** `PROPOSED`  
**Dependencies:** `D-8501`; elementary odd-affine cylinder algebra  
**Scope:** all type directives of the local linear connector system

## Statement

Fix an initial height `t_0`, initial edge `(i_0,i_1)`, and consider the first `N` residual transitions of `D-8501`. A choice of the next `N` types

\[
i_2,\ldots,i_{N+1}
\]

selects at most one initial residual cylinder modulo

\[
2^{D_N},
\]

where

\[
\boxed{
D_N
=
\sum_{n=0}^{N-1}11(t_0+16n+33)
=
88N^2+(11t_0+275)N.
}
\tag{1}
\]

There are at most

\[
4^N=2^{2N}
\]

such cylinders. Consequently the set `C_(t0,i0,i1)` of all `2`-adic initial residuals admitting some infinite type continuation satisfies

\[
\boxed{
\mu_{\rm Haar}(C_{t_0,i_0,i_1})=0,
\qquad
\dim_H(C_{t_0,i_0,i_1})=0.
}
\tag{2}
\]

More explicitly, its depth-`N` cover has total Haar mass at most

\[
\boxed{
2^{2N-D_N}.
}
\tag{3}
\]

## Proof

Each residual step has the odd-affine form

\[
Q_nz_{n+1}=N_nz_n+C_n,
\]

where `Q_n` is the displayed power of two in (1) and `N_n` is odd. Composing a fixed finite directive gives

\[
Q^{(N)}z_N=P^{(N)}z_0+F_N,
\]

with

\[
Q^{(N)}=\prod_{n<N}Q_n=2^{D_N}
\]

and `P^(N)` odd. Hence exactly one residue `z_0 mod 2^(D_N)` satisfies all `N` divisibility conditions. There are only `4^N` choices of the next types, proving the cylinder count and (3).

For any real `s>0`, the `s`-dimensional content of this cover is at most

\[
4^N(2^{-D_N})^s
=2^{2N-sD_N}.
\]

Because `D_N=88N^2+O(N)`, this tends to zero for every `s>0`. Therefore the Hausdorff dimension is zero. Taking `s=1` gives Haar measure zero. ∎

## Interpretation

Quotient refund supplies archimedean growth but does not supply symbolic abundance. The directive contributes only `2N` choice bits while exact ordinary continuation demands `88N^2+O(N)` dyadic bits. A positive witness must therefore use the growing ordinary quotient itself as the information carrier. Entropy surplus or finite-prefix abundance cannot substitute for the integer-first invariant of `T-8501`.

Zero dimension is not emptiness. This theorem does not exclude an isolated ordinary positive residual.
