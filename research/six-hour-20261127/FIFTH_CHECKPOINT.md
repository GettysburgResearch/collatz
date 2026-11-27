# Fifth checkpoint: ordinary safe suffixes and strict cycle-rank convexity

**Collatz remains open.** This checkpoint follows `df2f17a117bea06bb34040a5a97e7dc9711d9871`. Its main additions are an actual ordinary-orbit equivalence proved in Lean, a finite logarithmic bound for its existential suffix, and a written strict-convexity theorem for the canonical height-one cycle class. The written results have fresh independent reconstructions. They do not have complete Lean formalizations unless identified below.

The [root review](../../reports/six-hour-20261127/ROOT_REVIEW_WAVE5.md) records the proof interfaces, priority corrections, frozen identities, and first remaining inference. The [fourth checkpoint](FOURTH_CHECKPOINT.md) retains the exact fifth-moment certificate and its distinct verification scope.

## 1. An actual ordinary equivalence, with a bounded suffix index

For a positive odd integer let

$$
 U(n)=\frac{3n+1}{2^{\nu_2(3n+1)}},\qquad
 E_j(n)=\sum_{i<j}\nu_2(3U^i(n)+1).
$$

Call a source permanently safe when $4E_j(n)\le7j$ for every $j\ge0$. The three modules [PermanentSafeDebt](pointwise/PermanentSafeDebt.lean), [PermanentSafeOrdinary](pointwise/PermanentSafeOrdinary.lean), and [PermanentSafeBitClock](pointwise/PermanentSafeBitClock.lean) prove, on the physical natural-number map,

$$
 \bigl(\forall j,\ U^j(n)\ne1\bigr)
 \quad\Longleftrightarrow\quad
 \exists t\le80(\lfloor\log_2n\rfloor+1),\
       \forall j,\ 4E_j(U^t(n))\le7j.                 \tag{1}
$$

Every odd source is covered; the theorem does not assume a globally least counterexample. If $n\le2^b$ and its orbit is bad, the genuine first safe suffix is at most $80b$. The first-suffix definition is noncomputable, with kernel-checked safety and minimality. Its existence does not make the infinite predicate decidable.

The proof telescopes the exact recurrence using $81(3x+1)^4\le10000x^4$ for $x\ge3$ and the integer inequality $2\cdot10000^{20}\le10368^{20}$. After $80b$ steps, the physical debt $7j-4E_j$ is nonnegative. Its global minimum lies in the preceding finite prefix; every future increment from that minimum is nonnegative. A source reaching one has valuation two forever after that hit and therefore cannot be permanently safe.

The final universal theorem is an exact equivalence:

$$
 \text{all positive odd sources reach one}
 \quad\Longleftrightarrow\quad
 \forall n\text{ odd},\ \exists j,\ 7j<4E_j(n).       \tag{2}
$$

Neither universal side is proved here. The remaining task is to exclude every permanently safe ordinary source, or to prove the prefix crossing on the right of (2). The [independent formal review](../../reports/six-hour-20261127/ORDINARY_SAFE_LEAN_INDEPENDENT_REVIEW.md) and [bit-clock explanation](pointwise/SAFE_BIT_CLOCK.md) distinguish this completed reduction from the open exclusion.

## 2. Strict convexity in the true rank of a height-one cycle

Consider positive primitive ordinary cycles whose canonical real discrepancy width is $W<2$, equivalently canonical grades zero or one. Accelerated valuation three is allowed. Let $P$ be the least odd period and $L_r$ the canonical scaled integer labels, extended by $L_{r+P}=2L_r$.

The [strict rank-convexity theorem](cycles/STRICT_CONVEX_RANKS.md) proves, for every sufficiently long cycle in this class,

$$
 L_{r+1}>L_r,\qquad L_{r+2}-2L_{r+1}+L_r\ge1.       \tag{3}
$$

The argument uses the published finite irrationality bound for $\log_2 3$, exact unit drift, and both arithmetic wrap interfaces. It does not use a Subspace Theorem, a source-counting estimate, or a binary-valuation restriction. The [fresh review](../../reports/six-hour-20261127/CONVEX_RANK_INDEPENDENT_REVIEW.md) reconstructs the seam avoidance, sign transitions and arithmetic-progression contradiction.

For every $1\le t<P$, (3) makes $L_{r+t}-L_r$ strictly increasing in $r$. Thus all fixed-rank gap fibres are singletons. The adjacent gaps also satisfy $g_0\le g_r<2g_0$ and

$$
 L_0\ge\frac{3P^2-P}{2},\qquad
 0<L_{r+t}-L_r\le\frac{8tX}{P},\quad X=\max_i x_i.  \tag{4}
$$

Eleven local sign and parity interfaces are proved in [RankConvexityInterfaces](cycles/RankConvexityInterfaces.lean). The global asymptotic theorem (3), including its imported Diophantine estimate, remains written mathematics.

### Consequences for actual cyclic disagreements

The [all-lag consumer](cycles/CONVEX_RANK_CONSUMERS.md) removes the earlier population-estimate input from the height-one entropy argument. Every proper chronological lag has limiting valuation-mismatch fraction strictly greater than $1/1000$ with the published 2018 logarithm estimate, or strictly greater than $1/36$ with the separately quoted 2026 exponent-three input. These are restrictions on growing hypothetical cycles, not their exclusion.

For smaller rank offset $t=P^{v+o(1)}$, $0\le v<1$, the [sharper consumer](cycles/MICROSCOPIC_CONVEX_LAG_BOUND.md) gives, for any limiting mismatch fraction $0\le\epsilon\le2/3$,

$$
 H(\epsilon)+\epsilon\log2\ge\frac{\log3}{M-1+v},     \tag{5}
$$

where $H$ is binary entropy in nats and $M$ is the stated irrationality-exponent bound. For $t=P^{o(1)}$, this yields strict lower limits $1/17$ with the published bound and $5/32$ with $M=3$. Exact integer comparisons certify the numerical margins.

A proposed local induction to strict third-difference signs fails: four columns on overlapping portions of the actual ordinary orbit from 83 have third differences $-1,0,1,1,0,0$ under one legal common calendar, while first and second differences remain positive. The [consumer paper](cycles/CONVEX_RANK_CONSUMERS.md) preserves all rows and the replay. It makes no claim that this local segment occurs at consecutive ranks of a cycle.

## 3. Cycle restrictions beyond the narrow binary class

| Class and hypotheses | Conclusion | Imported analytic input |
|---|---|---|
| Ordinary binary cycles, $W\le2.42$ | Uniform positive valuation-mismatch fraction for every proper lag | Fixed-place separation and published 2018 logarithm bound |
| Primitive positive rational cycles, all positive valuations, $W\le2.1$, full denominator $d=P^{o(1)}$ | $\liminf\log(dX)/\log P\ge60/29$; uniform positive mismatch fraction for every nonresonant lag | Fixed-place separation; the mismatch conclusion also uses the 2018 bound |
| Distinct ordinary binary trajectory segment in $[s,Rs]$, $R<2^{2.42}$ | Length $O_\epsilon(s^{2/5+\epsilon})$ | Fixed-place separation |
| Same finite trajectory problem with $R<2^{2+10^{-5}}$ | Length $O_\epsilon(s^{1/3-1/80000+\epsilon})$ | Fixed-place separation and the audited fifth-moment certificate |

The relevant manuscripts are [classical full-band lags](cycles/CLASSICAL_FULL_BAND_ALL_LAG.md), [unrestricted three grades](cycles/UNRESTRICTED_THREE_GRADE_ALL_LAG.md), and [physical residence](cycles/PHYSICAL_BAND_WINDOWS_AND_OCCUPATION.md). Each has an independent review in the [report directory](../../reports/six-hour-20261127/). A residence bound ends at first exit, nonbinary transition or repetition; it does not prove termination.

For rational cycles put $g=\gcd(A,P)$ and $q=P/g$, where $A$ is the total division clock. The unrestricted lag statement excludes the $g-1$ proper resonant multiples of $q$. The full denominator stays in all source multipliers and rank-copy counts. The ordinary case has $g=1$ in the stated strip.

The [physical occupation transfer](cycles/UNRESTRICTED_PHYSICAL_ODD_OCCUPATION.md) also gives four alternatives for arbitrary positive valuations: either $d>P^\delta$, or more than a $\delta$ fraction of the odd states exceed $R$ times the odd minimum, eventually in least period.

| $R$ | $\delta$ | Input qualification |
|---:|---:|---|
| $12/5$ | $1/5000$ | Published 2018 logarithm bound; elementary counting route |
| $5/2$ | $1/10000$ | Published 2018 bound and fixed-place separation |
| $3$ | $1/100000$ | Quoted exponent-three input and fixed-place separation |
| $31/10$ | $10^{-7}$ | Quoted exponent-three input and fixed-place separation |

**Priority qualification:** the independent review derives all four ordinary $d=1$ numerical rows from Weaver 181 by a clock-transfer argument, using the newer exponent-three input for the last two. The separate contributions here are the variable full-denominator alternatives, a uniform real-depth-to-physical conversion, and an elementary route for the first row. The [review](../../reports/six-hour-20261127/INDEPENDENT_PHYSICAL_ODD_TRANSFER_REVIEW.md) contains the earlier-source specialization with exact logarithmic enclosures.

## 4. Ordinary safe-entry concentration and sparse visitors

Write $\tau$ for first entry into the permanently safe set, and $C_*=(2-\log_2 3)^{-1}$. The [ordinary entry analysis](pointwise/CRITICAL_SAFE_ENTRY.md) proves that, for each fixed $\delta>0$, the ordinary-octave probability of a **bad source** whose entry time differs from $C_*\log_2 n$ by more than $\delta\log_2 n$, or whose entry height exceeds $n^\delta$, is exponentially small in the octave index. This is an absolute probability over all sampled sources. It does not assert a conditional law given an unproved positive population of bad sources.

The critical trajectory envelope is already available in Inselmann's 2024 Theorem 3.8, and the primary entry concentration follows from that envelope plus the coercive debt argument. The paper also gives an elementary block transport reconstruction and an extension avoiding predetermined polynomially sparse target families before any fixed subcritical time. The latter includes a separately qualified application to all future states of sufficiently few specified visitor orbits.

The [fresh transport review](../../reports/six-hour-20261127/INDEPENDENT_CRITICAL_SAFE_ENTRY_REVIEW.md) checks exact completed cylinders, the affine multiplicity term $+1$, moving octave ranges and repeated square-root losses. No restart is assigned an unsupported uniform endpoint law. The additional visitor-orbit application retains its stated reciprocal-packing dependency.

## 5. Verification and remaining work

The packet-wide replay builds every local Lean module from source with warning-as-error, disabled implicit binders and version-pinned Lean/Mathlib. Every public and private theorem has an axiom report. All finite controls run normally and with Python `-O`; their complete output bytes must agree with the frozen receipts. These controls check finite arithmetic interfaces and certificates. They do not prove imported analytic theorems or the asymptotic steps of the written arguments.

The new exact equivalence leaves a clear unresolved predicate: no positive odd integer is permanently safe. The cycle arguments leave wider discrepancy classes and finite exceptional periods. The strict second-difference theorem offers additional arithmetic structure, but the displayed third-difference counterexample prevents the most direct attempted iteration. No result in this checkpoint converts ordinary-density estimates into an all-source theorem.

Primary external inputs: [Inselmann, Theorem 3.8](https://arxiv.org/html/2402.03276v3), [Bondareva–Luchin–Salikhov, Theorem 1](https://m.mathnet.ru/links/79505d0269e906a6bf62eae1d2929560/cheb619.pdf), [Weaver 114](https://rstation.ai/problems/collatz/papers/114/v1), [Weaver 145](https://rstation.ai/problems/collatz/papers/145/v1), [Weaver 181](https://rstation.ai/problems/collatz/papers/181/v1), and [the separately quoted 2026 exponent-three preprint](https://arxiv.org/html/2610.28079v1#S11).
