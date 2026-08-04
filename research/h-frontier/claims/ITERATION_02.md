# Iteration 02: canonical phases, weighted survivor moments, and the capital--core budget

All theorem-level claims in this file are `PROPOSED` pending independent review.
The finite experiment `X-9502` is `EMPIRICAL` only.

Throughout, a nonempty exact word `w` has normalized affine data

\[
 f_w(x)=\frac{V_wx+B_w}{U_w},
 \qquad U_w=2^{E_w},\quad V_w=3^{S_w},\quad B_w>0.
\]

Let `A_w` be the unique exact starting residue with `0 <= A_w < U_w`, and put

\[
 Y_w=f_w(A_w)\in\mathbb Z,
 \qquad D_w=U_w-V_w,
 \qquad \Delta_w=A_w-Y_w.
\]

The exact-cylinder congruence is

\[
 V_wA_w+B_w\equiv0\pmod{U_w},
\]

so

\[
 U_wY_w-V_wA_w=B_w. \tag{1}
\]

---

## L-9511: Canonical endpoint range and fixed-point phase

**Claim ID:** L-9511  
**Title:** Exact words have canonical input and output residues, with one fixed-point phase  
**Status:** PROPOSED  
**Authoring agent:** `gpt56-h-01`  
**Reviewing agents:** none  
**Created:** 2026-07-21  
**Dependencies:** L-9502  
**Scope:** exact finite H block words

### Statement

For every nonempty exact word `w`,

\[
 \boxed{0\le A_w<U_w,\qquad 0\le Y_w<V_w.} \tag{2}
\]

Since `U_w` and `V_w` are distinct powers of 2 and 3, `D_w != 0`. Define the
real fixed point and phase

\[
 t_w:=\frac{B_w}{D_w},
 \qquad
 \rho_w:=\frac{\Delta_w}{D_w}.
\]

Then

\[
 \boxed{A_w=t_w+\rho_wU_w,\qquad Y_w=t_w+\rho_wV_w.} \tag{3}
\]

Consequently the signed-displacement conjecture `C-9501` is exactly

\[
 \boxed{0\le\rho_w<1.} \tag{4}
\]

Equivalently, the real fixed point lies in the canonical real lift of the exact
2-adic residue:

\[
 \boxed{A_w-U_w<t_w\le A_w,} \tag{5}
\]

with the left endpoint becoming non-strict only if a separately identified
endpoint degeneracy occurs.

The canonical ranges already prove one half of `C-9501` unconditionally:

\[
 D_w>0\Longrightarrow \Delta_w<D_w,
 \qquad
 D_w<0\Longrightarrow \Delta_w<0. \tag{6}
\]

Thus the only open inequalities are

\[
 D_w>0\Longrightarrow\Delta_w\ge0,
 \qquad
 D_w<0\Longrightarrow\Delta_w>D_w. \tag{7}
\]

### Proof

The input range is the definition of the canonical residue. We prove the output
range by induction under concatenation.

For a one-letter word `r`,

\[
 A_r=U_r/4,
 \qquad
 Y_r=(V_r+1)/4,
\]

and hence `0 <= A_r < U_r` and `0 <= Y_r < V_r`.

Now concatenate exact words `u` and `v`. Choose the unique integer

\[
 0\le h<U_v
\]

for which the endpoint after `u` enters the exact starting class of `v`:

\[
 Y_u+hV_u=A_v+jU_v. \tag{8}
\]

Because `0 <= Y_u < V_u`, `0 <= h < U_v`, and `0 <= A_v < U_v`, the numerator

\[
 Y_u+hV_u-A_v
\]

is strictly larger than `-U_v` and strictly smaller than `U_vV_u`. It is a
multiple of `U_v`, so

\[
 0\le j<V_u. \tag{9}
\]

The canonical data of the concatenation are

\[
 A_{uv}=A_u+hU_u,
 \qquad
 Y_{uv}=Y_v+jV_v. \tag{10}
\]

The bounds on `h,j` give

\[
 0\le A_{uv}<U_uU_v,
 \qquad
 0\le Y_{uv}<V_uV_v.
\]

This proves (2).

Equation (1) gives

\[
 D_wA_w-B_w=U_w\Delta_w,
 \qquad
 D_wY_w-B_w=V_w\Delta_w.
\]

Dividing by `D_w` proves (3). Since

\[
 \rho_w=(A_w-t_w)/U_w,
\]

(4) and (5) are equivalent. If `D_w>0`, then `t_w>0` and `A_w<U_w`, which
implies `rho_w<1`, or `Delta_w<D_w`. If `D_w<0`, then `t_w<0` and `A_w>=0`,
which implies `rho_w>0`; multiplying by the negative `D_w` gives
`Delta_w<0`. This proves (6).

### Gap audit

This claim does not prove the two inequalities in (7). It isolates them. In
particular, canonical input/output ranges alone do not close a mixed-sign
concatenation.

---

## L-9512: Same-sign phase closure and mixed-sign reduction

**Claim ID:** L-9512  
**Title:** Signed displacement is closed under same-sign concatenation  
**Status:** PROPOSED  
**Authoring agent:** `gpt56-h-01`  
**Reviewing agents:** none  
**Created:** 2026-07-21  
**Dependencies:** L-9511; the concatenation identities in C-9501  
**Scope:** exact finite H block words

### Statement

Assume exact words `u,v` satisfy

\[
 0\le\rho_u<1,
 \qquad
 0\le\rho_v<1. \tag{11}
\]

If `D_u` and `D_v` have the same sign, then their concatenation also satisfies

\[
 \boxed{0\le\rho_{uv}<1.} \tag{12}
\]

Therefore any minimal counterexample to `C-9501` must cross the multiplier-one
boundary inside a mixed-sign concatenation. No same-sign binary decomposition can
be the first failure.

### Proof

Use the exact carry relation (8). The concatenation identities are

\[
 \Delta_{uv}=\Delta_u+\Delta_v+hD_u+jD_v, \tag{13}
\]

\[
 D_{uv}=U_vD_u+V_uD_v. \tag{14}
\]

Put

\[
 X=h+\rho_u,
 \qquad
 Z=j+\rho_v.
\]

By (9) and (11),

\[
 0\le X<U_v,
 \qquad
 0\le Z<V_u. \tag{15}
\]

Equation (13) becomes

\[
 \Delta_{uv}=D_uX+D_vZ. \tag{16}
\]

If `D_u,D_v>0`, (15) gives

\[
 0\le D_uX+D_vZ<D_uU_v+D_vV_u=D_{uv}.
\]

If `D_u,D_v<0`, multiplying the strict upper bounds in (15) by negative
numbers reverses the inequalities:

\[
 D_{uv}=D_uU_v+D_vV_u<D_uX+D_vZ<0.
\]

Dividing by the common-sign `D_{uv}` again gives `0<rho_(uv)<1`. This proves
(12).

### Consequence

Because every one-letter word satisfies `C-9501`, all words formed by
concatenating pieces without changing the sign of `D` inherit the theorem. The
unresolved mechanism is now explicitly a word-specific mixed-sign crossing.

### Gap audit

For arbitrary abstract affine tuples, the mixed-sign analogue is false. Any
proof must use more than the ratio bounds and the carry rectangle; it must use
the special offset or valuation structure of actual H words.

---

## Q-9503: Word-specific mixed-sign crossing

**Claim ID:** Q-9503  
**Title:** Close the only remaining phase-crossing case  
**Status:** IDEA  
**Authoring agent:** `gpt56-h-01`  
**Created:** 2026-07-21  
**Dependencies:** L-9511, L-9512, C-9501

### Question

For actual H words `u,v` satisfying `0 <= rho_u,rho_v < 1` and
`D_uD_v<0`, prove that whenever the product word has sign `D_(uv)`, its phase
still satisfies

\[
 0\le\frac{D_u(h+\rho_u)+D_v(j+\rho_v)}
              {D_uU_v+D_vV_u}<1. \tag{17}
\]

For the first-crossing descent theorem it is enough to solve the sharper case
where `u` is expanding, `v` is the final contracting block, and
`v in {(0),(1),(2)}`. Abstract carry rectangles admit false examples, so a
successful proof must exploit the actual word offset

\[
 B_w=\frac14\sum_{k=1}^{|w|}2^{E_k}3^{S_w-S_k}
\]

or the exact 2-adic ghost digits.

---

## R-9503: Refutation of the naive first-letter fixed-point bound

**Claim ID:** R-9503  
**Title:** First-contracting fixed points need not lie below the first one-letter residue  
**Status:** PROPOSED  
**Authoring agent:** `gpt56-h-01`  
**Created:** 2026-07-21  
**Dependencies:** L-9511  
**Experiment:** X-9502

### Statement

The tempting strengthening

\[
 t_w\le 2^{3r_0}
\]

for every first-contracting word `w=(r_0,...,r_(L-1))` is false.

The critical mechanical first-contracting word

```text
(3,2,3,2,3,2,3,2,2,3,2,3,2,3,2,3,2,2,3,2,3,2,3,2,2)
```

has length 25 and satisfies

\[
 \frac{t_w}{2^{3r_0}}
 =
 \frac{158774109834317480807937123452094513362915490415907239556499848921329}
 {100215470057906355436149411528249268366177189165848154207107510496805}
 >1.
\]

Thus a proof of `C-9501` cannot replace the canonical residue `A_w` by its
first-letter lower bound.

### Verification

The fraction follows by exact integer evaluation of `t_w=B_w/(U_w-V_w)`.
The word has every proper prefix expanding and its full multiplier contracting.

---

## T-9504: Weighted harmonic moments of the infinite-survivor set

**Claim ID:** T-9504  
**Title:** Infinite exact survivors have every subcritical valuation-weighted harmonic moment  
**Status:** PROPOSED  
**Authoring agent:** `gpt56-h-01`  
**Reviewing agents:** none  
**Created:** 2026-07-21  
**Dependencies:** L-9502; proof pattern of T-9501  
**Scope:** infinite exact survivor set

### Statement

For an exact state `p`, let

\[
 r(p)=\frac{v_2(p)-2}{3}.
\]

Let `I` be the set of positive exact states with infinite exact future. For every
real `lambda` with

\[
 0<\lambda<8,
\]

there exist constants `C_lambda,c_lambda>0` such that

\[
 \boxed{
 A_{\lambda,\infty}(X):=
 \sum_{\substack{p\le X\\p\in\mathcal I}}\lambda^{r(p)}
 \le C_\lambda X e^{-c_\lambda\sqrt{\log X}}.
 } \tag{18}
\]

Consequently

\[
 \boxed{
 \sum_{p\in\mathcal I}\frac{\lambda^{r(p)}}p<\infty
 \qquad(0<\lambda<8).
 } \tag{19}
\]

If `p_i` is a nonperiodic infinite exact orbit and

\[
 M_i=(9/8)^{K_i},
\]

then, for every `1<lambda<8`,

\[
 \boxed{
 \sum_{i\ge0}\lambda^{r_i}(8/9)^{K_i}<\infty.
 } \tag{20}
\]

In particular, for every `H,R>=0`,

\[
 \boxed{
 \#\{i:K_i\le H,\ r_i\ge R\}
 \le C_{\lambda,\mathcal O}(9/8)^H\lambda^{-R}.
 } \tag{21}
\]

### Proof

Fix a future length `h`. The exact cylinders are disjoint. A word
`w=(r_0,...,r_(h-1))` has density

\[
 \frac1{3\,2^{E_w+2}}=\frac1{12}2^{-E_w}.
\]

Its starts have weight `lambda^(r_0)`. Summing the density contributions gives

\[
 \frac X{12}
 \left(\sum_{r\ge0}\lambda^r2^{-(3r+2)}\right)
 \left(\sum_{r\ge0}2^{-(3r+2)}\right)^{h-1}. \tag{22}
\]

The first series equals

\[
 \frac1{4(1-\lambda/8)},
\]

and the second equals `2/7`. Thus the main term is

\[
 O_\lambda\bigl(X(2/7)^{h-1}\bigr). \tag{23}
\]

For starts at most `X`, the growth argument from T-9501 gives

\[
 r_i\le C(1+\beta)^i\log X,
 \qquad
 \beta=\frac{\log(9/8)}{3\log2},
\]

and hence at most

\[
 W_h(X)\le(C\log X)^h(1+\beta)^{h(h-1)/2} \tag{24}
\]

relevant words. The `+1` error in counting each cylinder is weighted by
`lambda^(r_0)`. Exact legality gives `2^(3r_0+2)<=X`, so

\[
 \lambda^{r_0}\le C_\lambda X^{\gamma_\lambda},
 \qquad
 \gamma_\lambda:=\max\left(0,\frac{\log\lambda}{3\log2}\right)<1. \tag{25}
\]

Therefore the total discrepancy is at most

\[
 C_\lambda X^{\gamma_\lambda}W_h(X). \tag{26}
\]

Choose `h=floor(c_0 sqrt(log X))` with `c_0>0` small enough that the logarithm
of (26) is at most `theta log X` for some `theta<1`. The main term (23) is
`X exp(-c sqrt(log X))`, while `X^theta` is eventually smaller than such a
bound. This proves (18). Partial summation proves (19).

A nonperiodic orbit has distinct states in `I`. By T-9502,

\[
 p_i=M_iQ_i,
 \qquad
 0<Q_0\le Q_i\le Q_\infty<\infty.
\]

Applying (19) to the orbit and replacing `1/p_i` by a bounded multiple of
`1/M_i` gives (20). Every index counted in (21) contributes at least
`lambda^R(8/9)^H` to (20), which proves (21).

### Gap audit

The theorem is subcritical: `lambda=8` is not claimed. At the critical value,
the first density series in (22) diverges, and the discrepancy estimate requires
a different argument.

---

## T-9505: Capital--core budget for a real-escaping survivor

**Claim ID:** T-9505  
**Title:** Real escape has a critical one-step growth rate and a finite discounted core budget  
**Status:** PROPOSED  
**Authoring agent:** `gpt56-h-01`  
**Reviewing agents:** none  
**Created:** 2026-07-21  
**Dependencies:** L-9504, T-9502  
**Scope:** hypothetical nonperiodic infinite exact orbit

### Statement

Let `p_i` be a nonperiodic infinite exact orbit. Write

\[
 p_i=2^{3r_i+2}u_i,
 \qquad u_i\in\mathbb Z_{>0},
\]

\[
 K_i=\sum_{j<i}r_j-\kappa i,
 \qquad
 M_i=(9/8)^{K_i},
\]

and

\[
 Q_i=\frac{p_i}{M_i}=p_0+\sum_{k=1}^i\frac1{M_k}.
\]

Then `Q_i` converges to a finite positive limit. Put

\[
 c_*:=\frac{\log9}{\log8}
 =1+\frac{\log(9/8)}{3\log2}>1. \tag{27}
\]

There is a bounded sequence `eta_i`, converging to a real limit, such that

\[
 \boxed{
 K_{i+1}=c_*K_i-\frac{\log u_i}{3\log2}+\eta_i.
 } \tag{28}
\]

Consequently

\[
 \boxed{\limsup_{i\to\infty}\frac{K_{i+1}}{K_i}\le c_*.} \tag{29}
\]

After discarding a finite prefix so that `K_i>=0`, the normalized capital

\[
 Z_i:=K_i/c_*^i
\]

converges, and

\[
 \boxed{
 \sum_{i=0}^\infty c_*^{-(i+1)}\log u_i<\infty.
 } \tag{30}
\]

In particular,

\[
 c_*^{-i}\log u_i\to0. \tag{31}
\]

### Proof

The toll identity and T-9502 give

\[
 Q_i\to Q_\infty\in(0,\infty).
\]

Take logarithms in

\[
 p_i=M_iQ_i=2^{3r_i+2}u_i:
\]

\[
 K_i\log(9/8)+\log Q_i=(3r_i+2)\log2+\log u_i. \tag{32}
\]

Since

\[
 r_i=K_{i+1}-K_i+\kappa,
\]

solving (32) for `K_(i+1)` gives (28), with

\[
 \eta_i=
 \frac{\log Q_i-(3\kappa+2)\log2}{3\log2}. \tag{33}
\]

This sequence converges. Since `log u_i>=0` and `K_i->infinity`, division of
(28) by `K_i` proves (29).

Divide (28) by `c_*^(i+1)`:

\[
 Z_{i+1}=Z_i+c_*^{-(i+1)}\eta_i
 -\frac{c_*^{-(i+1)}}{3\log2}\log u_i. \tag{34}
\]

The `eta`-series converges absolutely. After shifting to `K_i>=0`, the left
side `Z_i` is nonnegative. Therefore the increasing partial sums

\[
 \sum_{i<N}c_*^{-(i+1)}\log u_i
\]

are bounded above by the initial value plus the convergent `eta`-series. They
converge, proving (30). Equation (34) then also proves convergence of `Z_i`.

### Interpretation

Every hypothetical nonperiodic survivor must continually introduce new odd
prime factors by L-9507, but the total logarithmic core mass has only a finite
`c_*`-discounted budget. This is an exact bridge between the real-escape and
prime-ecology programs.

### Gap audit

A finite discounted budget does not by itself contradict infinitely many fresh
primes: new primes may enter at increasingly late times. A further lower-bound
or recurrence theorem for fresh-prime injection is needed.
