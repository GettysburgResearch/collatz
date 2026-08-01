# L-6907 — every nonmechanical canonical failure is one exact dyadic wrap

**Claim ID:** `L-6907`  
**Status:** **PROPOSED**  
**Authoring agent:** `gpt56-positive-tangent-01` (`GPT-5.6 Pro`)  
**Created:** 2026-07-31  
**Issue:** #75  
**Dependencies:** `L-6904`, `L-6906`; elementary modular arithmetic  
**Scope:** comparison of one first-crossing word with the upper mechanical word at the same length

## Setup

Fix a valid first-crossing length `j`, its unique weight `q`, and put

\[
M=2^j,
\qquad
p=3^q,
\qquad
D=M-p>0.
\]

Let `u=w^mech` be the upper mechanical word, and let `v` be any other first-crossing word of the same length.

Write

\[
A_u,\ A_v
\]

for their affine numerators,

\[
r_u,\ r_v\in\{1,\ldots,M-1\}
\]

for their canonical positive parity-cylinder representatives, and

\[
x_u^*=\frac{A_u}{D},
\qquad
x_v^*=\frac{A_v}{D}.
\]

By `L-6906`,

\[
\Delta=A_u-A_v>0.
\tag{1}
\]

Let

\[
\delta=[\Delta p^{-1}]_M
\in\{1,\ldots,M-1\}
\tag{2}
\]

be the canonical residue modulo `M`.

## Exact residue comparison

One has

\[
\boxed{r_v\equiv r_u+\delta\pmod M.}
\tag{3}
\]

Hence exactly one of the following occurs:

### No wrap

\[
r_u+\delta<M,
\qquad
r_v=r_u+\delta>r_u.
\tag{4}
\]

### One wrap

\[
r_u+\delta>M,
\]

and, putting

\[
s=M-\delta,
\tag{5}
\]

one has

\[
\boxed{0<s<r_u,
\qquad
r_v=r_u-s.}
\tag{6}
\]

Equality `r_u+delta=M` cannot occur because it would give `r_v congruent 0 mod 2`, whereas every first-crossing word begins with an odd bit.

### Proof

The canonical congruences are

\[
pr_u+A_u\equiv0\pmod M,
\qquad
pr_v+A_v\equiv0\pmod M.
\]

Subtracting and multiplying by `p^{-1}` gives `(3)`. Since `r_u,delta` lie strictly between zero and `M`, their sum lies in `(0,2M)`, so only `(4)` or `(6)` is possible. ∎

## Failure requires the wrap case

Assume the mechanical word descends canonically:

\[
\boxed{r_u>x_u^*.}
\tag{7}
\]

Then every no-wrap word also descends:

\[
r_v>r_u>x_u^*>x_v^*.
\]

Therefore any nonmechanical failure

\[
r_v\le x_v^*
\tag{8}
\]

must lie in the one-wrap case `(6)`.

Moreover `(8)` is equivalent to

\[
\boxed{
s\ge(r_u-x_u^*)+\frac{\Delta}{D}.}
\tag{9}
\]

Thus the wrap must pay both the mechanical integer descent margin and the real threshold lost by moving odd bits left.

## Exact wrap equation

In the wrap case, `(2)` and `(5)` give

\[
\Delta+sp=hM
\tag{10}
\]

for one positive integer `h`.

If `(7)--(8)` hold, then `(9)` implies

\[
\Delta<sD,
\]

and therefore

\[
\boxed{1\le h<s.}
\tag{11}
\]

Because `h` and `s` are integers, one obtains the stronger finite inequality

\[
\boxed{sD\ge\Delta+M.}
\tag{12}
\]

The corresponding canonical endpoints satisfy

\[
T_v^j(r_v)=T_u^j(r_u)-h.
\tag{13}
\]

Thus a failed word is obtained from the mechanical canonical segment by lowering its start by `s` and its endpoint by the strictly smaller integer `h`.

## First-difference valuation

Let `a` be the first position at which `v` differs from `u`, indexed from zero. Proper-prefix dominance forces

\[
v_a=1,
\qquad
u_a=0.
\]

Then

\[
\boxed{\nu_2(\Delta)=a.}
\tag{14}
\]

Since multiplication by the odd unit `p^{-1}` preserves 2-adic order modulo `2^j`, equations `(2)` and `(5)` give

\[
\boxed{\nu_2(\delta)=\nu_2(s)=a.}
\tag{15}
\]

### Proof

The words agree before `a`. In the affine numerator formula, all contributions before `a` cancel. At position `a`, `v` has one odd contribution and `u` has none; every later contribution is divisible by `2^(a+1)`. Hence

\[
\Delta\equiv-2^a\cdot(\text{odd})\pmod{2^{a+1}},
\]

proving `(14)`. The remaining assertions follow because `p` is odd and `M` is divisible by `2^(a+1)`. ∎

## Immediate consequences

Any nonmechanical canonical failure, after mechanical descent is known, must satisfy simultaneously

\[
\boxed{
\begin{aligned}
&r_v=r_u-s,\qquad 0<s<r_u,\\
&\Delta+sp=h2^j,\qquad 1\le h<s,\\
&sD\ge\Delta+2^j,\\
&\nu_2(s)=\nu_2(\Delta)=a,
\end{aligned}}
\tag{16}
\]

where `a` is the first departure from the mechanical word.

In particular,

\[
2^a\le s<r_u,
\]

so no failure can first depart at a position

\[
a\ge\lceil\log_2 r_u\rceil.
\tag{17}
\]

## Strategic meaning

Real extremality alone does not order the canonical residues because reduction modulo `2^j` can wrap. `L-6907` proves that this is the **only** obstruction and gives its exact arithmetic signature.

The surviving Box-2 task splits cleanly:

1. prove canonical descent for the single mechanical word;
2. exclude integer solutions of the one-wrap system `(16)` for every nonmechanical word.

This is a corrected finite-place interface. It does not rely on an assumed monotonicity of canonical residues under adjacent swaps.

## Gap audit

- The lemma does not prove that the mechanical word descends at every length.
- The one-wrap system may still have solutions; `(16)` is a necessary condition, not an exclusion.
- The first-difference bound can be weak when `r_u` is exponentially large.
- No claim from the superseded colliding PR #82 is imported.
