# T-9314 — Exact depth-46 minimum survivor and bounded ordinary-room exclusion

**Claim ID:** T-9314  
**Title:** Dual meet-in-the-middle minimization computes the exact depth-46 minimum survivor and excludes ordinary rooms through `2^227`  
**Status:** PROPOSED  
**Authoring agent:** `gpt56-pro-04`  
**Reviewing agents:** none  
**Created:** 2026-07-21  
**Last updated:** 2026-07-21  
**Dependencies:** `T-9313`; exact computation `X-9303`  
**Scope:** exact finite survivor minimum and finite ordinary-section exclusion  
**Related counterexample candidates:** none

## 1. Exact minimum statement

Let

\[
R_{46}\subset[0,64^{46})
\]

be the standard set of residues surviving `46` induced `64 -> 81` steps. Then

\[
\boxed{
\min(R_{46}\setminus\{0,1\})
=
275396778563393867136351926990265018601508986973296055235244496661568.
}
\tag{1}
\]

One chronological length-46 word attaining the minimum is

```text
0110110111101001010000011100110000101010111011
```

and its final ordinary tail is

\[
13995580641937679806861747515838198945935546006963182029787326398035667034.
\]

## 2. Ordinary-section consequence

If

\[
A=\Phi(\varepsilon)\in\mathbb Z_{\ge0}
\]

is an infinite ordinary survivor, then either

\[
A\in\{0,1\},
\]

or

\[
\boxed{
A
\ge
275396778563393867136351926990265018601508986973296055235244496661568
>
2^{227}.
}
\tag{2}
\]

Hence there is no nontrivial ordinary survivor room in

\[
\boxed{2\le A\le2^{227}.}
\tag{3}
\]

## 3. Proof

At depth `j=46`, `X-9303` computes exactly

\[
\boxed{
 m_{46}
 =
 \min(C_{46}\setminus\{0,1\})
 =
 13995580641937679806861747515838198945935546006963182029787326398035667034.
}
\tag{4}
\]

One low-to-high triadic word attaining `(4)` is

```text
1101110101010000110011100000101001011110110110
```

`T-9313(18)` proves the exact minimum duality

\[
\min(R_j\setminus\{0,1\})
=
\left\lceil
m_j(64/81)^j
\right\rceil.
\tag{5}
\]

Applying `(5)` at depth `46` gives the integer in `(1)`.

The verifier additionally reverses the minimizing triadic word, reconstructs the fixed-room numerator, and directly replays all 46 induced steps. It ends at the class in `(4)` with no congruence or digit failure.

An infinite ordinary survivor lies in `R_j` for every `j`, so it is at least the minimum in `(1)`. Finally,

\[
275396778563393867136351926990265018601508986973296055235244496661568
>
2^{227}
\]

by direct integer comparison. This proves `(1)`--`(3)`. QED.

## 4. Algorithmic certificate

The depth-46 class set has

\[
2^{46}=70368744177664
\]

words. `X-9303` does not enumerate that full set in memory.

It splits the 46 modular subset-sum generators into two sets of 23, sorts the `2^23` exact right-half sums, and scans the `2^23` left-half sums in Gray-code order. For each left sum it checks the first admissible modular complement on both sides of the wrap point.

The script then:

1. reconstructs one minimizing subset mask;
2. replays the modular class sum;
3. reverses the word into chronological order;
4. reconstructs the starting room from the exact fixed-room identity;
5. replays every survivor step;
6. verifies the final tail class;
7. checks direct full enumeration independently at all frozen depths through `16`.

Frozen digest:

```text
f2c4dd9b0c436c9450c03424b27d80366865f54bb8c286944a35047d0662c9bc
```

Replay:

```bash
python3 -B -m py_compile \
  experiments/X-9303-fixed-room-cantor-minimum/run.py
python3 -B experiments/X-9303-fixed-room-cantor-minimum/run.py \
  --check-results \
  experiments/X-9303-fixed-room-cantor-minimum/results/canonical.json
```

## 5. Monotonicity and the universal frontier

Let

\[
M_j=\min(R_j\setminus\{0,1\}).
\]

Every `(j+1)`-step survivor is a `j`-step survivor, so

\[
\boxed{M_{j+1}\ge M_j.}
\tag{6}
\]

`T-9313` proves that the ordinary-section problem is equivalent to

\[
\boxed{M_j\longrightarrow\infty.}
\tag{7}
\]

The exact value `(1)` is one large finite checkpoint on that monotone sequence. It does not prove `(7)`.

## 6. Relationship to the requested decisive theorem

This theorem is stronger than a lower-bound-only room certificate: it computes the exact first nontrivial point of the entire finite survivor set at depth 46.

It uses the full fixed-room synchronization:

- the reversed past is a triadic class;
- the chronological word is an exact survivor prefix;
- the endpoint is an ordinary integer;
- the starting room is recovered exactly;
- every finite prefix of an infinite ordinary point must lie above the corresponding minimum.

The result remains finite and therefore does not exclude all infinite itineraries.

## 7. Dependency audit

- `T-9313` supplies the exact class-to-survivor ceiling transform and minimum identity.
- `X-9303` supplies the exact finite minimum, minimizing words, and direct survivor replay.
- No floating-point arithmetic, random sampling, external theorem, or issue-#4 unmerged claim is used.

## 8. Gap audit

- The depth-46 computation must be independently replayed before promotion.
- A finite exact minimum is not an asymptotic M1 theorem.
- Translation to an original shortcut-Collatz starting value remains branch-qualified.
- No counterexample, nontrivial cycle, or Collatz resolution is claimed.

## 9. Suggested next attack

Use the dual MITM formulation to study why the minimizing word changes and to build a branch-and-bound proof for the monotone sequence `M_j`. Any structural argument showing that a bounded starting room cannot appear at arbitrarily large depths proves `(7)` and closes the ordinary section.
