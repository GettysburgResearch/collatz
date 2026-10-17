# L-0008 — Arbitrary-precision two-word atomic collision codes

Claim ID: `L-0008`  
Title: Explicit two-word weight-one collision codes of every prescribed 3-adic precision  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: `L-0005`, `L-0006`  
Scope: explicit finite parity codes with unbounded precision surplus  
Related counterexample candidates: none

## Statement

For every integer \(p\ge1\), define

\[
R_p=2\cdot3^{p-1},
\qquad
L_p=R_p+1.
\]

Let \(e_j^{(L_p)}\) denote the length-\(L_p\) parity word with one `1` in chronological position \(j\) and zeros elsewhere. Define

\[
V_p=\{e_0^{(L_p)},e_{R_p}^{(L_p)}\}.
\]

Then:

1. every word in \(V_p\) has weight one;
2. its affine constants are
   \[
   B(e_0)=1,
   \qquad
   B(e_{R_p})=2^{R_p};
   \]
3. the exact 3-adic valuation is
   \[
   \boxed{
   v_3(2^{R_p}-1)=p;
   }
   \tag{1}
   \]
4. therefore \(V_p\) is a two-word collision code of precision exactly \(p\), with surplus \(p-1\);
5. relative to \(e_0\), its normalized offset digit at denominator \(3^p\) is
   \[
   \boxed{
   K_p=\frac{2^{R_p}-1}{3^p},
   }
   \tag{2}
   \]
   and \(K_p\) is odd.

Thus fixed-weight collision codes exist with arbitrarily large precision surplus.

## Proof

For a weight-one word whose unique `1` occurs at position \(j\), the affine constant is \(2^j\). Hence the two constants are \(1\) and \(2^{R_p}\).

Because \(R_p=2\cdot3^{p-1}\), the lifting-the-exponent identity gives

\[
\begin{aligned}
v_3(2^{R_p}-1)
&=v_3(2^2-1)+v_3(3^{p-1})\\
&=1+(p-1)=p.
\end{aligned}
\]

For completeness, this special case can also be proved inductively. If
\(x\equiv1\pmod{3^q}\) but \(x\not\equiv1\pmod{3^{q+1}}\), then

\[
x^3-1=(x-1)(x^2+x+1)
\]

and \(v_3(x^2+x+1)=1\), so cubing raises the valuation by exactly one. Starting from \(2^2-1=3\) proves (1).

It follows that the constants agree modulo \(3^p\) but not modulo \(3^{p+1}\), establishing exact precision. Since \(2^{R_p}-1\) is odd and the divisor \(3^p\) is odd, \(K_p\) is odd. ∎

## Significance

The code-composition law consumes precision when an independent prefix is attached. `L-0008` supplies an explicit reservoir of arbitrarily large precision, making repeated exact tensor amplification possible.

The code is intentionally elementary. Its role is not to provide dense geometry by itself, but to preserve and multiply a more useful base alphabet through `L-0007`.

## Gap audit

- The code length \(L_p=2\cdot3^{p-1}+1\) grows exponentially in the requested precision.
- The two offsets are very far apart; this code is a precision resource, not a vertically closed carry grammar.
- Infinite concatenation is neither used nor permitted. Every application in the repository remains finite.

## Adversarial tests

`X-0004` verifies (1) and (2) for \(1\le p\le8\), constructs explicit concatenated codes, and checks their exact precision.

## Suggested next attack

Search for shorter or larger codes at the same precision, but retain this family as a theorem-level fallback guaranteeing that precision can never be the fundamental obstruction to finite code composition.