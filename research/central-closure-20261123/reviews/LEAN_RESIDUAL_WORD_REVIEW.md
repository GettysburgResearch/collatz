# Independent semantic review of the residual-word Lean bridge

Reviewed source:
`collatz_work/nov23_root/ResidualWord.lean`

SHA256:
`420d1eb7976dca248cc4e85846586e253751379907739bc6a2bd816aca3f79e6`

Reviewer: cycle research lane, 2026-11-23.

## Outcome

The 12 public theorem statements and their proofs match the stated
finite algebraic part of `RESIDUAL_UNIT_EXCLUSION.md`. The source
does not contain a proof of unrestricted Collatz or conceal the
irreducibility premise of the generic preservation theorem.

This was an independent semantic source review. The root agent supplied
the completed Lean compilation and axiom audit; this review did not
repeat compilation or broaden earlier testing.

## What is formalized

The finite numerator uses the same coefficient convention as the
research note:

\[
Q(X)=\sum_{i<p}2^{d_i}X^{p-1-i}.
\]

The geometric quotient is exactly

\[
S_p(X)=\sum_{i<p}4^iX^{p-1-i},
\qquad S_p(X)(X-4)=X^p-4^p.
\]

Coefficient extraction is valid at every `i<p`, including `i=0`
and `i=p-1`. The truncated natural-number exponents in the definition
are harmless under this range condition: the proof explicitly shows
distinct in-range indices give distinct powers.

For `p>0`, both `Q` and `S_p` are proved nonzero of degree `p-1`.
Thus `S_p | Q` forces the quotient to be a constant. Leading coefficient
comparison identifies that constant as `2^(d 0)`; this step is proved,
not assumed as a coefficient hypothesis.

The subsequent theorems prove all exponent equalities
`d i=d 0+2*i` for `i<p`. The single position bound
`d(p-1)<2*p` forces `d 0<=1`. An ascending-position assumption is
unnecessary here because the polynomial identity itself implies the
ascending profile. The phase `d 0=1` is explicitly retained.

The generic theorem `principal_factor_survives` correctly assumes
`Irreducible M`, `M | G*F0`, `G | Q`, and a positive real root of `M`.
It derives `M | F0` from primality and strict positivity of the actual
numerator at that root. It does not assume numerator nonvanishing as
a hidden stand-in for Collatz; positivity of its finite sum is proved
in `numerator_positive`.

The linear-residual bridge assumes the exact identity
`G*(X-4)=X^p-4^p`, proves `G=S_p`, then derives the alternating profile.
The final realizer theorem assumes the actual affine equality
`(4^p-3^p)*n=Q(3)` and proves `n=1 or n=2`. The positive denominator
is proved using `p>0`, so the cancellation is valid.

## What remains a written mathematical input

The Lean file does not specialize the irreducibility premise to
`M=X^b-2^a`; the root-modulus/constant-term proof of that fact remains
in the written note. Nor does it formalize the full passage from
`|F0(3)|=1` to `A=2p` and `F0=X-4`, which uses principal-binomial
survival, the elementary modulo-eight argument, and the equality case
in the complex root-distance bound.

The ordinary realizer theorem identifies the starting natural number
as 1 or 2. Its statement is an affine-realizer conclusion, not a
general theorem about arbitrary orbit convergence. Referring to these
as phases of the ordinary trivial cycle additionally uses the direct
known transitions `1 -> 4 -> 2 -> 1` (or shortcut `1 -> 2 -> 1`).

These are clear scope boundaries. The formal bridge proves the actual
polynomial-to-word implication, while the accompanying elementary note
supplies the algebraic-number/root part of the complete unit theorem.
