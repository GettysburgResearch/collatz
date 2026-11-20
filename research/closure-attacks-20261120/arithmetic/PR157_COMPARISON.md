# Concurrent PR157 arithmetic comparison

**Status: narrow source comparison, not acceptance of an entire PR.** This
source appeared during the present research pass. The arithmetic proofs
in `CLOCK_HEIGHT.md` and `PRIME_CIRCULATIONS.md` were already frozen, and
their hashes remain unchanged.

Source: PR157, full head
`64361ecca770092d6c8242dc6211e38818af2e50`,
[`research/global-closure-20261120/arithmetic.md`](https://github.com/GettysburgResearch/collatz/blob/64361ecca770092d6c8242dc6211e38818af2e50/research/global-closure-20261120/arithmetic.md),
GA-001--005. The companion `closing-attempts.md` at the same head was
also read. No later revision inherits this inspection.

## What the concurrent arithmetic note proves

GA-001 uses the exact valuation-one clock
\(B(n)=v_2(n+1)-1\). Its finite run is
\(U^j(n)=3^j2^{b+1-j}u-1\) for \(n=2^{b+1}u-1\), and its recharge
identity retains every later step of valuation at least two.

GA-002 counts binary strings with a prescribed number of one-runs and
uses multiplication by an odd number as a permutation modulo \(2^L\).
The union bound produces simultaneous run complexity for a whole finite
valuation-one block. GA-003 chooses source bitlength \(17m\) for a
block of \(m\) states and proves exact legality, dispersion and
logarithmic occupancy of translated intervals. GA-004 enlarges its source
by an explicit odd factor

\[
 Q_m=\prod_{d=1}^{m-1}(3^d-2^d)\prod_{k=1}^m(2k-1).
\]

The actual common-divisor identity
\(\gcd(n_i,n_j)\mid3^{j-i}-2^{j-i}\), together with
\(n_i\equiv-1\pmod{Q_m}\), makes the displayed states pairwise
coprime and removes every small prime in the stated range. GA-005 gives
the exact ordinary edge

\[
 z=2^{m+3}u-3\ \longmapsto\ x=3\cdot2^m u-1,
 \quad v_2(3z+1)=3,
 \quad B(z)=0,
 \quad B(x)=m-1.
\]

Its logarithmic height drop is bounded while its valuation-one recharge
is unbounded. These are genuine finite ordinary controls, with every
source allowed to depend on the requested length.

The counting formula, union-bound argument, ordinary edge identities,
gcd avoidance, and fixed-valuation recharge were independently
reconstructed for this comparison. The external numerical replay was
not rerun here, and no whole-PR mathematical verdict is implied.

## Relation to the present clock-height bounds

There is no conflict. On GA-003's blocks, the number of states is \(m\),
while both source height and mean height are \(\Theta(m)\).
AR-CLOCK-002 therefore gives

\[
 \sup_{|S|\le s}\frac{Y_m(S)}{W_m}
 =O\!\left(\frac{s\log(m+1)}{m}\right).
\]

This strengthens the displayed blockwise \(O(s/\sqrt m)\) estimate
on that particular family, while reinforcing its conclusion: exact
ordinary growing segments can disperse height across moving primes.
GA-004's pairwise-coprime family has its own stronger special bound
\(O(s/m)\); no claim that the generic estimate dominates that bound is
made.

The source term cannot be dropped on these controls. GA-004's source
height is already \(\Theta(m^2)\), and all displayed states remain
near that height. A cyclic peak window would require enough actual
predecessor states before the displayed segment; those predecessors are
not supplied. AR-CLOCK-005 is a cycle theorem, not a theorem that any
finite high segment must have the same support lower bound. The source
alternative in AR-CLOCK-006 is exactly what handles this distinction.

## What remains unproved after both packets

The concurrent controls show that prime dispersion, binary complexity,
and spatial sparsity can coexist with every local Collatz recurrence on
arbitrarily long finite segments. They neither provide one fixed source
for all lengths nor realize a nontrivial ordinary cycle. The present
ordered estimate imposes stronger quantitative necessary conditions on
actual histories and on complete cycles, but still supplies no upper
restriction on moving prime support that contradicts those conditions.

Both notes retain the same decisive boundaries: fixed-source all-time
compatibility, accumulated recharge control, and complete cycle
denominator divisibility. None is discharged by combining the proved
finite statements.
