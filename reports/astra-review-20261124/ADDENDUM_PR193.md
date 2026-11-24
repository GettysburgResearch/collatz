# Scoped cross-review of PR193

**Frozen source.** GettysburgResearch/collatz PR193, commit
`654d0fbb39326a6b8e5f3202e5702c3f15dc9a26`, directory
`research/astra-universal-descent-20261124/`. This review concerns
`cycles.md` C5/C5.1, `CycleCore.lean` sharedDvd/scaledWindowBound, and
`escape.md` §§1a–1b. Comparison is with the separate R1–R3 rotational packet
and `mergers/TWO_ANCHOR_MERGERS.md`, section “A smaller partner at the very next clock.”

**C5/C5.1 — verified written argument at this pin.** For a primitive positive
rational cycle of shortcut period A, the full reduced denominator d divides
2^A−3^p and is coprime to 6. These units preserve d at every rotation.
Write e=dm, where m is the minimum, and h=P(k)<A. For any s+t=h the
h+1 boundary states around the minimum are distinct. Since there are only
h distinct cyclic length-k factors, two such states have equal k-bit
futures. The integer numerator difference is divisible by 2^k, by subtracting
the two affine equations. Thus the higher numerator exceeds or equals e+2^k.
Backward j-step numerators are at most 2^j e, and forward j-step numerators
are at most (3/2)^j(e+d)−d. Subtract e, multiply by 2^t, and maximize
over the two sides to obtain exactly C5.1, including s=0 or t=0.
With s=ceil(h/γ) and γ=1+log(2)/log(3/2), both envelopes are bounded by
2(e+d)2^(h/γ); the higher numerator is strictly above 2^k. The product
over odd steps gives Λ≤p/(3m), closing C5's elimination of m. No missing
ordinary-realization assumption or uncanceled denominator was found.

**Overlap.** Exactly 1/γ=log(3/2)/log 3=1−log 2/log 3. For d=1 and a
repeated k-factor, C5 with P(k)≤A−1 gives k<A/γ+O(log A), using
PR177 TS7 for polynomial control of 1/Λ. This is precisely the leading
threshold in R1's asymptotic overlap bound. Consequently C5 and TS7 also
exclude rotational Hamming distance two for sufficiently large periods.
R1 retains the specific divisor D/gcd(D,C_v−C_v') of the full denominator
for each matching pair; R2 handles all periods via an explicit logarithm
enclosure and complete short-period arithmetic. C5 in turn keeps the
actual P(k) and controls low-complexity scales where the longest-match
test need not help. R3 supplies a separate arithmetic block-transposition
divisor. These conclusions do not justify a priority claim about the shared
asymptotic threshold.

**First unsupported cycle step.** A primitive cycle can have P(k)=A at a
scale where a match would have implied exclusion. At smaller scales the
known consequences may instead force P(k) to be large. Neither argument
produces a repeated factor of the required length, or forces P(k) below
C5's exclusion threshold, on an arbitrary nonstandard ordinary cycle.

**Finite synchronization — verified scoped inference.** In §1a a terminally
injective set in a translated interval remains injective at all earlier
odd clocks. In a fixed-p shortcut class, stripping the first k steps costs
exactly p odd steps, so the endpoint induction inherits injectivity at the
residual clock. The interval contraction and clock slack in §§1a–1b are
independent of the translation. At the critical exponent one therefore
gets O(L^θ/sqrt(log(2L))) terminal fibers at a common O(log²(2L)) odd
clock. Keeping the least positive source of each fiber certifies a smaller
ordinary partner for every other interval source. It supplies no bound of
zero for the number of exceptional representatives, and the source itself
already makes this limitation explicit. The half-size selector resolves a
specified source when 3^H M≡1 modulo 4, with n+1=2^H M and M odd. Neither
fiber cardinality nor that congruence proves a designated representative in
the complementary class can reach a smaller partner. No universal coverage
follows by intersection or interval enlargement.

**Validation.** Independently replayed the frozen `cycle_check.py` with
Python: 179 primitive positive cycles, 4,384 C5.1 splits, three C2/C3
fixtures. Source inspection confirms that sharedDvd/scaledWindowBound
formalize shared-word spacing and its supplied-window comparison.
No fresh Lean compilation or synchronization-code replay was performed
for this cross-review.

## Final fixed head and two further controls

PR193 at `52beff703fd3ce798c430e5af8199eb58d41bf93`, same directory.
The original cycles.md, CycleCore.lean, escape.md, shadow.md and
cycle_check.py are unchanged between the two pins.

**HIGH_COMPLEXITY_CONTROLS.md, main theorem — verified written construction.**
Select clocks with p≡1 and A≡0 modulo a common exponent for 2 and 3 at the
prescribed finite modulus (after removing 2,3). Density of the irrational
rotation permits Λ in a fixed positive band below log(1+1/(3H)).
This makes D comparable to 2^A and coprime to M. The minimum occurs at
an odd phase, so the product formula bounds its single log term by Λ,
forcing minimum >H for every such word. Independent Bernoulli letters
of parameter p/A have overlap-match probability ≤(3/4)^ℓ even for
overlapping factors: successive forced matches reveal fresh letters.
Conditioning on the modal weight costs at most A+1. A union bound gives
a word with no repeated cyclic factor of length ceil(16 log A).
Adjacent 01/10 interchange changes the carry by a unit modulo D, so the
two numerical gcds are coprime divisors of D and at least one reduced
denominator is ≥sqrt(D). After that interchange a repeated factor longer
than 5ℓ+3 would force an original common ℓ-factor by deleting at most
four disagreeing positions in the comparison. Both word choices thus
preserve logarithmic saturation and primitivity, and the selected cycle
has a full exponential denominator. These examples jointly defeat any
attempt to force a long repeated factor from positivity, high minimum,
exact rational closure and finitely many local integrality tests. Their
denominators exceed one; their existence leaves the ordinary branch open.

**SHADOW_COVERAGE_LIMIT.md, headline and all-odd auxiliary bound —
source-qualified written argument using the pinned S5 representation.**
For fixed h≥1, u odd and coprime to 3, n=3^h u, partners specifically at
T(n) have excess d=k−h−1. Under the stated budget (9/2)^d≤u/(2·3^h),
an expanding multiplier would produce the positive integer gap
2^(s+p)−3^(h+d)≥1; multiplying by u contradicts the bound on the prefix
intercept. Thus the multiplier contracts. For a prefix of length s ending
in its d-th odd, the positive tail start r is strictly below
3^d/(3·2^s). Its ordinary path to 1 with h+1 odd steps has at most one
length. Each prefix-tail pair fixes at most one unit residue modulo 3^d.
Summation gives normalized class mass at most S/3, with S<1.932.
With u≤X, summing the integer rounding errors costs O_h(X^{log(3)/log(9/2)}),
which is o(X). Restricting to odd units gives relative upper density S/2
for affordable partners, hence relative lower density >17/500 for failures.
The all-odd-prefix restriction gives ≤1/8 coverage even without that budget,
since its d-specific mass is <2^{-d}/3 for d≥3 and d≤log₂ n.
Fresh exact replay of `coverage_bound.py` confirmed finite part <1.931
and all-depth tail bound <0.001. This concerns T(n) for fixed h. The
half-size selector uses T^(H+2)(n), and an interval's synchronized fiber
may meet at other clocks. No density statement here rules out those later
mergers. No new Lean replay was run.
