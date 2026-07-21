# R-9301 — Refutation of exact-prefix interval amplification

**Claim ID:** R-9301  
**Title:** One exact reciprocal carry prefix cannot persist on a nontrivial consecutive frequency interval  
**Status:** PROPOSED  
**Authoring agent:** `gpt56-pro-04`  
**Reviewing agents:** none  
**Created:** 2026-07-21  
**Last updated:** 2026-07-21  
**Dependencies:** `L-9309`  
**Scope:** methodological obstruction for exceptional-frequency amplification  
**Related counterexample candidates:** none

## Statement

Fix `K>=1` and an exact reciprocal-chain prefix of length `L>=1` in the sense of `L-9309`.

The set of integers realizing that prefix is exactly one arithmetic progression

\[
\boxed{
h=h_0+m81^L,
\qquad m\in\mathbb Z.}
\tag{1}
\]

Consequently:

1. no two consecutive integers realize the same nonempty exact prefix;
2. every interval of length less than `81^L` contains at most one realizing frequency;
3. an exact prefix cannot by itself produce a consecutive interval of large Fourier coefficients;
4. any amplification proof based on a single exceptional frequency must use approximate phase margins, a union of many exact prefixes, or a theorem transferring arithmetic-progression mass to consecutive blocks.

Thus the tentative statement

> “one exact length-`L` carry pattern persists on a consecutive neighborhood of its frequency”

is refuted for every `L>=1`.

This refutation does **not** rule out the broader exceptional-frequency amplification program. It rules out only its naive exact-prefix/Euclidean-neighborhood version.

## Motivation

`T-9301` reduces all-depth EQ to a growing low-frequency window, and the issue-#4 frequency theorem controls consecutive blocks. A natural proposed bridge was:

1. a large coefficient forces a low-complexity carry pattern;
2. nearby numerators preserve that pattern;
3. a whole consecutive block is therefore large;
4. the block mean gives a contradiction.

`L-9309` shows that step 2 is false for an **exact** carry prefix. Exact symbolic stability is `81`-adic, not Euclidean: the prefix lives on one class modulo `81^L`.

The distinction is important. Low phase energy is an approximate condition and may correspond to a large union of exact cylinders. The correct theorem must count and organize that union rather than promote one cylinder into an interval.

## Proof / refutation

By `L-9309(10)`, fixing a length-`L` prefix selects exactly one residue class

\[
h\equiv h_0\pmod{81^L}.
\]

This is precisely `(1)`.

If two consecutive integers `h` and `h+1` realized the prefix, then

\[
81^L\mid1,
\]

which is impossible for `L>=1`.

More generally, two distinct realizing integers differ by at least `81^L` in absolute value. Hence every interval of length less than `81^L` contains at most one. This proves all four conclusions. QED.

## Dependency audit

- `L-9309` supplies the exact prefix/residue-class bijection.
- No Fourier estimate, block theorem, computation, or asymptotic argument is used.
- The refuted proposal is methodological and deliberately narrow.

## Gap audit

- Approximate low-energy patterns are unions of exact cylinders and may still contain consecutive intervals.
- A long interval contains many points of one arithmetic progression; the obstruction is to **consecutive local persistence**, not global repetition.
- A block theorem for arithmetic progressions could revive exact-prefix amplification in another form.
- The result does not show that exceptional frequencies exist.
- The result has no implication for the truth of Collatz.

## Adversarial tests

1. At `L=1`, one prefix is one residue class modulo `81`; adjacent integers have different `q_0`.
2. At `L=2`, the spacing is `81^2`, although the two frequencies may be close relative to a much larger global search range.
3. The empty prefix `L=0` is excluded; it is realized by every integer.
4. A union of all `81^L` prefixes is the whole integer set, showing why approximate unions require separate counting.

## Remaining uncertainty

None for the stated exact-prefix obstruction. The open question is how many exact cylinders can satisfy a given low-energy inequality and how their residue classes are distributed.

## Suggested next attack

Fix an energy budget `E` and a prefix length `L`. Bound the number of lift-digit tuples whose first `L` cosine losses total at most `E`. Then study whether the associated residue classes modulo `81^L` can cluster in a short interval or must be equidistributed enough for a block contradiction.