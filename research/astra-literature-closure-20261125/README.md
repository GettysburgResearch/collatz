# Exact carry returns and regeneration on the original source interval

**PROPOSED research packet; universal Collatz convergence remains OPEN.** This pass continues the diagonal-closure packet at `1f1d3d690d7517e1b2a44b5f2f4930bd45b63302`. Three GPT-6.2 Astra agents at ultra effort attacked the actual carry, the whole inverse basin of a bounded cycle, and the original ordinary source interval. The new positive results are an exact smaller canonical return and a source-qualified return to genuine four-trit heads at polynomial landing heights. Primary literature is used with its hypotheses retained.

Throughout, the shortcut map is

\[
T(n)=\begin{cases}n/2&2\mid n,\\(3n+1)/2&2\nmid n.\end{cases}
\]

Write `Good n` for a finite hit at 1, and count odd departures separately from total clocks. A displayed hypothetical bad integer is never supplied by a finite numerical test.

## 1. A smaller source with the original upper certificate

For every integer \(a\ge0\), set

\[
z=89585+48\,2^{19}a,\qquad w=1121+48\,3^8a.
\]

Both numbers are 17 modulo 48 and \(0<w<z\). Their two physical arms have their first equal-grade crossing at clock 14. Using two low reference trajectories, from 10 and 3, gives

\[
\operatorname{Good}(z)\iff\operatorname{Good}(w),\qquad
T^H(3z)=1\Longrightarrow T^{H-19}(3w)=1,
\]

with exactly eight fewer odd departures on the transferred hit. The original upper hit covers the matching clock even when it is the first hit. Thus a reverse disagreement on this entire progression descends to a smaller reverse disagreement. This extends the previous aligned-carry mechanism to a crossing at which the upper state is odd.

The return concatenates to every prescribed finite depth: there are unbounded ordinary starts with \(N\) strict replacements, preserving the same supplied upper suffix while saving \(19N\) clocks and \(8N\) odd departures. A fixed component can be reached through such a chain by an explicit two-odd inverse construction inspired by Monks et al. The source depends on \(N\); an infinite chain for one positive start is not claimed.

The paired endpoint is exact. For a fixed positive 3-unit \(x\), the chosen terminal \(w\) satisfies

\[
T^{4+k}w=x,\qquad T^{4+k}(3w)=3^{k+1}x-1.
\]

Yu's theorem on \(3\)-adic logarithmic forms proves that this particular entry requires \(k\) at least exponential in \(N\), with a constant depending on \(x\). The construction supplies neither a smaller terminal than \(x\) nor a known hit from \(3^{k+1}x-1\). These are the two missing properties of a universal paired entrance. The packet also proves a second moving-origin return and precise limits on low-reference and cheap inverse-word repairs. [Carry statement, proofs and literature](carry/README.md)

## 2. Actual disagreements return to much smaller head rows

Keep the original PR197 interval of parents, its physical query envelope, and its separately stated source-population hypotheses. Let \(d\) be the logarithmic row height, \(W\asymp\sqrt{d\log d}\), and \(Y\ge d^B\) a sufficiently large polynomial floor. All sites in every eligible query window are transferred together, with exceptional mass \(O_A(d^{-A})\). At each first entrance below \(Y\), the affine error is \(O_A(\log d)\), rather than an unspecified power of the landing height. The absolute clocks lie in a common interval of length \(O_A(W)\).

For a fixed landing ordinate and clock, the narrow original row permits only one ternary grade. This bounds source fibres without paying separately for every window, path, site or seed. On truly discordant parents the pinned native merger theorem improves the fibre cost by \(d^{-1/2}\), applied on the whole ordinary interval before selection.

An opposite-color query pair consequently yields a nearby ordinary adjacent disagreement. A bounded dyadic multiplier places it in the desired mantissa interval. If successive base-81 parents fail to give a true head, their shared boundary is divisible by successive powers of 81. Retaining that exact boundary gives the smaller-head recurrence

\[
w\ll_A d^{-A}+\frac{(\log d)^{3/2}}{Y}
\#\{z\in\mathcal H_J:cY/d^D\le z\le CY\},
\]

where \(\mathcal H_J\) consists of actual children with different color from \(\lfloor z/81\rfloor\) in a fixed mantissa interval \(J\subset(7,8)\). The source fraction \(w\) retains the upstream hypotheses; no unconditional positive source density is asserted. The estimate holds at every floor up to \(2^{\beta d}\), for fixed \(\beta<0.34\), and gives a harmonic bound over dyadic floors without counting a repeatedly used head at full cost each time.

At \(Y=d^B\), the returned logarithmic height is \(d'=\Theta(\log d)\). This is below the earlier head-incidence range. The missing iteration is quantitative: input \(w\asymp d^{-3}\) need yield only exponentially small mass in \(d'\), below the polynomial population required for another use of the resampling theorem. [Source argument and exact assumptions](source/README.md)

## 3. A whole-denominator coordinate on the inverse basin

For a positive odd rational cycle with coprime odd and shortcut periods \((p,h)\), minimum \(s\), and reduced denominator \(d_0\), every positive odd ancestor in the same denominator lattice has an integer label \(L\). A unit \(u\) modulo \(d_0\) satisfies \(u^p=2\), \(u^h=3\). For any two ancestors,

\[
\operatorname{den}(z'-z)=
\frac{d_0}{\gcd(d_0,u^{|L(z')-L(z)|}-1)}.
\]

Adjacent labels retain the whole denominator, including all prime powers; equal labels give an even integral difference. A real-height estimate applies simultaneously to arbitrary inverse words and all terminal phases. When every departure is at least \(s/3\), all distinct sources through depth \(K\) are at least two apart if

\[
2p/3+2K+6<s\log(2)/p.
\]

This is a limitation on inferring ordinary integrality from local spacing. An exact nonordinary control has a 301,971-bit denominator and satisfies that spacing conclusion through 762,148 odd steps on its floor-clipped basin. The theorem does not assert the floor for all its paths. A separate polynomial-size enumeration tests every potentially forbidden inverse source on supplied ordinary progressions through depth 384 at eight endpoints. Neither result excludes every bounded ordinary cycle. [Cycle theorem, exact control and remaining inference](cycle/README.md)

## Formal and review scope

The six new Lean modules contain 32 public theorems: 14 in the carry lane, 11 in the source lane, and 7 in the cycle lane. The asymptotic source transfer, global rational label construction, and applications of published number theory are written mathematics. They are not presented as kernel-checked theorems. All project imports and public axiom reports are included in the fresh replay.

[Final proof obligations](FINAL_PROPOSAL.md) · [Literature and frozen intake](LITERATURE.md) · [Independent mathematical review](../../reports/astra-literature-closure-20261125/ROOT_REVIEW.md) · [Replay driver](../../reports/astra-literature-closure-20261125/replay.py)
