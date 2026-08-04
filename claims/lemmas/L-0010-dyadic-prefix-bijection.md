# L-0010 — Fixed-weight prefixes encode every dyadic residue

Claim ID: `L-0010`  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Created: 2026-07-21  
Dependencies: `L-0001`

## Statement

Fix \(b\ge1\). For every binary vector

\[
x=(x_0,\ldots,x_{b-1})\in\{0,1\}^b,
\]

choose a binary word \(u_x\) of length \(2b\) and weight exactly \(b\) whose first \(b\) symbols are \(x\). For example, place exactly \(b-|x|\) additional ones in the last \(b\) positions.

Then the map

\[
F_b(x)=B(u_x)\pmod{2^b}
\]

is a bijection from \(\{0,1\}^b\) onto \(\mathbb Z/2^b\mathbb Z\), independently of how the compensating high-position ones are arranged.

## Proof

All words have total weight \(b\). Modulo \(2^b\), contributions from positions \(j\ge b\) vanish. Hence

\[
F_b(x)=\sum_{j=0}^{b-1}x_j2^j3^{b-c_j(x)}\pmod{2^b},
\]

where

\[
c_j(x)=x_0+\cdots+x_j.
\]

We prove injectivity by triangular recovery of the bits. Modulo \(2\), only the term \(j=0\) can contribute, and its coefficient is odd, so \(F_b(x)\bmod2\) determines \(x_0\).

Assume \(x_0,\ldots,x_{j-1}\) have been recovered. Reducing modulo \(2^{j+1}\), all terms with index larger than \(j\) vanish. The contribution of the already known lower positions is known. The remaining term is

\[
x_j2^j3^{b-c_j(x)}.
\]

If \(x_j=0\) it contributes zero; if \(x_j=1\), after division by \(2^j\) its coefficient is odd. Therefore the \(j\)-th binary digit of the residual uniquely determines \(x_j\).

Thus every bit vector is uniquely recoverable from \(F_b(x)\), so the map is injective. Domain and codomain both have cardinality \(2^b\), hence it is bijective. ∎

## Consequence

After any later suffix beginning at position \(2b\), the completed word's affine constant modulo \(2^b\) still retains this complete dyadic encoding up to multiplication by an odd unit.

## Limitations

This lemma concerns finite low-order geometry only. It does not enforce a common inverse signature; `L-0009` supplies that correction.
