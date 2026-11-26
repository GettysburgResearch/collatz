# Original-source descent and projection for the two-class remainder

**Collatz remains OPEN.** This packet advances the actual two-class weighted problem left by [the triple-moment checkpoint](../joint-renewal/README.md). Its central written result is an incidence inequality: a discordant original head supplies linearly many smaller discordant heads, while each smaller head can carry only a bounded amount of original source mass. A second result preserves the entire ordered pair of futures while recovering polynomial-density control of retrospective source tests.

**Status and evidence.** The probability and source-transfer arguments in the linked manuscripts are **PROPOSED written proofs**, with **SOURCE-QUALIFIED** imported pair-chain and first-passage estimates. Their relevant algebra and quantifiers received internal independent reconstruction. Selected exact arithmetic, finite counting and contraction interfaces are separately checked in Lean. Neither internal review nor the Lean interfaces constitute a full formalization of the manuscripts or a proof of universal convergence. [Evidence and exact source hashes](../../../reports/ayh-resource-reset-20261124/two-class-descent/README.md) · [Source ledger](SOURCES.json).

Use the shortcut map
\[
T(n)=\begin{cases}n/2&2\mid n,\\(3n+1)/2&2\nmid n.\end{cases}
\]
Let \(f\) be an invariant binary color, in particular the indicator that the orbit reaches one. On \(R=81^j\), put \(d=\log_2R\) and
\[
a_j=\frac1R\#\{7R\le x<8R:f(x)\ne f(\lfloor x/81\rfloor)\}.
\]
These are counts of the original positive ordinary sources. The auxiliary fair-bit law is used only through complete finite grids and explicit counting transfers.

## 1. A recurrence for the original discordant mass

Fix \(A>1\). Uniformly for
\[
\sqrt{d\log d}\le B\le d/4,
\]
the argument gives
\[
a_j\ll_A d^{-A}+
\frac{\sqrt{\log d}}{B}
\sum_{\substack{z\in\bigcup_{\ell\ge0}[7\cdot81^\ell,8\cdot81^\ell)\\
B-O(1)\le\log_2 z\le2B+O_A(\sqrt{d\log d})}}
\frac{\mathbf1_{f(z)\ne f(\lfloor z/81\rfloor)}}{z}.
\tag{1}
\]
One exceptional set of \(O_A(Rd^{-A})\) original children works for the entire range of \(B\). The sum is comparable, up to fixed constants and boundary rows, with the sum of the smaller \(a_\ell\).

Each good discordant source produces at least \(c_AB\) admissible physical times while the first of the two arms crosses from height \(2^{2B}\) to \(2^B\). Every such time supplies a genuine discordant four-trit head edge. Conversely, at a fixed time and returned child \(z\), a bounded actual affine intercept confines the original source to an interval of length \(O(R/z)\). The native pair-merger estimate on that very interval bounds discordant sources by \(O(R/(z\sqrt d))\). Ordinary odd-count concentration leaves only \(O_A(\sqrt{d\log d})\) times for that \(z\). Double counting gives (1), with no factor exponential in the grade or truncation depth.

A classical lower bound for a nonzero linear form in \(\log2,\log3\) further proves that the \(c_AB\) returned children of one good source are **distinct**, with inverse-polynomial separation between their logarithms. This input is not needed for (1). The construction can restrict all returned heads to any prescribed nonempty open mantissa interval \(J\subset(7,8)\).

**What is still missing:** (1) is not a strict contraction. It allows a profile of order \(a_j\asymp j^{-1/2}\). Neither distinctness nor smaller heights alone proves that \(\sum_j a_j\) converges. [Full incidence argument and sparse-band criterion](HEAD_INCIDENCE.md).

## 2. The ordinary arithmetic that makes the descent possible

At a large positive grade, orient the actual pair as \(Y=3^s(X-W)\). A scalar affine recursion brings \(W\) near \(1/2\) at a positive fraction of appropriate times. The exact bottom certificate is
\[
X=8192q+2242,\qquad
X,\ X-1,\ 3X-2,\ 9X-5,\ 27X-14
\ \xrightarrow{\,T^{13}\,}\ 729q+200
\]
for every \(q\in\mathbb N\). Lean proves all five identities with the unbounded parameter.

The upper value's real phase permits removal of zero to three initial trits to enter a genuine head row. Repeated four-trit truncation then reaches one of the certified bottom values. The top truncated value meets \(Y\); the bottom meets \(X\). If the original colors differ, some edge of this finite chain differs. Simultaneous scalar frequency estimates place these requirements at common physical times without assuming independent arms.

The high-grade shadow calculation also gives a small-ball estimate for the normalized offset, transferred to actual sources through the earlier polylogarithmic first entrance and a prescribed logarithmic buffer. Its control interval is explicit; an eventual shadow after that interval is not ruled out.

[Rounded descent proof](ROUNDED_HEAD_DESCENT.md) · [Shadow and source-window estimates](HIGH_GRADE_SHADOW.md) · [Exact five-family certificate](RoundedHeadDescent.lean) · [Word and shadow algebra](HighGradeShadow.lean).

## 3. A summable part of the actual first-entrance problem

Outside \(O_A(Rd^{-A})\) sources, the total number of live physical clocks at absolute grade at most \(k\log d\), through the earlier true entrance to \(M=d^D\), is \(O_{A,k}((\log d)^5)\). This statement continues beyond the initial binary horizon. It follows from a killed entry-chain contraction, frontier control, interior occupation, and explicit original-source transfers at geometric scalar stages.

One physical clock can first cross at most one integer dyadic floor. The largest-slope cancellation strengthens the live-band occupation bound to \(O_A(K^2(\log d)^3)\) for every prescribed \(2\le K\le O(d)\), removing the earlier exponential grade census. The resulting coarea theorem proves, for
\[
0<\beta<1/4,\qquad 1/2+2\beta<b<1,
\]
a **computable** dyadic floor \(Y_j=2^{\ell_j}\), with \(d^b\le\ell_j\le2d^b+O(1)\), such that the normalized original discordant mass with entrance-clock gap at most a fixed multiple of \(d^\beta\) is summable. Its rowwise upper bound is
\[
O_A\!\left(d^{-A}+d^{-1/2+2\beta-b}(\log d)^3\right).
\]
The floor minimizes an explicitly finite certificate-failure count; its definition requires no oracle for eventual basin colors. On controlled sources its entrance time is \(\bigl(1-\tfrac12\log_2 3\bigr)^{-1}d+o(d)\). The large-lag complement remains open. For combination with rounded descent, one may minimize directly against the common-time small-grade mark, avoiding reversal of the one-way lag implication.

A finite menu improves the exponent further. For any \(\beta<1/2\), choose \(2\beta<b<1\) and an integer \(m\) with \(m(b-2\beta)>1/2\). There is a common menu of \(m\) actual deep floors such that sources having grade at most \(d^\beta\) at **every** earlier entrance have summable discordant mass. The fixed menu can be chosen by finite rowwise minimization; an almost-everywhere version uses one fixed tuple of scale parameters across all rows. For example, two floors allow \(\beta<3/8\), and three allow \(\beta<5/12\).

Order the menu from higher floors to lower ones and select the first earlier entrance whose current grade exceeds \(d^\beta\). This is an actual stopping rule using only the revealed trajectories. Outside a summable discordant contribution, it succeeds at a late physical clock. The statement concerns one adapted choice from a common finite menu; it does not assert the near-half exponent at a single floor fixed in advance.

The menu proof raises a **floor-parameter measure** to the \(m\)-th power on each fixed ordinary trajectory. It requires no independence of orbit segments. A further local-stage occupation bound \(O_A(K^2\log d+(\log d)^2)\) gives a growing menu of \(O(\log d/\log\log d)\) floors with threshold \(\sqrt d/(\log d)^{1/2+\epsilon}\), for any \(\epsilon>0\), again outside summable discordant mass.

[Original occupation proof](ACTUAL_FRONTIER_OCCUPATION.md) · [Quarter-exponent improvement](AREA_FRONTIER_EXTENSION.md) · [Finite menus and local occupation](FINITE_FLOOR_FRONTIER.md) · [Finite floor counting](FrontierCoarea.lean) · [Killed contraction algebra](KilledEntryContraction.lean).

## 4. Polynomial-density source tests while retaining the full future

Take a fixed number \(m\) of positive ordinary arms \(a_i n+b_i\), with positive odd \(a_i\), on a block of \(H=2^h\) consecutive source integers. Retain every arm's exact endpoint and odd count at clock \(h\), in order. Equal records preserve all subsequent trajectories simultaneously.

Write \(\lambda=\max_i a_i3^{p_i(h)}\), \(F=H/\lambda\). The positive scalar affine intercepts have a uniform fractional moment. On intercepts at most \(L\), the largest-slope endpoint gives both:

* at most \(C_m\lambda(1+L)^m\) exact records at each count vector;
* diameter at most \(LF\) for each source fiber.

The factors \(\lambda\) and \(1/\lambda\) cancel when small fibers are discarded. Put \(J=(h+1)^m(1+L)^m Q\), \(Q\ge1\). After discarding probability at most \(C_{m,\alpha}L^{-\alpha}+C_m/Q\), every retained good fiber has at least \(F/J\) members and diameter at most \(LF\). A further cutoff on \(F\) costs its actual probability.

For any residue test modulo \(q\) of density at most \(\epsilon\), chosen **after seeing the full ordered future record**, its conditional probability on each retained fiber is at most
\[
\min\{1,\epsilon J(L+q/F)\}.
\tag{2}
\]
The bound survives every union of retained fibers with their actual weights. Polynomial choices of \(L,Q\) therefore allow polynomially sparse retrospective tests, even inside polynomially rare future marks, with the discarded mass explicitly accounted for. An interior-window version retains a known prefix; its slope cutoff is averaged over original prefixes, not assumed for every prefix.

The earlier exponential-scale shuffle additionally supplies two-sided nearby representatives and, via the classical additive large sieve, a prime-average total-variation estimate for original residues conditional on the retained futures. Exceptional primes may depend on the selected mixture. These statements randomize aspects of the source's **past**. The common continuation remains fixed.

[Adaptive finite-family projection](ADAPTIVE_PAIRED_PROJECTION.md) · [Two-sided shuffle and prime averages](PAIRED_SOURCE_SHUFFLE.md) · [Finite trimming and residue bounds](PairedSourceShuffle.lean) · [Largest-slope band, diameter and integer census](LargestSlopeProjection.lean).

## 5. A further forward source-transfer interface

The same largest-slope cancellation controls a second forward window of an actual pair. Fix the intermediate odd counts and put the lower output in a real interval of length \(V+L\); its canonical offsets range over \(O(3^sL)\) integers. Each exact output pair has at most \(O(LF)\) original preimages over the **entire** original interval, with \(3^sFV=N\). A uniform ordinary-interval bad-event bound of \(\delta V\) for each permitted incoming offset therefore costs only \(C(t+1)^2L^2\delta\) in original probability, plus the stated intercept, count and interval-fringe exceptions.

This permits sparse finite tests at total physical deadlines strictly beyond the original \(\log_2N\) bit horizon. The future-event estimate must hold for every permitted incoming canonical profile with the required interval normalization. A square-root merger tail with a large inherited grade does not meet the needed arbitrary-power rarity. [Exact forward transfer and boundary terms](FORWARD_SOURCE_REEXPOSURE.md).

The deterministic version applies at any late physical clock on a subset with bounded actual intercepts. Its exact per-count-vector coefficient is \(3E(E+1/F)\). The true scalar sliding estimates supply polynomial bounds for both \(E\) and \(1/F\) before the earlier polylogarithmic entrance, allowing high-grade profile tests there with polynomial cost. This is the joint transfer used in the improved occupation theorem. [Late physical-clock projection](PHYSICAL_CLOCK_PROJECTION.md).

## 6. A summable arithmetic portion of true discordance

For any fixed \(0<c<1\), consider the actual paired observations through \(h=\lfloor c\log_2R\rfloor\). The normalized discordant mass for which both physical arms are prime at some common clock \(0\le t\le h\) is
\[
O_c\!\left((\log d)^2d^{-3/2}\right),
\]
which is summable across head rows. More generally, if both observed integers have no prime factor at most \(\exp(\eta d^\beta)\), the bound is \(O((\log d)^2d^{1/2-2\beta})\), summable for \(3/4<\beta\le1\) and sufficiently small fixed \(\eta>0\).

The proof first retains every actual native survivor cylinder. Its unexposed high source parameter still ranges over exponentially many consecutive integers. At each inspected clock the two physical outputs are affine forms in that parameter with slopes supported on the primes two and three. A uniform large-sieve bound on each surviving cylinder combines with the native \(d^{-1/2}\) survival fraction. This is a bound on a concrete subset of the original color-discordant weight; it does not assume that every discordant orbit has such a visit. A one-arm version allows the observation time and arm to depend on the whole exposed prefix. [Finite sieve and source-weight proof](SIFTED_DISCORDANT_SOURCES.md).

## 7. What would close the remaining color problem

Fix an open mantissa interval \(J\subset(7,8)\). Let \(L_i\) increase without bound with \(L_{i+1}\le L_i^{2-\varepsilon}\), for fixed \(0<\varepsilon<1\). If the true basin-of-one color satisfies
\[
\sum_{\substack{z/81^\ell\in J\text{ for some }\ell\ge0\\
L_i/2\le\log_2z\le3L_i}}
\frac{\mathbf1_{f(z)\ne f(\lfloor z/81\rfloor)}}{z}
=O(1/L_i),
\tag{3}
\]
then (1) makes \(\sum_j a_j\) finite. Together with the source-qualified fixed-target positivity and one-arc rigidity interface in [the macroscopic closing criterion](../literature-step/MACROSCOPIC_PAIR_CLOSURE.md), this would imply universal convergence.

Equation (3) is **OPEN**. The new projection theorem also lacks a proof that every discordant future necessarily determines a sufficiently sparse retrospective source test. These are color-dependent estimates about ordinary sources. Neither is supplied by marginal stopping-time laws or by a fair restart at a selected endpoint.

One concrete next attack uses the whole exact-future fiber \(S\): if that fiber is discordant, every child \(81a+r\), \(a\in S\), has a different color from every parent \(b\in S\). A certified meeting anywhere in this family of pairs would eliminate the entire fiber's original weight. The projection now supplies many nearby candidates while preserving both futures. A summable bound on the weight of fibers without such a meeting remains unproved.

## Literature and current repository work

The mixed binary/ternary architecture comes from Emre Yolcu, Scott Aaronson and Marijn Heule's automated termination approach. This packet uses the earlier four-trit ordinary-head reduction and constructs actual smaller head witnesses. It does not provide a terminating interpretation for the full eleven-rule rewriting system.

The scalar sibling construction in recent [paper 124](https://rstation.ai/problems/collatz/papers/124) inspired the exact ordered-family projection; the largest-slope count is the additional mechanism here. Duran's pair-chain framework and the Leen estimates discussed with corrected attribution in [post 20](https://rstation.ai/r/collatz/posts/20) supply named source-qualified inputs. The prime-average extension uses [Montgomery–Vaughan's published large-sieve inequality](https://doi.org/10.1112/S0025579300004708).

Current PR 201's low-grade Green estimate overlaps the preceding checkpoint and is credited in the ledger. PR 193's current actual-root and boundary arguments were read to preserve their ordinary-source and conditional-law distinctions. PRs 192 and 195 received updated description comparison, not a complete re-audit. Exact heads, paths, blobs and reading depth are in [SOURCES.json](SOURCES.json).

## Replay

Using the built Mathlib checkout pinned to d13f23b723b8a846827a245b89c10fc7d3f11612 with Lean 4.34.1:

    lake env bash /path/to/two-class-descent/check_lean.sh
    python -B /path/to/two-class-descent/check_high_grade.py

The script rebuilds the entire local import closure into a fresh temporary directory and queries each new public theorem's axioms. The finite checker verifies bounded word meshes and actual high-grade paths; it is not an asymptotic proof. The final published-head repository receipt is kept in PR 197; the preceding checkpoint's full PR description is preserved in the reports.
