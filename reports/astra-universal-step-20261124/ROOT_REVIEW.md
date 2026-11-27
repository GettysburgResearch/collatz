# Root review of the unrestricted-step attempt

Status: **partial arithmetic estimates verified in written review; closing implication OPEN.** The starting repository checkpoint is 045be43632f274dd64faf15714e42cc8de27a2e9. This review does not promote any external manuscript's claimed formalization to a locally rebuilt dependency.

## Exact ordinary kernel

I reconstructed the signed determinant for powers and for two distinct chronological words. Equal raw clocks and odd counts are retained separately from equality of carries. Coprimality of the powers of two and three is used only after the integral identity. For a periodic reference matching a longer arbitrary history, multiplying the carry congruence by Q-P gives the advertised divisor P^k. If the deviation vanishes, the actual parity-cylinder residue shows that the positive integer endpoint realizes the reference word and is itself periodic. It is not enough merely to call a rational affine fixed point an integer cycle.

I checked the carry upper bound by moving odd bits to the end, and injectivity at fixed length and odd count through the unique dyadic parity residue. The number of carries in one ternary class is at most the integer interval length divided by its modulus. In the weighted norm, appending zero multiplies the counting weight by ell; appending one has weight one and changes C to 3C+2^h. Minkowski gives the stated recurrence. Its induction uses M_ell at least one, including the all-even case.

For flanks, positivity of the final affine map gives y at least its leading coefficient times the core endpoint. The last flank therefore loses only its time tilt. The interpolation retains the dependence on the actual y and uses theta=1/350, giving exponent 1/200. The numerical constants are conservative rational comparisons. The two-class summation is bounded by

    384 (1+1/(1-0.606)) / (1-0.995)^5 < 10^15.

Descriptions may overlap; all estimates sum nonnegative contributions and hence permit this overcount. The written theorem is restricted to the stated carry classes and to endpoints not on a cycle. No maximal probability over ternary roots or independent replacement law is used.

Reviewed scientific sources: descent.md SHA-256 c1b288428db8ead7412050f0802584aac4e4165469247e272cabaed469c1cabe; descent.lean dae16e576d80f83b8d990018c836138ba623305d32c2b6ffe3fc8466c55ab119; descent.py 7e27b2dc3e62e57551f9f76f1176623f900674e4e0a971bd3e79ba7cf051c07c. The Lean core is inspected here; the separate fresh replay supplies execution evidence.

## Fixed source and rational leakage

The fixed-source separation follows by subtracting the actual two affine equations. A nonzero difference divisible by 3^v has magnitude at least 3^v. The shifted coordinate n+1 grows by 3/2 on an odd edge and decreases on an even edge. On positive integers the unshifted odd edge grows by at most two, yielding h at most 2v+log_2 x. The resulting bound h<(175/18)log_2(b+1) with the short initial flank is valid. It prevents a compulsory-large-matching-pair argument from treating arbitrarily long prefixes of one injective source. It does not prove that the source converges. Reviewed arithmetic.md SHA-256 1419df3f23d5021dc15b298c4732191b46e859cb4ce9f8a98e289fbf23f5ae59. The root added only two named axiom queries to arithmetic.lean after the worker's check.

For the singular-kernel identity, the exact denominator drops by one under each rational odd step until the input is integral. Keeping real source at least one makes the displayed fractional tail sum finite. The d=0 summand is exactly the ordinary survivor term and has no decay factor. In the rational amplification, the initial safe exponent and the tail fractional-moment bound imply every intermediate inverse is positive and every denominator is exact. Deterministic forward evaluation proves distinctness; projecting the positive-probability infinite tail event onto finite words is legitimate. The final congruence repair reads a complete class modulo 3^d and supplies no small representative bound. I also checked the independent collision identity and the bounded-multiplier untilted subseries estimate. Reviewed moment.md SHA-256 610ae05c5747e847d2e45507d75d164a59063e6efc2b389dd73523b9573c293c.

## Upstream comparison and failed universal argument

The root read the updated PR193 ordinary head diagonal, PR197 original-source first-passage and spatial estimates, and PR199 joint first-passage criterion. Their supplied marginals or positive diagonal mass do not bound the full weighted off-diagonal mass. The affine-pair coalescence estimate gives a square-root clock tail, while the direct complete binary-grid sample offers logarithmically many clocks. This is insufficient for the stated summability route. No missing law on the selected late trajectories was assumed.

The main new carry estimates are elementary and do not depend on the recent external positive-basin-density results or on the newly inspected critical L2-law manuscripts. Those sources were explored for the remaining trace bound; they did not provide it. The formalization does not assert any analytic limit or universal convergence. Fresh compile logs, exact-control logs and the clean-checkout receipt belong to the verification report, not to this written proof verdict.
