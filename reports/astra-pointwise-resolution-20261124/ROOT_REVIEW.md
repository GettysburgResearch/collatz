# Coordinator review of the pointwise continuation

**Result:** all 18 public declarations in the three new Std-only Lean modules passed Lean 4.34.1 with warnings as errors. Complete printed axiom dependencies contain only propext, Classical.choice and Quot.sound. Normal and optimized exact controls passed with identical output. Universal Collatz convergence remains unproved.

This review covers the new packet, whose final hashes are in [SOURCE_HASHES.json](SOURCE_HASHES.json), and the execution in [kernel/CHECKS.json](kernel/CHECKS.json). The infinite theorems below are written mathematics. Imported results have the exact source qualifications in [SOURCES.json](../../research/astra-pointwise-resolution-20261124/SOURCES.json). No prior Lean packet was rebuilt.

## Ordinary paired fibers

I reconstructed the cross-carry identity for the actual shortcut iterates of x and 9x+2. If its determinant vanishes, the ternary valuation of the carry on the right is zero, including when its odd count is zero. The left carry is a ternary unit as soon as its odd count is positive. Thus the exponents differ by exactly two and the actual endpoints agree.

When the endpoints differ, the nonzero determinant is divisible by every common halving divisor. Its carry bound is uniform in the starting integer. The odd-count levels at joint-even stretches increase strictly. Summing their bounds gives h≤S²+6S+4, including the initial and final stretches. The integer marked-fiber theorem is a genuine consequence on each ordinary member; no distribution of marked records is assumed. The real logarithmic formulation and diagonal limsup are written deductions.

For the diagonal, zero right odd inputs would require a left intercept of two with two odd inputs, whose minimum is five. Exactly one right odd input forces three on the left. The binary equation gives positions (1,2,3;5), now also kernel-checked. The all-integer cylinder x=46 mod64 and the residual cylinder k=12 mod64 are kept distinct. The ordinary six-step identity reaches 243v+47. The primitive-root order modulo 243 supplies the infinite target-specific clock progression.

The bounded-clock generation bound is written. At a fixed clock budget there are finitely many accidental solutions to nonidentity affine return equations. Above those exceptions, equality of slopes forces equal clocks and equal odd counts. Split each such return into positive first returns. Their prefix code omits x=46 mod64, so its binary mass is at most 63/64. The outgoing quotient has odd slope, preserving uniformity of unexposed binary tails. On each dyadic size band, at least order log(X)/H such pieces are needed to reach a fixed small root. Tiling the grid at depth at most log₂X gives the power saving. This does not control unbounded-clock programs.

[Independent transfer review](../../research/astra-pointwise-resolution-20261124/arithmetic/REVIEW_TRANSFER.md)

## Common first landings

The residual cylinder and two-gap inverse equation are proved for ordinary natural numbers. Reduction modulo three and nine ensures both inverse odd steps are integral and their intermediate state is a unit; odd parents give the exact valuations. The same original parameter supplies both arms.

The real correction in the arbitrary-depth route is uniformly O(1/y): each inverse exponent is at least two and y_j−1 grows by at least a factor 4/3. Continued-fraction grids for log₂3/d steer the total clock while localizing the actual parameter. A fixed outgoing parameter and an allowed odd depth determine the incoming y, giving the claimed multiplicity bound. The initial six states and every intervening odd state stand above the floor, so the result concerns first landing, including at periodic targets.

For the unconditional count I checked the residue-depth recurrence, the rounded fifth-power weight inequalities, the minimum mass above one, and the stopping-cut argument. The initial unit child is chosen above a uniform multiple of max(M,Q), so the entire outward tree is strictly increasing. Its unique forward path prevents collisions between different cut words, even at differing depths. A leaf's probability is bounded by its multiplier to the power −2/5, giving the number of leaves. This argument uses no analytic predecessor theorem. Lean certifies the finite weight/cut computation; the infinite stopping-tree inference is a written proof.

The linear count imports precisely paper 12's Theorem 14 with Lemma 13's written assumptions. Its target and scale quantifiers were checked in the primary text. The joint-target density classification additionally imports the pinned binary coalescence and fixed-target density existence. The witness (29,263) has incomparable complete forward traces despite common eventual convergence; the kernel checks both traces. Its zero limiting joint mass uses the source-qualified classification.

[Independent renewal review](../../research/astra-pointwise-resolution-20261124/transfer/REVIEW_RENEWAL.md)

## Complete denominators and fixed-source words

I checked Corvaja–Zannier's primary Theorem 1 and equation (2.30). The relevant gcd bound has exceptional translated subtori, not just subgroups. Negating the local negative-log terms makes them nonnegative, so discarding places in S is valid. The polynomials are fixed, coprime after removing their symbolic gcd, and not both zero at the origin. Constant-polynomial cases are handled directly.

The affine commutator is a unit away from six under every allowed dictionary move in both coordinates. The carry identity therefore retains every prime power in the cancellation comparison. Unimodular clock vectors exclude each fixed translated subtorus along irrational limiting density. Homogenized cyclotomic factors above the primitive factor have no positive real roots and give the claimed logarithmic fractions. The primary Lagarias Lemma 2.2(1) controls the primitive two-power difference.

For arbitrary densities, on a translate containing a dictionary point the two valuations of its rational positive constant are coprime. In a complementary monomial coordinate the primitive-clock binomial is irreducible: the constant coefficient of a rational factor would force its degree to be divisible by the full binomial degree. Its positive root cannot annihilate the positive suffix sum. A fixed Laurent-polynomial resultant bounds the numerical gcd on each exceptional translate. This proves the lower fraction 1/g; it does not preserve the exact higher-factor cancellation at rational limiting slopes. The explicit specialized cancellation example illustrates that limitation.

The mechanical-window argument uses distinct ordinary states and matching parity windows, not a fresh random word law. The initial run and first occurrence of the other member remain at polynomial height in the fixed starting value. For a primitive cycle, each segment contains distinct inputs even if it crosses the original mark; the two-log estimate then bounds log(minimum) by O(log period).

The fixed ancestor with initial bits 0011 lies in the same hypothetical escaping component and has no nontrivial positive Nielsen desubstitution of any longer prefix. This correctly limits a proposed universal seed-complexity upper bound at arbitrary marks. It does not exclude a later-mark argument, and the packet makes no such claim.

## Execution and publication scope

The aggregate execution compiled six public theorems per module. The source bytes and the appended audit copies were stable. Exact controls checked 276 dictionaries, 4,416 affine/valuation instances, 552 exact seed-10 denominators, 4,953 physical segments and 40 exceptional specializations; the renewal control checked 1,458 ternary units, 8,748 complete two-arm routes and 37,908 physical odd steps, plus all four cut minima.

The late refresh found changed PR200 and PR201 heads and new PR203. Their new interfaces were inspected, without rebuilding them, before publication; [LATEST_CONNECTIONS.md](../../research/astra-pointwise-resolution-20261124/LATEST_CONNECTIONS.md) records the overlaps and remaining fixed-target filters. They do not close the directed basin implication. Complete-checkout integrity and actual remote publication are recorded separately; those checks are not mathematical proof.
