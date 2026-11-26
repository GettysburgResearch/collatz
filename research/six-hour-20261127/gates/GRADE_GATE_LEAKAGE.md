# Subcritical leakage and the critical square-weight coefficient

**Status.** Written proposal for the physical positive shortcut. The main results give a leading constant and overshoot distribution. A finite odd-departure cutoff is explicit in the critical-square result. These quantities retain contributions from ordinary trajectories that reach 1.

Let \(\tau,x,z,w,a,L,p\) have the definitions in [the harmonic note](EARLY_GATE_BACKGROUND.md). For a successful first exit let \(q\) be its number of odd departures and \(j=\tau\) its native physical clock. The chain rule on each ordinary edge gives the exact telescoping identity
\[
 w/x=3^q/(2^j z).
\]
Write \(C_i=3^{q_i}/2^i\) for the slope of the last \(i\) native letters, now reading backwards from \(z\). Then \(z=C_i x_{-i}+A_i\), with \(0\le A_i\le(3/2)^{q_i}-1\). Indeed a new inverse odd letter at depth \(i\) increments the intercept by \(C_{i-1}/2\), and even letters add nothing. Before the \(h\)-th odd letter we have \(C_{i-1}\le(3/2)^{h-1}\). Summing this geometric progression gives the bound.

## A thin arithmetic sieve through the harmonic endpoint

Use the weaker multiplier-floor odd-depth sieve defined next, or the stricter PR201 sieve \(E'_X\) specified below. Put \(b=\lceil\log_3X\rceil\). In the physical gate shell, keep each \(z=(3p_0+1)/2\) with positive odd pre-gate \(p_0\) satisfying the rank-\(b\) terminal congruence for some sequence of positive odd return exponents with total native clock at most \(b\log_2 3+1\). Call this set \(D_X\). Such a word specifies one ternary congruence on \(p_0\) modulo \(3^b\). It follows from the rank equation, since the coefficient of \(p_0\) is a power of two, invertible modulo \(3^b\).

There are \(\binom{\lfloor b\log_2 3+1\rfloor}{b}=3^{(\theta+o(1))b}\) candidate positive compositions, where \(\theta=H_2(\log_3 2)<1\). Each class has \(O(1)\) representatives here, so \(|D_X|=o(X)\). If an exit has more than \(b\) odd departures, its pre-gate follows at least \(b\) complete odd-to-odd return steps. Every previous odd state is strictly smaller than the pre-gate, since its next native state otherwise would already reach \(z\). The last \(b\) complete return steps have intercept at most \((3/2)^b-1=o(X)\), and \(p_0\asymp X\). Their slope is consequently at least \(1/2\). They put this physical pre-gate in the indicated depth-\(b\) class. Therefore every off-sieve exit has \(q\le b\).

The same two properties hold for PR201's original \(E'_X\), namely \(|E'_X|=o(X)\) and \(q\le b\) off the sieve for all large cutoffs. PR201 requires *strict* critical inequalities on all reversed odd prefixes. Its first-failing-suffix proof invokes the specified real two-logarithm estimate, and yields \(|E'_X|\ll X^\theta/(1+\log X)^{3/2}\). The elementary \(D_X\) proof does not need this extra input. [PR201, Theorem P and (G3)–(G5)](https://github.com/GettysburgResearch/collatz/blob/21bed7ac2b1b1bb4baf0f6cabd53f8b9dd11b58a/research/unconventional-20261126/renewal/GATE_PROXIMITY.md)

For either sieve, or any sequence \(F_X\) with those two stated properties, fix \(0<s<2\), put \(u=s-1\), and \(m(u)=\int e^{uh}\,L(dh)\). As \(X\to\infty\),
\[
 X^{s-1}\sum_{x<X,\,\tau<\infty,\, z\notin F_X}
       (w/x)^s\delta_{\log(z/X)}
 \quad\Longrightarrow\quad
 \frac{e^{-uv}\int_{(v,a]}e^{uh}\,L(dh)}{1-m(u)}
    \mathbf1_{0\le v\le a}\,dv .                                      \tag{1}
\]
The same limit is obtained by retaining all exits of grade \(q\le b\), without any deletion of gate labels. At \(s=1\) this gives the harmonic law. For \(s\ne1\) its total is
\[
             \frac{m(u)-p}{u(1-m(u))}.
\]
It sharpens PR201's order bounds at \(1<s<2\) on that paper's actual off-sieve observable, with its stated input for the strict sieve retained.

For the proof, every off-sieve word has \(q\le b\) and hence \(3^q\le3X\). Its terminal lies in one class modulo \(3^q\) and each terminal yields at most one source. A necessary slope condition follows from the just-proved intercept bound and \(x<X\),
\[
 C_j\ge (X-(3/2)^b)/X\ge1/2 .
\]
The normalized contribution of a word is at most \(C_s C_j^s/3^q=C_s2^{-j} C_j^u\), even when its ternary class has very few representatives. Choose \(\max(0,u)<t<1\). Our slope floor makes this at most \(C_{s,t}2^{-j}C_j^t\). Summing over all words of time \(j\), then over \(j\ge J\), bounds the entire late contribution by \(C_{s,t}\lambda(t)^J/(1-\lambda(t))\), with \(\lambda\) from the harmonic note. This dominates also the grade-truncated tails. There is no terminal congruence estimate beyond the range \(3^q\le3X\).

For the fixed clocks use the dyadic Riemann argument from the harmonic note, replacing \(dx/x\) by \(X^{s-1}dx/x^s\). Its continuum source law in initial log gap \(r>0\) is \(e^{ur}dr\). The first \(J\) clocks give \(O_{s,J}(|F_X|/X)\) normalized mass on the deleted labels. Each ladder increment \(h\) after an earlier record \(R\) sends the covered initial gaps to overshoots \(v\in[0,h]\) with density \(e^{u(R+h-v)}\). Summing successive record laws gives (1). In fact \(m(1)=1\). The martingale \(e^{S_{n\wedge\sigma}}\) is bounded by \(e^a\), and on \(\sigma=\infty\) it tends to zero by the strong law and the negative mean increment. Taking expectations proves the identity. As \(h>0\) on success, \(m(u)<1\) for every \(u<1\).

## An exact leading coefficient at the square weight

Here take \(b=\lfloor\log_3 X\rfloor\). On each physical finite first-exit path use its own grade cutoff \(q\le b\), without any deletion of labels. Let the reversed letters now be independent with odd probability \(3/4\), and let \(S_i\) be the corresponding log slope. Then
\[
 \frac{X}{b}\sum_{x<X,\,\tau<\infty,\,q\le b}(w/x)^2
 \longrightarrow
 \frac43\,\mathbb E_{3/4}\left[\left(1-e^{-\inf_{i\ge1}S_i}\right)_+\right]>0 .
 \tag{2}
\]
PR201 proved the critical order \(X^{-1}\log X\) on its off-sieve sites and a corresponding lower bound after arbitrary power-thin deletion. Formula (2) computes a precise coefficient on the specified *grade-truncated* physical flux. No equality of critical coefficients after site deletion is asserted.

For each reversed word of positive length \(j\) and grade \(q\le b\), let \(M=\min_{1\le i\le j}C_i\) and \(V=\min_{1\le i\le j}(XC_i+A_i)\). In particular \(M\le3/2\) and \(XM\le V\le XM+(3/2)^q\). The exact first-exit endpoint interval is \(X\le z<V\) in its one ternary class for sufficiently large \(X\). The rank congruence ensures integral inverse histories at every prefix. This can also be checked one ternary guard at a time by reducing the full congruence at the first backwards odd letter and cancelling one factor of three. All inverse states are positive because \(z\ge X>(3/2)^b\ge A_i\). Their being below \(X\) is precisely \(z<XC_i+A_i\) at every nonempty prefix. If the first reversed letter is even, the interval is empty. Positivity, strictness, and deterministic forward iteration leave no further history ambiguity.

For \(f(r)=(1-1/r)_+\) on \(r>0\), a one-dimensional Riemann bound on that progression gives
\[
  X\sum_{X\le z<V,\ z\equiv r_w\ (3^q)}(C_j/z)^2
   = \frac{C_j^2}{3^q}\left[f(M)+O(3^q/X)\right].                 \tag{3}
\]
Indeed \(f(M)=\int_1^{\max(1,M)}t^{-2}dt\). Replacing \(V\) by \(XM\) costs at most \(O(1+(3/2)^q/3^q)\) grid points, each of weight at most \(C_j^2/X\) after normalization. The monotone integrand on the grid has an endpoint error of the same size. Constants are uniform even in \(j\).

The factor \(C_j^2/3^q=3^q/4^j\) is exactly the Bernoulli-\(3/4\) probability of the reversed word. At each fixed grade \(q\) its sum over all words and lengths is at most \(4/3\), by the geometric waiting time for the next odd letter. Thus the total error in (3) through grade \(b\) is \(O(\sum_{q\le b}3^q/X)=O(1)\). Its main term is
\[
 \mathbb E_{3/4}\sum_{1\le j<\tau_{b+1}} f\!\left(\exp\min_{1\le i\le j} S_i\right),
\]
where \(\tau_{b+1}\) is the time of the \((b+1)\)-st odd letter. Almost surely the bounded summands have a limit, and \(\tau_{b+1}/b\to4/3\). These ratios have bounded second moments since they are sums of \(b+1\) independent geometric wait times divided by \(b\). Uniform integrability passes to the displayed Cesàro limit in expectation. This proves (2). Its right side is positive because a fixed initial run of odd letters raises the walk above a positive level and the remaining positive-drift walk has an almost surely finite negative infimum. A sufficiently long initial run leaves a positive probability of staying above a fixed positive level at all later times.

The subcritical and critical statements characterize the ordinary leakage through explicitly limited histories or finite sieves. For the harmonic exponent they give a positive unnormalized contribution of order one. The harmonic mass on the retained long-history labels is uncontrolled at order \(\log X\).
