# Report: loop — close fuel deep-burn, open highway / 3-adic paths

Agent: `grok45-01`  
Branch: `cursor/affine-pingpong-schottky-a643`  
PR: https://github.com/gfreund123/collatz/pull/11  
Date: 2026-07-21

## Exhausted → closed / residual

| Path | Action |
|---|---|
| 2-adic deep fuel burn | **Proved** `L-0114` (elevates `C-0104`(1)) |
| 2-adic regenerative fuel | Residual stalled (`O-0108`) |
| Classical Schottky / tensor radius | Already closed |

## New directions opened

| Direction | Baseline |
|---|---|
| `D-HIGHWAY-*` odd-run ladder | `O-0111` — huge peaks, always return |
| `D-COVERING-*` mixed-modulus ladder | `O-0112` — delay to ~500 steps, still return |
| `D-ADIC3-*` 3-adic shadow | `L-0115` + `O-0110` |
| `D-RETURN-*` (handoff) | Prove return bounds after highways |

## Lemmas

- `L-0114` — \(v_2(T_w(n)-c)=v_2(\kappa)-L\) when deeper than \(\kappa\) (0 mismatches).
- `L-0115` — 3-adic ultrametric ledger; \(\kappa=0\) holds gain \(+a\) in \(v_3\) (0 mismatches).

## No K-candidate

Mixed-modulus “400-step survivors” all hit \(\{1,2\}\) by step ~470–540.

## Next EV

1. Mixed \(v_2\)/\(v_3\) certificate that refunds 2-adic fuel.
2. Non-all-ones mixed-modulus ladders / larger primes.
3. Analytic return bound (`D-RETURN-*`) or a violating family.
