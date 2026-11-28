# Checkpoint 4: global operators, actual landing clocks and irregular schedules

**Collatz remains unresolved. The nine-hour pass continues.** This checkpoint extends published head `d91a6b9f14daea79d35edf8cffc8548d98796197`. Scientific files were frozen at approximately 02:01 UTC on 28 November 2026. The requested endpoint remains 07:56:49 UTC. The results below distinguish finite Lean theorems from source-qualified written analysis. In particular, the existing analytic landing, synchronization, harmonic-density and cycle-verification inputs are not silently promoted to newly formalized theorems.

## The actual positive Green operator separates the cycle question

On positive odd integers coprime to three, write $U$ for the ordinary accelerated map, $w_x=3x/(3x+1)$ and $t_x=1-w_x$. The established positive harmonic weight $a_x$ satisfies $\sum_{Ux=y}a_xw_x=a_y$. On $\ell^2(a)$, let $Pf(x)=w_xf(Ux)$. The [positive Green analysis](../../research/astra-global-20261128/cycles/POSITIVE_GREEN_SPECTRUM.md) keeps this entire original graph. It uses the stated harmonic identity and the uniform reciprocal packing estimate for distinct vertices of a simple trajectory.

The survival operator $P$ has the entire closed unit disk as Fredholm essential spectrum. In contrast, its two-sided killed Green operator
$$
 L=\lim_{r\uparrow1}\sqrt t\,(I-rP)^{-1}\sqrt t
$$
exists in the strong operator topology and is bounded and positive. Its eigenvalue one is semisimple, with one independent principal mode for each positive cycle. Every other spectral value lies in the disk of radius $1/4$, using the stated external bounds for additional integer cycles. If $\Pi$ is its principal spectral projection, $R=L-\Pi$ is Hilbert–Schmidt, and its powers decay at every exponential rate strictly larger than $1/4$ in Hilbert–Schmidt norm. The first-visit Green part is itself Hilbert–Schmidt. The proof of these compact and Hilbert–Schmidt remainders uses simple-path packing and does not require the aggregate period-gap budget.

The principal projection is explicit: on a basin, its output is $\sqrt{t_x}$ times the cycle average of $f(y)/\sqrt{t_y}$ with weights proportional to $t_y/w_y=1/(3y)$. It vanishes on escaping components. Thus a spectral gap alone does not bound the number of principal modes or remove an escaping basin.

The [ordinary spectral-grid theorem](../../research/astra-global-20261128/cycles/ODD_SPECTRAL_GRID.md) identifies each positive odd integer $y$ coprime to three:
$$
          \frac1{3y+1}\in\sigma(L)
          \quad\Longleftrightarrow\quad y\text{ is not periodic}.
$$
Each such nonperiodic value is simple and isolated. A cyclic block cannot replace a missing native grid point. This last arithmetic obstruction is proved in [CycleGridObstruction.lean](../../research/astra-global-20261128/root/CycleGridObstruction.lean): after clearing the actual native denominators, a putative zero at $1/(3y+1)$ would give $\prod_i(x_i-y)=\prod_i x_i$. The left side is even and the right side odd. The formal statement allows any nonempty indexed family of positive odd integers, including repeats, and any positive odd test integer. The denominator identity and native-weight nonvanishing endpoint are both checked. The cycle-track agent independently reviewed the coordinator's five public endpoints and their [scope note](../../research/astra-global-20261128/root/CYCLE_SPECTRAL_FINITE.md).

Every extra positive integer cycle would also force a pair of nonreal spectral values. The proof uses the ordinary transition bound, a geometric majorization of reciprocal cycle heights, and a strict negative second inverse-root moment; its weak minimum and period prerequisites follow from the explicitly cited external verification inputs. Hence reality of the whole spectrum is equivalent to the absence of extra cycles, but no independent reality theorem is supplied.

There is a finite signed trace with a sharp equality criterion. Put
$$
 B_0=\sum_{x>1,\ x\ {\rm odd},\ 3\nmid x}\frac1{(3x+1)^2},
 \qquad \Xi=\operatorname{Tr}(R^2).
$$
The written proof gives $B_0-\Xi\ge0$, with equality exactly when the known cycle is the only positive cycle. Every extra cycle contributes a strictly positive deficit. The separately source-qualified aggregate gap bound gives $B_0-\Xi<(0.023835)^2$. An independent lower bound $\Xi\ge B_0$ would close this route; it remains unproved. A gamma-function reference determinant and its exact cycle corrections record the same obstruction without discarding the native spectral grid.

## A physical resolvent has a finite-cycle versus natural-boundary dichotomy

The [marked return resolvent](../../research/astra-global-20261128/cycles/MARKED_RETURN_RESOLVENT.md) uses the original trace-class diagonal mark $D_x=\rho_1(x)/(x(3x+1))$. Its function $H_D(z)=\operatorname{Tr}D(I-zP)^{-1}$ has the exact positive cycle expansion. For finitely many cycles it is rational. For infinitely many it has the unit circle as a natural boundary, with signed radial derivative blowup on the dense angles $2\pi j\log_2 3$.

The proof evaluates the original positive terms at those angles. Each small-gap cycle makes a contribution comparable to its physical moment, whose per-cycle lower bound prevents infinitely many terms from remaining bounded. It does not invoke a generic lacunary-series theorem. Every positive trace-class determinant perturbation $\det[I+uD(I-zP)^{-1}]$, $u>0$, has the analogous dichotomy, through an exact product and a positive integral formula for its derivative. Neither analytic continuation of the actual resolvent nor an independent upper bound on the physical moment has been established. Finitely many additional cycles remain possible under this dichotomy.

## The complete landing law now keeps the exact shortcut date

Let the first odd landing below a floor $B$ be sampled from an ordinary source octave of height $X$. Put $v=\log(X/B)$, $D_0=\log(4/3)$, and let $f_v$ be the normal envelope with mean $2v/D_0$ and variance $2(\log3)^2v/D_0^3$. The [global joint clock theorem](../../research/astra-global-20261128/escape/GLOBAL_LANDING_CLOCK.md) gives the full integer-label and integer-date law through finite approximations $g$ of the already constructed physical/ternary density $G$:
$$
 p(y,t)\simeq \frac2B g(y/B,y)f_v(t)
 W\bigl(t\log2+\log(y/B)-v\bigr),
 \qquad
 W(r)=\log3\,e^{r\bmod\log3}\mathbf1_{[0,\log2)}(r\bmod\log3).
$$
The approximation is in the sum of absolute errors over all labels and dates, including failure, whenever both $B$ and $X/B$ diverge, at **arbitrary relative rates**. The normal envelope does not erase the persistent phase. The limiting total-variation discrepancy between octaves whose heights differ by a factor three is zero; for factors two, four and five it is respectively $2/3$, $1/2$ and $31/45$.

The [mesoscopic proof](../../research/astra-global-20261128/escape/MESOSCOPIC_LANDING_CLOCK.md) first retains the exact total geometric gap count in a finite ternary template. The all-scale extension then derives a two-step recursion from the actual even and odd source branches and iterates it to an intermediate floor. A stopping-time local limit and irrational phase averaging transfer the mesoscopic law to arbitrarily distant sources. The crucial signed input retains the **joint physical endpoint and native total clock**, as stated in PR195 `MARKED_FIBRES.md` equation (3), pinned at `3fa7ef4a0011b35447a70f587b400878d5ea8ebe`. The coordinator read that source in full and checked this interface. Its imported analytic mixing theorem remains source-qualified.

## Entry, exit and the unresolved postminimum path

The [first/last landing theorem](../../research/astra-global-20261128/escape/FIRST_AND_LAST_LANDING.md) proves joint independence between specified observations at the first landing and an arbitrary countable observation of the later lower landing. The incoming observations include a fixed physical-height partition, growing ternary residues and a genuine forward binary word, with the stated conductor bound. Choosing a lower floor $\sqrt B$ transfers this to the actual outgoing last-exit label and its full future, on escape. A separate theorem keeps the whole inward shortcut clock: its phase is the autocorrelation of an explicit wrapped height density, with every nonzero Fourier coefficient strictly positive.

The proof uses PR213's source-suffix theorem at `5ac2b4a7ab9fee19d2e1b1c2e4aadecd08413128`. The coordinator independently read the whole source and checked both its growing original-digit law and its joint endpoint/native-clock cancellation interface. No independence between successive nested inward clocks is asserted: they share an intermediate height phase.

The [preminimum recrossing law](../../research/astra-global-20261128/escape/PREMINIMUM_RECROSSINGS.md) controls the entire sequence of high upcrossing dates before the trajectory's first global minimum. Once the path has first fallen below $B/M$, the probability of a return above $B$ before that minimum is $O_\eta(M^{-\eta})$ for every $\eta<1$, uniformly over the source octave in the stated limiting sense. Its complete preminimum crossing list converges in total variation to the corresponding multiplicative random-walk list. The limiting expected number of upcrossings is $\log(3/2)/(2D_0)$; a uniform-integrability claim for all finite-source crossing counts is not made.

Consequently the native outward edge flux obeys the lower bound
$$
       \liminf_{B\to\infty}\sum_{y\le B<Uy}w_ya_y
                        \ge\frac{\log(3/2)}4+H,
$$
where $H$ is the original escaping mass. The preminimum crossings and permanent last exits are disjoint contributions. A matching upper bound on this **uncapped** shell would force $H=0$. The concurrently inspected PR213 power-capped ordinary trace does not provide that upper bound: its excluded forward hull can contain an entire escaping ray. The deterministic path after the minimum remains the central missing control.

## Near-full parity information, spikes and the sharp real gauge exponent

The [growing-conductor theorem](../../research/astra-global-20261128/escape/GROWING_LANDING_PHASES.md) treats joint real partitions, ternary residues and actual forward binary words whenever their combined conductor is smaller than the floor by a diverging multiplicative factor. It includes binary words of length $\log_2 B-\omega(1)$, with entropy equal to their maximal value minus $o(1)$. This unconditioned range is distinguished from the smaller range used while conditioning on an arbitrary later label. A zero-slack counterexample gives a fixed total-variation obstruction.

The [profile-spike construction](../../research/astra-global-20261128/escape/LANDING_PROFILE_SPIKES.md) gives a ternary address set of Hausdorff dimension $H_2(\log_3 2)$ with positive-volume cylinders on which the profile grows at least linearly in depth. Thus $G$ is essentially unbounded and its finite-$p$ norms grow at least linearly in $p$. This address set contains no positive ordinary integer. The balanced-peak construction and capped-density family in Papers12 and146 are explicitly credited.

The [real-fibre theorem](../../research/astra-global-20261128/escape/REAL_FIBRE_LOG_GAUGE.md) extends the $[\log(1/r)]^{-1/2}$ neighbourhood lower bound to each fixed unit target and proves interval bounds on increasing full-measure restrictions for every gauge $r[\log(1/r)]^s$ with $s>1/2$. Combined with Weaver Paper175's earlier zero-carrier result for $s<1/2$, this fixes the critical logarithmic exponent at $1/2$ for the stated terminal and first-arrival measures. The endpoint $s=1/2$ remains open. The proof counts actual bounded-gap histories and labels, rather than assuming independent future parity indefinitely.

## Finite restrictions on irregular event clocks

The [intrinsic clock theorem](../../research/astra-global-20261128/broad/INTRINSIC_CLOCK_DISCREPANCY.md) permits arbitrary arrangements of the observed odd gaps. For actual even-input times $t_0=0,\ldots,t_{7s}$, set $u_j=t_j-j$, $m=4s+1$, and let $W_0$ be the width of all translated additive discrepancies $u_k+u_j-u_{k+j}$ with $k\le4s$ and $k+j\le7s$. Put $C=8(m3^{W_0})^4$. If the smallest of the first $4s$ gaps is $g$ and $8C(2/3)^g\le1$, then
$$
                  2^{t_{7s}}\le3^{u_{4s}}2C(x+2).
$$
The normalized finite matrix has a small nonzero integer kernel. A geometric sign condition prevents the resulting real form from vanishing; its exact native binary precision and ternary denominator give the inequality. The [adaptive-column version](../../research/astra-global-20261128/broad/ADAPTIVE_CLOCK_COLUMNS.md) allows selected and reflected weights. It also proves a limitation of this box-and-sign method on globally bounded positive curvature: its useful windows are too short to give a universal contradiction.

Five new Lean modules prove the small integer kernel, the sign lemma, finite convolution cancellation, the actual trajectory remainder, and the native denominator clearing. The endpoint `actual_integer_barrier` takes explicit row certificates and coefficient, decay, denominator and clock inequalities and returns a negative integer with its binary divisor lower bound. The normalization that supplies those certificates from the full intrinsic-discrepancy hypothesis and the final upper size estimate remain written. The [broad report](broad/CHECKPOINT_04.md) gives the precise module scopes.

The [late-window theorem](../../research/astra-global-20261128/broad/LATE_QUADRATIC_INTERVALS.md) allows an unrestricted earlier history. If the actual gaps are $b+hj$ for $m\le j<K$, with fixed $b\ge0,h\ge1$, and the vertical offset at $m$ has positive part $o(m^2)$, no fixed positive source can have infinitely many such intervals with $K\ge2.6m$. The corrected Padé head absorbs every earlier ternary denominator; negative vertical offsets are free, while positive offsets cost an explicit factor $(3/2)^c$. This excludes bounded actual gap defects confined to powers of three, including aperiodic schedules. The coordinator independently checked the extension for both offset signs.

Finally the [convex minor calculation](../../research/astra-global-20261128/broad/CONVEX_EVENT_MINORS.md) computes the unique binary and ternary extremal terms of a native determinant and retains the prime-to-six common divisor of its cofactors. In the exact quadratic case that divisor is a Vandermonde product whose logarithm cancels the otherwise adverse cubic term. This identifies useful arithmetic structure rather than asserting it for arbitrary rough clocks. Weaver Papers70 and104 and the classical Padé antecedents are credited explicitly.

## Verification and publication

The fresh [Lean replay](CHECKPOINT_04_LEAN.json) passed **31 modules and 932 declarations**, including **140 private declarations**. All **16 finite control programs**, **32 ordinary/optimized runs**, passed with identical paired outputs in the [bounded replay](CHECKPOINT_04_BOUNDED.json). The axiom audit includes every local private and generated declaration and permits only `propext`, `Classical.choice` and `Quot.sound`. It uses the same pinned Lean 4.34.1 and clean Mathlib dependency tree as earlier checkpoints, and is not a cold rebuild of all Mathlib.

The new cycle controls include 9,216 native Green entries, six finite-section determinants, 852 rational characteristic evaluations and 14,200 odd-grid exclusions. The new landing controls include 8,670 actual sources, 10,230 forward/reverse stopping comparisons and 795 exact phase checks. The irregular-clock controls include 42,981 ordinary parity observations, 104 vanishing convolution rows, 120 convex cofactors, 15 exact Vandermonde contents and 72 late-window sources, including 24 positive and 24 negative vertical offsets. All are bounded controls; none proves an infinite analytic law or universal convergence.

The source review binds the reviewed scientific files by SHA-256, records the external inputs and the independently checked coordinator work, and lists the remaining critical implications. The complete-checkout validator is run before publication, the GitHub tree is compared exactly with the validated local tree, the branch update uses its expected parent, and the published commit receives another integrity replay. PR212 remains a draft on the existing research branch. The next work targets the missing raw-shell upper bound, a cycle trace lower bound or spectral rigidity, and a genuinely irregular-clock obstruction.

The clean scientific freeze is `c96989ff84acb9cf4c14c18b292ffdfeab440516`, tree `f256dd30a69a2732783f40a2b4ec39b17bf09770`. Its [complete-checkout regression receipt](CHECKPOINT_04_INTEGRITY.json) passed before this publication receipt was added. The final published commit is checked again after the branch update.
