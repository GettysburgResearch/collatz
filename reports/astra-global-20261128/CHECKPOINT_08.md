# Checkpoint 8: strict memory improvement, sharp positionwise limits and critical deadline entropy

This is the eighth checkpoint of the nine-hour pass, whose scheduled end is 28 November 2026 at 07:56:49 UTC. Its published parent is `21f5cfef697de0941200286abaef2f8373d6915a`. All three research agents used GPT-6.2 Astra with ultra reasoning. The work remains on draft PR212.

**The Collatz conjecture is not proved.** This checkpoint resolves several substantial questions about the available methods and supplies a genuine improvement theorem for every finite inverse controller. It also gives a fixed, exactly computable forward-orbit observation with positive multiplicative entropy beyond the binary observation horizon, under the named ordinary landing and clock inputs. These conclusions have different proof scopes, stated below.

## 1. Every finite inverse window can be strictly improved

Let `c_W` be the minimum stationary mean inverse gap for a controller seeing `W>=2` ternary digits, with the actual uniform fresh top trit after each legal inverse division. Let `L=inf_W c_W`. The [strict improvement theorem](../../research/astra-global-20261128/broad/STRICT_FINITE_WINDOW_IMPROVEMENT.md) proves

$$
c_{W+n}\le c_W-\frac{3^{-n}}n,
\qquad H=3^{32W},\qquad
n=32W\left\lceil\frac{256H}{32W}\right\rceil.
$$

Thus **no finite window attains the actual unrestricted optimum**. This remains true if that optimum is strictly above the known Shannon bound `a_*`, defined by

$$H(a_*)=\log3,\qquad H(a)=a\log a-(a-1)\log(a-1).$$

It is not an assertion that every pair of adjacent widths has different values. The guaranteed numerical improvement is tiny; the new conclusion is strict nonattainment at every finite memory, without first having to identify the limiting optimum. Weaver's earlier finite-window completeness theorem supplies the interpretation of this limit as the reciprocal Haar-optimal inverse slope. His separate finite-width entropy gaps concern the entropy ceiling, which is a different comparison.

The proof uses the exact arithmetic of signed rational paths to build improvements on **positive ordinary source cells**. For each initial observed row, construct a periodic negative rational path of length `32W` and total gap at most `39W`. One part of the period starts at row `-1 mod 3^W` and requires gap five; another part presents the same row and requires gap one. A deterministic width-`W` rule cannot follow a full lap.

After that rule leaves the comparison cycle, it cannot revisit any state. Each rational state has a unique true forward odd predecessor, determined by the two-adic valuation of `1+3y`. A repeated inverse state would create a forward cycle in the same component, which is incompatible with departure from the original cycle. All subsequent numerators are therefore distinct positive integers in one fixed negative rational lattice.

For a path `-u_j/D`, its literal recurrence is

$$3u_{j+1}=2^{e_j}u_j+D.$$

If `T_n` is its total gap, multiplying these identities and sorting the distinct numerators gives

$$
3^n\le 2^{T_n}u_0\binom{n+D}{D}.
$$

The explicit `H,n` above make the baseline cost exceed the periodic alternative by at least `61H`. A finite Bellman bias has span at most `6*3^(W-1)`: from any row a suitable exponent makes the next state hit any specified row with probability one third. The cost difference therefore survives the terminal-bias correction.

In each initial row, substitute the cheaper word on one full source cell of depth `W+n`. Its conditional Haar mass is exactly `3^-n`. Both finite words are genuinely legal on that cell, including on all its positive odd integer representatives. They consume the consulted digits and leave a Haar tail at the block boundary. Averaging over a stationary block-boundary law and then disintegrating its finite occupations produces a valid stationary rolling controller of width `W+n`, proving the displayed improvement.

The new [SignedDistinctCost.lean](../../research/astra-global-20261128/root/SignedDistinctCost.lean) proves the extremal product, the native recurrence calibration, the endpoint with terminal numerator retained, and the exact binomial inequality. Its hypotheses explicitly supply distinctness and positivity. The cycle construction, nonrepetition argument, Bellman equation and stationary-controller construction are independently reviewed written mathematics. The [formal scope note](../../research/astra-global-20261128/root/SIGNED_DISTINCT_COST.md) connects the statements precisely.

## 2. All deterministic finite-window rules lose on the same critical sources

The [simultaneous regret theorem](../../research/astra-global-20261128/broad/UNIVERSAL_WINDOW_REGRET.md) concerns a geometric gap law of mean `1<b<=a_*` and its actual ternary source measure `mu_b`. Let `C_n(x)` be the minimum total over all legal length-`n` inverse words, and let `T_n(f,x)` be the total under a deterministic rule depending on the current `W`-trit row. For every fixed `W`, a constant `delta(b,W)>0` satisfies

$$
T_n(f,x)\ge C_n(x)+\delta(b,W)n
$$

for `mu_b`-almost every source, for all sufficiently large `n`, **simultaneously for every such rule**. The rule may be chosen afresh for each root and tested depth. There is no common action cap across the rules. The statement nevertheless requires one deterministic function of the row throughout each tested execution; it does not prohibit a randomized controller from realizing an individual cheap word with small probability.

The key counting argument avoids enumerating policies. The words `1^W` and a length-`W` word starting with gap five from the signed point `-1` both code the same initial row. Their first actions differ. Any deterministic row rule must omit at least one of those words everywhere. Testing disjoint blocks gives an exponential deficit in the number of cheap words compatible with **any** deterministic rule.

To transfer that deficit to the original source measure, the proof strengthens the imported Shannon-dimension input. Conditional on the first `m` source trits, the next block is a mixture of affine permutations of an independent suffix law. Convexity gives submultiplicativity of its order-`q` mass sums for every `q>1`. A finite block with nearly maximal Shannon entropy, followed by `q` tending down to one, yields exponentially small mass for every exponentially undersized cylinder family. This uses Leen's stated geometric-law dimension theorem; it does not assume absolute continuity at the critical parameter.

There is an explicit growing-memory form when `b<=log_2 3`. Set `theta=1/b`, `t=-log(1-theta)` and `r=theta(1-theta)^4`. For any `c<1/(2|log r|)`, let `W_n=max(2,floor(c log n))`. Almost every source eventually satisfies, for every deterministic rule of width at most `W_n`,

$$
T_n(f,x)-C_n(x)\ge
\frac{r^{W_n}}{8t}\left\lfloor\frac n{W_n}\right\rfloor.
$$

This exceeds `sqrt(n log n)` by a polynomial factor. Here the precise source-dependent word numerator bounds the number of typical words in one ternary cylinder. This direct finite bound reaches the real-drift threshold; the fixed-width argument reaches the larger entropy threshold.

Both results have simultaneous finite versions on ordinary positive odd unit inputs in every large octave. Through depths `n=log_3 X+O(1)`, the number of inputs is

$$X^{H(b)/\log3+o(1)}.$$

At `b=a_*` the exponent is one. The subexponential factor is not controlled, so the count can have vanishing density. The theorem does not assert that one fixed positive integer realizes the infinite typical source law.

## 3. A stopped survival criterion for the remaining critical optimum

The [stopped-corridor construction](../../research/astra-global-20261128/broad/STOPPED_CRITICAL_CORRIDORS.md) identifies a concrete sufficient condition for `L=a_*`. Let `G_j(a,c)` be the set of sources carrying a legal `j`-letter inverse word whose every prefix cost satisfies `S_r<=ar+c`. For Haar probability `h_i` on either initial unit trit,

$$
(L-a)\sum_{j=0}^{N}h_i(G_j(a,c))\le c+6-a.
$$

The proof stops at the first failed depth or a fixed cap. It deliberately reads one extra trit, follows a surviving word, and uses one final gap at most six to return exactly to the original Haar trit law. Averaging the variable-length block occupations gives the displayed mean-cost bound. It does not require the selected words at different possible stopping depths to be compatible.

Consequently, if `a<L`, the complete survival series is summable and `n h_i(G_n)->0`. Divergence at slopes **strictly above** `a_*` and decreasing to it would identify the optimum. The exact endpoint is already known to be summable: Weaver150, Theorem3 equation(7), with its barrier parameter set to `(3/2) log(n+1)-t_*c`, gives `h_i(G_n(a_*,c))=O_c((1+log n)(n+1)^(-3/2))` for every fixed credit. The live question therefore requires slopes above the endpoint. This source correction was made before publication. The exact exponential rate is already determined:

$$
\lim_{n\to\infty}\frac1n\log h_i(G_n(a,c))
=\min\{H(a),\log3\}-\log3,
$$

for the stated nonempty initial credits. Above the entropy threshold that rate is zero. A sequence can still be both subexponential and summable, so this rate alone does not close the endpoint.

A separate entropy inequality explains why almost entirely prescribing one generic low-cost word cannot solve the problem at bounded mean cost. If a block devotes a fraction `rho` of its positions to a dictionary of entropy rate `s<log3`, then its filler must supply the missing source information. The resulting total cost is strictly above `a_*`; for a subexponential dictionary and `rho` tending to one, bounded total cost is impossible. A sufficiently rich source-dependent dictionary remains available.

[StoppedCorridor.lean](../../research/astra-global-20261128/broad/StoppedCorridor.lean) proves the true positive path transfer across source lifts, nested corridor tests, the at-most-six terminal repair, appended cost, exact finite tail sum and rational reward inequality. The analytic infimum bound is an explicit premise in the final finite inequality. The independent C++ recurrence enumerates every unit source through depth twelve at three slopes and agrees with a direct action minimum through depth seven. Its normal and `NDEBUG` outputs match; this finite enumeration does not decide the survival series.

## 4. The full fixed-horizon, positionwise ranking class has a sharp computable obstruction

The [all-position one-step theorem](../../research/astra-global-20261128/escape/ALL_POSITION_CERTIFICATES.md) closes the general-width ordinary carry interface left open in checkpoint 7. The [fixed-horizon extension](../../research/astra-global-20261128/escape/FIXED_HORIZON_POSITION_CERTIFICATES.md) then proves it for **every fixed shortcut horizon `s` and every fixed ternary radius `r`**.

There is a rational mean odd count `p>s log_3 2` and one positively integer-weighted finite seed which extends to every sufficiently large length. Every source is a positive unit. Its actual `s`-step endpoint has the same length, and the input/output width-`2r+1` window histograms agree at **each individual position**, including padding. The intermediate heights need not stay in that band. Every intermediate value nevertheless exceeds any specified floor once the length is large, since a shortcut step is at least half its input.

Thus an additive score whose coefficients depend arbitrarily and jointly on length, position and local window cannot certify

$$F(T^s n)-F(n)\le s\log_3 2-O_s(n)$$

on all sufficiently large ordinary inputs. These are actual integer certificates against the entire class, not only limiting real measures or solutions of a relaxed leading-digit problem.

The proof identifies the exact long-division carry equations as a finite matrix pencil. Its only persistent regular coordinates are the separate parity-word tag masses; the unit Jordan blocks have size one. The classical Kronecker canonical form then gives bounded signed connectors between any two compatible interior strings with the same tag masses. Positive interpolation joins a smooth leading law to a constant interior and then to a true lower suffix law. Rationality of the finite constraints gives rational nonnegative flows; clearing denominators and decomposing those flows produces ordinary integers. A repeated constant interior supplies every subsequent length.

At horizons greater than one, the lower law need not have full three-adic support. The [remote-trit support lemma](../../research/astra-global-20261128/escape/REMOTE_TRIT_SUPPORT.md) supplies exactly the finite band needed for the final splice. Rationally independent displacements in its uncountable affine support give equidistribution of **varying-depth real normalized residues**. This is a real torus statement; it does not assert impossible joint Haar independence of a one-parameter three-adic tuple. The required cylinders all have positive mass at one common remote band.

The [sharp envelope theorem](../../research/astra-global-20261128/escape/SHARP_POSITION_ENVELOPE.md) goes further. Let `A_L` be the optimal average odd count among all such actual, balanced, fixed-length endpoint families. There is a computable real `A_*(s,r)>s log_3 2` with

$$|A_L-A_*|\le C e^{-cL}.$$

The finite leading-prefix LP upper bounds decrease to the same limit at an exponential rate. Positive mixing with a smooth law allows a connector to reach the uniform interior in `O(log(1/epsilon))` layers while changing the cost by only `O(epsilon)`. A compactness argument makes the true lower cap uniformly bounded over the relevant positive tag simplex. Taking `epsilon` exponentially small in the available length gives the rate. Enumerating rational upper LPs and pumpable rational lower seeds computes the limit to arbitrary accuracy without first knowing usable numerical rate constants.

This establishes the sharp limiting value and its computability for the entire class. It does not give a short formula or a practically small seed at general width. It leaves methods with growing horizons, growing interaction ranges or nonadditive global features outside the obstruction. The new [NativeWindowBlock.lean](../../research/astra-global-20261128/escape/NativeWindowBlock.lean) checks the genuine parity-count lift, the strict endpoint residual bound and the exact arbitrary-cut carry formula. The matrix-pencil, support and positive-gluing arguments remain reviewed written proofs using their stated classical inputs.

## 5. A fixed computable postcritical orbit bit has positive multiplicative entropy

For a positive odd target `y` with ordinary predecessor density `d>0`, define

$$
f_y(n)=1\quad\Longleftrightarrow\quad
\exists m\ge0:\ T^m n=y\ \hbox{and}\ 4^m\le3^m n^2.
$$

This is one fixed function on actual positive integers, with no floating-point logarithm in its definition. [MedianDeadline.lean](../../research/astra-global-20261128/cycles/MedianDeadline.lean) proves that the unbounded existential test is equivalent to a finite search below five times the binary bit length. It also checks the concrete distinction: `3` reaches `1` before its deadline; `27` does not, although its true seventieth shortcut iterate is `1`.

The [critical dilation theorem](../../research/astra-global-20261128/cycles/CRITICAL_DILATION_ENTROPY.md) is explicitly source-qualified. Its ordinary orbit inputs are the complete exact-label first-landing template, counted equal-date synchronization for translated sources, and the fixed-target Gaussian clock theorem at the cited PR215 pin with its predecessor density. The initial joint invariance principle uses the separately credited two-adic logarithm bound.

Write `theta=log(4/3)/(2 log 2)` and `c=sqrt(theta)`. Let `I_d` be the strictly positive mutual information of bits satisfying

$$
\Pr(B=1)=\tfrac12,\qquad \Pr(F=1)=d/2,\qquad
\Pr(B=F=1)=d\left(\tfrac14+\frac{\arcsin c}{2\pi}\right).
$$

For any fixed odd multipliers whose pairwise ratios are outside the powers of three, and fixed offsets, ordinary octave sampling satisfies

$$
\liminf_{X\to\infty}H\bigl(f_y(A_1n+e_1),\ldots,f_y(A_rn+e_r)\bigr)\ge rI_d.
$$

Along powers of every prime at least five, this gives exponentially many actual deadline patterns in each fixed observation length and positive entropy in the corresponding stationary dilation limits. The ordinary density of the one-coordinate bit is `d/2`.

The proof retains the exact early landing label. A weak Gaussian-clock averaging argument makes the early clock independent of every bounded function of its own label, even a moving function. That label determines the remaining time to the target. The known scalar late Gaussian law therefore identifies a bivariate early/late Gaussian relation with correlation `c`. Independently varying early clocks retain positive information about their own late deadline bits, whether or not the different late clocks are independent. Entropy inequalities turn these own-coordinate correlations into the family lower bound.

The same construction forces a growing rank for every joint limiting covariance matrix of genuine late clocks: its rank is at least `ceil(r d theta)`. For first odd landings at growing floors with sublogarithmic floor height, use `d=1`; five nonsmooth dilations cannot all have an identical limiting clock fluctuation. The stationary rational-dilation field also has a quantitatively nonzero absolutely continuous covariance spectrum. These moment and spectral assertions refer to the specified limiting fields and their Gaussian finite parts, not unproved uniform integrability of every rare prelimit hitting time.

The pure eventual-visit bit has no deadline. This argument establishes no corresponding positive entropy for eventual fate, and does not determine the probability that two nonsmooth trajectories eventually meet.

## 6. Rare native grades repel every nonsmooth companion toward the fair grade

The [biased grade theorem](../../research/astra-global-20261128/cycles/BIASED_GRADE_REPULSION.md) gives a separate ordinary result requiring no landing or global-fate theorem. Give the first fixed odd affine source an iid parity law of mean `p!=1/2`. Every nonsmooth companion has its limiting grade uniformly closer to `1/2`, outside probability

$$C\exp\left(-ct/\log^4(2+t)\right).$$

For two of the multiplier residue classes the exception is exponentially small. The general estimate uses the stated fixed-ratio two-adic logarithm bound. At the actual mixed-parity clock, the grade difference is a biased nearest-neighbor walk. An explicit Green potential bounds its arithmetic waiting-cost occupation; separate native three-date controls keep both common and mixed departures at positive fractions.

The estimate survives conditioning ordinary `n in [X,2X)` on the exact, exponentially rare count `k_t(A n+a)=k`, where `k/t->p` and `2^t=o(X)`. Tilting at `p_t=k/t` makes every word in that slice equally likely. Conditioning costs only a square-root factor. Each binary residue has the same relative counting error in the ordinary octave, so the rarity of the whole slice introduces no additional loss.

At `p=log_3 2`, the selected ordinary trajectory has subexponential net size change through the tested interval, while every fixed nonsmooth companion decreases by an exponential factor with high conditional probability. This is an ensemble theorem before the binary horizon; a distinguished periodic word may lie in the exceptional set. The associated biased source laws under any two nonsmooth odd affine maps are mutually singular, including different biased parameters.

## Validation and next work

**Fresh validation passed:** 50 Lean modules and 1,428 declarations, including 229 private declarations. The full transitive axiom audit permits only `propext`, `Classical.choice` and `Quot.sound`. All 32 finite control programs passed ordinary and optimized execution, for 64 successful runs with identical paired output; the additional C++ corridor enumerator also passed both guarded and `NDEBUG` builds. The aggregate Lean replay ran from 04:58:37 to 05:13:10 UTC. Compiler and Mathlib identities, all eight clean dependency trees, and source hashes were checked. The independent review records 178 scientific source hashes and 93 reviewed Markdown manuscripts. [Lean receipt](CHECKPOINT_08_LEAN.json) · [Bounded-control receipt](CHECKPOINT_08_BOUNDED.json) · [Review and source hashes](CHECKPOINT_08_REVIEW.json) · [C++ receipt](broad/STOPPED_CORRIDOR_CPP.json). No finite control establishes one of the infinite written theorems.

The remaining central questions are explicit: determine `L` by proving sufficiently large original-source corridor survival or a sufficiently rich cheap routing dictionary; control truly nonlocal forward information; and exclude every extra positive cycle and every escaping positive integer. The next batch investigates actual synchronization classes, full native endpoint fibres, randomized controllers with hidden memory, and positive escaping-component budgets. Those drafts are outside this checkpoint until separately reviewed.

## Immutable scientific freeze

The complete reviewed scientific tree is commit `125e84b67ce9d3e3007b817951bd29f544c38ab5`, tree `b3ff48211db6decebc171bd9c52ae3657c498c56`. The repository integrity and regression validator passed on that clean commit. This publication adds its [integrity receipt](CHECKPOINT_08_INTEGRITY.json) and this reference. The GitHub commit and final clean-checkout receipt are verified separately after the exact tree is published.
