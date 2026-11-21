# Focused semantic review: the ordinary affine pump

**Verdict: VERIFIED at the stated arithmetic and first-hit scope.** The
context-free and regular-language consequences are verified paper deductions,
not Lean declarations. No universal Collatz coverage result follows.

## Exact inputs

- `research/reframe-20261121/lean/DiscretePump.lean`, SHA-256
  `d7985c9dd16f6b5eb986b7d75e13a53852615b3f063534cb3a7e9dfa1ea2098f`.
- `research/reframe-20261121/DISCRETE_CLOSURE.md`, SHA-256
  `e3dd7d63c47e7d32a73b7e381af5a5b234eb223ed6ce87d900d94e1438382113`.

The primary agent reconstructed the algebra, the fixed-prefix orientation,
the first-hit contradiction, and the language deductions from the displayed
statements. This review records that semantic reconstruction. The combined
execution receipt separately records actual Lean checking and its axioms;
this document is not a substitute compiler receipt.

## Arithmetic

Write `a=2^A`, `b=3^r`, and `D(x)=(a-b)x-C`. From `b*y+C=a*x`, direct
expansion gives `b*D(y)=a*D(x)`. Iterating gives

\[
3^{rk}D(q_k)=2^{Ak}D(q_0).
\]

Since a power of two is coprime to a power of three, `3^(r*k)` divides
the ordinary integer `D(q_0)`. For a nonzero defect it is therefore at most
the absolute value of that one fixed integer. Choosing arbitrarily large
`k` when `r>0` contradicts this bound. The remaining zero-defect case is
exactly the inverse block's fixed-point equation; multiplication by the
nonzero integer `3^r` then forces every successive `q_k` to be equal.

The proof needs no positivity, divisibility-density argument, or completion
extraction. It does not apply unchanged after replacing `A`, `r`, or `C`
by a different block's parameters.

## Canonical clocks and prefix orientation

For a canonical family `u v^j z`, reading backwards from endpoint one
first fixes the ordinary value at the start of `z`. Repeating `v` acts on
this fixed value by the displayed inverse recurrence. Validity of each
whole certificate supplies ordinary intermediate values for every `j`.

The fixed prefix satisfies `3^b*n_j+P=2^U*q_j`. Thus `q_1=q_0` forces
`n_1=n_0`. The two claimed canonical clocks differ by `A>0`, contradicting
uniqueness of the first hit for a deterministic map. This is stronger than
an endpoint-only comparison, which would allow padding by the terminal
cycle. It also excludes a repeated block anchored at one without assuming
that positive nontrivial cycles have already been classified.

## Language scope

For literal parity words, an accepting run with at least `N` odd edges in
an `N`-state automaton repeats one of the initial/after-odd cut states. The
resulting accepted pump contains an odd edge. The preceding contradiction
therefore bounds the accepted odd count by `N-1`. Purely even loops are
allowed; `E*` supplies an immediate check of that limitation.

For a fixed finite alphabet of positive accelerated exponents, a nonempty
pump always contains an odd step. The regular-language corollary follows.
For a context-free language use its pumping form `u v^j x y^j z`. If `y`
is nonempty, the actual suffixes `y^j z` of the accepted canonical words
are themselves canonical certificates anchored at the fixed suffix `z`.
They violate the same inverse-block theorem. If `y` is empty, `v` is
nonempty and the fixed suffix is `xz`. This proves the stronger finite
context-free-sublanguage conclusion. It does not prove that claim for the
literal parity alphabet: in that alphabet the rightmost pump could contain
only even steps.

The infinite bounded-gap example is consistent with the theorem. For an
odd ternary unit `q>1`, one of the inverse gaps `2,4` or `3,5` gives a
strictly larger odd ternary unit. When the first candidate `p` is divisible
by three, replacing it by `4p+1` removes that divisibility. Starting from
five gives arbitrarily long canonical certificates over `{2,3,4,5}` by
changing the chosen block. It supplies no one fixed block that can be
pumped indefinitely, and no divergent forward orbit.

## Coverage boundary

The Lean theorem `no_canonical_affine_pump` takes actual affine equations
and first-hit certificates as hypotheses. It does not assert that every
symbolic word is legal or that every positive integer has a certificate.
The source note retains the missing total arithmetic dispatcher and the
rank cost of changing blocks. Those qualifications are essential to the
review verdict.
