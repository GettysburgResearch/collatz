# X-6200 — where the coverage deficit switches on

```text
Experiment ID:   X-6200
Agent:           claude-opus5-61
Claims:          O-6201
Serves:          issue #25
Runtime:         seconds (reuses the X-6180 profile)
```

## Contents

| file | purpose |
|---|---|
| `branching.py` | proves/verifies the branching factor is exactly `4/3` (`n` has 2 predecessors iff `n = 2 mod 3`) |
| `deficit.py` | per-level growth ratio against `4/3`, and `c(e)` vs the naive tree prediction |
| `escape_model.py` | parameter-free escape model; valid to `10%` below `X^0.66`, wrong beyond |
| `results/` | outputs |

## Commands

```sh
python3 branching.py > results/branching.txt
python3 deficit.py   > results/deficit.txt
```

## Result

The backward tree from `1` is a genuine tree (unique parent `T(n)`), so **the only loss is
nodes escaping above `X`**. It realises its full `4/3` branching to within `0.5%` for the first
`~32` levels — coverage up to `X^0.55` — and then decays: `88%` of ideal at `X^0.75`, `79%` at
`X^0.91`, `75%` at `X^0.99`.

The Krasikov-Lagarias-type exponent `0.84` sits at depth `62`, well past the onset. See O-6201.

## Limitations

Onset measured at `X = 10^8` only. The `c(e)` versus `c_naive(e)` comparison carries an
additive-constant ambiguity; the per-level ratio does not and is the published statement.
