# Uniform transient endpoint atoms and the cycle-phase law at the native cutoff

Let \(\mu_{X,L}\) be the law of the actual state \(T^L n\), for \(n\) uniform on \(1,\ldots,X\) and any nonnegative deterministic shortcut clock \(L\). Call a vertex periodic if it lies on a finite forward cycle. There is an absolute \(C\) such that, on the frozen uniform first-arrival row input,
\[
       \sup_{L\ge0}\sup_{y\ {\rm nonperiodic}}\mu_{X,L}(y)
                       \le C/\sqrt{\log(2X)}.                         \tag{1}
\]
In particular the total \(q\)-collision weight of all nonperiodic endpoints is \(O_q((\log(2X))^{-(q-1)/2})\) for every fixed \(q>1\). This bound uses original, unweighted finite endpoint counts; it is uniform even at clocks far exceeding any function of \(X\).

For the limiting law also use the natural-source fixed-basin inputs and finite coverage in the [critical native count theorem](CRITICAL_NATIVE_COUNT.md). Put \(\mu=2/\log(4/3)\), \(\sigma^2=2(\log3)^2/(\log(4/3))^3\), and suppose \((L-\mu\log X)/\sqrt{\log X}\to z\in[-\infty,+\infty]\). Set \(p_z=\Pr(H\le z)\) with \(H\sim N(0,\sigma^2)\). Let \(C\) range over all periodic components, with cycle \(\Gamma_C\) of native length \(\ell_C\), and natural density \(d_C\). Define the subprobability
\[
            \pi=\sum_{C\ {\rm periodic}}d_C\,\operatorname{Unif}(\Gamma_C).
\]
Then, for *any* integer \(s_X=o(\sqrt{\log X})\),
\[
 \sup_{\substack{A\subset\mathbb N_{>0}\\ |A|\le s_X}}
       |\mu_{X,L}(A)-p_z\pi(A)|\ \longrightarrow\ 0.                 \tag{2}
\]
The periodic restriction converges in total variation to \(p_z\pi\), and \(\|\mu_{X,L}-p_z\pi\|_{\ell^q}\to0\) for all \(q>1\). In particular the probability that \(q\ge2\) independent sources meet **at the same tested native clock**, for integral \(q\), converges to
\[
             p_z^q\sum_C d_C^q/\ell_C^{\,q-1}.                       \tag{3}
\]
A nontrivial finite cycle contributes with its true period. Infinite rays have no limiting atoms.

PR215 gives a uniform *early cumulative* first-arrival upper bound for every moving odd target using this same signed physical kernel. It also gives the critical affine correction mixture and a critical parity process. Here the cubic and general \(q\)-collision observable counts equality of the *actual native endpoint*, including every cycle's native phases. The all-clock atom estimate follows from an individual row bound; the residue law (5) is a separate lattice calculation. [PR215, uniform early arrivals](https://github.com/GettysburgResearch/collatz/blob/8a50018b6a861e810b18512fdd59aaf45214bba1/research/astra-nine-hour-20261128/escape/UNIFORM_EARLY_ARRIVALS.md) · [PR215, parity process](https://github.com/GettysburgResearch/collatz/blob/8a50018b6a861e810b18512fdd59aaf45214bba1/research/astra-nine-hour-20261128/escape/TERMINAL_WINDOWS.md)

## Uniform first-hit anti-concentration

For every odd target \(a\), native first-hit clock \(s\) and odd grade \(j\), the frozen first-arrival theorem bounds the row's count by \(C p/\sqrt{1+\log p}\) with \(p=a2^s/3^j\), and bounds every source in it by \(c_0p\le n\le p\) for absolute \(c_0>0\). Use the all-positive-start version, which includes initial powers of two. For \(Q\le n<2Q\), the possible \(p\)'s are in \([Q,2Q/c_0]\). At fixed \(s,a\), their consecutive grade values have ratio three, so only \(O(1)\) grades occur. The number first hitting \(a\) at \(s\) in this octave is at most \(C Q/\sqrt{\log(2Q)}\), including bounded \(Q\) by adjustment of constants. Sum over dyadic octaves up to \(X\), splitting off the at most \(O(\sqrt X)\) sources below \(\sqrt X\). This proves
\[
     \sup_{a\ {\rm odd},\ s\ge0}
       X^{-1}\#\{n\le X:\tau_a(n)=s\}\le C/\sqrt{\log(2X)} .       \tag{4}
\]
No local limit has been inferred from a weak central limit theorem. [PR213, uniform first-arrival rows, equations (1), (3) and the all-positive extension, at 5ac2b4a7ab9fee19d2e1b1c2e4aadecd08413128](https://github.com/GettysburgResearch/collatz/blob/5ac2b4a7ab9fee19d2e1b1c2e4aadecd08413128/research/astra-diagonal-frontier-20261127/mass/SHARP_UNIFORM_FIRST_ARRIVAL_ROWS.md)

If \(T^L n=y=2^e a\) with \(a\) odd and \(y\) nonperiodic, the first visit to \(a\) occurs at exactly \(L+e\). There is no earlier visit during the specified halvings; any visit before \(L\) would put \(a\to\cdots\to y\to\cdots\to a\) on a directed cycle. This proves (1) from (4). For \(q>1\) use \(\sum_{\rm nonper}\mu(y)^q\le(\sup_{\rm nonper}\mu(y))^{q-1}\sum_{\rm nonper}\mu(y)\).

## The residue of a fixed-target arrival clock

For a fixed odd unit \(a\) and fixed integer \(\ell\ge1\), under the natural input conditioned on \(B_a\) one has
\[
 \left((\tau_a-\mu\log X)/\sqrt{\log X},\ \tau_a\bmod\ell\right)
       \ \Rightarrow\ (H,U_\ell),                                    \tag{5}
\]
where the Gaussian \(H\) and the uniform residue \(U_\ell\) are independent. Use the full row, real mark, signed-tail crop and local limit argument of [the fixed-basin window derivation](FIXED_BASIN_NATIVE_WINDOW.md). In its central smooth source sum restrict the integer native clock to \(s\equiv r\bmod\ell\). Periodizing the same continuous compactly supported test now gives an \(\ell\)-periodic function of \(\log_2(a/X)-j\log_2 3\), with mean \(1/\ell\) times the unrestricted phase mean, for each \(r\). Irrationality of \((\log_2 3)/\ell\) supplies the same translated equidistribution on each consecutive grade block of order \(\sqrt{\log X}\). The noncentral and endpoint-strip losses are bounded by the unrestricted absolute masses. For a fixed initial halving count, adjusting the physical clock cyclically permutes the residues; send its cap to infinity as in that derivation. Thus the source-normalized limit in each residue is exactly \(1/\ell\) times the same weak Gaussian, proving (5).

For a fixed periodic component \(C\), take \(a\in\Gamma_C\) an odd unit; a cycle contains one because an odd departure produces a ternary unit after stripping twos. All sources in this component eventually hit \(a\), and no others do. If \(\tau_a\le L\), the tested endpoint is a fixed function of \(L-\tau_a\bmod\ell_C\) cycling once around \(\Gamma_C\). Equation (5), continuity of the Gaussian, and a subsequence of fixed \(L\bmod\ell_C\) give mass \(p_z d_C/\ell_C\) at each phase. If already in the cycle at \(L\) before the first hit of \(a\), then \(\tau_a\) is one of the next \(\ell_C\) dates and (4) costs \(o(1)\). This argument also gives the extended cases \(z=\pm\infty\) by tightness.

For total variation on the union of cycles, fix a finite set of seeds satisfying the physical small-seed coverage from [the finite component partition](FINITE_COMPONENT_PARTITION.md). Their full components cover at least \(1-\epsilon\) of all sources in lower limit. Any unrepresented periodic component can receive endpoints only from its own sources. Its entire union has upper limiting input mass at most \(\epsilon\), and the sum of its individual densities is at most \(\epsilon\) by finite subsums. The finite represented cycles have already been treated phase by phase. Send \(\epsilon\) down to zero. Combining with (1) proves (2). The stated \(\ell^q\) convergence follows from the transient collision bound and the periodic total variation conclusion.

## The surviving fixed-ray scale

At a supercritical clock with \((L-\mu\log X)/\sqrt{\log X}\to+\infty\), suppose one supplied odd unit \(a\) escapes. For a sufficiently large constant \(B\), a subgroup of mass at least \(d(B_a)/2\) has first-hit clock in \([\mu\log X-B\sqrt{\log X},\mu\log X+B\sqrt{\log X}]\), by the fixed-basin clock law. All these clocks precede \(L\) for large \(X\), and their endpoints are in at most \(2B\sqrt{\log X}+2\) distinct nonperiodic positions of the actual forward orbit of \(a\). Hence
\[
  \liminf_X(\log X)^{(q-1)/2}\sum_{y\ {\rm nonperiodic}}\mu_{X,L}(y)^q>0
\]
by the power-mean inequality. If all positive orbits are bounded, the total nonperiodic endpoint mass tends to zero at these clocks: finite component coverage and the phase clock law give \(\sum_C d_C=1\) and all periodic mass tends to one. In this case (1) makes the same normalized collision sum tend to zero. Thus (1) attains the exact possible order under one escaping ray. An independent little-oh at these supercritical clocks would exclude escape; the uniform atom bound itself leaves this possibility.
