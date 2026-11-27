# Complete cycle divisors and finite meeting windows

**2026-11-24 checkpoint on PR193.** This packet continues the whole-problem attack from `ebeec2cda24b1deafff17cb2a9ce6e1bed7d9784`, using the latest frozen PR197 and PR195 work and three GPT-6.2 Astra research lanes. It contains new written proofs, independent reviews, and eleven kernel-checked Lean declarations. **It does not prove universal Collatz convergence.**

The two leading advances are an all-word restriction on cancellation of a complete cycle denominator and a finite time window containing essentially every eventual meeting of independently sampled ordinary trajectories. The arithmetic argument uses the Subspace Theorem through Corvaja–Zannier's torus gcd theorem. The meeting argument retains the original source measure through successive first passages. A third lane transports entire ordinary futures out of arbitrarily rare subpower residue classes and determines the resulting clock displacement.

## Results and exact scope

| Result | What the proof covers | Remaining boundary |
|---|---|---|
| [Full-divisor factor bounds](arithmetic/README.md), ``1–2 | Every odd word with coprime clocks \(p,A\), \(p\le A\le Bp\); all multiplicities and the whole numerical divisor | No bound excludes the required high-degree cancellation for an unrestricted word |
| [Equal-clock block resultants](arithmetic/README.md), ``3–4 | Arbitrary primitive arrangements of two distinct equal-clock blocks, composite block counts included | No theorem forces every cycle into this description |
| [Full eventual meeting window](transfer/ALL_EVENTUAL_MEETINGS.md) | Every eventually merging component, on independent resolved moving patches; upper deadline also under arbitrary dependence | The finite meeting probability is not proved to tend to one |
| [Entire ordinary future comparison](spectral/PHYSICAL_TAILS.md) | Individual growing residue classes and adaptive transcript selections with subpower information budget | A native surviving head profile can exhaust that budget |
| [Original-source trace sampling](transfer/TRACE_SAMPLING.md) | Weighted landings and every pre-passage visit to prescribed sparse sets, with summable errors | Full predecessor basins are not sparse forward traces |
| [Marked stationary dynamics](spectral/MARKED_EQUILIBRIUM.md) | A unique mixing binary–ternary chart, and its exact invariant component-label extension | Mixing within a component does not establish a single component |

The arithmetic bounds are deductions from classical number theory and the displayed finite algebra. The analytic results are **SOURCE-QUALIFIED written theorems**: their exact external estimates and repository versions are retained in the proofs and [source record](SOURCES.json). The authors' original PROPOSED labels remain visible; the independent review verdicts below specify which frozen statements were checked. Neither a review nor the Lean build formalizes the external analytic packages.

## 1. Where a complete cycle divisor would have to cancel

For an odd word of \(p\) steps with gaps \(e_i\ge1\), let \(E_i=\sum_{j<i}e_j\), \(A=E_p\), and
\[
 C=\sum_{i=0}^{p-1}3^{p-1-i}2^{E_i},\qquad D=2^A-3^p.
\]
A positive integer cycle requires \(D>0\) and reduced denominator \(d=D/\gcd(D,C)=1\).

When \(\gcd(A,p)=1\), a shifted discrepancy mask
\[
 M(X)=\sum_{i<p}X^{K+pE_i-Ai}
\]
has coefficients zero or one, constant coefficient one, and exactly one exponent in each class modulo \(p\). Consequently \(M=S_pQ\), where \(S_p=1+\cdots+X^{p-1}\) and \(Q(1)=1\). In the full composite ring modulo \(|D|\), a Bézout generator \(z\) satisfies \(z^p=2,z^A=3\), and
\[
 \gcd(D,C)=\gcd(D,Q(z)).
\]
The unavoidable \(S_p\) factor is a unit at \(z\).

For every fixed \(k,B\), the complete product \(L_k\) of factors of \(M\) of degree at most \(k\), **with multiplicities**, satisfies
\[
 \log\gcd(|D|,L_k(z))=o_{k,B}(p).
\]
The proof controls non-torsion roots with Corvaja–Zannier and handles all repeated torsion factors through a fixed set of rational primes and Ridout's theorem. Jensen's formula supplies a uniform bound on non-torsion multiplicities. The result ranges over every word with those clocks; it does not fix the number of carry terms.

There is also an effective estimate for an arbitrary changing monic subproduct \(P\mid M\), with \(r=\deg P\):
\[
 \log\gcd(|D|,P(z))\ll_B r+\sqrt{pr\log p}.
\]
This uses a short integer relation between \(p,A\), an integral resultant, and \(\mathcal M(P)\le\sqrt p\). Thus factors of total degree \(o(p/\log p)\) cancel only a subexponential part. An ordinary coprime-clock cycle would need aggregate degree \(\gg p/\log p\) among factors of degree **greater than every fixed bound**, after their bounded-degree companions have been removed.

The separate Fourier/resultant theorem permits a large common divisor of the clocks. If \(g\) blocks have the same shortcut length \(b\) and odd count, each is chosen from two different blocks, \(2^b>3^r\), and the selector has least period \(g\), then in the regime \(g\to\infty\), \(\log g=o(b)\), the reduced denominator tends to infinity. For prime \(g\),
\[
 \log d=(1-o(1))gb\log2.
\]
For composite \(g\), the bound retains every active cyclotomic Fourier component and its prime powers. The arbitrary-arrangement and multivalued-variance formulas are in `4.

## 2. Every eventual meeting has a central ordinary clock window

Use the shortcut map \(T(n)=n/2\) at evens and \((3n+1)/2\) at odds. Put
\[
 C_*=\frac{2}{\log(4/3)},\qquad
 I_R=\left[C_*\log R-B\sqrt{\log R\log\log R},
           C_*\log R+B\sqrt{\log R\log\log R}\right].
\]
Changing the logarithm convention inside the square-root term only changes \(B\).

For independent ordinary samples \(X,Y\) in the resolved patches defined in the proof,
\[
 \Pr(X\sim Y)-
 \Pr\{\exists i,k\in I_R:T^iX=T^kY\}\longrightarrow0.
\]
Here \(X\sim Y\) means that their complete ordinary futures intersect. The two clocks may differ. This captures every eventual merging component, even if a hypothetical component escapes. On the actual correlated head pair only the upper deadline has been established, with absolute \(o(1)\) error.

The upper proof first reaches a polylogarithmic level, then uses a duration mark in the relative first-landing comparison to reach any fixed floor \(K\) in an additional \(O(\log\log R)\) clocks, with limiting miss \(O((\log K)^{-2})\). Only finitely many landing pairs lie below \(K\). Every such pair that eventually meets does so within some finite bound \(b(K)\). Fix \(K\), take \(R\to\infty\), then take \(K\to\infty\). The proof never assumes a quantitative bound on \(b(K)\).

The lower proof tests one arm against the partner's **entire forward trajectory**, with the partner clock unrestricted. Uniform orbit sparsity and the ordinary first-landing atom bound make any early encounter negligible. Independence is used exactly here.

With the stated density input, let \(\delta_C\) be the natural density of ordinary component \(C\). These masses sum to one, and
\[
 \Pr(X\sim Y)\longrightarrow\sum_C\delta_C^2.
\]
The normalized first meeting time therefore has a two-atom limit: finite mass at \(C_*\), and the remainder at infinity. Fixed-target positivity makes universal Collatz convergence equivalent to this **finite central-window probability tending to one**. Its value remains unproved; this checkpoint locates the full finite mass in time.

## 3. Conditioning on a rare residue changes the clock in a known way

Write \(q=2^hm\), \(m\) odd, and select one input class modulo \(q\) in \([X,2X)\). Its first \(h\) parities contain \(p\) odd inputs. Set
\[
 J=\left\lfloor3^pX/2^h\right\rfloor,\qquad Q=3^pm.
\]
The new total-variation comparison identifies \(T^{h+K}n\) with \(T^KU\), where \(U\) is uniform on the entire ordinary interval \([J,2J)\), up to
\[
 O\left(\sqrt{\frac{\log(2Q)}{t+1}}+\frac{(2^t+1)Q}{J}+\frac qX\right),
 \qquad K\ge t.
\]
It is uniform over all later \(K\) and hence over every mark of the complete post-clock ordinary future. The comparison retains a real integer endpoint; it does not substitute a Haar trajectory for an ordinary one.

For \(q=X^{o(1)}\), the error tends to zero at \(t=\lfloor\frac12\log_2J\rfloor\). The full finite meeting mass on two independently selected cells is then located at arm-specific centers
\[
 h+C_*\log J
 =C_*\log X+C_*\log3\,(p-h/2)+o(1).
\]
This also holds for unions of adaptive residue-query transcripts, even when different leaves use different moduli.

For example, the actual class \(n\equiv-1\pmod{2^h}\) with \(h=\lfloor(\log X)^{3/4}\rfloor\) has \(p=h\). Its positive displacement exceeds the entire unconditioned central window. Independent starts from this class retain positive eventual meeting mass, but the probability of meeting by the unshifted central deadline tends to zero. This gives an explicit reason the time shift must survive the source conditioning.

## 4. Formal evidence and independent review

The three Std-only modules contain **11 public theorems**:

| Module | Declarations | Formal scope |
|---|---:|---|
| [MaskDenominator.lean](arithmetic/MaskDenominator.lean) | 5 | Unbounded-list carry congruence, torsion certificate transfer, block carry decomposition, geometric identity, prefix difference |
| [TraceClocks.lean](transfer/TraceClocks.lean) | 3 | Prefix/whole-trace equivalence and exact ordinary/shortcut clock conversions |
| [TraceKernel.lean](spectral/TraceKernel.lean) | 3 | Binary progression lifting, lower height bound, and ternary suffix erasure numerator |

Official Lean 4.34.1 accepted every declaration with warnings treated as errors. The audit found no axioms outside `propext`, `Classical.choice` and `Quot.sound`. The global analytic and Diophantine proofs remain written mathematics. They are not eleven Lean proofs of their full asymptotic conclusions.

The exact replay passed in normal and optimized Python modes: 2,307 complete-modulus carry cases, 443 explicit masks, and 2,026 block selectors, including 468 with inactive Fourier frequencies. [Reproduction driver](check.py) · [Execution record](../../reports/astra-ordinary-boundary-20261124/kernel/CHECKS.json)

Independent reviews reconstructed the new arguments rather than rebuilding the earlier packets:

- [Arithmetic review by the transfer lane](transfer/REVIEW_ARITHMETIC.md).
- [Meeting-window review by the arithmetic lane](arithmetic/REVIEW_MEETING_FRONT.md).
- [Meeting and trace review by the spectral lane](spectral/REVIEW_TRANSFER.md).
- [Ordinary-future and rare-class review by the transfer lane](transfer/REVIEW_PHYSICAL_TAILS.md).
- [Root mathematical review and scope](../../reports/astra-ordinary-boundary-20261124/ROOT_REVIEW.md).

## Closing work still required

The arithmetic route must rule out the remaining unrestricted high-degree cancellation, including arbitrary noncoprime-clock words, or connect it to a universal descent argument. The fixed-source calculation in arithmetic `5 keeps one hypothetical escaping integer fixed and proves large reduced denominators for all its late periodized prefixes; it does not contradict their existence.

The analytic route must prove \(\sum_C\delta_C^2=1\), or a summable estimate on the actual head's color discordance. The whole-future residue comparison supplies neither when conditioning consumes all remaining source digits. The [actual transient-basin construction](spectral/TWO_CLASS_SHADOW.md) demonstrates infinitely many two-class head disagreements even among certified convergers, so profile counting alone cannot make this last inference.

All previous science and receipts are preserved. [Frozen latest-work connections](LATEST_CONNECTIONS.md) · [Previous checkpoint](../astra-closure-20261124/README.md)
