# Fixed-defect shifted-core returns, with arbitrarily long valuation-one runs

**PROPOSED, with the explicit Evertse S-unit dependency.** A fixed number
of defect transitions and fixed shifted cores at the two endpoints permit
only finitely many canonical ordinary segments, even when the number of
intermediate valuation-one steps is unbounded. A canonical segment begins
and ends with a defect. Excursions out of a prescribed core class meet this
condition automatically.

This is a stronger recurrence statement than a bound for fixed odd length.
It does not prove that an unrestricted orbit converges or bound the heights
of the finitely many exceptional segments.

## Notation

Use the positive odd map \(U(n)=(3n+1)/2^{v_2(3n+1)}\).
Let \(n_0,\ldots,n_r\) be an actual odd path, write
\(m_i=n_i+1\), \(a_i=v_2(3n_{i-1}+1)\), and
\(A_i=a_1+\cdots+a_i\), with \(A_0=0\).

Suppose there are exactly \(d\ge1\) defects, at positions

\[
1=i_1<i_2<\cdots<i_d=r,
\qquad a_{i_j}\ge2.
\tag{1}
\]

Every other \(a_i\) equals one. The equalities at the two ends of
(1) are the canonical-segment hypothesis. A fixed pool \(P\) of
\(s\) primes contains 2 and 3; shifted cores mean \(R_P(n+1)\).

The only external input is Evertse's Theorem 3, with the same arbitrary
fixed coefficients and \(s+1\) place convention stated in
`MULTISTEP_CORE_RETURNS.md`:
[primary PDF, printed page 7](https://pub.math.leidenuniv.nl/~evertsejh/95-decforms.pdf).

## FD1. Nondegeneracy survives compression by defect positions

The shifted recurrence is

\[
m_i=\frac{3}{2^{a_i}}m_{i-1}+1-2^{1-a_i}.
\tag{2}
\]

Its additive term vanishes precisely when \(a_i=1\). Define

\[
P_0=3^r m_0,\quad E=2^{A_r}m_r,\quad
P_j=3^{r-i_j}2^{A_{i_j}},\quad
Q_j=3^{r-i_j}2^{A_{i_j-1}+1}.
\]

Unrolling (2) gives the homogeneous equation

\[
\boxed{P_0+\sum_{j=1}^d(P_j-Q_j)-E=0.}
\tag{3}
\]

**Theorem FD1.** The \(2d+2\) signed summands in (3) have no proper
nonempty vanishing subsum.

**Proof.** The binary valuations of the correction terms are strictly
ordered:

\[
v_2(Q_1)<v_2(P_1)<v_2(Q_2)<v_2(P_2)<\cdots
<v_2(Q_d)<v_2(P_d).
\tag{4}
\]

The first inequality in each pair follows from the defect condition;
between pairs, \(A_{i_{j+1}-1}\ge A_{i_j}\). Also
\(v_2(E)\ge A_r+1>v_2(P_d)=A_r\). Because the first edge is a
defect, \(v_2(m_0)=1\), so the initial term has the same valuation
as \(Q_1\), namely one.

If a nonempty zero subsum omitted both \(P_0\) and \(-Q_1\),
its selected term of smallest binary valuation would be unique by
(4), which is impossible. Including exactly one of these two also
leaves a unique smallest valuation. Thus it includes both. Their sum
is

\[
P_0-Q_1=3^{r-1}2^{a_1}n_1,
\]

whose binary valuation is exactly \(a_1\), since \(n_1\) is odd.
The next available term of that valuation is \(P_1\); all later
terms have greater valuation. Hence \(P_1\) must be included too.

After the terms through \(P_j\) have been included, their sum is

\[
S_j=P_0+\sum_{t=1}^j(P_t-Q_t)
=3^{r-i_j}2^{A_{i_j}}m_{i_j}.
\tag{5}
\]

If \(j<d\), there are exactly
\(\ell=i_{j+1}-i_j-1\) valuation-one steps before the next defect.
Each reduces the binary valuation of the shift by one, so
\(v_2(m_{i_j})=\ell+1\). Consequently

\[
v_2(S_j)=A_{i_j}+\ell+1=v_2(Q_{j+1}).
\]

Every remaining term after \(Q_{j+1}\) has larger valuation.
Thus \(-Q_{j+1}\) is forced. The ordinary recurrence at that defect
then gives

\[
S_j-Q_{j+1}
=3^{r-i_{j+1}}2^{A_{i_{j+1}}}n_{i_{j+1}},
\]

of valuation exactly \(A_{i_{j+1}}\). Hence \(P_{j+1}\) is forced,
and (5) follows at the next index. Induction forces every correction
term. The resulting sum is \(E>0\); cancellation forces \(-E\)
as well. Only the whole set of summands can vanish. QED.

The proof uses the actual integer trajectory, especially the exact
valuation of the shifted state between successive defects. A formal
collection of signed units satisfying only selected size inequalities
would not justify (5) or this forced-cancellation argument.

## FD2. Uniform count independent of the intervening run lengths

**Theorem FD2.** Fix shifted endpoint cores \(q,q'\). Among all
canonical actual segments with exactly \(d\ge1\) defects and these
cores, the number of distinct segments is at most

\[
\boxed{
F_{s,d}=\bigl(2^{35}(2d+1)^2\bigr)^{(2d+1)^3(s+1)}.
}
\tag{6}
\]

The odd length \(r\), intermediate run lengths and intermediate
cores are unrestricted.

**Proof.** Write \(m_0=qu\), \(m_r=q'v\), with positive
\(P\)-units \(u,v\). Since \(i_1=1\),
\(Q_1=2\,3^{r-1}\). Move \(-Q_1\) to the other side of (3)
and divide by \(Q_1\):

\[
\frac{3q}{2}u
+\sum_{j=1}^d\frac{2^{A_{i_j}-1}}{3^{i_j-1}}
-\sum_{j=2}^d\frac{2^{A_{i_j-1}}}{3^{i_j-1}}
-q'\frac{2^{A_r-1}v}{3^{r-1}}=1.
\tag{7}
\]

This has exactly \(2d+1\) unit variables and fixed rational
coefficients \(3q/2\), signs \(\pm1\), and \(-q'\). Primes
in \(q,q'\) stay in the coefficients. Every nonempty zero subsum
of its left side would be a proper zero subsum in (3), so FD1 proves
nondegeneracy. Evertse's theorem gives (6).

The encoding is injective. Its first coordinate recovers
\(n_0=qu-1\). Each positive correction coordinate
\(2^{A_{i_j}-1}/3^{i_j-1}\) separately recovers \(i_j\) and
\(A_{i_j}\) by unique prime factorization. In particular the final
one recovers \(r=i_d\); the actual ordinary path is then fixed.
Thus distinct canonical segments cannot encode one unit vector. QED.

At \(d=1\), a canonical segment has only its one defect edge and
the bound is the original SC1 constant. Higher \(d\) allows any
number of valuation-one steps between defects.

## FD3. Arbitrary end runs and actual excursions

An arbitrary path containing exactly \(d\ge1\) defects can be
trimmed to a canonical segment by deleting its initial and terminal
valuation-one runs. These runs preserve shifted cores. Each canonical
segment admits only finitely many such extensions: if its first
shift is \(m\), a backwards valuation-one run has length at most
\(v_3(m)\); if its final shift is \(m'\), a forward valuation-one
run has length at most \(v_2(m')-1\).

Thus, for fixed endpoint cores and fixed \(d\), even all untrimmed
paths form a finite set. Formula (6) counts canonical segments only.
It is not a uniform bound on the number of their extensions, whose
finite multiplicities depend on the solution heights.

An excursion leaving a finite core set \(Q\) and returning for the
first time has both its first and last edges defective: valuation-one
steps preserve the core and cannot cross either boundary. Hence these
excursions are canonical. If \(|Q|=K\), the total number of distinct
excursions with at most \(D\ge1\) defects, across all ordinary source
values, is at most

\[
K^2\sum_{d=1}^D F_{s,d}.
\tag{8}
\]

Along one ordinary orbit with no repeated state (equivalently, an orbit
that is not eventually periodic), distinct excursion occurrences
have distinct initial states. Therefore the number of defects in its
successive completed excursions tends to infinity, whenever there
are infinitely many excursions. This strengthens the conclusion that
their odd lengths tend to infinity; long valuation-one runs cannot
be substituted for the increasing defect count.

Finite cycles cannot be excluded by counting their repeated laps as
different segments. No consequence here supplies an upper bound on
outside visits or proves that every required excursion returns.
