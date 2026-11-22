# Independent review: unrestricted zero-atom bound and minimum census

Date: 2026-11-22. Reviewer lane: potential / sibling transport.

Reviewed `research/lean-global-closure-20261121/closing/ZERO_ATOM_CLOSING_ATTEMPT.md` at SHA-256

`7bada4db374c4150e59421bf36b9a829f58cd172a4e6211af5ef2faba39cadb6`.

**PASS within the stated written scope.** I reconstructed the atom/ordinary-point correspondence, the minimum inequality, the count including repeated primitive periods, the Matveev conversion, and the polynomial-time claim as a function of numeric A. I found no mathematical correction needed. This receipt does not claim full cycle exclusion, replay the general proof of Matveev, or replace the separate Lean build receipt.

## 1. Whole-word correspondence

The affine numerator in ZA1 is correct for zero-based odd positions: each odd-step contribution is multiplied by all subsequent factors of three and by the appropriate earlier power of two. A positive integer fixed point for the supplied affine word must follow that word physically. At the first wrong parity, its reduced denominator becomes two with odd numerator; every later supplied affine branch keeps the numerator odd while increasing that dyadic denominator. It cannot return to an integer.

Conversely the actual parity itinerary of a positive T^A-fixed point supplies the displayed whole-denominator divisibility. Two distinct words cannot correspond to the same ordinary point because its itinerary is deterministic. Thus N₀ counts the actual fixed points with the stipulated odd count, not formal residue realizations.

## 2. ZA3–ZA5: minimum and exact cycle counting

Multiplying the odd-to-odd equations over one complete traversal, including repeats of a shorter primitive traversal, cancels the full multiset of positive odd states. The total accelerated valuation is exactly the complete shortcut clock A. This gives the product 3^p/2^A in Section 2.

The product-deficit inequality applies to u_i=1/(3x_i+1). Since x_i≥m, each u_i≤1/(3m+1). Cross multiplication by the positive denominators gives exactly

D(3m+1)≤p2^A.

Rearrangement and the floor yield ZA3 with no missing rounding term. The minimum is odd because an even minimum would halve to a smaller state. It is not divisible by three: an odd multiple of three leaves that class, and a shortcut orbit that has left it cannot re-enter. Hence the finite candidate set ZA4 contains every actual cycle minimum.

A primitive cycle of least shortcut period ℓ divides any return clock A and contributes exactly ℓ ordinary points to N₀. Its minimum is unique. Distinct primitive cycles have distinct minima, since a deterministic orbit cannot lie in two cycles. This proves N₀≤A·#M and then ZA5. No restriction on the supplied word's block complexity is used.

In particular, a repeated length-A traversal of a primitive ℓ-cycle contributes ℓ rather than A. The zero-atom target N₀<A can exclude primitive A-cycles while still allowing these shorter repeated traversals. The note preserves that distinction.

## 3. External logarithmic-form input and ZA7

I independently inspected the primary statement of Matveev's Corollary 2.3, printed page 1219, in the English publication:

[Matveev, Izvestiya: Mathematics 64 (2000), 1217–1269](https://www.mathnet.ru/links/f6f77a36b461e5d67deec84dbd605a71/im314_eng.pdf), DOI [10.1070/im2000v064n06ABEH000314](https://doi.org/10.1070/im2000v064n06ABEH000314).

It bounds a nonzero homogeneous logarithmic form using fixed algebraic heights and permits the unweighted coefficient maximum B*. For 2 and 3 over Q, the height cutoffs log 2 and log 3 exceed 0.16, and B*≤A because 1≤p≤A. Its constant satisfies C₁(2)≤2^32. The pinned PR183 specialization at `68345f60a4f757acb42a69a4ac95910f8ce26163`, `FREE_EXPONENT_CYCLES.md`, Section 4, therefore gives the stated conservative effective power bound. Unique factorization excludes a zero form.

For Λ=A log 2−p log 3>0, the identity D/2^A=1−e^(−Λ) is exact. Splitting at Λ=1 gives the displayed uniform lower bound D≥c2^AA^(−K). Combining it with the elementary minimum bound gives M≤(3c)^(−1)A^(K+1), and multiplication by A gives ZA7. Constants are absolute and effective; their enormous size is explicitly retained.

The primary theorem is an external imported result. This review checks its statement and the specialization, not its general transcendence-theory proof. The elementary atom and minimum-census statements do not depend on it.

## 4. Complete minimum census and numeric-period complexity

The proposed algorithm enumerates every possible ordinary minimum, follows its actual shortcut orbit, and rejects any proposed minimum that falls below its starting value. If a return occurs, the first return has the primitive period ℓ and the recorded odd count q. The acceptance conditions ℓ|A and q(A/ℓ)=p are exactly the required complete traversal conditions. Adding ℓ gives the correct number of fixed points. A non-minimal state on an eligible cycle encounters its actual minimum before its first return and is rejected, preventing duplication.

I read `zero_atom.py`. Its `zero_count_by_minima` routine implements this order: it counts the parity of each starting state, steps once, checks the floor, records the first return, and terminates that candidate. The repeat-period arithmetic and contribution ℓ match the written proof. The exhaustive word census is a separate finite control; it is not part of the polynomial-complexity claim for the minimum routine.

Under ZA6 there are polynomially many candidate minima in numeric A, with at most A steps per candidate. The bound T^j(m)+1≤(3/2)^j(m+1) gives O(A+log M) bits for every intermediate integer. Computing the full powers 2^A and 3^p, integer division for M, the orbit steps, and the divisibility checks all use polynomial bit complexity in A. Even storing an entire candidate path remains polynomial. The note correctly does not claim polynomial complexity in log A or that all periods have thereby been checked.

The binomial denominator is exponentially large throughout 4A≤7p and 2^A>3^p because p/A remains in a fixed compact subinterval of (0,1). A polynomial upper bound on the numerator thus gives an exponentially small zero-atom probability, but it does not reach the primitive-cycle exclusion threshold N₀<A. The note explicitly retains that final missing factor.

## Review exclusions

The exact finite census totals and the optional (27,17) maximum-fiber calculation are not independent proof premises in this review. I did not rerun those controls or any old Lean build. The separate compiler receipt owns the assertion that `CycleMinimum.lean` checks the stated finite inequality. No unrestricted cycle theorem follows from this receipt.
