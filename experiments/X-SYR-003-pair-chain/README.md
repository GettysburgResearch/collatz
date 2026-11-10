# X-SYR-003: the Syracuse pair chain on the affine group

Supports [`research/syracuse-pair-chain`](../../research/syracuse-pair-chain/README.md).

| File | What it does |
|---|---|
| `verify_group.py` | 14 checks, floating point at tolerance 1e-9: `Q_1 = W`, mass 1, the pair recursion, the martingale property, the exact `L^2` formula on the affine group (levels 1 to 4, brute force), blow-up at resonant maps, and the Gram matrix of the two level-1 modes to level 14. About 15 s. |
| `results_group.json` | Output of the above. |

```bash
python3 verify_group.py
```

Limits: numerical confirmations at small levels of identities whose proofs are in the note; not a proof of conjecture C1.
