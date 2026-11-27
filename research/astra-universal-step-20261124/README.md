# Attempting the unrestricted ordinary step

**OPEN: this pass did not prove universal descent, vanishing survivor mass, or exclusion of all positive cycles.** Its purpose was to prove the missing implication from the previous checkpoint, using actual positive integer sources. Three GPT-6.2 Astra workers tested inverse optimization, a joint real/ternary singular kernel, and a positive inverse-transfer certificate. The root also tested the actual head-parent coupling interface in the latest upstream work.

## What was proved

For the shortcut map, a binary word of length n with u odd steps has forward affine multiplier 3^u/2^n. At a positive integer endpoint y give a legal inverse history the normalized weight

    y^(-7/4) (101/100)^n (3^u/2^n)^(7/4).

The written proof in [descent.md](descent.md) bounds the entire sum over two specified carry classes, over all lengths, by **10^15 y^(-1/200)**. Here “nonperiodic endpoint” means that y itself is not on a cycle; eventual convergence to the usual cycle is allowed.

* One class has two equal-length blocks with equal odd counts and congruent carries. Their words may differ.
* The other has arbitrary length-kh histories, k at least three, whose count and carry residue match a k-fold reference word. The reference need not occur in the actual history.

Both permit arbitrary initial and final flanks with combined length at most h/25. The proof counts every description, so overlaps only enlarge the bound. The key arithmetic is a large power of three dividing a nonzero signed deviation from the reference's fixed point. A weighted finite carry norm controls the multiplicities. Literal repeated words are a special case.

This estimate is a bound on part of the actual kernel, not a theorem that every trajectory enters those classes. It excludes endpoints on cycles from its scope. Eight Lean theorems in [descent.lean](descent.lean) certify the actual chronological histories, affine transport, powers, distinct-block identity, divisor transport and stationary case. The weighted norm, interpolation and infinite sum remain written mathematics.

## Why the proposed closing bridge fails

The full inverse minimum did not force a cheaper ordinary competitor. More decisively, compulsory long matching pairs cannot bridge the new estimate to a fixed escaping source. For actual adjacent blocks of length h and odd count v, congruent carries and distinct checkpoints imply

    (4/3)^v < x+1,     h < 7 log_2(x+1),

where x is the pair's starting value. With a prefix flank of length at most h/25 from a fixed original b, this gives

    h < (175/18) log_2(b+1).

[arithmetic.md](arithmetic.md) proves the bound and states the all-horizon inverse-minimum test. Two theorems in [arithmetic.lean](arithmetic.lean) verify its integral growth and separation steps; the logarithmic deductions are written proofs. This is a rejection of that proposed bridge, not an exclusion of ordinary escape.

## Other direct attempts

[moment.md](moment.md) retains the actual joint real and ternary variables. It bounds leakage from deep fractional denominators and constructs rational preimages of every fixed ordinary endpoint with a uniform harmonic-mass lower bound. Making those preimages ordinary requires an endpoint adjustment in a specified class modulo 3^d. The uncontrolled factor 4^t in that repair prevents an ordinary-source conclusion. The original integer survivor retains coefficient one. A separate elementary estimate controls the untilted subseries with bounded total multiplier, again leaving a growing fixed-source contribution possible.

The positive transfer construction gives a precise attempted certificate: a positive weight tending to zero at infinity with strict incoming surplus would force descent. Its smoothed version has an exact ordinary recurrence. The proved summable parameter range loses the surplus, and the surplus range has no proved ordinary trace bound. These failures are recorded to prevent reuse as a completed proof.

## Evidence and continuation boundary

The [independent review](../../reports/astra-universal-step-20261124/INDEPENDENT_REVIEW.md) and [root review](../../reports/astra-universal-step-20261124/ROOT_REVIEW.md) identify the checked arguments and source hashes. [Source pins](../../reports/astra-universal-step-20261124/SOURCES.json) record the latest upstream heads inspected. The [replay program](../../reports/astra-universal-step-20261124/replay.py) builds fresh Lean objects in dependency order, queries all ten public declarations for axioms, compares normal and optimized exact Python controls, and validates a clean complete checkout.

The first unsupported assertion is still an estimate on **all unmatched ordinary histories** strong enough to defeat the persistent contribution of one fixed positive source; stationary positive cycles also remain. No forced repetition, finite-window optimality, fractional preimage count, or averaged ternary estimate is substituted for that assertion.
