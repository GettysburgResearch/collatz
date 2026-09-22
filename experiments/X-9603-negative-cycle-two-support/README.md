# X-9603 — Two-support pulses on the negative three-cycle

**Status:** `EMPIRICAL` exact finite computation  
**Agent:** `gpt56-pro-04`  
**Issue:** #46  
**Associated claim:** `L-9603`

## Family

Start with either primitive rotation of `(1,2)^r`. Insert extra divisions at exactly two support positions. By cyclic rotation the first support is placed at position zero; the second is `q`.

For total pulse `B=b+c`, `L-9603` reduces the full cycle condition to

\[
2^b(U_q-V_q)
\equiv U_q-V_q2^B
\pmod {2^{3r+B}-3^{2r}}.
\]

A gcd test removes impossible rows before the bounded exponent scan. Every congruence hit is reconstructed as an exact accelerated word and replayed.

## Frozen scope

```text
1 <= r <= 400
both primitive rotations
B_min(r) <= B <= B_min(r)+3
1 <= q < 2r
1 <= b < B, c=B-b
```

## Result

```text
exact pulse splits:               59,385,744
gcd-admissible position rows:      1,160,328
nontrivial positive cycles:                0
```

The only hit is `(2,2,2,2)` at `r=2`, the trivial `n=1` cycle traversed repeatedly.

```text
results SHA-256:
5c9bccab0a7012940650f011f380dd243335d4e547eb59aff1faa860c92efa4e

semantic audit:
c408dfa7e2359bdc0b27e479753cd90cd14d4872d15e7fe3fa9db881e1107f97

run.py SHA-256 used in the authoring replay:
bd84f7d48babf14b5f67112673b618750a0900dd8bbe7b06d8af5a9706662776
```

## Replay

```bash
python3 -B experiments/X-9603-negative-cycle-two-support/run.py \
  --check-results \
  experiments/X-9603-negative-cycle-two-support/results/canonical.json
```

The authoring replay used exact Python integers, completed in about 26 seconds, and peaked below 111 MiB. Resource figures are informational only.

## Boundary

- Three or more support positions are outside this experiment.
- Only four total-pulse levels are tested.
- Only the negative three-cycle is included.
- The result is a finite family exclusion, not a global cycle theorem.
- No counterexample is claimed.
