# Checkpoint 6: sharp digit prices, finite certificates and full prime-chain laws

**Collatz remains unresolved. The nine-hour pass continues.** This checkpoint extends published head `0172f15109b8749c14fed272e733c97a5a0f7d24`. The scientific files were frozen at approximately 03:38 UTC on 28 November 2026; the requested endpoint remains 07:56:49 UTC. The main new result is a classification of a complete family of proposed digit-ranking functions, including exact sharp prices at every ternary width. Separate results give the empirical law along all prime-factor additions, untrimmed landing moments, and a quantitative obstruction to a proposed inverse stationary construction.

The coordinator independently reconstructed every new written proof included below. Named analytic inputs, including results from other project branches and unrefereed Collatz manuscripts, remain explicit premises. Seven new Lean modules prove finite arithmetic and measure-tree interfaces. The complete analytic theorems are written mathematics, with no claim that their classical inputs have been formalized here.

## Every radix, every finite width and every polynomial position weight

Fix an integer radix $p\ge2$, radius $r$, degree $D$, and the terminating digit representation with distinct lower and upper sentinels. Consider
$$
 F(n)=b(n)+\sum_{i=0}^{L_p(n)-1}\sum_{j=0}^{D}i^j A_j(w_i(n)),
$$
where $b$ is any bounded function and the window coefficients are arbitrary real numbers. The [polynomial-digit theorem](../../research/astra-global-20261128/root/DIGIT_POLYNOMIAL_RANKING.md) proves that finite uniform upper increments on both actual shortcut branches force
$$
                         F(n)=\gamma L_p(n)+O(1).
$$
Consequently a uniform negative odd increment $-\varepsilon$, with $\varepsilon>0$, and a finite even allowance $a$ can occur exactly when
$$
                         a\ge\varepsilon\frac{\log2}{\log(3/2)}.
$$
At and above that threshold a negative multiple of $\log n$ works, represented by constant digit weights and a bounded correction. If $F$ must be bounded below, no such negative odd drift is possible for any finite even allowance.

The proof first takes expectations under multiplication-invariant digit laws. The corrected Hochman version of Host's equidistribution theorem forces the top interior coefficient to be a constant plus a finite de Bruijn coboundary. Weighted summation by parts retains the leading boundary term. Conditional averages over **actual** even and odd progressions force the top constant to vanish; irrational rotation of the real mantissa makes the remaining leading coefficient constant. Its length power is exactly a sum of lower-degree position weights. Induction gives the displayed rigidity. Neither an iid assumption about a true Collatz path nor a truncated computational search supplies this conclusion.

The root and both relevant research lanes independently checked the expectation limit, carry control, boundary reduction, parity averages and degree induction. The classical input is [Hochman, corrected version 2, Theorem 1.1](https://arxiv.org/html/2103.08938v2). The earlier unweighted finite-window use of this method is credited to [Paper 98](https://rstation.ai/problems/collatz/papers/98).

## Finite actual-step certificates exist at every width and every floor

For each digit window and each degree, write $\Phi(n)$ for the integer vector of its position moments and $d(n)=\Phi(Tn)-\Phi(n)$. The [finite-witness theorem](../../research/astra-global-20261128/escape/DIGIT_RANKING_FINITE_WITNESSES.md) proves that, for every fixed $p,r,D$ and every input floor, there are finitely many **actual positive unit inputs** $n_s$ above that floor and positive integers $b_s$ such that
$$
 \sum_s b_s d(n_s)=0,
 \qquad
 \frac{\sum_s b_s(n_s\bmod2)}{\sum_s b_s}>\log_3 2.
$$
All inputs are prime to three. Thus the certificate excludes every bare local score at a normalized parity price at most $\log_3 2$, independently of lower-boundedness. Adding a nonnegative multiple of $\log n$ cannot rescue such a score: the same weighted true log increment is positive.

Infinite infeasibility alone would not justify a finite certificate. The proof therefore identifies every nonincreasing recession direction. Unit-core digit rigidity reduces it to a finite boundary function; a full-support invariant product of a real mantissa, binary Haar coordinate and finite residue law forces every such direction to be neutral on all high actual steps. A finite coercive subcover then bounds the relevant coefficients. Compactness gives a finite infeasible subsystem, and rational separation gives integer weights. Exhaustive integer enumeration terminates, although this argument supplies no bound on its running time or first witness height.

[Paper 189, current version 2 of 23 November 2026](https://rstation.ai/problems/collatz/papers/189) previously supplied explicit ternary witnesses at widths one and three above every floor, and at width five above 64. Its larger-width and larger-floor certificate questions are addressed by this written existence theorem. The earlier explicit witnesses retain their value as concrete small certificates. An arbitrary externally supplied bounded correction is a different class and can attain the critical price.

## The exact optimal price is a finite graph problem

The [sharp-price theorem](../../research/astra-global-20261128/escape/SHARP_DIGIT_PRICES.md) goes further. For bare scores of radius $r$, the least $q$ for which
$$
                         F(Tn)-F(n)\le q-(n\bmod2)
$$
is a rational number $q_{p,r}$ **independent of the polynomial degree and of the input floor**. It is attained by a nonincreasing degree-zero score valid at every positive integer, including the small inputs. Restricting sources to units gives the same optimum. At every floor, the supremum of the odd fractions of actual finite witnesses balancing all original features is also $q_{p,r}$; attainment of that supremum by a finite witness is not asserted.

Radius-preserving cohomology leaves exactly a length term, a function of the first $2r$ digits, and a function of the last $2r$ digits. The low boundary cannot improve either branch's worst increment. The leading labels and integer length changes give a finite rational linear program. A nonincreasing tail envelope converts any feasible ideal scaling score into a score for the true map: its positive odd offset helps the inequality. This is why the graph optimum applies to all actual input floors.

For ternary digits the two ideal branches have the same mantissa motion, with length changes differing by one. Let $M=3^{2r-1}$ and iterate
$$
 h\longmapsto
 \begin{cases}
  \lfloor3h/2\rfloor,&h<2M,\\
  \lfloor h/2\rfloor,&h\ge2M.
 \end{cases}
$$
The fraction of first-case steps in its eventual cycle is exactly $q_{3,r}$. Monotonicity on the lifted grid bounds every possible graph cycle; shortest-path potentials attain that bound.

| Ternary window width | Exact sharp normalized price |
| --- | --- |
| 1 | $1$ |
| 3 | $2/3$ |
| 5 | $7/11$ |
| 7 | $12/19$ |
| 9 | $171/271$ |
| 11 | $983/1558$ |

At width seven the exact control checks a 19-state extremal cycle, 12 decrements and a 19-threshold potential against all **1,458** parity-labelled leading edges. Of these, 1,436 are tight. The checker uses integers and rational numbers, including $3^{12}>2^{19}$, and contains explicit guards that survive Python optimization. The complete graph-to-actual-score theorem remains the independently reviewed written proof. This rounded graph cycle is not an integer Collatz cycle.

For every $r\ge1$, $q_{p,r}>\log_3 2$ and
$$
 q_{p,r}\le\log_3 2+\frac{\log(1+p^{1-2r})}{\log3}.
$$
In radix three the proof also gives a matching exponential width rate, up to a logarithmic factor: $(q_{3,r}-\log_3 2)^{1/(2r)}\to1/3$.

## A genuine infinite-memory obstruction

The [infinite-context extension](../../research/astra-global-20261128/broad/INFINITE_DIGIT_CONTEXT_RANKING.md) allows bounded two-sided digit observables with variation
$$
 \operatorname{var}_R g_j=O((1+R)^{-P}),
 \qquad P>2+\frac{D(D+3)}2.
$$
This includes exponentially decaying dependence on arbitrarily distant digits. The same rigidity and sharp drift threshold hold. A fixed finite truncation would have an accumulated error growing with numeral length, so it would not prove this result.

The proof constructs a bounded subaction explicitly. A full-support maximizing measure makes its continuous slack vanish everywhere, yielding an exact coboundary with a controlled loss of two variation powers. Both infinite sentinel tails are summed uniformly; their leading terms fit into lower-degree observables. The degree induction tracks every loss of regularity. This rules out a broader class of smooth digital scores while leaving more irregular or unbounded-memory constructions open.

## All prime-factor additions have the ordinary empirical fate law

Let $s_j$ be the divisor chain obtained from an ordinary integer $n$ by adding its distinct primes in increasing order, each with its full exponent. For a fixed component union or fixed odd-target visit event $F$ with ordinary density $d$, the [full-chain occupation theorem](../../research/astra-global-20261128/cycles/PRIME_BAND_OCCUPATION.md) proves
$$
 \frac1{\max(1,\omega(n))}\sum_{j=1}^{\omega(n)}F(s_j)
       \longrightarrow d
       \quad\text{in natural probability}.
$$
With the stated full ordinary component-law input, the empirical component measure converges in total variation. The result includes hypothetical additional cycle basins and escaping components under the explicitly cited premises.

For independent geometric prime valuations, the conditional law at a later full cutoff $z$ also approaches the ordinary law in expected total variation whenever $\log(2w)=o(\log z)$, after conditioning on the entire history through $w$. **No RH assumption is used.** A typical band contains a smaller prime whose Vinogradov–Korobov cancellation can be multiplied by an elementary mean-value bound for all remaining factors. Boxed tagged-prime sampling then controls each unit interval of $\log\log p$. Uniform second moments and a truncated covariance argument yield the empirical conclusion. The coordinator read the precise primary bound in [Matomäki–Radziwiłł–Shao–Tao–Teräväinen, 2026, Lemma 3.2](https://doi.org/10.1007/s00222-026-01408-6).

The [canonical variation theorem](../../research/astra-global-20261128/cycles/CANONICAL_PRIME_VARIATION.md) separately proves that a fixed nonconstant fate changes on a positive fraction of consecutive prime additions, with natural probability tending to one. Its null-set prefix lemma lets one replace the visit-one indicator by the total finite computation that runs at most $5(1+\lfloor\log_2 n\rfloor)$ shortcut steps. Under the stated first-hit clock and basin-positivity inputs, universal convergence is equivalent to the normalized variation of that computable test having lower limiting ordinary mean zero. Any counterexample would force a strictly positive lower bound on density-typical chains. No estimate establishing the zero alternative is proved here.

The [RH baseline](../../research/astra-global-20261128/cycles/PRIME_BAND_MIXING.md) is retained with its complete smoothed-prime proof. Its full-band statement is strengthened by the unconditional companion above. Its stronger conclusion for every prescribed word of **immediately consecutive individual prime additions** still uses RH in this checkpoint. It asserts positive frequencies, without an iid formula for adjacent links.

## Positive moments of raw landings and terminal fibres

Put $g=1-H_2(\log_3 2)+1/351$. The [raw landing theorem](../../research/astra-global-20261128/escape/RAW_LANDING_MOMENTS.md) proves untrimmed positive-order moment bounds, including the cemetery for a miss, from every ordinary source octave above a floor $B$:
$$
                 B^q\sum_x p(x)^{1+q}=O_q(1),
                 \qquad0<q<\frac{g}{1-g}.
$$
In the distant-source regime it also gives convergence of these discrete moments, with the exact odd-grid normalization, to the physical-height/ternary profile moments. The written proof combines the cited relative renewal comparison with Paper 102's beyond-horizon counting estimates.

For each positive terminal fibre, [the all-scale density theorem](../../research/astra-global-20261128/escape/ALL_SCALE_FIBRE_DENSITY.md) proves that its normalized $1+q$ cell moments have order $(\log B)^{q/2}$ for $0<q<g$. The upper bound applies uniformly to actual normalized target rows. At almost every fibre point,
$$
 \frac{\log[\nu(B(x,r))/r]}{\log\log(1/r)}\longrightarrow\frac12.
$$
The lower and the full pointwise conclusion use the stated quantitative ray covers and natural-law identification from Paper 175. The coordinator checked those source interfaces directly. These results control concentration without eliminating the possible positive escaping flux.

## A quantitative failure of frozen inverse marginals

The [inverse transport theorem](../../research/astra-global-20261128/broad/FROZEN_MARGINAL_TRANSPORT.md) studies a precise stationary construction: at each width, keep the preceding target marginal and expose one uniform new trit. If $N=2\cdot3^{W-1}$, $M$ is a heavy target atom and $A$ is the largest required mean positive gap through width $W$, exact finite routing gives
$$
                       NL M\le L^2+1+2(N-2)A.
$$
For the critical iid geometric Syracuse law, the fixed signed $-1$ cylinders force these frozen-marginal costs to grow exponentially along a subsequence. More generally, bounded-cost policies uniformly comparable to that law on every working-precision cylinder require a comparison ratio at least approximately **1.21538639**. This excludes an entire prescribed construction; it does not resolve the unrestricted adaptive inverse-pressure endpoint. In particular a vanishing total-variation error is weaker than the relative cylinder control tested here.

Three new Lean modules formalize the rational tents, actual positive-gap routing and coherent finite-hierarchy atom bound. Their checks include 1,264 finite routed packets and 960 exact atom inequalities.

## Native meetings and parity separation

[MeetingBarrier.lean](../../research/astra-global-20261128/root/MeetingBarrier.lean) formalizes the actual affine offsets, their budget, and the finite meeting barrier from checkpoint five. If $A/B$ is outside the multiplicative group generated by two and three and $n\ge3^h$, every pair of dates $s,u\le h$ satisfies $T^s(An)\ne T^u(Bn)$. Its source-uniform integer proof uses no logarithmic-form theorem.

The [parity separation theorem](../../research/astra-global-20261128/cycles/MULTIPLIER_PARITY_SEPARATION.md) gives a positive lower asymptotic Hamming fraction for two fixed odd multipliers whose ratio is outside $3^{\mathbb Z}$, under binary Haar input. The bounds are $2/7$ or $2/9$ according to the ratio's mod-eight class. The grade difference is a simple symmetric walk at the true mismatch clock. The second bound uses the cited Bugeaud–Laurent two-adic logarithm estimate. [MixedParity.lean](../../research/astra-global-20261128/cycles/MixedParity.lean) checks the native two-child identities, including exact first and second moments; the infinite waiting-time argument is written separately.

## Verification and next work

The fresh aggregate compilation, full declaration audit, normal/optimized controls and exact publication receipts are recorded with this checkpoint. The seven new Lean modules are `CyclicTent`, `CyclicMarginalTransport`, `CyclicAtomBound`, `DyadicDensityStopping`, `MixedParity`, `DigitRankingKernel` and `MeetingBarrier`. The digit kernel proves both weighted telescoping endpoints, monomial degree reduction, literal all-odd trajectories and the final obstruction for bounded perturbations of a monotone height. The dyadic kernel proves finite high-then-low stopping budgets for arbitrary nonnegative additive tree mass.

**Fresh validation passed:** 42 Lean modules, 1,264 declarations including 190 private declarations; the aggregate transitive axiom audit permits only `propext`, `Classical.choice` and `Quot.sound`. All 24 finite control programs passed both ordinary and optimized execution, for 48 successful runs with identical paired output. The Lean replay completed at 03:46:02 UTC after 518.7 seconds of compilation and audit. The pinned Lean compiler, Mathlib commit and all eight manifest dependencies were checked, with clean tracked dependency trees. Source hashes match before and after each replay. [Lean receipt](CHECKPOINT_06_LEAN.json) · [Bounded-control receipt](CHECKPOINT_06_BOUNDED.json) · [Independent review and source hashes](CHECKPOINT_06_REVIEW.json).

The remaining pass targets the unrestricted critical inverse policy, an unconditional theorem for prescribed consecutive prime-factor words, and a fully checked finite width-seven price. The global obstructions remain: no upper bound here excludes an extra integer cycle, and no proved endpoint forces escaping flux to vanish. The new ranking classification closes a substantial proposed route and its finite-certificate questions, while the next work continues to seek a positive route to the universal conjecture.


## Immutable scientific freeze

The complete reviewed scientific tree is commit `e46e977e28ebd71a5690dc99c03ceda1af9ed2d1`, tree `d07f37c2f505ac9be254f8c9943b6114eb828e0a`. The repository integrity and regression validator passed on that clean commit. This publication adds its [integrity receipt](CHECKPOINT_06_INTEGRITY.json) and this reference. The GitHub commit and final clean-checkout receipt are verified separately after the exact tree is published.
