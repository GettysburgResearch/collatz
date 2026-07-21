# Notation and semantic conventions

Last updated: 2026-07-21  
Maintainer for this revision: `gpt56-pro-01`

This file fixes the conventions used by the first collision-rewrite contribution. Later work should state explicitly when it departs from them.

## Shortcut Collatz map

Throughout the current packet,

\[
T(n)=
\begin{cases}
n/2,&n\text{ even},\\[1mm]
(3n+1)/2,&n\text{ odd}.
\end{cases}
\]

This map has the same positive-integer termination question as the ordinary Collatz map: the ordinary odd step \(3n+1\) is immediately followed by a forced division by two.

Unless a claim says otherwise, all Collatz variables are ordinary nonnegative or positive integers, not 2-adic integers and not rational 2-adic points.

## Parity words

A length-\(L\) parity word is written

\[
w=t_0t_1\cdots t_{L-1},\qquad t_i\in\{0,1\},
\]

in **chronological order**. Thus \(t_0\) is the parity of the starting value, and \(t_i\) is the parity immediately before the \((i+1)\)-st shortcut step.

Define

\[
a(w)=\sum_{i=0}^{L-1}t_i.
\]

Define the affine constant

\[
B(w)=
\sum_{\substack{0\le j<L\\t_j=1}}
2^j3^{\sum_{i=j+1}^{L-1}t_i}.
\]

Claim `L-0001` proves that any integer following \(w\) satisfies

\[
T^L(n)=\frac{3^{a(w)}n+B(w)}{2^L}.
\]

## Collision-bundle parameters

For a bundle of length \(L\) with \(a\) odd steps, write

\[
M=2^L,\qquad N=3^a.
\]

The bundle is called **supercritical** when

\[
N>M.
\]

A width-\(m\) consecutive collision bundle has integers \(r,s\) such that

\[
T^L(Mq+r+j)=Nq+s
\]

for every \(q\ge0\) and every \(j\in\{0,\ldots,m-1\}\).

For such a bundle define

\[
c=N-M,\qquad d=Ms-Nr,\qquad h=s-r.
\]

The affine coordinate used in `T-0001` is

\[
\Phi(n)=cn+d.
\]

The induced partial radix map is

\[
H(MB+j)=NB+j,
\qquad j\in\{0,\ldots,m-1\}.
\]

## Digit constructors and word orientation

For a radix \(M\), define

\[
L_d(x)=Mx+d,
\qquad 0\le d<M.
\]

For a second radix \(N\), define

\[
R_c(x)=Nx+c,
\qquad 0\le c<N.
\]

Strings of constructors are read as function composition with the **leftmost digit least significant**:

\[
L_{d_0}L_{d_1}\cdots L_{d_k}\#
:=L_{d_0}(L_{d_1}(\cdots L_{d_k}(0)\cdots)).
\]

Thus the represented integer is

\[
d_0+Md_1+\cdots+M^kd_k.
\]

The mixed-radix normalization rule is

\[
R_cL_d\longrightarrow L_rR_q,
\qquad Nd+c=Mq+r,
\]

with \(0\le r<M\) and \(0\le q<N\).

## Finite words versus adic objects

A **finite canonical word** contains finitely many digits and a terminal marker `#`. It represents one ordinary nonnegative integer.

A left-infinite or non-terminating digit string may represent an element of a radix-adic completion. Compatibility of all finite suffixes does not imply that the resulting object is an ordinary finite positive integer.

No candidate may be promoted to a Collatz counterexample unless it proves all of the following:

1. the starting object is one finite positive integer;
2. every claimed rewrite step agrees with the deterministic Collatz trajectory;
3. the infinite argument never relies on an unproved infinite left tail;
4. integrality and positivity hold at every required boundary;
5. the trajectory avoids the known terminal cycle forever or is unbounded/nonperiodic as claimed.
