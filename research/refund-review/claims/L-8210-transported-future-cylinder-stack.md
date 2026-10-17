# L-8210 — The future legality stack is an inverse-affine transported cylinder

**Claim ID:** `L-8210`  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-refund-01`  
**Created:** 2026-07-23  
**Dependencies:** `L-8203`, `R-8203`; for the phase-34 growth corollary, frozen PR #49 `T-8512`  
**Scope:** exact changing-modulus quotient paths with odd transport, including PR #49 and PR #51  
**Related counterexample candidates:** none

## 1. Exact path setup

Fix one finite legal path and suppress its initial index. At step `h` write

\[
 m_h=\rho_h+H_h\ell_h,
 \qquad 0\le \rho_h<H_h,
 \qquad \ell_h\in\mathbf Z_{\ge0},
\tag{1}
\]

and suppose the exact transition is

\[
 m_{h+1}=\sigma_h+A_h\ell_h,
 \qquad \sigma_h\in\mathbf Z,
 \qquad A_h\text{ odd}.
\tag{2}
\]

Since the next state is legal,

\[
 \boxed{
 H_{h+1}\ell_{h+1}
 =A_h\ell_h+\delta_h,}
 \qquad
 \delta_h=\sigma_h-\rho_{h+1}.
\tag{3}
\]

In the live refund systems every `H_h` is a positive power of two, so every odd `A_h` is invertible modulo every product of future radices.

## 2. The transported cylinder cocycle

Define

\[
 K_0=P_0=1,
 \qquad B_0=0,
\tag{4}
\]

and, for `s>=0`,

\[
 \boxed{
 \begin{aligned}
 K_{s+1}&=K_sH_{s+1},\\
 P_{s+1}&=A_sP_s,\\
 B_{s+1}&=A_sB_s+K_s\delta_s.
 \end{aligned}}
\tag{5}
\]

Then every legal path satisfies the exact `s`-step identity

\[
 \boxed{
 K_s\ell_s=P_s\ell_0+B_s.}
\tag{6}
\]

Consequently, legality through the first `s` future cylinders is equivalent to one residue of the initial lift:

\[
 \boxed{
 \ell_0\equiv\Theta_s\pmod {K_s},
 \qquad
 \Theta_s=[-P_s^{-1}B_s]_{K_s}.}
\tag{7}
\]

The residue is unique because `P_s` is odd. Moreover,

\[
 \boxed{
 \Theta_{s+1}\equiv\Theta_s\pmod {K_s}.}
\tag{8}
\]

Thus the actual future-cylinder stack is the nested sequence `Theta_s`, not the plain Euclidean expansion of `m_0` identified in the refuted interpretation of PR #49 `T-8512`.

## 3. One transported digit at a time

Put

\[
 \Theta_0=0,
 \qquad
 c_s={P_s\Theta_s+B_s\over K_s}.
\tag{9}
\]

By `(8)` there is a unique digit

\[
 \boxed{
 d_s={\Theta_{s+1}-\Theta_s\over K_s},
 \qquad 0\le d_s<H_{s+1}.}
\tag{10}
\]

It is generated causally by the inverse-affine rule

\[
 \boxed{
 d_s=
 \left[
 -(A_sc_s+\delta_s)(A_sP_s)^{-1}
 \right]_{H_{s+1}}.}
\tag{11}
\]

The transported carry updates by

\[
 \boxed{
 c_{s+1}
 ={A_sc_s+A_sP_sd_s+\delta_s\over H_{s+1}}.}
\tag{12}
\]

Equations `(10)--(12)` are ordinary exact integer arithmetic. They expose the missing stack transducer: before a later cylinder digit can be read, it must be pulled back through every intervening odd affine multiplier and carry.

## 4. Exact quotient transport

For any finite horizon `s`, write

\[
 \boxed{
 \ell_0=\Theta_s+K_su_s.}
\tag{13}
\]

Then the actual future lift is

\[
 \boxed{
 \ell_s=c_s+P_su_s.}
\tag{14}
\]

In particular, `u_s` is the genuine free ordinary quotient beyond the complete transported `s`-step cylinder. It is not the `s`th plain Euclidean digit of `m_0`.

## 5. Ordinary stabilization criterion

Because `K_s` tends to infinity, the nested residues `Theta_s` define one unique element

\[
 \Theta_\infty\in\mathbf Z_2.
\tag{15}
\]

An ordinary nonnegative integer can satisfy all of the finite cylinder congruences only when

\[
 \boxed{
 \Theta_s\text{ is eventually constant},}
\tag{16}
\]

or, equivalently,

\[
 \boxed{d_s=0\text{ for every sufficiently large }s.}
\tag{17}
\]

This is only the ordinary-support criterion. A proposed infinite path must additionally prove nonnegativity and every physical finite-state gate. Existence of the `2`-adic limit is automatic and is not a counterexample certificate.

## 6. Corrected phase-34 stack consequence

Let `D_plain(m_N)` be the numerical mixed-radix capacity used in PR #49 `T-8512`, so

\[
 D_{\rm plain}(m_N)\ge d
 \quad\Longrightarrow\quad
 m_N\ge\prod_{h=0}^{d-1}H_{N+h}.
\tag{18}
\]

Since

\[
 m_N=\rho_N+H_N\ell_N,
 \qquad 0\le\rho_N<H_N,
\]

`(18)` implies, for `d>=1`,

\[
 \ell_N\ge\prod_{h=1}^{d-1}H_{N+h}=K_{d-1}.
\tag{19}
\]

Along an actual legal path, `(13)` and `(19)` force

\[
 \boxed{u_{d-1}\ge1.}
\tag{20}
\]

Therefore the numerical bounds of `T-8512` do have a correct physical interpretation after one index shift: they lower-bound the depth of the **transported** future-cylinder stack.

If a permanent refund tail begins at connector `n`, the retained numerical estimates of `T-8512` imply

\[
 \boxed{
 D_{\rm trans}(n+r)
 \ge
 \max\left\{0,\left\lfloor{r\over288}\right\rfloor-1\right\}}
 \qquad(r\ge288),
\tag{21}
\]

and

\[
 \boxed{
 D_{\rm trans}(n+r)
 \ge
 \left\lfloor{r\over233}\right\rfloor-1}
 \qquad(r\ge100{,}909).
\tag{22}
\]

Hence

\[
 \boxed{
 \liminf_{r\to\infty}
 {D_{\rm trans}(n+r)\over r}
 \ge{1\over233}.}
\tag{23}
\]

The loss of one level comes from separating the current radix `H_N` from the future-radix product.

## Proof

Identity `(6)` follows by induction. For `s=0` it is tautological. If it holds at `s`, then `(3)` gives

\[
 \begin{aligned}
 K_{s+1}\ell_{s+1}
 &=K_s(A_s\ell_s+\delta_s)\\
 &=A_s(P_s\ell_0+B_s)+K_s\delta_s\\
 &=P_{s+1}\ell_0+B_{s+1}.
 \end{aligned}
\]

This proves `(6)`. Divisibility by `K_s` and oddness of `P_s` give the unique residue `(7)`. Reducing the `s+1` condition modulo `K_s` proves nesting `(8)`.

Substitute `Theta_(s+1)=Theta_s+K_sd_s` into

\[
 P_{s+1}\Theta_{s+1}+B_{s+1}\equiv0\pmod {K_sH_{s+1}}.
\]

Using `(5)` and `(9)`, division by `K_s` gives

\[
 A_sc_s+A_sP_sd_s+\delta_s\equiv0\pmod {H_{s+1}},
\]

which has the unique solution `(11)` and yields `(12)`.

Finally, substituting `(13)` into `(6)` gives `(14)`. The stabilization criterion follows from `K_s\to\infty`: if an ordinary integer `ell_0` satisfies every congruence, then for all sufficiently large `s` one has `K_s>ell_0`, so the canonical representative `Theta_s` must equal `ell_0`; the converse is immediate. Equations `(18)--(23)` follow from ordinary Euclidean division as displayed. ∎

## Consequences

1. `R-8203` remains correct: the raw mixed-radix digits are not future legality residues.
2. PR #49's stack interpretation can be repaired with a fresh claim using `Theta_s,d_s,c_s`.
3. The repaired stack is causal but not free: every digit is twisted by the accumulated odd multiplier `P_s` and carry `c_s`.
4. The same cocycle applies to PR #51 with `A_s=9^(r_s+1)` and its changing run modulus.
5. A strictly causal controller determines a unique `2`-adic transported stack automatically; ordinary eventual-zero closure remains the load-bearing theorem.

## Gap audit

- The cocycle does not construct one infinite legal path.
- The transported digits depend on the actual finite-state path and cannot be chosen independently.
- Linear growth of transported capacity is conditional on the hypothetical infinite phase-34 orbit used by `T-8512`.
- Large stack depth is capacity plus correctly transported content; it is still not an all-time routing invariant.
- No `K-82xx` object is produced.