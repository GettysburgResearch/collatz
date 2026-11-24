# Translated prime witnesses, cyclotomic denominators, and one directed head patch

**Research checkpoint, 24 November 2026. Collatz remains open.** This continuation starts at PR195 `8edc24b576e7c7da56f99d882ce6fd1e014ee730`. Three GPT-6.2 Astra streams developed the ordinary, arithmetic and head arguments, then reviewed each other's exact files. The controller independently reconstructed the main deductions and rebuilt all five new Lean modules from source. The packet contains **28 checked finite declarations**, written asymptotic proofs, exact finite controls, and explicit external dependencies.

The main results are below. Their full statements and proofs are in the linked notes. The latest repository intake is recorded separately so a moving PR does not silently change a theorem's hypotheses.

| Result | Mathematical scope | Open implication |
| --- | --- | --- |
| [Prime witnesses in every translated interval](ordinary/README.md) | A power-saving exceptional count for logarithmic odd-orbit prefixes; constants independent of interval location | No prescribed exceptional orbit is forced to leave the exceptional set |
| [Quadratic-residue schedules with altered intervals](arithmetic/README.md) | A pointwise lower bound for the **complete reduced denominator**, retaining prime powers and arbitrary changes inside weight-preserving intervals | General cycle words need not have this repeated-clock structure |
| [Cyclotomic degree and many templates](arithmetic/CYCLOTOMIC_DEGREE.md) | The same resultant method with arbitrary reference blocks; a positive denominator exponent for reflection-symmetric schedules | Full cyclotomic degree can make the bound insufficient |
| [One directed transition on one patch](head/README.md) | Under T3, the whole head sum is bounded by one chosen direction and terminating phase on any fixed open patch | The selected directed series has no proved summable bound |
| [Killed moments and a common physical clock](controller/KilledClock.lean) | Six finite recurrence and selection statements, with all source-count hypotheses explicit | The statements do not produce the missing probabilistic estimate |

## 1. Almost every odd source in any interval has a long independent prefix

Let (U(q)=(3q+1)/2^{v_2(3q+1)}) on positive odds. In any interval (I) of (L) consecutive positive integers, consider its odd sources and their first (t) odd states (q_0,ldots,q_{t-1}). Call a state covered if every prime valuation in it is at most the sum of that valuation in all the other states. For every fixed (0<\delta<1/4),

\[
 \#\{x\in I\text{ odd}:\text{some state is covered}\}
       \ll_\delta L^{1-\kappa_\delta},
 \qquad 2\le t\le\delta\log_2L,
\]

for some (\kappa_\delta>0), uniformly over the location of (I). At (t=\lfloor(\log_2L)/16\rfloor), the bound is (O(L^{4/5})). Every state in each remaining prefix has its own strictly dominating prime valuation, which proves multiplicative independence of the entire prefix. For (t=o(\log L)) and (\limsup\log t/\log\log L\le\beta\), the exceptional count improves to (L^{\beta/(1+\beta)+o(1)}).

The useful new counting step works above any translated height. If a set (S) of divisors of (P) has diameter at most (Y), then

\[
 |S|\le(1+\omega(P))\#\{g\mid P:g\le Y\}.
\]

Each large divisor has a first prime-factor product crossing (Y); that product can divide at most one member of (S). A finite Rankin estimate bounds the smaller divisors. Exact Collatz carry identities place covered states among those divisors. A maximal bound on the physical binary prefix multiplier controls expansion, while the binomial clock tail controls unusually long division words. The length of the original interval pays for all these counts; its starting height never enters the clock budget.

Two applications preserve different quantifiers. The published Krasikov–Lagarias theorem gives many predecessors of a **prescribed fixed target**. Combining it with the explicit exception bound yields at least

\[
 (1-o(1))\frac{X^{0.84}}{1+\lfloor\log_2X\rfloor}
\]

odd sources up to (X) that reach that target and have all the logarithmic prime witnesses. PR193's synchronized image bound instead gives many good sources in **each translated interval** meeting at one common (O(\log L)) odd clock; that common endpoint may depend on the interval. Both terminating basins and hypothetical nonterminating basins admit the first application. The population estimate is therefore not a pointwise descent certificate. [Proof, exact inputs, and formal boundary](ordinary/README.md)

## 2. Complete denominators survive structured cancellation

For a binary physical cycle word of length (NL), with (Np) odd bits, put (Q=2^L>P=3^p), let (C) be its literal carry, and let

\[
 d=\frac{Q^N-P^N}{\gcd(Q^N-P^N,C)}.
\]

An integer cycle requires (d=1). Take two distinct length-(L), weight-(p) blocks and place one of them at the nonzero quadratic-residue slots of a prime (N\equiv3\pmod4). Change (r) disjoint circular intervals, each of at most (H) blocks, preserving the **total** odd weight in each interval. Individual cells inside them can change weight and every physical bit may change. For any integer (K\ge1) with (K^r<N),

\[
 d\ge
 \frac{Q^{N-1-4N/K}}
 {\left((r^2+r+(N+1)/4)3^{2HL}\right)^{K^r}}.
\]

For fixed (r) and (H=o(N)), this yields (\log_2d/(NL)\to1), uniformly in the block clocks. A suitable fixed positive fraction of changed slots still leaves an exponential denominator. The construction includes near-critical positive rational cycles with arbitrarily high minima and a positive mismatch fraction at every nonidentity physical rotation. These examples verify the breadth of the exclusion; they do not supply integer counterexamples.

The proof combines a quadratic Gauss-period identity with simultaneous approximation of the altered positions. Its integral resultant is divisible by the **whole** numerical gcd. Nonvanishing follows from a local obstruction: the binomial roots lie in an extension unramified at (N), while the relevant quadratic field is ramified there. This is why neither reduction to the radical nor an unsupported irreducibility assumption is needed. [Full proof and explicit constants](arithmetic/README.md)

The general extension uses the degree (m) of the reference carry sum at a primitive (N)-th root. It allows arbitrarily many different reference blocks. Hensel lifting and the Eisenstein cyclotomic polynomial give the same nonvanishing argument. For an undamaged nonconstant-off-zero schedule invariant under reflection, (m\le(N-1)/2). Parseval and the sharp elementary carry cap then yield

\[
 \liminf\frac{\log_2d}{NL}\ge\tfrac12\log_3 2>0.315,
 \qquad N\to\infty,\quad \log N=o(L).
\]

The method is classical algebra applied to the actual carry. Related sequence determinant methods and the newly inspected PR193 arbitrary-arrangement result are credited in the source and intake records. No historical priority claim is made. [Degree theorem](arithmetic/CYCLOTOMIC_DEGREE.md) · [Latest comparison](../../../reports/astra-global-closure-20261124/round4/LATEST_INTAKE.md)

## 3. The remaining head estimate can be localized and directed

Label an integer (B) if its orbit never reaches one, and otherwise label it (+) or (-) according to the parity of its first hitting time. At row (j), put (R_j=81^j), use child (x) and parent (\lfloor x/81\rfloor), and let (V_N) count all bad–good transitions through row (N) with their natural logarithmic weights.

Choose any nonempty open interval (J\subset(7,8)), either terminating phase, and either one of the two directions. Let (D_N(J)) count just those chosen transitions with (x/R_j\in J), weighted by (1/R_j). Under the pinned first-fusion input T3,

\[
                         V_N\le C_J(1+D_N(J))
\]

for all (N), with a fixed constant. Under the separate fixed-target density input M, summability of this one subseries is equivalent to Collatz.

The proof joins physical parent-child paths without changing their original sources. Third-label errors are summable by T3. Exact doubling swaps the terminating phases. After a telescoping identity, this gives bounded signed Fourier coefficients at every fixed mode; approximation by one fixed trigonometric polynomial then isolates the chosen patch and direction. The argument does not need a uniform high-frequency Fourier bound.

The optional restriction to PR201's remaining mesoscopic two-class profiles additionally uses its pair-chain input P. At a first landing, the terminating phase also requires the actual clock parity. Unmarked landing values or separate endpoint marginals do not supply this information or the missing summability. [Theorem, dependencies, and remaining event](head/README.md)

## Verification and reproduction

The controller rebuilt all five new modules in a fresh project output directory with Lean 4.34.1, `-j1 -DwarningAsError=true`, using the recorded Mathlib/package cache. All 28 selected transitive axiom inventories contain only `propext`, `Classical.choice`, and `Quot.sound`. Source hashes were unchanged across the build. These are finite interfaces: the entropy limits, cyclotomic local-field argument, Fourier approximation and external probabilistic theorems are written proofs. [Exact Lean receipt](../../../reports/astra-global-closure-20261124/round4/lean/receipt.json)

| Module | Checked declarations | Scope |
| --- | ---: | --- |
| `TruncatedDivisors` | 6 | First crossing, translated divisors and rows, finite Rankin inequality |
| `DyadicCutoff` | 4 | Physical affine law, one binary residue, finite first-passage bound |
| `PaleyResultant` | 5 | Period algebra, short exponents, full-modulus resultant divisibility, reducedness interface |
| `PhaseCut` | 7 | Label identities, physical-path abstraction, telescoping, horizontal recurrence |
| `KilledClock` | 6 | Killed recurrence, survival, charge, one clock for a whole source family |

Normal and optimized Python both reproduced all four control outputs: eight passing runs. They include 6,102 translated divisor windows, 12,288 odd-source probes, 720 altered-word resultants, 9,280 template pairs, 5,640 rotations, 8,064 affine lifts and 62,208 head paths. A separate example verifies divisibility by (31^2). Finite counts are not extrapolated into asymptotic proofs. [Control replay](../../../reports/astra-global-closure-20261124/round4/controls-replay.json)

Run [check_lean.py](check_lean.py) with explicit `--lean`, `--mathlib`, optional `--runtime-library`, and `--report-dir` arguments. Run `python -B research/astra-global-closure-20261124/round4/check_controls.py --report /tmp/collatz-round4-controls.json` from the repository. The latter needs SymPy for the independently written prime-power example; the three main control scripts use the standard library.

[Controller reconstruction](../../../reports/astra-global-closure-20261124/round4/ROOT_REVIEW.md) · [Ordinary review](../../../reports/astra-global-closure-20261124/round4/arithmetic/REVIEW_ORDINARY.md) · [Arithmetic and clock review](../../../reports/astra-global-closure-20261124/round4/head/REVIEW_ARITHMETIC.md) · [Head review](../../../reports/astra-global-closure-20261124/round4/ordinary/REVIEW_HEAD.md) · [Pinned sources](SOURCES.json)

The final metadata refresh returned 161 PRs; the source and intake records identify the particular proofs actually inspected. Earlier proof bundles and external formalization archives were not globally rebuilt. Publication receipts separately certify complete-checkout integrity. The next unresolved mathematical task is still a universal ordinary-source implication: a summable bound for the selected directed head mass, a forced original-floor descent, or a denominator exclusion covering every remaining cycle word.
