# First-landing fibres of every prefix of one fixed ordinary orbit

Use the shortcut map on the integers and on rationals with odd denominator. Fix a positive integer \(x\) once and for all. For \(n\ge1\), let \(t_n\) be the date immediately after its \(n\)-th odd departure, \(z_n=T^{t_n}x\), and \(L_n=3^n/2^{t_n}\). All these dates exist because each positive integer has a finite initial even run. In particular \(z_n\equiv2\pmod3\).

For \(W>0\) let \(\mathcal F_n(W)\) consist of the reduced sources \(m/3^n\) with \(0<m/3^n<W\), whose first \(t_n\) departure parities agree with those of \(x\). Let \(\mathcal N_n(W)\) be their first integer landings. We obtain the following conditional alternatives for each individual integer, with a separate unconditional arithmetic constraint on every one of its shadows.

1. If the orbit of \(x\) is eventually periodic, \(\mathcal F_n(W)\) is empty for all sufficiently large \(n\), for each fixed \(W\).
2. If the orbit is aperiodic, there is \(A_x>0\) so that for each fixed \(W>0\),
   \[
        \frac{\#\mathcal F_n(W)}{z_n}\longrightarrow
                      \frac{2W}{3(x+A_x)}.                                \tag{1}
   \]
   Each cohort lands on precisely the integers in two fixed residue classes in a real interval of length \(WL_n\), with both endpoints determined by the prefix. The uniform probability on \(N/z_n\), for \(N\in\mathcal N_n(W)\), converges to uniform probability on
   \[
       \left[\frac{A_x}{x+A_x},\frac{A_x+W}{x+A_x}\right].                \tag{2}
   \]
   If \(W>A_x/2\), then **every sufficiently large integer congruent to zero or one modulo three** occurs in \(\bigcup_{n\ge1}\mathcal N_n(W)\). One may take \(W=Cx\) with an absolute constant \(C\) for all divergent integer orbits.
3. Fix a single marked landing, for instance \(N=1\). For every \(n\) there is exactly one **signed** reduced source \(u_{n,N}\) of denominator \(3^n\) which reads the prefix of \(x\) and first lands at \(N\). This holds for every fixed integer \(N\not\equiv2\pmod3\). The sources converge to \(x\) in \(\mathbb Z_2\) in both alternatives. In the aperiodic alternative they converge in the real numbers to \(-A_x<0\), independently of the chosen mark. In the eventually periodic alternative \(|u_{n,N}|\to\infty\) in the real numbers. Consequently boundedness over all grades of the real preimages of the single mark \(1\) along these actual prefixes is equivalent to divergence of \(x\).

## Exact source and terminal intervals

A parity word of length \(t\) fixes exactly one dyadic class modulo \(2^t\) among rationals of odd denominator. Indeed a common initial portion of length \(i\) multiplies a difference by \(3^{g_i}/2^i\) for the common odd count \(g_i\). Thus equality of residues modulo \(2^t\) suffices by induction, and agreement of the first \(t\) bits makes the terminal difference dyadically integral, proving necessity. For the prefix in question this shows
\[
 m=3^n x-2^{t_n}j,\qquad (x-W)L_n<j<xL_n,\qquad 3\nmid j.                \tag{3}
\]
At the end of the prefix the two true states differ by \(j\). A ternary-unit numerator keeps that property at every positive remaining level: an even step halves it, and an odd step leaving level \(h+1\) replaces it by \((d+3^h)/2\), which is a unit if \(h>0\). This is valid for signed inputs as well. Hence the first integer landing occurs at exactly \(t_n\); each such source gives a different terminal \(N=z_n-j\).

Put \(A_n=z_n/L_n-x\). The word carry formula gives \(A_n=\tfrac12\sum_{i=1}^n L_i^{-1}>0\). Equation (3) thus becomes
\[
 \mathcal N_n(W)=\{N\in\mathbb Z:\ A_nL_n<N<(A_n+W)L_n,\quad
                          N\not\equiv2\pmod3\}.                            \tag{4}
\]
The count differs from \(2WL_n/3\) by an absolute constant. For a prescribed admissible integer \(N\), without a real source restriction, its unique signed preimage is
\[
          u_{n,N}=x+(N-z_n)/L_n=N/L_n-A_n .                                \tag{5}
\]
The shifted inverse sums underlying (5) and their two-place limits are already present at odd phases in the [matched-intercept paper, equation (6)](https://github.com/GettysburgResearch/collatz/blob/78fb05edaaf76acf0d336e37c0321b91f3db96b7/research/astra-nine-hour-20261128/machinery/phase2/MATCHED_INTERCEPT_AND_SMOOTH_PARTS.md). Here the post-odd endpoint gives the exact unit restriction and characterizes first landings of every allowed mark. The initial numerator of (5) is \(3^nx-2^{t_n}(z_n-N)\). It is a ternary unit, so the denominator really is \(3^n\), and its dyadic distance from \(x\) is at most \(2^{-t_n}\).

## The ordinary-source dichotomy

The known correction product is
\[
 z_n=xL_n\prod_{0\le i<t_n,\,T^i x\ {\rm odd}}
             \left(1+\frac1{3T^i x}\right).                               \tag{6}
\]
For an aperiodic positive integer orbit all states are distinct, so they tend to infinity. Garcia and Tal's fundamental lemma, their Proposition 1 and equation (6) give absolute \(C_0,\eta>0\) such that at most \(C_0 H^{1-\eta}\log(2H)\) members of this orbit can lie in any interval of \(H\) consecutive positive integers. Indeed two distinct states of the same aperiodic orbit never coincide after the same number of additional steps. The lemma provides exactly such a coincidence by date \(\lfloor\log_2 H\rfloor\) if the bound is exceeded. Summing over \([2^k,2^{k+1})\) gives an absolute bound for the sum of the reciprocals of all orbit states, since \(\sum(k+1)2^{-\eta k}<\infty\). Formula (6) yields \(A_n\uparrow A_x\in(0,C_1x)\) with absolute \(C_1\), and \(L_n=z_n/(x+A_n)\to\infty\). This discrepancy escape and its summability argument predate the present fibre statements. [Garcia and Tal, Lemma 3, (6), Corollary 1](https://matwbn.icm.edu.pl/ksiazki/aa/aa90/aa9033.pdf) · [Pulowski, July 2026, explicit dyadic summation and correction product](https://mathoverflow.net/questions/513539/is-it-known-that-a-divergent-collatz-trajectory-must-have-summable-reciprocals) · [Weaver, real shadow and mirror defect, Section 3](https://rstation.ai/problems/collatz/papers/168/v1)

Equations (1) and (2) now follow by counting two residue classes in every subinterval of (4). For cofinite coverage take any \(0<\varepsilon<W-A_x/2\). For all sufficiently large \(n\), the interval in (4) contains the open interval \((A_x L_n,(A_x+W-\varepsilon)L_n)\). Its multiplicative length ratio exceeds \(3/2\). Since \(L_{n+1}/L_n=3/2^{t_{n+1}-t_n}\le3/2\), upward crossings of the sequence \(L_n\to\infty\) cannot skip a sufficiently large prescribed target: choose the first late index with \((A_x+W-\varepsilon)L_n>N\). Its preceding upper endpoint was at most \(N\), and \(A_x L_n\) is strictly less than that preceding endpoint. This proves the covering claim, including possible downward jumps. Formula (5) gives the asserted real limit.

On an eventually periodic positive integer orbit, a full eventual lap of length \(p\) and grade \(g\ge1\) has \(3^g/2^p<1\) by its strictly positive affine correction. Successive full laps thus make \(L_n\to0\) exponentially. For any fixed \(W\) the interval in (3) shrinks to zero; \(j=0\) is forbidden. In (5) the two integers \(N,z_n\) are incongruent modulo three and \(|u_{n,N}|\ge L_n^{-1}-x\to\infty\).

## Prime factors required to shadow the fixed orbit

Fix a finite prime set \(S\supseteq\{2,3\}\) and \(K>0\), and let \(b_S(a)\) denote the factor of \(|a|\) supported outside \(S\), with multiplicity. For any nonzero signed ternary-unit numerator \(|m|\le2^{Kt_n}\) shadowing the entire prefix of this fixed \(x\), uniformly,
\[
                  \log_2 b_S(m)\ \ge\ t_n-o_{x,S,K}(t_n).                 \tag{7}
\]
In particular the least *positive* unrestricted ternary-unit numerator shadowing that word has \(\log_2 b_S(m)/t_n\to1\) on **every** positive integer orbit. An admissible residue occurs among the first three positive integers in its class modulo \(2^{t_n}\), which gives the matching size upper bound.

In the signed relation \(3^n x=m+2^{t_n}j\) we have \(j\ne0\) and \(g=\gcd(3^n x,m)\mid x\). Apply the primitive three-term outside-prime estimate (3) from [the endpoint product note](COPRIME_ENDPOINT_PRODUCTS.md) after dividing by \(g\). Its height is at least \(2^{t_n}|j|/g\), and its outside product at most \(b_S(x)b_S(m)|j|\). Therefore, for every \(\delta>0\),
\[
       2^{t_n}\ll_{x,S,\delta} b_S(m)^{1+\delta}|j|^{\delta}.
\]
Here \(|j|\le 2^{O_{x,K}(t_n)}\) since \(n\le t_n\). Taking logs and sending \(\delta\downarrow0\) gives (7). Its application to each fixed mark in (5) is permitted as well: \(z_n+1\le(3/2)^{t_n}(x+1)\), so its signed numerator is at most exponential in \(t_n\). The estimate uses the ineffective arithmetic Subspace Theorem.

## What future collisions in a cohort establish

For a divergent \(x\), let \(H=\lceil WL_n\rceil+2\). Garcia and Tal's same fundamental lemma bounds the number of distinct ordinary images of this entire terminal cohort after \(\lfloor\log_2 H\rfloor\) further dates by \(O(H^{1-\eta}\log(2H))\): select one representative from each image and apply the lemma in a containing interval of length \(H\). At least one genuine same-date collision class therefore has \(\gg H^{\eta}/\log(2H)\) first landings. At most \(O(H^{1-\eta}\log(2H))\) cohort members are themselves on the specified forward orbit, by the orbit-set bound. Neither conclusion supplies a later collision with the distinguished \(z_n\). For a finite sharp control, at \(z=2^d-1\) all first \(d\) departures are odd. Every positive \(y<z\) has \(T^i y+1\le(3/2)^i(y+1)<T^i z+1\) through every \(0\le i\le d\), regardless of how many of those smaller sources coalesce among themselves. This concerns varying finite controls. The invariant future of one specified positive integer remains the convergence obligation.
