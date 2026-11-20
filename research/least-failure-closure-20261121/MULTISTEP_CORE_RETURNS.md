# Bounded-length shifted-core returns have only the valuation-one degeneracy

**PROPOSED, with an explicit external S-unit dependency.** For a fixed
number of actual odd steps and fixed shifted cores at the two endpoints,
there are only finitely many paths containing a division exponent at least
two. The bound is uniform in both cores. The intermediate shifted cores
may be arbitrary.

The new ingredient is an exact nondegeneracy classification for the whole
path equation. Successively inspecting the least binary valuation forces
every division exponent to be one whenever a subsum vanishes. This extends
the one-transition SC1 argument from PR161 without assuming that the
intermediate states remain in a prescribed prime pool.

This is not a proof of unrestricted Collatz convergence, a bound on the
heights of the exceptional paths, or a bounded algorithm deciding all
ordinary orbits.

## Definitions and frozen source boundary

Use the positive odd map

\[
U(n)=\frac{3n+1}{2^{v_2(3n+1)}}.
\]

Fix a finite prime pool \(P\) containing 2 and 3, and write \(s=|P|\).
For a positive integer \(m\), let \(R_P(m)\) be the factor remaining after
all prime factors in \(P\) are removed. A shifted core of an odd state
\(n\) is \(R_P(n+1)\).

Fix \(r\ge1\) and one actual ordinary path

\[
n_0,n_1,\ldots,n_r,\qquad n_i=U(n_{i-1}).
\]

Put \(a_i=v_2(3n_{i-1}+1)\), \(A_0=0\),
\(A_i=a_1+\cdots+a_i\), and \(m_i=n_i+1\). Thus
\(0=A_0<A_1<\cdots<A_r\) and each \(m_i\) is a positive even integer.
A **defect** means \(a_i\ge2\).

The comparison source is PR161 at
`4a0536b587fc91ee0c7bb1b160c06dda16ddbf23`,
`research/source-rigidity-20261120/SHIFTED_CORE_TRANSITIONS.md`, SC1--SC3.
Its one-step argument and its distinction between a simple orbit and
repeated traversals of a cycle are retained. The theorem below is proved
directly rather than assuming its multistep extension.

The external input is J.-H. Evertse, *The number of solutions of
decomposable form equations*, Theorem 3, printed page 7:
[primary author-hosted PDF](https://pub.math.leidenuniv.nl/~evertsejh/95-decforms.pdf).
For an equation with \(d\) variables in the units for a set of \(S\)
places over \(\mathbb Q\), with arbitrary fixed nonzero rational
coefficients and no vanishing nonempty subsum, it bounds the number of
solutions by \((2^{35}d^2)^{d^3|S|}\). Here \(|S|=s+1\), including
the real place. This bounds solutions, not their heights.

## RU1. Exact path equation and all subsums

Unrolling the ordinary transitions gives

\[
2^{A_r}n_r
=3^r n_0+\sum_{i=0}^{r-1}3^{r-1-i}2^{A_i}.
\]

After shifting both endpoints and combining the \(i=0\) term with
\(-3^r\), this becomes

\[
\boxed{
3^r m_0
+\sum_{i=1}^{r-1}3^{r-1-i}2^{A_i}
+2^{A_r}-2^{A_r}m_r=2\,3^{r-1}.
}
\tag{1}
\]

Regard the left side as \(r+2\) signed summands: the initial positive
term, the \(r-1\) middle terms, the final positive power of two, and
the unique negative endpoint term.

**Theorem RU1.** A nonempty subsum of these \(r+2\) signed summands
vanishes if and only if

\[
a_1=a_2=\cdots=a_r=1.
\tag{2}
\]

In that case the unique vanishing subsum is
\(3^r m_0-2^{A_r}m_r\).

**Proof.** A zero subsum must contain the unique negative summand.
Its complementary terms are positive and sum to \(2\,3^{r-1}\)
by (1). The complement is nonempty because the full sum in (1) is
not zero. It cannot include the initial term: \(m_0\ge2\) gives
\(3^r m_0\ge6\,3^{r-1}>2\,3^{r-1}\).

Consequently some subset of

\[
\{3^{r-1-i}2^{A_i}:1\le i<r\}\ \cup\ \{2^{A_r}\}
\tag{3}
\]

must sum to \(2\,3^{r-1}\). The terms in (3) have strictly increasing
binary valuations \(A_1,\ldots,A_r\). Since the right side has
binary valuation one, the first term must be selected and \(A_1=1\).
For \(r=1\) the list has only its final term; the same argument directly
gives \(A_r=1\).

For \(r\ge2\), suppose the first \(j-1\) middle terms have been
selected and \(A_i=i\) for \(1\le i<j\). Subtracting them leaves

\[
2^j3^{r-j}.
\tag{4}
\]

For \(j<r\), the next available term has binary valuation
\(A_j\ge j\), and all later terms have strictly greater valuation.
The valuation of (4) therefore forces this next term to be selected
and \(A_j=j\). Subtracting it leaves \(2^{j+1}3^{r-j-1}\),
establishing the induction. At \(j=r\), the remaining equation is
\(2^{A_r}=2^r\), so the final term is selected and \(A_r=r\).
Thus every increment is one and every term in (3) is selected.

Conversely, an actual valuation-one step satisfies
\(m_i=3m_{i-1}/2\). Under (2),
\(2^{A_r}m_r=3^r m_0\), giving the asserted zero subsum.
The preceding argument shows that its complement must be all of (3),
so no other nonempty zero subsum is possible. QED.

The exact exception is necessary. For every \(r\ge1\) and \(t\ge0\),
the source \(n_0=2^{r+1}3^t-1\) has its first \(r\) exponents equal
to one, and both endpoint shifted cores are one. These provide infinitely
many paths if the defect hypothesis is removed.

## RU2. A uniform finite bound for a prescribed core pair

**Theorem RU2.** For fixed positive \(P\)-free integers \(q,q'\),
there are at most

\[
\boxed{
B_{s,r}=\bigl(2^{35}(r+2)^2\bigr)^{(r+2)^3(s+1)}
}
\tag{5}
\]

distinct ordinary \(r\)-step paths such that

\[
R_P(n_0+1)=q,\qquad R_P(n_r+1)=q',
\]

and at least one of their division exponents is at least two.
No restriction is imposed on any intermediate shifted core.

**Proof.** Write \(m_0=qu\) and \(m_r=q'v\), where \(u,v\)
are positive \(P\)-units. Dividing (1) by \(2\,3^{r-1}\) gives

\[
\frac{3q}{2}u
+\sum_{i=1}^{r-1}\frac{2^{A_i}}{2\,3^i}
+\frac{2^{A_r}}{2\,3^{r-1}}
-\frac{q'2^{A_r}v}{2\,3^{r-1}}=1.
\tag{6}
\]

Its \(r+2\) unit variables are

\[
\bigl(u,2^{A_1},\ldots,2^{A_{r-1}},2^{A_r},2^{A_r}v\bigr).
\tag{7}
\]

The primes dividing \(q,q'\) remain in the fixed coefficients; they
do not enlarge \(P\). RU1 verifies the required nonvanishing of every
nonempty subsum because the path contains a defect. Evertse's theorem
with \(r+2\) variables and \(s+1\) places therefore gives (5).

The encoding is injective: \(u\) recovers \(n_0=qu-1\), and the
displayed powers of two recover all \(A_i\). In particular distinct
ordinary source paths cannot have the same vector. Counting all
nondegenerate S-unit solutions is an upper bound even though most
solutions need not encode legal positive odd paths. QED.

For \(r=1\), (5) is exactly
\((9\,2^{35})^{27(s+1)}\), the SC1 constant. The advantage at larger
\(r\) is that only the two endpoint cores are prescribed.

## RU3. Short excursions outside a finite core set occur only finitely often

Fix a finite set \(Q\) of \(K\ge1\) shifted cores. An outside
excursion of length \(\ell\ge1\) is a segment

\[
n_a,n_{a+1},\ldots,n_b,\qquad b-a=\ell+1,
\]

whose two endpoint cores belong to \(Q\), while every interior
core is outside \(Q\). Its length counts those \(\ell\) outside
visits, not the total number of transitions.

A valuation-one transition preserves the shifted core because it
multiplies the shift by \(3/2\). The first edge of every outside
excursion is therefore a defect. By RU2, across all ordinary starting
values, the number of distinct such excursions of outside length at
most \(H\ge1\) is at most

\[
\boxed{
K^2\sum_{r=2}^{H+1} B_{s,r}.
}
\tag{8}
\]

Along one nonperiodic ordinary orbit, source states never repeat, so
its distinct excursions can be charged to this finite count. Hence,
if that orbit makes infinitely many outside excursions, their lengths
tend to infinity. This is stronger than merely saying the number of
outside visits is unbounded.

For the shifted \(\{2,3\}\)-smooth class, set \(P=\{2,3\}\),
\(Q=\{1\}\). Formula (8) supplies an explicit bound for the total
number of short excursions, with arbitrary shifted primes allowed
inside every one of them. Repeated laps of a hypothetical cycle are
not counted as distinct paths and cannot be excluded by this argument.

## Scope of the quantitative bound and verification

The bound (5) counts paths. It gives no numerical upper bound for
their initial values, their division exponents, or the last time at
which a short excursion might occur in a fixed orbit. It must not be
turned into an unproved finite height search.

The elementary RU1 proof concerns every positive ordinary path,
including paths with repeated states; nonperiodicity enters only when
RU3 counts different occurrences as different paths. The finite
checker reconstructs the whole path equation through literal shortcut
steps and checks all subsums on its selected finite domains. It
preserves the all-ones degeneracy as a negative control. It does not
reprove or compute the external S-unit theorem.

No comparison to the ordinary predecessor-depth theorem in PR146's
`MERSENNE_ODD_COST.md` is claimed as a new bound for that target. The
new application is arbitrary endpoint shifted cores with no condition
on the intermediate arithmetic. Whether an arbitrary orbit is forced
to spend sufficiently little time outside a core class remains open.
