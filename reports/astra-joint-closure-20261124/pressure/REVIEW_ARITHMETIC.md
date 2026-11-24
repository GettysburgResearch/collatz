# Independent cross-review of the arithmetic lane

**VERIFIED at the written theorem level** for the local rational-cycle
construction in
[the arithmetic README](../../../research/astra-joint-closure-20261124/arithmetic/README.md),
SHA-256 `a568b6e5fb765968b51ca18756c87c8ca651ff0729cac972985ba6d6169139f7`.
The phase constrained modulo M is integral at primes of M; a former
wording that could assert ordinary integrality was corrected before
this verdict. Every constructed denominator contains E.

* Over the finite residues prime to six, both elementary affine maps
  are permutations. Comparing their two orders of composition gives
  a translation by the unit 1/4. Their powers thus realize the whole
  additive translation group. Finite semigroup inverses allow a
  bounded correction for each prefix permutation and fixed suffix.
  A prescribed slope 2^(-t) already belongs to this group.
* The lift of each prime-power modulus by the exact valuation of
  2^t-1 prevents division of congruences from losing precision.
  Equality of return maps modulo the lifted modulus pins both
  intercept and slope (evaluation at zero and one). At each prime
  dividing E the intercept is a unit while the slope defect vanishes
  to the prescribed order. At primes dividing J the phase is integral
  and the full denominator contains J, so every rotated numerator
  includes the requested common factor.
* The terminal ones reset all inputs integral at three to -1 at the
  requested precision; common halving reaches the desired unit using
  the powers of two. Inserting the two identity permutations before
  this suffix preserves both that action and the other finite tests.
  Irrationality of log(2)/log(3/2) gives dense signed displacements
  using nonnegative run lengths. Compactness allows a common finite
  bound even though the two run lengths vary with the middle word.
* The positive fixed point and each of its rational rotations have
  denominator prime to six. Consecutive displayed phase values being
  2-integral forces the indicated input parity, so all rotations
  follow the actual rational dynamics. The least phase is odd, and
  its own factor in the telescoping coefficient product gives the
  claimed common lower height bound.
* The free middle encoding is injective at each fixed middle length.
  Total imprimitive words cost at most a polynomial times 2^(n/2),
  strictly below the binomial exponential rate. Forgetting the marked
  phase costs at most the period. The upper rate follows by counting
  all near-critical binomial rows at bounded clock offsets. The
  simultaneous finite-place diagonal is valid because the forced
  outside denominator prime may vary, while every fixed precision
  remains among the growing list of local tests.
* For a fixed ordinary source, reducing the return numerator modulo
  its odd full denominator gives 2^h times the endpoint displacement.
  This proves the gcd identity. Distinct-orbit reciprocal summability
  is an inherited input for the lower height asymptotic, and the
  elimination of small denominators invokes the explicitly cited
  PR 195 upper count. I checked the latter count's statement at the
  pinned source, without auditing its proof here. Neither consequence
  controls the word-dependent prime divisibility on an actual infinite
  orbit.

**Executed checks.** I independently ran the optimized-mode Python
rational orbit replay: primitive period 184, 116 odd inputs, cancelled
gcd 5, source residue 157 mod 180 and the stated denominator and
minimum. I also independently compiled
[FiniteCycleTests.lean](../../../research/astra-joint-closure-20261124/arithmetic/FiniteCycleTests.lean),
SHA-256 `6d59babca177a85ead06fcfcd732b4e9715296d0521284b3b9f71d858e0ee0bc`,
with Lean 4.34.1 and the supplied built Mathlib. The four declarations
reported only `propext` and, for two declarations, `Quot.sound`.
These formal checks cover the finite algebraic implications; the
group, local lifting, counting, and global scope above were reviewed
as written mathematics.
