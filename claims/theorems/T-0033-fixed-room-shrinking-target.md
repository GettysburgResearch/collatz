# T-0033 — Fixed-room floor law and doubly-exponential shrinking target

Claim ID: `T-0033`  
Title: Every infinite corrected-stage path is the floor orbit of one fixed real room with an exponentially tiny positive defect  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-22  
Dependencies: `L-0025`, `L-0031`  
Scope: positive ordinary trajectories through the fixed corrected 256-transition phase-34 stage architecture  
Related counterexample candidates: none

## Setup

Use the scaled ordinary stage equation of `L-0031`:

\[
2^{\mathcal E_m}W_{m+1}
=
3^{\mathcal A_m}W_m+\Tau_m,
\tag{1}
\]

where

\[
\mathcal A_m
=
\frac{5369}{2}2^m+1792,
\tag{2}
\]

\[
\mathcal E_m
=
\frac{8459}{2}2^m+2816,
\tag{3}
\]

and, for the stage source word `w_m`,

\[
\boxed{
\Tau_m
=
\sum_{k=0}^{255}
2^{U_{m,k}+\alpha_{i_{m,k}}}
3^{V_{m,k}+\beta_{i_{m,k}}}>0.}
\tag{4}
\]

Define the homogeneous scale exponents

\[
\boxed{
a_m
=
\frac{5369}{2}2^m+1792m,}
\tag{5}
\]

\[
\boxed{
e_m
=
\frac{8459}{2}2^m+2816m,}
\tag{6}
\]

and the positive rational scale

\[
\boxed{
H_m=\frac{3^{a_m}}{2^{e_m}}.}
\tag{7}
\]

Then

\[
\boxed{
\frac{H_{m+1}}{H_m}
=
\frac{3^{\mathcal A_m}}{2^{\mathcal E_m}}.}
\tag{8}
\]

## Statement

Let

\[
W_{m_0},W_{m_0+1},\ldots
\in\mathbb Z_{>0}
\]

be any infinite ordinary scaled-tail trajectory satisfying (1), with
`m_0 >= 12`.

### 1. One fixed real room

The normalized values

\[
\boxed{C_m=\frac{W_m}{H_m}}
\tag{9}
\]

increase strictly and converge to one finite real number

\[
\boxed{C_\infty>0.}
\tag{10}
\]

Their exact increment is

\[
\boxed{
C_{m+1}-C_m
=
\frac{\Tau_m}{3^{\mathcal A_m}H_m}
=
\frac{2^{e_m}\Tau_m}{3^{a_{m+1}}}.}
\tag{11}
\]

Thus

\[
\boxed{
C_\infty
=
\frac{W_{m_0}}{H_{m_0}}
+
\sum_{m=m_0}^{\infty}
\frac{2^{e_m}\Tau_m}{3^{a_{m+1}}}.}
\tag{12}
\]

### 2. Uniform toll bound

Put `B=2^m`. For every stage word,

\[
\boxed{
0<
\frac{\Tau_m}{3^{\mathcal A_m}}
<
\frac{108}{3^{7(B+1)}}.}
\tag{13}
\]

Consequently

\[
\boxed{
0<C_\infty-C_m
<
\frac{216}{3^{7(B+1)}H_m}.}
\tag{14}
\]

### 3. Exact floor representation

Multiplying (14) by `H_m` gives

\[
\boxed{
0<C_\infty H_m-W_m
<
\frac{216}{3^{7(2^m+1)}}<1.}
\tag{15}
\]

Therefore every stage boundary is exactly

\[
\boxed{
W_m=\left\lfloor C_\infty H_m\right\rfloor.}
\tag{16}
\]

Equivalently, the fixed room satisfies the shrinking-target condition

\[
\boxed{
0<
\left\{C_\infty H_m\right\}
<
\frac{216}{3^{7(2^m+1)}}.}
\tag{17}
\]

The target width decays doubly exponentially in the scale index `m`.

### 4. Exact defect recurrence

Define

\[
\varepsilon_m=C_\infty H_m-W_m.
\tag{18}
\]

Then

\[
\boxed{
\varepsilon_{m+1}
=
\frac{3^{\mathcal A_m}}{2^{\mathcal E_m}}\varepsilon_m
-
\frac{\Tau_m}{2^{\mathcal E_m}},}
\tag{19}
\]

with every `epsilon_m` lying in the interval (15). The stage word is therefore
an exact digit selector keeping one expanding real orbit inside a rapidly
shrinking positive window.

## Proof

Equation (8) follows from

\[
a_{m+1}-a_m=\mathcal A_m,
\qquad
e_{m+1}-e_m=\mathcal E_m.
\]

Divide (1) by `H_(m+1)` and use (8). This gives (11), so `C_m` is strictly
increasing.

It remains to prove convergence and the quantitative bound. Divide each toll
term in (4) by `3^(mathcal A_m)`. Let

\[
r_{m,k}
=
2^{U_{m,k}+\alpha_{i_{m,k}}}
3^{V_{m,k}+\beta_{i_{m,k}}-\mathcal A_m}.
\tag{20}
\]

The first term satisfies

\[
0<r_{m,0}
=
\frac{b_{i_{m,0}}}{3^{7(B+1)}}
\le
\frac{54}{3^{7(B+1)}}.
\tag{21}
\]

For consecutive terms,

\[
\frac{r_{m,k+1}}{r_{m,k}}
=
2^{11(t_{m,k+1}+1)+\Delta\alpha}
3^{-7(t_{m,k+1}+1)+\Delta\beta},
\tag{22}
\]

where

\[
|\Delta\alpha|\le3,
\qquad
|\Delta\beta|\le2.
\]

Hence

\[
\frac{r_{m,k+1}}{r_{m,k}}
\le
72
\left(\frac{2^{11}}{3^7}\right)^{t_{m,k+1}+1}.
\tag{23}
\]

The exact integer inequality

\[
144\,2048^{128}<2187^{128}
\tag{24}
\]

implies that the right side of (23) is less than `1/2` whenever
`t_(m,k+1)+1 >= 128`. This certainly holds for `m >= 12`. Therefore the
normalized toll is dominated by a geometric series:

\[
0<\frac{\Tau_m}{3^{\mathcal A_m}}
=\sum_{k=0}^{255}r_{m,k}
<2r_{m,0}
\le\frac{108}{3^{7(B+1)}},
\]

proving (13).

Put

\[
u_m=\frac{108}{3^{7(2^m+1)}H_m}.
\]

By (11) and (13),

\[
0<C_{m+1}-C_m<u_m.
\]

Also

\[
\frac{u_{m+1}}{u_m}
=
3^{-7\cdot2^m}
\frac{H_m}{H_{m+1}}
<\frac12.
\tag{25}
\]

Here `H_(m+1)>H_m`: using `log_2(3)>84/53` from `L-0025`,

\[
\log_2\frac{H_{m+1}}{H_m}
>
\frac{2669}{106}2^m+rac{1280}{53}>0.
\]

Thus the increment series converges, and its tail is less than

\[
\sum_{r=m}^{\infty}u_r<2u_m.
\]

This proves (10), (12), and (14). Equation (15) follows after multiplication by
`H_m`; its final upper bound is less than one already for `m=0`. Since `W_m` is
an integer, (16)--(17) follow. Finally, subtract the stage recurrence for
`W_(m+1)` from the homogeneous recurrence for `C_infinity H_(m+1)` to obtain
(19). ∎

## Interpretation

The corrected tower route has an exact real companion analogous to a fixed-room
or Mahler shrinking-target problem:

```text
one real room C_infinity
    -> expanding rational scales H_m
    -> integer floors W_m
    -> stage words keep the fractional defects in tiny positive windows.
```

This is stronger than a generic bounded-window statement. The allowed window
at scale `m` is smaller than `3^(-7*2^m)`.

Together with `T-0032`, a hypothetical ordinary path must simultaneously:

1. hit every shrinking real target in (17);
2. generate infinitely many fresh ordinary prime factors;
3. satisfy the canonical cap-to-correction stitches of `T-0031`.

These are three views of the same exceptional path: real, multiplicative, and
2-adic/canonical.

## Gap audit

- The theorem constructs `C_infinity` from an assumed infinite ordinary path;
  it does not prove such a path exists.
- An arbitrary real number may have exceptional shrinking-target behavior; no
  equidistribution or transcendence conclusion is claimed.
- The floor law does not replace the exact connector and marked-Collatz replay.
- No positive starting integer or counterexample is supplied.

## Adversarial tests

`X-0016` verifies the homogeneous exponent recurrence, exact normalized
increments, toll ordering, and the floor identity on finite exact synthetic
stage chains. The infinite convergence proof is the geometric estimate above,
not finite computation.