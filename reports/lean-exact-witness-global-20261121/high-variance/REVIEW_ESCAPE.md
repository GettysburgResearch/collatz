# Independent reconstruction of the pressure and ordinary-atom argument

**Verdict: VERIFIED at the written-argument scope stated below.**

Reviewer: the separate `global_witness` research lane in this session.
This review is independent reconstruction, not an external peer-review
endorsement and not a Lean formalization of the analytic statements.

Reviewed file:

`research/lean-exact-witness-global-20261121/HIGH_VARIANCE_ESCAPE.md`

Final SHA256:

`d47a77884d979d99a0580d6d34f1f8ebc1e2e62a92fa3833f8fd3ce06f080cfc`

The review covers the elementary positive-product reconstruction, HE-P1
through HE-P6, HE1--HE29 including HE24a--HE24e, and their stated
nonclosure boundaries. It does not re-audit the entire cited canonical
construction, the external analytic/formal source chains, or the proofs
of the literature classifications discussed in Section 7. None of those
external statements is needed for the newly reconstructed deductions.

## 1. Actual-orbit counting and positive product

The length-r gap cylinder includes the endpoint odd bit, hence has one
odd residue modulo `2^(A+1)`. For `A<=m` and `2^m<=X`, its population
below X is at most `X/2^(A+1)+1 <= (3/2)X 2^(-A)`. The number of words
with total A is `binomial(A-1,r-1)`.

The inserted generating-function factor `z=4/5` gives precisely
`rho^3=3125/3456`. For the high-total lane, `A>=floor(5r/3)+1` is
strictly greater than `5r/3`. The physical affine remainder is bounded
by `(3/2)^r-1`, so the endpoint bound and the count of distinct odd
endpoints are valid. Injectivity of `U^r` on the one stipulated escaping
orbit is the necessary point; it is not being assumed for an arbitrary
set of ordinary sources.

I checked the numerical margin as an exact integer inequality:
`8*3125^24 < 3456^24`. Together with the floor error in
`r=floor((3/5)log_2 X)`, this proves the displayed
`N_S(X)<=4X^(39/40)` bound. The r=0 case is harmless.

Tonelli gives `sum_(n in S)1/n <= 4/(1-39/40)=160`. The actual orbit
has no repeated odd states. Therefore its product of
`lambda(n)=1/(1+1/(3n))` is at least `exp(-160/3)>0`, uniformly over
such ordinary orbits. This argument uses no predecessor-population,
canonical-envelope, mixing, or random-parity premise.

## 2. Haar normalization and the pressure gap

For normalized Haar measure on `Z_3^units`, the injection
`Phi_e(y)=(3y+1)/2^e` scales measure by exactly `1/3`. Both its domain
and image use the same normalization by the additive-Haar mass of the
unit group. The image is exactly the clopen legal unit-predecessor
domain for `I_e`.

Changing variables in each nonnegative summand therefore gives

`m P_s = [3^(s-1)/(2^s-1)] m`.

The factor `1/3` is retained. The values at s=1,2 are both one. For
`s=1+u`, `0<u<1`, the displayed auxiliary geometric random variable
computes this same multiplier as `E(Y^u)`, with `E(Y)=1`; strict
concavity proves it is below one. This is a calculation under Haar,
not a claim about the actual integer gap distribution.

For HE-P2, the convex function at positive integer gaps lies above the
extension of its secant through gaps 1 and 2. The inequality remains
valid even when its summed linear coefficients are negative. The exact
ordinary logarithmic telescope and `sum 1/q_i<=H_N` have the correct
signs. The lower bound `c_u>1` follows from the two-point exponential
convexity argument with weighted logarithm zero. The numerical c_1 in
the note agrees with `(9-3 log_2 3)/4`.

## 3. Exact ordinary Green formula

The physical product is

`3^j/2^A = (q/n) Lambda(n,q)`.

At an ordinary root, every legal ternary branch produces an actual
positive odd unit predecessor, whose exact valuation is its branch
label. A nonperiodic root can be reached from a fixed ancestor at only
one odd depth. Hence the Green source sum counts actual sources once
and is bounded by `q^s sum n^(-s)` for s>1. The restriction excluding
periodic roots is necessary and is present.

Along an escaping ray, a fixed original source remains in every future
predecessor sum. The sourcewise bound by `n^(-s)` justifies the stated
dominated-convergence limit over the entire meeting component. The
limit coefficient is positive, and the unchanged-source lower bound
HE17 is retained before every limiting operation.

## 4. Atomic eigenmeasure: both directions and the full cone

The positive-product identity gives exactly

`r(n) = (3/2^a(n)) r(Un)`, with `r(n)=Lambda_infinity(n)/n`.

Every meeting component is closed under legal ordinary unit
predecessors. Reindexing the nonnegative series proves
`mu_(E,s) P_s = mu_(E,s)`, and its total mass is finite for s>1 by
the ordinary `n^(-s)` bound.

For the converse, testing an ordinary atom n leaves exactly one
ordinary odd forward image: `(3n+1)/2^e` is odd integral precisely at
`e=v_2(3n+1)`. The other branch terms are outside the countable ordinary
set carrying the measure. Multiplication around a positive cycle gives
the factor `product 3n/(3n+1)<1`, forcing zero atom mass there and at
every eventual ancestor. Some atom of a nonzero finite measure
concentrated on this countable set must have positive mass, so its
forward orbit is not eventually periodic. On positive integers that
means escape. No nontrivial-cycle exclusion is inferred from this
escape equivalence.

Dividing the atom recurrence by the canonical component recurrence
makes their ratio constant at every edge and hence at a common forward
endpoint. This proves the countable cone decomposition and its extreme
rays. The proof of full topological support is also sound: 2 generates
the units modulo each `3^(k+1)`, and an appropriate positive inverse
exponent supplies a positive atom in any prescribed unit cylinder.
This does not conflict with countable concentration or mutual
singularity of different components.

The ordinary-cylinder bounds HE24b--c follow by summing the tails
`a+j3^k` and `j3^k-a`, respectively. They apply to each canonical
component measure with the stated constants; no uniform bound on an
arbitrary mixture's coefficients is being asserted.

HE24d follows from Tonelli and repeated eigenmeasure invariance. It
correctly shows infinite Green integral despite pointwise finiteness at
every ordinary atom. In HE24e, the fixed-source summand gives exactly

`r(q_k)^s * [(q_k/p) Lambda(p,q_k)]^s = r(p)^s`.

The future vertices are distinct, so these equal positive contributions
already force the divergent integral. This identifies the actual term
an attempted uniform-integrability argument would need to control.

## 5. Negative boundary and the norm obstruction

The cylinder around -1 has normalized unit-Haar mass
`1/(2*3^k)`. Its first k gap-one inverse steps are legal, with weight
`(3/2)^(sk)`. The disjoint annuli have mass `3^(-k-1)`. These facts
prove HE26 and HE27, including divergence at the equality threshold
`sp=log(3)/log(3/2)`.

The note now says **strict operator-norm contraction**, which is the
conclusion supplied at the equality threshold. It does not confuse
strict contraction with a merely nonexpansive bound.

`P_s^N 1` depends only on the unit residue modulo `3^(N+1)`. The
point-evaluation cost is therefore exactly the reciprocal cylinder mass
`2*3^N`; dropping it is not justified. The resulting exponential base
`3/(2^s-1)^(1/s)` exceeds `3/2` and is weaker than the elementary
ordinary-source growth bound. The changing positive integer cylinder
representatives are not treated as one fixed escaping orbit.

## 6. Changes requested and incorporated

The author incorporated three scoped wording fixes before the reviewed
hash was frozen:

- Distinguish concentration on the countable ordinary set from closed
  topological support, especially after proving full support on the
  ternary unit space.
- Describe the norm conclusion as absence of **strict** operator-norm
  contraction.
- State the local tail comparison at a negative **integer** boundary
  point, matching the bound actually proved.

No substantive algebraic correction to HE-P1--HE-P6 was required.

## Remaining uncertainty

The proof does not identify the atomic eigenmeasure with Haar and does
not bound its retained ordinary-source atom by a decaying quantity. It
does not instantiate a thermodynamic or Martin-boundary classification
for this expanding inverse-branch operator. The distinction between
Haar L1 growth and an unidentified topological pressure is retained.

The reviewed packet establishes a new exact escape/eigenmeasure
interface and accompanying estimates. It does not eliminate the
eigenmeasure, exclude all positive cycles, or prove Collatz. No infinite
analytic theorem in this review is claimed to have been checked by
Lean.
