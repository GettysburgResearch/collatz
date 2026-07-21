# Notation and semantic conventions

Last updated: 2026-07-21  
Maintainer for this revision: `gpt56-pro-01`

This file fixes the conventions used by the active collision-rewrite packet.
Later work should state explicitly when it departs from them.

## Shortcut Collatz map

Throughout the current packet,

\[
T(n)=
\begin{cases}
n/2,&n\text{ even},\\[1mm]
(3n+1)/2,&n\text{ odd}.
\end{cases}
\]

This map has the same positive-integer termination question as the ordinary
Collatz map: the ordinary odd step \(3n+1\) is immediately followed by a
forced division by two.

Unless a claim says otherwise, all Collatz variables are ordinary nonnegative
or positive integers, not `2`-adic integers and not rational `2`-adic points.

## Parity words

A length-\(L\) parity word is written

\[
w=t_0t_1\cdots t_{L-1},
\qquad t_i\in\{0,1\},
\]

in **chronological order**. Thus \(t_0\) is the parity of the starting value,
and \(t_i\) is the parity immediately before the \((i+1)\)-st shortcut step.

Define

\[
a(w)=\sum_{i=0}^{L-1}t_i
\]

and

\[
B(w)=
\sum_{\substack{0\le j<L\\t_j=1}}
2^j3^{\sum_{i=j+1}^{L-1}t_i}.
\]

`L-0001` proves

\[
T^L(n)=\frac{3^{a(w)}n+B(w)}{2^L}
\]

for every integer following the word \(w\).

## Affine residue tables

For \(0\le r<2^L\), define

\[
a_L(r)=\#\{0\le t<L:T^t(r)\text{ is odd}\},
\]

\[
s_L(r)=T^L(r).
\]

Then

\[
T^L(2^Lq+r)=3^{a_L(r)}q+s_L(r)
\qquad(q\ge0).
\]

A collision fiber is a level set of

\[
r\longmapsto(a_L(r),s_L(r)).
\]

## Collision-fiber parameters

For a collision fiber of length \(L\) with \(a\) odd steps, write

\[
M=2^L,
\qquad N=3^a.
\]

The fiber is **supercritical** when

\[
N>M.
\]

Choose an anchor \(r\) and a finite digit set

\[
D\subseteq\{0,1,\ldots,M-1\}
\]

such that \(r+D\subseteq\{0,1,\ldots,M-1\}\) and

\[
T^L(Mq+r+d)=Nq+s
\qquad(q\ge0,\ d\in D).
\]

The canonical experimental anchor is \(r=\min F\), where \(F\) is the
untranslated fiber. Then \(0\in D\).

Define

\[
c=N-M,
\qquad \kappa=Ms-Nr,
\qquad h=s-r.
\]

The affine coordinate of `T-0002` is

\[
\Phi(n)=cn+\kappa.
\]

The induced partial radix map is

\[
H_D(MB+d)=NB+d,
\qquad d\in D.
\]

Its invariant lifting class is

\[
A\equiv h\pmod c,
\]

and the corresponding Collatz integer is

\[
\nu(A)=\frac{NA-\kappa}{c}.
\]

`T-0001` uses the older symbol \(d=Ms-Nr\) for the constant now denoted
\(\kappa\). New files use \(d\) for an actual digit.

## Digit constructors and word orientation

For radix \(M\), define

\[
L_d(x)=Mx+d,
\qquad0\le d<M.
\]

For radix \(N\), define

\[
R_c(x)=Nx+c,
\qquad0\le c<N.
\]

Strings are low-order first:

\[
L_{d_0}L_{d_1}\cdots L_{d_k}\#
=L_{d_0}(L_{d_1}(\cdots L_{d_k}(0)\cdots)).
\]

Thus the represented integer is

\[
d_0+Md_1+\cdots+M^kd_k.
\]

For a low-order-first word \(U=(u_0,\ldots,u_{k-1})\), write

\[
[U]_M=\sum_{i=0}^{k-1}u_iM^i.
\]

The mixed-radix normalization rule is

\[
R_cL_x\longrightarrow L_eR_q,
\qquad Nx+c=Mq+e,
\]

with \(0\le e<M\), \(0\le q<N\).

A closed carry path

\[
R_cX\longrightarrow ER_c
\]

is called a **carry macro-tile**. It may be repeated horizontally, but that
alone does not prove vertical closure of an induced orbit.

## Run-length skeleton

For a nonzero integer \(z\), define

\[
\operatorname{ord}_M(z)
=\max\{u\ge0:M^u\mid z\}.
\]

This is divisibility by powers of the whole radix \(M\), not the usual prime
valuation unless \(M\) itself is prime.

A maximal constant-digit phase begins at

\[
A=d+M^uC,
\qquad d\in D,
\qquad M\nmid C,
\]

and evolves as

\[
H_D^t(A)=d+N^tM^{u-t}C
\qquad(0\le t\le u).
\]

The sequence of triples \((d,u,C)\) is the **run-length skeleton** of the
induced orbit.

## Real and 2-adic conventions

For an induced orbit, put

\[
\rho=M/N,
\qquad\lambda=N/M.
\]

The series

\[
\frac{N-M}{N}\sum_{t\ge0}d_t\rho^t
\]

may be interpreted in both \(\mathbb Q_2\) and \(\mathbb R\). The coefficients
are the same, but the limiting identities are different. Claims must state the
topology being used.

## Finite words versus adic objects

A **finite canonical word** contains finitely many digits and a terminal marker
`#`. It represents one ordinary nonnegative integer.

A left-infinite or nonterminating digit string may represent an element of a
radix-adic completion. Compatibility of all finite suffixes does not imply that
the resulting object is an ordinary finite positive integer.

No candidate may be promoted to a Collatz counterexample unless it proves all
of the following:

1. the starting object is one finite positive integer;
2. every claimed rewrite step agrees with the deterministic Collatz trajectory;
3. the infinite argument never relies on an unproved infinite left tail;
4. integrality and positivity hold at every required boundary;
5. the trajectory avoids the known terminal cycle forever or is
   unbounded/nonperiodic as claimed.
