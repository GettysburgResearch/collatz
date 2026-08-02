# Frontiers and open problems

Collatz remains unsolved. This page records the smallest current obligations that would materially change the repository’s scientific state.

A frontier is not closed by a longer finite prefix, a new coordinate system, a proper-factor hit, a compatible 2-adic point, or a conditional growth theorem unless it resolves the exact ordinary or complete-denominator boundary stated below.

## SC*: universal fixed-source coefficient stopping

For the shortcut map, let

\[
C_k(n)=\frac{3^{q_k(n)}}{2^k},
\qquad
\tau_c(n)=\min\{k\ge1:C_k(n)<1\}.
\]

Define

\[
S_N=\{n\ge1:C_k(n)\ge1\text{ for }1\le k\le N\},
\qquad m_N=\min S_N.
\]

The integrated theorem proves

\[
m_N\to\infty
\iff
\tau_c(n)<\infty\text{ for every positive integer }n.
\]

### Open obligation

Prove either equivalent form:

1. every fixed positive integer has finite coefficient stopping time; or
2. the least all-supercritical source `m_N` tends to infinity.

### Smallest useful missing lemma

For every fixed `n`, construct a finite bound `Φ(n)` such that every all-supercritical parity word realized from `n` has length at most `Φ(n)`. In valuation form, beyond a source-dependent threshold prove

\[
v_2(3^{q(w)}n+A_w)<|w|.
\]

### What does not close SC*

- an abstract supercritical parity word;
- different finite sources at different depths;
- endpoint growth conditional on ordinary realization;
- zero entropy or thinness of the word family;
- a finite verified range without cofinal source-dependent control.

## FC*: complete first-crossing exclusion

Let `w` be a first coefficient crossing of length `j` and weight `q`, so

\[
D=2^j-3^q>0.
\]

For canonical source `r`, endpoint `s=r+d`, and affine numerator `A_w`, use

\[
A_w=Dr+2^j d=Ds+3^q d.
\]

### Open obligation

Apart from the trivial `1↔2` cycle word, exclude every complete canonical first-crossing realization with

\[
d\ge0.
\]

This must include:

- `d=0` nontrivial positive cycles;
- `d>0` acyclic near-returns;
- every complete prime-power factor of `D`;
- one common ordinary displacement across factors;
- compatible source and endpoint quotient data;
- every proper first-crossing inequality;
- exact physical replay.

### Smallest useful missing lemma

Prove one of the following globally for growing support:

1. balanced large-factor quotient jets cannot agree;
2. a dominant large factor and its small cofactor cannot complete the same displacement;
3. the resultant-root Laurent sum has least residue larger than the permitted displacement window, including zero.

### What does not close FC*

- congruence modulo one factor;
- independently chosen local residues;
- bounded-support or bounded-length searches;
- a real near-integer without dyadic replay;
- a cycle numerator identity without complete divisibility.

## Proposed SC* + FC* bridge

The intended repository-level implication is:

```text
SC* + FC* => every positive integer reaches 1.
```

The ingredients are compelling:

- a least positive counterexample has no smaller iterate;
- either it has no coefficient crossing or it has a first crossing;
- the no-crossing lane is the fixed-source SC* lane;
- no-descent at a first crossing produces a canonical displacement `d≥0`;
- a nontrivial positive cycle rotates to its minimum and enters the same first-crossing lane.

### Status

**PROPOSED.** The component reductions were reviewed at exact SHAs, but the exact combined normalization and coverage crosswalk has not yet been independently accepted as one theorem.

### Narrow review requested

Check:

1. the canonical positive source convention when the least residue is zero;
2. the sign of displacement under higher lifts;
3. that every repeated-state witness is retained by the primitive/injective reduction;
4. the trivial `10` cycle boundary;
5. notation and denominator orientation across the source packets;
6. that no source-qualified theorem is silently promoted.

Until that review passes, call this the **principal proposed roadmap bridge**, not an established exhaustive reduction.

## Aperiodic ordinary extraction

For a fixed architecture with nested positive survivor sets `S_N` and minima `m_N`, the integrated theorem gives the exhaustive decision:

```text
m_N bounded/eventually constant
    -> one positive all-depth seed;

m_N -> infinity
    -> no positive ordinary survivor in that architecture.
```

### High-value concrete targets

- the reviewed stationary six-branch chart;
- centered nearest-integer forced-tail systems with an explicit most-significant boundary;
- changing-height quotient-refund systems after transported-residue correction;
- nonlinear negative-cycle run-core systems;
- H-renewal systems with complete ordinary initialization.

### Required positive outcome

Write one finite positive seed and prove all-time legality and exact physical replay.

### Required negative outcome

Prove direct canonical-root escape or a sound ranking/height theorem for the entire declared architecture.

### What does not decide extraction

- every finite level being nonempty;
- a unique inverse-limit path;
- branch multipliers larger than one;
- an unbounded finite stack manufactured along hypothetical paths;
- fresh-prime turnover conditional on existence;
- a periodic or modular lasso.

## Periodic-tail synthesis review

A local proof packet now presents the complete-denominator periodic classification. Its source components were independently reconstructed, but the exact integrated synthesis still needs one narrow review.

### Review the following clauses together

- the all-zero word gives `x=0` rather than a positive/negative sign case;
- the denominator is the complete `2^L-3^s`;
- a finite preperiod reaches the unique periodic tail point;
- a controller symbol may be used only when it emits one fixed finite parity block;
- the trivial positive cycle is explicitly separated;
- no statement about genuinely aperiodic seed-first machines is inferred.

A passing review would remove the last integration-wording qualification from `IC-PERIODIC-001` without proving any new cycle or Collatz result.

## Six-branch least-root decision

For the stationary chart with

\[
P=3^{12},\qquad Q=2^{19},
\]

and six reviewed digits, finite affine and rational complete-tree self-sections collapse to the original expanding map, and no semilinear sanctuary exists.

### Open obligation

Decide the least legal roots:

\[
\sup_N m_N<\infty
\quad\text{or}\quad
m_N\to\infty.
\]

### Consequence of the known rigidity

A successful positive construction must use genuinely unbounded nonlinear arithmetic state or a proper source-specific sublanguage. Another finite tame rational recoding of the full tree cannot be the missing extraction theorem.

## Automata and proof-carrying ordinary boundaries

The fixed-depth safety languages are cofinite and their obvious recurrent SCC is a canonical-language artifact.

### Open obligation

Develop an abstraction that carries enough information to prove ordinary concretization, such as:

- a canonical most-significant boundary;
- a height or length counter;
- an exact finite-support certificate;
- a transported residue tied to one initial integer;
- or another sound ordinary witness invariant.

A residue-only recurrent graph is not sufficient.

## Complexity and recurrence route

The repaired factor-complexity theorem excludes nonconstant centered-cylinder words with lower complexity slope below

\[
1/\log_{64}(81/64).
\]

### Open obligation

Derive such a low-complexity presentation from a natural equality, near-extremal, substitutional, automatic, or finite-state language that would otherwise support ordinary stabilization.

### Required care

- preserve the nonconstant hypothesis;
- preserve the strict inequality;
- keep the result inside the reviewed `64→81` induced section;
- do not identify low factor complexity with eventual periodicity without proof.

## Proof-residency frontier

Round 1 places readable packets for the initial integrated layer on the branch. Remaining repository-wide residency work includes:

- importing local proof bodies for other reviewed claims outside the initial eight records;
- importing the PR #16 dependencies used by the factor-complexity repair;
- resolving source-ID collisions through manifests rather than renaming source claims;
- recording large artifact replay states without rerunning expensive computations merely for integration.

Proof residency is an information and durability problem. It must not be confused with mathematical promotion.

## Proposed connections for new work

These are invitations, not theorems.

1. **Ordinary-boundary PDR:** couple finite-state safety kernels to a canonical top boundary or length counter.
2. **Extraction–rigidity dichotomy:** turn failure of every finite tame section into a direct least-root escape theorem.
3. **Periodic endpoint of FC\*:** make the `d=0` cycle case a verified specialization of one clean FC\* bridge.
4. **Complexity–stabilization coupling:** force a low-complexity itinerary from an equality language, then apply the repaired screen.
5. **Source valuation versus factor synchronization:** seek a common arithmetic invariant that constrains both SC\* source divisibility and FC\* denominator residues.

Any strengthening developed from these connections should be committed as **PROPOSED** until independently reviewed.
