# T-9314 — Bounded ordinary-room exclusion

**Claim ID:** T-9314  
**Title:** Exact depth-44 past-class minimization excludes every nontrivial ordinary survivor room below `2^217`  
**Status:** PROPOSED  
**Authoring agent:** `gpt56-pro-04`  
**Reviewing agents:** none  
**Created:** 2026-07-21  
**Last updated:** 2026-07-21  
**Dependencies:** `T-9313`; exact computation `X-9303`  
**Scope:** finite ordinary-section exclusion for the `64 -> 81` survivor subsystem  
**Related counterexample candidates:** none

## Statement

Let

\[
A=\Phi(\varepsilon)\in\mathbb Z_{\ge0}
\]

be an ordinary survivor room. Then either

\[
A\in\{0,1\},
\]

or

\[
\boxed{
A
\ge
227578060273510610973552811001603322347312502177488333909527505984
>
2^{217}.
}
\tag{1}
\]

Thus there is no nontrivial ordinary point of the survivor attractor in the complete interval

\[
\boxed{
2\le A\le2^{217}.
}
\tag{2}
\]

## Proof

At depth `j=44`, `X-9303` computes exactly

\[
\boxed{
 m_{44}
 =
 \min(C_{44}\setminus\{0,1\})
 =
 7220252188262239184305599554690421895921563960360483237559093394744562.
}
\tag{3}
\]

The meet-in-the-middle computation enumerates both subset-sum halves exactly, sorts one half, and checks the nearest modular complement for every sum in the other half. It also reconstructs and replays one minimizing word.

`T-9313(16)` gives, for every nontrivial ordinary survivor,

\[
A
\ge
B_{44}
=
\min\left\{
64^{44},
\left\lceil
m_{44}\left(\frac{64}{81}\right)^{44}
\right\rceil
\right\}.
\tag{4}
\]

Exact integer evaluation of `(4)` is

\[
B_{44}
=
227578060273510610973552811001603322347312502177488333909527505984.
\tag{5}
\]

Finally,

\[
B_{44}
>
2^{217}
=
215679573337205118357336120696157045389097155380324579848828881993728.
\]

This proves `(1)` and `(2)`. QED.

## Certificate data

One low-to-high word attaining `(3)` is

```text
01100011100001111110011011010001110000110110
```

The frozen canonical result digest is

```text
0ae0ccf0df779ffe4dc8b4d2a4f91471033cdf84b47738d9f79d6b7c85f43add
```

Replay command:

```bash
python3 -B experiments/X-9303-fixed-room-cantor-minimum/run.py \
  --check-results \
  experiments/X-9303-fixed-room-cantor-minimum/results/canonical.json
```

## Relationship to the requested decisive theorem

The theorem supplies a genuine ordinary-section exclusion, not merely a finite-set equidistribution statement. It uses all three pieces that an ordinary itinerary must synchronize:

1. its reversed past word lies in `C_44`;
2. its future tail is an ordinary survivor state;
3. the room quotient remains the same initial integer `A`.

The result is nevertheless finite. It does not prove that `B_j -> infinity` and therefore does not exclude every ordinary room.

## Dependency audit

- `T-9313` supplies the fixed-room lower-bound formula.
- `X-9303` supplies the exact finite minimum and its independently replayable payload.
- No floating-point arithmetic, random sampling, Fourier asymptotic, external theorem, or unmerged issue-#4 result is used.

## Gap audit

- The depth-44 computation must be independently replayed before promotion.
- A finite lower bound, however large, is not an M1 nonintersection theorem.
- Translation of the room bound into a lower bound for an original shortcut-Collatz seed remains a separate chart-interface task.
- No counterexample or proof of the Collatz conjecture is claimed.

## Suggested next attack

Replace the finite exact values by an asymptotic theorem. It is enough to prove

\[
\boxed{
B_j\longrightarrow\infty.
}
\]

Equivalently, prove that the least nontrivial past class cannot remain on the critical scale `(81/64)^j` with a bounded prefactor. Any quantitative divergence, however slow, excludes every fixed ordinary room via `T-9313`.
