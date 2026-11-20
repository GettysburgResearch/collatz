# Publication refresh: stationary regularity, all-time moments, and phase scope

**The global gap remains OPEN.** The refreshed sources do not provide an
absolute bound for the uncovered term in CR3, invalidate the frozen
renewal or phase proofs, or prove universal convergence. They do require
more precise concurrent credit: endpoint-conditioned renewal is also
present in PR168 and PR169, and the advanced PR146 gives a closely related
rank-one phase obstruction with a stronger multiplication-anchor analysis.

This addendum leaves the local proof, checker, and report bytes unchanged.
The fetched refs were checked against these exact heads:

| PR | Full commit SHA | Relevant path and claim identifiers |
|---|---|---|
| 168 | `e4599b32e4b1a955ac9315d46782d4ad6a5db96c` | `research/closure-frontier-20261121/TERNARY_STATIONARY_BOUNDARY.md`, TM1--TM7; `FINITE_CONDUCTOR_RIGIDITY.md`, especially FC4--FC5; `CLOSING_ATTEMPTS.md` |
| 169 | `6cb9bfdc828f91576066b0e4a099d47d8144e915` | `research/certificate-renewal-20261121/MOMENT_QUANTILES.md`, MQ1--MQ5 and BC/NC/QC/PC; `FIXED_ENDPOINT_SUMMABILITY.md`, ES1--ES4; `FULL_THEOREM_ATTEMPT.md`, sections 2--3 |
| 146 | `66970775e4bdc945a68308e37a8eb028ebde42d2` | `research/upper-bit-mergers/FIVE_RETURN_IN_EVERY_CLASS.md`, sections 1--4 |

## 1. The stationary result preserves the ordinary error, but does not construct it

[PR168 TM1--TM7](https://github.com/GettysburgResearch/collatz/blob/e4599b32e4b1a955ac9315d46782d4ad6a5db96c/research/closure-frontier-20261121/TERNARY_STATIONARY_BOUNDARY.md)
concern the random affine process on the ternary quotients that chooses
`x/2` and `(3x+1)/2` independently with equal probabilities. Its
stationary step densities are `g_s(x)=3^s*pi_s(x mod3^s)`. The elementary
mixing proof and the ordinary weighted-error transfer have different
roles; no successive parities of a fixed integer are replaced by coins.

TM5 proves that the stationary measure has no square-integrable density.
TM6 imports Tao's fine-scale estimate to obtain an `L^1` density and
rapid `L^1` approximation. The latter retains its explicit published
dependency; this comparison did not reprove or independently inspect
that external Fourier theorem. The deductions from the supplied estimate
are sound. In particular, for a supplied bounded ordinary error `e`, TM7
gives, uniformly in the conductor,

\[
\delta_s(e)\le 2^m\delta_H(e)+C_A m^{-A}.
\]

The same error appears on both sides. Taking the ordinary average of the
periodic difference `|g_s-g_m|` requires no equidistribution of `e`.
This supplies a useful conversion when an actual ordinary approximation
already exists. It does not construct an approximation to a component
indicator. TM3 and TM7 would force weighted near-constancy from Boolean
periodic approximations with ordinary mean error
`exp(-c*s^beta)`, but that approximation remains unproved.

[FC4--FC5](https://github.com/GettysburgResearch/collatz/blob/e4599b32e4b1a955ac9315d46782d4ad6a5db96c/research/closure-frontier-20261121/FINITE_CONDUCTOR_RIGIDITY.md)
give a separate finite-source route. With the named Krasikov--Lagarias
predecessor bound and the existing antichain amplification, every
nonconstant actual Boolean invariant requires approximation error
`omega(N^(21/25)/log N)` on the specified enlarged ordinary windows.
An actual construction attaining `O(N^(21/25)/log N)` would suffice.
The current prefix-survivor estimate neither reaches that exponent nor
identifies the mismatch set. These are two separate missing steps.

### Conditional observation: positive component density removes the weighted-mass premise

This paragraph is **conditional**, not an additional unconditional
closing result. Assume every nonempty ordinary invariant set has positive
lower natural density. This follows from the source-qualified hypothesis
PD stated in
[the earlier critical note](https://github.com/GettysburgResearch/collatz/blob/5204a6f19beb490fb7c305908188bb3f392abd2e/research/closure-attacks-20261120/critical/CRITICAL_SINGULARITY.md),
section 1; this refresh does not promote that external dependency into
the accepted baseline.

Such a set `K` also has positive lower density among ternary-unit
integers. Indeed discard the inputs divisible by `2^(V+1)`, choosing
fixed `V` so that their density is smaller than half the lower density
of `K`. Keep unit inputs unchanged. For each remaining nonunit write
`n=2^v*m`, with `m` odd and `v<=V`, and send it to `(3m+1)/2`.
This is a ternary unit in the same component, at most `2n`, and each
image has at most `V+2` preimages under this rule.

The support argument in TM5 needs only `L^1`, before its later squaring
step: stationarity gives `g(x)>=g(2x)/2`, and multiplication by two is
ergodic on ternary units. Hence TM6's `g` is positive almost everywhere
on those units. If `K` intersected with the ternary units has lower
density `eta>0` among all positive integers, choose
`a>0` so that the Haar measure of unit points with `g<a` is less than
`eta/4`. The convergence `g_s -> g` in `L^1` makes the Haar measure of
unit points with `g_s<a/2` less than `eta/2` for all sufficiently large
`s`. The latter is a periodic set, so its ordinary density is exactly
its Haar measure. Consequently

\[
\liminf_{X\to\infty}\frac1X\sum_{n\le X}g_s(n)1_K(n)
\ge a\eta/4>0
\]

uniformly for those conductors. No equidistribution of `K` is assumed.
Applied to both fibers of a nonconstant invariant, this removes TM7's
separate weighted-mass premise under PD. It still supplies no periodic
approximation and no bound on the actual uncovered five-defect energy.

## 2. The all-time moment theorem has a different endpoint weight

[PR169 ES3](https://github.com/GettysburgResearch/collatz/blob/6cb9bfdc828f91576066b0e4a099d47d8144e915/research/certificate-renewal-20261121/FIXED_ENDPOINT_SUMMABILITY.md)
is an unconditional global positive estimate, including hypothetical
nontrivial cycles. For one original odd source `n`, write
`n_q=U^q(n)`, `n_q=n*J_q*I_q`, and

\[
V_q=(J_q/n_q)^4=1/(n^4I_q^4).
\]

Its exact telescope and the sharp rational bound on the decrement give

\[
\sum_{q\ge0}\frac{J_q(n)^4}{n_q^5}
\le\frac{256}{175n^4},\qquad
\sum_{q\ge1,w}\frac{J_w^4}{r_w^5}<\frac{512}{175}.
\]

The argument handles repeated cycle visits through contracting Jacobian
weights. It does not exclude those cycles. On a hypothetical nonperiodic
orbit, the imported simple-path occupancy bound already permits the
correction product `I_q` to have a finite limit. Thus `V_q` can retain
a positive limit while the telescope remains summable; no vanishing
residual follows.

There are three endpoint powers between this summand and the arithmetic
moment `P_q=sum_w J_w^4/r_w^2`. ES4 removes the entire region `r_w<=q`
from the positive-average closing target, because its cumulative
contribution is `o(N^3)`. What remains is explicitly OPEN:

\[
\liminf_{N\to\infty}N^{-59/19}
\sum_{q\le N}\sum_{r_w>q}\frac{J_w^4}{r_w^2}=0.
\]

MQ1--MQ5 correctly retain one fixed hypothetical nonperiodic source and
give the weaker sufficient criteria BC, NC, QC, and PC. None is proved
for the actual moment sequence. Even proving one would leave nontrivial
positive cycles to exclude separately. The normalized word law behind
this fourth-Jacobian moment has exponent probabilities `15/16^a`, not
the stationary Syracuse law `2^(-a)` used by TM6. No comparison theorem
transfers the latter regularity to this moment or to our actual invariant
defect. Neither the fifth-denominator estimate nor the conditional moment
criteria supply an absolute estimate for CR3's source-weighted remainder.

## 3. The advanced PR146 strengthens localization and qualifies phase novelty

[PR146 sections 1--3](https://github.com/GettysburgResearch/collatz/blob/66970775e4bdc945a68308e37a8eb028ebde42d2/research/upper-bit-mergers/FIVE_RETURN_IN_EVERY_CLASS.md)
construct ordinary proportional returns inside every prescribed
arithmetic progression, including simultaneous shifted blocks, with
bounded multiplicative source enlargement for each fixed pattern.
If a failed five comparison exists, it can therefore be replicated in
every progression. Independent five-closure on any entire progression
would settle the global criterion. The construction does not assert
closure of that progression, and descent on a refined subprogression
does not include every fixed supplied source. Its quantitative failed
block count has exponent `1/log_2(2^23/9)`, far below `21/25`; it gives
no contradiction to our still unbounded `Q_(21/25)`.

Section 4 now analyzes the same stopping grade as TP1--TP2 and uses the
same PR157 rank-one family to force unbounded negative five phase.
Our rank-one application must therefore be described as a concurrent
reconstruction/application of that mechanism, with this advanced source
credited. No invention of the invariant or first finite-anchor
obstruction is claimed.

There is also a precise architectural distinction. PR146 permits
**nonnative multiplication links** at certified anchors. With anchors
1 and 7 and both orientations, it proves that, when `5q` converges, the
minimum number of such links is `|2D(q)-5|`. The construction uses the
two supplied hitting paths and has no uniform cost even on rank-one
antecedents. Our TP1 preserves phase through ordinary affine paths,
including reverse ordinary edges, and TP2 treats finite terminal bases
for those proportional rewrites. The multiplication links change the
adjusted phase and fall outside TP1. They are a legitimate larger
architecture, not a contradiction or a target certificate obtained
from the antecedent certificate alone.

## 4. Renewal attribution and the remaining contribution

PR168 FR4 and PR169 FW5 also use joint endpoint congruences to bound
positive inverse kernels. Their selected domains have coefficients
`903/1000` and `249/250`, respectively, at exponent `21/25`; their
cutoffs and source domains differ from CR3. The shared four-step row is
a concurrent reconstruction. These methods and that row must not be
advertised as new relative to the refreshed heads.

Our remaining explicit energy contribution is the complete inverse
kernel for the unbounded safe carry sublanguage `b>=r+2`, coupled with
the old ladder and shared short row. Its source domain is different
from the two refreshed selected domains. CR3 retains

\[
E_{21/25}(X)\le Q_{21/25}(X)
+\frac{248549}{248775}E_{21/25}(X/6),
\qquad
E_1(X)\le Q_1(X)+\frac45E_1(X/6).
\]

There is still no absolute bound for either remainder. PR168 FR5's
superunit column on an explicit ordinary endpoint family also shows
why blindly adjoining every valid balanced return cannot establish
uniform contraction in the same weights. The full language and domain
comparison is recorded in
[the certificate refresh](../certificates/LATEST_COMPARISON.md).

The source arguments identified above were reconstructed at the written
proof level. This refresh does not claim a new run of their checkers,
their external computational certificates, or any Lean supplement.
No correction to the frozen CR1--CR3 or TP1--TP2 statements is indicated.
