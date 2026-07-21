# X-9303 — Exact fixed-room Cantor minimum certificate

**Experiment ID:** X-9303  
**Status:** INTERNAL EXACT COMPUTATION / EMPIRICAL artifact  
**Agent:** `gpt56-pro-04`  
**Issue:** #15  
**Associated claims:** `T-9313`, `T-9314`  
**Date:** 2026-07-21

## Research question

For the depth-`j` triadic past class set

\[
C_j
=\left\{
-17\sum_{r=0}^{j-1}
\frac{81^r}{64^{r+1}}\eta_r
\pmod{81^j}:
\eta_r\in\{0,1\}
\right\},
\]

what is the exact least standard representative other than the two trivial classes `0` and `1`?

`T-9313` proves that if a nontrivial ordinary survivor has initial room `A`, then for every depth `j`

\[
A
\ge
B_j
:=
\min\left\{
64^j,
\left\lceil
m_j(64/81)^j
\right\rceil
\right\},
\qquad
m_j=\min(C_j\setminus\{0,1\}).
\]

Thus any exact computation of `m_j` supplies an independently replayable finite exclusion certificate.

## Algorithm

The class set is a modular subset-sum problem with generators

\[
g_r
\equiv
-17\,81^r64^{-(r+1)}
\pmod{81^j}.
\]

A direct scan costs `2^j` storage and work. The committed script splits the generators into two halves:

1. enumerate and sort all right-half subset sums;
2. enumerate left-half sums in Gray-code order;
3. for each left sum, use binary search to find the least positive combined residue;
4. exclude the two trivial residues `0` and `1`;
5. reconstruct and replay one minimizing binary word.

The work is `O(2^(j/2) log 2^(j/2))` and the storage is `O(2^(j/2))`.

For depths through `16`, the script also performs an independent direct enumeration and requires exact agreement.

## Replay

```bash
python3 -B -m py_compile experiments/X-9303-fixed-room-cantor-minimum/run.py
python3 -B experiments/X-9303-fixed-room-cantor-minimum/run.py \
  --check-results \
  experiments/X-9303-fixed-room-cantor-minimum/results/canonical.json
```

The depth-44 checkpoint sorts `2^22 = 4,194,304` exact integer subset sums. It is intentionally a bounded exact computation, not a large stochastic search.

## Frozen result

At depth `44`,

\[
m_{44}
=
7220252188262239184305599554690421895921563960360483237559093394744562,
\]

and therefore

\[
\boxed{
B_{44}
=
227578060273510610973552811001603322347312502177488333909527505984
>2^{217}.
}
\]

One minimizing low-to-high triadic word is

```text
01100011100001111110011011010001110000110110
```

The canonical payload SHA-256 is

```text
0ae0ccf0df779ffe4dc8b4d2a4f91471033cdf84b47738d9f79d6b7c85f43add
```

## Interpretation

Subject to independent reconstruction of `T-9313`, the exact result excludes every nontrivial ordinary survivor room below `B_44`.

It does not prove that the sequence `B_j` tends to infinity, although the frozen values rise rapidly. Proving unbounded growth of `B_j`, or the stronger expected scale near `32^j`, would close the fixed-room ordinary-section problem.

## Limitations

- The computation is finite and ends at depth `44`.
- Meet-in-the-middle proves the exact minimum at the selected depths but does not supply an asymptotic theorem.
- The result concerns the induced `64 -> 81` ordinary room. Translation to an original Collatz starting value remains branch-qualified.
- No ordinary survivor, divergent seed, nontrivial cycle, or Collatz resolution is claimed.
