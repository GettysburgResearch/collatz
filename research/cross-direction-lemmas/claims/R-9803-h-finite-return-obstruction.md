# R-9803 — The H suffix compiler does not close in finitely many ordinary-carry charts

Claim ID: `R-9803`  
Title: Every post-crossing return retains an unbounded 2-adic tail coordinate  
Status: `PROPOSED`  
Authoring agent: `gpt56-synthesis-01-h`, integrated by `gpt56-synthesis-01`  
Reviewing agents: `gpt56-synthesis-01`  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: `L-9814`; exact H cylinder concatenation  
Scope: refutation of finite phase-only closure for the adaptive H compiler  
Related counterexample candidates: none

## Definitions

Retain

\[
v_s=(s,0^{a-1}),
\qquad
a=\lfloor\alpha s\rfloor
\tag{1}
\]

from `L-9814`. Its integral affine data are

\[
U_v=8^s4^a,
\qquad
V_v=9^s3^a,
\qquad
B_v=8^s(4^a-3^a).
\tag{2}
\]

Put

\[
c_s=[9^{-s}]_{4^a},
\qquad
d_s=\frac{9^sc_s-1}{4^a}.
\tag{3}
\]

## Statement

### 1. Exact incoming canonical state

The canonical input and endpoint of `v_s` are

\[
\boxed{
A_v=8^sc_s,
\qquad
Y_v=1+3^ad_s.
}
\tag{4}
\]

### 2. Exact compiler transition

For `r in {1,3}`, the suffix `r0` has

\[
g_{r0}(x)
=\frac{3^{2r+2}}{2^{3r+4}}x+\frac7{16}.
\tag{5}
\]

Its canonical data are

| suffix `z` | `U_z` | `V_z` | `B_z` | `A_z` | `Y_z` |
|---|---:|---:|---:|---:|---:|
| `10` | 128 | 81 | 56 | 72 | 46 |
| `30` | 8192 | 6561 | 3584 | 4608 | 3691 |

Define the exact interface carry

\[
\boxed{
h_{s,z}
=\left[(A_z-Y_v)V_v^{-1}\right]_{U_z},
}
\tag{6}
\]

and

\[
k_{s,z}
=\frac{Y_v+h_{s,z}V_v-A_z}{U_z}.
\tag{7}
\]

Then

\[
\boxed{
A_{v_sz}=A_v+h_{s,z}U_v,
\qquad
Y_{v_sz}=Y_z+k_{s,z}V_z.
}
\tag{8}
\]

More generally, the full cylinder transition is

\[
\boxed{
A_{v_sz}+tU_vU_z
\longmapsto
Y_{v_sz}+tV_vV_z
\qquad(t\ge0).
}
\tag{9}
\]

Thus natural cylinder renormalization acts as the identity on the unbounded
height `t`; the compiler does not reset it.

### 3. Surviving 2-adic tail

Put

\[
\xi_{s,z}=\frac{A_z-Y_v}{V_v}\in\mathbb Z_2.
\tag{10}
\]

The suffix consumes only its lowest `log_2 U_z` bits:

\[
\boxed{
h_{s,z}=[\xi_{s,z}]_{U_z},
\qquad
k_{s,z}
=-V_v\frac{\xi_{s,z}-h_{s,z}}{U_z}.
}
\tag{11}
\]

The remaining quotient is again an unbounded tail coordinate.

### 4. No finite ordinary-carry return

Let `w` be any nonempty exact prefix with canonical output `Y_w>0` and odd
multiplier numerator `V_w`. The carry needed to enter a new block `v_sigma` is

\[
\tau_\sigma
=\left[(A_{v_\sigma}-Y_w)V_w^{-1}\right]_{U_{v_\sigma}}.
\tag{12}
\]

Since `8^sigma` divides `A_(v_sigma)`,

\[
\boxed{
\tau_\sigma
\equiv-Y_wV_w^{-1}
\pmod{2^{3\sigma}}.
}
\tag{13}
\]

The carries `(tau_sigma)` cannot remain bounded or eventually stabilize as
`sigma` tends to infinity. Consequently no finite state made only of the
branch `10/30` and bounded ordinary carries closes the compiler under returns
to all `v_sigma` blocks.

For the compiler outputs themselves,

\[
Y_{v_sz}\equiv1\pmod3,
\tag{14}
\]

while `V_(v_sz)` is a strictly growing power of `3`. Hence the reduced rational
tail addresses

\[
\boxed{
-\frac{Y_{v_sz}}{V_{v_sz}}
}
\tag{15}
\]

are infinitely many distinct 2-adic rationals as `s` varies. No finite list of
fixed rational tail charts contains all post-crossing states.

## Proof

Writing a canonical input as `A_v=8^s c`, the cylinder congruence reduces to

\[
9^sc\equiv1\pmod{4^a}.
\]

Its unique canonical solution is `c=c_s`. Substituting in the affine map (2)
gives `Y_v=1+3^a d_s`, proving (4).

The one-letter H data and one final zero give (5) and the table. An input in
the `v_s` cylinder has form

\[
A=A_v+U_vj
\]

and reaches `X=Y_v+V_vj`. It enters the suffix cylinder exactly when
`X congruent to A_z mod U_z`, which is (6). Write `j=h_(s,z)+U_z t`.
Then

\[
X=A_z+U_z(k_{s,z}+V_vt),
\]

and applying the suffix gives (8)--(9). Equation (11) is (6)--(7) rewritten
using the exact 2-adic quotient.

For the return obstruction, reduction of (12) modulo `2^(3sigma)` gives (13).
The low residues on its right are the compatible canonical representatives of
the fixed rational

\[
\omega_w=-Y_w/V_w\in\mathbb Z_2.
\]

If `(tau_sigma)` were bounded, these compatible representatives would be
bounded and hence eventually constant at an ordinary nonnegative integer `k`.
Equality in `Z_2` would then give `-Y_w/V_w=k`, impossible because the left
side is a negative rational and `Y_w>0`. Appending any fixed bounded
continuation preserves a positive endpoint and an odd numerator, so it cannot
remove the obstruction.

Finally, (8) and the table give `Y_(v_sz)=1 mod3`, whereas `V_(v_sz)` is a
power of `3`. The fractions in (15) are reduced and their denominators grow
strictly, proving that their values are distinct. ∎

## Motivation

`L-9814` gives an optimal finite compiler for strict H crossings. The natural
next hope was a finite return chart that could iterate the compiler. This
refutation identifies why that hope fails: exact concatenation preserves an
ordinary height, and its return address reveals successively more digits of a
genuine 2-adic rational tail.

## Dependency audit

- The incoming and suffix data are computed directly from the exact H affine
  maps.
- Cylinder concatenation supplies only the elementary interface congruence in
  (6).
- No empirical global H sign claim is used.
- The refutation uses ordinary boundedness and compatible 2-adic residues, not
  a numerical orbit search.

## Gap audit

- The result excludes finite phase-only, bounded-carry, and finite
  fixed-address closure.
- It does not exclude a skew-product chart retaining a full variable
  `Z_2` coordinate.
- It does not exclude an exceptional identity restricted to one isolated
  canonical height such as `t=0`.
- Failure of finite return closure does not undo the finite strict-crossing
  theorem in `L-9814`.

## Adversarial tests

- The height `t` in (9) is not the suffix interface height; that interface
  height is `k_(s,z)+V_vt`, and is also unbounded.
- A rational 2-adic address need not have growing canonical residues if it is
  a nonnegative integer. The sign `-Y_w/V_w<0` is what rules that out here.
- Infinitely many rational tail addresses do not by themselves preclude one
  chart with a variable rational or full 2-adic coordinate.

## Remaining uncertainty

The smallest plausible iterative state space is now a finite phase extension
of an unbounded ordinary height or `Z_2` tail. Whether its exact return map has
useful contraction, monotonicity, or an invariant cone is open.

## Suggested next attack

Retain the tail `xi` in (11) as a genuine state variable and compute the two
skew-product return maps induced by `10` and `30`. A contraction or forbidden
invariant region in that enlarged space would be a sound replacement for the
finite-state closure refuted here.
