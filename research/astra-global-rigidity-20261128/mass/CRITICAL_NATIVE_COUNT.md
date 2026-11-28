# The critical observation window for the ordinary odd-count test

**Source-qualified written theorem.** For the shortcut map \(T(2x)=x,\ T(2x+1)=3x+2\), take \(n\) uniformly from the ordinary sources \(1,\ldots,X\), and count odd departures \(Q_L(n)\) in its first \(L\) steps. All clocks below are deterministic integers. No minimum, hitting time, cycle or component is tested in the observable. Set
\[
 D=\log(4/3),\quad \mu=2/D,\quad N=\log X,\quad
 \sigma^2=2(\log3)^2/D^3,\quad \beta=D/(2\log3).
\]
Thus \(\mu\approx6.952\) and \(\beta^2\sigma^2=1/(2D)\). Define \(\psi(t)=t/(1+|t|)\).

* If \(L/N\to c\) with \(0<c\le\mu\), the ordinary unscaled variance \(\operatorname{Var}(Q_L/L)\to0\), regardless of what all orbits do.
* For each fixed \(c>\mu\), \(L/N\to c\) gives \(\operatorname{Var}(Q_L/L)\to0\) under universal convergence, whereas any counterexample gives a strictly positive lower limit.
* If \(L=\mu N+u_X\), with \(u_X/\sqrt N\to+\infty\) and \(u_X=o(N)\), the expectation of \(\psi((Q_L-L/2)/u_X)\) tends to zero under universal convergence and has strictly positive lower limit if there is a counterexample.
* At **every fixed real \(z\)**, let \(L=\mu N+z\sqrt N+o(\sqrt N)\) and \(S_X=(Q_L-L/2)/\sqrt N\). Under universal convergence \(S_X\Rightarrow N(0,1/(2D))\). One positive counterexample implies
\[
                    \liminf_{X\to\infty}\mathbb E\psi(S_X)>0.          \tag{1}
\]
The same strictly increasing bounded odd test works for every \(z\), including \(z<0\).
* Immediately before this window, if \((L-\mu N)/\sqrt N\to-\infty\) and \(L/N\to\mu\), the same centered Gaussian law holds **unconditionally**. In particular the bounded test then tends to zero even if there were a bad component.

The linear-time transition sharpens the sufficient superlogarithmic regime in [PR211, source variance at 4b44cded44af5bb7c3ce67fb16a70c898ad505d5](https://github.com/GettysburgResearch/collatz/blob/4b44cded44af5bb7c3ce67fb16a70c898ad505d5/research/astra-reciprocal-rigidity-20261127/descent/postpeak/stopped/SOURCE_VARIANCE.md). The critical Gaussian and its one-sided comparison use the actual last part of an ordinary trajectory before a fixed target. Their analytic inputs, in particular the fixed-root pinned bridge with its joint mixing premise, are stronger than PR211's two-input logarithmic-arrival lemma. The uncentered variance at \(L/N\to\mu\) always vanishes; identifying the fluctuation scale and testing its law is essential.

## Parallel source comparison

PR215 at 8a50018b6a861e810b18512fdd59aaf45214bba1 independently gives the critical ordinary parity comparison, the exact change of logarithmic multiplier, and a stronger subsequential *process* law across a compact range of critical shifts. Its argument stops at the first global minimum and transfers a fresh two-scale first-landing estimate. Its companion separates eventual cycles and escape through the affine correction, with a distinct Laplace test. The proof below instead derives the first-hit law and prehit modulus at each supplied ordinary root from exact two-clock first-arrival rows and the pinned inverse bridge. The single clipped odd test, fixed-anchor proof, and subcritical Gaussian statement are presented with this overlap disclosed. [PR215, terminal parity windows](https://github.com/GettysburgResearch/collatz/blob/8a50018b6a861e810b18512fdd59aaf45214bba1/research/astra-nine-hour-20261128/escape/TERMINAL_WINDOWS.md) · [PR215, affine correction mixture](https://github.com/GettysburgResearch/collatz/blob/8a50018b6a861e810b18512fdd59aaf45214bba1/research/astra-nine-hour-20261128/escape/CRITICAL_CORRECTION.md)

## Physical calculation at a fixed anchor

Use the natural-source, first-hit conclusions (1)–(2) of [the fixed-basin window derivation](FIXED_BASIN_NATIVE_WINDOW.md). These conclusions concern sampling *within* \(B_a=\{n:\exists t,\ T^t n=a\}\) at a fixed positive odd ternary unit \(a\). They give a positive natural basin density \(h_a\), \(H_X=(\tau-\mu N)/\sqrt N\Rightarrow H\sim N(0,\sigma^2)\), and negligible odd-count fluctuations on the last \(o(\log X)\) steps *before* the first hit, at scale \(\sqrt{\log X}\). The derivation identifies prior fixed-target clock work and the precise original row inputs.

The simple segment up to first hit satisfies
\[
 \log a=\log n-\tau\log2+Q_\tau(n)\log3
             +\sum_{i<\tau:T^in\ {\rm odd}}\log(1+1/(3T^in)).
\]
Its departures are distinct, so the last sum is at most \((1+\log(1+\tau))/3\) by ordering the positive integer heights. On a positive-density basin \(\log n-N=O_{\mathbb P}(1)\), by the unconditional count \(n<Xe^{-v}\). Thus
\[
          (Q_\tau(n)-\tau/2)/\sqrt N=\beta H_X+o_{\mathbb P}(1).       \tag{2}
\]
This also identifies why dividing the accumulated prefix error by a fixed multiple of \(\log X\) loses the signal at the critical clock.

Put \(A_a(r)=Q_r(a)-r/2\), \(A_a(0)=0\). For \(L/N\to\mu\), in this same fixed basin,
\[
 \frac{Q_L(n)-L/2}{\sqrt N}
  =\beta H_X+\frac{A_a((L-\tau)_+)}{\sqrt N}+o_{\mathbb P}(1).        \tag{3}
\]
When \(L\ge\tau\) this is finite count additivity and (2). When \(L<\tau\), \((\tau-L)_+=o_{\mathbb P}(N)\), and the centered count over those missing prehit steps is \(o_{\mathbb P}(\sqrt N)\) by the uniform backward-window statement. Formula (3) does not posit a limiting frequency or a growth speed on a putative escaping ray. Its future term is the literal deterministic count from the supplied ordinary \(a\).

For any \(a\) eventually reaching one, \(|A_a(r)|\le C_a\) for all \(r\), because the \(1,2\) tail alternates. A nonconvergent \(a\) instead has all states at least three. Multiplying shortcut ratios gives
\[
 3\le T^r(a)\le a\,2^{-r}(10/3)^{Q_r(a)}.
\]
Consequently
\[
 A_a(r)\ge\delta r-C_a,\qquad
 \delta=\frac{\log2}{\log(10/3)}-\frac12>0,\qquad
 C_a=\frac{\log(a/3)}{\log(10/3)}.                                  \tag{4}
\]
This includes nontrivial positive cycles and escape. The same constant \(\delta\) applies to each nonconvergent anchor.

## The central one-sided shift

Take a fixed \(z\). On \(B_a\), \((L-\tau)_+/\sqrt N=(z-H_X)_++o(1)\). At a convergent anchor, (3) gives \(S_X\Rightarrow\beta H\). At a nonconvergent anchor, monotonicity, boundedness and continuity of \(\psi\) together with (3)–(4) give
\[
 \liminf_X\mathbb E(\psi(S_X)\mid B_a)\ \ge\
 \mathbb E\psi\bigl(\beta H+\delta(z-H)_+\bigr)
   =:g(z)>0.                                                         \tag{5}
\]
Indeed \(\mathbb E\psi(\beta H)=0\) by symmetry. The added term is strictly positive on the Gaussian event \(H<z\), and the test is strictly increasing. This uses no unbounded-moment convergence.

To pass to the entire population, fix \(\varepsilon>0\). The tight minimum lemma (2) in [the component partition](FINITE_COMPONENT_PARTITION.md) places lower asymptotic mass at least \(1-\varepsilon\) in the union of the complete forward components of a finite initial set of seeds. A stronger fact holds by its proof: the same fraction of sources **visits** at least one of these finitely many seeds. In every represented component take a common forward waypoint of those seeds, continuing to an odd ternary unit if needed. All sources that visited any selected seed in that component belong to the chosen waypoint's predecessor set. Thus these finitely many pairwise disjoint fixed \(B_a\)'s have total lower mass at least \(1-\varepsilon\).

If there is a nonconvergent odd unit \(b\), include \(b\) among the seeds. The chosen waypoint in its component has \(B_b\subseteq B_a\), and \(h_b>0\) by fixed-target positivity (or the indicated trace input). On the covered basins the limiting test expectation is zero for a convergent component and bounded below by \(g(z)\) for any bad component. The omitted fraction costs at most \(\varepsilon\), since \(|\psi|\le1\). Increasing the fixed seed set consequently gives
\[
             \liminf_X\mathbb E\psi(S_X)\ge h_b g(z)>0.              \tag{6}
\]
Any bad positive source has an odd unit in its component. If every source instead reaches one, use \(a=1\) alone in (3) to obtain the stated centered Gaussian and zero test expectation.

For \(L/N\to\mu\) with \((L-\mu N)/\sqrt N\to-\infty\), the event \(L>\tau\) has probability tending to zero in each fixed \(B_a\). Equation (3) now gives the same law \(\beta H\) regardless of the anchor's future. Use the finite coverage again with an arbitrary bounded continuous test to obtain convergence in distribution on all ordinary sources.

## At other observation clocks

Inselmann's Theorem 1.6 gives \(\sup_{j\le\mu\log n}|Q_j(n)-j/2|\le\epsilon\log_2 n\) on a natural-density-one set for each \(\epsilon>0\). For \(0<c<\mu,\ L/N\to c\), the tested date lies below this source-dependent horizon for all but \(o(X)\) starts. For \(c=\mu\), truncating at \(\lfloor\mu\log n\rfloor\) changes the date by \(o_{\mathbb P}(N)\), since \(N-\log n=O_{\mathbb P}(1)\). The centered count is \(1/2\)-Lipschitz in integer time. Let \(\epsilon\downarrow0\). In both cases \(Q_L/L\to1/2\) in probability, giving variance decay by boundedness. [Inselmann, arXiv:2402.03276v3, Theorem 1.6](https://arxiv.org/html/2402.03276v3)

For fixed \(c>\mu\), the first hit in every selected fixed basin occurs before \(L\) outside a conditional \(o(1)\) exception. Equations (2) and exact posthit count additivity show that \(Q_L/L\to1/2\) in the convergent basin, whereas in any bad \(B_b\) it is at least \(1/2+\delta(1-\mu/c)-o_{\mathbb P}(1)\). If every source converges this proves zero variance. Otherwise \(B_1,B_b\) have fixed positive densities. The identity \(2\operatorname{Var}(Y)=\mathbb E(Y-Y')^2\) for independent copies gives a strictly positive lower limit from their two cross orders.

Finally take \(\sqrt N\ll u_X\ll N\) with \(u_X>0\). On each fixed selected basin \((L-\tau)/u_X\to1\) in probability, and the stopped fluctuation (2) divided by \(u_X/\sqrt N\) tends to zero. Therefore the centered count divided by \(u_X\) tends to zero in every convergent basin, and is bounded below by \(\delta-o_{\mathbb P}(1)\) in every bad basin. Apply the same finite coverage and the bounded \(\psi\). Under any counterexample its lower limiting expectation is at least \(h_b\psi(\delta)>0\). None of the positive lower bounds in this paper specifies an effective density or a finite input cutoff.

**OPEN.** Prove a centered critical Gaussian comparison for the genuine *unstopped* finite ordinary odd counts independently of the fates of their small visited states. The existing prehit Brownian and pinned-bridge laws in the proof control the first term of (3). The second remains the actual deterministic forward tail of one fixed ordinary integer.
