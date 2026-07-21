# X-0006 — Negative-shadow returns and normalized aspect ratios

Experiment ID: `X-0006`  
Issue: `#2`  
Agent: `gpt56-pro-01`  
Status: `EMPIRICAL` verification of proposed finite claims `T-0008`, `T-0009`, `T-0010`, and `L-0011`

## Research questions

1. Does every recorded positive collision chart exactly shadow a coalescing family of negative integers?
2. Does the natural quotient dynamics satisfy the signed rational-base equation
   
   \[
   Nq_t=Mq_{t+1}+a_t?
   \]
3. What are the normalized real-window aspect ratios
   
   \[
   \Delta=\frac{\operatorname{diam}D}{N-M}
   \]
   
   of the recorded charts?
4. How strongly does a long common all-odd drift tail compress this aspect ratio?
5. Can the elementary return system around \(-1\) expose the subcritical branch forced in every finite complete one-target renewal code?

## Method

The dependency-free script uses exact Python integers and fractions. It:

- verifies the negative-template identities for every branch of `O-0001` through `O-0005`;
- reads and checks all 339 offsets from the committed `X-0003` certificate;
- verifies the signed rational-base return equation and finite address polynomial on an exact three-block `O-0001` trajectory;
- checks the complete one-step return table around the negative fixed point `-1`;
- reconstructs the complete-dyadic-projection examples for `1 <= b <= 5`;
- verifies the exact odd-tail aspect-ratio identity from `L-0011`;
- reports the rapid normalized-window collapse in those examples.

## Command

```bash
python3 -m py_compile experiments/X-0006-shadow-return/run.py
python3 experiments/X-0006-shadow-return/run.py
```

## Interpretation

The negative-shadow theorem is not merely a change of notation. It identifies the intrinsic signed digit alphabet

\[
A=\{v-u_i\}
\]

and removes the separate lifting congruence from the return equation. The counterexample problem becomes a rational-base renewal problem over exact negative templates.

The aspect-ratio audit also corrects a strategic overstatement from earlier sessions. Branching and a common odd tail are algebraically separable, but a long tail leaves branch offsets fixed while enlarging the radix gap. It can therefore make the real control window extraordinarily narrow.

## Limitations

- The experiment verifies finite identities only.
- Fractional-window confinement is a necessary condition, not a nonexistence theorem.
- The renewal-code criterion remains conditional.
- No positive-integer counterexample is proposed.
