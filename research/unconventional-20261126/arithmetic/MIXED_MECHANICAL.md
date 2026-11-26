# One ordinary integer in a two-sided mechanical cylinder

**Status.** Proposed mathematical results for independent review. The effective bound below uses a classical explicit two-logarithm inequality. A stronger, ineffective exponent is a source-qualified application of a recent manuscript. Neither result excludes general positive cycles or escaping orbits.

Write \(\alpha=\log_2 3\). Fix an intercept \(0\le t<1\), put \(P_j=\lfloor j\alpha+t\rfloor\) for **all** integer \(j\), and set \(e_j=P_{j+1}-P_j\in\{1,2\}\). In particular \(P_0=0\). The coordinates of the same cut in this two-sided word are
\[
 u_2=-\sum_{i=0}^\infty 2^{P_i}3^{-i-1}\in\mathbb Z_2,
 \qquad
 u_3=\sum_{i=1}^\infty 3^{i-1}2^{P_{-i}}\in\mathbb Z_3.
\]
Their defining series converge in the indicated fields. All logarithms below are natural unless a base is displayed.

**M1.** There are absolute effective constants \(C,X_0\) such that for every odd positive integer \(X\ge X_0\) and every intercept \(t\),
\[
 2^{v_2(X-u_2)}3^{v_3(X-u_3)}
 \le C\frac{X^2}{(\log X)^{2/4.117}}.
\]
The constants are not evaluated numerically. In particular neither valuation can be infinite in this range. In M1 the pair of local obligations is imposed on one and the same ordinary integer. The proof also gives a finite test involving realized gaps and rotation spacings.

**M2, source-qualified.** For every \(\eta>0\) the left side is at most \(C_\eta X^{3/2+\eta}\) for sufficiently large \(X\), uniformly in the intercept. This constant is ineffective. The sole extra input is Weaver, *A two-thirds source bound for critical Sturmian Collatz itineraries*, Paper 140/v1, Theorem 1. Its input is one-sided binary agreement for a positive **integer**. The statement here transports that theorem through an actual integral past. We have not independently checked the complete analytic proof of that input. [Weaver, Theorem 1](https://rstation.ai/problems/collatz/papers/140/v1)

## 1. Recovering the physical interval

Set \(a=v_2(X-u_2)\) and \(b=v_3(X-u_3)\), allowing infinity temporarily. Since both dyadic numbers are odd, \(a\ge1\). A right length \(r\) is available when \(P_r<a\). In fact the dyadic starting state defined by the series has signed affine iterate
\[
 u_{2,j}=-\sum_{h\ge0}2^{P_{j+h}-P_j}3^{-h-1}
\]
at each cut, and these states are odd in \(\mathbb Z_2\). Differences at the \(j\)-th prescribed endpoint are \(3^j2^{-P_j}(X-u_2)\). For \(j\le r\) all differences are even in \(\mathbb Z_2\). The prospective endpoints are dyadic rationals by forward affine composition, so they are odd ordinary integers, and they are positive by the forward formulas. Thus all prescribed exponents are exact. Choosing \(P_r\le a\) would lose the terminal oddness at equality.

A left length \(l\le b\) is available. For \(1\le j\le l\) put
\[
 A_j=2^{-P_{-j}}3^{-j},\quad
 B_j=\sum_{h=1}^{j}3^{h-1}2^{P_{-h}},\quad
 x_{-j}=A_j(X-B_j).
\]
The numerator of \(x_{-j}\) over \(3^j\) is integral. The congruence \(X=B_j\pmod {3^j}\) in \(\mathbb Z_3\) gives an integer. The single-step identity \(3x_i+1=2^{e_i}x_{i+1}\) makes each backward numerator odd. Positivity follows on the short interval used below.

For signed \(i\) in that interval set \(g_i=3^i2^{-P_i}=2^{\{i\alpha+t\}-t}\). The exact affine formula, in both directions, is
\[
 x_i=g_i(X+V_i),\qquad V_0=0,\qquad V_{i+1}-V_i=1/(3g_i).
\]
In particular \(1/2<g_i<2\) and \(|V_i|\le2|i|/3\). If \(l+r=N\le(\log X)^2\) and \(X\) is sufficiently large, every state on \([-l,r]\) lies between \(X/4\) and \(3X\).

## 2. Distinct states and the effective gain

Wu and Wang, *On the irrationality measure of log 3*, Theorem 1, give an effective lower bound \(H^{-4.1163051-\varepsilon}\) for \(|b+u\log 2+v\log 3|\) above an effective coefficient cutoff, where \(H=\max(|u|,|v|)\). Set \(b=0\), \(v=h\) and choose \(-u\) nearest to \(h\alpha\), so \(H\asymp h\). Irrationality and finitely many small coefficients then give \(\|h\alpha\|\ge c h^{-4.117}\) with an effective \(c>0\). Any fixed exponent greater than \(4.1163051\) works throughout M1. The weaker exponent 13.3 follows separately by reciprocation of Lagarias, Lemma 2.2(1). [Wu and Wang, Theorem 1](https://doi.org/10.1016/j.jnt.2014.03.007) · [Lagarias, Lemma 2.2](https://arxiv.org/abs/math/0512006)

Equality \(x_i=x_j\) at two dates with \(h=j-i>0\) would give, by multiplying the physical recurrences,
\[
 |h\alpha-(P_j-P_i)|=\sum_{k=i}^{j-1}\log_2(1+1/(3x_k))
 \le C h/X.
\]
This is impossible for \(h\le (\log X)^2\) and all sufficiently large \(X\). Thus every state in the truncated window is distinct. No assumption on eventual positive cycles is needed.

Let \(\Delta_m\) denote the largest length of an interval in the unit circle cut at \(\{-j\alpha\}\), \(0\le j\le m\). For a convergent \(P/Q\) with next denominator \(Q'\), the points with indices less than \(Q\) lie within \(1/Q'\) of a permuted \(Q\)-grid. Given \(Q\le m<Q'\), this implies \(\Delta_m\le 3/Q\). The two-log bound and \(\|Q\alpha\|<1/Q'\) give \(Q'\le C Q^{4.117}\). Hence \(\Delta_m\le C' m^{-1/4.117}\), with small \(m\) absorbed in the constant.

Take \(m=\lfloor(N-1)/2\rfloor\) for \(N\ge3\). There are \(N-m+1>m+1\) starting positions for \(m\) successive gaps. The vectors of partial sums at intercept \(z\in[0,1)\) are \((\lfloor j\alpha+z\rfloor)_{j=1}^m\). They are constant on each of the \(m+1\) half-open intervals and distinct on different intervals, since at each internal boundary a coordinate increases. Two starts \(i<j\) have the same word and intercepts in the same interval. The cut at zero ensures their distance in \([0,1)\) is at most \(\Delta_m\), including the last interval before one. Therefore
\[
  |x_i-x_j|\le C (X\Delta_m+N).
\]
If \(E\) is the common total of the \(m\) exact gaps, subtract the two forward affine identities:
\[
 3^m(x_i-x_j)=2^E(x_{i+m}-x_{j+m}).
\]
The right endpoint difference is even. Distinctness and coprimality imply \( |x_i-x_j|\ge2^{E+1}>3^m\), since \(E\ge\lfloor m\alpha\rfloor\). Consequently
\[
 3^m\le C(Xm^{-1/4.117}+N).                                    \tag{1}
\]
For large \(X\) it is impossible for the available total to be at least \(\lfloor(\log X)^2\rfloor\): take exactly that many left and right gaps from the available interval. Equation (1) would have exponential left side on that scale while the right is \(O(X)\). Therefore both available lengths are finite, their full total \(N\) is below the truncation threshold, and (1) applies to the entire interval.

For maximal \(r\), \(P_r<a\le P_{r+1}\le P_r+2\). With \(l=b\) and \(P_r=r\alpha+O(1)\), the required product is \(O(3^N)\). If \(N\le\log_3 X\) the conclusion follows at once. Otherwise \(m\gg\log X\), the term \(N=O((\log X)^2)\) is absorbed into \(X/(\log X)^{1/4.117}\), and squaring (1) bounds \(3^N\) up to an absolute factor. This proves M1.

## 3. The stronger one-sided input at the correct physical start

The positive integer \(x_{-b}\le 3X\) physically realizes the whole word from the oldest recovered state through \(x_r\). Its shortcut length is \(n=P_r-P_{-b}\). Its odd dates are precisely the positions \(P_i-P_{-b}\) for \(-b\le i<r\). The indicator of the entire two-sided set \(\{\lfloor i\alpha+t\rfloor:i\in\mathbb Z\}\) at date \(k\) is
\[
 \lceil(k+1-t)/\alpha\rceil-\lceil(k-t)/\alpha\rceil.
\]
This is an upper mechanical binary word of slope \(1/\alpha=\log_3 2\). Apply Weaver's uniform Theorem 1 at this actual positive integer to get \(2^n\le C_\eta(3X)^{3/2+\eta}\). Finally \(2^a3^b\asymp 2^n\) up to absolute factors, proving M2. This argument does not multiply separate one-place estimates.

## 4. Ordinary scope

The uniform statement concerns a common intercept for past and future. Independent intercepts, an arbitrary critical word, or an arbitrary orbit need not give the phase-interval comparison used in (1). Paper 222 obtains strict order for an actual finite integer segment confined to an octave and identifies its critical word. Here the input is simultaneous local approximation at an *interior* ordinary cut. [Weaver, Paper 222, Theorem 1](https://rstation.ai/problems/collatz/papers/222)

The companion construction gives positive rational cycles that approximate the same pair more closely than any power of their real size even while every fixed finite collection of primes regards the points as integral. Their full rational height includes the denominator. The two results give an obstruction to explaining the integer bound by any fixed finite integrality test. They make no conclusion assigning a mechanical two-sided window of a required length to a hypothetical counterexample.
