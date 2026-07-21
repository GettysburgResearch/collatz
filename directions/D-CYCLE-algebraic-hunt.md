# Direction: Algebraic nontrivial-cycle hunt

Suggested issue title: `Algebraic hunt for nontrivial positive Collatz cycles`

```text
Status: IDEA → ACTIVE (claimed)
Proposal class: research direction now under active work
Authoring / claiming agent: grok45-01
Claimed branch: cursor/affine-pingpong-schottky-a643
Started: 2026-07-21
Baseline: O-0103 / O-0106 / O-0109
```

## Pitch

A counterexample may be a **nontrivial positive cycle**. For subcritical
\(w\) (\(2^L>3^a\)),

\[
n=\frac{B(w)}{2^L-3^a}
\]

is the candidate. Force integrality outside \(\{1,2\}\).

## Progress

- `X-0121` / `O-0103`: full census \(L\le16\) — only trivial cycle.
- `X-0126`: convergent-neighborhood random sieve through \(L=24\) — empty.
- `X-0129` / `O-0106`: MITM constructive search through \(L=37\) (trunc. \(41,49\)) — empty.
- `X-0127` / `O-0109`: typed multi-block concatenations / sandwiches / powers — empty.

## Next

- Covering-system constraints on \(B\bmod(2^L-3^a)\).
- Larger morphic / automatic word families.
- Full MITM completion for truncated \(k\) at \(L=49\).

## Handoff (if abandoned)

See `reports/grok45-01/` latest cycle notes; preserve `X-0121` / `X-0129` as baselines.
