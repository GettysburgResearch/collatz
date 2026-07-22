# L-9902 -- Term-count-binned ESS capacity and the growing-coordinate no-go

Claim ID: `L-9902`
Title: Quantitative S-unit bounds apply term-count bin by term-count bin and do not exclude one nondegenerate tuple at each increasing coordinate count
Status: `PROPOSED`
Authoring agent: `gpt56-synthesis-01-wave14-cap-cell-hierarchy`
Reviewing agents: `gpt56-synthesis-01`, `gpt56-synthesis-01-wave14-period-ten`
Created: 2026-07-22
Last updated: 2026-07-22
Dependencies: local `L-9901`, `T-9805`; Evertse--Schlickewei--Schmidt 2002, Theorem 1.1
Scope: normalized linear equations whose number of terms may vary
Related claims: local `T-9805`, `T-9828`; live PR #3 and PR #33

## 1. Term-count-binned quantitative bound

Let `K` be a field of characteristic zero, let
`c_1,...,c_n` belong to `K^times`, and let

\[
 \Gamma\le(K^\times)^n
\tag{1}
\]

be a subgroup of finite multiplicative rank `rho`.  Consider solutions
`y=(y_1,...,y_n)` in `Gamma` of the `n`-term equation

\[
 c_1y_1+\cdots+c_ny_n=1
\tag{2}
\]

Then Evertse--Schlickewei--Schmidt bounds the number of nondegenerate such
solutions by

\[
 \boxed{
 A(n,\rho)=\exp\!\left((6n)^{3n}(\rho+1)\right).}
\tag{3}
\]

Both the number `n` of terms and the common group `Gamma` are fixed in this
statement.

For each `n`, suppose a solution family `mathcal F_n` can be partitioned into
classes

\[
 \mathcal F_n
 =\bigsqcup_{\lambda\in\Lambda_n}\mathcal F_{n,\lambda},
\tag{4}
\]

where, within each class:

1. the coefficient vector

   \[
   (c_{n,\lambda,1},\ldots,c_{n,\lambda,n})
   \tag{5}
   \]

   is fixed;

2. all solutions lie in one common subgroup

   \[
   \Gamma_{n,\lambda}\subset(K^\times)^n
   \tag{6}
   \]

   of rank at most `rho_(n,lambda)`;

3. every solution is nondegenerate; and

4. the normalized solution vectors are distinct.

Then

\[
 \boxed{
 |\mathcal F_n|
 \le\sum_{\lambda\in\Lambda_n}
 \exp\!\left((6n)^{3n}(\rho_{n,\lambda}+1)\right).}
\tag{7}
\]

If

\[
 |\Lambda_n|\le K_n,
 \qquad
 \rho_{n,\lambda}\le R_n,
\tag{8}
\]

this simplifies to

\[
 \boxed{
 |\mathcal F_n|
 \le K_n\exp\!\left((6n)^{3n}(R_n+1)\right).}
\tag{9}
\]

For every finite set `I` of term counts,

\[
 \boxed{
 \sum_{n\in I}|\mathcal F_n|
 \le\sum_{n\in I}K_n
 \exp\!\left((6n)^{3n}(R_n+1)\right).}
\tag{10}
\]

Hence a rigorous growing-coordinate exclusion requires a finite collection of
term counts for which the claimed number of distinct solutions exceeds the
right side of (10).  In particular, it is sufficient that one term count `n`
occur more than the capacity in (9).

### Proof

Apply ESS separately to each fixed coefficient vector and common group in (4),
then sum the bounds.  The theorem supplies no relation between classes with
different dimensions, coefficient vectors, or ambient groups. **QED**

## 2. Necessary common-group qualification

It is not enough that each individual solution lie in some group of rank at
most `R_n`.  Every single vector lies in the cyclic group it generates.

The group in (6) must be common to all solutions being counted in that class.
Likewise, varying coefficients must be frozen or partitioned into explicitly
boundedly many coefficient classes.

This is exactly what `T-9805` does:

- `n=257` is fixed;
- the word gives at most `4^256` coefficient classes;
- each word class lies in one common group of rank at most `2s_N+1`; and
- a coordinate ratio proves distinctness.

Without those four ingredients, (3) cannot simply be summed over
trajectories.

## 3. Growing-coordinate counterexample

Let

\[
 S_0=\{2\}.
\tag{11}
\]

For every integer `n>=2`, define a primitive zero-sum tuple with `n+1`
coordinates by

\[
 a^{(n)}=
 \left(2^{n-1},-1,-2^1,-2^2,\ldots,-2^{n-2},-1\right).
\tag{12}
\]

Designate the first two coordinates as the two moving endpoints and the
remaining `n-1` coordinates as internal coordinates.  The identity

\[
 \sum_{j=1}^{n-2}2^j=2^{n-1}-2
\tag{13}
\]

gives

\[
 2^{n-1}-1-\sum_{j=1}^{n-2}2^j-1=0.
\tag{14}
\]

Thus:

- exactly one coordinate is positive;
- all other coordinates are strictly negative;
- no nonempty proper subsum vanishes;
- every coordinate is a `{2}`-unit;
- the gcd is one; and
- the raw height is

  \[
  H_n=2^{n-1}.
  \tag{15}
  \]

The two designated endpoints have

\[
 \operatorname{out}_{\{2\}}(2^{n-1})
 =\operatorname{out}_{\{2\}}(-1)=1.
\tag{16}
\]

Consequently the combined endpoint exponent is the minimum possible value,

\[
 \Theta=0,
 \qquad\gamma=0.
\tag{17}
\]

The endpoint ratio

\[
 {2^{n-1}\over-1}=-2^{n-1}
\tag{18}
\]

also separates every member numerically.  Nevertheless, the tuples live in
different projective spaces as `n` changes, so this ratio does not place them
under one fixed-dimensional theorem.

## 4. Exact ESS audit of the counterexample

Normalize (14) by its positive coordinate.  This gives the `n`-term equation

\[
 {1\over2^{n-1}}
 +\sum_{j=1}^{n-2}2^{j-(n-1)}
 +{1\over2^{n-1}}=1.
\tag{19}
\]

All terms are positive, so the solution is nondegenerate.

Let `x^(n)` in `(Q^times)^n` be the ordered vector of terms in (19), and take

\[
 \Gamma_n=\langle x^{(n)}\rangle.
\tag{20}
\]

This is a multiplicative group of rank one.  Therefore even the quantitative
theorem says only that the number of solutions at this fixed `n` is at most

\[
 A(n,1)=\exp\!\left(2(6n)^{3n}\right).
\tag{21}
\]

There is exactly one displayed solution, so `1<A(n,1)` and no contradiction
occurs.

The family therefore has simultaneously:

- one tuple for every growing coordinate count;
- fixed prime support;
- two fixed designated endpoints;
- endpoint budget exactly one;
- primitive gcd one;
- one-positive nondegeneracy;
- unbounded primitive height;
- an explicit separating ratio; and
- multiplicative-group rank one at every individual dimension.

Yet it is infinite because the equation length changes.

## 5. Unbounded subpower-gcd variant

To place the same example directly in the unbounded-gcd regime of `L-9901`,
multiply every coordinate in (12) by

\[
 G_n=2^{\lfloor\sqrt n\rfloor}.
\tag{22}
\]

The raw gcd becomes `G_n`, while

\[
 H_n=G_n2^{n-1}.
\tag{23}
\]

Hence

\[
 {\log G_n\over\log H_n}
 ={\lfloor\sqrt n\rfloor\over n-1+\lfloor\sqrt n\rfloor}
 \longrightarrow0.
\tag{24}
\]

Thus the gcd is unbounded but subpower: `gamma=0`.  All outside-`{2}`
contents remain one, so `Theta=0`, and primitive normalization recovers (12).
The growing-term-count family therefore survives even the strongest
`gamma=0,Theta=0` budget.

More generally, multiplying by

\[
 G_n=2^{\left\lfloor{\gamma_0\over1-\gamma_0}(n-1)\right\rfloor}
\tag{25}
\]

produces any prescribed `0<=gamma_0<1`, still with `Theta=0`.  The gcd is
unbounded when `0<gamma_0<1`; at `gamma_0=0`, (25) gives `G_n=1`.

## 6. Consequence for `L-9901`

The conclusion of `L-9901` cannot be extended by merely replacing its fixed
coordinate count with a sequence tending to infinity.  For every fixed `n`,
Evertse finiteness remains true.  The invalid inference is

\[
 \forall n,\quad|\mathcal F_n|<\infty
 \quad\not\Longrightarrow\quad
 \left|\bigcup_n\mathcal F_n\right|<\infty.
\tag{26}
\]

Small endpoint budget controls arithmetic height but not how many internal
`S_0`-unit terms are used.  Equation (12) exploits exactly this freedom by
splitting one power of two into an increasing number of powers of two.

## 7. Exact boundary of what survives

A growing-term-count argument is rigorous only with additional multiplicity data
such as

\[
 |\mathcal F_n|
 >K_n\exp\!\left((6n)^{3n}(R_n+1)\right)
\tag{27}
\]

for some fixed `n`, or a cumulative violation of (10) over a finite set of
term counts.

Useful separation must occur among solutions inside the same fixed-`n`,
fixed-coefficient, common-group class.  Separation between tuples in different
dimensions does not improve the ESS count.

The endpoint-budget hypotheses of `L-9901` alone do not imply common finite-
rank multiplicative groups for moving endpoints.  Therefore the quantitative
ESS result imported by `T-9805` is available only after an additional
factorization proving such common-group membership.

## Caveats

- The counterexample does not disprove any Evertse or ESS theorem; it supplies
  one permitted solution to each of infinitely many different equations.
- Characteristic zero in Section 1 is essential.  Over `K=F_p(t)`, the
  rank-one group generated by `(t,1-t)` contains the infinitely many
  nondegenerate solutions

  \[
  (t^{p^k},(1-t)^{p^k}),
  \qquad
  t^{p^k}+(1-t)^{p^k}=1,
  \tag{28}
  \]

  produced by Frobenius.
- Padding tuples with zero coordinates does not reduce them to one fixed
  dimension: ESS variables lie in `K^times`, and zeros also create degenerate
  subsums.
- Combining the internal coordinates into one coordinate changes its
  multiplicative support and is not a valid rank-preserving compression.
- A bounded coordinate count on an infinite subsequence restores the fixed-
  term-count argument.
- A quantitative theorem uniform in growing `n` would still need a summable or
  otherwise globally restrictive bound.  The imported estimate (3) grows
  rapidly with `n` and provides no such diagonal control.

## Suggested next attack

Before applying a quantitative S-unit theorem to a moving family, bin the
equations simultaneously by coordinate count, coefficient vector, and one
common multiplicative group.  A valid contradiction must overfill one of
those fixed-term-count bins; distinctness across dimensions alone has no counting
force.
