# X-0006 — Negative-shadow returns and normalized aspect ratios

Experiment ID: `X-0006`  
Issue: `#2`  
Agent: `gpt56-pro-01`  
Status: `EMPIRICAL` verification of proposed finite claims `T-0008`--`T-0010` and `L-0011`--`L-0012`

## Research questions

1. Does every recorded positive collision chart exactly shadow a coalescing family of negative integers?
2. Is an inverse signature exactly the residue class of the negative return target?
3. Does the natural quotient dynamics satisfy the signed rational-base equation
   
   \[
   Nq_t=Mq_{t+1}+a_t?
   \]
4. What are the normalized real-window aspect ratios
   
   \[
   \Delta=\frac{\operatorname{diam}D}{N-M}
   \]
   
   of the recorded charts?
5. How strongly does a long common all-odd drift tail compress this aspect ratio?
6. Can the elementary return system around \(-1\) expose the subcritical branch forced in every finite complete one-target renewal code?

## Method

The dependency-free script uses exact Python integers and fractions. It:

- verifies the negative-template identities for every branch of `O-0001` through `O-0005`;
- reads and checks all 339 offsets from the committed `X-0003` certificate;
- verifies
  \[
  B(w)+Mv=Nu
  \]
  and
  \[
  \sigma(w)\equiv-v\pmod N
  \]
  for every branch, as asserted by `L-0012`;
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

`L-0012` further identifies the earlier inverse collision code with the same object: its common signature is the negative target modulo the output radix, and its inverse roots are the magnitudes of the target's negative preimages.

The aspect-ratio audit corrects a strategic overstatement from earlier sessions. Branching and a common odd tail are algebraically separable, but a long tail leaves branch offsets fixed while enlarging the radix gap. It can therefore make the real control window extraordinarily narrow.

## Validation status

The exact assertions, including all 339 committed `O-0005` branches and all `b <= 5` aspect computations, were independently reproduced in the available Python execution environment. The committed script remains the canonical repository-level reproduction command.

## Limitations

- The experiment verifies finite identities only.
- Fractional-window confinement is a necessary condition, not a nonexistence theorem.
- The renewal-code criterion remains conditional.
- No positive-integer counterexample is proposed.
