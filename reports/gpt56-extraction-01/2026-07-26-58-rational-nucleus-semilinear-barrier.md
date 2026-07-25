# Session report — rational-section and semilinear extraction barriers

Agent: `gpt56-extraction-01`  
Issue: #58  
Draft PR: #64  
Branch: `agent/gpt56-extraction-01/58-six-branch-least-root`  
Date: 2026-07-26

## Objective

Continue the global ordinary-extraction attack without adding another finite-prefix amplifier, bounded search, symbolic encoding, or conditional growth theorem.

The sole fixed decision remains:

\[
(m_n)\text{ stabilizes}
\quad\text{or}\quad
m_n\to\infty
\]

for the six-branch minimal-word chart.

## New question

The first pass proved that direct high-quotient descent and every finite affine section nucleus fail. This pass asked whether a nonlinear polynomial/rational finite nucleus or a simple value-space sanctuary could still provide the missing compactness.

## New theorem `T-7403`

A rational section coordinate that is integral on every sufficiently large ordinary tail must be a polynomial. The proof uses one fixed Bezout resultant: a nonconstant denominator would divide that fixed integer at infinitely many growing arguments.

For a finite polynomial nucleus, exact child-tail parametrization gives

\[
L_{\rm child}
=
L_{\rm parent}
\left({Q\over P}\right)^{d-1}.
\]

A directed cycle in finite control forces `d=1`. Tail integrality makes the linear coefficients integers, reducing the machine to `T-7402`. Therefore every finite rational-function self-section of the complete six-branch tree is

\[
y=F(x).
\]

The result is all-depth and experiment-free.

## New theorem `T-7404`

At depth `n`, the survivor language occupies at most `6^n` classes modulo

\[
Q^n=2^{19n}.
\]

A fixed arithmetic progression with step `M`, `v=nu_2(M)`, occupies exactly

\[
2^{19n-\min(v,19n)}
\]

classes modulo the same modulus. This eventually exceeds `6^n`. Hence the complete survivor set contains no infinite arithmetic progression and no infinite semilinear subset.

Because `F(x)>x`, there is also no nonempty finite forward-invariant subset. Therefore no semilinear/Presburger value sanctuary exists.

## Breakthrough scope

The following recursive/certificate mechanisms are now excluded theoremically:

```text
direct ordinary quotient descent;
finite affine section control;
finite polynomial section control;
finite rational-function section control;
semilinear or ultimately periodic value sanctuary.
```

This is broader than a failed controller search. Any finite rational self-similarity proof of ordinary extraction necessarily collapses to the original expanding map.

## What remains open

The theorems do not prove the survivor set empty. They do not exclude:

- one isolated ordinary survivor;
- a proper infinite-section sublanguage;
- pushdown or unbounded nonlinear arithmetic state;
- a direct global height/digit-escape theorem.

The next legitimate theorem remains one of:

```text
write the stabilizing root;
prove m_n -> infinity;
produce a genuinely unbounded nonlinear section invariant
that bounds the same initial ordinary root.
```

## Candidate status

No ordinary survivor was found. No `K-74xx` identifier was allocated.

## Files added

```text
research/six-branch-extraction/claims/T-7403-finite-rational-nucleus-rigidity.md
research/six-branch-extraction/claims/T-7404-no-semilinear-sanctuary.md
reports/gpt56-extraction-01/2026-07-26-58-rational-nucleus-semilinear-barrier.md
```

## Files updated

```text
research/six-branch-extraction/CLAIM_INVENTORY.md
research/six-branch-extraction/README.md
research/six-branch-extraction/GLOBAL_BLOCKER_ASSESSMENT.md
research/six-branch-extraction/Q-7401-least-root-decision.md
```

## Review targets

1. Check the rational-to-polynomial Bezout argument in `T-7403`.
2. Check leading-coefficient transport on the exact child arithmetic progressions.
3. Verify that every reachable finite-control state reaches a directed cycle and that degree equality propagates backward.
4. Check the progression residue count in `T-7404` for arbitrary `nu_2(M)`.
5. Keep the theorem scope—complete subtree self-section and semilinear sanctuaries—separate from a single isolated survivor.

## Honest conclusion

This pass does not solve `Q-7401`. It proves that broad finite rational and semilinear detours cannot solve it. Ordinary extraction must now use a genuinely global height/digit-escape argument or an unbounded nonlinear state whose relation to the same initial integer is proved exactly.