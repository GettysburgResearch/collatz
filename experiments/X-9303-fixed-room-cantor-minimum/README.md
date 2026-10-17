# X-9303 — Exact dual minimum-survivor certificate

**Experiment ID:** X-9303  
**Status:** INTERNAL EXACT COMPUTATION  
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

compute

\[
m_j=\min(C_j\setminus\{0,1\})
\]

exactly.

`T-9313` proves the exact duality

\[
\boxed{
M_j
:=
\min(R_j\setminus\{0,1\})
=
\left\lceil m_j(64/81)^j\right\rceil,
}
\]

where `R_j` is the standard depth-`j` survivor set. Thus the triadic subset-sum minimum gives the exact first nontrivial survivor without scanning all `2^j` starting residues.

## Algorithm

The class set is a modular subset-sum problem with generators

\[
g_r
\equiv
-17\,81^r64^{-(r+1)}
\pmod{81^j}.
\]

The verifier:

1. splits the generators into two halves;
2. enumerates and sorts all right-half subset sums;
3. enumerates left-half sums in Gray-code order;
4. uses binary search for the least positive modular complement;
5. excludes the trivial residues `0` and `1`;
6. reconstructs one minimizing low-to-high triadic word;
7. reverses it into chronological survivor order;
8. reconstructs the starting room from the exact fixed-room identity;
9. replays all survivor steps and verifies the final tail class.

The work is `O(2^(j/2) log 2^(j/2))` and storage is `O(2^(j/2))`.

For depths through `16`, the script independently performs direct full class enumeration and requires exact agreement.

## Replay

```bash
python3 -B -m py_compile \
  experiments/X-9303-fixed-room-cantor-minimum/run.py
python3 -B experiments/X-9303-fixed-room-cantor-minimum/run.py \
  --check-results \
  experiments/X-9303-fixed-room-cantor-minimum/results/canonical.json
```

The depth-46 checkpoint sorts `2^23 = 8,388,608` exact integer right-half sums. It is bounded deterministic computation, not random sampling.

## Frozen depth-46 result

The least nontrivial triadic class is

\[
m_{46}
=
13995580641937679806861747515838198945935546006963182029787326398035667034.
\]

One minimizing low-to-high triadic word is

```text
1101110101010000110011100000101001011110110110
```

The reversed chronological survivor word is

```text
0110110111101001010000011100110000101010111011
```

Its exact starting room—and the exact minimum of `R_46 \ {0,1}`—is

\[
\boxed{
M_{46}
=
275396778563393867136351926990265018601508986973296055235244496661568
>2^{227}.
}
\]

The replay ends at the ordinary tail `m_46` after exactly 46 valid steps.

Canonical payload SHA-256:

```text
f2c4dd9b0c436c9450c03424b27d80366865f54bb8c286944a35047d0662c9bc
```

## Interpretation

Subject to independent reconstruction of `T-9313`, the result is both:

- an exact finite minimum-survivor theorem at depth 46;
- an exclusion of every nontrivial infinite ordinary survivor room through `2^227`.

The monotone sequence

\[
M_j=\min(R_j\setminus\{0,1\})
\]

satisfies `M_(j+1)>=M_j`. Proving `M_j -> infinity` would close the ordinary-section problem.

## Limitations

- The computation is finite and ends at depth `46`.
- Meet-in-the-middle proves exact selected-depth minima but no asymptotic growth theorem.
- Translation to an original Collatz starting value remains branch-qualified.
- No ordinary survivor, divergent seed, nontrivial cycle, or Collatz resolution is claimed.
