# X-9610 — Christoffel/Farey commutator audit

This exact standard-library experiment supports `L-9606` and `T-9606`.

It checks every ordered reduced Farey-neighbor pair whose two denominators are at most `100` and verifies

```text
r*q-p*s=1:
C(C_(p/q) C_(r/s))-C(C_(r/s) C_(p/q))
  =-2^(r+s-1) 3^(q-1),

r*q-p*s=-1:
C(C_(p/q) C_(r/s))-C(C_(r/s) C_(p/q))
  = 2^(p+q-1) 3^(s-1).
```

It also checks:

- contextual prefix/suffix multiplication of the commutator;
- every primitive standard factorization through denominator `100`;
- coprimality of the complete affine numerator and cycle denominator;
- upper/lower mechanical conjugacy;
- nonprimitive power decomposition;
- absence of a nontrivial positive cycle in the frozen rational-mechanical corpus.

Frozen totals:

```text
Farey-neighbor formulas                 12,174
contextual commutators                   14,014
primitive standard factorizations         3,043
full-denominator gcd checks               3,043
upper/lower rotation checks               3,043
rational mechanical words                 5,150
nonprimitive power checks                 1,907
nontrivial cycle hits                          0
```

Digests:

```text
semantic SHA-256
45bbd4de20d349d620f411fc31520d57bea07b19e7dc3914686ab339f684150c

canonical results SHA-256
351bd0fc54889ee07109cdac8dc7b5e4b7345b717be1f3b5826e7a0760d6c4dc
```

Replay:

```bash
python3 -B experiments/X-9610-christoffel-commutator/run.py \
  --check-results \
  experiments/X-9610-christoffel-commutator/results/canonical.json
```

The experiment is a finite interface audit. The all-denominator theorem is the proof in `T-9606`; no finite bound is extrapolated into a counterexample claim.