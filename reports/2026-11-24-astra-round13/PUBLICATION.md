# Publication checkpoints

All publication uses PR182's existing research branch
`research/dyadic-band-descent-20261121`, with an expected previous head
and a non-forced ref update. No merge to the default branch is performed.

## First scientific checkpoint

- Parent: `cbec52dde5bed390a693310dd04e911033ba0cc9`.
- Published commit: `cf1f04db7f9f84d3a31bfccf2546431b711312d0`.
- Tree: `865d198cb4d01b2571391e84bffd1e14052b6f2f`.
- 49 changed/added paths; 728 total tracked files.
- Every uploaded blob was checked against its native Git blob hash.
  The remote tree exactly matched `git write-tree` in the complete
  local checkout.
- The remote commit object was reconstructed byte-for-byte from its
  metadata, including the original `+0200` author/committer timezone.
  Its native Git object hash matched the remote commit SHA. An initial
  attempt assuming `+0000` failed to reconstruct the object; the
  validator correctly refused that still-dirty checkout. No successful
  validation is attributed to that preliminary attempt.
- The exact resulting complete checkout passed all five default
  validation commands, clean before and after. Full receipt:
  [SCIENCE_CHECKOUT_VALIDATION.json](SCIENCE_CHECKOUT_VALIDATION.json).
- The branch ref update returned success. A stale normalized PR response
  initially showed the parent; separate direct ref and PR API readbacks
  both confirmed `cf1f04d...` as the new published head. The current title
  and Round 13 body were then updated and read back.
- `MarkedHalfReturn.lean` was fetched at the published commit and matched
  the uploaded source exactly, blob
  `124866c94e3052ae7d27c5d06891d48b3cc9df89`. All 32 entries in the first
  source manifest matched the clean local checkout.

The first checkpoint contains the initial finite Lean receipt (15
compilations, 79 named audits), nine normal/optimized finite programs,
the source-specific reviews and the scientific packet. Subsequent
freshness deductions and their verification are identified separately.

## Follow-up checkpoint contents

The follow-up adds the exact-head first-checkpoint receipt, three frozen
freshness notes with new mathematical deductions, the guarded-predecessor
module, and the mixed-top rational fixture. Its consolidated replay has
16 successful Lean compilations, 82 named axiom audits and 20 successful
finite-program executions. The first checkpoint's raw evidence and
source manifest are retained; the updated inputs have a separate final
manifest and separate follow-up receipts.

The final commit and tree are recorded in the live PR's exact-head
receipt after the object exists. No self-referential commit identifier
is embedded in this file.

## Evidence boundaries

Repository validation checks structure, frozen identities and its named
finite self-tests. It does not prove Collatz or validate the unformalized
infinite arguments. Compiler receipts bind specific Lean bytes and
declarations. A publication readback establishes that those bytes are
available at the recorded remote identity.

The final head is reported in the PR metadata with its own complete
checkout receipt. A receipt stored inside a Git commit necessarily names
an earlier commit; the PR's exact-head receipt avoids a circular hash.
