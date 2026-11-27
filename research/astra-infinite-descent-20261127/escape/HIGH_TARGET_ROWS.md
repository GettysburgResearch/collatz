# High-weight target rows meet a small ordinary orbit

**Unconditional written theorem.** Let \(T\) denote the positive shortcut map and \(U\) the accelerated odd map. For each positive odd \(y\) put
\[
 D(y)=\sup_{d,m}\frac{3^d2^{-m}}{y}
     \#\{z\ge1:\text{first shortcut visit to }y\text{ at clock }m
                              \text{ and odd grade }d\}.
\]
All positive integer starts are counted, including initial even terms and nonunit leaves. For every \(\epsilon>0\), all targets with \(D(y)\ge\epsilon\) lie on the odd forward orbits of finitely many explicitly bounded positive integers. In particular
\[
  \limsup_{\substack{y\to\infty\\y\ \mathrm{odd}}}D(y)=0
  \quad\Longleftrightarrow\quad
  \text{every positive Collatz orbit is bounded}.                         \tag{1}
\]
This equivalence at the fair **first-moment exact-clock** weight follows from elementary parity-word packing and the finite affine grid bound. Fixed-root closed-support, stationary trace, synchronization and predecessor-density inputs are unnecessary here. The [stronger source cutoff and exact limiting extremal-class formula](FAIR_CLOCK_DIFFUSION.md) use additional written hypotheses. Finite cycles of any number and length fall on the bounded side of (1).

## Kernel-checked complete-row theorem

The Lean declaration `TargetExtinction.bounded_iff_complete_rows` proves (1) in its uniform epsilon form on the actual shortcut map. Its `completeRow m d y` enumerates \(z<2^m y+1\), checks positivity, the exact visit and grade, and checks every earlier clock for a first visit. The affine inequality shows that this finite interval contains every possible source. Both directions use arbitrary positive integer starts and arbitrarily high odd targets. The kernel has no imported analytic or density hypothesis. [Complete finite row and equivalence](TargetExtinction.lean)

The kernel proof obtains an independent geometric bound. The actual number of simple-prefix indices below \(8192^k\) is at most \(4\cdot6561^k\). Summing the finite shells bounds the reciprocal occupation above \(8192^K\) by \(262144(6561/8192)^K\). Every first-hit normalized mark is at least \(\exp(-262144)\). When every visited state in a row exceeds the cutoff, the full normalized row weight is at most \(262145(6561/8192)^K\). These constants suffice for the qualitative equivalence. The separate finite estimate \((d/3+1)/H\) is also checked on the actual odd departures. [Simple-prefix packing](../root/OrbitPacking.lean) · [Finite reciprocal shells](ReciprocalPacking.lean) · [Actual mark and first-visit simplicity](ReciprocalTrace.lean) · [Positive floor and high-row estimate](ActualPacking.lean) · [Finite odd-grade cutoff](HighRows.lean)

## Two explicit low-vertex tests

For \(H\ge1\) define
\[
 T(H)=\sup_{\rm simple}\sum_{i<d,\ x_i>H}\frac1{x_i}
\]
on finite simple positive odd segments \(x_0,\ldots,x_d\). Suppose no source in a supplied first-arrival row at \(y>H\) visits an odd departure at most \(H\). For \(h=3^d2^{-m}/y\) its normalized integer marks are \(hz=\prod_{i<d}3x_i/(3x_i+1)\). If the row is nonempty then \(h\le1/z<1/H\), since its first odd departure is at most its start or, for \(d=0\), its start is a dyadic multiple of \(y\). Each mark lies in
\[
 \left[\max\!\left(\exp(-T(H)/3),\ 1-\frac{d}{3H}\right),1\right].
\]
Indeed \(-\log(3x/(3x+1))=\log(1+1/(3x))\le1/(3x)\), and \(1-\prod_i w_i\le\sum_i(1-w_i)\). Distinct marks are spaced by at least \(h\). Hence the entire normalized row has mass at most
\[
 b_H(d)=\min\!\left(1-\exp(-T(H)/3),\frac{d}{3H}\right)+\frac1H.        \tag{2}
\]
The estimate also holds for any subset of sources in the row whose odd departures all exceed \(H\). This uses the actual shortcut visits; the finite real-interval cardinality estimate is in [FairGrid.lean](FairGrid.lean).

Thus a row of grade \(d\) with mass strictly above \((d/3+1)/H\) has target in
\[
             \{U^j q: q\le H\ {\rm positive\ odd},\ 0\le j\le d\}.       \tag{3}
\]
Include \(j=0\) for \(y\le H\). This set has at most \((d+1)\lceil H/2\rceil\) labels. At a specified weight \(b>0\), choosing \(H>(d/3+1)/b\) reduces every possible maximizing target with weight at least \(b\) to \(O((d+1)^2/b)\) ordinary labels, with no ternary quotient enumeration. The onset and the constant in this finite test are explicit.

## Elementary uniform packing

For completeness let a finite simple shortcut path be given and \(X\ge2\), \(k=\lceil\log_2 X\rceil\). Discard its last \(k\) states when testing \(k\)-step images. All remaining \(k\)-step images are distinct. The usual parity lift gives one residue modulo \(2^k\) per parity word. Thus the number of states at most \(X\) with more than \(3k/5\) odd inputs in the next \(k\) steps is bounded by
\[
                  (5/2)^k(2/3)^{3k/5},
\]
by summing binomial coefficients with the weight \((3/2)^j\). On the other states the \(k\)-step affine formula gives \(T^k z\le3^{3k/5}+(3/2)^k\), using that its real additive term plus one never exceeds \((3/2)^k\). Distinctness of the images then yields, for the number of visited positive states at most \(X\),
\[
                       N(X)\le 12 X^{49/50}.
\]
In detail the three exponential bases above are at most \(2^{49/50}\). For the first this follows from \(5^{50}<2^{69}3^{30}\); the second uses \(3^{30}<2^{49}\). Also \(k\le 2(2^k)^{49/50}\) for \(k\ge1\) and \(2^k<2X\) except that the harmless weak inequality suffices. These give the stated constant including the discarded tail. A simple odd segment expands to a simple shortcut segment: a repeated intermediate even state would force its next odd state to repeat. Consequently dyadic summation gives the explicit bound
\[
 T(H)\ \le\ \frac{12\cdot2^{49/50}}{1-2^{-1/50}}\,H^{-1/50}
       \qquad(H\ge1).                                                   \tag{4}
\]
The same computation plus finitely many small states bounds the full reciprocal sum uniformly, hence every simple correction exceeds an absolute positive constant. This is the elementary packing argument already supplied in [PR193's pinned input](https://github.com/GettysburgResearch/collatz/blob/aa6868996f6f30b12d91c367f7c6edcfd93784b2/research/astra-unconventional-20261126/boundary/TILTED_TRACE.md). The exponent here is chosen for its brief exact integer check.

## Removing the grade budget

Choose \(H\) so large that \(1-\exp(-T(H)/3)+1/H<\epsilon/2\); (4) gives an explicit sufficient \(H\). If \(D(y)\ge\epsilon\), some row exceeds \(\epsilon/2\). By (2), \(y\) is on an odd forward orbit from a positive odd \(q\le H\). The number of such \(y\le Y\) is \(O_\epsilon(Y^{49/50})\) by the same elementary path packing, with each eventual periodic orbit regarded through its first repeat. If all orbits are bounded, each of the finitely many such forward trajectories is finite, giving the forward implication in (1). More quantitatively, once all odd starts up to \(H\) are verified bounded and their largest visited odd state \(V_H\) is known, all \(y>V_H\) satisfy \(D(y)\le1-\exp(-T(H)/3)+1/H\).

Conversely, take any escaping odd start \(u\) and \(y_d=U^d u\to\infty\). For its actual first-arrival physical clock \(m_d\),
\[
  D(y_d)\ge \frac{3^d2^{-m_d}}{y_d}
         =\frac{1}{u}\prod_{i<d}\frac{3U^i u}{3U^i u+1}
         \ge\frac{1}{u}\prod_{i\ge0}\frac{3U^i u}{3U^i u+1}>0.
\]
The last product is positive by the uniform reciprocal sum. This proves (1). Establishing vanishing of the target limsup for the actual positive map is the remaining escape question.

