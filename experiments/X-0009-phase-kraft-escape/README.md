# X-0009 — Rounded phase martingale and escape-transform checks

Experiment ID: `X-0009`  
Issue: `#2`  
Agent: `gpt56-pro-01`  
Status: `EMPIRICAL` verification of proposed exact claims `L-0013` and `T-0017`

## Research questions

1. Does physical Collatz parity reduce the exact phase coupling to the rounded pair
   \[
   S_0(v)=\lceil v/2\rceil,
   \qquad
   S_1(v)=\lfloor3v/2\rfloor?
   \]
2. Do finite complete parity prefix codes satisfy the phase–Kraft identity
   \[
   \sum_w2^{-|w|}(S_w(v)-1)=v-1?
   \]
3. Is the Doob transform for the harmonic function \(h(v)=v-1\) exactly
   \[
   \mathbb Q_v([w])=2^{-|w|}\frac{S_w(v)-1}{v-1}?
   \]
4. Does phase survival force a physical odd-step bias of at least \(3/4\), and therefore positive logarithmic Collatz pressure?
5. How does fair survival mass decay while the harmonic first moment remains constant?

## Method

`run.py` uses exact Python integers and fractions, plus floating-point evaluation only for explicit positive logarithmic lower bounds. It:

- checks the rounded phase formula on 500,000 exact `(q,v)` pairs;
- verifies `S_0(v)+S_1(v)=2v` through phase 500;
- checks phase–Kraft identities on four complete prefix codes and six starting phases;
- verifies the exact escape probabilities through phase 10,000;
- checks every length-12 path from phase 136 against the telescoping density formula;
- verifies uniform positive physical and phase logarithmic drift bounds;
- propagates the exact fair phase distribution through depth 32;
- confirms that the harmonic first moment remains exactly `v-1=135` while survival probability falls.

## Command

```bash
python3 -m py_compile experiments/X-0009-phase-kraft-escape/run.py
python3 experiments/X-0009-phase-kraft-escape/run.py
```

## Checked output

The exact checked-in output is:

```text
results/summary.txt
```

The local validation digests are:

```text
da4fccfb3733b70447b3c00a7e87eb1812b21ec8c071a48a1fed797425e99ce0  run.py
e508cc352f6d010acdb3593cfb2b00fe96cd84d9aa83eb3ab4d94087e47dfea7  results/summary.txt
```

## Interpretation

The fair physical-parity phase is an exact nonnegative martingale that is eventually absorbed at phase `1`. Its escape Doob transform is the endpoint-size-biased measure

\[
2^{-|w|}\frac{S_w(v)-1}{v-1}.
\]

Under that transform, physical odd parity has conditional probability at least `3/4`, phase magnitude has uniformly positive logarithmic drift, and the formal Collatz multiplier has uniformly positive logarithmic drift.

This gives a principled exceptional search measure. It does not produce an ordinary positive starting integer.

## Limitations

- All executable checks are finite.
- The absorption theorem and graph rigidity remain mathematical claims pending independent review.
- Symbolic escape paths typically represent 2-adic states; ordinary-integer membership is still the central missing step.
- No counterexample candidate is proposed.
