# T-6811 — The full first-crossing obstruction language is polynomially sparse but square-root rough

**Claim ID:** `T-6811`  
**Status:** **PROPOSED / SOURCE-DEPENDENT SYNTHESIS**  
**Agent:** `gpt56-positive-entropy-01` (`GPT-5.6 Pro`)  
**Issue:** #75  
**Date:** 2026-07-31  
**Dependencies:** PR #83 `T-6911`; local `T-6806`, `L-6811`, `T-6810`, `L-6812`, `L-6814`; the quoted effective logarithmic-form bound  
**Scope:** all nontrivial coefficient-first-crossing words with a positive non-descending ordinary realization

## 1. Exceptional language

For every valid first-crossing length `j`, let

\[
\mathcal E_j
\]

be the set of length-`j` parity words for which some positive ordinary
realization does not descend at the crossing.

The weight is the unique integer

\[
q=q(j)=\lfloor\alpha j\rfloor
=\lceil\alpha(j-1)\rceil,
\qquad
\alpha={\log2\over\log3},
\]

and put

\[
\lambda_j=j\log2-q\log3>0.
\]

The trivial word `10` at `j=2` is retained separately.

## 2. Exact family-cardinality ceiling

Corrected PR #83 `T-6911` proves the source-free bound

\[
\boxed{
|\mathcal E_j|
<
{j\over3(1-e^{-\lambda_j})}
\le
{2j\over3\lambda_j}.}
\tag{1}
\]

Indeed, every exceptional word has one least positive non-descending start,
different words have different starts, and every such start lies below the
right side of `(1)`.

If a reviewed effective logarithmic-form theorem gives

\[
\lambda_j\ge c_0j^{-\mu},
\tag{2}
\]

then

\[
\boxed{
|\mathcal E_j|
\le {2\over3c_0}j^{\mu+1}.}
\tag{3}
\]

Hence

\[
\boxed{
\limsup_{j\to\infty}
{1\over j}\log_2(1+|\mathcal E_j|)=0.}
\tag{4}
\]

The complete bad language has zero **family entropy**.

## 3. Every member has one short displacement

For every `w in E_j`, let `r_w` be its canonical source and put

\[
T^j(r_w)=r_w+d_w.
\]

`L-6812` gives

\[
\boxed{
0\le d_w<{q\over3}}
\tag{5}
\]

and the bilateral identities

\[
\boxed{
A_w
=(2^j-3^q)r_w+2^jd_w
=(2^j-3^q)(r_w+d_w)+3^qd_w.}
\tag{6}
\]

Thus every exceptional word is recovered from the polynomial-sized ordinary
source in `(1)` and one common displacement in the one-third window.

The cases are:

```text
d_w=0:
  canonical positive-cycle level;

d_w>0:
  acyclic canonical near-return.
```

`L-6814` proves that every nontrivial positive cycle produces some canonical
first-crossing member of `E_j`.  The cycle problem is therefore contained in
the same exceptional language rather than appended as a third lane.

## 4. Mechanical and no-wrap sectors

`T-6806` proves that every nontrivial upper-mechanical canonical member
descends, unless its finite segment already contains a nontrivial positive
cycle.  The latter possibility is already included in Section 3.

The exact wrap law on PR #83 proves that every no-wrap nonmechanical word is
easier to descend than the mechanical word.

Consequently every **acyclic** member of `E_j` is

\[
\boxed{
\text{nonmechanical and a genuine dyadic wrap.}}
\tag{7}
\]

## 5. Square-root internal roughness

For an acyclic member `v in E_j`, let `R(v)` be the number of odd positions
displaced from the upper-mechanical word.

`L-6811/T-6810` give the explicit source-qualified floor

\[
\boxed{
R(v)
\ge
\max\left\{
0,
\left\lfloor
{-A_j+\sqrt{A_j^2+2(\log_2 3)(j-2)}
 \over2\log_2 3}
\right\rfloor
\right\},}
\tag{8}
\]

where

\[
A_j=14.3\log_2j+1+\log_2(3/2).
\]

Therefore

\[
\boxed{
\liminf
{R(v_j)\over\sqrt{j}}
\ge
\sqrt{{\alpha\over2}}
=0.5615\ldots}
\tag{9}
\]

for every unbounded acyclic exceptional family.

Thus zero family entropy does **not** mean that the surviving words are small
repairs of the extremizer.  Each acyclic exceptional word must differ at
square-root many distinct odd positions.

## 6. Other mandatory geometry

Every unbounded acyclic exceptional family additionally satisfies the local
results:

\[
I_j
\ge
\left(\left({\alpha\over2}\right)^{2/3}-o(1)\right)j^{2/3}
\tag{10}
\]

for integrated displacement;

\[
\ell_{\rm mech}
\le(42.9+o(1))\log_2j
\tag{11}
\]

for initial agreement with the mechanical word; and

\[
\ell_{\rm self}
\le v_2(d_w)<\log_2(q/3)
\tag{12}
\]

for agreement with its own parity tail after the near-return.

Hence the remaining acyclic language is simultaneously:

```text
polynomially sparse across words;
short-description from its ordinary source;
nonmechanical and wrapped;
square-root-supported;
two-thirds-scale displaced;
early departing at both boundaries;
and governed by one 0<d<q/3.
```

## 7. Complete finite-place target

`L-6809` shows that membership in `E_j` is equivalent to one complete tuple:

```text
generalized-CRT-compatible local excess paths;
the unique physical monotone lift;
all proper first-crossing inequalities;
one common 0<=d<q/3;
every complete prime-power equation A == 3^q d;
the canonical positive source (A-2^j d)/(2^j-3^q).
```

For `d=0`, this contains the positive-cycle level.  For `d>0`, the tuple must
also obey the roughness and boundary constraints above.

Thus the unrestricted FC theorem is now exactly emptiness of this thin but
rough complete-tuple language, apart from the trivial word `10`.

## 8. Strategic interpretation

The synthesis rules out two misleading intuitions.

1. **The bad set is not a large random cloud.**  It has polynomial cardinality
   at each length, source-dependently.
2. **The bad set is not a sparse perturbative family.**  Every acyclic member
   has square-root-growing displaced support.

The surviving possibility is a polynomially sparse sequence of globally
coordinated, high-internal-complexity, complete-denominator cancellations.
The next theorem must attack that arithmetic coordination, not merely count
words or bound local edit number.

## 9. Gap audit

- Polynomial sparsity is not emptiness.
- Short description length does not imply low internal factor complexity.
- Square-root support does not force a residue miss modulo the complete
  denominator.
- The logarithmic-form constants and the all-length mechanical closure retain
  their source-qualified statuses.
- No proof of FC, SC, or Collatz is claimed.
