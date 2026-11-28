# Two exact obstructions to a generic spectral or power-envelope proof

**PROPOSED written deductions.** The first theorem uses only the actual shortcut branches, elementary Fourier estimates and Dirichlet approximation. The second uses only an explicitly displayed family of positive integer inverse paths. These are obstructions to two proposed proof mechanisms, not counterexamples to Collatz and not a proof that every possible method of those types fails.

They address two concrete routes examined in this pass. A reversible sampler imported from the factoring project needs certified ordinary connections between its inputs. A sublinear bound for the canonical inverse trace would exclude escape, but its upper envelope must accommodate highly nonuniform integer profiles. The results below quantify what the obvious implementations cannot supply.

## 1. Any short certificate staying high preserves a logarithmic phase

Write

\[
 T(n)=\begin{cases}n/2,&2\mid n,\\(3n+1)/2,&2\nmid n,\end{cases}
 \qquad \gamma=\log_2 3,
 \qquad \chi_q(n)=e^{2\pi i q\log_2 n}\quad(q\in\mathbb N_{>0}).
\]

A **connection certificate** from \(x\) to \(y\) is a finite path in the undirected graph of actual shortcut edges: every adjacent pair is \((v,Tv)\) in one of its two orientations. A pair of forward paths to one actual common endpoint supplies such a certificate. Its length counts both paths, and its height floor is the least integer appearing anywhere on them.

For an even forward edge, \(\chi_q(Tv)=\chi_q(v)\) exactly. For an odd one,

\[
 \log_2(Tv/v)=\gamma-1+\log_2\!\left(1+\frac1{3v}\right).
\]

Consequently, with \(\varepsilon_q=\|q\gamma\|_{\mathbb R/\mathbb Z}\),

\[
 |\chi_q(Tv)-\chi_q(v)|
 \le 2\pi\left(\varepsilon_q+\frac{q}{3v\log2}\right).
 \tag{1}
\]

The same bound holds when traversing that edge backwards, using its actual odd departure \(v\). Therefore a certificate of length at most \(L\), with every state at least \(M\), gives

\[
 |\chi_q(x)-\chi_q(y)|
 \le 2\pi L\left(\varepsilon_q+\frac{q}{3M\log2}\right).
 \tag{2}
\]

No probabilistic model, branch independence or distribution of the certificate is used. Its intermediate states may be much larger than its endpoints.

There is a sharper path-specific form. Let \(b\) be the signed number of odd edges, counting forward traversal positively and backward traversal negatively, and sum \(1/v\) over the odd departures on the path, with multiplicity. Then

\[
 |\chi_q(x)-\chi_q(y)|
 \le 2\pi\left(|b|\varepsilon_q+
                \frac{q}{3\log2}\sum_{\text{odd edges}}\frac1v\right).
 \tag{3}
\]

This follows by adding the logarithmic edge identities before taking the distance to an integer. In particular, a merger certificate whose two forward paths have the same odd count has \(b=0\): it does not need Diophantine approximation in this estimate.

## 2. A quantitative obstruction for a doubly stochastic sampler

Let \(X\) be a positive integer and

\[
             V_X=\{X+1,\ldots,2X\}.
\]

Let \(P\) be any doubly stochastic transition matrix on this set. Its Dirichlet energy is

\[
 \mathcal D_P(f)=\frac1{2X}
          \sum_{x,y\in V_X}P(x,y)|f(x)-f(y)|^2.
\]

Let \(\lambda\) be a Poincaré constant valid for every real function, and hence for every complex function after applying the inequality to real and imaginary parts:

\[
        \lambda\operatorname{Var}_{V_X}(f)\le\mathcal D_P(f).
\]

No reversibility is needed for this definition; the energy is that of the symmetrized matrix. It should not be confused with an arbitrary complex eigenvalue gap of a nonreversible chain.

Suppose transitions of total normalized weight at least \(1-\eta\) have actual connection certificates of length at most \(L\), all of whose states are at least \(M\). The remaining weight \(\eta\) may include uncertified transitions, paths visiting below \(M\), or paths longer than \(L\). For every integer \(1\le q\le X/100\),

\[
 \boxed{\quad
 \lambda\le\frac{16}{15}
 \left[2\eta+2\pi^2L^2
       \left(\varepsilon_q+\frac{q}{3M\log2}\right)^2\right].
 \quad}                                                        \tag{4}
\]

### Variance of the test function

Put \(\omega=2\pi q/\log2\). An exact integral gives

\[
 \left|\frac1X\int_X^{2X}e^{i\omega\log u}\,du\right|
            =\frac1{\sqrt{1+\omega^2}},
\]

because \(e^{i\omega\log2}=1\). Comparing each right-endpoint sample with its unit-interval integral gives error at most

\[
 \frac1X\int_X^{2X}\frac{|\omega|}{u}\,du=\frac{2\pi q}{X}.
\]

Thus the empirical mean of \(\chi_q\) has absolute value at most

\[
       \frac1{\sqrt{1+(2\pi q/\log2)^2}}+\frac{2\pi q}{X}<\frac14
\]

in the stated range. Its modulus is identically one, so its variance is at least \(15/16\).

### Energy

On the certified weight, use (2). On the remainder, use \(|\chi_q(x)-\chi_q(y)|\le2\). The energy is at most

\[
       2\pi^2L^2
       \left(\varepsilon_q+\frac{q}{3M\log2}\right)^2+2\eta.
\]

Divide by the variance lower bound to obtain (4).

### A uniform version without a new logarithm theorem

If \(4\le M\le X\) and \(X\ge10^4\), Dirichlet approximation with \(Q=\lfloor\sqrt M\rfloor\) provides an integer \(1\le q\le Q\) with

\[
                 \varepsilon_q\le Q^{-1}\le2M^{-1/2}.
\]

This \(q\) lies in the variance range. Equation (4) gives an absolute constant \(C\) such that

\[
                    \boxed{\lambda\le C\left(\eta+\frac{L^2}{M}\right).}
 \tag{5}
\]

This estimate applies even when the endpoints of a transition are a macroscopic distance apart. It therefore addresses a different obstruction from a short-range random-walk bound of order \(R^2/X^2\).

For example, certificates of polylogarithmic length that remain above \(X^\epsilon\) give \(\lambda\ll\eta+X^{-\epsilon}(\log X)^{O(1)}\). A uniform positive Poincaré gap then forces a positive transition weight to be uncertified, to pass below that floor, or to exceed the permitted length. The conclusion is not that an orbit-preserving expander is impossible; it says exactly which omitted trajectories would have to support its expansion.

### Balanced certificates have the stronger squared-height obstruction

If every certified connection has signed odd count zero and \(X\ge100\), use (3) with \(q=1\), without Dirichlet approximation. The same variance proof gives

\[
 \lambda\le\frac{16}{15}
       \left[2\eta+\frac{2\pi^2L^2}{9M^2(\log2)^2}\right]
       \ll\eta+\frac{L^2}{M^2}.                                \tag{5b}
\]

This applies to certificates from two forward arms with equal odd counts, including the balanced-fusion certificates used in the semiprime argument.

There is also a direct synchronous version. Suppose two starts \(x,y\in(X,2X]\) meet at the same forward date, their two prefixes have total length at most \(L\), and all their states are at least \(M\). Adding their exact logarithmic branch identities gives

\[
              \log(x/y)=k\log3+\Delta,\qquad
              k\in\mathbb Z,\quad|\Delta|\le L/(3M).
\]

If \(L/(3M)<\log(3/2)\), then \(k=0\): otherwise the right side has absolute value greater than \(\log2\), while the left side does not. Consequently

\[
                         |\log(x/y)|\le L/(3M).
\]

Thus a same-date merger of macroscopically separated starts in one octave cannot have a short certificate staying high. This is an exact path consequence, not an assumption about a typical parity word.

## 3. An explicit positive integer obstruction to power supersolutions

For odd positive integers write

\[
 U(x)=\frac{3x+1}{2^{v_2(3x+1)}}.
\]

The usual weighted inverse operator is

\[
 (Lg)(a)=\sum_{\substack{e\ge1\\x=(2^ea-1)/3\text{ positive odd}}}
                      \frac3{2^e}g(x).
 \tag{6}
\]

Suppose \(g\) is nonnegative and \(Lg\le g\). In particular, every actual exponent-one inverse edge obeys

\[
                 g(a)\ge\frac32g((2a-1)/3).                 \tag{7}
\]

For every positive even integer \(k\), define

\[
             a_i=2^{i+1}3^{k-i}-1,\qquad 0\le i\le k.
 \tag{8}
\]

All these numbers are positive odd integers prime to three. For \(i<k\), \(a_i\equiv2\pmod3\), and direct integer arithmetic gives

\[
              \frac{2a_i-1}{3}=a_{i+1},\qquad U(a_{i+1})=a_i.
\]

The valuation is exactly one, since \(3a_{i+1}+1=2a_i\) with \(a_i\) odd. Thus these are genuine positive integer paths, not a negative fixed point or only a ternary completion. Iterating (7),

\[
        g(2\cdot3^k-1)\ge(3/2)^k g(2^{k+1}-1).              \tag{9}
\]

### No envelope comparable to a sublinear power

There is no such supersolution with constants \(c,C>0\) and \(\theta<1\) satisfying

\[
       c a^\theta\le g(a)\le C a^\theta
\]

at all sufficiently large positive odd units. Substitution in (9) would require a fixed constant to dominate

\[
                       (3/2)^{(1-\theta)k}\longrightarrow\infty.
\]

In particular an ansatz \(g(a)=a^\theta\phi(a\bmod 3^m)\), with a fixed finite modulus and a positive bounded correction on units, cannot be a global inverse supersolution when \(\theta<1\). Adding a bounded positive correction depending on the real logarithmic phase does not evade (9). The statement concerns a positive supersolution comparable to the proposed scale, rather than every possible pointwise upper estimate.

More generally, if only \(g(a)\ge c a^\eta\) and \(g(a)\le C a^\theta\) are proposed, the same paths force

\[
              \theta\ge\frac{\log(3/2)+\eta\log2}{\log3}.
 \tag{10}
\]

With a constant lower floor, this requires only \(\theta\ge\log_3(3/2)\). It does **not** refute a genuinely irregular sublinear upper bound for the actual canonical trace. The elementary exponent-one word and its negative-anchor connection are prior ingredients in inverse-profile theory; the conclusion here is the precise obstruction to the proposed envelope induction. [Weaver, Paper 12, Sections 8–11 and Corollary 10](https://rstation.ai/problems/collatz/papers/12).

### No eventually increasing sublinear supersolution, even near the linear scale

There is a stronger obstruction when the proposed barrier is eventually nondecreasing in ordinary height. Suppose \(g\ge0\), \(Lg\le g\), and \(g\) is nondecreasing on all sufficiently large positive odd units. If \(g(n_0)>0\) at one unit beyond that onset, then \(g\) cannot be \(o(a)\).

Given such an odd unit \(n\), choose the smallest integer \(a\equiv11\pmod{18}\) with

\[
                         a\ge(3n+1)/2.
\]

Then \(a\) is an odd unit, and its exponent-one parent

\[
                         x=(2a-1)/3
\]

is an odd unit congruent to 7 modulo 12. The choice gives \(x\ge n\) and

\[
                    \tfrac32n<a\le\tfrac32n+19.
\]

By monotonicity and the actual single-edge inequality (7),

\[
                         g(a)\ge\tfrac32g(x)\ge\tfrac32g(n).
\]

Iterate this selection, writing \(n_{j+1}=a(n_j)\). The elementary recurrences yield

\[
 n_j\le(3/2)^j(n_0+38),\qquad
 g(n_j)\ge(3/2)^j g(n_0),
\]

and hence \(g(n_j)/n_j\ge g(n_0)/(n_0+38)>0\). In fact monotonicity between successive \(n_j\) gives an eventual positive linear lower bound on all odd units.

This rules out an increasing supersolution of scale \(a/\log a\), as well as the smaller powers. A successful sublinear supersolution must oscillate in ordinary height; replacing it by its increasing envelope need not preserve the inverse-superharmonic inequality. The conclusion concerns a barrier satisfying \(Lg\le g\), not every possible increasing pointwise upper bound for the actual trace.

## 4. Why the ordinary trace remains a load-bearing target

The source-qualified canonical trace has the form

\[
 H(a)=\frac{a\,\beta_a\log(4/3)}{2}
\]

at a nonperiodic odd target, where \(\beta_a\) is the natural predecessor density with its first-hit correction weight. The cited source gives absolute comparison of this weight with the unweighted predecessor density and the exact inverse harmonic equation. The resulting trace is nonnegative, has a positive floor at units, and need not be comparable to any positive power. These are imported facts, not conclusions of (6) alone. [Canonical trace and density comparison](https://rstation.ai/problems/collatz/papers/12).

These inputs give a further obstruction without a monotonicity assumption: **no pointwise finite nonnegative inverse-supersolution can tend to infinity at all large odd units.** Let \(\rho_k=L^k1\), and let \(\rho_k^{\rm unit}(5)\) retain only inverse endpoints prime to three. The total one-step inverse weight at any unit is at most 2, and a nonunit has no odd predecessor. Hence

\[
                     \rho_{k+1}(5)\le2\rho_k^{\rm unit}(5).
\]

The integer 5 is nonperiodic. Each fixed positive integer can reach it at only one odd depth; therefore its depth-\(k\) unit ancestors eventually avoid every bounded height range. If \(g(a)\to\infty\) on units and \(Lg\le g\), then for every fixed \(R>0\) and all sufficiently large \(k\), nonnegative iteration gives

\[
                     g(5)\ge L^kg(5)\ge R\rho_k^{\rm unit}(5).
\]

Since \(R\) is arbitrary, \(\rho_k^{\rm unit}(5)\to0\) and then \(\rho_k(5)\to0\). This contradicts the positive canonical Cesàro trace \(H(5)>0\). Only that fixed-root positive trace is needed; no uniform convergence rate or moving-target theorem is assumed. Thus a viable barrier of this type must retain bounded values along some arbitrarily large ordinary units.

If a fixed ordinary source escapes, all sufficiently late odd states \(a_j\) on its orbit are distinct and tend to infinity. Their predecessor sets contain the predecessor set of one fixed eligible state on that orbit. Positive predecessor density consequently gives

\[
                       H(a_j)/a_j\ge c_x>0.
\]

Therefore a global bound \(H(a)=o(a)\) at positive odd integers would exclude escape. The existing decay along the ancestors of **one fixed root** has a different quantifier: the escaping forward targets move, and there is no fixed final root containing that entire forward tail as ancestors. Haar regularity of the ternary density also does not control these specified ordinary integers.

The spectral theorem above isolates one difficulty in manufacturing a mixing proof of this global bound. The path theorem isolates another difficulty in proving it by a scale-regular inverse envelope. Neither closes the global bound. A viable replacement has to use a nonregular ordinary-integer estimate, a comparison uniform in moving targets with the necessary physical clock, or a certificate mechanism whose low-state visits are proved rather than inferred from high-state mixing.
