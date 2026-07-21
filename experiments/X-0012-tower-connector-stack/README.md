# X-0012 — Tower tail replacement and connector-stack audit

Experiment ID: `X-0012`  
Issue: `#2`  
Agent: `gpt56-pro-01`  
Status: `EMPIRICAL` verification of proposed exact claims `L-0016`, `L-0017`, `L-0018`, and the finite algebra used by `T-0021`

## Research questions

1. Do the negative-eleven-cycle self-return towers act as exact binary-to-ternary block replacements with one unchanged ordinary high tail?
2. Is the finite recovery core periodic in the padding counter?
3. Does every ordered pair of tower instances admit an exact ordinary connector family?
4. Do growing inverse powers modulo growing powers of two defeat a fixed periodic residue table?
5. Does fixing the high tail leave only finitely many affine-geometric counter rays?

## Method

The dependency-free script reconstructs the negative eleven-cycle at phase `-34` and its four self-return mismatch types. It uses exact Python integers only.

It verifies:

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
- exact two-block replay after each connector;
- the order formula
  
  \[
  \operatorname{ord}_{2^K}(3)=2^{K-2}
  \]
  
  through `K=63`;
- the exact dyadic-ray decomposition obtained when the high tail is restricted to a finite library.

The same-type `t=0 -> t=1` canonical connector seeds are recorded as regression anchors:

```text
k0=5: eta=2241439 theta=1168 next_K=22
k0=6: eta=865722  theta=451  next_K=22
k0=7: eta=577148  theta=300  next_K=22
k0=8: eta=1782866 theta=929  next_K=22
```

## Command

```bash
python3 -m py_compile experiments/X-0012-tower-connector-stack/run.py
python3 experiments/X-0012-tower-connector-stack/run.py
```

## Expected final line

```text
all tower-connector-stack checks passed
```

The checked-in output is `results/summary.txt`.

## Digests

```text
63d315e387b592be937357f6819c0af9ec5cd589a08bf88a639d602a266e4442  run.py
d39bfbc2851c01e0d83040700e38bb1168c5b219ad49545b6f912d55c63f2d76  results/summary.txt
```

## Interpretation

The tower counter is only a scale parameter. The exact memory channel is the arbitrary ordinary high tail `h`.

Every finite tower schedule is connectable, so finite-depth compatibility is universal and carries little evidentiary weight. Conversely, restricting the high tail to finitely many values leaves only finitely many dyadic counter rays; `T-0021` uses a nondegenerate power-sum theorem to show that fixed affine counter updates cannot join such rays at all heights.

The next construction must therefore manipulate a genuinely unbounded high-tail stack or cofactor.

## Limitations

- The experiment checks finite identities only.
- It does not verify the Skolem–Mahler–Lech step in `T-0021`; that is imported as `LIT-KTHM-0008` from PR #13.
- It does not construct a self-regenerating stack language.
- No positive-integer counterexample is proposed.
