# Independent review of the signed-target arithmetic note

**Reviewer:** pressure agent, separate from the author.

**Reviewed artifact:** zen_arithmetic/SIGNED_TARGET_ARITHMETIC.md,
SHA-256

    ff735ef39a5b7de1830d40b8a6b21cdaca2a183346ecf5129992bf659a04ff6b

The repository source claims in that note are pinned to PR146,
561d48a4d3a793a59b1cdf0406062ae1a6d47515. The verdict below applies
to the four claims at the displayed artifact hash, not to later edits,
the whole source packet, or a complete Collatz proof.

## Verdict

**STA1–STA3: VERIFIED at their stated scope.**

**STA4: VERIFIED relative to the explicitly imported reciprocal
packing estimate**
\(\sum 1/x\le160F^{-1/40}\) for a nonrepeating odd orbit above
\(F\). I checked the source statement and its domain in
research/astra-three-routes/pass2/ORBIT_MELLIN.md, Section 3.
This review does not independently reprove that earlier packing
theorem.

No correction to the four statements is needed.

## Main checks

For STA1, positivity of the target and the fact that a signed path
reaching five stays at or above five imply \(b\ge1\). An even target
therefore has even signed magnitude. Removing its first halving
preserves the first-hit property and decreases \(b\) by one.
The converse follows by prepending a halving. On a nonrepeating
ordinary orbit, distinct even stretches cannot normalize to the
same odd state.

For STA2, the two starts \(c\) and \(-M\) differ by \(5\,2^b\),
so the first \(b\) parity bits agree. The accumulated affine
difference is exactly \(5\,3^r\), with \(r\) the signed odd count
in those \(b\) steps. This gives the claimed ordinary endpoint
without requiring a bound on \(b\). The remaining signed path
has length \(3k\), and its affine numerator has the correct minus
sign. Multiplication by \(3^q\) gives the upper bound
\(5(9^k-8^k)\).

The endpoint set permits visits to the signed cycle before the
last clock; that is a valid enlargement of the first-hit targets.
Appending one cycle lap increases the length by three and the
odd count by two, leaving its target value unchanged. This proves
the nesting assertion but does not prove convergence of its new
members.

For STA3, I independently enumerated signed inverse states with
ordinary integer arithmetic. The first two target sets are exactly
\(\{1,5\}\) and \(\{1,2,5,7,23,27,28,85\}\). Independent shortcut
replay reproduces every displayed hitting time.

For STA4, the first-hit signed path can contain the odd input seven
at most once, cannot contain five before its terminal time, and has
all other odd inputs at least nine. Multiplying its signed factors
therefore proves the stated bound with
\(\theta=13/(9\sqrt2)\).
The fixed-floor assumption covers both future representation
lengths \(b_i\); neither need be bounded by the time between the
two visits.

The exact integer inequalities

\[
169^{32}>3\,162^{32},\qquad
25\,169^{64}<2^{128}162^{64}
\]

validate the two comparisons involving \(\theta\). Each signed
logarithmic error lies in
\((-4F^{-1/64},0)\), so their difference is bounded by
\(4F^{-1/64}\), not twice that number. Adding the ordinary
correction gives a constant below 64.

At \(F\ge2^{448}\), the resulting error is at most one half.
Since the odd-clock gap is positive, the binary exponent \(B\)
is then positive. Unique factorization makes \(3^d\) and \(2^B\)
distinct, and their integer separation gives the claimed
\(F\le2^{448}3^{64d}\). The complementary small-\(F\) case is
immediate. No algebraicity of a limiting correction is assumed.

## Independent arithmetic receipt

signed_review_report.json records a separate implementation's
inverse enumeration through \(k=6\). The target counts are

    2, 8, 22, 54, 133, 317

and their maxima are

    5, 85, 1085, 12325, 131405, 1346485.

Nesting and the exact maximum formula hold in those checks.
The two small sets and all eight stated ordinary hitting times
were independently reproduced. I also ran the author's checker,
which reported PASS with 11,791 signed first-hit replays and
20,632 dyadic replays.

These computations verify finite arithmetic interfaces. They do
not prove convergence of every finite target set as \(k\) varies
or exclude infinitely many increasingly separated visits.
