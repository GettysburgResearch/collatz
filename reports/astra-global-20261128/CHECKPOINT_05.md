# Checkpoint 5: multiplicative meetings, divisor fates and native postminimum paths

**Collatz remains unresolved. The nine-hour pass continues.** This checkpoint extends published head `0e4b428211b0bce432efc7d9d19ff4ea552248ec`. Scientific work was frozen at approximately 02:45 UTC on 28 November 2026; the requested endpoint remains 07:56:49 UTC. The new manuscripts below have received independent coordinator review. Their analytic and Diophantine inputs remain explicitly source-qualified. Four new Lean modules prove finite arithmetic interfaces; none silently imports an infinite Collatz conclusion.

## Fixed multiplicative ratios have two different meeting clocks

For the ordinary shortcut map, let
$$
 H_{A,B}(n)=\min\{\max(s,u):T^s(An)=T^u(Bn)\},
$$
with infinity for disjoint forward orbits. The [multiplicative meeting theorem](../../research/astra-global-20261128/cycles/MULTIPLICATIVE_MEETING_TIME.md) fixes positive integer multipliers $A,B$ and samples ordinary $n\in(X,2X]$. Both dates are genuinely optimized and may differ.

If $A/B\in\langle2,3\rangle$, the horizon is tight, with limiting tail $O_{A,B}(h^{-1/2})$. Doubling gives an immediate one-step meeting. Tripling uses the actual first branch from odd $x$ and counted synchronization of $3x,3x+1$. Stripping a common power of two and joining a finite chain of multipliers preserves the tight tail.

For every ratio outside this group, put $\mu=2/\log(4/3)$. For every $g_X/\sqrt{\log X}\to\infty$,
$$
 \Pr\{H_{A,B}\le\mu\log X-g_X\}\longrightarrow0.
$$
The deterministic part is an exact positive-offset identity. A putative meeting forces a nonzero fixed-base logarithmic form involving $A/B,2,3$ to be small. Matveev's bound then forces one of the two true cumulative parity counts to have accumulated source loss at least $\log n-O_{A,B}(\log(2+h))$ by the meeting horizon. The precritical binomial estimate is used at a grid of dates with spacing proportional to $g_X$. Monotonicity of the actual odd count fills the intervening dates. The resulting Gaussian tails sum without an extra logarithmic loss.

This source input is PR215's **true native count** estimate (2), pinned at `7902faf17d50851b46cdcd420ae479d19f0c845c`. The coordinator read its full stopped-size-walk argument and checked the use of its signed endpoint/native-clock transport. It applies beyond the elementary complete-parity-word horizon. The proof does not declare the whole original parity path iid. A separate pointwise consequence of the logarithmic form and simple-path reciprocal packing forces an actual visit below a multiplier-dependent polynomial in the meeting horizon.

With the separately stated minimum-tightness and fixed-minimum Gaussian inputs, the other finite tail also vanishes:
$$
 \Pr\{\mu\log X+g_X<H_{A,B}<\infty\}\longrightarrow0.
$$
Truncate to finitely many true minima. Every pair in a common component has one fixed pair of merger dates; their finite maximum is harmless beside $g_X$. This includes hypothetical shared escaping components. The result leaves the eventual meeting mass undetermined. For example, $n,3n$ meet at a tight horizon in ordinary sampling; finite meetings of $n,5n$ concentrate in the critical square-root window. A limiting Gaussian law for this pair statistic is not asserted.

There is also an elementary bound uniform in moving multipliers. Clearing the smaller binary denominator leaves a nonzero integer coefficient of $n$ whenever $A/B\notin\langle2,3\rangle$. Both positive affine offsets are smaller than $3^{\max(s,u)}$, so every meeting forces $n<3^{\max(s,u)}$. This finite assertion uses no logarithmic-form estimate.

## Entire component laws on almost primes and complete small-prime signatures

The [almost-prime theorem](../../research/astra-global-20261128/cycles/ALL_SEMIPRIME_COMPONENTS.md) transports the entire countable component distribution, in total variation, from ordinary integers to unrestricted semiprimes and to products of any fixed number $r\ge2$ of primes. No RH input is used. The component distribution need not first be shown to converge. Hypothetical escaping components are retained.

For semiprimes the arithmetic input is Evans's published full semiprime correlation theorem. A triangular second-moment calculation gives an $L^2$ short-window law, including the exceptional shifts and the singular-series mean. Brun–Titchmarsh bounds semiprimes in each binary residue class; the arbitrary-offset counted-fusion estimate then transfers every bounded component test. The proof uses $H=\exp(\log X/\log\log X)$, and the coordinator checked its compatibility with the actual theorem and the proof's almost-prime factor range. For higher fixed orders, complete semiprime completions saturate the largest-prime partner multiplicity. The proof does not replace the population by a hand-selected semiprime subfamily.

The same comparison preserves cleared first-hit records: miss, exact shortcut date, exact odd count, landing, and the final ordered parity word. The real survival mark is tested in bounded-Lipschitz norm. A convenient common clearance is $2^\ell B\le X^{4/5}$; no claim is made at arbitrary source/floor separation. A random largest-prime-and-partner deletion chain on even-order almost primes has the stated independent fixed-fate limits. This does not assign that law to the deterministic pair of the two smallest primes. Prior restricted semiprime ancestors, prime transport, and prime-factor/product results in PR213 and Papers221/233 are credited.

Write $D_z(n)=\prod_{p\le z}p^{v_p(n)}$. The [full signature theorem](../../research/astra-global-20261128/cycles/SMOOTH_DIVISOR_FATES.md) gives, for $z\ge2$ and $\log(2z)=o(\log X)$,
$$
 d_{\mathrm{TV}}\big(\mathcal L(C(N),D_z(N)),
       \mathcal L(C(N))\otimes\mathcal L(D_z(N))\big)\longrightarrow0.
$$
Here $N$ is ordinary uniform in $(X,2X]$ and $C(N)$ is its actual eventual component. This controls **every joint test of the complete prime-power signature**, including arbitrary nonlinear functions of all the valuations. It is stronger than a list of correlations with individual multiplicative functions. The same cleared stopped-record and real-mark qualifications apply.

Conditioning on the signature writes $N=dm$ with $m$ having no prime factor at most $z$. The fundamental sieve lemma gives uniform interval and binary-progression counts. A logarithmic-moment truncation controls $d$; a separate geometric tail controls its power of two. Counted fusion, rough-number smoothing, and a tiling comparison show that every retained conditional law has the same ordinary component mean, uniformly over its own chosen test. The signature marginal itself tends in total variation to independent geometric prime valuations. The coordinator read Ford's precise fundamental-lemma statement and checked the remainder levels used here.

## Deterministic divisor chains must change nonconstant fates many times

At widely separated cutoffs, the same manuscript proves joint independence of the fates of the deterministically selected smooth divisors. For fixed $k$, assume $z_1\to\infty$, $\log z_{i-1}=o((\log z_i)^{1/200})$, and $\log z_k=o(\log X)$. For fixed component or odd-target events of densities $d_i$, the joint event on $D_{z_1}(N),\ldots,D_{z_k}(N),N$ has limiting probability $\prod_i d_i$.

The proof uses independent prime bands under the geometric signature law. Matomäki–Radziwiłł's 2016 short-interval theorem supplies a uniform **absolute** error $(\log T)^{-1/150}$. The spacing makes this adequate after the harmonic band normalization. The unquantified ordinary-density error keeps its factor equal to the band population; losing that factor would invalidate the argument. The coordinator checked the published uniform parameter statement and the complete partial-summation step.

One can retain a growing number of bands without accumulating a dimension-dependent total-variation error. Choose $\log z_{j+1}=(\log z_j)^{201}$. Conditional expectations of a fixed fate given the entire earlier signature tend to its ordinary density. Bounded martingale differences give empirical fate and switch laws. At ordinary scale $X$, all $k\sim\log\log\log X/\log201$ observations are a deterministic function of one full signature, so one total-variation comparison transfers the entire vector.

Let $s_j$ be the canonical divisor chain obtained by adding each distinct prime factor, in increasing order, with its whole exponent. For any fixed fate indicator $F$ of density $0<d<1$, and every $c<2d(1-d)/\log201$,
$$
       \sum_j |F(s_j)-F(s_{j-1})|\ge c\log\log\log n
$$
on a natural-density-one set of ordinary integers. Every fixed ordered word of positive-density fate events occurs along these canonical chains. This already has a concrete application: the predecessor sets of $5$ and $85$ are disjoint, both have positive density under the cited predecessor input, and their own forward trajectories never visit each other. Almost every integer's canonical divisor chain therefore contains arbitrarily many prescribed alternations of those actual visit events.

Under the same positivity input, universal convergence is equivalent to bounded prime-factor variation of the visit-one test on some set of positive upper natural density. The manuscript does **not** prove that bound. It also derives a divergent prime-influence Euler sum by separating single-prime additions from a summable repeated-prime error. These statements do not exchange a finite subpower signature with the full factorization of a fixed integer.

## Stopped clock characters and the native Lean interface

The [stopped-clock analysis](../../research/astra-global-20261128/cycles/STOPPED_CLOCK_SYMMETRY.md) retains a moving bounded stopping set, genuine first-hit time and odd count, arbitrary exact terminal labels, a final parity word, and the original real survival product. Counted consecutive synchronization gives approximate source-dilation eigenrelations. A unimodular pair of continued-fraction convergents supplies a nontrivial character contrast. Together with the cited irrationality measure this gives sharp-cutoff residue estimates. Compactly supported Mellin frequency windows instead admit a smooth inverse of the two dilation multipliers and the stronger stated window error. The resonant real mark is handled with an explicit positive survival cutoff; a singular unbounded Lipschitz factor is not used.

The coordinator's [StoppedRecord.lean](../../research/astra-global-20261128/root/StoppedRecord.lean), independently reviewed by the cycle agent, proves the finite interface directly on the ordinary shortcut map. Height clearance prevents an early hit before a counted merger. The first date, accumulated odd count, actual landing and complete final parity word then agree. The actual unshifted product equals $3^k n/(2^s y)$, lies in $(0,1]$ for positive sources, and obeys the exact merged-source ratio and shift bound. This product is distinguished from the older shifted cofactor weight. No merger-frequency, sieve, irrationality or density hypothesis is part of that Lean module.

PR215's newer component-clock and smooth Mellin results are explicitly compared and credited. They have different homogeneous and quotient-clock scopes. The present statement retains a moving first-stop record and a sharp ordinary source cutoff; it does not claim that prime sampling or component-clock symmetry originated here.

## The postminimum trajectory pays for every later downward return

The [postminimum flux theorem](../../research/astra-global-20261128/escape/POSTMINIMUM_FLUX.md) disintegrates the original ordinary source measure by its first global minimum. Each donor and every subsequent site is a genuine positive integer. Write $\gamma_m$ for the retained minimum charge and $\eta_m=\gamma_mF(m)$ for its escaping part. Their tails are controlled by the stated minimum inputs and $\sum_m\eta_m=H$.

For a floor $B$, the surviving postminimum outward flux is exactly
$$
 Q_{\rm post}(B)=\sum_{m\le B}\eta_m+
                         \sum_m\eta_m N_m^-(B),
$$
where $N_m^-$ counts actual downward crossings after the minimum. Every escaping path has infinitely many downward edges spanning an interval of fixed relative width. After exhausting the donors of one component that have joined its common tail, this yields
$$
       \limsup_{B\to\infty} Q(B)
          \ge \frac{\log(3/2)}4+H+\max_C H_C.
$$
The proof gives the corresponding lower bound on arbitrarily high proportional intervals. It does not synchronize the downcrossing dates of all components.

The logarithmic floor integral controls each donor's actual number of visited sites below a height. A zero-exponential-speed escaping component forces that integral divided by $\log B$ to diverge. At positive speed, a fixed donor with a limiting exponent-one frequency has an exact outward coefficient. Infinite mixtures are treated only in the justified Fatou direction. Fixed-arity arithmetic gives a secondary integrated excess larger than every fixed multiple of $\log\log B$; the stronger explicit $\log\log B\log\log\log B$ term uses the additional unrefereed Paper15/v2 input.

The full discounted postminimum outward-minus-inward flux tends to $H$, and the corresponding preminimum difference tends to $-\kappa$, where $\kappa=\log(4/3)/2$. These follow from an exact finite telescoping identity with the kill on the departed state. Weaver Paper176 already supplied the total loss $\sum_y(1-w_y)a_y=\kappa-H$; this is credited as prior work. [PostminimumLevelBalance.lean](../../research/astra-global-20261128/escape/PostminimumLevelBalance.lean) checks the finite level balance, its low-to-high consequence and the actual survival-weighted split at any supplied date, allowing repeated states and returns.

## Critical geometric grids retain the original positive representatives

For an odd edge of exponent $e$, choose grid ratio $g_1=3/2$ and $g_e=2^e/3$ for $e\ge2$. Its ideal multiplicative edge crosses exactly one grid level. The actual positive offset adds or removes one precisely when the interval $[y,y+1/3)$ contains a grid point. The [critical-grid theorem](../../research/astra-global-20261128/escape/CRITICAL_GEOMETRIC_SAMPLING.md) shows
$$
 \int_0^1\sum_y w_ya_y\,|C_\theta(y)-1|\,d\theta
       \le\frac{\kappa-H}{\log(4/3)}.
$$
This is finite total variation over the entire original graph, even if its raw occupation is infinite. Actual donor and date marks can be retained.

A separate deterministic argument holds at every phase, even with an independently selected phase for each exponent. Every escaping integer ray has only $o(N)$ defective edges through odd date $N$, uniformly over those phases. More generally, any fixed geometric base generated by two and three approaches its true sites from above within an absolute distance $c<1$ on only $o(N)$ dates, uniformly over all translates of the progression.

The proof uses the exact physical coordinate $\log r_i=\log(m/F(m))+i\log3-S_i\log2+\log F(r_i)$. Two late candidate sites with the same integral coefficient class cannot reuse the same grid slope beyond a bounded cluster: the actual affine offset is at least $1-(2/3)^{j-i}$. Irrational-rotation counting treats the remaining coefficient classes. Large exponent classes are paid for by the true total division count. The conclusion also holds after integration over all original postminimum charges. On the cited two-logarithm input, superpolynomially growing rays have the stronger $O_m(\sqrt N)$ error.

[NativeOffsetFloor.lean](../../research/astra-global-20261128/escape/NativeOffsetFloor.lean) proves the native denominator-cleared inequality $3^j(x+1)\le2^s y+2^j$ on every supplied actual positive-gap odd segment, and its one-third-strip consequence. The grid theorem still does not supply an upper bound on raw late crossing multiplicity.

## How complicated must an actual parity word be?

The [finite power-tree theorem](../../research/astra-global-20261128/broad/FINITE_POWER_GRAMMAR.md) permits bit leaves, concatenation and arbitrary integer powers, with arbitrary nesting and no exponent-length charge. On every simple positive input segment, its minimum tree size divided by $\log(1+T/B)$ tends to infinity uniformly as $T/B\to\infty$, where $B=\log_2(x_0+1)$. Shared references are counted separately in this tree theorem. The proof combines logarithmic-time bounds for the union of short-period windows with a finite-depth extraction and a disjoint-subtree count. [PowerTreeArithmetic.lean](../../research/astra-global-20261128/broad/PowerTreeArithmetic.lean) checks its finite shared-prefix and literal-power height interfaces.

For [copies from arbitrary previous positions](../../research/astra-global-20261128/broad/PREVIOUS_FACTOR_ADDRESSES.md), a separate theorem handles exact matches ending at their first discrepancy, with final truncation allowed. Put $c=\log_2(3/2)$ and $D=\log(1+T/B)$. Every such parse with $O(D)$ packets must obey
$$
 \liminf\frac1D\sum_i\frac{b_i}{B+a_i}
       \ge\frac{1-c}{2c}=0.3547556\ldots,
$$
where $a_i$ is the destination date and $b_i<a_i$ its actual earlier source. Copies with vanishing relative addresses occupy at most $c$ of logarithmic time. The fixed-arity Evertse bound charges the two neighboring source addresses only after their corresponding destinations become visible; integration controls those charges without pretending the earlier states have bounded height.

With arbitrary shared grammar nodes, a finite traversal gives $\int_0^Tdt/H(t)\le2g+1$, where $H$ is the prior maximum shifted bit length and $g$ counts reachable rules. Every fixed subexponentially growing aperiodic positive ray therefore has superlogarithmic grammar size even with arbitrary sharing. A finite dyadic factor-count estimate records what this gives toward the earlier local factor-complexity criterion. Unrestricted growth and unrestricted comparable-time references remain outside the superlogarithmic shared-grammar conclusion.

Finally, [the Gaussian repair calculation](../../research/astra-global-20261128/broad/GAUSSIAN_CLOCK_REPAIR.md) records a failed proposed extension instead of promoting it to an irregular-clock theorem. A single bounded cumulative-clock defect introduces the exact reduced denominator outside two and three
$$
                \prod_{d=1}^{n-1}(3^{hd}-2^{hd})
$$
in one normalized Gaussian interpolation coefficient, for even $h>0$. Lagrange interpolation proves this formula. Its quadratic logarithmic size consumes the unperturbed height margin in the direct repair; the formal inverse correction also has infinite support. Other auxiliary forms or further cancellation in the final form are not excluded.

## Verification, source review and publication

The fresh [Lean replay](CHECKPOINT_05_LEAN.json) passed **35 modules and 1,082 declarations**, including **162 private declarations**. The axiom audit accepts only `propext`, `Classical.choice` and `Quot.sound`, including for private and generated declarations. All **21 finite control programs**, **42 ordinary/optimized runs**, passed with identical paired outputs in the [bounded replay](CHECKPOINT_05_BOUNDED.json). The pinned environment remains Lean 4.34.1 and the same clean Mathlib checkout and dependency manifest; the run rebuilds this packet and its explicit earlier imports, not all of Mathlib. Source hashes were checked at both ends of the replay.

The new finite controls include 43,008 native affine rows, 2,007 genuine meetings with 1,770 unequal-date pairs, 512 disjoint-prefix comparisons, 8,000 signature factorizations, 729 independent bounded geometric signatures, 24,576 actual/ideal grid comparisons, 1,211 original minimum splits, and 37,422 native offset comparisons. The grammar control checks 254 exhaustive short words, 100 simple ordinary prefixes, 3,102 literal powers, 1,136 shared copies, 4,588 boundary inequalities and 105,283 signed transports. The Gaussian control solves 32 systems by exact rational elimination. These are finite checks of the stated identities, not evidence of universal convergence.

The coordinator independently reconstructed the new written proofs and checked their exact source interfaces. The cycle agent separately reviewed the coordinator's stopped-record Lean module. New primary inputs checked directly include Evans's full semiprime theorem, Ford's fundamental sieve lemma and the published Matomäki–Radziwiłł theorem. The overlapping source frontier was refreshed at the three exact heads listed in the packet README; prime transport, total stationary loss, component-clock symmetry and earlier complexity results are credited.

Publication uses a clean scientific commit, a complete-checkout regression receipt, a GitHub tree matching the validated local tree exactly, and an expected-parent branch update. The published checkout is checked again. PR212 remains a draft. The next work targets stronger canonical prime-factor mixing, untrimmed critical real-fibre moments, an optimal inverse-pressure endpoint, and the still-missing global cycle and raw-escape bounds.

The clean scientific freeze is `5af427675b6fbf9dafc2ee1fb772671f28213e99`, tree `a23e8ee463271552f75a63a1e6fde4a29a232ff2`. Its [complete-checkout regression receipt](CHECKPOINT_05_INTEGRITY.json) passed before this publication receipt was added. The final published commit is checked again after the branch update.
