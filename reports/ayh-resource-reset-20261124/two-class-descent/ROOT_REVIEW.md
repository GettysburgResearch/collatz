# Coordinator reconstruction of the two-class descent packet

## Scope and verdict

This review concerns the sources in the accompanying source-hash manifest, based on PR 197 parent 9ab91d964b38fc870d1034bac628d62f59488467. It reconstructs the new mathematical inferences and their quantifiers. The verdict is **VERIFIED at the written inference level under the explicitly named source inputs**, with the limitations below. The manuscripts remain **PROPOSED**, and recent external pair-chain estimates remain **SOURCE-QUALIFIED**. This is internal review, not external peer review.

The Lean verification has narrower, exact scope: six new modules and their local import closure, with 15 new public theorem declarations. The build record and axiom inventory report the actual execution separately. No inference from a finite test or kernel check to an unformalized probability theorem is made.

## 1. Largest-slope projection

Reviewed ADAPTIVE_PAIRED_PROJECTION.md at SHA-256 e712cf35c130499ea85355c36ea9876c1041ffb1c969122ecdd19521e0c9e38c.

For each individual odd-affine arm, a complete source block gives uniform temporal parity words. This statement is marginal in the arm and is sufficient for its scalar intercept moment: the recurrence is \(e'=(3^u e+u)/2\), with a fair next bit independent of that arm's own past. Concavity gives a strict contraction for every fractional power between zero and one. The proof never makes the different arms independent.

At a fixed count vector, the largest effective slope is \(\lambda\), and its intercept is in \([0,L]\). Its endpoint ranges over an interval of length at most \(\lambda+L\). Once this integer endpoint is fixed, elimination of the common source leaves each remaining endpoint in an interval of length \(2L\), whose center may depend on the anchor. Therefore the count pays for \(\lambda\) once, rather than separately for all arms. Equal anchor endpoints give source diameter \(LH/\lambda\).

Discarding fibers smaller than \(H/(\lambda J)\) cancels the factor \(\lambda\) exactly. The residual factor from at most \((h+1)^m\) count vectors is already included in \(J\). The estimates remain valid when the fiber threshold is below one; they do not then promise a large family of siblings. A useful common modulus range requires the separately stated lower cutoff on \(F=H/\lambda\).

The residue estimate counts each residue inside the actual fiber's short interval and divides by the actual retained fiber size. Tests can depend on the full ordered future because the bound is deterministic for every residue list on every fiber. A union of retained fibers inherits the bound with its original mixture weights. Before removal of bad sources, conditioning on a rare mark requires dividing the absolute discarded mass by that mark's probability; the text keeps this term.

For an interior source window after a fixed prefix, the correct effective slopes are the original coefficients times the **total** accumulated powers of three. The useful exponential lower bound for \(F\) is asserted only after averaging original prefixes and excluding its explicitly bounded bad slope event. No uniform typical-count assertion is made for a specially chosen prefix.

LargestSlopeProjection.lean checks the endpoint-band elimination, equal-anchor diameter and finite integer record census by an injection. PairedSourceShuffle.lean checks two-sided fringe counting and the residue numerator. The fractional moment, probabilistic discard and ordinary-row assembly are written.

## 2. Original-source transfer at late physical clocks

Reviewed FORWARD_SOURCE_REEXPOSURE.md at SHA-256 e86033f86567dbadbd514c1f4089d7131baed2275791d0e8e78b290427b9fa0a and PHYSICAL_CLOCK_PROJECTION.md at ee71892a47320bb92c5165916297d4161b4b60ed3c73e86cf1c52fe47f61f631.

With fixed counts, the low endpoint lies in an interval of length \(V+E\). The possible canonical offsets number at most \(3\rho E\). For a specified low endpoint and offset, the high endpoint is fixed, so all original parameters, over every source block together, lie in one interval of diameter \(EF\). Its integer multiplicity is at most \(1+EF\). The identity \(\rho FV=N\) then gives the coefficient \(3E(E+1/F)\) for a per-offset bad ordinary count of at most \(\delta V\).

This deterministic count is valid even when \(2^t>N\). At such a clock it uses the already established actual scalar intercept envelope, not a new fair-word law for the original sources. Before the earlier polylogarithmic entrance, sliding scalar contraction gives \(E\le d^C\), upper height at most \(Rd^C\), and hence \(1/F\le d^C\). The original row's fixed ratio of endpoints, together with the lower height being much larger than \(E\), makes \(V\) comparable to the lower physical scale.

A periodic bad set is counted by covering the whole low-endpoint interval with complete periods. Every added period is charged at the same bad fraction, so the refined bound has no additive unrestricted-period error. This requires the indicated test to be defined on all residues, or to dominate the positive-input event there. If a target is chosen from the fresh future, its ordinary count bound must still be proved with that selection. Merely averaging over offsets under some unrelated law is insufficient.

The native-window note retains a valid weaker fringe term; the late-clock note explicitly strengthens it. Their statements are compatible. The remaining fair fusion tail depends on the inherited grade and does not become arbitrarily power-small from this counting identity.

## 3. Actual occupation, coarea and the quarter-exponent improvement

Reviewed ACTUAL_FRONTIER_OCCUPATION.md at d4f74cf6ed121d5fa8d2f2f39eb33ce866f4fb7903aa9d94ecddfad100cc01af and AREA_FRONTIER_EXTENSION.md at e7ac7cfbc97b4c19c374a19346004ec91a8ad1cb452f16137e5e492c4af04328.

The source-qualified successive-entry drift and finite-set absorbing trial imply a geometric tail in the **number of entries**. At a fixed skeleton length, add a sufficiently large constant to the nonnegative drift function. On its bounded part the killing probability decreases the constant term; outside that part the strict drift decreases the variable term. Both decreases dominate a uniform positive fraction of the sum. KilledEntryContraction.lean verifies exactly this algebra. Converting it to a probability tail is a written Markov iteration.

An interior excursion has expected occupation of levels two through \(K\) bounded by \(CK^2\), uniformly in its starting level and integer offset. The killed simple-walk Green function bounds visits by \(2(\ell-1)\), and the physical waiting means have summatory order \(K\). Reapplying the bound at occupation stopping times gives an exponential tail on the \(K^2\) scale. This controls occupation, not the duration of a long excursion at much higher grade.

The original scalar stages have logarithmically many thresholds and test lengths that fit a complete grid at any inspected clock in the stage. The older proof enumerated all offsets at grade up to \(K\), costing a factor exponential in \(K\). The new late-clock projection counts those offsets with their smaller high-endpoint fibers, removing that factor. Every relevant per-profile test is uniform in the offset. Thus \(O(\log d)\) occupation quanta suffice at all \(K\le O(d)\). With \(O(\log d)\) excursions per stage and \(O(\log d)\) stages, total band occupation is \(O(K^2(\log d)^3)\).

For a surviving source, a single clock first crosses at most one integer dyadic floor: the previous joint running minimum is at most twice the new one. The source population failing the native merger certificate is \(O(R/\sqrt d)\). Multiply its size by the pathwise occupation bound and divide by the number of tested floors. This gives \(d^{-1/2+2\beta-b}(\log d)^3\), summable for \(1/2+2\beta<b<1\), hence every \(\beta<1/4\). The minimizing floor is computable from a finite trajectory predicate independent of eventual colors.

The logarithmic endpoint \(K=d^{1/4}/(\log d)^{2+\epsilon}\), floor-log scale \(d/(\log d)^\epsilon\), gives \(1/[d(\log d)^{1+\epsilon}]\), also summable. The floor log remains \(o(d)\), preserving the stated late passage time. The finite floor theorem can use the common-time grade directly; the argument does not reverse the implication from small entrance lag to small grade.

## 4. High-grade regeneration and genuine smaller heads

Reviewed HIGH_GRADE_SHADOW.md at a7eb5e317ccafcb505a876dbb6fc5723e1de89f6f3656c697895f07352ccf990 and ROUNDED_HEAD_DESCENT.md at c57bd423824faaba39ac50575687a19afeaa7fe47bcdf9b3640a0554edf61bdb. The independent shadow and rounded-descent reviews reconstruct their detailed scalar transfer.

At grade initially at least twice a window length, orientation remains fixed in that window. The true normalized-offset recursion differs from the scalar affine proxy by a forcing term bounded using the high grade. The total error is less than \(2^{-L}\). At a fixed odd count the chronological word numerators are injective modulo \(2^L\), so the proxy has the stated translated-mesh small-ball bound. Neither the bit on the other arm nor its correlations are replaced by an independent bit.

Actual long-time transfer uses scalar sliding tests and polynomial source fibers at geometric first entrances. Forgetting a polynomial incoming proxy costs a sufficiently long logarithmic window. The inspected grid also accommodates the explicitly stated extra logarithmic buffer. It does not control every eventual source-dependent shadow time after one arm has reached a bounded cycle.

For rounded descent, the candidate phase schedules are deterministic after a finite phase mesh is fixed. Irrational-rotation recurrence gives a bounded spacing. A tilted drift with a finite forced word gives a positive frequency of lower marks. Upper truncation failures have a separately controlled frequency on the same schedules; a union bound on the two frequency deficits creates common successful times. This does not require independence between the arms or a probability claim conditioned on the actual lower success.

If \(|W-1/2|<1/100\), then for \(0\le i\le3\),
\(\lceil3^iW\rceil=(3^i+1)/2\).
Nested floors therefore terminate at one of the five unbounded families checked in RoundedHeadDescent.lean. The interior mantissa margin preserves the leading head interval under every later four-trit floor. The bottom is still large, so all intervening head exponents are nonnegative.

## 5. The actual weighted incidence inequality

Reviewed HEAD_INCIDENCE.md at dc13a8daf06eb7827ff4989eeca7d00745504405308f312a3e344cc723dfd4d9. Harmonic's independent review pins the earlier 6eef0b44bf6bb201e19f671958377c8d26c6f01fd7ad10727d8332f940ada2d4 version of the main inequality. The final additions about distinctness and sparse bands were reconstructed by the coordinator; the earlier review does not automatically certify them.

From the first joint passage below \(2^{2B}\) to the first below \(2^B\), there are at least \(B-1\) clocks. At the former time both heights are at least \(2^{2B-1}\), even if the crossing arms later differ. Blocks starting at low grade are removed by the occupation theorem. A fixed fraction of every remaining block supplies witnesses with a bounded full-history upper affine intercept. The tilted upper-proxy estimate used for this bound is a high-value frequency estimate, not a false pointwise boundedness assertion.

For a returned child \(z=\lfloor U_t/3^u\rfloor\), bounded intercept gives the original interval
\[
n\in 2^t3^{-(p-u)}[z-E,z+1].
\]
At a fixed \(t,z\) and original-arm label, at most one integer \(p-u\) meets the source row: distinct choices differ by a factor of three, whereas the row ratio is \(8/7\). Its length is \(O(R/z)\). The uniform native merger test is applied on **that original interval**, whose logarithmic length is comparable with \(d\). This yields \(O(R/(z\sqrt d))\) discordant sources without summing over trit depths.

The prefix concentration and grade bound confine \(t\) to \(O(\sqrt{d\log d})\) choices at a fixed \(z\). Each original source supplied \(cB\) incidences, giving the coefficient \(\sqrt{\log d}/B\). The source interval, time count and number of witnesses have separate justifications.

For distinctness, subtracting the logarithmic source equations at two times gives a nonzero integral form in \(\log2,\log3\), up to exponentially small errors in the witness height. Switching which original arm is upper only changes the coefficient of \(\log3\) by four and adds \(O(1/R)\). The cited classical polynomial separation defeats these errors. A fixed mantissa subarc survives all floors by its interior margin.

The sparse-band criterion chooses the largest \(L_i\le d/4\). From \(L_{i+1}\le L_i^{2-\varepsilon}\) it obtains \(L_i\gg d^{1/(2-\varepsilon)}\), so the whole returned range fits inside the hypothesized band. Its assumed weighted mass \(O(1/L_i)\) then gives a summable bound on \(a_j\). This is an implication, not a proof of that hypothesis. The final universal-convergence consumer also retains the earlier source-qualified fixed-target positivity input.

## 6. Remaining limitation

The recurrence permits a nonsummable square-root discrepancy profile. The finite-family projection permits clusters with identical ordered futures of different colors. The improved coarea theorem removes a summable small-lag part but not every surviving large-gap pair. No manuscript in this checkpoint supplies the missing true-color estimate or establishes global termination.

The finite replay checks word lengths at most 14 and the explicitly bounded physical paths, while Lean verifies all parameters only for its named declarations. External probability libraries were not rebuilt. The recent primary sources retain their stated evidence levels; repository integrity is not mathematical validation.

## 7. Final finite-menu and local-stage extension

Reviewed FINITE_FLOOR_FRONTIER.md at author SHA-256 3e1209d5cf22913bb89e20431f70829589ad8d0022bf8ed3c7d99277d4eeca16. Integration removes trailing spaces on one blank line; the mathematical text is unchanged. For a fixed good source, the measure of low-grade floor parameters is at most \(q=O(K^2(\log d)^3/B)\). The measure of the Cartesian \(m\)-th power of that set is exactly its measure to the power \(m\). Multiplying by the native survivor fraction and charging the common source exception once gives \(O(d^{-A}+d^{-1/2}q^m)\). This product is over floor parameters on one deterministic trajectory, not over independently imagined orbit segments.

At \(K=d^\beta\), \(B=d^b\), the condition \(m(b-2\beta)>1/2\) makes the row series summable. It gives every \(\beta<1/2\) with a fixed finite menu. The dyadic minimizing menu uses finite certificates and is color-independent; the first qualifying entrance is detected using only the current grade and already observed path. The later-arm lag is then at least \((\log_2 3)K-O(1)\). A single fixed floor does not inherit this exponent.

For the local improvement, only a bounded number of geometric stages intersect one logarithmic height band. Each interior excursion's band occupation has a uniformly bounded exponential moment at scale \(K^2\). At a fixed restart, expose a deterministic number of excursions, pad by zero after death, and iterate their conditional exponential-moment bounds. On the separate event that the number of entries is at most this quota, the truncated observed occupation is dominated by that sum and at most a terminal full excursion. Choosing a quota proportional to \(\log d\) pays both tails. This avoids conditioning a duration on its own stopping count. The finite stage grid contains each tested remainder.

Thus local occupation is \(O(K^2\log d+(\log d)^2)\). Substitution verifies both the sharper single-floor logarithmic endpoint and the growing menu \(K=\sqrt d/(\log d)^{1/2+\epsilon}\), \(m=O(\log d/\log\log d)\). The latter has \(q=O((\log d)^{-\epsilon})\) and \(d^{-1/2}q^m=d^{-1/2-c\epsilon+o(1)}\), summable for \(c\epsilon>1/2\). The independent FINITE_FLOOR_REVIEW.md confirms these steps. This extension leaves the successful large-grade source class open.

## 8. Sifted actual discordant sources

Reviewed SIFTED_DISCORDANT_SOURCES.md at author SHA-256 973436f60430a547d6d4f477f5a909ac0da63b95e7cc04e632ddd90e2449df96, independently also checked in SIFTED_SOURCES_REVIEW.md. The integrated copy corrects one missing backslash in a displayed LaTeX spacing command; its current hash is in the source manifest.

Fixing the shared native residue fixes every inspected physical output as an integer affine form in the remaining high parameter. True disagreements occupy only the \(O(2^h/\sqrt d)\) nonfused residues. Their high-parameter intervals have exponentially large, comparable lengths. Neither color is assumed independent of that parameter; the proof simply overcounts by every rough point of each surviving cylinder.

For a nonzero determinant, primes larger than \(d^2\) and not dividing it remove two distinct residues. The determinant is at most exponential in \(d\), so deleting its larger prime factors changes the local product by only a bounded factor. The one-form case removes one residue. At each prime, the specified mean-zero function has squared Fourier norm \(k/(p-k)\); its squarefree CRT product has primitive Fourier support and norm equal to the product of those factors. On every sifted integer its value is that same product. Cauchy–Schwarz followed by the separated-frequency large sieve yields the displayed upper bound after summing squarefree moduli.

The product measure includes a prime with probability \(k/p\). Its expected logarithmic modulus is \(O(k\log y)\); choosing the fixed sieve exponent sufficiently small ensures that at least half the product weight lies below \(Q^{1/3}\). This justifies the truncation without an unjustified full Euler product. When the determinant is zero, unequal slopes give an integral factor of three between the outputs, preventing simultaneous standard roughness; equal slopes and equal endpoints would already fuse.

The two-form sieve, union over \(O(d)\) clocks and native survivor factor give \((\log d)^2d^{1/2-2\beta}\). The one-form prefix-selected observation has no clock-union loss and gives \(\log d\,d^{-1/2-\beta}\). The stated exponent ranges make both series converge. Prime coordinates are larger than the sieve threshold because every inspected clock is before a fixed fraction of the initial bit length. This removes a real arithmetic subpopulation; no universal rough-visit statement follows.
