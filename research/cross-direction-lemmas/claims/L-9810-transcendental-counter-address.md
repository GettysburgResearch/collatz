# L-9810 — Transcendental targets force nonrational counter addresses

Claim ID: `L-9810`  
Title: An exponential 2-adic counter isometry cannot preload a transcendental target in a rational address  
Status: `PROPOSED`  
Authoring agent: `gpt56-synthesis-01`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: `L-9809`; the exponential counter isometry of `PR3/T-0028` for the specialization  
Scope: algebraic exponential isometries on `Z_2` and logarithmic connector targets  
Related counterexample candidates: none

## Definitions

Let

\[
b\in\mathbb Q\cap(1+8\mathbb Z_2),
\qquad b\ne1,
\]

and let `alpha,beta` be algebraic elements of `Q_2` with `beta!=0`. For
`s in Z_2`, define

\[
\Omega(s)=\alpha+\beta b^s,
\qquad
b^s:=\exp_2(s\log b).
\tag{1}
\]

Assume `Omega` is an isometry of `Z_2` onto `Z_2`. For `xi in Z_2`, let
`s_infinity=Omega^(-1)(xi)`, and let `s_H` be the unique residue in
`[0,2^H)` satisfying

\[
\Omega(s_H)\equiv\xi\pmod{2^H}.
\tag{2}
\]

## Statement

If `xi` is transcendental over `Q`, then:

### 1. Address irrationality

\[
\boxed{s_\infty\notin\mathbb Q\cap\mathbb Z_2.}
\tag{3}
\]

In particular, the all-depth address is neither an ordinary signed integer nor
an odd-denominator rational 2-adic integer.

### 2. No stabilization or eventual periodicity

The canonical finite addresses are exactly

\[
\boxed{s_H=[s_\infty]_{2^H}.}
\tag{4}
\]

They do not eventually stabilize, and the binary digit word of `s_infinity`
is not eventually periodic.

### 3. Address-complexity floor

If `p_s(n)` counts distinct length-`n` factors in the binary address word,
then

\[
\boxed{p_s(n)\ge n+1\qquad(n\ge1).}
\tag{5}
\]

### 4. Padding-counter specialization

For a fixed tower type and core class in `PR3/T-0028`,

\[
\Omega(s)
=\frac{\mu_*+3^{-g_*-7Ps}}{2^{r+1}}
=\frac{\mu_*}{2^{r+1}}
+\frac{3^{-g_*}}{2^{r+1}}(3^{-7P})^s
\tag{6}
\]

is an isometry of `Z_2`. Since `P=2^(r-1)>=2`, its base

\[
b=3^{-7P}
\]

lies in `1+8Z_2`. Taking the transcendental logarithmic bulk `xi=u_infinity`
from `L-9809`, the unique padding-counter address matching all of its bits is
nonrational and has the properties (4)--(5).

Thus every finite logarithm prefix has an ordinary counter address, but those
addresses cannot stabilize or become eventually periodic as the requested
precision tends to infinity.

## Proof

Suppose, toward a contradiction, that

\[
s_\infty=\frac nd\in\mathbb Q\cap\mathbb Z_2
\]

in lowest terms. Then `d` is odd. Put `y=b^(n/d)` using the analytic power in
(1). The exponential law gives

\[
y^d=b^n.
\tag{7}
\]

Since `b^n` is rational, (7) makes `y` algebraic over `Q`. Therefore

\[
\Omega(s_\infty)=\alpha+\beta y
\]

is algebraic, contradicting `Omega(s_infinity)=xi` and the transcendence of
`xi`. This proves (3).

Because `Omega` is an isometry, reduction modulo `2^H` is a permutation and

\[
\Omega(s)\equiv\Omega(s_\infty)\pmod{2^H}
\iff
s\equiv s_\infty\pmod{2^H}.
\]

The canonical solution is therefore (4). Eventual stabilization would make
`s_infinity` an ordinary nonnegative integer, contradicting (3). An eventually
periodic binary expansion represents a rational element of `Q intersect Z_2`
by the finite geometric-series calculation in `L-9809`, again contradicting
(3).

Finally, the elementary one-sided Morse--Hedlund argument used in `L-9809`
shows that any non-eventually-periodic word has at least `n+1` factors of every
length `n`; this proves (5). Formula (6) is the definition in `PR3/T-0028`,
which supplies the required isometry. Its rational coefficients and
`3^(-7P) in 1+8Z_2` verify all abstract hypotheses. ∎

## Motivation

`PR3/T-0028` proves that the unbounded padding counter can route every finite
binary connector prefix. `L-9809` proves that the completed logarithmic target
is transcendental. The present lemma joins those facts and identifies the
precise nonuniformity:

- every finite inverse image `s_H` is an ordinary address;
- the compatible all-depth inverse image is not rational and cannot be frozen
  into one ordinary counter register.

This does not defeat the adaptive counter program. It shows that a successful
program must generate the changing addresses forward rather than preload their
completion.

## Dependency audit

- Algebraicity of `b^(n/d)` follows directly from (7); no transcendence theorem
  is used in the abstract proof beyond the assumed transcendence of `xi`.
- `L-9809` supplies a concrete transcendental target in `Z_2`.
- `PR3/T-0028` is used only to identify the four padding maps as isometries of
  the form (1).

## Gap audit

- Dynamic addresses may change with scale and with the chosen coarse cell;
  this lemma rules out only one fixed all-depth preload.
- Linear factor complexity does not rule out a simple online generator.
- The physical residual state could generate successive `s_H` without ever
  representing `s_infinity` as an ordinary integer.
- No marked Collatz initialization is constructed or excluded.

## Adversarial tests

- Rational nonintegers in `Z_2` have eventually periodic, nonterminating binary
  expansions; they are excluded by (3), not merely by nonstabilization.
- The denominator `d` must be odd for `n/d` to lie in `Z_2`; this is exactly
  what makes the analytic `d`-th root in (7) unambiguous near `1`.
- An arbitrary nonlinear isometry need not preserve algebraicity. The
  exponential algebraic form (1) is essential.

## Remaining uncertainty

None in the abstract address theorem. Its force against a physical construction
depends on whether that construction tries to reuse one fixed counter chart.

## Suggested next attack

Study the transition map between the scale-dependent addresses `s_H` rather
than the completed address itself. A true forward router must compute the next
bit of `s_infinity` from finite residual data without storing a rational or
completed oracle.
