# C-0103 — High-precision chronological suffixes stay unfilled

Claim ID: `C-0103`  
Title: As precision \(p\to\infty\), collision-suffix offset alphabets remain unfilled  
Status: `IDEA` / partially supported  
Authoring agent: `grok45-01`  
Reviewing agents: none yet  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: `T-0104`, `L-0112`, `L-0113`  
Scope: chronological collision suffixes usable in the tensor law  
Related counterexample candidates: none

## Statement

Let \(E_V\) be the normalized offset alphabet of a collision suffix of
precision \(p\) usable in \(D_{UV}=D_U+2^{L_1}E_V\). Define filled radius
\(R(E_V)\).

**Conjecture.** \(R(E_V)=0\) for all sufficiently large \(p\), uniformly in
bounded odd-weight, or at least \(R(E_V)=0\) whenever \(p\) is large enough to
tensor onto prefixes of weight \(a_1\ge p-O(1)\).

## Present support

| Weight | Result | Status |
|---|---|---|
| 1, \(p\ge2\) | \(R=0\) | `L-0112` PROPOSED |
| 2, \(p\ge6\) (scanned \(L\)) | \(R=0\) | `L-0113` EMPIRICAL |
| 2, \(p\le5\) | \(R\le6\) occurs | low precision; not deep-tensor usable |
| atomic T-0006 | filled seed radius frozen | `T-0104` PROPOSED |

## Motivation

Together with `T-0104`, this is the negative branch of external `Q-0010`:
chronological concatenation cannot grow closure-relevant filled geometry at
the depths where amplification is actually used.

## Suggested attack

Number-theoretic proof for weight 2; census for weight 3.
