# Q-9302 — Two-place room-cusp proof mechanism

**Claim ID:** Q-9302  
**Title:** Can the equivalent two-place formulation yield a proof mechanism unavailable in the one-place presentation?  
**Status:** IDEA  
**Authoring agent:** `gpt56-pro-04`  
**Reviewing agents:** none  
**Created:** 2026-07-21  
**Last updated:** 2026-07-21  
**Dependencies:** `T-9304`, `L-9306`, `L-9307`, `T-9305`  
**Scope:** issue-#4 room/Cantor EQ frontier after exact split collapse  
**Related counterexample candidates:** none

## Exact reduction already proved

For `n,j >= 1`, put

\[
K=n+j,
\qquad
Q=64^n81^j,
\]

\[
u=(81^j)^{-1}\pmod{64^n},
\qquad
v=(64^n)^{-1}\pmod{81^j}.
\]

Define

\[
\mathcal D_{n,j}(H)
=
\sum_{1\le h\le H}
\frac1h
\left|
\widehat\mu\!\left(\frac{hu}{64^n}\right)
\widehat\nu\!\left(\frac{hv}{81^j}\right)
\right|.
\tag{1}
\]

`L-9307` proves that the two local character classes are the components of the same rational character

\[
r=\frac hQ,
\]

and that the two local products stitch one contiguous reciprocal phase chain. `T-9305` then proves

\[
\boxed{
\left|
\mathcal D_{n,j}(H)
-
\sum_{1\le h\le H}
\frac1h\frac{|S_K(h)|}{2^K}
\right|
<
\frac{2\pi H}{64^K}.
}
\tag{2}
\]

Consequently, whenever

\[
H=o(64^K),
\tag{3}
\]

the two-place absolute-Fourier target is asymptotically equivalent to the original one-place EQ target, uniformly in the split.

In particular, for the issue-#4 range

\[
H=2^K,
\]

the discrepancy between the two criteria is at most

\[
2\pi2^{-5K}.
\tag{4}
\]

Thus the open problem is **not** whether `(1)` is a weaker decay statement. It is not. The open problem is whether the two-place dynamics offers a better way to prove the same statement.

## Reframed research question

Can one exploit the fixed product measure

\[
\mu\otimes\nu
\quad\text{on}\quad
\mathbb Z_2\times\mathbb Z_3
\]

and the global rational diagonal

\[
h\longmapsto
\frac h{64^n81^j}
\]

to prove the equivalent weighted decay by a mechanism that is invisible in either local product alone?

A successful answer must use more than the pointwise absolute factorization. `T-9305` proves that the latter merely repackages the original phase chain.

## What remains genuinely new

### 1. Signed transfer operators

The absolute products collapse, but complex phases need not. Construct a transfer operator retaining the phase of

\[
\widehat\mu(h/Q)\widehat\nu(h/Q)
\]

across neighboring frequencies or room transitions. Signed cancellation between frequencies could beat the copy barrier even though pointwise magnitudes are equivalent.

A useful output would be a rigorous estimate for a smoothed sum

\[
\sum_h w(h/H)
\widehat\mu(h/Q)
\widehat\nu(h/Q),
\]

with a kernel adapted to the positivity-native room recursion.

### 2. Bilateral inverse theorem

`L-9307` identifies a single reciprocal phase chain indexed by

\[
0\le\ell<K.
\]

A split merely decides which indices are read at the `3`-adic place and which are read through dyadic reciprocity. Prove that a low-energy chain has a bounded-complexity bilateral carry description, then classify those descriptions.

The target is now sharper than the earlier vague combined-energy proposal:

> Low energy on one stitched chain should force exact `64`- or `81`-divisibility, a periodic carry template, or amplification to a forbidden full frequency block.

### 3. Hyperbolic solenoid renewal

The character pair is not an arbitrary CRT graph. It is the local image of one global rational `h/Q`. Under the hyperbolic action induced by `81/64`, its two local coordinates move in opposite directions.

Seek a quantitative renewal theorem for this rational diagonal that controls how often the digit mask is nearly annihilated along a finite bilateral orbit. The theorem must be uniform in rational height and strong enough for the initial segment `1<=h<=H`.

### 4. Room recursion with positivity

Issue #4 shows that the base-`81` room digits are wrap counts of the `H`-orbit and that the finite marginals form an inverse-limit tower. Fourier absolute values may remain the wrong language below the fair window.

Use the stationary local measures to write the exact tower kernel, but prove contraction directly for interval counts, relative entropy, or a positive transfer operator. Such a proof could solve the equivalent EQ criterion without passing through `(1)` term by term.

## What would count as progress

1. A signed or smoothed two-place estimate not reducible to the pointwise triangle inequality of `T-9305`.
2. A low-energy inverse theorem for the stitched reciprocal chain.
3. A positive transfer-operator contraction for the room tower.
4. A theorem showing that exceptional depths across adjacent scales force an impossible bilateral carry template.
5. A rigorous obstruction proving that every two-place signed strategy also collapses to the one-place wall; this would close the method branch honestly.

## What is now ruled out

The following is no longer a viable claim of progress by itself:

- proving decay of `D_(n,j)(H)` in a sub-`64^K` range without recognizing that the same proof has simultaneously established the original EQ weighted decay;
- treating the two local absolute factors as independent sources of energy;
- using full-group moment factorization alone to infer short-orbit decay;
- invoking the branch-qualified room-position map merely to transfer absolute Fourier magnitudes, because `T-9305` supplies a direct phase-level comparison for that purpose.

## Dependency audit

- `T-9304` supplies the exact product coefficient.
- `L-9306` supplies full-group moment factorization.
- `L-9307` supplies the global rational diagonal and phase stitching.
- `T-9305` proves the weighted equivalence `(2)`.
- The research routes above are open and are not used as premises elsewhere.
- No external large-sieve, mixing, renewal, or rigidity theorem is asserted to apply.

## Gap audit

- Equivalence of targets gives no decay theorem.
- Complex signed sums may not interact favorably with the positive counting recursion.
- The room tower does not close at any fixed modulus.
- A hyperbolic orbit theorem must handle low rational height and a singular Bernoulli measure, not Haar-generic points.
- A proof for density-one depths would not close the all-depth criterion.
- None of these routes decides whether the infinite survivor attractor contains one ordinary positive integer.

## Adversarial tests

1. At `H=1`, one coefficient can remain large; any theorem must exploit growth of the frequency set or orbit length.
2. Frequencies divisible by powers of `64` or `81` generate exact trivial factors and must be normalized before an inverse theorem.
3. Full-group Parseval is compatible with a highly exceptional initial interval.
4. A split-dependent claimed gain contradicts `T-9305` unless it comes from a genuinely split-dependent proof tool rather than the value of the target.
5. Signed cancellation that disappears after taking absolute values cannot be inserted silently into an Erdős--Turán argument; the smoothing/counting interface must be written explicitly.

## Remaining uncertainty

The most promising route is a bilateral low-energy inverse theorem followed by frequency-block amplification. The positivity-native room transfer operator is a serious alternative because the existing copy barrier may make every absolute-Fourier proof inefficient even after stationarization.

## Suggested next attack

Derive the exact carry recurrence for the common phases `q_ell(h)` across the split and classify maximal intervals on which the carries remain unchanged. This is the correct starting point for either a signed transfer operator or exceptional-frequency amplification.