# Report: new paths forward (cycle MITM, −17 model B, fuel engine)

Agent: `grok45-01`  
Branch: `cursor/affine-pingpong-schottky-a643`  
PR: https://github.com/gfreund123/collatz/pull/11  
Date: 2026-07-21

## What opened

Classical Schottky / filled-radius tensor growth remain closed (`T-0103`–`T-0105`).
This session pushed three forward surfaces:

1. **Constructive cycle hunt** — MITM on ones-positions (`X-0129`) plus typed
   multi-block families (`X-0127`).
2. **Heteroclinic model B** on the density-\(7/11\) chart \(-17\) (`X-0128`).
3. **Valuation-fuel regenerative divergence** as an explicit new direction
   (`D-FUEL-*`, `X-0130`–`X-0132`, `C-0104`).

## Results (no K-candidate)

| ID | Result |
|---|---|
| `O-0109` / `X-0127` | 21786 structured multi-block words → only trivial cycles |
| `O-0106` / `X-0129` | MITM empty through \(L=37\); truncated empty at \(41,49\) |
| `O-0107` / `X-0128` | −17 model B: deep growth burns; mild repair + **local grow+keep** |
| `O-0108` / `X-0131` | Iterated grow+keep stalls (max \(+2\) bits, \(0\) escapes) |
| `X-0132` | Scheduled dip/repair: max \(1\) epoch, max \(+2\) bits |
| `X-0130` | Coarse fuel automaton: regen events, no \(+8\) size-bucket proxy |

## Methodological fix

Model A CRT-glues excursions as immediate prefixes of template cylinders,
vacuously killing mild `0…` words on templates starting with `1`. Model B
(shadow, then deviate) is the correct heteroclinic move and is what reveals
repair / grow+keep.

## Working conjecture

`C-0104`: deep growth burns depth; shallow grow+keep exists but does not
iterate into a regenerative unbounded fuel engine in short concatenation
alphabets.

## Next highest-EV moves

1. Mixed-template fuel (`-5` ↔ `-17`) with scheduled chart switches.
2. Morphic / automatic large excursion alphabets for fuel walks.
3. Covering-system cycle obstructions or full \(L=49\) MITM.
4. Attempt a lemma elevating the deep-burn half of `C-0104`.
