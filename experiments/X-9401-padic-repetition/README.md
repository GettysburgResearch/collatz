# X-9401 — Exact checks for p-adic repetition rigidity

Experiment ID: X-9401
Issue: #18
Agent: `gpt56-complexity-01`
Status: EMPIRICAL support and interface verification; not an infinite proof

## Research question

Do the exact rational-height, first-difference valuation, and
repeated-factor prefix identities used by L-9401, L-9402, T-9401, and
T-9402 survive exhaustive small cases and adversarial boundary tests?

## Code

```text
run.py
```

The script uses only the Python standard library and exact `Fraction`
arithmetic.

## Command

From the repository root:

```bash
python3 -B experiments/X-9401-padic-repetition/run.py \
  --check-results experiments/X-9401-padic-repetition/results/canonical.json
```

To regenerate the frozen result:

```bash
python3 -B experiments/X-9401-padic-repetition/run.py \
  --write-results experiments/X-9401-padic-repetition/results/canonical.json
```

## Frozen parameters

- all binary prefixes of lengths `0..6`;
- all nonempty binary periods of lengths `1..6`;
- all pairs from a separate small eventual-code presentation corpus for the
  exact first-difference valuation;
- every binary word of length `11`, every repeated-factor placement visible
  in that word, including overlaps;
- length-`16384` finite prefixes for illustrative complexity profiles at
  factor lengths `1,2,4,8,16,32,64`;
- pseudorandom seed `9401` where applicable.

## Checks

1. The explicit numerator/denominator formula equals an independently
   assembled geometric sum.
2. The unreduced and reduced denominators are odd.
3. The reduced denominator divides
   `81^r*(81^s-64^s)` and is strictly below `81^(r+s)`.
4. Every periodic rational lies in `[0,1]` in the real embedding.
5. For distinct eventually periodic codes, the numerator of the rational
   difference has valuation exactly six times the first differing position.
6. Equal factors at positions `r<t` force agreement with periodic
   continuation through position `t+ell`, including overlapping factors.
7. Familiar low-complexity words are profiled only as illustrations of the
   scale in T-9402.

## Output digest

The environment-independent SHA-256 of `results/canonical.json` is:

```text
c19c075ceaf0883e989e8050028f29cfd58740e1ce507e15f380242f753d5086
```

## Interpretation and limitations

The finite assertions above are exact for the frozen ranges.  They do not
prove the universal theorems, do not find an ordinary M1 witness, and do not
show that no such witness exists.  The claim files contain the proofs; this
experiment is designed to expose indexing, denominator, overlap, and
valuation mistakes.
