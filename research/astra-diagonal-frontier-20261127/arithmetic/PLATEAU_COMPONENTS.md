# How long one homogeneous component can survive a constant clock

Use the dyadic homogeneous ceiling \(H_N\) at odd cutoff \(N\) defined in [the ordinary upper-bundle theorem](UPPER_BUNDLE.md). All logarithms written \(\log\) are natural. A component here means the actual ordered cyclic list of distinct odd parts with its actual lifted raw edges, taken up to cyclic reindexing. Its period \(q\) need not equal the period of any given ordinary cycle.

## Exact birth and death and a finite count of persistent components

On an odd part \(n\) the raw edge equals \(3n+d_n\), where \(d_n\in\{0,1,3\}\). At any cutoff where a component \(R\) exists, put
\[
 M_R=\max R,\qquad
 B_R=\min\big(\{3n:n\in R,\ d_n=1\}
                      \cup\{(3n+1)/2:n\in R,\ d_n=3\}\big).
\]
The minimum is nonempty since all-exact tripling cannot close positively. Exactly the odd cutoffs in \([M_R,B_R)\) realize this specified component. For cutoffs down to \(M_R\) every used target is still eligible, and deletion of unused grid points cannot change the ceiling. Below \(M_R\) the component loses a vertex. For a \(+1\) edge the earliest newly eligible blocker is the odd raw triple \(3n\): a noninteger dyadic point in the skipped interval has odd numerator larger than \(6n\). For a \(+3\) edge, \(3n+1\) has dyadic order one since its odd part was ineligible where division by four would already have put it below the cutoff. The first blocker thus has odd part \((3n+1)/2\), smaller than the odd integer alternatives \(3n,3n+2\) and every noninteger alternative. Once a blocker is eligible it stays eligible. This proves the exact interval.

Suppose \(L,U\) are odd and \(U\ge(3L+1)/2\). Every component surviving all cuts from \(L\) through \(U\) uses only \(+0,+1\) edges, and every \(+1\) source lies in \((U/3,L]\). Write \(K\) for the number of these persistent components. They have a common rotation \(\theta\) and a common period \(q\), the reduced denominator of \(\theta\), by the order-preserving translation on each component. They are disjoint at \(L\). Their respective product identities give the exact upper bound
\[
  Kq(\theta-\log_2 3)\ \le\!
   \sum_{\substack{U/3<n\le L\\n\ \text{odd}}}
                   \log_2(1+1/(3n)).                                    \tag{1}
\]
Here every contributing correction is counted once on its actual component.

## An angular upper bound for a single persistent component

Consider \(L\to\infty\) and components that individually survive through \(U\) with \(U/L\to\kappa>3/2\). Then
\[
     3(\log2)^2 U(\theta-\log_2 3)\ \le\ 3-U/L+o(1).                   \tag{2}
\]
No individual component survives to \(U\ge3L\) by the exact blocker formula. To prove (2) one may therefore take \(3/2<\kappa\le3\). At each date, normalize the odd part \(n\) to its unique dyadic lift \(z\) in \((L/2,L]\). Its angle \(t=\log_2(z/L)\bmod1\) evolves by \(\log_2 3+O(1/L)\) on the circle: all nonzero corrections have \(n>U/3\). Every subsequential empirical angular limit is invariant under this irrational rotation, hence is Haar, by testing the Fourier characters. The underlying periods necessarily tend to infinity because the positive rotations converge to an irrational number.

A correcting source already lies in this one normalized octave. The indicator of its possible high interval \((U/3,L]\) has endpoints converging to fixed angles. Taylor expansion, Haar convergence and a fixed-mesh approximation at the two endpoints therefore give
\[
\begin{aligned}
  3\log2\ U(\theta-\log_2 3)
   &\le \frac1q\sum_{z\ \text{on the component}}
                 \mathbf1_{U/3<z\le L}\,\frac{U}{z}+o(1)\\
   &=\int_{U/3}^{L}\frac{U}{z}\,\frac{dz}{z\log2}+o(1)
     =\frac{3-U/L}{\log2}+o(1).
\end{aligned}
\]
The sum is over the \(q\) normalized actual vertices and includes each once. This proves (2) without asserting that the correcting vertices themselves have a uniform distribution inside the interval.

For comparison, every growing ordinary cycle of maximum odd state \(X\), minimum \(s\), and native clock \(\theta=A/p\) satisfies
\[
                3(\log2)^2 X(\theta-\log_2 3)\ge 1-o(1).                \tag{3}
\]
Indeed normalize its phases to \(z\in(X/2,X]\). One has \(1/x\ge1/z\); the increasing minima make \(\log(1+1/(3x))\ge(1-o(1))/(3x)\) uniformly. Angular equidistribution under the true \(\log_2 3+O(1/s)\) increments then gives \(p^{-1}\sum X/z\to1/\log2\).

Apply (2)–(3) when an individual reference component has this particular ordinary clock and survives from \(L\sim X/2\) to \(U\). If \(U/L\) stays above \(3/2\) by a fixed margin, (2)–(3) give \(U/X+U/L\le3+o(1)\), hence \(U\le X+o(X)\). If the ratio stays at or below \(3/2+o(1)\), the same upper bound is automatic. Subsequence extraction covers the general case. Thus a single unchanged component from the initial cut of the ordinary plateau cannot reach its final cutoff \(4s-1\) on any fixed width \(X/s\le R<4\). This is an upper bound on component persistence, **not** a lower bound of four for ordinary cycle width.

## A uniform restriction independent of any ordinary candidate

Let \(\mu_0=5.116201\). For the lifetime of **any** sequence of actual reference components with \(M_R\to\infty\),
\[
                      \limsup B_R/M_R\le3^{1-1/\mu_0}<2.421.              \tag{5}
\]
Moreover (2) has the strict improvement
\[
  3(\log2)^2 U(\theta-\log_2 3)
           \le 3-(U/L)(1+(\log2)/20)+o(1),                              \tag{6}
\]
on components persisting from \(L\) to \(U\) with limiting ratio greater than \(3/2\). Consequently the actual-clock component starting at \(L\sim X/2\) above has
\[
               U\le\left(\frac{3}{3+(\log2)/10}+o(1)\right)X
                  < (0.978+o(1))X.                                       \tag{7}
\]
These estimates use the published finite irrationality bound; they do not assume an irrationality measure of three.

Normalize the \(q\) distinct vertices to the integers \(Z_i\in(L/2,L]\). They are integers because their odd parts are at most \(L\). At a correcting source its representative already lies in this octave. Therefore the true normalized recurrence is
\[
           2^{b_i} Z_{i+1}=3Z_i+c_i,\qquad c_i\in\{0,1\},
\]
with \(c_i=1\) only if \(Z_i>U/3\). Order the distinct lifted vertices and extend their ranks by doubling after each \(q\) positions. Monotonicity and the primitive component give a translation by \(q\theta\) ranks. Thus the cumulative windings of the orbit starting at rank \(r\) are \(\lfloor r/q+j\theta\rfloor\) for \(0\le r<q\). The \(k\) possible correcting positions, meaning all physical ranks with \(Z>U/3\), form the last \(k\) ranks in this octave. For a length-\(h\) window, the winding calendar and allowed-site indicators \(a_i=\mathbf1_{Z_i>U/3}\) together have \(O(h+1)\) possible words across all origins. Their only cutpoints in the origin phase are the rotated endpoints \(0,1-k/q\) and the ordinary winding cuts. Endpoint singletons may be counted separately. By the angular equidistribution already established, \(k/q\to\eta=\log_2(3/\kappa)\).

Take \(h=\lceil\log_3(2L)\rceil+2\). The total winding \(B=\sum b_i\) on each window exceeds \(h\log_2 3-1\), so \(2^B>L\). If two starts have the same winding calendar and defects, subtraction of the iterated affine equations gives \(2^B\mid3^h(Z-Z')\). Thus they coincide. For a uniform origin, its entropy \(\log q\) is therefore at most the environment cost \(O(\log(h+1))\) plus the conditional entropy of the defect word. Write \(m\) for the fraction of all \(q\) dates at which \(a_i=1,c_i=0\) and \(t=k/q\). By stationarity and Shannon subadditivity, the last conditional entropy is at most \(ht H(m/t)\), where \(H(v)=-v\log v-(1-v)\log(1-v)\). Indeed conditioning just on the individual \(a_i\) leaves zero uncertainty at \(a_i=0\), and binary entropy \(H(m/t)\) otherwise.

Theorem 1 of Bondareva, Luchin and Salikhov gives \(q\theta\log2-q\log3\gg q^{-4.116201}\) for these unbounded integral log forms, whose two coefficients are comparable. Since \(\theta-\log_2 3=O(1/L)\), this implies \(\log q/\log L\ge1/\mu_0-o(1)\). The entropy argument now gives
\[
                   tH(m/t)\ge (\log3)/\mu_0-o(1).                        \tag{8}
\]
The left side is at most \(t\log2\). Substitution of \(t\to\log_2(3/\kappa)\) proves (5) by taking \(L=M_R, U=B_R-2\); subsequences with ratio at most \(3/2\) already obey the bound. The left side is also at most \(H(m)\) by conditioning. Since \(H(1/20)<(\log3)/\mu_0\), (8) forces \(m\ge1/20\) eventually. Each missed date on the high interval costs at least \(U/L\) in the right-hand angular average used for (2). Removing these dates yields (6), and combining with (3) gives (7). [Bondareva, Luchin and Salikhov, Theorem 1, p. 18](https://doi.org/10.22405/2226-8383-2018-19-1-15-25)

## The asymptotic lifetime factor is at most two

In fact every growing sequence of individual reference components satisfies the stronger unconditional bound
\[
                         \boxed{\limsup B_R/M_R\le2.}                     \tag{9}
\]
The proof uses order-six integer differences and the published exponent \(\mu_0<6\). It applies to the actual unchanged lifted edges of each component, with no ordinary cycle as input.

Suppose \(M=M_R\to\infty\), \(U=B_R-2\), and pass to a subsequence with \(U/M\to\kappa>2\). The exact lifetime bound gives \(\kappa\le3\). As in the previous section normalize the component to integers \(Z_r\in(M/2,M]\), now labeled by sorted spatial rank \(0\le r<q\). The raw normalized correction \(c_r\) is zero or one, and a one requires \(Z_r>U/3\). Extend both arrays to all integer ranks by doubling across each period. The exact lifted map gives \(Z_{r+A}=3Z_r+c_r\), where \(A=q\theta\), and
\[
 r'=(r+A)\bmod q,\qquad b=\lfloor(r+A)/q\rfloor\in\{1,2\}
\]
at fundamental ranks for sufficiently large \(M\). The sorted labels obey \(\log_2(2Z_r/M)=r/q+o(1)\) uniformly by angular Haar convergence and continuity of the limiting distribution. Write \(\alpha=\log_2(3/2)\), so \(A/q-1\to\alpha\).

Take the same spatial polynomial as in [the order-six width theorem](WIDTH_THREE.md):
\[
 P(T)=(T-1)^2(T^2-1)(T^3-1)(T^4-1)(T^5-1),\quad
 H_r=P(E)Z_r,\quad d_r=P(E)c_r.
\]
It has degree 16, positive coefficient mass six and negative mass minus six. Thus
\[
                         2^b H_{r'}=3H_r+d_r,\qquad |d_r|\le6.             \tag{10}
\]
The last bound holds on every unwrapped 17-position stencil. At a spatial seam the wrapped low fundamental ranks have size \((1/2+o(1))M<U/3\), so their doubled correction is zero. All other participating corrections are zero or one.

Every date of type \(b=1\) has \(r/q<2-A/q\) and consequently \(Z_r/M\le2/3+o(1)\). The same upper estimate holds for the following 16 spatial ranks since this interval is a fixed distance from the seam. Thus every member of this stencil has correction zero, by \(\kappa>2\). Each of its labels is even: its own native departure is an exact normalized tripling and its own winding is at least one. Hence on type-one rows \(d_r=0\) and \(2\mid H_r\).

If a chronological value \(H\) is zero, it generates the invariant
\[
                   |H|\le3\ \text{everywhere},\qquad |H|\le2
                         \ \text{at each type-one date}.
\]
Indeed a two-step from \(|H|\le3\) gives \(|4H'|\le15\), hence \(|H'|\le3\). A one-step from \(|H|\le2\) uses \(d=0\) and gives \(|2H'|\le6\). If the new date has type one, its evenness sharpens either bound to two. Induction covers the full chronological circuit.

Take a nonempty closed height interval in the open normalized interval \((2/3,\kappa/3)\), staying below one. Its interior corresponds to a fixed open spatial rank interval of positive length, with margins, by uniform angular convergence. All 17 labels starting on a slightly smaller such interval have \(Z/M>2/3\), hence individual winding two, and \(Z/M<U/(3M)\), hence correction zero. Their exact triples are all divisible by four. Thus \(4\mid H_r\) on this whole interval. Under the bounded invariant \(H_r\) must vanish there.

A fixed open spatial interval of zeros contradicts the sorted shape. Precisely, \(P\mid(T^{60}-1)^6\). On every interior subinterval the stride-sixty sixth difference vanishes. Multiply by \((1+E^{60}+\cdots+E^{60(t-1)})^6\) and choose \(60t/q\to c>0\) so small that every term stays in the interval. The resulting difference divided by \(M/2\) tends to \(2^{f_0}(2^c-1)^6>0\) at an interior start with \(r/q\to f_0\). This excludes the possibility of any zero.

Finally, nonzero consecutive values cannot change sign. A type-one step has zero correction; a type-two step from \(H\ge1\) gives \(4H'\ge-3\), and the symmetric inequality holds from \(H\le-1\). Therefore \(H\) is a nonzero integer of constant sign on the whole cycle. With \(P=(T-1)^6 B(T)\), the convolution identity
\[
     (E^t-1)^6B(E)Z=(1+E+\cdots+E^{t-1})^6H
\]
at rank zero with \(t=\lfloor(q-20)/6\rfloor\) gives \(t^6\le2^6\|B\|_1 M\). All terms on the left are fundamental and on the right all summands have that same sign. This forces \(M\gg q^6\), contradicting \(M\ll q^{5.116201}\) proved above. This proves (9).

The argument needs open clearance \(\kappa>2\). It supplies neither a strict factor below two nor any bound on the complete rotation plateau when its components can change. In the previous section the entropy-only bound (5) remains useful as an independent argument, and its missed-site refinement (6) gives the stricter ordinary-clock consequence (7).

## Quantitative replacements on the ordinary plateau

Fix \(2<R<4\) and suppose the growing ordinary cycles obey \(X/s\le R\). As \(N\) runs from the first odd cutoff at least \((X+1)/2\) through \(4s-1\), their explicit reference cycle undergoes at least
\[
                       (1-\log_2(R/2)-o(1))p                            \tag{4}
\]
distinct single-vertex replacements with unchanged rotation \(A/p\).

The explicit component uses the odd part of \(x+1\) before \(N=2x+1\), then the new odd vertex \(2x+1\) afterwards. For large cycles of the indicated fixed width, every phase \(s\le x<2s\) produces an insertion inside this cutoff interval, with its preceding odd cutoff also inside. Distinct phases give distinct cuts. The period of this component equals \(p\): on the indicated geometric branch \(\gcd(A,p)=1\) by the monotone ordinary full-step chart, and the explicit cyclic list has \(p\) entries and rotation \(A/p\). Thus all its odd parts are distinct at either cut. Its other \(p-1\) states stay unchanged, and the new vertex first becomes eligible here. Newly inserted vertices stay on this explicit component as the cutoff increases. Every one of these replacements occurs at \(2x+1\equiv3\pmod4\), so it does not require a strict Farey drop. [Finite ordinary coprime clock](FULL_STEP_CHART.md) · [Upper-bundle pointwise formula](UPPER_BUNDLE.md)

Finally, every phase with angular coordinate \(\{\log_2(x/s)\}>\log_2(R/2)\) lies below \(2s\) by the upper height bound. Their angular proportion tends to \(1-\log_2(R/2)\). This proves (4). The exact lifetime formula and transience at the first quarter insertion do not forbid a sequence of different components with the same rotation. In fact (4) proves that any proposed ordinary cycle in this branch supplies such replacements.

[Exact component lifetimes and persistent-component census](check_plateau_components.py) · [Recorded controls](plateau_components_controls.json)
