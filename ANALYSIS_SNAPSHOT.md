# Analysis snapshot

**Agent:** `gpt56-cartographer-01`  
**Issue:** [#36](https://github.com/gfreund123/collatz/issues/36)  
**Purpose:** immutable provenance for `GLOBAL_COUNTEREXAMPLE_MAP.md`

> This file is finalized immediately before the cartography commit. Branches in this repository move rapidly; statements in the map are scoped to the exact heads below.

## Cutoff

- Repository: `gfreund123/collatz`
- Requested name: `gideonf123/collatz`; resolved to the connected private project above
- Main commit: `b40e5c44959b20842e6c064084c668f5243b6ebd`
- Cutoff UTC: `2026-07-22T15:17:37Z`
- Cutoff Asia/Jerusalem: `2026-07-22T18:17:37+03:00`
- Issue range enumerated: `#1` through `#36`
- Proof policy: no independent proof verification; source statuses preserved, with newer refutations and stricter labels taking precedence

## Open/merged pull-request heads

| PR | State | Head SHA at cutoff | Updated at |
|---:|---|---|---|
| #1 | merged | `a332b517397eaedd98fc4b5bee8e98494d2cfbb2` | `2026-07-21T07:01:49Z` |
| #3 | open draft | `537e1cab2e8dacc444e973e730daa463273bab6f` | `2026-07-22T15:06:39Z` |
| #6 | open draft | `4810a0771da61a1cb609ef8707dfcf7f0f6e666f` | `2026-07-21T15:17:07Z` |
| #11 | open draft | `7950713cbb6ba0af0a424806cc36ce01ad24cf9e` | `2026-07-21T15:17:23Z` |
| #12 | open draft | `7ea63c56c423f09b856818fc8a051c9d064d8eae` | `2026-07-21T16:42:34Z` |
| #13 | open draft | `de517c6d157e89d505176bc141f1f52083392e7f` | `2026-07-22T15:15:55Z` |
| #14 | open draft | `9e3d90f50a6bf908401d2a2556513077daca3eb4` | `2026-07-21T15:11:51Z` |
| #16 | open draft | `900ba417c968d8a41bc56a30d3ccc941284d8ce2` | `2026-07-22T14:31:10Z` |
| #19 | open draft | `188e93cd7118495269b545de946a019521e68962` | `2026-07-22T12:11:45Z` |
| #20 | open draft | `82ca2f932438a9fe0897704ba62959ca23ec830f` | `2026-07-22T15:07:00Z` |
| #32 | open draft, based on PR #16 | `bc397f0f4c80cb001493beaebb170ea880f4a114` | `2026-07-22T10:12:31Z` |
| #33 | open draft | `c9d62bce3e93f5785f72e4520bc576863d9379eb` | `2026-07-22T15:09:33Z` |
| #34 | open draft | `c75e11d53595b1b6b2dec03a308a54312212e62d` | `2026-07-22T15:11:18Z` |
| #35 | open draft | `8060aa4d3155d526ab4f6405ef9ecb47fa8107e1` | `2026-07-22T15:13:52Z` |

## Branch-only packets inspected

- Issue #4 symbolic-rewrite branch through its issue thread and reachable commits/files, including commit `3291766ceb1e1bb52b02a2542e11e78ab41c90f2`.
- Issue #21 foundry file blob `71257410f44a4dce3d1a76489b098bb4b304c1e9`.
- Issue #24 solution-cone README blob `73bea1862605144815b427996716804b8a8b106f` and claim-index blob `c3306571cafb2571453abebf54d3b4374c5a81a4`.
- Issue #30 foundations index blob `028981a533cbf29320a59f5fefa6edeebc840412`.
- PR #3 current-state blob `d9c99f1b212cc7b2b6c6f7e0b89452c0354b98c7`.
- PR #33 residue-cylinder README blob `f4826bba8da8ce1b022401e335dfe0246b044c62`.
- PR #34 cross-direction map blob `75ef8025c9a6caed452db879aed105895f2c77e3`.

## Materials covered

- root README / operating constitution;
- every issue and pull request present in the enumerated range;
- current PR bodies and current-state/index files for active mathematical branches;
- issue and PR discussions carrying later status corrections;
- source-audited literature crosswalk;
- independent-review PR #32;
- cross-direction lemma forge and its refutation register.

## Status conflict rule

1. A branch's explicit claim index controls its native status.
2. A later refutation or withdrawal controls dependent edges.
3. Internal same-session review does not become `INDEPENDENTLY_VERIFIED`.
4. Exact finite computations remain `EMPIRICAL`.
5. Literature results are blue only when the source and native hypotheses were inspected.
6. A result may be proved and still be a negative filter rather than a path toward a counterexample.

## Cutoff-changing event

The live refresh discovered PR #33's new proposed `T-9705` full signed-ordinary exclusion for the frozen corrected 256-stage class. The map was revised after reading the current PR head and its residue-cylinder README. Earlier open-cap wording is intentionally superseded in this snapshot.

## Known moving-frontier caveat

Any commit or issue update after the cutoff is outside this snapshot. The next pass should diff heads and claim-index files rather than silently rewriting this provenance.
