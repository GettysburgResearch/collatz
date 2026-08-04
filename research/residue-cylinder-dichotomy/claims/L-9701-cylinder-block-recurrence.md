# L-9701 — Exact nested cylinders and residue-block recurrence

**Claim ID:** `L-9701`  
**Title:** Every finite odd-affine directive selects one cylinder, with an exact new-block carry formula  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-cylinder-01`  
**Reviewing agents:** none  
**Created:** 2026-07-22  
**Last updated:** 2026-07-22  
**Dependencies:** none  
**Scope:** arbitrary finite or infinite chains of odd-affine maps divided by powers of two  
**Related counterexample candidates:** none

## Motivation

Several active branches reach the same boundary: finite directives determine nested exact residue cylinders, while ordinary realization is equivalent to stabilization. This lemma supplies one self-contained algebraic recurrence for the new block `a_k`, so later theorems can reason about stabilization without importing a branch-specific cylinder formalism.

## Definitions

For an integer `z` and positive modulus `M`, `[z]_M` denotes the least representative in `{0,...,M-1}`. All modular inverses below exist because their arguments are odd and every modulus is a power of two.

## 1. Odd-affine chain

Let

\[
f_n(x)=\frac{N_nx+C_n}{q_n},
\tag{1}
\]

where

\[
N_n\in2\mathbb Z+1,
\qquad
q_n=2^{d_n},
\qquad d_n\ge1,
\qquad
C_n\in\mathbb Z.
\tag{2}
\]

Define

\[
P_0=1,
\qquad F_0=0,
\qquad Q_0=1,
\tag{3}
\]

and recursively

\[
\boxed{P_{k+1}=N_kP_k,}
\tag{4}
\]

\[
\boxed{F_{k+1}=N_kF_k+Q_kC_k,}
\tag{5}
\]

\[
\boxed{Q_{k+1}=Q_kq_k.}
\tag{6}
\]

Then chronological composition gives

\[
\boxed{
x_k=\frac{P_kx_0+F_k}{Q_k}.}
\tag{7}
\]

## 2. Exact finite-domain equivalence

The following are equivalent:

1. every local quotient \(x_1,\ldots,x_k\) is an integer;
2. the composite numerator satisfies
   \[
   P_kx_0+F_k\equiv0\pmod{Q_k}.
   \tag{8}
   \]

### Proof

The forward implication follows by composing the exact integer equations.

For the reverse implication, expand the composite numerator as

\[
P_kx_0+F_k
=
\left(\prod_{j=1}^{k-1}N_j\right)(N_0x_0+C_0)
+q_0Z
\tag{9}
\]

for one integer \(Z\). Divisibility by \(Q_k\), hence by \(q_0\), and oddness
of the product force

\[
N_0x_0+C_0\equiv0\pmod{q_0}.
\]

Thus \(x_1\) is an integer. Divide the composite relation by \(q_0\) and repeat
on the suffix. Induction proves every local quotient integral. ∎

## 3. Unique finite cylinders

Because \(P_k\) is odd, it is invertible modulo \(Q_k\). Define the least
representative

\[
\boxed{
R_k=[-F_kP_k^{-1}]_{Q_k},
\qquad0\le R_k<Q_k.
}
\tag{10}
\]

Then

\[
\boxed{
x_0\text{ realizes the first }k\text{ maps integrally}
\iff x_0\equiv R_k\pmod{Q_k}.}
\tag{11}
\]

The cylinders are nested:

\[
R_{k+1}\equiv R_k\pmod{Q_k}.
\tag{12}
\]

Hence there is a unique block

\[
\boxed{
a_k=\frac{R_{k+1}-R_k}{Q_k},}
\tag{13}
\]

with

\[
\boxed{0\le a_k<q_k.}
\tag{14}
\]

## 4. Exact block-state recurrence

Let the endpoint of the current least representative be

\[
\boxed{
H_k=\frac{P_kR_k+F_k}{Q_k}\in\mathbb Z.
}
\tag{15}
\]

Any lift of the current initial cylinder has the form

\[
x_0=R_k+Q_ka.
\]

After the first \(k\) maps its endpoint is

\[
x_k=H_k+P_ka.
\tag{16}
\]

Define the next local correction

\[
\rho_k=[-C_kN_k^{-1}]_{q_k}.
\tag{17}
\]

The next map is integral exactly when

\[
H_k+P_ka\equiv\rho_k\pmod{q_k}.
\]

Therefore the new residue block is

\[
\boxed{
a_k=[(\rho_k-H_k)P_k^{-1}]_{q_k}.}
\tag{18}
\]

Equivalently,

\[
\boxed{
a_k=
[-(N_kH_k+C_k)(N_kP_k)^{-1}]_{q_k}.}
\tag{19}
\]

The new endpoint is

\[
\boxed{
H_{k+1}
=
\frac{N_k(H_k+P_ka_k)+C_k}{q_k}.
}
\tag{20}
\]

Equations (13), (18), and (20) are an exact finite state recurrence for the
nested residue blocks. No inverse-limit digit is assumed as input.

## 5. Infinite directives and ordinary integers

Since \(Q_k\to\infty\), the nested cylinders determine one point

\[
x^*\in\mathbb Z_2.
\tag{21}
\]

If \(a_k=0\) for all sufficiently large \(k\), then the least representatives
stabilize at one nonnegative integer \(R\). That integer belongs to every
finite cylinder and therefore generates an infinite integer trajectory under
(1).

Conversely, if \(x^*=R\in\mathbb Z_{\ge0}\), then once \(Q_k>R\), the least
representative is exactly \(R\), so all later blocks vanish.

Thus

\[
\boxed{
x^*\in\mathbb Z_{\ge0}
\iff R_k\text{ eventually stabilizes}
\iff a_k=0\text{ eventually}.}
\tag{22}
\]

For negative integers the least nonnegative representatives do not stabilize.
Theorems `T-9701` and `T-9702` prove the stronger conclusion that their frozen
completion is not in \(\mathbb Z\) at all.

## Dependency audit

The proof is elementary and self-contained. It uses only:

- oddness of every `N_k`, hence invertibility modulo powers of two;
- exact integer composition of affine maps;
- uniqueness of least representatives.

PR #20 `T-9409` and PR #19 `L-9503` are comparison interfaces only.

## Gap audit

- The lemma proves finite integrality and the stabilization equivalence; it does not decide whether blocks vanish eventually.
- Equation (22) concerns nonnegative ordinary completions. Negative integers require a separate argument because their least nonnegative residues do not stabilize.
- The recurrence is exact but may involve exponentially large moduli; no complexity claim is made.

## Adversarial tests

`X-9701` computes each cylinder both from `(P,F,Q)` and from the incremental block recurrence. The independent checker instead replays `R` and `R+Q` through every accepted prefix and solves the next congruence from their endpoint stride.

## Remaining uncertainty

None is known in the finite algebra. Independent mathematical reconstruction is still required before promotion beyond `PROPOSED`.

## Suggested next attack

Find a directive-class invariant forcing either infinitely many nonzero values of (18), or a finite symbolic rule making (18) zero from some point onward.

## Interface note

Equation (18) is the common carry formula behind PR #20 `T-9409` and PR #19 `L-9503`, written for a general odd-affine chain. This file re-proves the needed algebra and does not promote either external claim.
