# Ordinary source closure: six-hour research pass

**Status: research checkpoint; Collatz is not proved.** This packet pursues the
full positive-integer problem from the exact geometric Syracuse law, complete
cycle denominators, and global component colorings. It builds on the preceding
[three-hour pass](../astra-unconventional-20261126/CLOSING_PROPOSAL.md) and the
five changed research heads recorded below. It does not replay earlier bulk
verification or import their branch histories.

The odd map is `U(x) = (3*x+1)/2^v₂(3*x+1)` on positive odd integers. The
shortcut map is `T(x)=x/2` on even integers and `(3*x+1)/2` on odd integers.
The density `rho_k` has mean one on `Z/(3^k)`, and its defining independent
gap has probability `2^(-e)` for `e>=1`. No inverse policy replaces that law.

## The escape attack

[Exponential dust](escape/EXPONENTIAL_DUST.md) gives a source-qualified written
decomposition of the original finite harmonic mass. Its diffuse part has a
uniform fixed dyadic residue at each specified depth. Its atomic part retains
the actual ordinary rays and their positive component charges. This removes
the clipping function from the preceding escape detector.

For the literal modulus-eight test

\[
 (W(1),W(3),W(5),W(7))=(-1,3,-5,3)/4,
 \qquad Z_k=\sum_{\substack{1\le y<2\cdot3^k\\y\text{ odd}}}
                   W(y)\rho_k(y)/y,
\]

the proposed asymptotic theorem gives

\[
 \liminf Z_k/k\ge(7/4-\log_2 3)\sum_{C\text{ escaping}}H_C.
\]

Every nonempty positive escaping component has `H_C>0` under the retained
predecessor and passage inputs. [The Dirichlet completion](root/DIRICHLET_TRACE.md)
replaces the moving endpoint interval by an ordinary convergent series `S_k`
with the explicit depth-independent bound `|S_k-Z_k|<=5/8`. It is the fixed
character combination

\[
 4S_k=-3L_k(1,\chi_{-4})+L_k(1,\chi_8)+L_k(1,\chi_{-8}),\qquad
 L_k(s,\chi)=\sum_{n\ge1}\rho_k(n)\chi(n)n^{-s}.
\]

Proving a nonpositive lower normalized subsequential limit of that expression
would exclude every positive escape. **That sign assertion is open.** These
series retain the periodic coefficient `rho_k`; they are not ordinary
multiplicative Euler products.

Two additional written results describe the actual inverse process at every
ordinary root: [canonical path laws](escape/CANONICAL_INVERSE_PATHS.md) give
geometric-word frequencies, an iterated-log fluctuation bound, and polynomial
growth of the canonical trace along typical paths;
[real fibres and the traveling front](escape/REAL_FIBRE_AND_FRONT.md) identify
full-dimensional singular real fibres and a common two-sided escape profile.
They explicitly retain target-dependent entrance clocks. Singularity of normal
legal rays, including the first-minimum-cell result, is credited to Weaver's
paper 175. These are analytic written deductions from cited inputs, not Lean
theorems in this packet.

## The cycle and global attacks

| Result | What it controls | Remaining pointwise obligation |
|---|---|---|
| [Complete-divisor tail](arithmetic/COMPLETE_DIVISORS.md) | The entire cancellation `gcd(C,2^h-3^p)` for all fixed-weight near-critical parity words, with no gap cutoff | Rule out an exceptional primitive word with complete ordinary cancellation |
| [Periodic sibling floor](arithmetic/PERIODIC_TRACE.md) | `liminf rho_k(a)/a >= alpha/7` at every phase of every positive cycle, and a reciprocal bound over all periodic phases | Obtain a conflicting upper estimate at those actual phases |
| [Component word complexity](arithmetic/COLOR_WORDS.md) | Uniform catalogue complexity of every finite Collatz-invariant coloring, including rare blocks; the external compression theorem gives exponent strictly below binary entropy `H₂(log₃2)` | Force a matching lower complexity from two distinct positive components |
| [Farey current](global/FAREY_CURRENT.md) | Exact positive lattice counts at all integer scales and a small positive cyclotomic angle on complete ordinary paths | A global restriction incompatible with that current |
| [Primitive modular markers](global/ELLIPTIC_MARKERS.md) | The complete reduced cycle denominator is recovered by two consecutive even-cut marker defects | Exclude the exceptional case in which every primitive marker is integral |

The divisor estimate is a finite-population theorem, not an exclusion of a
single cycle. The modular congruence controls are actual positive one-edge
paths and show why closure modulo a fixed level is insufficient. The coloring
bound is topological and uniform; zero complexity entropy alone does not imply
a constant coloring.

## Lean and reproducible checks

Six new Lean modules check finite arithmetic and exact orbit kernels:

* [MinimumCode.lean](arithmetic/MinimumCode.lean): physical minimum, carry cap,
  and full numerator decoding from a bounded binary prefix.
* [PeriodicSiblings.lean](arithmetic/PeriodicSiblings.lean): the genuine odd map,
  distinct transient siblings, disjoint entry branches, and transfer floors.
* [ColorWords.lean](arithmetic/ColorWords.lean): exact affine lifts, labelled
  endpoint partitions, and factoring a shifted color word through its partition.
* [FareyCurrent.lean](global/FareyCurrent.lean): integral cone bijection, first
  occupied level, and angular identities.
* [EllipticMarkers.lean](global/EllipticMarkers.lean): primitive first columns,
  integral marker existence, and complete polynomial divisor obstructions.
* [FormalTransport.lean](root/FormalTransport.lean): legal inverse traces are
  actual odd iterates, exact affine offsets, and signed real-mark transport.

[check_lean.py](check_lean.py) compiles into fresh project objects, using Lean
4.34.1 and Mathlib `d13f23b723b8a846827a245b89c10fc7d3f11612`, and prints and
audits the axioms of every public theorem. The build does not formalize the
infinite analytic limits or the cited external theorems.

[check_linear_trace.py](escape/check_linear_trace.py) uses integer outward
enclosures of the exact finite law. The retained depth-16 interval for `Z_16`
is `[-0.0672309,-0.0672270]`. Independent wrapped-exponent enumeration checks
every density entry through depth five. These finite values do not settle the
asymptotic sign. The retained table and compilation receipt are in
[reports/astra-six-hour-20261127](../../reports/astra-six-hour-20261127/).

## Frozen repository intake

The full all-state metadata inventory and pass timing are in
[PR_INTAKE.json](../../reports/astra-six-hour-20261127/PR_INTAKE.json). New
mathematics was inspected at these five heads, which had advanced since the
preceding pass:

| PR | Full head | Relevant advance retained |
|---|---|---|
| [201](https://github.com/GettysburgResearch/collatz/pull/201) | `21bed7ac2b1b1bb4baf0f6cabd53f8b9dd11b58a` | Exact escape gates, finite Lean trapping equivalence, actual cofactor bounds |
| [200](https://github.com/GettysburgResearch/collatz/pull/200) | `ad70a3b831867cb8a74d402a2a1abdc419f5a09b` | Exact component pressure, completed reset estimates, squareclass rank criterion |
| [197](https://github.com/GettysburgResearch/collatz/pull/197) | `1f0f496fbea37792439feada6106eaaff596bcd1` | Fixed ordinary-source clock obstructions and sparse modified-carry controls |
| [195](https://github.com/GettysburgResearch/collatz/pull/195) | `51d97cbe17054415acaf95e422801a3532545033` | Full frontier consumer, canonical floor families, fixed-word cover obstruction |
| [192](https://github.com/GettysburgResearch/collatz/pull/192) | `ed7a6fe30b8602407f77855ceb74ce0489ce9c10` | Paid hard-parent repairs, all-clock grammar, corrected two-place regulator |

The prior own published head is `25f5462e2c43feea65760884f7ea8f53576fbc18`.
Each note states its external inputs and the first unsupported inference.
No claim of complete convergence, cycle uniqueness, or absence of escape is
made by this checkpoint.
