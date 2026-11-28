# Exact gain spectra on a fixed ordinary escaping component

Let \(T(x)=x/2\) for even \(x\) and \(T(x)=(3x+1)/2\) for odd \(x\).
For a path \(z,Tz,\ldots,T^jz=y\) write \(a(z,j)=3^{q_j(z)}2^{-j}\).
Take all genuine positive integer sources and allow all incoming lengths. Denote
by \(G(y)\) the largest incoming gain, including the empty path, and by \(L(y)\)
its length. This is the positive-integer specialization of Weaver's
ternary maximum gain and length. At a positive integer the maximum is actually
attained and its length is unique. A gain at least one only comes from
\(z\le y\), since the affine offset is nonnegative. Each such \(z\) makes one
visit to a nonperiodic \(y\). At a periodic \(y\) each additional lap strictly
lowers gain since its positive affine offset forces its slope to be less than
one. Finally, equality of two gains forces equality of both exponents by
unique factorization. [Weaver, Paper 178/v1, §§1–3](https://rstation.ai/problems/collatz/papers/178/v1).

## A fixed minimizing source and exact stabilization

Suppose one positive component \(\mathcal C\) escapes. Equivalence in a
component means that two forward trajectories meet, with their clocks allowed
to differ. Every trajectory in \(\mathcal C\) tends to infinity, without
repetition. Define
\[
 \xi(x)=\lim_{j\to\infty}\frac{T^j x}{a(x,j)}
       =x\prod_{\substack{i\ge0\\T^ix\ {\rm odd}}}
                      (1+1/(3T^ix)),\qquad x\in\mathcal C.
\]
This is a finite positive real and \(x<\xi(x)\le Cx\) with one universal
\(C\). The product telescopes at finite times and the elementary uniform
distinct-state bound gives \(\sum_{y\in O(x)}1/y\le C_*\). For clarity, on a
simple orbit the \(k\)-step map is injective; for \(k=\lceil\log_2 Y\rceil\)
the image of \([1,Y]\) has \(O(Y^\eta)\) points for some \(\eta<1\). Words
of odd weight above \(3k/5\) have at most \(2^{kH_2(3/5)}\) representatives,
by the parity-cylinder bijection. The remaining images are bounded by
\(3^{3k/5}+(3/2)^k\). Dyadic summation proves the asserted reciprocal bound.
The correction from any sufficiently late state tends to zero. Consequently
\(\xi(T^t x)/T^t x\to1\). This use of the real mirror from earlier work is
specific to simple positive integer trajectories.
[Weaver, Paper 177/v1, §10](https://rstation.ai/problems/collatz/papers/177/v1)
· [PR218, elementary uniform native lower bound, pin 960b4252f9a787ab8d25e9e5894cb007d1b08977](https://github.com/GettysburgResearch/collatz/blob/960b4252f9a787ab8d25e9e5894cb007d1b08977/research/astra-full-proof-20261128/mass/REPEAT_STOPPED_NATIVE_BOUNDARY.md)
· [Real mirror in Paper 168/v1, §3](https://rstation.ai/problems/collatz/papers/168/v1).

**Theorem.** The amplitude set \(\xi(\mathcal C)\) is locally finite. It has
a least element \(S\) and a strictly larger next element \(S'\). If \(x_0\)
is any source attaining \(S\) and \(y_t=T^tx_0\), then for every \(t\)
\[
 G(y_t)=a(x_0,t),\qquad L(y_t)=t.                                  \tag{1}
\]
Every competing positive source outside the finite set \(\xi^{-1}(S)\)
has gain at most \((S/S')G(y_t)\) at \(y_t\), uniformly in \(t\).
After a finite date, all possible maximizing sources occur at every \(y_t\).

More generally let \(x\) be *any one fixed member* of \(\mathcal C\),
\(v_t=T^tx\), and fix \(b>0\). After a date depending on \(x,b\), the set
of all incoming gains at \(v_t\), divided by \(\xi(v_t)\) and restricted
to \([b,\infty)\), is exactly
\[
                   \{1/\xi(z):z\in\mathcal C,\ \xi(z)\le1/b\}.       \tag{2}
\]
The multiplicity of each displayed value, counted by ordinary sources or
by incoming words, also stabilizes to the number of the corresponding \(z\).
Thus for some fixed integer \(d_x\),
\[
 L(T^t x)=t+d_x,\qquad
 \frac{G(T^tx)}{a(x,t)}=\frac{\xi(x)}S,\qquad
 \frac{G(T^t x)}{T^t x}\longrightarrow \frac1S .                    \tag{3}
\]
The first two equations hold exactly for all sufficiently large \(t\).

**Proof.** A genuine incoming word from \(z\) has the identity
\(\xi(y)=a(z,j)\xi(z)\), by shifting the defining limit. All its sources
belong to the same component. Each bounded amplitude cutoff contains
finitely many sources, since \(z<\xi(z)\). The component is unbounded in
amplitude, for example \(\xi(2^i x)=2^i\xi(x)\). This proves the first
two assertions about its ordered amplitudes. Every incoming gain from \(z\)
at \(y_t\) equals \(\xi(y_t)/\xi(z)\le \xi(y_t)/S\). The original source
attains equality by definition, giving (1) and the uniform relative gap.
Each member \(z\) of a finite cutoff meets the fixed path \(v_t\) by a finite
date, and visits every subsequent \(v_t\). Take the largest of these finitely
many dates. There is only one visit per source to any specified \(v_t\), so
(2) follows with multiplicities and without extracting a subsequence.
Finally synchronize one minimizing source at \(T^u x_0=T^v x\). Its word
to \(T^t x\) then has length \(t-v+u\) for \(t\ge v\) and the largest possible
gain. This proves (3) with \(d_x=u-v\), using the tail correction for its last
limit.

Equivalently, the complete finite-mass inverse gain powers have a fixed
component profile. For \(s>1\) let
\[
 Z_s(y)=\sum_{(z,j):\,T^jz=y} a(z,j)^s .
\]
On every such escaping component, the normalized sum along \(v_t\) increases
to \(\sum_{z\in\mathcal C}\xi(z)^{-s}\), finite and strictly positive:
\[
 \frac{Z_s(v_t)}{\xi(v_t)^s}
  =\sum_{z:\,v_t\in O(z)}\xi(z)^{-s}
  \ \uparrow\ \sum_{z\in\mathcal C}\xi(z)^{-s}\le\zeta(s).          \tag{4}
\]
The incoming cones increase and exhaust the component; the counts per source
are one. In particular the same limit holds with the physical denominator
\(v_t^s\). Equation (4) gives exact pointwise convergence on the spine,
including its full positive mass, not only the universal upper bound from
counting distinct integer sources.

## What the two inverse results imply at this root

Weaver's direct Haar estimate \(\pi(G>b)\le b^{-2}\) and his natural
first-meeting clock law are compatible with (1). A word of \(t\) steps and
\(q\) odds marks the endpoint in one class modulo \(3^q\). The squared
gain times that cylinder's mass is \(3^q/4^t\le(3/4)^t\). Even one
uniformly isolated winning cylinder per date therefore has summable squared
cost. This bound alone cannot rule out the fixed positive spine.
[Paper 178/v1, (3)](https://rstation.ai/problems/collatz/papers/178/v1).

The worst-root inverse-odd-frequency theorem guarantees frequencies up to
the Haar-typical optimum from below, which lies below the gain threshold
\(\log_3 2\). It neither supplies a growing gain at every root nor rules out
a specially supplied large winning gain. The extremal claim here requires
an alternative *at the same positive ordinary endpoint*. An arbitrarily
small relative gain gap along one fixed escaping spine would contradict
(2), but such a comparison has not been established. Nontrivial bounded
cycles are a separate question.
[Paper 229/v1, §§1–2](https://rstation.ai/problems/collatz/papers/229/v1).

## The skipped even predecessors have summably smaller gain

At every odd departure \(z\) on the fixed minimizing spine let
\(y=(3z+1)/2\) and \(w=2y\). The complete predecessor cones of these
\(w\)'s are pairwise disjoint. Each \(w\) is off the spine: a visit there
would be followed by \(y\), which is already visited from \(z\), and
nonrepetition leaves no such distinct splice. Starting from \(w\) enters
the spine in one step and stays there, so one orbit cannot visit two of the
selected \(w\)'s. These are exact shortcut statements; the unshortened map
inserts \(w=3z+1\) at this same odd step.

Choose any maximizing ordinary source \(r_w\) for \(G(w)\). The \(r_w\) are
pairwise incomparable by forward reachability. The amplitude identities give
\[
       \frac{G(2y)}{G(y)}
         = \frac{2S}{\xi(r_w)} < \frac{2S}{r_w}.                    \tag{5}
\]
Thus for every \(s>1\) the sum of the \(s\)-th powers of these ratios is at
most \((2S)^s\zeta(s)\). This first conclusion uses no density theorem.

In fact, the first powers are also summable subject to the published
uniform predecessor-count input. For each \(r_w\) choose a unit \(u_w\)
on its path through \(w\) with \(u_w\le2r_w\). If \(r_w\) itself is a unit
use it. Otherwise powers of two alone cannot take its factor of three to
\(w\equiv1\bmod3\); the image of its first odd departure is a unit and
is at most \((3r_w+1)/2\le2r_w\). The \(u_w\)'s still form an antichain.
Wren's bound \(\pi_u(X)\ge cX/u\) for positive ternary units and \(X\ge u\)
gives \(\sum_w1/u_w\le1/c\), by disjointness of every finite collection of
these predecessor sets. Hence
\[
           \sum_{z\ {\rm odd\ on\ spine}}
                \frac{G(3z+1)}{G((3z+1)/2)}\le \frac{4S}{c}.         \tag{6}
\]
In particular there are infinitely many actual positive targets \(y\to\infty\)
with \(G(y)/y\to1/S>0\) but \(G(2y)/G(y)\to0\). Among the first \(N\)
such targets at least half have ratio at most \(8S/(cN)\). The same tail
conclusions hold along every starting point of this component after the fixed
ordinary merger in (3).
[Wren, Paper 10/v3, Theorem 1 and antichain corollary, with its stated joint mixing input](https://rstation.ai/problems/collatz/papers/10/v3).

A global lower bound on \(G(2y)/G(y)\) restricted to
\(G(y)/y\ge\epsilon\) and \(y\equiv2\bmod3\), for each fixed \(\epsilon>0\),
would therefore rule out escape. No such lower bound is used in (1)–(6).
