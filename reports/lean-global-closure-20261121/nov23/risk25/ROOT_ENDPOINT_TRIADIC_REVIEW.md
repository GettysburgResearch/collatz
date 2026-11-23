# Root review of the carry transfer and source-aware construction

Date: 2026-11-23. Reviewer: coordinating agent. This is an independent
reconstruction of the statements below, with finite execution recorded
separately. The verdict does not extend to later source bytes or to the
whole external theorem corpus.

## Critical carry transfer

Source: `research/lean-global-closure-20261121/risk25/CRITICAL_CARRY_TRANSFER.md`,
SHA256 `cc45bcd43a450405b7b7cd12dd67fab45d43ac32caac3d875f5fdc5dca04b03d`.

**VERIFIED** for the elementary finite word theorems and full-source
transfer inequality. **VERIFIED, SOURCE-QUALIFIED** for the stationary
distortion alternative, conditional on the explicitly pinned PR180
stationary theorem and PR185 flow construction. Neither is an actual
collision upper bound or an escape exclusion.

I reconstructed the following steps:

1. Rotating a zero-sum centered composition after a maximum makes every
   centered prefix nonpositive. Counting the union of at most m rotation
   images gives the reference-family lower bound, including periodic
   words. This operation is never applied to the actual time law.
2. At fixed total A, the complete carry decodes the shortcut parity word
   recursively. The endpoint residue plus the complete carry quotient
   determine that carry. The prefix bound gives at most 1+floor(m/3)
   possible quotients for the balanced family.
3. The binomial count at A=floor(m log_2 3) has size bounded below by
   c exp(m Phi)/sqrt(m). Combining it with the rotation and quotient
   losses gives the claimed m^(5/2) factor. The strip argument adds
   only exp(o(m)) for a sublinear integer slack schedule.
4. The residue class in (10) includes the final endpoint's oddness,
   modulo 2^(A+1), and has positive representatives coprime to three.
   It supplies a finite ordinary realization for each reference word;
   the initial integer is allowed to change. It is not one all-time
   ordinary source.
5. In Theorem 3 all occurrences of a word are combined before squaring.
   Fiberwise Cauchy bounds the retained collision by R times the word
   energy. The omitted measure has Euclidean norm at most its full
   mass tau. The triangle inequality retains all cross terms. Formula
   (15) includes off-ray mass, the first m positions, and every rejected
   word, with no normalization or profile cutoff.
6. Substituting the pinned strict stationary lower bound into the same
   full-mass inequality yields exactly the two alternatives in (20).
   The claimed exponent is epsilon*m, with the factor 1/4 after
   squaring. Taking the original time limit before the resolution
   limit is explicit; no convergence rate is supplied or used.

One clarification is retained here and in the packet overview: the
reference laws depend on m and are not claimed to form a projectively
consistent stationary process. The theorem needs only the declared
finite families. The same-source comparison for the actual law remains
the unproved quantity, including its high-profile mass.

## Source-aware triadic construction

Source: `research/lean-global-closure-20261121/risk25/SOURCE_AWARE_TRIADIC_CONSTRUCTION.md`,
SHA256 `ae7f16ca337ed1505f66248eb82ce21e6ae5b20b2bebf305add62a7f723801ad`.

**VERIFIED** as written finite algebra and the stated all-time
consequence. The universal successful-witness construction is **OPEN**.

The finite binomial identity is exact for ordinary n; the even-index
recurrence follows by expanding (2z+z^2)^k. I checked the coefficients
of the three displayed reduced odd equations and their elimination,
including a_1=3, a_3=32/9 and a_5=-16/3. A finite Pascal change of
basis is unimodular, so it cannot close an unprescribed graph endpoint
by itself. The final text correctly distinguishes a rational cycle
solution from a triadic solution.

For the source-aware anchors, I checked both carry recursions and the
ordinary affine identity. The -x-1 numerator has no factor three after
both parities have appeared. The reflection updates in (11) have the
claimed signs and cancel on each alternating pair. A polynomial in
Z[X] calibrated at 1 and 2 automatically has the correct parity and
the required congruences modulo three.

For calibrated rules, the two carries modulo three are the powers of
two at the last active positions. Their difference in position is the
final constant-run length. This proves the odd/even run criterion.
Direct expansion gives the two carry sums for 011 and 100, each a unit
modulo three. These calculations hold regardless of the earlier
prefix and can be applied to rules selected separately at each clock.

For the all-time consequence, a positive ordinary orbit cannot remain
even forever by integrality. On an all-odd tail, v_2(x+1) decreases by
one per step, which is also impossible. If both reset blocks stop
occurring, every late constant run has length one. At consecutive odd
states in that alternating tail, u_next-1=(3/4)(u-1); a nonzero positive
integer difference cannot contract forever. Hence the orbit reaches
one. A hypothetical source failing to reach one therefore has
infinitely many reset blocks, with complementary odd counts tending
to infinity. This does not rule out a favorable intervening subsequence.

## Lean execution and precise formal scope

The final module SHA256 is
`3a4b7e06a852348e9d1537c467dfabb4a33f104f5109292a6fbced2584f6f8c5`.
I read the module, copied those bytes into the publication worktree and
independently executed Lean 4.34.1. The command exited zero, with empty
stderr. All twelve printed key axiom inventories contain only
`propext` and `Quot.sound`. See `root-lean-receipt.json` for the exact
binary, source hash, command and output; the author's separate receipt
lists all 26 theorem declarations.

The module proves the finite numerator-unit arithmetic and the actual
integer iteration's affine identity. In particular its actual-source
anchor theorem does not assume the affine identity as an unexplained
premise. It does not formalize Mahler theory, polynomial evaluation,
reduced rational denominators, the all-time run argument, the analytic
collision argument, or universal triadic witness existence. The written
interpretations of its finite arithmetic are reviewed separately above.

## Higher-digit interpolation extension

Source: `research/lean-global-closure-20261121/risk25/HIGHER_DIGIT_INTERPOLATION.md`,
SHA256 `efb8c9ec2ebca67fd1d9d9f8381bfe4e5e6e96c4b3ef78c6c6e98ff00a74d79a`.

**VERIFIED as written construction and exact value-lattice classification.**
This extension is not part of the Lean formalization.

Over R=Z[1/3], the monic factors X-1 and X-2 give the exact calibrated
value coset 3-x+gR, with g the prime-to-three part of (x-1)(x-2).
For the integer-valued refinement I checked the choice d=3^j<=x<3d,
the factorial valuation (d-1)/2, and the coefficient-of-Z^d proof that
binom(x,d) is a unit modulo three. The resulting B_j(x) is divisible
by g and prime to three, hence gcd((x-1)(x-2),B_j(x))=g. Ordinary
Bezout coefficients then realize every integer in the claimed coset,
with even corrections on every integer input.

Clearing the terminal expression's denominator gives exactly the
modulus 2^K g in (5), since that modulus is prime to three. The
general Newton interpolant at degree x evaluates to an arbitrary
prescribed terminal z while vanishing at one and two. Its correction
is in 2R precisely for the required terminal parity. This proves both
directions of the original complementary-residue congruence (7),
without gaining a bound on its smallest numerator.

I checked the displayed actual prefix 6,3,5,8, its carries C=10,D=1,
and the three terminal values 65,-19,-1. They pull back to initial
integers 173,-51,-3, respectively. Their paid horizons are 100,82,46.
The smaller calibrated coefficient ring gives the residue 61 modulo
112; the full integer-valued class gives 13 modulo 16. These exact
calculations exhibit real denominator cancellation and its remaining
height cost. They are one supplied source control, not an all-source
existence theorem or an exclusion of future success.

## Late fixed-clock extension

Source: `research/lean-global-closure-20261121/risk25/FIXED_CLOCK_EXTENSION.md`,
SHA256 `ac6006a24fbafe5fc7fd2be9817e0c029e631252d2a9f85a26c864b389fd8fca`.

**VERIFIED as a source-qualified consumer of the explicitly pinned
PR180 product joining.** This verdict checks the deduction, not all
historical analytic inputs of that source.

Each fixed ternary endpoint cylinder is exactly a function of the
preceding gap block, apart from finitely many initial labels whose
empirical proportion vanishes. Pushing the stipulated joint law through
this function gives the product law for endpoint, rotation phase and
each fixed clock modulus. A finite collection of clock moduli is a
factor of their least common multiple, so cylinder consistency gives
the profinite extension without a moving-modulus rate.

For each fixed modulus h, joint endpoint collision is Col(rho)/h.
Conditioning on a clock class gives back rho. At the word level the
uniform reference has L*h atoms and the actual atom mass is p_w/h;
its energy is exactly (L*h)*sum_(w,c)(p_w/h)^2=L*sum_w p_w^2.
The omitted mass is also unchanged. Thus this new clock factor cannot
be used as an unproved gain in the original J/tau transfer.

The finite scripted-word discussion preserves its source payment and
does not assert an actual escaping stationary counterexample. The
source-qualified tail density result is not promoted to positive time
frequency or to an identification of the complete ordinary carry.
