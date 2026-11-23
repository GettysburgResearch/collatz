# Independent review: minimum flux, arithmetic tails, and integral repair

Reviewer: the separate `collision_core` research agent.
Date: 2026-11-23.

## Exact reviewed bytes and scope

The review binds the following files, rather than an unfrozen branch name:

| File | SHA256 |
|---|---|
| `research/whole-source-20261123/BOUNDARY_DESCENT.md` | `4b48bb2cff2c80ebe59c5b363c1e1c90c52395ddf0069284e44f246d8a465738` |
| `research/whole-source-20261123/ARITHMETIC_MINIMUM.md` | `931dfa3e20e3a77093f011d39d108996d63c7459569cacbd9b751d5689e13343` |

I independently reconstructed all the new written deductions in these two
files. I checked the scope of the quoted equal-depth-injective count in the
pinned `ORBIT_MELLIN.md`, rather than rerunning its historical proof. The
canonical flow, whole-path construction, coherent scale, and prior
fixed-reweighting dimension theorem remain precisely the qualified pinned
inputs stated by the authors. This review is not a claim that those inputs
were newly formalized. Formal replay of the new arithmetic module is reported
separately by its owner.

**Verdict: no mathematical gap found in the new claims at these exact bytes.
Neither file establishes escape exclusion.** Their first unproved closing
steps remain explicit and are correctly separated from their positive results.

## 1. Minimum partition and the two Green source equations

A two-sided ordinary path has pairwise distinct positive integer states.
Each bounded interval therefore contains only finitely many path entries.
Together with `chi(n)>=n/b`, this proves coherent-scale divergence at both
ends, not just in the deterministic forward direction. The minimum is attained
at a finite clock. Two distinct clocks cannot tie, because the exact scale
ratio is `3^h/2^A` with positive `h,A`.

The conditional minimum probability in (4) retains its ordinary root and
the actual inverse kernel. The deterministic future supplies membership in
`V`; the past supplies exactly the event defining `b_*`. The countable
minimum events are disjoint and exhaustive, so summing their probabilities
gives `sum sigma=C` without subtracting infinite level masses.

The pressure maximum is a coherent-scale minimum: the product `chi(n)r(n)`
is constant across every actual edge, hence on the eventual-meeting
component, by the two displayed edge laws. Thus the PR182 pressure maximum
really has `b_*=1`; a distinct ordinary state at the same component level
cannot occur on the same path and causes no uniqueness problem.

The new Green identity has the correct source sign. At a fixed vertex `n`,
the event that its path minimum lies at or before its clock is the disjoint
union over minimum sources whose deterministic future reaches `n`.
Therefore

`nu_+(n)=sum_(j>=0) (L^j sigma)(n)`.

Every term is nonnegative and the total is bounded by `nu(n)`. Shifting the
sum yields `L nu_+=nu_+-sigma`. Since `L nu=nu`, subtraction then gives
`L nu_- - nu_-=sigma`. Neither difference subtracts infinite vertex values.
Finally `nu_-(q_j)<=C*Pi(tau>j)`, while `nu(q_j)->C`, proves both limits
in (5b). The note correctly does not identify the harmonic `nu` itself with
a positive-source Green potential.

## 2. Occupation, progression bounds, and endpoint constants

For a whole path, `U^h(Q_j)=Q_(j+h)` is injective in `j` for every fixed
`h`. This satisfies the exact stated hypothesis of T-A3-401; invariance or
a one-sided initial source is not required by that theorem. Tonelli over
the component levels gives the occupation identity (6), hence
`W(X)<=4 X^theta`, with `theta=39/40`. Mellin integration then proves
both (8) bounds, including the component-floor factor. The infinite total
unweighted occupation mass is not treated as a probability measure.

I independently checked the arithmetic-progression split and its constants.
The trivial progression bound is `2X/Q` for `X>=Q`; intersecting it with
`4X^theta` puts the crossover at

`X_*=(2Q)^(1/(1-theta))`.

For `theta<s<1`, the first integral contributes at most

`[2s/(Q(1-s))] X_*^(1-s)`

and the second equals

`[4s/(s-theta)] X_*^(theta-s)`.

Both have the common factor
`4s*2^(-beta_s)*Q^(-beta_s)`, with
`beta_s=(s-theta)/(1-theta)`, giving exactly (10)--(11).
At `s=1`, the first term is

`2*(log2+theta*log Q)/((1-theta)*Q)`

and the second is `2/((1-theta)*Q)`, giving precisely (12).
The cutoff `n>=Q` is retained and is essential at fixed ordinary atoms.

In an unequal positive congruent pair the larger integer is at least `Q`.
Ordering pairs, applying the residue-tail estimate to that larger factor,
and summing the smaller mass gives (13); substituting the endpoint constant
gives (14), including its factor `4S_1`.

The actual change of measure is also exact. Equation (15) has the factor
`C S_s q_j^s/(N v_j)`. One application of the progression bound gives (16)
with one density factor, not two. At positive inverse depth, actual inverse
supports are unbounded and their pointwise density equals
`C S_s n^s/(N v_(r+j))`; its supremum is indeed infinite. The comparison
therefore cannot supply a stationary-time upper bound by omitting that norm.
For a fixed modulus, the critical running-height bound forces the displayed
time-law comparison factor to diverge, since `s>39/40>theta_0`.

The first unsupported step in this lane is the stated nonuniform bilinear
or arithmetic transport estimate for the actual late time law. Positive
information dimension of a minimum-conditioned earlier boundary is not
silently asserted to control residues on its deterministic future.

## 3. Full ordinary maximum and same-clock repair

The enlarged pressure maximum is a genuinely new optimization over all
positive odd sources in the component. A multiple of three can occur only
as an initial leaf before its unit image, so the positive product extends
without changing the edge identity. The bound `r(n)<=1/n` proves attainment,
and choosing the least maximizing integer justifies the later tie-breaking
comparison. The new maximum is not identified with the old unit maximum or
with the least nonconvergent integer.

The forward and incoming strict coefficient inequalities follow from the
same maximum and the exact edge balance. For a maximizing source congruent
to `2 mod3`, the positive odd gap-one ancestor is now inside the enlarged
domain and has `3/2` times its weight. This correctly excludes that class.
Together with the forward gap-one condition, the residue alternatives are
exactly `3,7 mod12`. The possible maximizing ternary leaf is retained.

At a future endpoint, comparing any actual incoming coefficient gives (8).
Equality forces both the same odd length and the same total clock; the least
maximizer then makes the actual carry maximal, with the sign in (9) correct.

For a positive-gap word of length `l` and total clock `B`, the prefix totals
satisfy `j<=s_j<=B-l+j`. Applying these bounds term by term yields the stated
carry minimum and maximum. Subtraction gives exactly

`2*(2^(B-l)-1)*(3^(l-1)-2^(l-1))`.

Composing an unchanged prefix, the edited same-clock window, and an unchanged
suffix gives

`n-m = 2^A_i*(C-D)/3^(i+l)`.

The suffix cancels because its affine slope is nonzero. Integrality and
coprimality force divisibility of `C-D` by `3^(i+l)`, and both carries are
odd, giving the additional factor two. Distinct sources make the difference
nonzero. These observations prove (13) and its strict consequence (14).

Multiplying (14) by `2^(i+l)`, using `A_i>=i`, and applying the actual
prefix coefficient inequality gives

`3^(i+1)*2^(i+l) < 2^(B+i) <= 2^(B+A_i) < 3^(i+l)`.

Cancellation proves (16), and taking logarithms gives the exact span bound
(17). No alphabet cutoff, bounded edited gap, or bounded total depth entered
this argument. The note correctly distinguishes an excluded bounded-span
repair from a sparse but nonlocal edit, and from changes of clock, length,
or endpoint.

The first unsupported step is construction of a positive integral
pressure-improving comparison for every hypothetical maximum. The new
restrictions on such a construction are not a proof that it exists.

## 4. Review correction

The arithmetic author removed the word “equivalent” from the formal-scope
description of the weaker integer corollary `i+1<l`. It is a necessary
consequence of (16), not an equivalence. The arithmetic hash above is the
corrected final version. No substantive proof correction was required.
