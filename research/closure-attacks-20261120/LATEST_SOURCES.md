# Latest-source audit and dependency boundary

The live repository was checked on 20 November 2026. The default branch
was ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a. This packet is a separate
research branch from that baseline; it does not merge the open research
branches or promote their contents to the accepted baseline.

The following are immutable source pins, not assertions that every claim
in the named PR has been verified. A path and local claim identifier or
section accompany each use.

## PR146: ordinary tripling, variation, and one-sided closure

**Dependency snapshot:** 6863d298187af8b2619efbf78cc4b0aa8e627393.
The later head discovered during this investigation is discussed below;
these earlier mathematical dependencies remain pinned to their original bytes.

- [THREE_RAY_ONE_SIDED.md](https://github.com/GettysburgResearch/collatz/blob/6863d298187af8b2619efbf78cc4b0aa8e627393/research/upper-bit-mergers/THREE_RAY_ONE_SIDED.md):
  its ordinary one-sided basin equivalences, including the implication
  \(16k+1\in C\Rightarrow32k+1\in C\), are alternate closing statements.
  They do not prove their own closure premise.
- [THREE_RAY_UPPER.md](https://github.com/GettysburgResearch/collatz/blob/6863d298187af8b2619efbf78cc4b0aa8e627393/research/upper-bit-mergers/THREE_RAY_UPPER.md),
  equation (1): the actual tripling-failure count
  \(O(X/\sqrt{\log(2X)})\) is the synchronization input to the critical
  singularity calculation. The source supplies its excursion argument
  and credits the earlier canonical-process and coalescence work.
- [THREE_RAY_DENSITY.md](https://github.com/GettysburgResearch/collatz/blob/6863d298187af8b2619efbf78cc4b0aa8e627393/research/upper-bit-mergers/THREE_RAY_DENSITY.md),
  section “A separate criterion when both components have positive upper
  density”: harmonic divergence of a separating boundary already has a
  predecessor here. The present packet does not claim to originate that
  consequence.

The analytic note gives the precise input hypotheses it uses. The one-sided
tripling criterion is not used as an unconditional merger law in the new
single-multiplier proof.

## PR154: the starting structural packet

**Head:** fe40bb6f88e8094290ef01207d9bf7c4798d35d0.

- [component/PROOF.md](https://github.com/GettysburgResearch/collatz/blob/fe40bb6f88e8094290ef01207d9bf7c4798d35d0/research/structural-reset-20261120/component/PROOF.md),
  CR-001--002: the old restricted five-ray criterion and complete
  conditional descent. M5-001--003 in this packet remove its need for
  the unbounded \(5\cdot3^i\) query family and reprove the descent directly
  on ternary units.
- [component/REDUCED_LAWS.md](https://github.com/GettysburgResearch/collatz/blob/fe40bb6f88e8094290ef01207d9bf7c4798d35d0/research/structural-reset-20261120/component/REDUCED_LAWS.md):
  the earlier smaller sufficient system still used tripling invariance.
  The new proof does not.
- [adelic/PRIME_HEIGHT_ESCAPE.md](https://github.com/GettysburgResearch/collatz/blob/fe40bb6f88e8094290ef01207d9bf7c4798d35d0/research/structural-reset-20261120/adelic/PRIME_HEIGHT_ESCAPE.md):
  the ordinary affine numerator, gcd bound, and blockwise height
  dispersion are the starting point for the localized clock proof.
  The current arithmetic note repeats its load-bearing elementary
  derivation rather than importing an unstated analytic hypothesis.

The fixed-word slope obstruction is also already in that component proof.
Its restatement and clock consequence in PC-001 carry no broad novelty
claim.

## PR155: subcritical Dirichlet coercivity and its endpoint

**Head:** 92f499b9d340d1ff8cc643c3eef3477d61b477c1.

- [ORDINARY_DIRICHLET_COERCIVITY.md](https://github.com/GettysburgResearch/collatz/blob/92f499b9d340d1ff8cc643c3eef3477d61b477c1/research/gemini-dirichlet-global-20261120/ORDINARY_DIRICHLET_COERCIVITY.md),
  OD1--OD4 and the finite ordinary variation input: the coercivity and
  equality-of-abscissa conclusions are subcritical, \(0<s<1\).
- [ENDPOINT_BOUNDARY.md](https://github.com/GettysburgResearch/collatz/blob/92f499b9d340d1ff8cc643c3eef3477d61b477c1/research/gemini-dirichlet-global-20261120/ENDPOINT_BOUNDARY.md),
  E1--E3: a finite harmonic tripling-defect sum gives a constant dyadic
  logarithmic-profile limit. This is the endpoint rigidity input to the
  source-qualified critical argument.
- Same endpoint note, E4--E5: the displayed centered harmonic-mass bound
  contains an additional logarithmic defect weight. No removal of that
  weight, or unconditional finiteness of the required defect sum, is
  imported.

The new calculation treats the approach \(s=1+\varepsilon\) from the
convergent side and distinguishes unnormalized component mass from its
normalized boundary. It does not extend OD1 to a missing endpoint by
continuity.

## PR156: fixed-source arithmetic and finite-probe boundaries

**Head:** c5cb84502c7289705d59a8781a65fd845b9b6b14.

- [FIXED_SOURCE_CLOSURE.md](https://github.com/GettysburgResearch/collatz/blob/c5cb84502c7289705d59a8781a65fd845b9b6b14/research/global-rigidity-20261120/FIXED_SOURCE_CLOSURE.md),
  FS1 and sections 2--4: the exact denominator/difference identities for
  an actual prefix retain the complete denominator. Local approximation
  alone does not supply an ordinary return. The natural Subspace-Theorem
  product is at the critical scale, and the needed algebraicity and
  stronger approximation are not supplied.
- [Q_SECTION_GUARDS.md](https://github.com/GettysburgResearch/collatz/blob/c5cb84502c7289705d59a8781a65fd845b9b6b14/research/global-rigidity-20261120/Q_SECTION_GUARDS.md),
  QG1--QG4: its section guards and ordinary orientation constraints are
  separate from the homogeneous \((x,5x)\) pair studied here.

The spectral, smoothing, and finite-place boundaries in the surrounding
packet motivated looking for ordered and source-preserving mechanisms.
They are not used as mathematical premises of the new elementary proofs.

## Concurrent PR157 and the later PR146 head

A second live check during this investigation found **PR157** at
64361ecca770092d6c8242dc6211e38818af2e50, published while this packet was
being developed. Its
[merger.md](https://github.com/GettysburgResearch/collatz/blob/64361ecca770092d6c8242dc6211e38818af2e50/research/global-closure-20261120/merger.md),
GCM-001--002, proves the stronger criterion

\[
x\in C,\quad x\ \text{odd},\quad 3\nmid x
\quad\Longrightarrow\quad5x\in C.
\]

It supplies a complete directed induction with one conditional five step
per applicable cell. The M5 equivalence in the present packet is a shorter,
independent equality-based proof; it is **not stronger than that new
one-sided result**. No old claim of progress is kept by ignoring this
concurrent source.

PR157's
[transport.md](https://github.com/GettysburgResearch/collatz/blob/64361ecca770092d6c8242dc6211e38818af2e50/research/global-closure-20261120/transport.md),
GCT-001--004, retains original source weights in a positive return
occupation functional. A sublogarithmic reciprocal-psi bound would exclude
both escape and nontrivial cycles. Its proved smaller reciprocal-height
Green bound deletes periodic states and does not supply that upper bound.
The source includes an entirely terminating control showing why qualitative
absorption alone does not imply the proposed quantitative rate. The root
reviewed the complete written argument for this interface; this packet
does not import or reexecute its separate acceleration stack.

Its [arithmetic.md](https://github.com/GettysburgResearch/collatz/blob/64361ecca770092d6c8242dc6211e38818af2e50/research/global-closure-20261120/arithmetic.md)
and [closing-attempts.md](https://github.com/GettysburgResearch/collatz/blob/64361ecca770092d6c8242dc6211e38818af2e50/research/global-closure-20261120/closing-attempts.md)
preserve changing-source long legal segments, recharge controls, and
shifted-power failures of simple five-lift plans. They reinforce the need
for a fixed-source argument. The ordered height inequalities in this
packet remain compatible with those finite constructions.

The same check found **PR146** at
1608bb607fadae62723a22156bc96f6ebb452e43. The root read
[DEEP_REVERSE_BASIN.md](https://github.com/GettysburgResearch/collatz/blob/1608bb607fadae62723a22156bc96f6ebb452e43/research/upper-bit-mergers/DEEP_REVERSE_BASIN.md):
the proposed directed equivalence reduces convergence to
\(128k+1\in C\Rightarrow128k+2\in C\) for positive \(k\) with
\(4\nmid k\). Its first nonempty antecedent rank already encodes
convergence of \(3^{27j-1}\) for every positive \(j\). The source reports
Lean verification of its reduction, but this task has not independently
rebuilt those new Lean files or promoted the remaining adjacent
implication into a proved ordinary fact. The earlier UP/EP inputs used
here were not silently repinned to this later head.

## External inputs and prior art

The critical note separately pins the positive lower predecessor-density
statement used by PR145 at
dd245a712f985909f541590e3f6c179b7ba011e4,
research/native-pressure-20261118/ORDINARY-DENSITIES.md.
Its external manuscript and formalization remain **SOURCE-QUALIFIED**:
this task did not independently rebuild that formalization or establish
its full dependency chain.

The arithmetic note compares its derivation with
[rStation paper 138](https://rstation.ai/problems/collatz/papers/138),
“Prime-power returns and multiplicative complexity of Collatz orbits,”
version 1, 13 November 2026. That source already has actual return
numerators, prime-power tails, joint-return estimates, and relative-height
escape statements, and credits Yang's earlier work. The localized
height-sum estimate and peak-window corollary are described at their
specific scope; no blanket priority or verification claim is made about
the external paper.

The physical note cites Applegate--Lagarias'
[*The 3x+1 Semigroup*](https://arxiv.org/abs/math/0411140), Theorem 1.1 and
Table 3, for its established multiplicative certificate. Its ordinary
carry calculation is proved explicitly. Multiplicative products and
actual integer orbit paths are kept distinct.

## What this source audit does not establish

It does not turn a source's PROPOSED statement into an accepted theorem,
review neighboring claims by association, or make an ordinary fixed-source
statement out of changing finite witnesses. Each dependent result in this
packet retains its exact hypotheses. None of these sources or the new
arguments supplies the remaining universal physical merger or excludes
cycles of unrestricted prime support.
