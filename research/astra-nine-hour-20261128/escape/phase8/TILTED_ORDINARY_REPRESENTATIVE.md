# The critical moment of the least positive ordinary representative

Let \(\sigma\) be the law on \(\mathbb Z_3\) of \(\sum_{i\ge1}3^{i-1}2^{-(e_1+\cdots+e_i)}\) for iid positive gaps with probability \(3/4^e\). For \(Z\sim\sigma\), let \(r_j=r_j(Z)\) be the **least positive odd** representative of \(Z\bmod 3^j\), in \(\{1,3,\ldots,2\cdot 3^j-1\}\). Set
\[
                        X_j=\frac{3^j}{r_j^2}.
\]
Weaver already proves exact dimension \(d_*=((8/3)\log2-\log3)/\log3>1/2\) for this law and identifies the ordinary squared-Jacobian trace at each positive odd integer. The depth-summed trace at a fixed nonperiodic \(y\) is at most \(\pi^2 y^2/8\); at a periodic \(y\) the source gives the geometric lap factor. It explicitly leaves uniform subquadratic control in a moving \(y\) open. We use those finite identities to evaluate the entire variable \(X_j\) on one common probability space. [Weaver, Paper 9/v2, (6) and Proposition 11 (31)–(32)](https://rstation.ai/problems/collatz/papers/9)

For every \(0<u<1\), \(\mathbb E X_j^u\) decays exponentially. At \(u=1\) its limit is precisely the surviving reciprocal-square source mass. For moments above one there is a stronger characterization:
\[
 \begin{split}
 &\exists u>1:\quad\limsup_{j\to\infty}j^{-1}\log\mathbb E X_j^u\le0\\
 &\ \Longleftrightarrow\
 \text{all positive orbits enter a fixed finite union of cycles}\\
 &\hspace{44mm}\text{within }O(\log(2n))\text{ native steps from }n .
                                                                         \tag{1}
 \end{split}
\]
The right side implies exponential decay of the moment at some \(u>1\). The finite cycles in (1) need not be specified in advance. The equivalence states the full uniform-time consequence of a supercritical moment bound.

## Lifting the quotient sum to positive sources

Use the odd map \(U(x)=(3x+1)/2^{v_2(3x+1)}\). For a positive odd source \(x\), set \(y_j(x)=U^j x\), \(A_j(x)=3^j2^{-S_j(x)}\), where \(S_j\) is the sum of its first \(j\) gaps, and
\[
 f_j(x)=\frac{x A_j(x)}{y_j(x)}
       =\prod_{i<j}\frac{3U^i x}{3U^i x+1}\in(0,1].
\]
Write \(W_j(y)=3^j\sigma(y+3^j\mathbb Z_3)\). Proposition 11 gives \(W_j(y)=\sum_{U^jx=y} A_j(x)^2\) for every positive odd \(y\). An integral-compatible inverse step from such a site gives the positive odd integer \((2^ey-1)/3\), so every word counted by the cylinder is a genuine ordinary inverse path. If \(I_j=\{1,3,\ldots,2\cdot3^j-1\}\), direct summation gives for every \(u>0\)
\[
      \mathbb E X_j^u=3^{(u-1)j}
         \sum_{x\ {\rm odd}>0:\ y_j(x)\in I_j}
              \frac{f_j(x)^2}{x^2}\,y_j(x)^{2(1-u)} .                 \tag{2}
\]
Every fixed \(x\) eventually meets the representative condition, since
\(y_j(x)+1\le(3/2)^j(x+1)\) by induction through genuine odd steps.

The log product is summable along any simple positive orbit by the uniform [reciprocal packing bound for simple trajectories](../phase4/HARMONIC_SOURCE_PHASE.md). Thus \(f_\infty(x)=\lim_j f_j(x)\) is positive on every escape; on any cycle basin it is zero, because the lap product is strictly below one. Dominated convergence in (2) at \(u=1\) gives
\[
 \lim_j\mathbb E X_j=\mathcal E
    :=\sum_{\substack{x\ {\rm odd}>0\\x\ {\rm escapes}}}
                        \frac{f_\infty(x)^2}{x^2}.                    \tag{3}
\]
So \(\mathcal E=0\) exactly when every positive trajectory is bounded. Independently, using all odd lifts of a quotient residue instead of its least positive odd representative changes \(\mathbb E X_j\) by \(O(3^{-j})\), since the other terms have denominators \((r_j+2k3^j)^2,\ k\ge1\).

At a moving target \(y\) far down a fixed escaping ray, the potential of the stationary law has the precise limit
\[
     \frac{1}{y^2}\sum_{j\ge0} W_j(y)
          \longrightarrow
              \sum_{x\ {\rm odd}\in C}\frac{f_\infty(x)^2}{x^2}>0 .
                                                                         \tag{4}
\]
Indeed every source in that component eventually first hits every sufficiently late target, and the nonperiodic target has at most one visit from each source. Apply dominated convergence to the first-hit sum, with zero for a source outside its basin. The sum on the left is also \(y^{-2}\int(3^{1+v_3(Z-y)}-1)/2\,d\sigma(Z)\), by positive summation. The singleton \(Z=y\) has zero mass by Weaver's fixed-root bound. Formula (4) evaluates the constant in the quadratic regime allowed by the earlier inequality.

## Exponential disappearance below the first moment

For \(1/2<u<1\), (2), \(f_j\le1\), and \(y_j(x)+1\le(3/2)^j(x+1)\) give
\[
                  \mathbb E X_j^u\ll_u (3/4)^{(1-u)j} .              \tag{5}
\]
The remaining sum converges because its summands are \(O(x^{-2u})\). At \(u=1/2\), split the sum at \(x=2^j\); for the tail use \(y_j\le2\cdot3^j\) from the representative restriction. This gives \(O((1+j)(3/4)^{j/2})\). For \(0<u<1/2\), concavity now gives \(O_u((1+j)^{2u}(3/4)^{uj})\). In particular \(X_j\to0\) almost surely, even with \(\limsup X_j^{1/j}\le3/4\) by Markov and Borel–Cantelli. Exact dimension separately gives the stronger almost-sure lower growth exponent \(\liminf j^{-1}\log r_j\ge d_*\log3\). For this last bound retain a Frostman exhaustion of any exponent \(b<d_*\). At depth \(j\) there are at most \(e^{vj}\) candidate representatives below \(e^{vj}\), and the masses of their cylinders on the restricted measure are \(O(3^{-bj})\). Use Borel–Cantelli for \(v<b\log3\), then exhaust. The estimates (5) control the **full law** without a rate assumption on that exhaustion.

The possible surviving first moment sits on events of exponentially small \(\sigma\)-probability. Choose \(M_j=(4/3)^{j/3}\), \(Y_j=(3/2)^j(M_j+1)\), and \(D_j=\{r_j\le Y_j\}\). Since \(\mathbb E X_j\le\sum_{x\ {\rm odd}}x^{-2}\),
\[
             \sigma(D_j)\ll(3/4)^{j/3},\qquad
             \mathbb E[X_j;\ D_j^c]\ll(3/4)^{j/3}.                   \tag{6}
\]
For the first bound use \(X_j\ge3^j/Y_j^2\) on \(D_j\). In (2) with \(u=1\), every source contributing to \(D_j^c\) has \(x>M_j\). Its whole contribution is at most \(\sum_{x>M_j}x^{-2}\). The fraction of \(\sigma\) reached by embedding any one such exceptional submeasure in all stationary prefixes of a common length is its original mass, because the prefix probabilities sum to one. Qualitative singularity of two fixed translates concerns their typical mass. It provides no quantitative estimate on the exponentially small set in (6) after weighting by \(X_j\). In particular (3), (5), and (6) identify uniform integrability of \(X_j\) as precisely equivalent to absence of escape.

## What a bound above order one entails

Put \(u=1+\epsilon\). If a fixed \(x\) escapes, its one contribution in (2), for all sufficiently large \(j\), is at least \(c_x(4/3)^{\epsilon j}\), because \(f_\infty(x)>0\) and \(y_j(x)\le(3/2)^j(x+1)\). This excludes a subexponential moment. On a cycle with least odd period \(q\), minimum \(m\), and lap product \(\omega\), take \(x=m\) and \(j\) multiples of \(q\). The one term gives exponential rate at least \(\epsilon\log3+2q^{-1}\log\omega\). A subexponential moment thus requires
\[
     (\epsilon/2)\log3\le -q^{-1}\log\omega
       \le \log(1+1/(3m))\le1/(3m).
\]
There are only finitely many possible minima, hence finitely many ordinary positive cycles. Let \(M\) be the largest of their odd sites. From any odd \(x\), let \(j\) be the first odd entry date to a cycle. The simple first-arrival product \(f_j\) has an absolute positive lower bound by the same packing theorem. Since \(y_j\le M\), it is in \(I_j\) once \(j\) exceeds a constant depending only on \(M\). In (2) the corresponding term is at least \(c_M3^{\epsilon j}x^{-2}\). The assumed subexponential bound, used with any positive exponent below \(\epsilon\log3\), shows \(j=O(1+\log x)\). The exact product identity gives \(S_j\log2=j\log3+\log x-\log y_j-\log f_j\), so the native physical time also obeys this bound. Initial halvings from even starts add at most \(\log_2 n\).

Conversely suppose every positive source reaches finitely many cycles within \(D\log(2n)\) native steps. Their maximal mean lap product per odd step is strictly below one. In (2) split the sources at \(e^{bj}\) with a small fixed \(b>0\) satisfying \(Db<1/3\). For the upper part \(\sum_{x>e^{bj}}x^{-2}\ll e^{-bj}\). For the lower part the orbit spends at least \(j/2\) odd steps on a cycle at large \(j\), so uniformly \(f_j^2\ll e^{-b'j}\) for some \(b'>0\). In both parts \(y_j^{-2\epsilon}\le1\). Choose \(0<\epsilon<\min(b,b')/\log3\) to conclude exponential decay. This proves (1).

## A critical entropy criterion with the exact escape mass

Define \(K_j=\mathbb E[X_j\log^+ X_j]\), where \(\log^+ t=\max(0,\log t)\). Directly on the positive source normalization of (2),
\[
 (\log(4/3))\mathcal E\ \le\ \liminf_{j\to\infty} K_j/j
 \ \le\ \limsup_{j\to\infty} K_j/j\ \le\ (\log3)\mathcal E .           \tag{7}
\]
Indeed the summand is \(f_j(x)^2/x^2\) times \((\log 3-2j^{-1}\log y_j(x))_+\) when \(y_j(x)\in I_j\), and zero outside. For fixed \(x\), the latter condition eventually holds. The factor is at most \(\log3\) and at least \(\log(4/3)-2j^{-1}\log(x+1)\) by the true forward growth bound. Apply Fatou and reverse Fatou with the common summable bound \((\log3)x^{-2}\). The same bracketing applies to the signed \(X_j\log X_j\), since its negative part is bounded by \(1/e\). Consequently \(K_j=o(j)\), and even \(\liminf K_j/j=0\), is equivalent to every positive ordinary orbit being bounded. This scale demands neither a uniform logarithmic entry time nor finitely many cycles; the stronger positive-power assertion (1) entails both.

## An upper limit from known long terminating paths

For the supercritical moment condition (1), existing terminating paths already exclude every
\[
                       u>1+\frac{2}{14.3\log2-1}.
\]
Weaver's slow-family theorem gives arbitrarily large positive odd \(x\) first reaching one after \(s>14.3\log x\) shortcut ticks. The first odd entry grade \(j\) satisfies \(s\log2=j\log3+\log x-\log f_j(x)\). This prefix is simple, so \(f_j(x)\ge c>0\), giving \(j\log3\ge(14.3\log2-1)\log x-O(1)\). The single native term at representative \(1\) in (2) gives \(\mathbb E X_j^u\ge c^2\,3^{(u-1)j}/x^2\). The displayed strict threshold makes this exponentially large along unbounded grades \(j\). The cited theorem in fact permits any stopping coefficient strictly below \(14.333854\ldots\) through its imported window certificate. [Weaver, Paper 127, §§10–11, in particular the stated slow terminating families](https://rstation.ai/problems/collatz/papers/127)

The finite positive and signed integer product inequalities and native exponential growth bound have a [Lean kernel](TiltedTraceBounds.lean). An [exact rational check](check_tilted_ordinary_trace.py) separately enumerates stationary cylinder masses and signed ordinary affine words.
