# Independent arithmetic and normalization review

**22 November 2026. Scope: the new displayed deductions in this packet.**
This is a written cross-check by the boundary-attack agent, separate from
the authors of the three notes below. It is not a Lean receipt, a review
of all inherited proofs, or evidence of universal Collatz convergence.
The review did not modify those notes or their fixtures.

## Termination: pair congruences and the existing envelope

Reviewed `../../research/deep-machinery-20261122/termination/MODE_REFINEMENT_ATTEMPT.md`
and its exact checker.
The pair composition, rational points, and displayed valuation table were
independently recomputed from `X=3^b`, `Y=2^b`, `D=9X-16Y`, and
`B=13X-8Y`.

For `b>=3`, `D` is a unit at both 2 and 3. If the stated CRT congruence
holds, the remaining dyadic precision at the final pair boundary `n_K`
is at least four. At each intermediate `y_j`, including the last one,
it is at least `b+5`. These margins preserve exact active modes 2 and
`b`; the different next modes make both repetition counts exactly one.
The ternary precision is strictly above the required `b+2` valuation
of `z_b(n_j)` and above all other displayed valuations. In particular
the final `n_K` still has the claimed envelope value.

The envelope convention was checked against its definition:
`z_0=-n`, `z_1=1-n`, and `z_2=n+5`. At a pair boundary the candidate
denominators are therefore `1,3,9,3^(b+2)`; at an intermediate point
they are `1,3,81`. For `n>=10`, the comparison
`(n+5)^2 < 3(n-1)^2` holds. The given bound
`z_3(n)>6(n+5)` and the exact identity
`z_(a+1)(n)-3z_a(n)=2^a(2n+1)>0` establish the remaining comparison.
Thus the selected index is genuinely 2, using the inherited finite
envelope formula as a premise.

The unsafe-start indexing gives precisely `2K-1` subsequent maximal
modules without repayment. The repaired pair rank has factor
`3^(b+2)/2^(2b+8)<1`; its dyadic counter drops by `b+4`.
No arithmetic error was found in these deductions. The review does not
prove the parent finite-envelope formula or any statement about an
infinite ordinary orbit.

## Rigidity: residue factors and the continuous Boolean control

Reviewed `../../research/deep-machinery-20261122/rigidity/GUARDED_DILATION_ATTEMPT.md`.

The normalizing factor in `B_r^q=q L_X(1_(n=r mod q) P)` was checked
by the logarithmic change of variables; the fixed multiplicative change
in cutoff costs `o(1)`. Splitting by parity gives the stated specified
ternary residue, rather than the unrestricted ternary correlation.
The finite-depth formula follows from the affine iterate on a complete
binary residue cylinder; the binomial coefficient counts and the
remainder retain exactly the displayed factors `2^(-k)`.

For the circle density, the sum of all absolute amplitudes is `1/2`.
Unique factorization makes the nonzero frequencies distinct, yielding
the Fourier coefficients in (3.3). For every integer frequency, their
ratios are exactly those needed for the averaged pushforward equation.
The density is therefore a positive continuous probability density,
but is not separately invariant under multiplication by 2 or 3.

Conditional uniformity of the independent phase makes the Boolean
rotation process stationary, and linearity in the slope law proves the
averaged identity for every finite-dimensional distribution. The covariance
sums were independently evaluated: only odd frequencies `3^k` contribute,
and summing their ratio `1/27` gives respectively
`3/(26 pi^2)`, `1/(13 pi^2)`, and `1/(26 pi^2)` at lags 1, 2, and 3.
Thus this is a valid control of the proposed inference to strong
stationarity, not a claimed ordinary Collatz sequence.

The exact source statement P1 in PR182's pinned
`INVARIANT_CORRELATION.md` was read to check the phase qualification.
It centers general rational polynomial phases; the linear phases
`a n/3` used here have zero mean. Its extension from invariant Boolean
labels to continuous functions of a bounded invariant label follows by
the stated uniform simple-function approximation. The joint empirical
product-law deduction then follows by Fourier density. No inherited
stationary-density, FLOOR, or LOG hypothesis was re-proved.

## Mahler: the first closure calculation and the final implication

Reviewed `../../research/deep-machinery-20261122/mahler/MIXED_DILATION_ATTEMPT.md`,
Sections 1--4.
The roots-of-unity filter in (M3), the ninth-root powers in (M4), and
the strict section range in (M6) were checked directly. The binary-to-
ternary section identity includes the zero residue correctly.

The eventual-period reduction was also checked: doubling invariance
removes factors of 2 from the period, the odd affine relation removes
factors of 3, and the two identities on `6r+1` and `6r+2` force constant
residue values when the remaining period is coprime to 6. Exact doubling
then transports eventual constancy back to every positive integer.
The missing finite Mahler closure remains a missing premise; this review
does not supply it.
