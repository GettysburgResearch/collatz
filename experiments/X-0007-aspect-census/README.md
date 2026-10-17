# X-0007 — Exact normalized-aspect census through depth 22

Experiment ID: `X-0007`  
Issue: `#2`  
Agent: `gpt56-pro-01`  
Status: `EMPIRICAL` finite census and exact verification of `O-0007`

## Research question

Among all nontrivial supercritical collision fibers at a fixed depth, which maximize the normalized signed-return aspect ratio

\[
\Delta=rac{\operatorname{diam}D}{3^a-2^L}?
\]

The quantity is introduced in `T-0010`. It measures the length of the real fractional-part window available to a stationary signed rational-base return system.

## Method

`run.py`:

1. generates every affine residue table through depth 22 by the exact recursion of `L-0003`;
2. groups all supercritical residues by the pair
   \[
   (a_L(r),T^L(r));
   \]
3. computes every nontrivial fiber's exact diameter and radix gap;
4. selects a maximum-aspect fiber at each depth using exact cross multiplication;
5. breaks aspect ties by choosing the target of smallest magnitude;
6. independently verifies the four branches and negative-cycle interpretation of `O-0007`;
7. checks the full negative 11-cycle containing `-136`.

## Command

```bash
python3 -m py_compile experiments/X-0007-aspect-census/run.py
python3 experiments/X-0007-aspect-census/run.py
```

## Main finite observations

- The largest aspect ratio through depth 22 is the depth-six value
  \[
  1/17\approx0.0588235.
  \]
- The next largest value is
  \[
  5/139\approx0.0359712
  \]
  at depth 11.
- Depth 19 also has a comparatively large value
  \[
  89/7153\approx0.0124423.
  \]
- Large branch count does not correlate monotonically with large aspect ratio.

`O-0007` is a depth-11 maximum-aspect chart centered on the negative cycle phase `-136`. It is not the tie-breaking representative printed by the census, but has the same exact ratio `5/139` and the especially clean signed alphabet `{0,2,4,5}`.

## Interpretation

The census supports the strategic shift from cardinality to a joint chart profile:

```text
(branch structure, radix gap, normalized diameter, target graph, renewal compatibility)
```

Near-critical pairs of powers can produce relatively large windows even with small fibers. Negative cycle phases are especially natural because they provide a built-in positive-cycle-mean spine for `T-0013`.

## Limitations

- The census stops at depth 22.
- Maximum stationary aspect ratio is not a counterexample criterion.
- A graph-directed system may be useful even when no individual chart has a large stationary window.
- No positive-integer candidate is proposed.
