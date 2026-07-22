# L-9832 — Exact small-remainder prime-power Padé factors

Claim ID: `L-9832`  
Title: Odd prime-power Padé residuals are exactly antisymmetric and simple when `p>s`  
Status: `PROPOSED`  
Authoring agent: `gpt56-synthesis-01-p`, integrated by `gpt56-synthesis-01`  
Reviewing agents: none yet  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: `L-9816`; exact diagonal coefficients and complement pairing  
Scope: reduced period-four residual order `L=p^k` with odd `p` and remainder `s<p`  
Related counterexample candidates: none

## Definitions

Use the normalized period-four residual variables of `L-9816`.  Thus an
eligible root order is `d=gL`, where

\[
g=\gcd(d,a),
\qquad
L=\frac d g,
\qquad
U=T^g,
\qquad
a_g=\frac ag,
\qquad
\zeta_g=\frac\zeta g,
\tag{1}
\]

with `(a_g,L)=1`.  Put `s=D mod L`.  For `r=4`, the reduced residual is

\[
R_{g,L,s}(U)
=
\sum_{v=0}^s(-1)^v
U^{\zeta_gv+a_g\beta_s(v)}
{s\brack v}_{U^{a_g}},
\qquad
\beta_s(v)=\frac{-3v^2+(8s-5)v}{2}.
\tag{2}
\]

Throughout this claim we retain the actual Padé parameter range

\[
a_g>0,
\qquad
\zeta_g>0.
\tag{2a}
\]

When `s` is odd, define

\[
C_{g,s}=\zeta_g+\frac{5a_g}{2}(s-1).
\tag{3}
\]

Then `s>=1` and

\[
C_{g,s}\ge\zeta_g>0.
\tag{3a}
\]

## Statement

Let the reduced order be

\[
L=p^k,
\qquad
p\text{ odd},
\qquad
k\ge2,
\qquad
0\le s<p.
\tag{4}
\]

The restriction `k>=2` is deliberate.  The prime case `k=1` is already
classified by `L-9816/(20h)--(20i)`.

If `xi` is a primitive `p^k`-th root, then

\[
\boxed{
R_{g,p^k,s}(\xi)=0
\iff
s\text{ is odd and }p^k\mid C_{g,s}.
}
\tag{5}
\]

In the vanishing case the residual cyclotomic factor is exactly simple:

\[
\boxed{
\operatorname{ord}_{\Phi_{p^k}(U)}R_{g,p^k,s}(U)=1.
}
\tag{6}
\]

Equivalently, every genuinely non-antisymmetric odd-prime-power residual zero,
and every higher odd-prime-power residual multiplicity, is confined to the
large-remainder frontier

\[
\boxed{p\le s<p^k.}
\tag{7}
\]

This is a residual-polynomial theorem.  It does not identify residual
multiplicity with excess multiplicity of the full common gcd `gcd(A,B)`.

## Proof

Write `s=2u` or `s=2u+1`.  The exact diagonal formulas of `L-9816`, applied
to the reduced parameters, give

\[
\left.
\frac{R_{g,p^k,2u}(U)}{(U-1)^u}
\right|_{U=1}
=
\frac{(2u)!(-4a_g)^u}{2^uu!},
\tag{8}
\]

and

\[
\left.
\frac{R_{g,p^k,2u+1}(U)}{(U-1)^{u+1}}
\right|_{U=1}
=
-\frac{(2u+1)!(-4a_g)^u}{2^uu!}C_{g,2u+1}.
\tag{9}
\]

Because `s<p` and `(a_g,p)=1`, every factor in (8) is a `p`-adic unit.  If
`Phi_(p^k)` divided an even residual, it would still divide the quotient after
removing `(U-1)^u`.  Evaluation at `U=1` would then make (8) divisible by

\[
\Phi_{p^k}(1)=p,
\]

a contradiction.  Thus no even `s<p` is exceptional.

Now suppose `s=2u+1`.  Complementing `v` to `s-v` in (2) gives the exact
summand ratio

\[
\frac{\operatorname{summand}(s-v)}
{\operatorname{summand}(v)}
=-U^{(s-2v)C_{g,s}}.
\tag{10}
\]

Pairing complementary summands therefore gives the formal factorization

\[
R_{g,p^k,s}(U)
=(1-U^{C_{g,s}})Q(U)
\qquad(Q\in\mathbb Z[U]).
\tag{11}
\]

The first factor has a simple zero at `U=1`, while the residual has exact
diagonal order `u+1`.  Hence `Q` has diagonal order `u`.  Dividing (9) by the
nonzero linear coefficient `-C_(g,s)` of `1-U^C`, justified by (3a), gives

\[
\left.
\frac{Q(U)}{(U-1)^u}
\right|_{U=1}
=
\frac{(2u+1)!(-4a_g)^u}{2^uu!},
\tag{12}
\]

up to sign.  This is a `p`-adic unit because `s<p`.

If `p^k` does not divide `C_(g,s)`, then `Phi_(p^k)` is coprime to the first
factor in (11).  Any residual zero would force `Phi_(p^k)|Q`, and after
removing `(U-1)^u`, evaluation at one would contradict (12) and
`Phi_(p^k)(1)=p`.  Conversely, if `p^k|C_(g,s)`, then
`Phi_(p^k)|(1-U^C)`, so (11) gives the residual zero.  The factor
`1-U^C` is squarefree in characteristic zero, and the same unit argument
shows `Phi_(p^k)` does not divide `Q`.  Its residual multiplicity is therefore
exactly one.  This proves (5)--(6), and (7) is the contrapositive. ∎

## Motivation

`L-9828` shows that one exceptional copy at every reduced prime-power order
has only subquadratic total degree, but it deliberately leaves higher
multiplicity open.  This lemma proves the strongest possible local statement
on the entire small-remainder range: the only zeros are the known complement
factors, and they are simple.

## Dependency audit

- The normalization (1)--(2) is `L-9816/(20a)--(20b)`.
- Equations (8)--(9) are the exact diagonal leading coefficients, not an
  asymptotic expansion.
- Equation (11) is the formal complement pairing `L-9816/(20l)`.
- The only cyclotomic input is `Phi_(p^k)(1)=p` and the squarefreeness of
  `U^C-1` over characteristic zero.

## Gap audit

- The `p>s` odd-prime-power sector is completely classified and simple.
- The sector `p<=s<p^k` remains open; there the upper-half factorial in
  (8)--(12) contains a multiple of `p`, so evaluation at one loses its force.
- Powers of two are not covered.  In the actual period-four family their
  remainder satisfies `s=0 mod 4`, but a proof of nonvanishing is still open.
- Residual simplicity is not automatically a theorem about extra common-gcd
  multiplicity after the macro block derivatives are restored.

## Adversarial tests

- Positivity is essential to the simplicity statement.  If one leaves the
  project parameter range and allows `C_(g,s)=0`, (10) makes every
  complementary pair cancel identically; the residual is the zero polynomial,
  not a polynomial with one simple cyclotomic factor.
- The strict inequality `s<p` is essential to this proof.  Once `s>=p`, the
  quotient value (12) can be divisible by `p`, so `Phi_(p^k)(1)=p` gives no
  contradiction.
- The normalization by `g` is essential: the theorem concerns reduced order
  `p^k`, while the original cyclotomic factor has order `d=gp^k`.
- The hypothesis `k>=2` avoids duplicating the exact reduced-prime theorem in
  `L-9816`; no prime case is being omitted from the packet.
- Exact polynomial division for `L=9,25,27` agreed with (5)--(6); these checks
  were used only as an audit.

## Remaining uncertainty

The census suggests that (5)--(6) may hold throughout the large-remainder
range as well, but the present proof does not control the `p`-divisible
upper-half factorial.  No such extension is claimed.

## Suggested next attack

For `p<=s`, divide the coefficient blocks of `L-9816/(20f)` by the forced
complement factor when `s` is odd, then work in the relative cyclotomic tower
`Q(zeta_(p^k))/Q(zeta_(p^(k-1)))`.  The target is to replace the failed
evaluation-at-one unit by a relative trace or first nonzero Hasse derivative.
