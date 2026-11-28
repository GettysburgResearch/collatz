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

## 4. Why the ordinary trace remains a load-bearing target

The source-qualified canonical trace has the form

\[
 H(a)=\frac{a\,\beta_a\log(4/3)}{2}
\]

at a nonperiodic odd target, where \(\beta_a\) is the natural predecessor density with its first-hit correction weight. The cited source gives absolute comparison of this weight with the unweighted predecessor density and the exact inverse harmonic equation. The resulting trace is nonnegative, has a positive floor at units, and need not be comparable to any positive power. These are imported facts, not conclusions of (6) alone. [Canonical trace and density comparison](https://rstation.ai/problems/collatz/papers/12).

If a fixed ordinary source escapes, all sufficiently late odd states \(a_j\) on its orbit are distinct and tend to infinity. Their predecessor sets contain the predecessor set of one fixed eligible state on that orbit. Positive predecessor density consequently gives

\[
                       H(a_j)/a_j\ge c_x>0.
\]

Therefore a global bound \(H(a)=o(a)\) at positive odd integers would exclude escape. The existing decay along the ancestors of **one fixed root** has a different quantifier: the escaping forward targets move, and there is no fixed final root containing that entire forward tail as ancestors. Haar regularity of the ternary density also does not control these specified ordinary integers.

The spectral theorem above isolates one difficulty in manufacturing a mixing proof of this global bound. The path theorem isolates another difficulty in proving it by a scale-regular inverse envelope. Neither closes the global bound. A viable replacement has to use a nonregular ordinary-integer estimate, a comparison uniform in moving targets with the necessary physical clock, or a certificate mechanism whose low-state visits are proved rather than inferred from high-state mixing.
