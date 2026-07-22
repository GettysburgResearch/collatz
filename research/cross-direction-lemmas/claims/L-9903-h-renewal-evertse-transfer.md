# L-9903 -- H renewal Evertse transfer and exact endpoint-height escape

Claim ID: `L-9903`
Title: Every H renewal star and bridge gives a primitive nondegenerate four-term zero sum, but a survivor forces linear endpoint outside-prime mass
Status: `PROPOSED / SOURCE-QUALIFIED METHOD BOUNDARY`
Authoring agent: `gpt56-synthesis-01-wave22-h-sunit-transfer`
Reviewing agents: `gpt56-synthesis-01-wave22-completion-master`
Created: 2026-07-22
Last updated: 2026-07-22
Dependencies: PR #19 at `f764bdc2a2620f3a898ce46ab5ac80c27fe64439`, especially `L-9518`, `L-9520`, `T-9513`, `T-9514`, and `R-9504`; local `L-9889`, `L-9890`, `L-9894`, `L-9897`, `L-9900`, `L-9901`, `L-9902`, `T-9828`; PR #38 `ACL-N017` at `5ad965771869a647102e22115ed56749dbe2e254`; Evertse 1984 Corollary 1
Scope: positive nonperiodic exact H chains
Related counterexample candidates: none; no H survivor is constructed
Related atom: PR #38 `ACL-N017`

## Motivation

The H direction already proves fresh-prime pressure, but qualitative fresh
primes do not by themselves trigger Evertse's height theorem. The purpose of
this claim is to build the exact fixed-dimensional zero sums, audit every
Evertse hypothesis, and determine whether the remaining obstruction is
algebraic structure or endpoint size. The result isolates one quantitative
height deficit and rules out further fixed-width bookkeeping as the missing
step.

## Setup

Assume a positive nonperiodic infinite exact H chain. By `L-9889`, it has
infinitely many nonzero renewal times `t_k`. Put

\[
 R_k=r_{t_k},
 \qquad
 L_k=t_{k+1}-t_k,
 \qquad
 U_k=u_{t_k}.
\tag{1}
\]

The bridge cores `W_k congruent 5 (mod 6)` satisfy

\[
 9^{R_k}U_k-1=4^{L_k}W_k,
 \qquad
 8^{R_{k+1}}U_{k+1}-1=3^{L_k}W_k.
\tag{2}
\]

At an interior renewal `k>=1`, abbreviate

\[
 a=L_{k-1},
 \quad b=L_k,
 \quad R=R_k,
 \quad U=U_k,
 \quad X=W_{k-1},
 \quad Y=W_k.
\tag{3}
\]

Then

\[
 3^aX+1=8^RU,
 \qquad
 4^bY+1=9^RU.
\tag{4}
\]

All `U,X,Y` are positive and coprime to six.

## Theorem 1 -- central-star transfer

Define

\[
 \mathbf C_k=
 \left(
 -8^R4^bY,
 \;9^R3^aX,
 \;9^R,
 \;-8^R
 \right).
\tag{5}
\]

Then:

1. `sum_i C_(k,i)=0`;
2. `C_k` is primitive;
3. it has no nonempty proper vanishing subsum;
4. its primitive height is exactly

   \[
    H_k=8^R4^bY=72^RU-8^R;
   \tag{6}
   \]

5. with `S_0={2,3}`,

   \[
    \prod_i\operatorname{out}_{S_0}(C_{k,i})=XY;
   \tag{7}
   \]

6. distinct interior renewals on a nonperiodic chain give distinct projective
   points.

Consequently, for every fixed `c>0` and `0<d<1`, only finitely many `k` can
satisfy

\[
 XY\le cH_k^d.
\tag{8}
\]

Equivalently, on any hypothetical survivor,

\[
 \boxed{{XY\over H_k^d}\longrightarrow\infty}
 \qquad(0<d<1).
\tag{9}
\]

### Proof

Equation (4) gives

\[
 8^R4^bY-9^R3^aX=9^R-8^R,
\tag{10}
\]

which proves the zero sum. The last two coordinates have gcd one, so the
whole tuple is primitive.

There are two positive and two negative coordinates. A proper zero subsum
must therefore be a cross-sign pair: a three-term zero sum would force the
omitted singleton to vanish. The four possible pairs are excluded by,
respectively:

- incompatible 2-adic valuations of `8^R4^bY` and `9^R3^aX`;
- incompatible 2-adic valuations of `8^R4^bY` and `9^R`;
- incompatible 3-adic valuations of `9^R3^aX` and `8^R`; and
- `9^R ne 8^R`.

Moreover,

\[
 8^R4^bY=72^RU-8^R,
 \qquad
 9^R3^aX=72^RU-9^R,
\tag{11}
\]

so the first magnitude is the largest. Removing 2- and 3-parts leaves
exactly `Y,X,1,1`, proving (7).

The coordinates `9^R,-8^R` recover `R`; the valuations of the first two
recover `b,a`; their values recover `Y,X`; and (4) recovers `U`. Repetition
would therefore repeat a deterministic renewal state and make the H chain
periodic. Primitive projective equality permits only equality up to a global
sign; the fixed ordered sign pattern in (5) rules out the negative
representative. Hence projective repetition is coordinate repetition.
Evertse's Corollary 1, equivalently `L-9901` with
`gamma=0`, now proves (8)--(9). **QED**

## Theorem 2 -- full-bridge transfer

For one bridge `k>=0`, put

\[
 R=R_k,
 \quad S=R_{k+1},
 \quad L=L_k,
 \quad U=U_k,
 \quad V=U_{k+1},
 \quad W=W_k,
\tag{12}
\]

and define

\[
 \mathbf B_k=
 \left(
 4^L8^SV,
 \;-4^L,
 \;-3^L9^RU,
 \;3^L
 \right).
\tag{13}
\]

Then `B_k` is another primitive, nondegenerate four-coordinate zero sum, with
exact height

\[
 J_k=4^L8^SV=4^L+12^LW
\tag{14}
\]

and outside-`{2,3}` product

\[
 \prod_i\operatorname{out}_{S_0}(B_{k,i})=UV.
\tag{15}
\]

Thus, for every fixed `c>0` and `0<d<1`, only finitely many `k` satisfy
`UV<=cJ_k^d`, and on any hypothetical nonperiodic survivor,

\[
 \boxed{{UV\over J_k^d}\longrightarrow\infty.}
\tag{16}
\]

### Proof

Eliminating `W` from (2) gives

\[
 4^L8^SV-4^L-3^L9^RU+3^L=0.
\tag{17}
\]

Primitivity follows from the coordinates `4^L` and `3^L`. A proper zero
subsum again reduces to a cross-sign pair, and the four possibilities are
excluded by

\[
 8^SV\ne1,
 \qquad
 v_2(4^L8^SV)>0=v_2(3^L9^RU),
\tag{18}
\]

\[
 4^L\ne3^L,
 \qquad
 9^RU\ne1.
\tag{19}
\]

The two large coordinates are

\[
 4^L+12^LW,
 \qquad
 3^L+12^LW,
\tag{20}
\]

so the first is the height. The tuple recovers `L,S,V,R,U` from its values
and exact 2- and 3-adic valuations. Repetition would repeat a deterministic
bridge state. Primitive projective equality again permits a global sign only,
and the fixed ordered sign pattern in (13) rules out its negative, proving
distinctness. Removing 2- and 3-parts gives (15), and
Evertse gives (16). **QED**

## Exact failed hypothesis

The endpoint products factor as

\[
 \boxed{
 {XY\over H_k}
 ={U\over3^a4^b}
 \left(1-{1\over8^RU}\right)}
\tag{21}
\]

and

\[
 \boxed{
 {UV\over J_k}
 ={W\over9^R8^S}
 \left(1+{1\over4^LW}\right).}
\tag{22}
\]

The correction factors lie in `[7/8,1)` and `(1,21/20]`, respectively.
Hence these canonical tuples obtain an Evertse exponent `d<1` on an infinite
subsequence precisely when one obtains, with fixed constants on that
subsequence, a proportional logarithmic deficit such as

\[
 \log U
 \le a\log3+b\log4-\eta\log H_k+O(1)
\tag{23}
\]

or

\[
 \log W
 \le R\log9+S\log8-\eta\log J_k+O(1)
\tag{24}
\]

for some `eta>0` along an infinite subsequence.

Conversely, any surviving chain must obey

\[
 \boxed{
 \liminf_k
 {\log U_k-L_{k-1}\log3-L_k\log4
  \over\log H_k}\ge0}
\tag{25}
\]

and

\[
 \boxed{
 \liminf_k
 {\log W_k-R_k\log9-R_{k+1}\log8
  \over\log J_k}\ge0.}
\tag{26}
\]

The distinct fixed-dimensional integer tuples also force
`H_k,J_k->infinity`, so every logarithmic quotient above is taken along a
divergent height sequence. Thus the H architecture retains essentially one
full projective height in its
moving odd endpoints. This is exactly what the corrected collision
architecture lacks: `T-9828` has bounded gcd and endpoint exponent at most

\[
 {6498\over346819}<{1\over50},
\tag{27}
\]

whereas an H survivor forces lower endpoint exponent one.

## Bounded-letter branch: an unconditional gate failure

If the bounded-letter alternative of `T-9514` has
`R_k,R_(k+1)<=M_0`, then `W_k>=5` and

\[
 \begin{aligned}
 UV
 &=J_k{U\over4^L8^S}\\
 &>J_k{W\over9^R8^S}\\
 &\ge5\cdot72^{-M_0}J_k.
 \end{aligned}
\tag{28}
\]

Since distinct bridge tuples have `J_k->infinity`, no fixed `d<1` gate can
hold even algebraically on this canonical bridge family. The bounded-letter
branch is not a hidden specialization of the collision closure.

## Adversarial tests -- sharp local counterfamilies

The obstruction is not caused by a weak estimate. For fixed
`R=3,a=2,b=1`, let

\[
 U_m=197+216m,
 \quad
 X_m=11207+12288m,
 \quad
 Y_m=35903+39366m.
\tag{29}
\]

Then

\[
 3^2X_m+1=8^3U_m,
 \qquad
 4Y_m+1=9^3U_m
\tag{30}
\]

for every `m>=0`. The central height is linear in `m`, while `X_mY_m` is
quadratic, so

\[
 {\log(X_mY_m)\over\log H_m}\longrightarrow2.
\tag{31}
\]

Likewise, the exact local bridge family

\[
 W_m=239+864m,
 \quad
 U_m=425+1536m,
 \quad
 V_m=269+972m
\tag{32}
\]

satisfies

\[
 9U_m-1=16W_m,
 \qquad
 8V_m-1=9W_m.
\tag{33}
\]

Here `R=S=1,L=2`, `J_m=128V_m`, and

\[
 {\log(U_mV_m)\over\log J_m}\longrightarrow2.
\tag{34}
\]

These are isolated exact local stars and segments, not globally compatible
orbits. Nevertheless, after assigning the `m`-th sample a linearly growing
formal time, all variables have logarithm `O(log(m+2))=o(rho^m)` for every fixed
`rho>1`, and the exponentially discounted scalar sums converge. Therefore
those listed scalar
subcritical and discounted numerical bounds alone cannot imply (23) or (24).
This does not refute the full globally compatible PR #19 pressure package.

## Hypothesis audit

| Evertse requirement | Central star | Full bridge |
|---|---:|---:|
| Fixed dimension | passes: 4 | passes: 4 |
| Fixed internal support | passes: `{2,3}` | passes: `{2,3}` |
| Nondegeneracy | passes | passes |
| Primitive normalization | passes: gcd 1 | passes: gcd 1 |
| Height divergence | passes | passes |
| Projective distinctness | passes | passes |
| Outside-`S` exponent `<1` | **sole missing Evertse hypothesis** | **sole missing Evertse hypothesis** |

Unrolling increasingly many renewals does not repair the failure: the
coordinate count then grows, and `L-9902` shows that Evertse or ESS finiteness
cannot be summed across changing dimensions without overfilling one fixed
term-count bin.

The strongest valid conclusion is:

> The H-to-Evertse conversion is structurally complete, but not
> admissibility-complete. Any positive nonperiodic H survivor must escape
> through asymptotically linear-or-larger endpoint outside-`{2,3}` content. A
> closing theorem must establish a fixed relative deficit in (23) or (24), or
> use genuinely new global compatibility information; qualitative
> fresh-prime divergence and orbit-time subcriticality do not supply it.

## Dependency and gap audit

- The two zero sums are exact consequences of the renewal bridge equations.
- Evertse is invoked only after primitive normalization, nondegeneracy,
  fixed dimension, fixed support, and projective distinctness are proved.
- The theorem isolates the missing outside-prime height gate; it does not
  prove that gate.
- The local counterfamilies satisfy one star or bridge but need not concatenate
  to an H orbit.
- No H survivor, Collatz counterexample, or proof of Collatz is claimed.

## Remaining uncertainty

The four-term transfer and its Evertse consequence are exact. What remains
unknown is whether global compatibility of successive H renewals forces a
fixed deficit in (23) or (24), or instead permits the exponent-one escape
identified here. The isolated affine families do not decide that global
question.

## Suggested next attack

Combine the successive-core identity of `L-9894` with (21)--(22) over two or
more adjacent bridges. A successful argument should control the joint odd
core after removing all reused prime powers and prove a uniform negative
proportion in either endpoint logarithm. Any unrolling must keep a bounded
essential term count or explicitly overfill one fixed term-count bin.
