# Completed first-hit grades on a primitive bounded cycle

Take a bounded least-disagreement cycle with odd states \(x_i\), \(x_0=s\), accelerated exponents \(a_i\in\{1,2\}\), fundamental odd period \(p\), shortcut period \(h\), and \(A_i=\sum_{l<i}a_l\). Its dyadic order gives \(\gcd(p,h)=1\). Both \(m_i=(x_i+1)/2\) and \(n_i=(x_i-1)/2\) are positive ordinary integers reaching one. Write \(H(y),K(y)\) for the actual shortcut clock and odd count through the **first** visit to one. All logarithms below are base two unless marked \(\ln\). [Ordinary floor and neighbors](../../astra-unconventional-20261126/cycle/GOOD_NEIGHBORS.md) · [Dyadic-order theorem](https://github.com/GettysburgResearch/collatz/blob/21bed7ac2b1b1bb4baf0f6cabd53f8b9dd11b58a/research/unconventional-20261126/adelic/DYADIC_CYCLE_ORDER.md)

## A permutation and two exact visit identities

Put \(F(2u)=3u,\ F(4v+1)=3v+1,\ F(4v+3)=3v+2\). This is the inverse of Collatz's original 1932 permutation. On the restricted ordinary cycle \(m_{i+1}=F(m_i)\), and no \(m_i\) is \(3\bmod4\). For \(a_i=1\), write \(x_i=4u_i-1\). Then
\[
 m_i=2u_i,\quad m_{i+1}=3u_i,\quad n_{i+1}=T(n_i).
\]
For \(a_i=2\), write \(x_i=8v_i+1\). Then
\[
 m_{i+1}=T^2(m_i)=3v_i+1,\qquad n_i=4v_i,\quad n_{i+1}=3v_i.
\]
The two sources \(u_i,v_i\) are individually below \(s\) for all large \(s\). For a one-edge \(6u_i-1\le(16s+7)/3\) bounds \(u_i\le(8s+5)/9\). For a two-edge the ceiling gives \(v_i\le(4s+1)/6\). The points \(3u_i,3v_i\) reach one by the actual neighboring trajectories. [Original permutation definition](https://www.ams.org/bookstore/pspdf/mbk-121-prev.pdf) · [Simons, 2022](https://doi.org/10.11648/j.ijtam.20220805.11)

For a good integer \(y\) let \(P(y)\) be the finite counting measure of all its departures before the first one. Brackets denote point masses and the index sets \(I_1,I_2\) indicate the two exponents. Telescoping the local paths separately in each consecutive coordinate gives the following identities of positive counting measures.
\[
\begin{split}
 \sum_{i\in I_1}(P(3u_i)-P(u_i))
     &=\sum_{i\in I_1}[2u_i]+\sum_{i\in I_2}([4v_i+1]+[6v_i+2]),\\
 \sum_{i\in I_2}(P(3v_i)-P(v_i))
     &=\sum_{i\in I_1}[2u_i-1]+\sum_{i\in I_2}([4v_i]+[2v_i]).
\end{split}
\]
The displayed nominal departures exceed one. Each right side has total mass \(h\). Its mass at odd inputs is \(|I_2|\) in the first row and \(|I_1|\) in the second. The pointwise identities hold simultaneously for every choice of an ordinary gate. They also follow by following \(3u_i\) to the next \(u\) through the intervening two-edges, and \(3v_i\) to the next \(v\) through the intervening one-edges.

## Exact grade capacity

Select
\[
 y_i=m_i\quad (i\in I_1),\qquad y_i=n_i\quad(i\in I_2).
\]
The upper-neighbor layer propagates directly across each two-edge and its blocks end at the one-edge phases. The lower-neighbor layer propagates directly across each one-edge and its blocks end at the two-edge phases. This selection takes one representative from every one of these \(p\) blocks. Define its completed pair and integer
\[
 (C_i,G_i)=(A_i+H(y_i),i+K(y_i)),\qquad B_i=pC_i-hG_i.
\]
If \(B_i=B_j\), coprimality gives \((C_i-C_j,G_i-G_j)=t(h,p)\) for one integer \(t\). The equality has an ordinary interpretation. Follow the lower cycle to a selected marker, pass to its prescribed good neighbor, then follow that good orbit to its first one. Starting the smaller completed pair after an extra \(|t|\) true lower laps makes the two marked routes reach one at the same total clock and odd count. The change to the chosen neighbor at the marked position is an explicitly supplied operation. All the other steps are ordinary shortcuts. The two resulting affine maps of the common initial variable are identical, since their slopes and value at \(s\) agree.

Put \(\alpha=\log 3\), \(\delta=h-p\alpha\). The native product gives \(0<\delta\le p/(3s\ln2)\). On a partial lap put \(e_i=\sum_{l<i}\log(1+1/(3x_l))\in[0,\delta]\). Write \(d_i=\log\rho(y_i)\) with \(\rho(y)=2^{H(y)}/(3^{K(y)}y)\), and \(\sigma_i=1\) on \(I_1\), \(-1\) on \(I_2\). The two actual affine products give
\[
 B_i=p\bigl(\log(s/2)+\log(1+\sigma_i/x_i)+d_i+e_i\bigr)
                   -(K(y_i)+i)\delta .                                  \tag{1}
\]
For any chosen odd budget \(J\ge0\), let \(L\) count the indices with \(K(y_i)>J\). On the remaining indices let \(R\) count the number of representatives beyond the first one in each equal-\(B_i\) class. If \(d_i\le b\) on these remaining indices, integer spacing in (1) gives the finite bound
\[
 L+R\ \ge\ p-1-pb-p\log\frac{1+1/s}{1-1/s}-(J+2p)\delta.              \tag{2}
\]
Indeed all the low grades lie in one real interval of length at most the last three positive terms subtracted in (2). This form uses only the indicated real upper bound on measured residues.

For a uniform numerical consequence, import Nikzad, Frinkle and Bagherzadeh's finite-path bound \(\rho<4/3\). Their Hexagon preprint uses the height-delay record through \(28{,}019{,}077{,}177{,}231{,}758{,}495\), the residue record below \(2^{32}\), and a further exact count in Appendix 1D. We use the result as a source-qualified input. Its Hexagon identifier is distinct from the arXiv record with the same digits. [Nikzad, Frinkle and Bagherzadeh, Hexagon:2611.00033v1](https://hexagonmath.org/2611.00033v1)

Taking \(b=2-\alpha\) and \(J=s/10\) in (2) gives, along every unbounded sequence of bounded candidates,
\[
 L+R\ge\left(\log_2 3-1-\frac1{30\ln2}-o(1)\right)p >0.53p .
\]
Here \(p/s\to0\) follows from the earlier strip estimate and \(p\to\infty\) follows from the cycle product. If all selected completed pairs are in different grade classes, at least one good marker satisfies
\[
 K(y_i)\ge\bigl(3\ln2\,(\log_2 3-1)-o(1)\bigr)s .
\]
Its first-hit path is simple. The pointwise upper bound \(O(X^{39/40})\) on the number of states at most \(X\) on such a path then forces a peak \(\gg s^{40/39}\). Keeping only the \(|I_2|=h-p\) lower-neighbor blocks in the same calculation gives \(L+R>(0.12)p\) for \(J=s/10\) in that single layer. [Period bound for the bounded alternative](https://github.com/GettysburgResearch/collatz/blob/32d722c5d5597846da5dad842c8ea15742abc176/research/astra-fixed-target-closure-20261124/ordinary/HEIGHT_STRIP.md) · [Simple-path count](https://github.com/GettysburgResearch/collatz/blob/2978d84f8a1fda9083593b26c6bf724d5976d859/research/killed-green-head-closure-20261124/escape-analysis/README.md)

The grade equalities can occur across many different blocks on ordinary finite paths. For example the restricted initial run from \(27367\) has fourteen selected indices with the identical completed pair \((136,77)\). They occur at odd indices \(8,9,10,11,12,14,15,16,18,19,20,22,23,24\). Each marked route follows its actual good branch to its first one. This example is an ordinary transient prefix. The missing step is an upper bound on these equalities specific to the full bad cycle, or a contradiction from the large good first-hit budgets.

The Lean module checks the local actual shortcuts, circulation algebra, primitive grade relation, logarithmic-coordinate algebra over ordered rings, and finite integer capacity. The analytic path-product substitutions, numerical specialization, and imported small residue bound are written arguments. [Lean core](GradeMesh.lean) · [Compiler output](../../../reports/astra-six-hour-20261127/cycles/GradeMesh.lean.log)
