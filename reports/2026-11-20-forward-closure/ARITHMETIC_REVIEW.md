# Independent bounded audit of the forward defect and asymptotic operator

## Forward inverse defect

**Verdict: VERIFIED at the narrow mathematical-claim level.**
Reviewed local file:
 /workspace/scratch/c6766c1207a3/collatz_forward/research/forward-inverse-defect/PROOF.md
SHA-256:
7df5e88c2b0b0ffc2a21178b1f00c65138975302353563efd6a79c640d6149c6

The exact unit-terminal domain is F_w(Z_3^times), of normalized unit Haar
mass 3^{-k}; the prefix-free subprobability cover therefore gives the stated
constant-one tail. The extra ternary digit for generic legality, density
of the pole set, all-action Bellman inequality, and its actual-forward
orientation are correct. No average-over-lifts step occurs.

The R inequality treats infinity in the extended order. Finiteness at one
cycle state propagates backwards around that closed cycle, so the cycle
conclusion is valid. Finiteness need not propagate forward on an open path;
the text does not rely on that implication.

The critical-height formula has exact exponent-one cancellation because
c_*(log_2 3-1)=3. Its uniform positive-gain argument handles unbounded actual
exponents: eta<1 handles the large exponents and the finite remaining
range is controlled uniformly in height. The explicit floor
56*2^43 and gain 1/16 follow from the displayed exact comparisons.
Infinitely many exponents greater than one on an escaping ordinary orbit
then suffice for Z to diverge.

The uniform ordinary upper bounds remain hypotheses. In particular no
almost-everywhere finiteness or predecessor density result supplies them,
and W(1)<infinity is not assumed. The immediate-converger control correctly
asserts a finite-word lower bound on W, not finiteness of W itself.

The separately written CRITICAL_HEIGHT_ADDENDUM.md proves the additional
loglog lower bound and the sufficient coefficient-1/4 upper-bound
hypothesis; it is not included in the frozen root file above.

## Asymptotic operator

**Verdict: VERIFIED conditional on the explicitly stated arithmetic inputs.**
Reviewed local file:
 /workspace/scratch/c6766c1207a3/collatz_work/pressure_next/ASYMPTOTIC_OPERATOR.md
SHA-256:
af43f14d86a6e45d9b8396fb7c2284b8b97f4ddfff8c76a878724012f4f9f4fa

The finite positive harmonic trace, its linear bound on escaping targets,
and simple-orbit reciprocal summability are inputs to this review. Their
external proofs and the literature attributions in Section 8 were not
independently audited here.

The adjoint P*f(x)=c(x)f(Ux), strict contraction on each nonzero vector,
weak convergence of powers, conservative b-mass, and synchronous-level
mass identity check algebraically. Indicator Gram matrices have limit
b(x)b(z)/b_C within one synchronous level and zero between levels, giving
the stated rank-one strong asymptotic blocks. Their eigenvalues approach
one along an escaping spine. The compactness/strong-stability criterion
therefore excludes escape precisely and does not exclude other cycles.

At every fixed time n, P^n(P*)^n is the diagonal multiplier d_n(t).
The uniform lower bound on every inverse state gives
d_n(t)>=1-n/(3((2/3)^n(t+1)-1)+1) when the denominator bound is positive.
It follows that d_n(t) tends to one at high targets, yielding essential
norm one. Section 7's two physical-truncation norms follow separately by
taking adjoints and using normalized point indicators at targets t
sufficiently large relative to the fixed M,n. This also permits arbitrary
finite schedules n=n(M); it does not exchange these limits with the
strong asymptotic limit.

No compactness estimate at infinite time has been proved by the packet.
Finite-power and finite-truncation operator norms cannot supply that
missing estimate, even under eventual periodicity of all ordinary orbits.
