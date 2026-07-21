# X-0014 — Adaptive counter isometry and stage Montgomery compression

Experiment ID: `X-0014`  
Issue: `#2`  
Agent: `gpt56-pro-01`  
Status: `EMPIRICAL` verification of proposed exact claims `L-0028` and `T-0027`--`T-0029`

## Research questions

1. Does a finite chain of odd-affine binary divisions compress to one offset Montgomery tile without losing any intermediate integrality condition?
2. Is the normalized connector-prefix map an exact 2-adic isometry in the fine padding-counter address?
3. Does every finite prefix have exactly one counter address at every precision?
4. Can arbitrary prefix requests be routed inside consecutive cells of one dyadic scale annulus while the padding height remains increasing?
5. What coarse cell count is sufficient for worst-case adaptive prefix changes to retain positive two-connector residual growth?
6. Do the complete stage odd exponent and binary depth obey exact normalized squaring laws?

## Method

`run.py` uses exact Python integers only. It:

- checks offset-Montgomery composition on several signed affine systems over every input in a finite interval;
- verifies that composite divisibility is equivalent to all intermediate local divisions;
- constructs an eight-step slice of the actual phase-`-34` residual chain and replays canonical stage corrections with several high tails;
- verifies the exact counter-prefix valuation identity for all four tower types;
- enumerates every counter address through seven-bit precision and checks that each finite-level map is a permutation;
- verifies the one-bit address lift by comparing the two ordinary lifts `s` and `s+2^H`;
- constructs a complete adaptive 512-cell annulus for every tower type at a representative precision;
- routes one deterministic but nontrivial requested prefix in every cell;
- checks all jump bounds and all two-connector growth inequalities using the exact lower bound `log_2(3) > 84/53`;
- verifies the complete stage exponent formulas and exact normalized scale squaring through several scales.

## Command

```bash
python3 -m py_compile experiments/X-0014-adaptive-counter-stage/run.py
python3 experiments/X-0014-adaptive-counter-stage/run.py
```

## Expected output

```text
verified offset Montgomery composition and exact path domains
verified padding-counter isometries and one-bit lifts
verified adaptive 512-cell prefix routing and robust growth
verified exact stage compression and normalized scale squaring
all adaptive-counter stage checks passed
```

The checked-in copy is `results/summary.txt`.

## Interpretation

The padding height has a canonical three-level coordinate system inside one scale annulus:

```text
scale m | 9-bit coarse cell j | H-bit fine address s | finite core residue
```

The fine address is isometrically equivalent to the normalized connector prefix. It can therefore route any requested logarithmic prefix without leaving the scale cell.

The fixed 256-step lane remains correct. The adaptive problem is different: arbitrary fine-address changes can nearly double one coarse jump. A 512-cell partition is the first dyadic chart for which the repository's exact cycle-margin bound proves positive two-connector growth under every such change.

The 256 local residual equations also compress exactly to one stage Montgomery tile. After removing the fixed contribution of 256 negative-cycle circuits, the stage odd multiplier and binary radix both square from one scale to the next.

## Limitations

- Prefix routing covers `O(m)` low bits per counter address, not the full `Theta(2^m)` connector block.
- The ordinary residual high tail remains necessary.
- The stage offset does not yet have a closed scale recurrence.
- No invariant ordinary stage quotient or marked Collatz seed is constructed.
- No positive-integer counterexample is proposed.
