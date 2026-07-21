# X-0012 — Tower tail replacement and connector-stack audit

Experiment ID: `X-0012`  
Issue: `#2`  
Agent: `gpt56-pro-01`  
Status: `EMPIRICAL` verification of proposed exact claims `L-0016`--`L-0024`, `T-0022`--`T-0023`, `O-0009`, and the finite algebra used by `T-0021`

## Research questions

1. Do the negative-eleven-cycle self-return towers act as exact binary-to-ternary block replacements with one unchanged ordinary high tail?
2. Is the finite recovery core periodic in the padding counter?
3. Does every ordered pair of tower instances admit an exact ordinary connector family?
4. Do growing inverse powers modulo growing powers of two defeat a fixed periodic residue table?
5. Can exact order-sized nonlinear counter jumps preserve a normalized connector prefix by Hensel lifting?
6. Can the negative cycle pay for both the current connector and the next residual-stack cylinder?
7. What exact finite-control structure appears at one dyadic scale?
8. Does fixing the high tail leave only finitely many affine-geometric counter rays?

## Programs

### `run.py` — tower and one-connector layer

The core script reconstructs the negative eleven-cycle at phase `-34` and its four self-return mismatch types. It verifies:

- the core periods
  
  ```text
  16, 8, 4, 2;
  ```
- the block identity
  
  \[
  A_t+2^{K_t}h
  \longmapsto
  B_t+3^{G_t}h;
  \]
- direct physical Collatz replay for padding heights `0,...,11` and several tails;
- every ordered pair of the four tower types at heights `0,...,7`, for a total of `1024` canonical connector families;
- canonical connector bounds on both the binary seed and ternary cap;
- exact two-block replay after each connector;
- the order formula
  
  \[
  \operatorname{ord}_{2^K}(3)=2^{K-2}
  \]
  
  through `K=63`;
- the Hensel-jump identity
  
  \[
  \omega_{t+2^{H+r-1}}
  \equiv
  \omega_t
  \pmod{2^H};
  \]
- the target-independent low connector prefix;
- the one-connector `C=7` height-growth window;
- the exact dyadic-ray decomposition for a finite high-tail library.

### `stage.py` — residual-stack and scale-stage layer

The stage audit verifies:

- the exact 128-step precursor odometer;
- the four rational stage-frontier limits
  
  \[
  19/243,\quad38/81,\quad76/243,\quad638/729;
  \]
- their exact binary periods
  
  ```text
  162, 54, 162, 486;
  ```
- the quadratic moving-bulk recurrence
  
  \[
  u_{m+1}=u_m+2^{m+1}u_m^2;
  \]
- the corrected residual recurrence
  
  \[
  z_{n+1}
  =
  \frac{3^{G_n}z_n+	heta_n-\eta_{n+1}}
  {2^{K_{n+2}}};
  \]
- positive exact residual slope for the `C=8` schedule;
- asymptotic residual contraction of the earlier `C=7` schedule;
- the exact 256-step, eight-bit odometer stage from `L-0024`.

## Regression anchors

The same-type `t=0 -> t=1` canonical connector seeds are:

```text
k0=5: eta=2241439 theta=1168 next_K=22
k0=6: eta=865722  theta=451  next_K=22
k0=7: eta=577148  theta=300  next_K=22
k0=8: eta=1782866 theta=929  next_K=22
```

The first twenty LSD-first bits of the four stage-frontier connector limits are:

```text
k0=5: 11111001110011001010
k0=6: 01011101101011001111
k0=7: 00111110011100110010
k0=8: 01001010001011001100
```

## Commands

```bash
python3 -m py_compile experiments/X-0012-tower-connector-stack/run.py
python3 experiments/X-0012-tower-connector-stack/run.py
python3 -m py_compile experiments/X-0012-tower-connector-stack/stage.py
python3 experiments/X-0012-tower-connector-stack/stage.py
```

## Expected final lines

```text
all tower-connector-stack checks passed
all stage-boundary checks passed
```

The combined checked-in output is `results/summary.txt`.

## Digests

```text
29d9fab85678830eb9496f718a7ada2faa61e35c87dbd26c23d2689e0b320385  run.py
9dcb670b2da24e4cfa1eb27c86c263e65e04b66003708b20f732928e24fabe93  stage.py
15b4cc2aca8582f37013f58edeb31c528b1d8324d07572af4a25d9cd636a5e0d  results/summary.txt
```

## Interpretation

The tower counter is only a scale parameter. The exact memory channel is the arbitrary ordinary high tail `h`.

Every finite tower schedule is connectable, so finite-depth compatibility is universal and carries little evidentiary weight. Restricting the high tail to finitely many values leaves only finitely many dyadic counter rays; `T-0021` uses a nondegenerate power-sum theorem to show that fixed affine counter updates cannot join such rays at all heights.

The one-connector `C=7` lane preserves growing Hensel prefixes and expands the immediate high-tail height, but `T-0023` shows that it contracts the true residual after the next connector is parsed. The corrected `C=8` lane uses 256 finite-control steps per scale and has positive residual-stack slope.

At stage boundaries the connector stack splits into three tracks:

1. a finite periodic rational frontier;
2. an eight-bit odometer/carry controller;
3. one odd moving bulk word satisfying a quadratic Hensel recurrence.

This is the cleanest current candidate architecture for a genuinely nonregular marked stack grammar.

## Limitations

- The experiment checks finite identities only.
- It does not verify the Skolem–Mahler–Lech step in `T-0021`; that is imported as `LIT-KTHM-0008` from PR #13.
- Nested Hensel prefixes naturally define a 2-adic limit and are not an ordinary-marker certificate.
- Positive residual slope applies only after exact integrality of the next residual transition.
- Same-precision quadratic updates do not manufacture missing higher bits.
- No forward self-regenerating stack language or positive-integer counterexample is constructed.
