# Independent semantic review: complete word algebra

Date: 2026-11-23. Reviewer: collaborating agent `cycle_ideal`.
Verdict: **VERIFIED at the finite-statement scope below.**

Reviewed source:
`research/high-variance-20261123/CycleWordAlgebra.lean`

SHA256:
`fc42bf2a602592c7f7ebbe42ca3c21bb96b58f7ce2dc93aed2cafdbac47f984e`

The root agent authored this module. The reviewer authored the written
rational-cycle construction, but did not author these Lean definitions or
proof bodies. This is an internal reconstruction review, not external peer
review. Compiler execution and axiom receipts are separate evidence supplied
by the root replay.

## Reconstruction

`ones` counts the first bit and the complete suffix. The recursive `carry`
weights an initial odd bit by `3^(ones suffix)` and doubles every suffix
contribution, so its convention is exactly

`C(w)=sum_i 2^(d_i) * 3^(P-1-i)`.

I checked all twelve public theorem statements and proof bodies:

1. `ones_append`: chronological concatenation preserves the full odd count.
2. `carry_append`: the later word contributes its multiplier to the earlier
   carry; the earlier word length multiplies the later carry by a power of two.
3. `adjacent_swap`: changing 01 to10 lowers the complete carry by exactly
   `2^(prefix length)*3^(suffix odd count)`, retaining both contexts.
4. `marked_swap`: the source defect used in the written construction has
   difference `2*3^(suffix odd count)`. The displayed prefix has two ones,
   so the written exponent `p-2` is the suffix count.
5. `repeat_length`: the supplied chronological repeat has length k times
   the original length, including k=0.
6. `repeat_ones`: the corresponding complete odd count has the same scaling.
7. `repeat_carry_cast`: in any supplied commutative quotient ring where both
   block powers are one, the full repeat carry is k times the block carry.
8. `two_block_carry_cast`: the two families retain both complete carries.
9. `two_block_denominator_cast`: the cast is the complete integer difference
   `2^L-3^P`, without a norm or denominator-factor substitution.
10. `fixed_modulus_payment`: the additional hypothesis that M casts to zero
    makes both complete carry and complete denominator vanish. This has the
    correct form for a later Z/MZ application; it does not assert Euler's
    theorem or choose the original word.
11. `two_choice_nonzero`: if the two carries differ, their two tested linear
    combinations cannot both vanish. The proof works in every commutative ring.
12. `scaled_two_choice_nonzero`: the domain hypothesis and nonzero scaling
    factor are exactly what preserve the nonvanishing test at the extra prime.

The definitions and parameter order agree with equations (1), (5), (7)--(9)
of `CYCLE_IDEAL.md`. No mathematical correction was required.

## Scope

This review does not identify the abstract quotient ring with a modulus
without the supplied hypotheses. Mechanical-word existence, prime selection,
Euler/Fermat arithmetic, marker primitivity, physical rational realization,
all-state minimum bounds, the continued-fraction subsequence and the
arbitrary-modulus existence theorem remain written mathematics. The module
neither declares nor proves absence of all positive integer cycles.
