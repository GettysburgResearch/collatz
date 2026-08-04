# Session report — completion attempt, exact depth frontier, and normality boundary

Agent: `gpt56-drift-01`  
Issue: #26  
Branch: `agent/gpt56-drift-01/26-5x1-portability`  
Date: 2026-07-22

## Starting hypothesis

The exact base-`5/4` forbidden-digit reduction might be small enough either to:

1. construct an infinite low-digit ordinary root; or
2. prove all roots eventually emit digit `2` or `3`.

The session attacked both directions and treated any finite computation only as
a certificate for its frozen scope.

## Approaches attempted

1. Recast global existence as boundedness or unboundedness of the exact least
   finite-depth roots `m_n`.
2. Derived a full cylinder-affine composition law for arbitrary split depths.
3. Converted exact minimization into a modular cyclic-successor problem.
4. Implemented and independently audited a meet-in-the-middle depth solver.
5. Reconstructed a first-omitted-term height argument for both symbols of a
   hypothetical ordinary directive.
6. Audited the precise literature location of the remaining problem in
   approximate multiplication and rational-base minimal words.
7. Tested possible shortcuts through measure zero, finite differences, phase
   scheduling, and support density; none yielded a valid global contradiction.

## New results

### Proposed mathematical claims

- `L-8804`: exact meet-in-the-middle cylinder composition and least-root formula.
- `T-8808`: sharp depth-50 least-root theorem.
- `T-8809`: both symbols in an ordinary survivor directive are multiplicatively
  syndetic with explicit support-count constant.
- `O-8802`: exact identification with the `p=5,q=4,S={0,3}`
  approximate-multiplication problem and the base-`5/4` minimal-word frontier.

### Exact finite computation

X-8803 proves within its frozen scope that

```text
m_50=4538335001132531.
```

The associated physical seed

```text
A=4538335001132530
```

survives exactly fifty chart macro-steps and then leaves on bottom digit `3`.
Every smaller positive `X`, equivalently every

```text
A<=4538335001132529,
```

leaves before fifty macro-steps.

## Main conceptual correction

The instruction to “complete the result” exposed a crucial boundary. The final
global step is not merely the unfilled tail of an internal connector argument.
It is exactly a two-residue instance of the approximate-multiplication
termination conjecture proposed by Dubickas and Mossinghoff, and equivalently a
weak digit-richness instance of the current rational-base minimal-word
normality conjecture.

A complete proof would be a genuine theorem at that frontier. No located
literature result was silently promoted to supply it.

## Hidden connections

### Finite roots as a monotone decision sequence

Let `m_n` be the least positive depth-`n` root. Then an infinite ordinary root
exists iff `(m_n)` is bounded, equivalently iff it eventually stabilizes. This
turns global termination into the concrete asymptotic target `m_n -> infinity`.

### Product-formula pressure on both colors

The ordinary completion makes both the one-support and zero-support rational
first-omitted tails. Each symbol must appear in every multiplicative interval

```text
(X, log_4(5)X+O_A(1)].
```

Thus a survivor cannot hide all arithmetic complexity in one sparse symbol.

### Complexity theorem is known-adjacent

The slope in T-8803 equals Dubickas's known minimal-word lower bound

```text
log(4)/log(5/4).
```

The repository proof remains useful as an independent, chart-native
reconstruction with an explicit repeated-factor inequality, but novelty claims
must reflect the prior theorem.

## Failed approaches

### Haar measure and dimension

T-8807 proves severe thinness, but a countable ordinary section can meet a
measure-zero Cantor set. No emptiness inference is valid.

### Support density alone

T-8809 and neighboring T-9819 force logarithmic support counts, but many binary
words satisfy them. A separate physical upper bound is required.

### Finite survival extrapolation

The depth-50 minimum is enormous, but monotone growth through any finite depth
does not prove unboundedness.

### Phase-only connector regeneration

Already closed by T-8805/R-8801; the exact state is the growing rational-base
node, not a two-state phase switch.

### Full normality as an imported result

Normality would immediately force exit, but it remains conjectural and was used
only to position the target.

## Candidate counterexamples

None. The depth-50 witness exits and is not a `K-####` candidate.

## Potential errors and adversarial targets

1. Reconstruct the cylinder identity and pair bijection in L-8804.
2. Reimplement X-8803 without copying its frontier recursion.
3. Audit cyclic wraparound and exclusion of the all-zero root.
4. Verify the exact physical inequality translating `X` ranges to `A=X-1`.
5. Rebuild the negative complementary-tail bound in T-8809.
6. Check the literature identifications against the original 2009 paper and
   arXiv `2510.11723v2`, not secondary summaries.
7. Do not describe T-8803's asymptotic slope as novel after O-8802.

## Files changed

```text
research/drift-isolation/claims/L-8804-meet-in-middle-cylinder-composition.md
research/drift-isolation/claims/T-8808-sharp-depth-50-frontier.md
research/drift-isolation/claims/T-8809-two-color-support-syndeticity.md
research/drift-isolation/claims/O-8802-known-frontier-identification.md
research/drift-isolation/NORMALITY_AND_APPROXIMATE_MULTIPLICATION.md
experiments/X-8803-mitm-frontier/README.md
experiments/X-8803-mitm-frontier/run.cpp
experiments/X-8803-mitm-frontier/results/canonical.json
reports/gpt56-drift-01/2026-07-22-26-mitm-normality-frontier.md
```

## Claims affected

New: `L-8804`, `T-8808`, `T-8809`, `O-8802`, `X-8803`.

No canonical root ledger is edited.

## Recommended next actions

1. Independent mathematical reconstruction of L-8804 and T-8809.
2. Independent implementation of the depth-50 minimum.
3. Derive a recursive lower bound on cyclic successor distances in L-8804.
4. Attack the weak minimal-word theorem “some digit 2 or 3 occurs,” rather than
   full normality.
5. Seek a residue-plus-height PDR invariant that can be exported as a finite
   proof certificate.

## Organizational improvement ideas

When a repository frontier is found to coincide with a named external
conjecture, add a mandatory boundary packet containing:

```text
EXACT EQUIVALENCE:
KNOWN THEOREMS RECOVERED:
CONJECTURAL INPUT THAT WOULD CLOSE IT:
WEAKEST SUFFICIENT NEW THEOREM:
BEST EXACT FINITE CERTIFICATE:
```

This prevents internal notation from disguising the true difficulty while still
making new finite and conditional advances cumulative.
