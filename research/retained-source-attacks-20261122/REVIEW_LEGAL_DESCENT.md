# Independent review: nonlocal source surgery

Reviewer: `/root/canonical_charge`. Date: 2026-11-22.

**Verdict: VERIFIED, for the stated finite ordinary deductions and the narrow
failed surgery classes. Universal source surgery remains OPEN.**

Reviewed file: `LEGAL_DESCENT.md`, SHA256
`32c2bf30b863fa78eafc33f3d7366b626e1382094241664e7c4cfc40802f8fb8`.

The reviewer independently read PR177 at
`e4ca639326bac73da8c2a698dec8a749e5efbe68`,
`research/lean-exact-witness-global-20261121/JOINT_MINIMAL_COUNTEREXAMPLE.md`,
including its original arbitrary-target interval hypothesis. The closing
statement in that source remains unproved. Its Lean build and all earlier
source proofs were not rerun for this written review.

## Checked deductions

- **Odd record maximum.** A suffix beginning at an odd state at least q is
  a complete actual certificate at strictly lower grade. Keeping the initial
  exponent gives a powered source at least S. The original full interval
  hypothesis applies because capture requires `0<t<=2S'+1`; it does not
  require the new source also to satisfy `S'+1<t`. Thus (L1) uses the actual
  upstream induction hypothesis correctly.

- **Whole-window deletion.** Reversing the unchanged prefix gives exactly
  `q'=q+2^E(v-u)/3^i`. Since 2 and 3 are coprime, its integrality condition
  is exactly `3^i | (v-u)`. For `v>u`, q' is positive and larger, and its
  difference from q is divisible by `2^E`. Hence all first E shortcut parity
  decisions agree; the computed terminal endpoint v is odd, so the literal
  accelerated gaps are exact too. The actual suffix remains complete and
  the nonempty removed block strictly reduces the grade. Equality of the
  endpoints likewise gives a forbidden lower-grade certificate. These facts
  prove (L3). Below q, a nonzero endpoint difference divisible by `3^i`
  forces `3^i<q`, giving (L4).

- **Gap-four endpoint obstruction.** At an odd `v=7 mod9`, the only legal
  positive gap at most three is two. Its parent `(4v-1)/3` is divisible by
  three and has no further odd parent. The complete restricted inverse
  language is therefore exactly the empty word and `[2]`. The identities
  `I_4(v)=4 I_2(v)+1` and their difference `4v` give the claimed failure
  to transport this replacement through any nonempty fixed prefix. The
  powered-source bound follows from `8 I_2(v)=2 I_4(v)-2`.

- **Concrete ordinary control.** All seven displayed gaps on
  `49 -> 37 -> 7 -> 11 -> 17 -> 13 -> 5 -> 1` were reconstructed by exact
  substitution. Replacing 37 by 9 at the retained initial gap indeed asks
  for `35/3`. The example is correctly not labeled as the joint minimum.

- **Unbounded positive carry.** Subtracting the two exact inverse identities
  gives (L7). With nonnegative new power and a positive old carry, its
  numerator is positive; simultaneous ordinary integrality makes the next
  carry a positive integer. Thus every legal update in this stated class
  retains a positive carry. If the source-end power fits the allowed initial
  exponent, the new powered source is `S-2^e c`. Its capture condition is
  exactly the original-slack inequality (L9).

## Scope

No altered certificate is accepted solely from a smaller formal grade.
The proof explicitly retains ordinary integrality, complete tails and the
same original target. It does not rule out negative powers, coordinated
edits of several regions, moving the common suffix, or a different target
merger. The previously proved target odd surplus is recorded as an input;
the note correctly does not assert that it pays (L2) or (L9). No new Lean
execution or universal descent theorem is claimed.
