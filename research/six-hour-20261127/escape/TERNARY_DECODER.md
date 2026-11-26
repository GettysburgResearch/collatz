# The ternary target predicts its past on part of the physical collision measure

**Status.** Source-qualified written theorem. A finite conditional prediction error tends to zero on an explicit portion of the original positive-lift statistic. The result uses the inverse-process entropy dichotomy in PR200 and the total-variation result in [PERMANENT_SIEVE.md](PERMANENT_SIEVE.md). Their external inputs remain dependencies. No absence of escape follows from predictability alone.

Retain \(S,e,\alpha,M_k,F\) from the companion proof. Put \(H(b)=b\log b-(b-1)\log(b-1)\). Let \(a_*=1.64179412\ldots\) be the unique root of \(H(a_*)=\log3\). Fix \(\alpha<b<a_*\). At ternary precision \(d\), let \(J_b(d)\) consist of targets admitting a genuine ternary inverse word of length \(d\) whose first \(j\) exponents **in backwards order** have sum at most \(bj\) for every \(j\le d\). Each word fixes one target modulo \(3^d\). These are nested compact cylinder unions and
\[
 \# J_b(d)\bmod3^d \ \le\ \binom{\lfloor bd\rfloor}{d}
 \ \le\ \exp(dH(b)).
\]
The first inequality drops all intermediate constraints and counts compositions of totals at most \(\lfloor bd\rfloor\). Write \(J_b=\bigcap_d J_b(d)\).

For fixed \(r\ge1\) mark the positive representative \(y\) with the target and the reversed \(r\) actual past gaps at this target,
\[
 z=S^r y\in\mathbb Z_3,\qquad 
 w=(e(S^{r-1}y),\ldots,e(y)).
\]
Write \(\eta_k^{[r]}\) for the pushforward of \(M_k\) by this pair. This requires only \(r\) positive ordinary forward steps per representative. For finite \(d\) define
\[
 P_{d,r}(k)=
 \sum_{t\in J_b(d)\bmod3^d}
 \left[\eta_k^{[r]}(t)-
       \max_w\eta_k^{[r]}(t,w)\right].                                \tag{1}
\]
Here \(t\) specifies \(z\bmod3^d\), and the first term sums over all words. Different integer targets in one ternary residue take part in the same prediction. A maximizing word may be chosen separately at each depth \(k\) and residue \(t\).

**Theorem.** For each fixed \(r\),
\[
 \lim_{d\to\infty}\limsup_{k\to\infty}P_{d,r}(k)=0,\qquad
 \inf_{d\ge1}\liminf_{k\to\infty}\eta_k^{[r]}(J_b(d))
        \ \ge\ \frac{b-\alpha}{b-1}F .                                \tag{2}
\]
In particular if \(F>0\), nearly all of the clipped mass on this positive-mass portion is predicted by a table of preceding words depending only on a fixed number of ternary digits at the positive target. The iterated limits require no common table independent of the data or of \(k\). The positive fraction can be taken arbitrarily close to \(0.08855\ldots\) by increasing \(b\) towards \(a_*\).

### Getting a stationary inverse-edge law from actual ordinary edges

For each escaping ray choose empirical windows around a uniform index \(0,\ldots,k-1\). On each fixed finite window one can delete its \(O(1)\) boundary indices. Ternary states are compact. The mean of the first \(k\) exponents on each fixed ray is at most \(\alpha+c_C/k\) by corrected height. The exponents in every fixed shifted window are tight: for a nonnegative shift \(s\) use the bound on the prefix ending at \(k+s\), and for a negative shift remove the finitely many initial sites. For every subsequence extract a common further subsequence on all finite windows and all countably many rays. Telescoping the empirical windows gives stationarity, and the limit has mean exponent \(\le\alpha\) on each ray by truncation. The inverse edges \(z\longmapsto I_e(z)=(2^e z-1)/3\) obey the closed legal relation in the product with discrete \(e\). The finite-mean limits give zero mass to an infinite label. Sum the limiting processes using the finite coefficients \(\Phi(H_C)\); their sum has mass \(F\) and mean integral at most \(\alpha F\). Formula (1) of the companion proof gives the same finite-window weak limits for the actual clipped data. This argument never applies total-variation convergence directly to an unbounded observable. If \(F=0\) both conclusions of (2) follow immediately.

Normalize a nonzero limit to probability. In reverse time its current state \(z\) has marginal \(\mu\), with actual next label conditional probabilities \(q_e(z)\). The stationary single-edge law is \(\mu(dz)q_e(z)\), and balance makes \(\mu\) invariant for the Markov kernel putting weight \(q_e(z)\) on the edge to \(I_e(z)\). Use the stationary two-sided **Markov extension of this one-edge law**. It need not reproduce the true correlations at two or more edges.

The external theorem [PR200 O15, §§2–4, (4)](https://github.com/GettysburgResearch/collatz/blob/ad70a3b831867cb8a74d402a2a1abdc419f5a09b/research/unconventional-20261126/operator/EXACT_BERGMAN_PRESSURE.md) applies to each ergodic component of that Markov extension with finite mean. It gives either zero branch entropy \(\int H(q(z))\,d\mu_\omega=0\), or \(\lim_d H_{\mu_\omega}(z\bmod3^d)/d=\log3\). The extension has finite mean, hence almost every component does. Its §2 explains why the ergodic components retain the very same kernel \(q\).

A component of full ternary entropy rate satisfies \(\mu_\omega(J_b)=0\). Indeed if \(p_d=\mu_\omega(J_b(d))\), the two-cell entropy bound gives
\[
 H_{\mu_\omega}(z\bmod3^d)
 \le \log2+p_d\,dH(b)+(1-p_d)d\log3 .
\]
Consequently \(p_d\to0\). On each zero-branch-entropy component, \(q(z)\) is a point mass almost everywhere. Its deterministic path stays within the set of point-mass states at every subsequent inverse time by stationarity. Formally let \(D_\infty\) be the Borel set of states whose Markov path has conditional probability one of visiting only point-mass states at every nonnegative time, including the present. Each zero-entropy component gives \(D_\infty\) full measure. The decomposition therefore proves
\[
                    \mu(J_b\setminus D_\infty)=0 .                    \tag{3}
\]
On \(D_\infty\), the original stationary process follows exactly the same deterministic inverse path. For each time the one-edge law assigns zero mass to a violation of its point-mass choice. A countable union of these null events proves the assertion for all times. Thus the entire true past is a measurable function of \(z\), almost everywhere on \(J_b\), even with arbitrary correlations in the original process.

### Finite prediction and positive mass

For any stationary limit \(\eta^{[r]}\), (3) allows prediction of the length-\(r\) word with arbitrarily small error over \(J_b\) by a finite ternary table. Indeed finitely many words cover all but arbitrarily small mass there, and each Borel set of targets carrying one of those words can be approximated in \(\mu\)-measure by a finite union of cylinders. Resolve overlaps in a fixed order. Since \(J_b(d)\downarrow J_b\), the same error estimate holds on \(J_b(d)\) with vanishing additional error. Hence \(P_{d,r}(\eta^{[r]})\downarrow0\) for each stationary limit. For fixed \(d,r\) this functional is upper semicontinuous in the edge-window law: it is the infimum over ternary tables of bounded clopen error integrals. It is nonincreasing in \(d\), since the tested set shrinks and finer tables include all coarser choices. The set of subsequential limits of the clipped edge-window laws is compact by the preceding tightness argument. Decreasing upper-semicontinuous functions tending to zero on this compact set converge uniformly there (intersect their nested closed superlevel sets). This proves the first assertion in (2).

For the mass bound on a fixed ray let \(B_i=bi-A_i(a_0)\). Strict upper records among \(B_1,\ldots,B_k\), including \(B_0=0\) as starting level, increase the running maximum by at most \(b-1\) apiece. Its terminal maximum is at least \((b-\alpha)k-c_C\). At each such record index \(i\), the actual incoming suffix of any length \(j\le i\) has total \(\le bj\). Its state therefore lies in \(J_b(d)\) if \(i\ge d\). Deleting \(O(d+r)\) boundary indices and using the total-variation replacement proves the second assertion in (2) by finite exhaustion. This argument permits \(d=o(k)\) in the mass bound. Monotonicity of (1) gives the small-error conclusion also for every \(d(k)\to\infty\). The mass bound here only asserts fixed or sublinear \(d\).

### What the decoder leaves open

The floor of the original-law density on legal unit residues gives a positive amount to other legal branches before normalizing at an integer target \(z\). A macroscopic harmonic amplitude has \(\rho_k(z)\) comparable to \(z\); that lower bound can then cost only order \(1/z\) as a conditional share. Single-target branching at this scale need not give prediction error across a positive proportion of the clipped mass. Conversely (2) identifies a specific missing assertion: a positive lower bound on (1) relative to the mass of \(J_b(d)\), uniformly at arbitrarily fine fixed ternary scales in the iterated limit, would contradict \(F>0\). No such estimate follows here from the exact affine recursion.

The elementary singular-support observation for one ternary marginal and the pressure radius alone do not prove (3). The componentwise entropy dichotomy for the Markov extension is the specific contribution of O15 used in this proof. For an independent biased geometric gap process, complete almost-sure recovery from the ternary value was already proved for a particular tilt in [Paper 9, Theorem 5](https://rstation.ai/problems/collatz/papers/9). Its existence illustrates compatibility between deterministic backwards decoding and nonconstant forward gaps.
