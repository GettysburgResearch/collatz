# Checkpoint 3: connected finite Lean proofs and the complete first-landing law

**Collatz remains unresolved. The nine-hour pass is continuing.** This checkpoint extends published head `61582bab723920a3ca50d80f9f80740c6c030be0`. The scientific sources were frozen at approximately 01:13 UTC on 28 November 2026, with a final explicit prior-work attribution added before publication. The requested endpoint remains 07:56:49 UTC.

## A complete finite proof chain on actual trajectories

The [formal Padé development](../../research/astra-global-20261128/root/FORMAL_PADE.md) now connects the polynomial construction to the ordinary shortcut map. It defines the coefficients, proves their integer normalization and size, proves finite cancellation, finds the exact binary valuation of the surviving term, and supplies every remainder from the same original trajectory. The comparison uses integer powers, including the checked inequality $3^{17}\le2^{27}$. It imports no p-adic irrationality or logarithmic-form theorem.

Let $t_j(n)$ be the actual time of the even input numbered $j$, starting at zero. For $h>0$, if
$$
 t_j(n)=j(b+1)+h\binom j2\quad(0\le j\le5s+2),
$$
Lean proves
$$
                         2^{3hs^2+4bs}\le(n+2)^{17}.
$$
The assumption at zero forces this source to be even. The final theorem does not assume abstract Padé tail bounds: it derives them from the observed clocks, using exact finite telescoping and the parity of the terminal input. With $n+2\le2^B$, it gives $3hs^2+4bs\le17B$.

The separate physical-window theorem also handles an arbitrary initial odd run. If the observed clocks are $a+j(b+1)+h\binom j2$ through the zero-based index $K\ge12$, the prefix is cut before its next prescribed even input, and $n+1\le2^B$, then its length satisfies
$$
                           L\le579B+289.
$$
For $B\ge1$ this is at most $868B$. The initial normalization, the interpolation index, and the final incomplete run are part of the formal argument. The exact scope is an integer bit budget and at least thirteen observed even inputs. The written all-window real-logarithm bound remains separately stated.

The decreasing finite chain is also connected to actual runs. For $h,s>0$, $b\ge200hs$, and
$$
 t_j(n)=j(b+1)-h\binom j2\quad(0\le j\le5s+2),
$$
Lean proves $2^{bs}\le(n+2)^8$, hence $bs\le8B$ under the corresponding bit budget. The spacing condition prevents the natural subtraction from truncating on the required range. Every integral Taylor term has an explicit common power of two; the formal proof extracts it before the size comparison. No infinite decreasing quadratic series is used. The complete $20{,}000\log_2(n+1)$ cutoff, including short and steep windows, is still the separate written argument.

The broad-track agent independently checked the coordinator's six new formal modules against these statements, including the indexing, source shift, incomplete-window ceiling, and both power margins. A successful Lean declaration and a more general neighboring manuscript are not treated as the same statement.

## A new information bound for every actual source octave

For a floor $B$, record the first odd landing at or below $B$, including a cemetery label on failure. Let $p$ be its law from uniform odd sources in any octave $[X,2X)$, $X\ge B$, or its limiting relative law. The [first-landing information theorem](../../research/astra-global-20261128/escape/FIRST_LANDING_ENTROPY.md) proves, for every $0<\eta<1$ and $K>0$,
$$
 p(A)\le C_{\eta,K}\left[(|A|/B)^\eta+(1+\log B)^{-K}\right]
$$
for every set of ordinary landing labels. The failure mass has every negative logarithmic power bound. In particular, a vanishing fraction of the labels has vanishing total probability, uniformly in the source octave.

For every fixed $r>0$ it also proves
$$
                 \sum_{p(y)>0}p(y)|\log(Bp(y))|^r\le C_r.
$$
The cemetery label is included. Thus the Shannon entropy is at least $\log B-C$. The previous Paper102 bound was $\log B-O(\sqrt{\log B})$ on the same source ranges. Its stronger individual-atom power bound is explicitly retained as prior work; the new setwise estimate has an additive logarithmic error and is not advertised as improving every regime.

The finite mechanism counts actual source integers. At a fixed first-landing label, odd grade and total division count, the survival product confines the uncorrected source to a short interval. [FirstLandingCell.lean](../../research/astra-global-20261128/escape/FirstLandingCell.lean) proves the integer strip and same-cell width on the factorization-defined native map. Elementary binary-prefix counting controls the exceptional clocks. The transfer from a selectable nearby source scale to all source scales uses the **source-qualified relative landing theorem in PR213**, pinned at `5ac2b4a7ab9fee19d2e1b1c2e4aadecd08413128`. The coordinator independently read that exact source and reconstructed the new deduction, but did not rebuild its imported analytic cancellation theorem.

## The complete integer label law has a universal local profile

The [local-profile theorem](../../research/astra-global-20261128/escape/LOCAL_LANDING_PROFILE.md) identifies a probability density $G$ on physical height $u\in[0,1]$ and the ternary integers. For every accuracy, a fixed finite function $g$, constant on finitely many height intervals and ternary residue classes, approximates the complete first-landing law by
$$
                         \frac2B g(y/B,y).
$$
The approximation is in the sum of absolute errors over **all actual integer labels**, including failure, as $B\to\infty$. It also holds along every sequence of actual source octaves with $X/B\to\infty$. Therefore the estimate can test arbitrary bounded donor functions, even when they depend on the future or change with $B$. The manuscript evaluates finite templates at integers; it does not assign arbitrary point values to a Lebesgue–Haar equivalence class.

The proof keeps the complete first-passage condition. A fixed finite word specifies one ternary progression, the true affine source interval, and an inequality for every earlier state. Ordinary progression counting gives its finite template. Uniform relative renewal makes these templates Cauchy in $L^1$.

The limiting density belongs to every finite $L^p$ space, and the entropy has a common constant term:
$$
 \mathsf H(p)=\log(B/2)-\int G\log G\,du\,d\lambda_3+o(1)
$$
on those distant-source sequences. The manuscript also identifies $G$ by an explicit record-time formula for a two-sided iid geometric sequence. The same past increments determine both the real record increment and the ternary perpetuity, preserving their dependence. It derives a recursive density equation and the exact covariance
$$
                         G(u/2,z)=G(u,2z).
$$
In particular its limiting probability of landing below the fraction $2^{-k}$ is exactly $2^{-k}$.

These are source-qualified written theorems. The coordinator independently reconstructed the finite templates, CRT passage, $L^1$ limit, information truncation, record-time averaging, recursion and scaling. Weaver's **Paper146 already defines the maximum-multiplier-restricted ternary family**; its fixed-cap approximations imply all finite moments. That antecedent is now explicit. The contribution here is the connection to the full actual first-landing label law, its record-time identification and its entropy constant. The lower bound on unit trits separately imports Paper12's controlled first-landing theorem.

First landing and last exit are distinct. The genuinely escaping last-exit labels form a sparse set, so the chance of first landing directly there tends to zero. Many other labels can descend to much lower states and subsequently merge into those last exits. The cardinality and cost of that full predecessor set are not bounded by this theorem. The escape mass $H$ is still not proved to vanish.

## Broader finite schedules and a cycle obstruction

The [arbitrary-word staircase proof](../../research/astra-global-20261128/broad/ARBITRARY_WORD_STAIRCASES.md) treats
$$
                         W^aVW^bVW^{b+d}V\cdots
$$
for any nonempty binary words $W,V$ and either sign of $d$. On a positive non-eventually-periodic shortcut orbit, its matching length is at most $10^6(\log_2(n+1)+|W|+|V|)$. The proof is uniform in the words, counts, slope and number of copies, covers ordinary expansion and contraction, and pays for incomplete terminal copies. Twelve additional finite interpolation terms absorb the precision lost at a separator. The coordinator checked both slope signs and the cutoff cases. This extension is written, not yet formalized. Wren's growing-block adaptation and Weaver's Paper70 remain explicit antecedents.

The [cycle arc theorem](../../research/astra-global-20261128/cycles/SHIFTED_ARC_INTERSECTIONS.md) proves a common-shift quadratic identity for every pair of proper lags, including coprime clocks. It also proves a sharp obstruction to coordinating those witnesses: for one-step arcs of a primitive integer cycle, different unoriented lag classes have different quadratic irrational shifts. A rational-cycle example shows that equal-count witnesses cannot be assumed. The result does not exclude an extra integer cycle.

The [absolute high-tail estimate](../../research/astra-global-20261128/escape/SMALL_REPRESENTATIVE_UPPER.md) controls the original signed character sum beyond every fixed polynomial shortening of the ordinary maximal-growth range. A stronger subexponential shortening is stated separately with Weaver's unrefereed Paper15/v2 as an additional input. The small representatives remain the unresolved cancellation problem.

## Verification and publication scope

The fresh [Lean replay](CHECKPOINT_03_LEAN.json) passed **24 modules and 837 declarations**, including **117 private declarations**, checking every current module and its explicitly imported local dependencies in a new build directory. It audits all declarations, including private and generated ones, for transitive axioms beyond `propext`, `Classical.choice` and `Quot.sound`. The pinned compiler and Mathlib checkout are unchanged. The receipt records the exact module and declaration counts; it is not a cold rebuild of Mathlib or an independent kernel implementation.

All **12 finite control programs**, **24 ordinary/optimized runs**, passed with identical outputs in [the paired replay](CHECKPOINT_03_BOUNDED.json). The new ordinary landing control checks 2,313 actual sources in 16 source octaves, 27,698 suffix identities, 134,380 word-and-endpoint tests, 1,892 source cells, and 1,364 finite joint dyadic covariance instances. The arbitrary-word control covers 354 physical remainders in 18 families. The shifted-arc control covers 24,861 paired filters on 314 primitive rational circles and 10,000 integer quadratic checks. These are finite controls, not proofs of limiting laws.

The [source review](CHECKPOINT_03_REVIEW.json) records exact scientific file hashes, independent review scope, external dependencies and remaining obligations. The exact published checkpoint2 tree passed [its separate integrity replay](CHECKPOINT_02_PUBLISHED_INTEGRITY.json). This checkpoint is committed and validated as a complete checkout before publication, then its remote tree and branch update are verified. The same draft PR212 and research branch are retained.

The clean scientific freeze is `4c7c9d3a3a697d02db8c46ce5792e3528e6836ff`, tree `bee7a4bb8f64141b2c3661a8b3f2a5802efa7834`; [its complete-checkout regression receipt](CHECKPOINT_03_INTEGRITY.json) passed before the publication receipt was added. The final publication tree is verified separately after the branch update.
