# Independent root review: ternary past and anchor carries

**Status: Collatz remains open.** The root read both complete new notes, all new Lean source and both checkers. The fresh independent replay passed three printed kernel audits and both complete controls in normal and optimized Python. The full outputs, source hashes and unchanged checker/C++ dependency hashes are in the receipt.

## The all-depth arithmetic theorem

For a binary odd predecessor, `3x+1=2^a y` with `a` one or two. The endpoint residue modulo three determines `a` uniquely whenever a predecessor exists. If three endpoints are in arithmetic progression with spacing a unit modulo three, one is a multiple of three and cannot have a predecessor. Otherwise they use the same exponent; reversing all three retains an arithmetic progression and removes exactly one factor of three from its spacing.

`TernaryPast.progression_spacing` proves this over signed integer witnesses at every finite depth. The eight exponent cases are handled explicitly by integer arithmetic. `no_progression` then chooses depth equal to the absolute integer spacing; divisibility by that power of three contradicts its size unless the spacing is zero. This is a genuine all-depth conclusion, not a bound observed at a chosen finite deadline. Actual binary cycle phases supply arbitrarily long predecessor histories, including when the three points belong to different cycles.

The same native reverse determinism gives a two-child ternary tree. The missing digit can depend on the entire preceding prefix. The proof never replaces this adaptive tree by a fixed digit Cantor set. Multiplication and translation by a ternary unit permute children, which proves the progression occupancy recursion after stripping the valuation of its spacing.

For a four-sum equality, the three unordered sums of two distinct first trits are distinct modulo three. The first-trit pairs must therefore agree as multisets, and their ordinary contributions cancel exactly. This gives the energy identity

\[
E(A)=E(A_0)+E(A_1)+4\sum_t r_0(t)r_1(t).
\]

The mixed sum is bounded by Cauchy–Schwarz. The root reopened [Kane–Tao, Lemma 8](https://arxiv.org/pdf/1702.00912), including its exponent `log_2 6`, and checked the scalar induction used here. It works for different adaptive subtrees and empty children as well. Constant allowed digits zero and one show sharpness on the abstract tree class. No sharpness claim is made for a collection of actual nontrivial integer cycles. The energy and occupancy inductions are written results; the third Lean declaration proves their finite first-trit separation interface.

The finite checker constructs every positive ordinary lift of the binary words through depth eight, with exact valuations and endpoint residues. It checks uniqueness, the ternary branching, modular progression exclusion and raw versus recursively split energy. It enumerates every one of the 2187 complete two-child trees of depth three and verifies the sharp interval occupancy recurrence through length 27. These controls independently test the adaptive-tree rather than only a fixed-digit example.

## Actual word entropy, without independent bridges

The entropy argument retains the previous ordinary four-segment source placement. For a fixed total division cost on a segment, its terminal residue modulo `3^n` is an invertible scalar multiple of its affine numerator, and recovers its actual native word. Thus the hereditary energy estimate bounds each selected family of words; no artificial independent source variable is introduced.

For an origin uniformly sampled among the actual cyclic phases, each segment has the same marginal word law. Recording the integer part of the surprisal of each of the four segment words costs only `O(log log p)` bits, while a bin of index `J` has at most `2^(J+1)` words. Conditional on those bins, cut dates, phase type and guards, the ordinary source count is at most a fixed constant times the geometric mean of the four energies. Taking conditional entropy and averaging gives `log_2 p <= kappa H_n + O(eta n+log n)`. Independence of the four actual words is unnecessary because the Cartesian family is only an upper envelope.

Subadditivity of stationary word entropy, followed by a weak limit at each fixed block length, yields the stated entropy lower bound. The additional inequality from the cycle product uses the quoted irrationality exponent of `log_2 3`; reducing the clock fraction's denominator does not invalidate that bound. Both the source separation and this number-theoretic input retain their stated qualification.

The root checked the opposing entropy bound without decimal approximations. A word without `222` is encoded by each `1` and a following run of zero, one or two `2`s, with weights `1,2,4`. At composition `a=2-gamma`, `b=gamma-1`, its entropy is at most `a log_2 7-b`. The exact inequalities `3^12>2^19`, `7^6<2^17` and `3^5>6^3` give

\[
a\log_2 7-b<43/72<3/5<\gamma/\log_2 6.
\]

Compactness therefore gives a positive density of `222` occurrences on any unbounded-period family in a fixed physical ratio. The exact iterate across a run of twos is `x -> 1+(3/4)^r(x-1)`. The fixed ratio bounds its run length, so many occurrences give many run starts. The preceding exponent one fixes residue `2 mod 3`; three following exact exponent-two edges and an odd endpoint fix `1 mod 128`. Their intersection is `257 mod 384`, and the third endpoint supplies `x >= 1+64(s-1)/27`. This still permits cycles with the required long descents.

## The third grade and its signed carry

The named ceiling proof is restricted to the bounded least-tripling-disagreement alternative. It uses its actual bad floor, bad-multiple-of-three floor, good neighbors and binary native exponents. It is not a theorem about arbitrary cycles with the same physical ceiling.

At a clean low phase below `4*2^(1/700)s`, the third row can occur precisely on the designated short rotation interval, up to seams whose frequency is charged separately. Sparse high sites and seams are marked; complete return pieces touching them are removed with their actual dates fixed. The full outer ceiling bounds the cost of those environments. Retained anchor visits have positive density and are not silently discarded as exceptional.

At a return cut the true signed prefix accumulator and the four terminal grades are already specified by the chosen suffix. The block therefore imposes one genuine residue condition modulo `3^r`. Fourier inversion and Hölder bound this arbitrary-residue count by the geometric mean of four individual zero-residue self-energies. This bound does not require the incoming accumulator to vanish. Relaxing negative-copy vetoes and dropping the two endpoint veto edges is performed inside this self-energy upper bound.

For a self-energy, all four terminal grades agree. At each two-row interior site the signed digit is one of `-4,-2,0,2,4`; divisibility by three forces zero. At the earliest three-row anchor, digits are `1,2,4` and only congruence modulo three is imposed. Nonzero multiples of three are retained. The next earlier return can consequently receive a nonzero carry. The proof bounds its true conditional residue anew instead of resetting that carry to zero in an ordinary equality.

The endpoint factors enumerate ordered quadruples literally. The middle transfer uses the previously reviewed two-history machine, now with the exact 23-letter rival catalogue and 1209 states. Both endpoint edges are omitted from its veto state, matching the definition of the tested one-copy families. Three short schedules independently enumerate complete one-copy paths and all fourfold modular coincidences with a nonempty toy veto; each fixture includes nonzero earliest signed digits and agrees with the matrix contraction.

The rotation enclosure checks its labeled cut order and unwrapped floors at both rational slope endpoints. It includes singleton boundaries as well as open-cell representatives. The return lengths are 665, 971 and 1636. The middle matrices are rounded upwards after division by three at every step, using scale `2^48`; the unchanged C++ implementation retains its accumulation overflow guards. Their denominator in the final endpoint test is `9*2^48`, accounting for the two removed endpoint factors. The exact comparison is below `97/100` at every common terminal grade, and `97^100000*3^1636<100^100000` gives the displayed per-letter exponent.

Conditional counting can now be iterated backwards: the chosen suffix determines the next actual accumulator, and the uniform residue bound applies to it. The source-placement argument gives the strict exponent `99999/300000`. The conclusion forcing a positive fraction above the named ceiling additionally uses the quoted irrationality exponent. Its onset and proportion remain ineffective, and the full ceiling `16/3` is not excluded.

## Neighboring work and remaining step

The root read the fifth-moment source reduction and third-layer extension on PR #200 at `df2f17a117bea06bb34040a5a97e7dc9711d9871`. That work retains one actual scalar Fourier variable, uses reciprocal-frequency separation, and pays rare third grades through a verified fifth-moment cochain. Its full numerical grid was not rebuilt here. A global real-discrepancy width bound is not identified with a physical max/min ratio without proof. The new notes credit that work and the antecedents of the hereditary and ordinary source arguments.

This checkpoint adds three exact Lean declarations, two fully replayed finite controls, and the stated written consequences. It supplies no proof that the open finite reciprocal mass vanishes, no unrestricted cycle exclusion and no exclusion of every escaping orbit.
