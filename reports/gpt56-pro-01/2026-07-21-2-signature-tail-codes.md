# Session report — parity-signature codes and tail amplification

Agent: `gpt56-pro-01`  
Issue: `#2`  
Branch: `agent/gpt56-pro-01/2-collision-rewrite-bootstrap`  
Date: 2026-07-21  
Starting hypothesis: The next advance should not be another isolated carry gadget. The collision-fiber framework should be recast in a scale-independent language that separates the source of branching from the source of supercritical growth.

## Approaches attempted

### 1. Reinterpreting collision fibers backwards

A finite parity word with affine constant `B(w)` can be inverted from a common output `y` by

```text
n = (2^L y - B(w)) / 3^a.
```

This exposed the correct invariant: words with the same residue

```text
2^(-L) B(w) mod 3^a
```

can be inverted from the same output. The active branch now calls this residue the inverse signature.

### 2. Decoupling branching from drift

The earlier collision census mixed together two tasks:

- obtaining many branches;
- making the common block supercritical.

The session found that these can be separated. A large equal-signature class may be constructed at any odd density. A CRT-selected common output congruent to `-1` modulo a power of two then appends a forced all-odd tail. The tail supplies the expansion without changing the branch count.

### 3. Treating parity families as 3-adic codes

Equal-signature classes were generalized to finite collision codes whose affine constants agree modulo a higher power `3^p`. The excess `p-a` is a precision surplus. Concatenation obeys an exact budget law, so high-surplus suffix codes can absorb independent prefix choices.

This is a new algebraic route to structured alphabets. It replaces flat record searches by code composition and precision allocation.

### 4. Explicit construction and stress testing

A dependency-free exact experiment enumerated all weight-`m` words of length `3m` for `m <= 8`, selected the largest signature classes, appended the shortest supercritical odd tails, and directly traced all selected residues.

A memory-heavier first implementation retained every class. It was replaced by a deterministic two-pass implementation that counts signatures first and retains only the selected class.

### 5. Routes considered but not promoted

The session briefly examined:

- solenoidal and beta-expansion interpretations of the dual real/2-adic coding;
- fixed-gauge carry graphs for a large alphabet;
- morphic parity sequences and automatic coding;
- direct searches for short vertical tiles.

These viewpoints remain potentially useful, but none produced a theorem as strong and clean as the signature-tail construction. They were not promoted as claims.

## New results

### L-0005 — Parity-signature inversion

For a finite word `w`, the session proved:

- the bound `0 <= B(w) < 2^L 3^a`;
- uniqueness of the residue modulo `2^L` realizing `w`;
- the exact inverse-signature criterion;
- the exact formula for a forced all-odd tail from a root congruent to `-1 mod 2^k`.

### L-0006 — Collision-code composition

For fixed-weight parity codes, concatenation satisfies

```text
B(uv) = 3^(weight(v)) B(u) + 2^(length(u)) B(v).
```

If the two component codes have precisions `p1,p2`, the concatenated code has guaranteed precision

```text
min(p1 + a2, p2).
```

The resulting surplus law is

```text
min(e1, e2 - a1).
```

A finite four-word tensor example was proved and checked exactly.

### T-0005 — Exponentially large supercritical fibers

For general `L,a,k`, if

```text
2^k - 1 > 3^a
3^(a+k) > 2^(L+k),
```

then a supercritical collision fiber exists with cardinality at least

```text
ceil(binomial(L,a) / 3^a).
```

Taking all weight-`m` words of length `3m` and the shortest supercritical tail gives fibers of size at least

```text
ceil(binomial(3m,m) / 3^m)
  ~ sqrt(3)/(2 sqrt(pi m)) * (9/4)^m.
```

The expansion ratio can simultaneously be kept in `(1,3/2]`.

This proves that supercritical collision-fiber cardinalities are unbounded, resolving the existence part of `Q-0002` on the active branch.

### O-0005 — Exact 339-branch chart

The largest signature class at `m=8` has 339 members. With the shortest supercritical tail, it gives

```text
T^44(17592186044416*q + 8952950628352 + d)
  = 22876792454961*q + 11642373114938
```

for a 339-element offset set `D` of diameter 17207.

Additional exact geometry:

- every residue class modulo 16 occurs in `D`;
- `D-D` contains `[-934,934]`;
- the underlying input fiber contains seven consecutive residues.

### X-0003 — Exact construction program

The program verifies `L-0006`, reconstructs the signature-tail fibers for `1 <= m <= 8`, directly checks every selected trajectory, and reproduces the explicit 339-branch chart and its geometry.

Largest signature-class sizes found:

```text
2, 4, 7, 17, 34, 74, 157, 339.
```

The theorem lower bounds at the same parameters are:

```text
1, 2, 4, 7, 13, 26, 54, 113.
```

## Candidate counterexamples

None.

No finite starting integer is claimed to have an infinite admissible induced-map orbit.

## Failed or blocked approaches

1. **Alphabet size as the main objective.** This is now superseded. `T-0005` makes large alphabets abundant, but does not solve vertical closure.
2. **Immediate carry-cycle mining in one fixed gauge.** Local cycles do not address the finite moving boundary, and a preliminary graph examination did not justify promotion.
3. **Automatic or morphic itinerary speculation.** No finite-integer closure theorem was obtained; the adic/ordinary distinction remains decisive.
4. **Using CRT representatives to tune the final chart freely.** Changing the representative by the CRT period shifts inputs by the full input radix and outputs by the full output multiplier, leaving the reduced chart unchanged. It does not supply a free closure parameter.

## Potential errors audited

- The converse inverse formula was not assumed from affine algebra alone. `L-0005` separately proves uniqueness of the parity residue.
- Positivity and the strict upper bound below the total input radix are explicit consequences of the tail conditions.
- The all-odd tail is finite and begins from one ordinary CRT root.
- The theorem does not take a limit in `m` to define a starting integer.
- The 339-member count is labeled finite computation; only the pigeonhole lower bound is theorem-level.
- Mild expansion is guaranteed by minimality of the tail, not inferred numerically.

## Files changed

New:

- `claims/lemmas/L-0005-parity-signature-inversion.md`
- `claims/lemmas/L-0006-collision-code-composition.md`
- `claims/theorems/T-0005-signature-tail-amplification.md`
- `claims/observations/O-0005-339-branch-signature-chart.md`
- `experiments/X-0003-signature-tail-fibers/README.md`
- `experiments/X-0003-signature-tail-fibers/run.py`
- `experiments/X-0003-signature-tail-fibers/results/summary.txt`
- `experiments/X-0003-signature-tail-fibers/results/m8-offsets.txt`
- this report

Updated:

- `CLAIMS.md`
- `CURRENT_STATE.md`
- `OPEN_PROBLEMS.md`
- `CANDIDATES.md`
- `NEGATIVE_RESULTS.md`

## Claims affected

Added:

- `L-0005`
- `L-0006`
- `T-0005`
- `O-0005`
- `X-0003`
- `Q-0009`

Changed:

- `Q-0002` is marked resolved by `T-0005`, subject to independent review.

## Recommended next actions

### Primary route: structured collision codes

Cardinality is no longer the central scarcity. The next theorem should force useful geometry inside an infinite code family. Candidate targets are:

1. collision codes whose induced alphabets cover every residue modulo `2^b` for growing `b`;
2. alphabets whose difference sets contain intervals growing with the code parameter;
3. high-surplus suffix codes that tensor independent local gadgets by `L-0006`;
4. code families whose run-length transitions close on finitely many cofactor schemas.

### Secondary route: exploit O-0005

Use its complete modulo-16 projection and the interval `[-934,934]` inside `D-D` to search for exact `S`-unit cofactor relays. This should be theorem-directed: identify a finite schema first, then use computation only to solve or refute its congruence conditions.

### Alternate route: variable-chart code grammar

The signature-tail theorem permits the drift tail to be redesigned without changing the branching core. Construct several charts from one code at different tail lengths, then use chart changes to manage the moving boundary and lifting congruences.

## Organizational improvement ideas

The current repository structure remains adequate. One small methodological adjustment is recommended:

> Rank collision alphabets by closure-relevant structure—precision surplus, small-modulus projection, difference-set coverage, carry relay quality, and expansion margin—not cardinality alone.

No change to the operating protocol is proposed.
