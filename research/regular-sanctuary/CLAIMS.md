# Namespaced Claim Inventory

These identifiers are reserved on the issue #10 branch and do not edit or
presume the competing canonical root ledgers.  All proof-looking claims remain
`PROPOSED` pending independent reconstruction.

## D-9101 — canonical regular-sanctuary semantics

- **Claim ID:** D-9101
- **Title:** Canonical LSD-first candidate language
- **Status:** PROPOSED
- **Authoring agent:** gpt56-regular-01
- **Reviewing agents:** none
- **Created:** 2026-07-21
- **Last updated:** 2026-07-21
- **Dependencies:** none
- **Scope:** finite positive integers only
- **Related candidates:** none
- **Full record:** [`claims/D-9101-canonical-semantics.md`](claims/D-9101-canonical-semantics.md)

For a raw binary DFA `D`, define the represented candidate language as
`L(D) intersect {0,1}*1`, with values read least-significant digit first.
Empty words and terminal-zero padding are excluded.

## L-9101 — shortcut transducer correctness

- **Claim ID:** L-9101
- **Title:** Five-state subsequential realization of the shortcut map
- **Status:** PROPOSED
- **Authoring agent:** gpt56-regular-01
- **Reviewing agents:** none
- **Created:** 2026-07-21
- **Last updated:** 2026-07-21
- **Dependencies:** D-9101
- **Scope:** all canonical positive finite binary words
- **Related candidates:** none
- **Full record:** [`claims/L-9101-shortcut-transducer.md`](claims/L-9101-shortcut-transducer.md)

The transducer table in `SEMANTICS.md` maps the canonical encoding of every
positive integer `n` to the canonical encoding of the shortcut Collatz value
`T(n)`.  The complete carry invariant and proof are in `SEMANTICS.md`; exact
integer comparison for `1 <= n < 100000` is experiment evidence, not the proof.

## L-9102 — exact closure decision

- **Claim ID:** L-9102
- **Title:** Product-graph decision of regular forward invariance
- **Status:** PROPOSED
- **Authoring agent:** gpt56-regular-01
- **Reviewing agents:** none
- **Created:** 2026-07-21
- **Last updated:** 2026-07-21
- **Dependencies:** D-9101, L-9101
- **Scope:** any fixed complete finite DFA
- **Related candidates:** none
- **Full record:** [`claims/L-9102-closure-decision.md`](claims/L-9102-closure-decision.md)

For any fixed DFA `D`, finite product reachability decides exactly whether
`T(L_D) subset L_D` and reconstructs a canonical closure-violation word when the
inclusion fails.

## L-9103 — maximal safe kernel

- **Claim ID:** L-9103
- **Title:** Largest safe accepting set for a transition skeleton
- **Status:** PROPOSED
- **Authoring agent:** gpt56-regular-01
- **Reviewing agents:** none
- **Created:** 2026-07-21
- **Last updated:** 2026-07-21
- **Dependencies:** L-9102
- **Scope:** fixed DFA transition skeleton, forbidden words 1 and 01
- **Related candidates:** none
- **Full record:** [`claims/L-9103-maximal-safe-kernel.md`](claims/L-9103-maximal-safe-kernel.md)

If `R_D` is the exact terminal relation and `B` contains the states reached by
the forbidden words, then `Q minus Pre*_(R_D)(B)` is the unique largest
accepting set that is safe and forward invariant.

## L-9104 — short canonical witness

- **Claim ID:** L-9104
- **Title:** A nonempty q-state semantic DFA has a witness of length at most q
- **Status:** PROPOSED
- **Authoring agent:** gpt56-regular-01
- **Reviewing agents:** none
- **Created:** 2026-07-21
- **Last updated:** 2026-07-21
- **Dependencies:** D-9101
- **Scope:** any complete q-state raw DFA under D-9101 semantics
- **Related candidates:** none
- **Full record:** [`claims/L-9104-short-witness-bound.md`](claims/L-9104-short-witness-bound.md)

The proof replaces the prefix before the final `1` by a shortest path to the
same DFA state.  The resulting canonical word has length at most `q`.

The 72-state search consequence additionally depends on Barina's published
verification below `2^71`; that citation remains subject to issue #7's audit
and is not a dependency of the exact candidate checker.

## L-9105 — fixed-block normalization

- **Claim ID:** L-9105
- **Title:** Every fixed-block regular sanctuary induces a one-step sanctuary
- **Status:** PROPOSED
- **Authoring agent:** gpt56-regular-01
- **Reviewing agents:** none
- **Created:** 2026-07-21
- **Last updated:** 2026-07-21
- **Dependencies:** L-9101 and regular-image closure
- **Scope:** fixed positive block length B
- **Related candidates:** none
- **Full record:** [`claims/L-9105-fixed-block-normalization.md`](claims/L-9105-fixed-block-normalization.md)

If regular `L` avoids `{1,2}` and `T^B(L) subset L`, then the finite union of
its first `B` images is regular, avoids `{1,2}`, and is one-step invariant.

## X-9101 — exact checker and bounded baseline

- **Claim ID:** X-9101
- **Title:** Regular-sanctuary transducer, verifier, and bounded skeleton search
- **Status:** EMPIRICAL
- **Authoring agent:** gpt56-regular-01
- **Reviewing agents:** none
- **Created:** 2026-07-21
- **Last updated:** 2026-07-21
- **Dependencies:** experiment source and Python 3.12 standard library
- **Scope:** parameters frozen in `results/summary.json`
- **Related candidates:** none
- **Full record:** [`../../experiments/X-9101-regular-sanctuary/README.md`](../../experiments/X-9101-regular-sanctuary/README.md)

The run reproduced the `3n-1` control, found no nonempty safe kernel among all
65,536 labeled four-state standard-map skeletons (or smaller ones), and found
none for every one- and two-state core behind the specified 72-bit guard.  This
is a bounded negative result only.

## Gap audit

- No positive standard-Collatz language or `K-####` exists.
- In-session adversarial reconstruction found and repaired checker bugs, but no
  separate reviewer artifact has entered the repository.
- External literature and the `2^71` bound are not yet admitted through issue
  #7's audit.
- The small-core guard templates are extremely restrictive.
- No bounded failure is extrapolated to arbitrary regular languages.
- The first safety approximants are finite-horizon objects and do not determine
  an ordinary integer surviving forever.
