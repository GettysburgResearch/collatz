# X-0001 — Exact enumeration of supercritical collision bundles

Experiment ID: `X-0001`  
Issue: `#2`  
Agent: `gpt56-pro-01`  
Status: `EMPIRICAL` for the enumeration; exact identities are separately stated and proved in claim files.

## Research question

For the shortcut Collatz map

\[
T(n)=\begin{cases}
n/2,&n\equiv0\pmod 2,\\
(3n+1)/2,&n\equiv1\pmod 2,
\end{cases}
\]

which runs of consecutive residues modulo \(2^L\) have the same \(L\)-step image and the same number of odd steps? Which such runs are supercritical, meaning \(3^a>2^L\)?

## Method

`run.py` uses exact Python integers only. For every residue `r` modulo `2**L`, it computes:

- the chronological parity word of length `L`;
- the number `a` of odd steps;
- `T**L(r)`.

It groups maximal consecutive residues with identical `(a, output)` data. It then retains bundles satisfying `3**a > 2**L`.

The script also independently checks:

- the parity-affine constant formula from `L-0001`;
- the affine conjugacy from `T-0001` on selected lifted residue classes;
- the length-6, length-9, and length-17 concrete bundles;
- the `64 -> 81` nine-column carry cycle;
- the finite-horizon stack-amplification identity from `L-0002`.

## Command

```bash
python3 experiments/X-0001-collision-enumeration/run.py
```

## Environment

- Python 3.11 or newer recommended
- standard library only
- deterministic; no random seed

## Parameter range

The enumeration covers every residue for each `1 <= L <= 17`.

## Output

The checked-in output is:

```text
results/summary.txt
```

SHA-256 digests at the time of this contribution:

```text
86783e21bb62a3289a57518f3df91d88456b7804905c2227b5f3132c48a77b4a  run.py
2122c12c9bd860d44f99874fb2f26f75eb193d33829f4bbda2176d17586634df  results/summary.txt
```

## Interpretation

The search finds supercritical consecutive collision bundles beginning at length 6. The maximum width found through length 17 increases from 2 to 6. In particular, it verifies the exact six-way identity

\[
T^{17}(2^{17}q+9090+j)=3^{11}q+12302,
\qquad 0\le j\le5.
\]

This is evidence that collision alphabets can become larger. It does **not** establish an infinite admissible orbit of any induced radix map.

## Limitations

- The enumeration stops at `L=17`.
- A large collision alphabet is not by itself a counterexample.
- Arbitrarily long finite admissible prefixes would still not prove that one finite positive integer has an infinite trajectory.
- No claim about asymptotic bundle width is made.
