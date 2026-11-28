# Checkpoint 2: growing arithmetic clocks and global physical obstructions

**Collatz remains unresolved. The nine-hour pass is continuing.** This checkpoint extends published head `31311116eac06e87320c84e11de6c105292a6f78`. The scientific sources were frozen at approximately 00:25 UTC on 28 November 2026. The planned pass endpoint remains 07:56:49 UTC.

## A uniform bound with genuinely growing arity

The strongest new arithmetic result is an elementary written theorem about actual parity prefixes. If a positive shortcut source $x$ follows
$$
 1^a0\,1^b0\,1^{b+h}0\,1^{b+2h}0\cdots,
 \qquad a,b\ge0,\quad h\ge1,
$$
for $L$ bits, then $L\le1000\log_2(x+1)$. The constant is independent of the initial run, spacing, slope and number of gaps. The [increasing-gap proof](../../research/astra-global-20261128/broad/QUADRATIC_CLOCK_PADE.md) constructs integer Padé forms whose dyadic valuation exceeds their logarithmic ordinary height by two positive uniform margins. The exact elementary comparison $3^{17}<2^{27}$ certifies both margins. The proof controls the growing number of terms directly.

The [finite decreasing-gap proof](../../research/astra-global-20261128/broad/FINITE_DECREASING_CLOCKS.md) handles the opposite sign by finite affine remainders at actually observed even inputs. Its bound is $L\le20{,}000\log_2(x+1)$. The formally continued decreasing quadratic series does not converge at the dyadic place, so the proof never uses that infinite series. An explicitly extracted common power of two makes the integer height comparison work. Together with the periodic zero-slope exception, these results force at least logarithmically many changes of gap slope along every hypothetical nonperiodic positive orbit.

The coordinator independently reconstructed the clearing denominators, unique minimum valuations, integer nonvanishing, positive and negative curvature estimates, and the physical cutoff cases. These are written proofs with exact finite controls; **neither complete Padé proof has been formalized in Lean at this checkpoint**. The next formal target is the finite interpolation identity and its original-source remainders.

The qualitative p-adic irrationality theorem is prior work of Väänänen–Wallisser. Aijaz's external Collatz atlas applies it to an explicit infinite ray, and this repository's PR48 has an eventual-affine exclusion for a different run-core recurrence. Zudilin's 2005 construction supplies the finite algebraic forms; its published numerical theorem concerns the real place. The manuscript credits these antecedents and identifies the additional uniform finite-prefix estimate. Irregular adaptive gap schedules remain outside the theorem.

## Arithmetic restrictions that retain the actual path

The [cofactor argument](../../research/astra-global-20261128/broad/SHIFTED_COFACTOR_COLLISIONS.md) studies the part of $2x+1$ prime to three. A repeated label on a positive segment of length $r$ forces an actual input below an absolute multiple of $r^{5.116201}$, using the stated external logarithmic-form estimate. A two-arm version has an essential equal-depth, compensated-grade alternative: immediate ordinary siblings really can have the same label.

The [formal finite result](../../research/astra-global-20261128/root/COFACTOR_FORMAL_BOUND.md) keeps that external estimate out of the kernel. If the endpoints satisfy $2x+1=q3^a$ and $2T^r(x)+1=q3^b$, and $s$ is the actual odd count, put $P=2^r3^b$ and $Q=3^{a+s}$. Lean proves $P>Q$ for a nonempty segment and
$$
 (2m+2)(P-Q)\le rP
$$
whenever every input state is at least $m$. A supplied relative power gap therefore forces a specific low iterate. The broad-track agent independently checked this formal interface against the written argument. **No result here forces an early collision.**

The [complete pin criterion](../../research/astra-global-20261128/broad/PinCriterion.lean) now connects the greedy dyadic clock to the rational discounted rank and then to convergence of the same positive integer, end to end in Lean. Its boundedness condition remains open.

The [rational-match accounting](../../research/astra-global-20261128/broad/RATIONAL_MATCH_MASS.md) and [overlapping-window theorem](../../research/astra-global-20261128/broad/OVERLAPPING_PERIODIC_WINDOWS.md) go beyond a fixed dictionary: they allow changing rational references and the union of every bit-length-scale periodic window with sublinear period. A maximal-extension selection bounds overlap, and shifted fixed-dimensional Subspace-Theorem applications give an asymptotic time proportion at most $1-\log_3 2$ in the bounded-terminal regime. The complementary gaps must supply adjacent-odd growth. The fraction and its fixed-budget predecessor are explicitly credited to Paper174; the proof does not silently take a dimension-uniform Subspace-Theorem constant.

## Exact cycle cost and a global closure boundary

The [diagonal cycle moment](../../research/astra-global-20261128/cycles/DIAGONAL_CYCLE_MOMENT.md) selects actual equal-source-and-target atoms of the native trace. It has an exact formula retaining every primitive cycle period. The known odd cycle contributes three. With the manuscript's pinned external minimum-height, period and total-gap inputs, any additional positive cycle raises the total above $27/4$. Finiteness of this moment is equivalent to finiteness of the set of positive cycles. **An independent upper bound by $27/4$ remains open.**

The same calculation shows why finite log-loss moments do not supply a bound on this ordinary-time moment. A rational cycle model retains finite gap and variation budgets while its diagonal costs diverge. Its omitted integer/global conditions are named explicitly.

The [annulus theorem](../../research/astra-global-20261128/cycles/ANNULUS_SPECTRAL_FACTOR.md) derives a measurable irrational rotation factor in any parity limit whose physical cycles retain positive mass in a fixed multiplicative height band. Bounded diagonal cost forces such a band. Integrality also forces positive entropy, using the height-to-word entropy injection already present in concurrent PR213, which is now credited. Consequently zero-entropy limits and weakly mixing limits separately force the diagonal cost to diverge; neither hypothesis is imposed on every possible cycle.

The [full-parent construction](../../research/astra-global-20261128/cycles/FULL_PARENT_LOCAL_MODEL.md) tests this route against a stronger control: packets of genuine positive integer trajectories, with all their actual local parent branches and joint binary, ternary and normalized real observations, approximate a bounded-height positive-entropy rotation model. Their endpoints are free and each segment has only logarithmic length in its height. This does not create a cycle or a divergent integer orbit. It shows exactly which global closure information is absent from fixed-radius arithmetic observations.

The finite cycle kernels now formalize the adjacent-mark obstruction, the CDF half-jump charge, the raw harmonic barrier, its circular closure and an all-offset mass identity. The source-qualified analytic and Diophantine consequences remain written.

## One explicit output character detects any escape mass

Let $H$ be the total stationary mass of possible escaping components and $\rho_N$ the original periodic positive row. On odd $x$, define
$$
 \psi(x)=\min(v_2(3x+1),3)-7/4,
$$
with values $(1,-3,5,-3)/4$ on the four odd classes modulo eight. The [dyadic-output theorem](../../research/astra-global-20261128/escape/DYADIC_OUTPUT_CONTRAST.md) proves, under the stated physical-front inputs,
$$
 -\tfrac34H\le\liminf_N\frac1N\sum_{x>0\ {\rm odd}}
 \frac{\rho_N(x)\psi(x)}x
 \le\limsup_N\frac1N\sum_{x>0\ {\rm odd}}
 \frac{\rho_N(x)\psi(x)}x
 \le-(7/4-\log_2 3)H.
$$
The sums converge by Dirichlet cancellation. The proof first averages the actual signed physical fronts, then uses their positive ordinary-ray placement; it does not substitute fair random future parities. A nonnegative subsequential upper limit of this one character sum would eliminate escape. An independent estimate making the normalized sum vanish is still missing.

Every limiting binary output measure is invariant and at least $(2-\log_2 3)H$ is singular with respect to odd binary Haar measure. Last-low escape flux is supported on one binary dimension defect. This contrasts with the separately established full real-mark dimension, without inferring a contradiction between different coordinates. An explicit positive-entropy coding shows that the binary clock bias need not generate the growing arithmetic patterns excluded above.

The [variation profile](../../research/astra-global-20261128/escape/VARIATION_PROFILE.md) and [critical source clock](../../research/astra-global-20261128/escape/CRITICAL_SOURCE_CLOCK.md) retain the marked physical information across all grades. The [ordinary product note](../../research/astra-global-20261128/escape/ORDINARY_PRODUCT_TRANSITION.md) credits PR145 for the prior Gaussian transition, half-mean test and terminal law; it contributes a uniform fixed-target soft-clock comparison and a direct marked telescoping proof. Leen's exact every-target statement was checked in the deposited source, including its absence of a target-convergence hypothesis. None of these source-qualified laws proves $H=0$.

## Verification, corrections and provenance

The [fresh Lean replay](CHECKPOINT_02_LEAN.json) passed all **nine modules** in a new build directory, including the explicitly imported old `CoreBranching` dependency. It audited **384 declarations**, including generated and private declarations, against the allowed axioms `propext`, `Classical.choice` and `Quot.sound`. This is not a count of 384 new theorems. It uses Lean4.34.1 and the pinned clean Mathlib checkout, with reused Mathlib dependency objects. No cold Mathlib rebuild or independent checker is claimed.

All **nine finite programs**, **18 normal/optimized runs**, passed with identical outputs in [the paired replay](CHECKPOINT_02_BOUNDED.json). These include 80 increasing Padé forms, 240 positive finite prefix lifts, 12 decreasing forms with 60 physical tails, signed transport and cofactor controls, and the cycle, annulus and variation checks. Finite examples verify implementation and expose incorrect statements; they do not establish the unbounded results. The [source review](CHECKPOINT_02_REVIEW.json) records the frozen identities and analytical scope.

The [published checkpoint1 replay](CHECKPOINT_01_PUBLISHED_INTEGRITY.json) is preserved. This checkpoint corrects the authors' names in the first report and its review metadata to **Bondareva–Luchin–Salikhov**. The theorem, exponent and cited source were already the intended ones; this is a bibliographic correction. The direct real-branch audit of López–Stoll's literal Lemma24 is separately documented and does not assert a Collatz counterexample.

The live-frontier refresh inspected PR213 at `a743bd04d33945b15a1ec91deaca4a82c0261a07`, PR214 at `7c381c5b53afec65fc473c598c5ed61762e9419f`, and PR215 at `8a50018b6a861e810b18512fdd59aaf45214bba1`, with focused overlap checks. Their entire formal and analytic packets were not rebuilt. The existing branch and draft PR212 are retained; no merge to main is part of this publication.

The clean scientific snapshot `d826357ed73f035112b7aee32eb676a6cf77320c`, tree `48ba9a3db7be81d8267ce0db911af9cdc3f77e11`, passed [complete repository integrity and regression validation](CHECKPOINT_02_INTEGRITY.json). The publication tree additionally preserves this receipt and reference; it is separately validated before updating the branch.
