# Independent review of the renewal and sibling calculation

Reviewed: RENEWAL_TRANSPORT.md, especially Sections 3--5.
Date: 2026-11-22.

**Result: no blocking mathematical error found in the new diagonal
comparison or either self-contained coding proof.** This review checks
the displayed deductions. It does not independently certify the upstream
population theorem or claim a new proof of the classical Goldie and
Brofferio imports.

## Exact ordinary source comparison

The chronological reversal is correct:
\[
f_{e_1}\circ\cdots\circ f_{e_r}(x)=B_r+A_rx,
\qquad
A_r=3^r/2^{e_1+\cdots+e_r}.
\]
For a positive odd compatible target, reversing the word produces
positive odd integer sources, with the specified exact valuations.
The possible nonunit occurs only at the oldest source, because every
subsequent odd image is a ternary unit. If the target is nonperiodic,
every preceding source is nonperiodic as well.

Consequently the added factor \(3/4\) in \(\delta'=3\delta/4\) is a
valid lower bound for the possible oldest nonunit. The ratio of the two
contributions from the same word is exactly
\[
\frac{\omega_r(x)Q(x)}{\omega_r(x)^2}
=\frac{xQ(x)}{q\Lambda_r(x)}.
\]
This proves the stated diagonal comparison once the quoted Goldie bounds
and path-product bound are supplied. The conditional prefix likelihood
is likewise exactly \(Q(x)/(\omega_r(x)Q(q))\).

The moving-source test retains \(p\) at depth \(k\), with
\(\omega_k(p)=q_k\Lambda_k(p)/p\); no extra height factor is lost.
The cases \(r<k\), \(r=k\), and \(r>k\) are correctly distinguished.

## Joint coding

For \(D_r=d\), the numerator \(C_r\) lies in a fixed residue class
modulo \(3^r\). The half-open interval in equation (17) has length one
after division by \(3^r\), and therefore selects at most one member of
that residue class. Its endpoint convention is correct.

For \(r\ge2\),
\[
C_r-3^{r-1}
=2^{e_r}\left(3^{r-2}
 +3^{r-3}2^{e_{r-1}}+\cdots\right);
\]
the parenthesized integer is odd. This recovers \(e_r\) from its exact
2-adic valuation, and recursion recovers the earlier exponents. The
known total \(D_r\) recovers \(e_1\); the case \(r=1\) is immediate.

The real moment estimate
\[
\mathbb E R^\theta
\le\frac{1}{2^{1+\theta}-1-3^\theta}
\quad(0<\theta<1)
\]
follows by subadditivity and the geometric series for
\(\mathbb E A_j^\theta\). It supplies finite entropy of the auxiliary
integer part. The entropy bound on \(D_r\) is \(O(\log(r+1))\).

The exact identity
\[
H(e_1,\ldots,e_r\mid R,Z)=rH(e_1\mid R,Z)
\]
is valid: after conditioning on each known prefix, its inverse affine
map recovers the suffix boundary, whose law and exponent sequence are
independent of that prefix. Finite one-symbol entropy justifies the
conditional chain rule. The sublinear upper bound therefore forces
zero one-symbol conditional entropy and full almost-sure coding.

## Tilted coding and singular translates

For \(V_r=C_r/3^r\), reversal of the tilted iid increments gives
\[
\mathbb E_* V_r^\theta
\le\frac{3^{-\theta}}{1-m(1-\theta)}.
\]
Here \(m(1-\theta)<1\), so the auxiliary integer-part entropy is
uniformly bounded. The same numerator recovery and conditional chain
rule prove the tilted coding assertion without assuming finite-precision
information bounds from the cited manuscript.

Coding makes distinct first-symbol branch laws mutually singular. Since
\[
f_e=f_{e+6j}\circ B^j,
\]
injectivity of \(f_{e+6j}\) transports that singularity back to the
original boundary law and its \(B^j\) translate. This proves both
claimed singularities; it does not claim a failure of the narrower
ordinary arithmetic sibling estimate.

The later likelihood martingale uses \((B^{-j})_*\sigma\), with the
correct sign: its cylinder mass is
\(\sigma(B^j(z+3^r\mathbb Z_3))\). Singularity therefore gives zero
almost-sure likelihood limit. The claim that positive integers have
zero \(\sigma\)-mass also follows from coding: an atom would determine
an entire iid word of positive mass, whereas each length-\(r\) tilted
word has mass at most \((3/4)^r\).

No ordinary fixed-point trace or moving-target estimate has been inferred
from these almost-everywhere conclusions. The remaining identification
with the canonical obstacle \(V^{[r]}\) or harmonic function \(G\) is
explicitly left unproved in the reviewed note.
