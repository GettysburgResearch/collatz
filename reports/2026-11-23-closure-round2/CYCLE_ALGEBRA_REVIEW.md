# Independent semantic review: complete-denominator cancellation

Reviewer: the in-session `escape_rigidity` agent, 2026-11-23.

**Verdict: PASS for the six public finite-arithmetic statements in
`CycleCancellation.lean`, and their interpretation as the carry/gcd
identities in Section 2 of the written note.** This is internal
reconstruction, not external peer review or a full audit of the cited
literature.

## Exact inspected sources

| Source | SHA256 |
|---|---|
| `research/closure-round2-20261123/CycleCancellation.lean` | `7d9118b6a8efeefc6e6b3229b95420771f88291ed2583f259c00ae665648724d` |
| Imported `research/high-variance-20261123/CycleWordAlgebra.lean` | `fc42bf2a602592c7f7ebbe42ca3c21bb96b58f7ce2dc93aed2cafdbac47f984e` |
| Corresponding `research/closure-round2-20261123/CYCLE_CANCELLATION.md` | `b77eb45c9c7852dba80f24aed88901f2720122a781ce05f4e24437306cadff5f` |

The imported chronological carry and its concatenation theorem were
read explicitly. The first bit is the first shortcut step; the formula
is `C(uv)=3^(ones v) C(u)+2^(length u) C(v)`. It has not been replaced
by a prefix-only correction or a different clock convention.

## Reconstruction of the new declarations

1. **`moving_one_carry`.** Moving the single one from after `h` zeroes
   to before them changes its complete contribution by
   `2^(length u)*3^(ones v)*(2^h-1)`. The earlier prefix and later
   suffix are unchanged, and the two words have the same length and
   weight. Natural subtraction is legitimate because `2^h>=1`.
   The formal theorem also covers `h=0`, where its displacement is zero.
   Both private all-zero-word lemmas have the expected values.
2. **`denominator_coprime_two_three`.** Positive exponents ensure the
   ordinary denominator `2^A-3^p` is odd and not divisible by three.
   The supplied inequality prevents truncated natural subtraction from
   silently standing for a negative denominator. The proof derives the
   two coprimalities from coprimality of the full powers.
3. **`gcd_after_unit_displacement`.** From `D|C` and
   `C=C'+factor*shift`, the gcd with `C'` equals the gcd with
   `factor*shift`, by divisibility in both directions. Removing the
   explicitly coprime factor gives exactly `gcd(D,shift)`. There is no
   prime-by-prime approximation or squarefree restriction.
4. **`moving_one_gcd`.** The factor `2^(length u)*3^(ones v)` is proved
   coprime to `D` from the two supplied coprimalities. Applying the
   preceding identity gives the entire numerical gcd with `2^h-1`.
5. **`full_denominator_moving_one_gcd`.** Here `D` is the denominator
   of the complete supplied word. The inserted one proves positive
   length and odd count; the positive-denominator hypothesis discharges
   the natural-subtraction guard. The needed two/three coprimalities
   are derived, not supplied as missing arithmetic input. Reordering
   the same one and zeroes preserves the neighboring word's denominator.
6. **`adjacent_zero_has_coprime_neighbor`.** At `h=1`, the displacement
   is a unit modulo `D`, so the neighboring carry is coprime to the
   entire denominator. The statement includes `D=1`; it correctly
   does not claim the neighboring rational state is then nonintegral.

The written adjacent-neighbor product claim is also algebraically
consistent: its two gcds are coprime and each divides `D`, so their
product divides `D`. The reduced-denominator formula uses the full
numerical gcd and retains every prime-power valuation.

## Scope

The original zero residue is an explicit hypothesis. The result tells
what happens to a complete word **if** its full carry is divisible by
its denominator; it does not prove that such a word is absent. It
neither bounds the numerical cancellation after polynomial gcd removal
nor proves the proposed all-word zero-fibre exclusion.

The graph packing, cyclic-window reconstruction, residue-order
normalization and literature applicability arguments in the note are
written mathematics. They are not included in the six Lean claims or
in this review's formalization verdict. The principal agent's actual
compilation and axiom-audit receipts are separate execution evidence.
