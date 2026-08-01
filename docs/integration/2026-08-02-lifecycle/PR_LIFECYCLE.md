# PR lifecycle and integration-disposition ledger

**Population:** the 45 source PRs open at the immutable cutoff `2026-08-01T21:16:40Z`  
**Frozen main:** `0ae0c67bb058f9a7c56cc7744fe5bf2650a7cb84`  
**Continuation observation:** `2026-08-01T22:18:52Z` / `2026-08-02T01:18:52+03:00`  
**Boundary:** advisory only; no source PR was merged or closed.

Review verdict and repository action are separate. A passing theorem can still require extraction or dependency repair; a rejected monolith can contain durable refutations or salvageable lemmas.

## Disposition vocabulary

- `CANONICALIZED BY REFERENCE`
- `CLEAN EXTRACTION REQUIRED`
- `MERGE CANDIDATE AFTER FIXES`
- `PRESERVE AS RESEARCH/REFERENCE`
- `CONTINUE ACTIVE DEVELOPMENT`
- `DEFER PENDING REVIEW`
- `DEFER PENDING DEPENDENCY OR REPAIR`
- `SUPERSEDED/ABSORBED`
- `REJECT/CLOSE CANDIDATE`
- `UNREVIEWED`
- `MIXED—CLAIM-LEVEL ACTION REQUIRED`

## Recommended-action vocabulary

- `KEEP OPEN`
- `IMPORT CLEAN PACKET THEN CLOSE`
- `MERGE AFTER REVIEWED FIX`
- `CLOSE AS SUPERSEDED WITH DURABLE POINTER`
- `CLOSE AS REJECTED WHILE PRESERVING REFUTATIONS`
- `NO ACTION UNTIL REVIEW`

## Counts

| Disposition | Count |
|---|---:|
| CANONICALIZED BY REFERENCE | 11 |
| CLEAN EXTRACTION REQUIRED | 5 |
| CONTINUE ACTIVE DEVELOPMENT | 4 |
| DEFER PENDING DEPENDENCY OR REPAIR | 6 |
| DEFER PENDING REVIEW | 2 |
| MERGE CANDIDATE AFTER FIXES | 6 |
| MIXED—CLAIM-LEVEL ACTION REQUIRED | 4 |
| PRESERVE AS RESEARCH/REFERENCE | 2 |
| REJECT/CLOSE CANDIDATE | 1 |
| SUPERSEDED/ABSORBED | 1 |
| UNREVIEWED | 3 |

| Recommended action | Count |
|---|---:|
| CLOSE AS REJECTED WHILE PRESERVING REFUTATIONS | 1 |
| CLOSE AS SUPERSEDED WITH DURABLE POINTER | 2 |
| IMPORT CLEAN PACKET THEN CLOSE | 22 |
| KEEP OPEN | 8 |
| MERGE AFTER REVIEWED FIX | 7 |
| NO ACTION UNTIL REVIEW | 5 |

## All 45 source PRs

| PR | Verdict | Primary disposition | Recommended action | Integrated records | Detail |
|---:|---|---|---|---|---|
| [#3](https://github.com/GettysburgResearch/collatz/pull/3) | VERIFIED WITH FIXES | CANONICALIZED BY REFERENCE | IMPORT CLEAN PACKET THEN CLOSE | IC-EXTRACT-001 (alternative source PR3:T-0043) | [`A-03-20`](pr-lifecycle/A-03-20.md#pr-3) |
| [#6](https://github.com/GettysburgResearch/collatz/pull/6) | VERIFIED WITH FIXES | MERGE CANDIDATE AFTER FIXES | MERGE AFTER REVIEWED FIX | — | [`A-03-20`](pr-lifecycle/A-03-20.md#pr-6) |
| [#11](https://github.com/GettysburgResearch/collatz/pull/11) | REJECTED | REJECT/CLOSE CANDIDATE | CLOSE AS REJECTED WHILE PRESERVING REFUTATIONS | — | [`A-03-20`](pr-lifecycle/A-03-20.md#pr-11) |
| [#12](https://github.com/GettysburgResearch/collatz/pull/12) | VERIFIED WITH FIXES | CONTINUE ACTIVE DEVELOPMENT | KEEP OPEN | — | [`A-03-20`](pr-lifecycle/A-03-20.md#pr-12) |
| [#13](https://github.com/GettysburgResearch/collatz/pull/13) | VERIFIED WITH FIXES | CONTINUE ACTIVE DEVELOPMENT | KEEP OPEN | — | [`A-03-20`](pr-lifecycle/A-03-20.md#pr-13) |
| [#14](https://github.com/GettysburgResearch/collatz/pull/14) | VERIFIED | CANONICALIZED BY REFERENCE | IMPORT CLEAN PACKET THEN CLOSE | IC-AUT-001 | [`A-03-20`](pr-lifecycle/A-03-20.md#pr-14) |
| [#16](https://github.com/GettysburgResearch/collatz/pull/16) | VERIFIED WITH FIXES | CLEAN EXTRACTION REQUIRED | IMPORT CLEAN PACKET THEN CLOSE | — | [`A-03-20`](pr-lifecycle/A-03-20.md#pr-16) |
| [#19](https://github.com/GettysburgResearch/collatz/pull/19) | GAP/BLOCKED | MIXED—CLAIM-LEVEL ACTION REQUIRED | IMPORT CLEAN PACKET THEN CLOSE | — | [`A-03-20`](pr-lifecycle/A-03-20.md#pr-19) |
| [#20](https://github.com/GettysburgResearch/collatz/pull/20) | VERIFIED WITH FIXES | MERGE CANDIDATE AFTER FIXES | MERGE AFTER REVIEWED FIX | — | [`A-03-20`](pr-lifecycle/A-03-20.md#pr-20) |
| [#32](https://github.com/GettysburgResearch/collatz/pull/32) | VERIFIED | CLEAN EXTRACTION REQUIRED | IMPORT CLEAN PACKET THEN CLOSE | — | [`B-32-50`](pr-lifecycle/B-32-50.md#pr-32) |
| [#33](https://github.com/GettysburgResearch/collatz/pull/33) | VERIFIED | MERGE CANDIDATE AFTER FIXES | MERGE AFTER REVIEWED FIX | — | [`B-32-50`](pr-lifecycle/B-32-50.md#pr-33) |
| [#34](https://github.com/GettysburgResearch/collatz/pull/34) | GAP/BLOCKED | MIXED—CLAIM-LEVEL ACTION REQUIRED | IMPORT CLEAN PACKET THEN CLOSE | — | [`B-32-50`](pr-lifecycle/B-32-50.md#pr-34) |
| [#35](https://github.com/GettysburgResearch/collatz/pull/35) | VERIFIED WITH FIXES | PRESERVE AS RESEARCH/REFERENCE | IMPORT CLEAN PACKET THEN CLOSE | — | [`B-32-50`](pr-lifecycle/B-32-50.md#pr-35) |
| [#37](https://github.com/GettysburgResearch/collatz/pull/37) | VERIFIED WITH FIXES | CANONICALIZED BY REFERENCE | IMPORT CLEAN PACKET THEN CLOSE | IC-REF-001, IC-REP-001 | [`B-32-50`](pr-lifecycle/B-32-50.md#pr-37) |
| [#38](https://github.com/GettysburgResearch/collatz/pull/38) | VERIFIED WITH FIXES | PRESERVE AS RESEARCH/REFERENCE | CLOSE AS SUPERSEDED WITH DURABLE POINTER | — | [`B-32-50`](pr-lifecycle/B-32-50.md#pr-38) |
| [#42](https://github.com/GettysburgResearch/collatz/pull/42) | GAP/BLOCKED | MIXED—CLAIM-LEVEL ACTION REQUIRED | IMPORT CLEAN PACKET THEN CLOSE | — | [`B-32-50`](pr-lifecycle/B-32-50.md#pr-42) |
| [#44](https://github.com/GettysburgResearch/collatz/pull/44) | VERIFIED | DEFER PENDING DEPENDENCY OR REPAIR | IMPORT CLEAN PACKET THEN CLOSE | — | [`B-32-50`](pr-lifecycle/B-32-50.md#pr-44) |
| [#45](https://github.com/GettysburgResearch/collatz/pull/45) | VERIFIED WITH FIXES | CLEAN EXTRACTION REQUIRED | IMPORT CLEAN PACKET THEN CLOSE | — | [`B-32-50`](pr-lifecycle/B-32-50.md#pr-45) |
| [#47](https://github.com/GettysburgResearch/collatz/pull/47) | GAP/BLOCKED | MIXED—CLAIM-LEVEL ACTION REQUIRED | IMPORT CLEAN PACKET THEN CLOSE | — | [`B-32-50`](pr-lifecycle/B-32-50.md#pr-47) |
| [#48](https://github.com/GettysburgResearch/collatz/pull/48) | VERIFIED WITH FIXES | MERGE CANDIDATE AFTER FIXES | MERGE AFTER REVIEWED FIX | — | [`B-32-50`](pr-lifecycle/B-32-50.md#pr-48) |
| [#49](https://github.com/GettysburgResearch/collatz/pull/49) | VERIFIED WITH FIXES | DEFER PENDING DEPENDENCY OR REPAIR | KEEP OPEN | — | [`B-32-50`](pr-lifecycle/B-32-50.md#pr-49) |
| [#50](https://github.com/GettysburgResearch/collatz/pull/50) | VERIFIED WITH FIXES | CLEAN EXTRACTION REQUIRED | IMPORT CLEAN PACKET THEN CLOSE | — | [`B-32-50`](pr-lifecycle/B-32-50.md#pr-50) |
| [#51](https://github.com/GettysburgResearch/collatz/pull/51) | VERIFIED WITH FIXES | CONTINUE ACTIVE DEVELOPMENT | KEEP OPEN | — | [`C-51-64`](pr-lifecycle/C-51-64.md#pr-51) |
| [#53](https://github.com/GettysburgResearch/collatz/pull/53) | VERIFIED WITH FIXES | DEFER PENDING DEPENDENCY OR REPAIR | KEEP OPEN | — | [`C-51-64`](pr-lifecycle/C-51-64.md#pr-53) |
| [#56](https://github.com/GettysburgResearch/collatz/pull/56) | VERIFIED WITH FIXES | CANONICALIZED BY REFERENCE | IMPORT CLEAN PACKET THEN CLOSE | IC-EXTRACT-001 (alternative source PR56:T-7801) | [`C-51-64`](pr-lifecycle/C-51-64.md#pr-56) |
| [#57](https://github.com/GettysburgResearch/collatz/pull/57) | VERIFIED WITH FIXES | CANONICALIZED BY REFERENCE | IMPORT CLEAN PACKET THEN CLOSE | IC-EXTRACT-001 (primary source), IC-GHOST-001 | [`C-51-64`](pr-lifecycle/C-51-64.md#pr-57) |
| [#60](https://github.com/GettysburgResearch/collatz/pull/60) | VERIFIED WITH FIXES | CANONICALIZED BY REFERENCE | IMPORT CLEAN PACKET THEN CLOSE | IC-EXTRACT-001 (alternative source PR60:T-7401) | [`C-51-64`](pr-lifecycle/C-51-64.md#pr-60) |
| [#61](https://github.com/GettysburgResearch/collatz/pull/61) | VERIFIED WITH FIXES | CANONICALIZED BY REFERENCE | IMPORT CLEAN PACKET THEN CLOSE | IC-PERIODIC-001 (source; corrected integration statement) | [`C-51-64`](pr-lifecycle/C-51-64.md#pr-61) |
| [#62](https://github.com/GettysburgResearch/collatz/pull/62) | VERIFIED | CANONICALIZED BY REFERENCE | IMPORT CLEAN PACKET THEN CLOSE | IC-PERIODIC-001 (supercritical firewall source) | [`C-51-64`](pr-lifecycle/C-51-64.md#pr-62) |
| [#63](https://github.com/GettysburgResearch/collatz/pull/63) | VERIFIED WITH FIXES | CANONICALIZED BY REFERENCE | IMPORT CLEAN PACKET THEN CLOSE | IC-PERIODIC-001 (fixed-point/escape source) | [`C-51-64`](pr-lifecycle/C-51-64.md#pr-63) |
| [#64](https://github.com/GettysburgResearch/collatz/pull/64) | VERIFIED WITH FIXES | CANONICALIZED BY REFERENCE | IMPORT CLEAN PACKET THEN CLOSE | IC-RIG-001 | [`C-51-64`](pr-lifecycle/C-51-64.md#pr-64) |
| [#65](https://github.com/GettysburgResearch/collatz/pull/65) | VERIFIED WITH FIXES | DEFER PENDING REVIEW | NO ACTION UNTIL REVIEW | — | [`D-65-74`](pr-lifecycle/D-65-74.md#pr-65) |
| [#66](https://github.com/GettysburgResearch/collatz/pull/66) | VERIFIED WITH FIXES | MERGE CANDIDATE AFTER FIXES | MERGE AFTER REVIEWED FIX | — | [`D-65-74`](pr-lifecycle/D-65-74.md#pr-66) |
| [#67](https://github.com/GettysburgResearch/collatz/pull/67) | UNREVIEWED | UNREVIEWED | NO ACTION UNTIL REVIEW | — | [`D-65-74`](pr-lifecycle/D-65-74.md#pr-67) |
| [#68](https://github.com/GettysburgResearch/collatz/pull/68) | UNREVIEWED | UNREVIEWED | NO ACTION UNTIL REVIEW | — | [`D-65-74`](pr-lifecycle/D-65-74.md#pr-68) |
| [#69](https://github.com/GettysburgResearch/collatz/pull/69) | UNREVIEWED | UNREVIEWED | NO ACTION UNTIL REVIEW | — | [`D-65-74`](pr-lifecycle/D-65-74.md#pr-69) |
| [#70](https://github.com/GettysburgResearch/collatz/pull/70) | VERIFIED WITH FIXES | DEFER PENDING DEPENDENCY OR REPAIR | KEEP OPEN | — | [`D-65-74`](pr-lifecycle/D-65-74.md#pr-70) |
| [#72](https://github.com/GettysburgResearch/collatz/pull/72) | VERIFIED WITH FIXES | CLEAN EXTRACTION REQUIRED | IMPORT CLEAN PACKET THEN CLOSE | — | [`D-65-74`](pr-lifecycle/D-65-74.md#pr-72) |
| [#74](https://github.com/GettysburgResearch/collatz/pull/74) | VERIFIED WITH FIXES (PRIVATE BASELINE); PUBLICATION GAP/BLOCKED | SUPERSEDED/ABSORBED | CLOSE AS SUPERSEDED WITH DURABLE POINTER | — | [`D-65-74`](pr-lifecycle/D-65-74.md#pr-74) |
| [#76](https://github.com/GettysburgResearch/collatz/pull/76) | VERIFIED WITH FIXES | MERGE CANDIDATE AFTER FIXES | MERGE AFTER REVIEWED FIX | — | [`E-76-83`](pr-lifecycle/E-76-83.md#pr-76) |
| [#77](https://github.com/GettysburgResearch/collatz/pull/77) | VERIFIED WITH FIXES | CANONICALIZED BY REFERENCE | IMPORT CLEAN PACKET THEN CLOSE | IC-SC-001, RD-SC-001 | [`E-76-83`](pr-lifecycle/E-76-83.md#pr-77) |
| [#79](https://github.com/GettysburgResearch/collatz/pull/79) | VERIFIED WITH FIXES | DEFER PENDING DEPENDENCY OR REPAIR | MERGE AFTER REVIEWED FIX | — | [`E-76-83`](pr-lifecycle/E-76-83.md#pr-79) |
| [#80](https://github.com/GettysburgResearch/collatz/pull/80) | VERIFIED WITH FIXES | DEFER PENDING DEPENDENCY OR REPAIR | KEEP OPEN | — | [`E-76-83`](pr-lifecycle/E-76-83.md#pr-80) |
| [#81](https://github.com/GettysburgResearch/collatz/pull/81) | VERIFIED WITH FIXES | CONTINUE ACTIVE DEVELOPMENT | KEEP OPEN | RD-FC-001 (roadmap architecture only) | [`E-76-83`](pr-lifecycle/E-76-83.md#pr-81) |
| [#83](https://github.com/GettysburgResearch/collatz/pull/83) | VERIFIED WITH FIXES | DEFER PENDING REVIEW | NO ACTION UNTIL REVIEW | RD-FC-001 (roadmap factor-synchronization source only) | [`E-76-83`](pr-lifecycle/E-76-83.md#pr-83) |

## Machine-readable ledger

- [`pr-lifecycle.json`](pr-lifecycle.json) — metadata, vocabularies, counts, and part index.
- [`A-03-20`](pr-lifecycle/records-A-03-20.json) — PRs #3, #6, #11, #12, #13, #14, #16, #19, #20.
- [`B-32-50`](pr-lifecycle/records-B-32-50.json) — PRs #32, #33, #34, #35, #37, #38, #42, #44, #45, #47, #48, #49, #50.
- [`C-51-64`](pr-lifecycle/records-C-51-64.json) — PRs #51, #53, #56, #57, #60, #61, #62, #63, #64.
- [`D-65-74`](pr-lifecycle/records-D-65-74.json) — PRs #65, #66, #67, #68, #69, #70, #72, #74.
- [`E-76-83`](pr-lifecycle/records-E-76-83.json) — PRs #76, #77, #79, #80, #81, #83.

## Interpretation

The primary disposition is the dominant next integration treatment. `secondary_dispositions` in the machine record preserve additional truths, such as a branch being both referenced canonically and still requiring a clean extraction. The action field is a recommendation, not an action already taken.

Before any future closure, follow the row’s `durable_destination_before_closure` and `closure_criteria`. A closure comment must point to the imported packet, archive manifest, successor issue/PR, and exact frozen review.
