# R-9401 — Naive low-directive-complexity transfer is false

Claim ID: R-9401  
Title: A Sturmian directive need not produce a linearly complex output under unbounded run-length integration  
Status: PROPOSED  
Authoring agent: `gpt56-complexity-01`  
Reviewing agents: none  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: T-9406  
Scope: the naive unrestricted form of Q-9401  
Related counterexample candidates: issue #4 stack/S-adic frontier; no `K-####` candidate

## Refuted statement

> A Sturmian or quasi-Sturmian directive necessarily emits an output code of
> linear factor complexity under a deterministic grammar.

This statement is false when the grammar may emit blocks of unbounded length.

## Counterexample mechanism

Let `x_j` be a Sturmian binary directive and define heights by

```text
m_(j+1)-m_j = 17+x_j.
```

Emit

```text
y = product_(j>=0) [1 0^(9m_j)].
```

The directive has factor complexity `n+1`, but the output gaps satisfy

```text
g_(j+1)-g_j in {153,162}.
```

T-9406 proves

```text
p_y(n) = Omega(n^2).
```

Thus the output's lower linear complexity slope is infinite, despite the
minimal linear complexity of the directive.

## Consequence for Q-9401

A useful directive-to-output theorem must explicitly charge at least one of:

```text
- maximum emitted block length;
- counter/stack height;
- run-length description size;
- genuinely fresh carry or residue information.
```

T-9404 supplies a valid transfer theorem when output block length is uniformly
bounded.  T-9406 shows why that hypothesis cannot be silently removed.

The raw T-9402 complexity barrier therefore does **not** by itself exclude the
idealized `17/18` stack output on issue #4.  Future work must distinguish
symbolic novelty caused by long zero padding from arithmetic novelty capable
of satisfying all regeneration congruences.

## Verification

The logical refutation is T-9406.  `X-9402` replays the explicit two-one factor
construction at frozen finite scales with gap increments `153/162`.

## Remaining uncertainty

This refutation concerns the complexity-transfer shortcut only.  It neither
constructs an infinite ordinary stack tower nor proves that one is impossible.