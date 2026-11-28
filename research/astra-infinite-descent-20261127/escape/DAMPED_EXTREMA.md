# Source damping and maximal balanced classes

**Unconditional written result.** In the fair exact first-arrival row, multiply the contribution of source \(z\) by any fixed \(\phi(z)\in(0,1]\) tending to zero as \(z\to\infty\), however slowly. All targets, grades and physical clocks then admit a uniform source cutoff by a finite affine count alone. If an escaping component exists, the limiting largest damped row is attained by a finite balanced class, and beyond a finite grade the maxima come from just the finitely many maximizing classes. This statement does not use the fixed-root closed-support hypotheses used for the [undamped extremal classes](EXTREMAL_ROWS.md).

For \(A=A_{d,m}(y)\) put \(h=3^d2^{-m}/y\) and
\[
       B^\phi_{d,m}(y)=h\sum_{z\in A}\phi(z).
\]
Since \(hz\le1\), every source satisfies \(1\le z\le1/h\), and \(h|A|\le1\). The subrow restricted to \(z>R\) therefore has weight at most \(\sup_{z>R}\phi(z)\). This is the announced unconditional cutoff. Let \(F(z)\) be the product of the odd correction factors on an escaping orbit and \(P(z)=z/F(z)\). The [elementary simple-path estimate](HIGH_TARGET_ROWS.md) gives the absolute floor \(F(z)\ge c>0\).

For any escaping balanced class \(G\), members have the same \(P(G)\) and satisfy \(z\le P(G)\), hence the class is finite. Set
\[
       b_\phi(G)=P(G)^{-1}\sum_{z\in G}\phi(z).
\]
Following every member to one sufficiently late common target shows that a class disjoint from \([1,R]\) has mass at most \(\sup_{z>R}\phi(z)\). Thus for every threshold there are only finitely many classes above it. At a nonperiodic target each genuine row in its escaping component is a balanced class intersected with its set of ancestors, as proved in the [undamped argument](EXTREMAL_ROWS.md). Replacing \(|G|\) by \(\sum_{z\in G}\phi(z)\) in its finite selection proof gives
\[
       \lim_{d\to\infty}\sup_{m,y} B^\phi_{d,m}(y)
          =M_\phi:=\sup_{\rm escaping\ classes} b_\phi(G),             \tag{1}
\]
with value zero if every orbit is bounded. If any orbit escapes, this is a positive maximum. Beyond a finite grade the exact value is
\[
       M_\phi\max_{G:\,b_\phi(G)=M_\phi}1/F(y_G(d)),
\]
so the maxima decrease strictly to \(M_\phi\). Indeed the mass of any class below \(cM_\phi/2\) cannot supply a contender, the other classes are finite in number, and the bounded-orbit targets contribute uniformly less than \(M_\phi/2\) eventually by the elementary source cutoff. These assertions apply for example to \(\phi(z)=(1+\log z)^{-\eta}\) at every fixed \(\eta>0\).

## Inverse and forward power inequalities

For \(\phi_s(z)=z^{-s}\), \(s>0\), denote \(B_s(G)=\sum_{x\in G}x^{-s}\) and \(M_s=\sup_G B_s(G)/P(G)\). Take a maximizing \(G_s\). For a shortcut clock \(m\), grade \(d\), \(\omega=3^d2^{-m}\), let \(I=\{z:T^m z\in G_s,\ O_m(z)=d\}\) and \(J=\{T^m x:x\in G_s,\ O_m(x)=d\}\), counting distinct integers in both sets. An initial or final even coast is included in the physical clock. The same balanced-class transfer as before gives
\[
        \omega\sum_{z\in I}z^{-s}\le B_s(G_s),\qquad
        \sum_{y\in J}y^{-s}\le \omega B_s(G_s).                        \tag{2}
\]
For the one-step forward-even word the image has weight \(2^s\) times the input weights of even members. Their share in \(B_s(G_s)\) is at most \(2^{-1-s}\). At one inverse odd step, an endpoint \(y\equiv2\bmod3\) has source \((2y-1)/3<2y/3\). The \(B_s\)-share of these endpoints, when nonempty, is strictly less than \((2/3)^{1+s}\). More generally the first inequality in (2) tests each actual incoming row, with the true affine additive terms retained.

As \(s\downarrow0\), \(M_s\) increases to \(\sup_G |G|/P(G)\) without a compactness assumption at \(s=0\): fix a class, take its finite sum limit and then take the supremum. Exchanging this limit with the full undamped large-grade row maximum still requires a separate argument. If an escaping orbit exists and \(N\) is the least positive escaping integer, the class of \(N\) is the unique maximizing class for every sufficiently large \(s\). Its mass is at least \(N^{-s}/P(N)\), while every other class has mass at most \((N+1)^{-s}\) since \(|G|\le P(G)\). In particular taking all large powers focuses the inequalities on the minimum itself.

## One true convergent family satisfies every power test through a prescribed horizon

Let the horizon \(L\ge1\) and family size \(W\ge1\) be fixed. Choose starts
\[
     x_j=A+j6^L,\quad 0\le j<W,\qquad
     A\equiv-1\bmod 2^L,\qquad A\equiv1\bmod 3^L.
\]
The [unconditional synchronized-pattern theorem](../merger/FINITE_BLOCKS.md) supplies arbitrarily high such \(A\) for which all these starts first reach 1 at one later grade and physical clock. For **every** \(s\ge0\) simultaneously, \(G=\{x_j\}\) satisfies (2) for every \(m\le L\) and every \(d\).

The first \(L\) shortcut inputs of every source are odd: \(T^k x_j+1=3^k(x_j+1)/2^k\) through that duration. Thus the only nonempty forward row at \(m\) has \(d=m\), \(\omega=(3/2)^m\ge1\), and forward images at least their corresponding starts. The forward inequality follows. For the inverse inequality, the admissibility of each parity word of grade \(d\) depends only on the endpoint modulo \(3^d\). Every \(x_j\) admits precisely the words ending at the ordinary positive endpoint 1. A word legal at 1 has a positive integer source \(n\le1/\omega\); hence \(\omega\le1\), and the number of such words is at most \(1/\omega\). At endpoint \(x_j\) the same inverse word has source \(n+(x_j-1)/\omega\ge x_j\) by the affine formula. Its damped weight is therefore at most \(x_j^{-s}\). After summing over words and then endpoints, \(\omega\sum_{z\in I}z^{-s}\le B_s(G)\). Empty inverse rows need no test. This argument works for every nonincreasing positive damping function as well.

The finite construction satisfies simultaneous true coalescence, the whole tested collection of exact physical rows and all positive powers. Genuine infinite-horizon maximality still encodes the forward orbit problem. None of these extrema alone supplies a strict loss that excludes every actual escaping class.

