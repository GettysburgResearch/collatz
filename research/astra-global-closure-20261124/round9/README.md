# Round nine: ordinary return certificates and the remaining critical range

**Collatz remains OPEN. This pass does not supply a complete proof.**
The concrete addition is an unconditional Lean certificate excluding one
whole progression of least odd tripling disagreements. The packet also
derives a ballot upper bound for large-endpoint exact rows and applies
Evertse's theorem to the literal carry without a bound on its number of
odd inputs. These results leave explicit, substantial gaps.

Three GPT-6.2 Astra agents pursued cycle arithmetic, exact rows, and
Diophantine closure, then cross-reviewed their arguments. The coordinator
reconstructed the key deductions, added the final ordinary certificate,
and rebuilt all eight project modules. The repository refresh reached
PR207 and found important overlapping work. The packet credits those
overlaps; an independently reconstructed theorem is not counted as a
second breakthrough.

[Final Lean proposal](formal/README.md) · [Literature applications](LITERATURE.md) ·
[Fixed-head intake](../../../reports/astra-global-closure-20261124/round9/INTAKE.md) ·
[Coordinator review](../../../reports/astra-global-closure-20261124/round9/ROOT_REVIEW.md)

## 1. A proved ordinary progression, without a cycle assumption

Use the shortcut map \(T(2v)=v\), \(T(2v+1)=3v+2\).
PR192 proves that any failure of positive Collatz gives a least positive
odd q whose basin membership differs from 3q. At this particular witness,
q reaches 1 and 3q does not. Every positive multiple of three below 3q
reaches 1.

For every natural number u, define
\[
q=163815229+1377495072u,\qquad
z=383076351+3221225472u.
\]
The actual finite identities give
\[
0<z<3q,\qquad 3\mid z,\qquad T^{30}z=T^5(3q).
\]
The smaller source would therefore be simultaneously good and in the
component of the bad source 3q. Lean proves that no q in this progression
is the least odd tripling disagreement. The proof uses the real ordinary
map at clocks 30 and 5 and no named analytic input.
[Construction and exact theorem](formal/README.md)

The certificate combines a 26-step inverse progression with a four-versus-
five-step recentering identity. The broader inverse family excludes
\(s=116582680\bmod3^{17}\) when s is a restricted cycle minimum.
An exact search checks all 7,813,124 eligible inverse exponent compositions
through sixteen odd steps under the stated height and seventeen-predecessor
hypotheses. The displayed class is the first surviving smaller-multiple
class for that precise test.
[Cycle packet](critical/README.md) · [Search scope](critical/SHALLOW_ANCESTORS.md)

The late comparison also yields a useful limit on this search strategy.
For every finite K, arbitrarily large ordinary centers s resist both
safe-ancestor tests through K odd inverse steps ending at that s.
Some of those very same centers give a cutoff certificate at forward
clock eleven. The construction transfers a denominator-13 cycle-component
control by congruences, with s depending on K. It neither constructs an
ordinary infinite obstruction nor blocks certificates meeting a later
forward point.
[Written all-depth-family consequence](../../../reports/astra-global-closure-20261124/round9/critical/LATE_INTAKE.md)

This does not show that every remaining least candidate has such a
certificate. The formal CompleteReturnCover predicate states that
unproved assertion. Its equivalence with positive Collatz is printed
explicitly in the final module so the conditional implication cannot be
mistaken for a complete proof.

## 2. An opposing row bound, with its range limitation

Let \(N_b(q,\epsilon)\) count ordinary unit sources that reach an odd unit
q in exactly 2b shortcut steps with b odd inputs and real affine carry
\(\beta\ge\epsilon q\). In the equation
\(q=(3/4)^b x+\beta\), encode even inputs as +1 and odd inputs as -1.
Let H be the maximum prefix excess of even over odd inputs.

The same physical word satisfies
\[
\beta+1\le2(3/2)^H.
\]
The finite integer form of this inequality and its physical endpoint
interpretation are checked in Lean. Set
\[
h=\left\lceil\log_{3/2}\big((1+\epsilon q)/2\big)\right\rceil.
\]
Reflection after the first visit to h gives
\[
N_b(q,\epsilon)\le {2b-1\choose b-h-1}\quad(1\le h<b);
\]
the count is zero for \(h\ge b\). This reflection count and the following
asymptotic estimate are written proofs with independent finite checks:
\[
\max_{q\ge(3/2)^{351b/352}}N_b(q,\epsilon)
<2^{\lceil b/32\rceil}
\]
for each fixed rational \(0<\epsilon<1\) and all sufficiently large b.
[Complete proof](rows/UPPER.md)

**The known forced witnesses lie outside this range.** PR201 produces
endpoints on one fixed orbit with
\(q_i+1\le(q_0+1)(3/2)^{31b/32-2}\), and
\(31/32=341/352<351/352\). PR207's new aggregate construction uses an
even lower diffusive range \(q\le2^{\lceil\sqrt b\rceil}\). Neither lower
construction contradicts this upper bound. The missing estimate must
control the actual fixed-cutoff rows in their lower endpoint range.

The row lane also reconstructs an exact finite-survivor equivalence and
large rows at decreasing carry thresholds. Late PR206 independently
contains the same finite-survivor result with a sharper clock version,
and overlapping convergent climbs. These are credited comparisons and
controls, not new universal coverage.
[Row packet](rows/README.md) · [Late comparison](../../../reports/astra-global-closure-20261124/round9/rows/LATE_INTAKE.md)

## 3. Heavy Diophantine machinery with the complete carry retained

Fix an ordinary positive n and write \(x=T^k n\), with p odd inputs.
For \(S\) a fixed finite prime set containing 2 and 3, write \(v_{S'}\)
for the complete factor of v outside S. The actual carry
\(A=2^kx-3^pn\) satisfies, once it is positive,
\[
\log A_{S'}\ge k\log2+\log x_S-o(k).
\]
At any actual subexponential-return subsequence this gives
\(\log A_{S'}/k\to\log2\) and \(\log A_S/k\to0\).

For a different source \(m=n+2^k t\), \(t\ge1\), whose actual suffix
from \(x+3^pt\) reaches 1 in l steps with h positive odd count, let C
be the entire suffix carry. The four-coordinate positive row is
\[
2^l=3^{p+h}t+3^h x+C.
\]
Evertse's fixed-dimensional theorem gives
\[
x_{S'}C_{S'}\ge c_{S,\epsilon}\,3^{p+h}2^{-\epsilon l}.
\]
There is no bound on the number of odd steps or internal powered blocks
in this statement. The complete carry supplies the outside-prime factor.
No upper bound on that factor is proved, so it pays for the inequality
without giving a contradiction.
[Arithmetic argument and its first-hit qualification](arithmetic/README.md)

Counting descriptions separately shows that an exponentially large
convergent witness family contains few continuations of small total
powered-root cost, even with an arbitrary number of blocks. Its application
to the paired family retains the named analytic input F. The actual
critical orbit has growing parity-factor complexity under subexponential
height assumptions; it need not admit the compression that the rejected
closure argument would require.

## 4. The cycle structure and the parallel frontier

For a positive integer cycle whose odd sites lie below eight times their
minimum, divide each odd site by 1, 2 or 4 to place it in one dyadic
interval. Quarter-integer spacing makes the normalized successor order
a single rotation. For least shortcut period h and odd period p,
\(\gcd(h,p)=1\). In a single dyadic interval the physical word is mechanical
and the adjacent-swap denominator argument excludes a nontrivial cycle.

The new PR192 packet independently derives this same three-band rotation,
coprimality and mixed-band congruence. Earlier repository work already
contains the one-octave exclusion; PR193 now strengthens its occupation
consequence and PR206 proposes a larger range ratio. Round nine includes
the reconstruction, narrower checked lemmas, and explicit controls.
[Precise credits and surviving mixed coefficients](critical/README.md)

The prospective mixed-band polynomial has coefficients in \(\{1,2,4\}\).
An admissible word with integer cycle divisibility is still the problem.
Dropping the physical edge constraints makes the desired nonvanishing
false already at h/p=8/5. With those constraints it has not been proved.
The separate branch that exceeds the initial height strip also remains.

Late PR200 improves the strip exponent from 0.49 to 0.479 and proves a
depth-192 inverse obstruction for a more restricted mechanical language.
That language forbids the initial 222 inverse block of our positive
sixteen-step class. The results concern different source classes and are
compatible. Its finite obstruction can itself be realized at arbitrarily
large ordinary centers; it does not exclude meetings farther forward.
[Late fixed-head review](../../../reports/astra-global-closure-20261124/round9/critical/LATE_INTAKE.md)

## 5. Verification and the remaining obligation

The coordinator rebuilt five new modules and three pinned dependencies
using Lean 4.34.1 with warnings as errors and an empty project output cache.
All 43 new selected axiom inventories and 33 dependency inventories
passed with at most the standard three axioms. All five finite scripts
passed both normal and optimized Python, with ten byte-identical matches
to their recorded output. Separate reviews distinguish written geometric
and asymptotic assembly from the statements actually checked in Lean.

* [Lean receipt](../../../reports/astra-global-closure-20261124/round9/lean/receipt.json)
* [Finite replay receipt](../../../reports/astra-global-closure-20261124/round9/control-replay.json)
* [Kernel scope audit](../../../reports/astra-global-closure-20261124/round9/arithmetic/KERNEL_SCOPE_REVIEW.md)
* [Source ledger](SOURCES.json)

A closing step must operate on the supplied exceptional ordinary source:
cover every least disagreement by a valid return, prove the required
fixed-cutoff upper bound in the range of the forced witnesses, or exclude
both the mixed-band cycles and the first-crossing branch by another theorem.
The current packet does not establish any of those universal conclusions.
