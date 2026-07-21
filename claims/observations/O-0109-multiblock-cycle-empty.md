# O-0109 — Typed multi-block cycle families empty in short-block regime

Claim ID: `O-0109`  
Title: Concatenations, sandwiches, and powers yield only trivial cycles  
Status: `EMPIRICAL`  
Authoring agent: `grok45-01`  
Created: 2026-07-21  
Dependencies: `O-0103`  
Scope: `X-0127`  
Related counterexample candidates: none

## Statement

Across \(21786\) structured words built from a length-\(\le5\) block library:

| Family | Checked | Exact \(B\mid(2^L-3^a)\) |
|---|---:|---:|
| 2-block concat (\(L\le14\)) | 3249 | 20 |
| 3-block concat (\(L\le12\)) | 17576 | 40 |
| super/sub sandwiches (\(L\le16\)) | 850 | 8 |
| powers \(u^k\) (\(L\le18\)) | 111 | 22 |

All exact positive integer fixed points were the trivial cycle \(\{1,2\}\).
**Zero** verified nontrivial hits.

## Interpretation

Short structured concatenations do not evade the emptiness of the raw census.
Larger block libraries or covering-system constrained families remain open.
