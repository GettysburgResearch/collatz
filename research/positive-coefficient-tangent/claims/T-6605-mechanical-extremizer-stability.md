# T-6605 — quantitative stability of the first-crossing mechanical extremizer

**Claim ID:** `T-6605`  
**Status:** **PROPOSED**  
**Authoring agent:** `gpt56-positive-tangent-01`  
**Created:** 2026-07-31  
**Dependencies:** elementary shortcut-Collatz affine algebra and the binary dominance/rightward-swap characterization  
**Scope:** all finite first-coefficient-crossing parity words  

## 1. Setup

Put

\[
\alpha={\log2\over\log3}.
\]

Let

\[
v=(v_0,\ldots,v_{j-1})\in\{0,1\}^j
\]

be a first coefficient-crossing word. Write

\[
S_m(v)=\sum_{r=0}^{m-1}v_r.
\]

Then

\[
S_m(v)\ge\lceil\alpha m\rceil
\qquad(1\le m<j),
\tag{1}
\]

and the final bit is even. Its total weight is the unique integer

\[
q=\lceil\alpha(j-1)\rceil=\lfloor\alpha j\rfloor.
\tag{2}
\]

Define the upper mechanical first-crossing word `w=w(j)` by

\[
S_m(w)=\lceil\alpha m\rceil
\quad(0\le m<j),
\qquad
S_j(w)=q.
\tag{3}
\]

Both words have the same length and weight, hence the same final coefficient

\[
C={3^q\over2^j}=e^{-\lambda},
\qquad
\lambda=j\log2-q\log3,
\qquad
{1\over2}\le C<1.
\tag{4}
\]

Let their exact affine maps be

\[
T_v^j(x)=Cx+E(v),
\qquad
T_w^j(x)=Cx+E(w).
\]

Put

\[
B(v)=\max_{0\le m<j}igl(S_m(v)-\alpha m\bigr)
\tag{5}
\]

and define the integrated prefix excess

\[
\boxed{
\mathcal I(v)
=
\sum_{m=1}^{j-1}
\left(S_m(v)-\lceil\alpha m\rceil\right).}
\tag{6}
\]

This is a nonnegative integer.

## 2. Exact swap distance

The dominance `(1)` and equal total weight imply that `v` can be transformed into `w` by rightward adjacent swaps

```text
10 -> 01.
```

Moreover, the minimum and monotone swap count is exactly

\[
\boxed{\mathcal I(v).}
\tag{7}
\]

One construction moves the ordered `1` positions of `v` rightward to the corresponding ordered `1` positions of `w`, beginning with the rightmost one. Every intermediate word still dominates `w` in prefix sums, and no intermediate prefix count exceeds the corresponding count of `v`.

## 3. Remainder gain of one swap

Consider one intermediate word and one swap at positions `t,t+1`.

After the common prefix, let the current ordinary value be `z`. The two local maps are

\[
T_{10}(z)={3z+1\over4},
\qquad
T_{01}(z)={3z+2\over4}.
\]

Thus `10 -> 01` increases the value after the pair by exactly `1/4`.

Let `C_{\rm suf}` be the multiplicative coefficient of the common suffix after the pair. The final affine remainder therefore increases by exactly

\[
{C_{\rm suf}\over4}.
\tag{8}
\]

For every monotone intermediate word, all proper-prefix coefficients are at least one, while its prefix bank is at most `B(v)`. Hence

\[
1\le C_{t+2}\le3^{B(v)}.
\]

The full coefficient is `C`, so

\[
C_{\rm suf}={C\over C_{t+2}}.
\]

Consequently every swap gain lies in the exact interval

\[
\boxed{
{C\over4\,3^{B(v)}}
\le
\Delta E_{\rm swap}
\le
{C\over4}
< {1\over4}.}
\tag{9}
\]

The upper estimate `1/4` also follows from `C_{t+2}>=1` and `C<1`.

## 4. Stability theorem

Summing `(9)` over the `I(v)` monotone swaps gives

\[
\boxed{
{C\over4\,3^{B(v)}}\,\mathcal I(v)
\le
E(w)-E(v)
<
{1\over4}\,\mathcal I(v).}
\tag{10}
\]

In particular, the mechanical maximizer is unique:

\[
E(v)=E(w)
\quad\Longleftrightarrow\quad
\mathcal I(v)=0
\quad\Longleftrightarrow\quad
v=w.
\]

This strengthens the qualitative adjacent-swap extremizer by quantifying the complete loss from every admissible displacement.

## 5. No-descent swap budget

Suppose a positive ordinary integer `n` follows `v` and does not descend at the crossing:

\[
T_v^j(n)\ge n.
\]

Then

\[
E(v)\ge n(1-C).
\]

Combining this with `(10)` yields

\[
\boxed{
\mathcal I(v)
\le
{4\,3^{B(v)}\over C}
\left(E(w)-n(1-C)\right).}
\tag{11}
\]

Because `C>=1/2`, the simpler bound is

\[
\boxed{
\mathcal I(v)
\le
8\,3^{B(v)}
\left(E(w)-n(1-C)\right).}
\tag{12}
\]

The right side must be nonnegative. Therefore:

1. if
   \[
   E(w)<n(1-C),
   \]
   no admissible word with this `(j,q)` can avoid descent;
2. if
   \[
   0\le E(w)-n(1-C)< {C\over4\,3^{B(v)}},
   \]
   then `I(v)=0`, so the only possible no-descent word is the mechanical word itself;
3. more generally, any small positive mechanical margin allows only finitely many adjacent-displacement units.

## 6. Canonical-cylinder form

Let `r^+(v)` be the least positive representative of the parity cylinder of `v`. If the canonical descent target fails, take `n=r^+(v)` in `(11)`.

Thus every canonical first-crossing target failure lies inside an explicit swap ball around the mechanical extremizer:

\[
\boxed{
\mathcal I(v)
\le
{4\,3^{B(v)}\over C}
\left(E(w)-r^+(v)(1-C)\right).}
\tag{13}
\]

This directly couples the three quantities that were previously controlled separately:

```text
mechanical remainder envelope;
ordinary canonical residue;
coefficient-bank / symbolic displacement.
```

## 7. Relation to `T-6604`

`T-6604` says that recurrent target failures require an exceptionally small logarithmic gap unless the bank is large.

`T-6605` says that target failures with little remaining affine margin must be near-mechanical in integrated swap distance.

Together they give the following offense:

```text
large margin:
  attack it by the exact return-gap inequality;

small margin:
  force a small swap ball around the recurrent mechanical word,
  then recover a long repeated factor and apply T-6604.
```

The final recovery of a sufficiently long repeated factor from a quantitative swap budget is not yet proved uniformly and remains the next combinatorial target.

## 8. Gap audit

- The theorem does not by itself bound the mechanical margin.
- A large bank weakens the per-swap lower cost.
- A word can have small normalized swap distance while strategically placing its edits; a uniform long-return theorem for such perturbations is still required.
- Positive cycles remain a separate repeated-state alternative.
- No proof of the universal canonical descent inequality or of Collatz is claimed.
