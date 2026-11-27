# Third checkpoint: independent root reconstruction

**Parent:** PR 200, `bf7d52e78631954a9fd35e4ce973acd27738fc80`.
This review concerns the identities in `WAVE3_SOURCE_MANIFEST.json`, including the explicitly modified integrations. Collatz remains open. The cycle finiteness statements below are restricted and import a separately identified 2026 preprint. Their finite exceptional cycles have not been classified.

## Dispositions and evidence boundaries

| Claim | Disposition | Evidence and limitation |
|---|---|---|
| Moving rational shadows, corrected M1–M8 | VERIFIED written deduction | Root reconstruction and separate EF/Yu review; not a full Lean analytic proof |
| Height-independent waiting interval | VERIFIED | Exact terminal inequality is Lean; anchor choice and Yu are written |
| Sliding dyadic stacks S1–S2 | VERIFIED written deduction | Root reconstructed the uniform starting-time argument and cofactor multiplicity |
| Weighted shallow/tropical coupling W1–W2 | VERIFIED with named imported premise | Uses PR 201's same-source sibling summability, not a newly established cheap sibling |
| Reflected-grade sparsity, gaps and digit families | VERIFIED at their stated scopes | Root proof reconstruction, two new Lean modules, independent physical-clock controls |
| Binary width `99/50` four-bridge bound | VERIFIED WITH CLARIFICATIONS | Separate review plus root reconstruction; analytic and preprint inputs remain explicit |
| Fixed-source binary excursion and full unforced pressure | VERIFIED at their stated scopes | Second independent review, root reconstruction, independent matrix controls |
| Binary finite energy kernel | VERIFIED by fresh compilation | Fourteen declarations; phase interpolation and asymptotic use are not formalized |

The fresh packet replay completed **21 local Lean modules and 190 public/private theorem audits**. It rebuilt every project module in an empty output directory, checked the pinned Lean and Mathlib revisions, and accepted only `propext`, `Classical.choice`, and `Quot.sound` in the printed axiom inventories. The pinned external Mathlib cache was reused. Two missing dependency objects were rebuilt from the unchanged pinned sources. This is not an independent rebuild of Lean or all of Mathlib.

The finite-control replay completed **27 programs**. Each normal and optimized Python execution reproduced the entire frozen output byte for byte. These computations check finite identities and interfaces; they do not prove an ineffective asymptotic threshold by enumeration.

## 1. Moving rational phases and the corrected singleton

The root first reconstructed the original moving-shadow argument, then checked the exact correction against the archived original. For a singleton at edge `j`, the incoming coefficient `2` has ternary exponent `l-j-1`, not `l-j`. Its outgoing coefficient `-1` has that same ternary exponent and the next binary time. This follows from

\[
3(x_j+1)=2^{e_j}(x_{j+1}+1)-2^{e_j}+2.
\]

The misplaced original term is a real identity error. The one-edge example `17 → 13` gives total 54 with the corrected expression and 58 with the original. Both identities are preserved with their own hashes. The repaired term has a smaller root-relative size by a factor of three and preserves the opposite ordering of the binary and ternary positions.

For a high packet with at most `m` pieces, the root checked the following points independently of the final reviewer report. Clearing all rational boundary denominators costs at most `H^(2m)` and may introduce powers of two, but no power of three. The root dominates the sum of the absolute nonroot terms, so deleting zero subsums cannot delete the root. A non-all-one packet retains at least two coordinates. Removing the common divisor `2^u 3^v γ` gives the stated primitive-height lower bound because `γ` divides a retained nonroot coefficient, the total bounds its binary part, and the root bounds its ternary part. The residual coefficients after separately clamping the two prime exponents are integers of the stated size.

I checked the projective normalization against **Evertse–Ferretti, Corollary 1.3 and Lemma 15.3**, in the authors' primary report. The forms are independent systems chosen from the coordinates and their total. After rounding and rescaling, all individual exponents are nonpositive and sum to `-d-1/200`. The ordered grids have exponentially many possibilities in the dimension, rather than a separate uncontrolled choice at every coordinate. The exceptional subspace is proper and requires a nonempty vanishing coordinate subsum, which the retained vector excludes. Its height intervals have an effective bound on their number and logarithmic-logarithmic width; their locations need not be effective. [Primary EF report](https://math.leidenuniv.nl/reports/files/2010-17.pdf)

Finally, fast record increments lie inside expanded exceptional intervals and have disjoint interiors on the log-log height axis. Slow increments cost a bounded amount each. The initial threshold absorbs the coefficient heights and the possibly even clearing. Choosing the packet size proportional to `log(k+2)` gives

\[
T+1\le \exp\!\left(C\frac{k+1}{\log(k+2)}\right)\log(n+2H+2).
\]

The quantifiers permit different rational phases in every piece and every packet. They require exact shadows or explicitly counted singleton edges and nonzero displacements. The result does not identify a smaller positive ancestor. Weaver's periodic-dictionary argument supplies the prior record/interval architecture; the moving endpoints and their clearing are the application audited here.

## 2. Waiting intervals, sliding stacks and the remaining cost comparison

For an exact run, the endpoint numerator has ternary order at least `k+r`. Its nonzero size is at least `2^s3^(k+r)` and at most `H(x_k+1)`. The ordinary inequality

\[
2^k(x_k+1)\le3^k(x_0+1)
\]

therefore gives `2^(k+s)3^r ≤ H(x_0+1)`. This uses terminal ternary divisibility and does not discard an even endpoint denominator. The three declarations in `TernaryEndpointBudget.lean` formalize this deduction from the finite cross-denominator transport data.

The full positive height ball has an integer anchor with initial depth at least `floor(log₃ H)`. Consequently a maximizing exact run satisfies `2^k<3(x_0+1)`. Its forced mismatch, together with Yu's local estimate, gives the common interval `j≤ceil(log₂(3(n+1)))`; the chosen clock can still depend on `H`. The signed version needs the stated noncoincidence condition.

For the new sliding-stack conclusion, I concatenated the actual pieces from `r` shells starting at `J,2J,…,2^(r-1)J`. If `S_i` counts each shell's simultaneous shallow dates, there are at most `4ΣS_i+r` pieces. For locally polynomial height caps, physical growth gives

\[
\log(x_J+2\max H_i+2)\le C_{n,B,b}J(r+2).
\]

Applying M1 once to the entire stack leaves a lower bound proportional to `r` on its logarithmic time ratio. Since the piece count is at least `r`, this forces `ΣS_i ≫ r log(r+1)`, uniformly in the starting clock `J`. A date is counted at most twice. Subdividing the shell-index interval proves the stated supply of distinct well-populated shells. No bound on the orbit's growth rate is assumed.

At fixed anchor `p/q`, a cofactor `u` and a depth `v` determine the integer state uniquely. On the certified dates, `v=O(r+log(2J))`; injectivity of a nonperiodic orbit then proves S2. This supplies many distinct cofactors, not a prescribed cofactor or a useful upper bound on the least one.

For W1, shell-index groups `[2^k,2^(k+1))` contain at least a constant times `2^k k` distinct certified dates. Each has weight comparable to `2^(-k)k^(-2)`, so the group contributes at least a constant times `1/k`. This proves the divergent weighted sum and its stated triple-logarithmic lower bound. For W2 I separately checked the inequality `2^(-R_t)≤Σ_j4^(-j)2^(m_t(a_t)-m_t(B^j a_t))`. The minimum exists because at least one small sibling is a ternary unit and costs tend to infinity with `j`. Summability is imported from the **same fixed ordinary source** in pinned PR 201. The root read that manuscript and reconstructed its source-selection argument; the underlying positive antichain theorem is a separate input. [Pinned tropical sibling premise](https://github.com/GettysburgResearch/collatz/blob/4c36876ebbe8d3cca69b2c4867aeee34f5700470/research/six-hour-20261127/escape/TROPICAL_SIBLINGS.md)

Thus a cheap sibling on a divergent-weight subset would close this particular route. Neither the shallow-clock theorem nor its weighted coupling constructs that sibling. The weaker ordinary harmonic weight `1/t` is not asserted to diverge on these dates.

## 3. Reflected grades on actual positive trajectories

For positive odd `c` with `c+m=A2^D`, I checked the physical, rather than merely accelerated, comparison. The first `D` parities agree; at that clock the two positive physical states sum to `A3^q`. If the signed full horizon has at most `b` odd departures, then `q≤b`. Continuing any final even run on the positive side adds no odd departure and produces an actual odd state at most `A3^b`. `SignedGradeSplit.lean` proves these statements for arbitrary complement coefficient and signed count.

For the mark 17, a first signed path of `7ℓ` distinct states has product at least `1/(7ℓ+1)`. Hence its complement ratio approaches 17 exponentially when `ℓ→∞`. The physical split is essential: on one nonperiodic positive orbit, its true future floor `M` forces `M≤17·3^(7ℓ)`, so late marked visits really have large `ℓ`. Large starting numerators alone would not suffice; the explicitly terminating marked family is a counterexample to that stronger inference.

I reconstructed the uniform rank count by splitting at `ℓ=floor(log₂ L/12)`. Each short signed path charges a genuinely visited positive state of size at most `17·3^(7ℓ)`. At a successful date the total positive multiplicative distortion is bounded by `K/w`, `K=17(3/2)^h`. Each small state consumes at least a constant divided by that cutoff in the logarithmic distortion budget; multiplicity of charging is at most the short path length. Long signed paths put the logarithmic phase in an arc of length `O(L^(-1/128))`.

A coprime rational approximation to `log₂3` produces the displayed circle-grid bound with errors `L/q`, `L/Q`, and `q(1+log(K/w))`. Summing over the finite pool uses `Σ_{w<K}log(K/w)=O(K)`, so the constants are uniform in the overhead and the location of the rank interval. Integer separation alone gives `O((3/2)^h L/log L)`.

I checked **Wu–Wang's actual Theorem 1**, rather than transferring a bound on `log 3` by its title. It bounds the three-term form `p+q₁log2+q₂log3`; setting the integer constant to zero and choosing a fixed allowed epsilon gives `||q log₂3|| ≫ q^(-5)`. This supports the claimed power saving and the `M^(1/640)` visit-gap bound. [Primary journal statement](https://doi.org/10.1016/j.jnt.2014.03.007)

For the finite recurring-difference conclusion, bounded distortion on infinitely many successes implies a finite product limit for each successful root. Each root supplies one limiting phase. A fixed positive gap can correspond to at most one orientation of an unordered pair of distinct phases, because two opposite positive gaps would give an integer multiple of the irrational `log₂3`. The recurrence-to-success converse separately imports finite simple-path reciprocal packing; the rank and visit-gap estimates do not use that converse.

The two terminating families and the ordinary-height count were also reconstructed. The marked family has exact word `[D+1,1,1,2,1,1,4]`. In the unmarked family the inherited strict cone confines `D-e` to seven values; their first signed images are `11,31,41,23,97,199,403`. The three that reach 17 do so with the wrong odd-count residue, and the others enter separate cycles. The negative Lean theorem keeps the cone as an explicit hypothesis. The full ternary coverage follows from `v₃(c₁(k)-c₁(j))=v₃(k-j)`; the common binary germ follows from `3c+1` being divisible by increasing powers of two. The ordinary endpoint count splits long signed paths into short intervals below `17·2^D` and counts short positive-part compositions. All strict exponent margins were checked as exact integer inequalities.

The root's separate native-clock checker used 21,387 positive complementary splits, found 44, 189 and 342 genuine graded instances at marks 1, 5 and 17, checked large family parameters through 1024, and enumerated 9,841 ternary residues per family. Its implementation follows every physical state instead of summing accelerated valuations. Both Python modes agreed. These are finite controls of the written all-input arguments.

## 4. Binary-cycle source concentration

For the four-bridge theorem I reconstructed the real-depth bit encoding and both transition inequalities. Reverse reduction modulo three identifies an ordinary four-sum equality with coordinatewise equality of the two bit-pair sums. The aggregate six-state recursion remains valid for nonsymmetric populations in the four middle states. The 216 point/open phase cases retain the equality boundary at `49/50`; endpoint order and unwrapped labels control interpolation through the whole slope enclosure. The three exact forced returns all have energy below `3^(999n/1000)`.

The key arithmetic transfer is made at the original numerator source. On each actual segment, least residues satisfy `2^vH-3^wZ=d` because the last binary margin dominates `d`. After summation, the **same** integer circular carry is subtracted in the two coordinates. The difference is `d` times the balanced ordinary numerator sum. Its exponential smallness and the actual coordinate divisibilities meet the integral, nonprimitive form of the Subspace Theorem. The two coordinates must eventually coincide: a zero coordinate is too large unless both vanish, and a fixed nondiagonal rational line cannot have coordinate ratio tending to one. I checked this against **Bilu, Theorem 2.3**, and Weaver's precise Lemma 4. [Bilu primary exposition](https://arxiv.org/pdf/0907.2098) · [Weaver 145](https://rstation.ai/problems/collatz/papers/145)

After fixing the exterior and cut data, the four local completions factor in the relaxed language. The actual cycle words are a subset; no independence of actual cycle phases is assumed. Normalized-frequency Fourier orthogonality equates the fourth norm of each unnormalized measure with its collision count. Hölder bounds every convolution atom. Four discarded fractional parts and the original short source interval cost at most six residues. Exterior bits and real-phase choices give the stated exponent, hence

\[
\liminf\frac{\log(dX)}{\log P}\ge\frac{3000}{999}
\quad\text{when }\log d=o(\log P),\ W\le99/50.
\]

The imported upper irrationality exponent 3 then contradicts such a sequence. Root and reviewer read Chudnovsky's **arXiv:2610.28079v1, Theorem 11.1**, including the ratio normalization and positive rational inputs `(3,2)`. Neither independently rebuilt that preprint's analytic proof or Lean chain. The conditional deduction is therefore labelled **SOURCE-QUALIFIED**. Its effective arithmetic certificates do not make its asymptotic threshold effective. [Primary preprint](https://arxiv.org/html/2610.28079v1#S11)

I also checked the reviewer's explicit improvement `d>P^(1/8000)` eventually: choose packing slack `1/2500`; the denominator is absorbed with positive margin `499/20000000`, and the final rational exponent margin is positive. Fixed-denominator finiteness follows. Finiteness alone is not equivalent to that stronger denominator-power statement, so the integration clarifies the implication and the actual equivalent sequence exclusion. It also distinguishes the reduced slope denominator `q` from the odd period `P`.

The fixed-source excursion uses the same located count at slope exactly `log₂3`. The affine sum gives height at most `4(A+n+1)`. Counting all but a logarithmic number of endpoints of an injective segment yields `n≤C_t(A+n+1)^t`, with `999/3000<t<1`. Splitting at `n>A+1` absorbs the `n^t` term. No irrationality exponent is needed. Repeated laps are excluded by the injectivity premise.

Finally, the full unforced transfer admits one strictly positive comparison vector. All three return matrices expand it between the stated exact power bounds. Positivity at bounded-length entrance and exit fragments extends the comparison to fixed single-bit ends and arbitrary intercepts. Its lower bound applies to the whole unforced path population; it is not a lower bound for an arbitrary selected subfamily. The upper bound gives the near-cubic height exponent `15000/5031`; the lower bound shows why this particular unweighted individual fourth-norm estimate does not cross three in the full two-layer language. Mixed convolution, additional actual-cycle constraints and other methods remain open.

## 5. Integration changes, external intake and open obligation

The original singleton manuscript is preserved as a rejected source. The corrected moving proof is copied unchanged. Four cycle manuscripts have only display-delimiter repairs, except for the three reviewed quantifier/conditioning clarifications in the four-bridge paper. Their originals are preserved. The binary Lean source has only fourteen added `#print axioms` requests; its proof terms are unchanged. The manifest records both original and integrated hashes.

The root also read the new guides at PR 195 `03b26119164664d08eaa04a1ea1d159dd4eccd7a` and PR 201 `4c36876ebbe8d3cca69b2c4867aeee34f5700470`. The latter's tropical sibling manuscript was reconstructed and used with the dependency boundary above. The root read the former's phase-population proof and parts of its height-to-entropy argument, and PR 201's cross-class floor proof. The new large enumerations and formal modules on those branches were **not** independently replayed in this checkpoint. No blanket verdict is assigned to their branches.

The next global steps remain explicit. In the escaping case, simultaneous valuation control must be turned into a sufficiently cheap ordinary off-ray ancestor on the same source. In the cyclic case, narrow/sparse constraints must become an exclusion of every permitted integer cycle, including all finite exceptions and all unrestricted excursions. No theorem in this checkpoint discharges either obligation.
