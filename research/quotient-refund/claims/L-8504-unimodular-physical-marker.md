# L-8504 — Refund states are intrinsic unimodular physical markers

**Claim ID:** `L-8504`  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-cylinder-01`  
**Dependencies:** `L-8503`; branch-qualified phase-`-34` tower identity  
**Scope:** every linear-grid connector state at a height divisible by `16`

## Unimodular complement basis

At source height `t`, use

\[
N=3^{7(t+1)},\qquad M=2^{11(t+17)},
\]

and the inverse/complement data

\[
Nr=1+Mc,\qquad d=M-r,\qquad e=N-c.
\]

Then

\[
\boxed{Me-Nd=1.}
\tag{1}
\]

Consequently

\[
\boxed{
A_t=
\begin{pmatrix}
M&d\\
N&e
\end{pmatrix}
\in \operatorname{SL}_2(\mathbf Z).}
\tag{2}
\]

For a type `i` and complement counter `k`, `L-8503` becomes

\[
\boxed{
\binom{W}{U}
=A_t\binom{k}{b_i},
\qquad
W=Mk+b_id,
\qquad
U=Nk+b_ie.}
\tag{3}
\]

The coordinates are recovered intrinsically from two consecutive boundary words:

\[
\boxed{k=eW-dU,}
\tag{4}
\]

\[
\boxed{b_i=MU-NW.}
\tag{5}
\]

There is therefore no hidden connector carry once the two ordinary physical boundary words are known.

## Farey cone

The two rational slopes bounding the positive cone are neighboring fractions:

\[
\boxed{\frac ed-\frac NM=\frac1{Md}.}
\tag{6}
\]

For `k>0` and `b_i>0`,

\[
\boxed{
\frac NM<\frac UW<\frac ed,}
\tag{7}
\]

and the exact lower-edge error is

\[
\boxed{
\frac UW-\frac NM=\frac{b_i}{MW}.}
\tag{8}
\]

Thus every refunded connector is one positive lattice point in a width-`1/(Md)` unimodular Farey cone. Equation `(4)` is its ordinary distance coordinate along the cone.

## Intrinsic physical marker

The stabilized type table has

```text
p=(5,30,20,56),
b=(9,54,36,24),
v_2(p_i)=v_2(b_i)=i.
```

For `(t,i,k)` define

\[
W=b_i d+Mk
\]

and the physical boundary integer

\[
\boxed{
n=2^{11(t+1)}\frac W{64}-34.}
\tag{9}
\]

Because `W == p_i (mod 64)`,

\[
\boxed{
\nu_2(n+34)=11t+5+i.}
\tag{10}
\]

When `16|t`, this gives the intrinsic signature

\[
\boxed{
\nu_2(n+34)\equiv5+i\pmod{176}.}
\tag{11}
\]

Hence the height and type are recoverable from the ordinary physical integer: the only permitted valuation residues are `5,6,7,8 modulo 176`, the residue selects `i`, and then

\[
\boxed{t=\frac{\nu_2(n+34)-5-i}{11}.}
\tag{12}
\]

The remaining counter is recovered from the odd boundary word:

\[
\boxed{
k=\frac{W-b_i(M-r)}M.}
\tag{13}
\]

## Exact physical return

If `T-8504` maps `(t,i,k)` to `(t+16,j,k')`, put

\[
U=b_i e+Nk.
\]

Then the next boundary is

\[
\boxed{
n'=2^{11(t+17)}\frac U{64}-34.}
\tag{14}
\]

The phase-`-34` tower identity gives

\[
\boxed{n'=T^{11(t+1)}(n),}
\tag{15}
\]

with exactly `7(t+1)` odd shortcut steps. Its intrinsic valuation marker advances by

\[
\boxed{
\nu_2(n'+34)-\nu_2(n+34)=176+j-i.}
\tag{16}
\]

Thus the abstract one-counter map is conjugate to an ordinary return map detected entirely from the valuations and odd cores of `n+34`. No external mark, future type, or inverse-limit address is part of the state.

## Proof

Equation `(1)` follows immediately from

\[
M(N-c)-N(M-r)=Nr-Mc=1.
\]

This proves `(2)`. Equations `(3)` are `L-8503/(1)--(3)`. Multiplication by

\[
A_t^{-1}=\begin{pmatrix}e&-d\\-N&M\end{pmatrix}
\]

proves `(4)--(5)`. Equations `(6)--(8)` are determinant-one algebra.

For the physical marker, `W == p_i (mod 64)` and `v_2(p_i)=i<6`, so `v_2(W)=i`. Substitution in `(9)` proves `(10)--(13)`.

The phase-`-34` anchor identity is

\[
64(n+34)=2^{11(t+1)}W.
\]

After the exact tower block,

\[
64(n'+34)=NW+b_i=MU,
\]

which proves `(14)--(15)`. Applying the same valuation calculation at height `t+16` and type `j` proves `(16)`. ∎

## Constructive consequence

A counterexample certificate no longer needs to carry a separately trusted stage number or tower type. A verifier can begin with the single written integer `n_0`, recover `(t_0,i_0,k_0)` from `(10)--(13)`, and then replay `T-8504`. The sole remaining positive obligation is still all-time definedness.