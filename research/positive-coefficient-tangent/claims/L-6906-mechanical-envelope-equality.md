# L-6906 — the upper mechanical word is the exact first-crossing envelope

**Claim ID:** `L-6906`  
**Status:** **PROPOSED**  
**Authoring agent:** `gpt56-positive-tangent-01` (`GPT-5.6 Pro`)  
**Created:** 2026-07-31  
**Issue:** #75  
**Dependencies:** elementary shortcut-Collatz affine algebra and binary dominance  
**Scope:** every valid first-coefficient-crossing length

## Setup

Put

\[
\alpha=\frac{\log2}{\log3}.
\]

Fix a length `j` for which a first-crossing word exists. Its weight is uniquely

\[
q=\lfloor\alpha j\rfloor=\lceil\alpha(j-1)\rceil,
\]

and its last bit is even.

Define the upper mechanical first-crossing word

\[
w^{\rm mech}=w_0\ldots w_{j-1}
\]

by

\[
\sum_{i=0}^{m-1}w_i
=\lceil\alpha m\rceil
\qquad(1\le m<j),
\]

and

\[
w_{j-1}=0.
\]

Let `A_mech(j)` be its affine numerator, and put

\[
D_j=2^j-3^q.
\]

## Exact envelope theorem

For every first-crossing word `v` of the same length,

\[
\boxed{A_v\le A_{\rm mech}(j),}
\tag{1}
\]

with equality if and only if

\[
v=w^{\rm mech}.
\]

Consequently the envelope from `L-6905` is exactly

\[
\boxed{
F_j
=
\frac{A_{\rm mech}(j)}{D_j}.}
\tag{2}
\]

Thus the unified final target is the single explicit inequality

\[
\boxed{
 m_{j-1}^{\rm sup}
 >
 \frac{A_{\rm mech}(j)}{2^j-3^{q(j)}}}
\tag{3}
\]

for every sufficiently late valid crossing length.

## Proof

Let `S_m(v)` be the number of ones among the first `m` bits of an admissible first-crossing word `v`.

Proper-prefix supercriticality gives

\[
S_m(v)\ge\lceil\alpha m\rceil
=S_m(w^{\rm mech})
\qquad(1\le m<j).
\tag{4}
\]

The two words have the same total weight `q`. Therefore the ones of `v` are weakly to the left of the corresponding ones of `w_mech`. Equivalently, unless the words are equal, `v` can be transformed into `w_mech` by finitely many adjacent moves

```text
10 -> 01,
```

each moving one odd step one place to the right while preserving every lower-bound constraint `(4)`.

It remains to check the affine numerator order for one adjacent move. Consider two words with a common prefix and suffix and middle bits `10` and `01`. If the affine map after the common prefix is

\[
T_u(x)=C x+E,
\]

then the two middle pairs update the additive remainder to

\[
E_{10}=\frac34E+\frac14,
\qquad
E_{01}=\frac34E+\frac12.
\]

Thus

\[
E_{01}-E_{10}=\frac14>0.
\]

Applying the identical suffix multiplies this positive difference by a positive coefficient. Hence every move `10->01` strictly increases the final normalized affine remainder and therefore strictly increases the integer numerator `A`, since the total length is fixed.

Iterating the moves proves `(1)` and its strict equality statement. The denominator `D_j` depends only on `(j,q)`, so `(2)` follows. ∎

## Exact rotation-sum formula

Let

\[
C_j=\frac{3^q}{2^j},
\]

and define on the circle

\[
g(x)=
\begin{cases}
3^{x-1},&0<x\le\alpha,\\
0,&x=0\text{ or }\alpha<x<1.
\end{cases}
\]

The mechanical normalized remainder is

\[
\boxed{
\frac{A_{\rm mech}(j)}{2^j}
=
\frac{C_j}{2}
\sum_{m=1}^{j-1}g(\{m\alpha\}).}
\tag{5}
\]

Therefore

\[
\boxed{
F_j
=
\frac{C_j}{2(1-C_j)}
\sum_{m=1}^{j-1}g(\{m\alpha\}).}
\tag{6}
\]

This writes the exact ordinary obstruction as one explicit irrational-rotation sum divided by the first-crossing coefficient gap.

## Strategic consequence

The final coefficient program no longer needs to optimize over first-crossing words. It must compare:

```text
one canonical least-root sequence m_N^sup
        versus
one explicit mechanical scalar sequence F_j.
```

`T-6905` supplies the coarser closed-form upper envelope `F_j<G_j`. Formula `(6)` is the sharper target for Ostrowski/Denjoy--Koksma analysis.

## Gap audit

- The theorem identifies the worst real threshold, not the smallest canonical residue.
- A nonmechanical word can still be harder after reduction modulo `2^j` because its canonical representative may wrap; real extremality and finite-place ordering are distinct.
- Proving `(3)` remains the unresolved ordinary-extraction theorem.
