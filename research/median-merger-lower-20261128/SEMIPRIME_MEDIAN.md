# First visits to 1 and first meetings within the semiprime family

**Status.** Proposed written consequences of the cited estimates. The finite transfer inequalities are checked in Lean.

Let \(\mathcal S\) consist of \(n=pq\) with primes \(p<q\) and \(\log n<p\le(\log n)^2\). Use the shortcut \(T\), first-1 time \(\tau\), and \(\mu=2/\log(4/3)\) from the [ordinary first-hit proof](EARLY_CLOCK_AND_HALF_MASS.md). Logarithms are natural. The following deductions use the weighted fusion and short-interval estimates already assembled in PR #217. The input concerning the supply of semiprimes is unconditional in analytic number theory. The fusion bound is a separate dynamical input. [PR #217, equations (2)–(7), pinned version](https://github.com/GettysburgResearch/collatz/blob/85b48ef9de755fe016166592cb048167c83fb7e8/research/astra-collision-factor-bridge-20261128/SEMIPRIME_SUFFICIENCY.md) · [Matomäki and Teräväinen, Theorem 1.1](https://arxiv.org/pdf/2207.05038v2) · [Leen, uniform pair fusion](https://doi.org/10.5281/zenodo.23268751)

## A semiprime sampler with the same limiting orbit statistics

At an integer scale \(Y\), choose \(N\) uniformly among \(Y<n\le2Y-H\), with \(H=\lceil(\log(2Y))^{2.1}\rceil\). List the members of \(\mathcal S\) in \((N,N+H]\). If the list is empty, redraw the source. Select \(M\) uniformly from the list. The resulting law \(\nu_Y\) is supported in \(\mathcal S\cap(Y,2Y]\). All choices in the sampler use only the integers and their factorizations.

Put \(t=\lfloor\frac14\log_2 Y\rfloor\). This sampler admits a coupling with a genuinely uniform integer \(U\in(Y,2Y]\) such that
\[
      \Pr(T^tU\ne T^t M)\ll
      (\log Y)^{-\delta}
      +\sqrt{\log\log Y/\log Y}+H/Y
      =:\varepsilon_Y
\]
for some absolute \(\delta>0\). In particular the laws of the **entire future from date \(t\)** in these two experiments differ in total variation by at most the right-hand side, as do their first-1 times with \(\infty\) included.

To prove this, write \(K(n)\) for the number of available targets. Outside \(O(Y/(\log Y)^\delta)\) starting points, \(K(n)\ge L=cH/\log Y\) by the short-interval theorem. Let \(f(n)\) count available \(n+j\) with \(T^t(n+j)\ne T^tn\). Summing the weighted residue estimate (4) in #217 over \(j\le H\) gives
\[
   \sum_n f(n)\ll (HY/\log Y)\sqrt{\log\log Y/\log Y}.
\]
The failure probability for a well-supplied \(n\) is \(f(n)/K(n)\le f(n)/L\). Sparse or empty windows cost at most their proportion. To couple, take \(N=U\) if \(U\le2Y-H\) and its list is nonempty. Upon an invalid first draw, draw a fresh accepted source for \(M\). This has the claimed marginal law, since accepted first draws are uniform on the accepted set. Both trajectories stay above 1 throughout their first \(t\) dates, by \(T^j n\ge n/2^j\). Equality at date \(t\) thus identifies every later visit to 1, including failure ever to visit. The two relevant finite arguments are formalized as theorems first_one_after_fusion and window_failure_budget. [Lean proofs](HalfMass.lean)

For example, under Leen's joint minimum and time law, let \(d\) be the ordinary natural density of starts reaching 1, let \(\Phi\) be the standard normal distribution function and let \(\sigma=(\log3/2)/(\log(4/3)/2)^{3/2}\). For each fixed real \(z\),
\[
 \Pr_{\nu_Y}\{\tau(M)\le \mu\log Y+z\sigma\sqrt{\log Y}\}
              \ \longrightarrow\ d\,\Phi(z),\qquad
 \Pr_{\nu_Y}\{\tau(M)<\infty\}\longrightarrow d.
\]
The ordinary octave law follows by subtracting the two cumulative counts, whose centers differ by a bounded number of steps. For two independent copies of the sampler, the probability of equality at any common date \(H'\ge t\) differs from the corresponding probability for two independent uniform integers in the octave by at most \(O(\varepsilon_Y)\). This follows by taking independent couplings and a union bound. Sampling each member of \(\mathcal S\) with equal probability defines a different law. We have used no short-interval asymptotic equidistribution of the unweighted family. [Leen, minimum and clock law](https://doi.org/10.5281/zenodo.23269488)

There is a stronger statement about individual windows. In an empty window use zero for any local fraction. On a well-supplied window, at most \(f(n)/K(n)\) of its semiprimes fail to have **exactly the same future as \(n\) from date \(t\)**. The mean of this exceptional fraction, counting an empty window as a failure, is \(O(\varepsilon_Y)\). Thus, outside a proportion \(O(\sqrt{\varepsilon_Y})\) of windows, all but \(O(\sqrt{\varepsilon_Y})\) of their semiprimes share the same future. This identifies their exact integer first-hit dates, with \(\infty\) allowed.

In particular, fix a common deadline \(B\ge t\). If \(R_B(n)\) is the fraction of the window's semiprimes that have reached 1 by \(B\), then
\[
 \mathbb E_U\big|R_B(U)-\mathbf1_{\{\tau(U)\le B\}}\big|\ll\varepsilon_Y .
\]
The bound is uniform in \(B\), and the trimmed endpoints cost \(O(H/Y)\). At \(B=\lfloor\mu\log Y+z\sigma\sqrt{\log Y}\rfloor\), for fixed \(z\), the distribution of \(R_B(U)\) therefore converges to a Bernoulli law of parameter \(d\Phi(z)\). At \(B=\lfloor(\mu+1)\log Y\rfloor\) that parameter is \(d\). Fast semiprimes concentrate together locally because their actual trajectories have already coalesced. Consequently a positive global fraction of fast semiprimes leaves open whether most short windows contain any. [Ordinary clock law](https://doi.org/10.5281/zenodo.23269488) · [Uniform pair-fusion input](https://doi.org/10.5281/zenodo.23268751)

### A nearby representative with a bounded search

The newest #217 checkpoint defines a smaller, integer-testable family \(\mathcal B\). For binary length \(b(m)\ge4\) its small prime satisfies \(b(m)<p\) and \(4p\le b(m)^2\). That paper checks that the semiprimes furnished by Matomäki and Teräväinen all lie in \(\mathcal B\) eventually, and that the residue upper estimate for \(\mathcal S\) bounds its subset. Thus every assertion in this note about \(\mathcal S\) also holds with \(\mathcal B\) substituted and the sampler restricted to \(\mathcal B\). [PR #217, integer family and its short-interval supply](https://github.com/GettysburgResearch/collatz/blob/015070fd03ef808ef3250c8a6348c7d8de1464a4/research/astra-collision-factor-bridge-20261128/SEMIPRIME_REPRESENTATIVES.md)

There is a deterministic consequence. For \(n\) in a dyadic octave \((Y,2Y]\), take \(t=\lfloor\tfrac14\log_2Y\rfloor\). Search its next \(H\) integers for an \(m\in\mathcal B\) with \(T^t m=T^t n\), testing the exact products and trajectories. One may take \(H\) to be the least positive integer with \(H^{10}\ge b(2Y)^{21}\); this only enlarges the original supply window by a bounded factor. The summed failure bound still applies with this \(H\). A well-supplied starting window with no matching \(m\) incurs at least \(L\) failing incidences. Hence this search succeeds for a proportion \(1-O(\varepsilon_Y)\) of inputs, producing a semiprime within \(O((\log n)^{2.1})\) that meets the input at the **same** date \(t\). The bounded search takes polynomially many bit operations in \(b(n)\), by trial division for \(p\), deterministic polynomial-time primality testing for \(q\), and \(O(b(n))\) genuine shortcut steps on \(O(b(n))\)-bit operands. A once-per-input fallback to #217's unbounded representative search gives its source-qualified totality on the residual inputs. This provides a polynomial bound on a density-one set and leaves the worst-case running time open. Existence of a representative still leaves the fate of that representative undecided. [Agrawal, Kayal and Saxena, deterministic primality testing](https://doi.org/10.4007/annals.2004.160.781) · [PR #217, terminating representative search](https://github.com/GettysburgResearch/collatz/blob/015070fd03ef808ef3250c8a6348c7d8de1464a4/research/astra-collision-factor-bridge-20261128/SEMIPRIME_REPRESENTATIVES.md)

## Counts for the unweighted semiprimes

There are absolute \(b,c,C>0\) such that, for all sufficiently large \(X\) and
\[
                 0\le w\le b\sqrt{\log X\,\log\log X},
\]
at least \(c(X/\log X)\exp(-Cw^2/\log X)\) distinct semiprimes of \(\mathcal S\) in \((X/4,X]\) visit 1 by \(\mu\log X-w\). The same lower bound holds for semiprimes in that interval whose first visit to 1 is finite and falls at or after \(\mu\log X+w\).

There are also at least
\[
       c\,\frac{X^2}{(\log X)^2}\exp(-Cw^2/\log X)
\]
unordered pairs **both** in \(\mathcal S\cap[1,X]\), at distance greater than \(X/8\), whose first synchronous meeting is at 2 through 1 and 4 by \(\lfloor\mu\log X-w\rfloor\). At the central deadline this supplies a fixed positive proportion on the scale of all semiprime pairs from this family. The proportion needed to establish convergence of all members is still unknown.

For the one-source result apply the coupling on the two octaves filling \((X/4,X]\), with the same first-hit event and absolute deadline on both. Rounding the octave endpoints costs \(O(1)\) starts if \(X\) is real. On a good, well-supplied first draw, the **unconditional subprobability** assigned to any individual output \(m\) is \(O(\log X/X)\). Indeed at most \(H\) choices of the uniform integer can reach it and each choice contributes at most \(1/(|I|L)\), where \(I\) is the original octave. Omit invalid first draws and sparse windows, including their possible redraws. Together with the failed fusions these cost \(O(\varepsilon_Y)\) on each octave. The ordinary signed first-hit proof gives a probability \(\gg\exp(-Cw^2/\log X)\) in their union. For some fixed \(\kappa>0\) the total error is \(O((\log X)^{-\kappa})\). Taking \(Cb^2<\kappa\) makes that error smaller than half the ordinary lower bound for all sufficiently large \(X\), uniformly in \(w\). Dividing the surviving mass by the bound per semiprime proves both one-source counts. In particular the late estimate counts only genuine finite visits.

For the pair result take \(X_0\) to be the largest multiple of 64 at most \(15X/16\). The separated ordinary pairs constructed at \(X_0\) have both sources in \((X_0/64,X_0]\), a union of six octaves. Select two independent uniform sources on this union and independently apply the sampler for each source's own octave. On well-supplied first draws the joint output subprobability per ordered pair is \(O((\log X/X)^2)\), by the preceding atom bound and independence. Discarding the two thin windows, boundary strips and failed fusions costs \(O((\log X)^{-\kappa})\). Each output stays in its own octave and is within \(O((\log X)^{2.1})\) of the original source on the retained event. Hence the original gap \(>3X_0/16\) leaves a gap \(>X/8\) and the outputs lie below \(X\).

Up to the larger of the two fusion dates, every source on either arm stays above 4 since the smallest source exceeds \(X_0/64\). On each arm the original and output paths agree from its fusion onward. The ordinary pairs that we retain consequently still first meet through 1 and 4, at the very same date. An earlier output equality would persist to that date's two distinct parents. The ordinary pair theorem gives probability \(\gg\exp(-C'w^2/\log X)\) at \(\lfloor\mu\log X_0-w\rfloor\), which is at most the requested deadline. Decrease \(b\) once more to dominate the discarded mass. Divide by the joint atom bound, and divide by two if both orders were counted. This yields the stated number of distinct unordered semiprime pairs. [Ordinary pair construction](EARLY_CLOCK_AND_HALF_MASS.md)

The connection with the factor clocks is that these results concern actual visits to 1 and actual meetings of two large semiprime starts. The larger-factor result uses a much earlier clock and a different event, the first drop of \(pq\) below the numerical value of \(q\). [PR #220, factor passage and merger bounds](https://github.com/GettysburgResearch/collatz/pull/220)

## A local sufficient condition with a finite deadline

There is an explicit local condition that would finish the conjecture. For definiteness take \(H=\lceil(\log(2Y))^{2.1}\rceil\) and \(B=\lfloor(\mu+1)\log Y\rfloor\). For a fixed \(0<\xi<1/2\), let \(G_B(n)\) count the distinct \(m\in\mathcal S\cap(n,n+H]\) with \(\tau(m)\le B\). Under the cited fusion, positive-predecessor and timing inputs, the following statements are equivalent.

1. Every positive start reaches 1.
2. For all but \(o(Y)\) integers \(n\in(Y,2Y]\), \(G_B(n)\ge(\log Y)^{0.6+\xi}\), as \(Y\to\infty\).

In particular the power \(0.61\) suffices. The usual guaranteed supply of family members, before imposing convergence, is of order \((\log Y)^{1.1}\) outside an exceptional set. The new condition requires a fraction of that supply tending to zero, but requires it in almost every window and requires genuine finite trajectories to 1.

For sufficiency, a nonconvergent \(n\) fails to fuse with every one of its \(G_B(n)\) certified neighbors. Summing \(f(n)\) as above gives
\[
  Y^{-1}\sum_{Y<n\le 2Y} f(n)
        \ll(\log Y)^{0.6}\sqrt{\log\log Y}.
\]
Outside the exceptional windows in condition 2, division by \((\log Y)^{0.6+\xi}\) bounds the fraction of nonconvergent \(n\) by \(O((\log Y)^{-\xi}\sqrt{\log\log Y})\). Their ordinary density is therefore zero. One counterexample would give positive lower density of nonconvergence by the positive-predecessor theorem. This implication uses only the fusion and residue upper bounds, plus positivity of predecessors. A lower theorem for the supply of unmarked semiprimes is unnecessary in this direction. [PR #217, sparse failure estimate (4)](https://github.com/GettysburgResearch/collatz/blob/85b48ef9de755fe016166592cb048167c83fb7e8/research/astra-collision-factor-bridge-20261128/SEMIPRIME_SUFFICIENCY.md) · [Mazur, positive predecessor density, Theorem 1.1 and Corollary 1.2](https://www.proofatlas.ai/papers/positive-lower-density-collatz-predecessors/paper-v1.pdf)

Conversely, if every start converges, the ordinary clock law with \(d=1\) gives \(\Pr_U(\tau(U)>B)=o(1)\), since the deadline exceeds the center by \(\log Y\). Coupling gives the same conclusion for \(\nu_Y\). In a nonempty window the probability of selecting a late semiprime is \(1-G_B(n)/K(n)\). Thus the fraction of accepted windows with \(G_B(n)<K(n)/2\) tends to zero. The arithmetic supply theorem gives \(K(n)\gg(\log Y)^{1.1}\) outside \(o(Y)\) windows. This proves condition 2 for every fixed \(\xi<1/2\). The same proof allows any common deadline \(\mu\log Y+g(Y)\sqrt{\log Y}\) with \(g(Y)\to+\infty\), rounded to an integer. [Leen, joint minimum and clock law](https://doi.org/10.5281/zenodo.23269488) · [Matomäki and Teräväinen, Theorem 1.1](https://arxiv.org/pdf/2207.05038v2)

The global moderate-deviation count establishes many certified products across a macroscopic range. Its proof supplies no bound on the fraction of individual short windows containing that many certificates. This distribution across windows is the unresolved step in this criterion.
