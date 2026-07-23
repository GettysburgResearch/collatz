# X-9609 — Exact eleven-defect normalized half-join

This experiment supports proposed theorem `T-9605`.

It exhausts every residual eleven-defect type after the centered contraction reduction and every normalized largest-gap row with `R<23`. Rows `R>=23` are excluded by the theorem's uniform height bound.

## Authoring search

`run.cpp` uses the split

```text
5 exceptional letters | 6 exceptional letters
```

and the exact congruence

```text
E_left * 2^(-A_left)
+ E_right * 3^(-k_right)
== 0 mod D.
```

The join key contains:

- the multiset of high valuations used on the left;
- the retained neutral-gap sum;
- the normalized residue.

Thus a match corresponds to one complete exceptional multiset and one complete normalized gap vector, not to unrelated half words.

Frozen totals:

```text
finite rows                         258
full candidates represented          27,283,361,062
left normalized states                   84,513,178
right normalized states                 122,629,329
formal divisor hits                                0
nontrivial cycle hits                              0
```

Row SHA-256:

```text
d1b2a4105d0f4bcf67d9e49584c202f77b022f67d0945079ebb04bb3735c62d8
```

Canonical JSON SHA-256:

```text
98d5318baed7eee50eaf276964058cd1253d0a6aede850f71bb960382a7dfe9c
```

## Independent verifier

`verify.cpp` reverses the split to `6+5` and hashes the smaller right side. It checks every row that can pass the exact height test:

```text
finite rows                 130
full candidates represented 188,604,494
left states                 9,327,609
right states                1,267,097
formal divisor hits         0
```

`verify_height.py` independently reconstructs:

- the cyclic contraction boundary;
- the exact finite height ranges;
- the universal `R>=23` bound.

The authoring and verification programs deliberately use different half orientations.

## Replay

```bash
g++ -O3 -std=c++17 -Wall -Wextra -Wpedantic \
  experiments/X-9609-eleven-defect-mitm/run.cpp \
  -o /tmp/x9609

/tmp/x9609 > /tmp/x9609.json

diff -u \
  experiments/X-9609-eleven-defect-mitm/results/canonical.json \
  /tmp/x9609.json

python3 experiments/X-9609-eleven-defect-mitm/verify_height.py

g++ -O3 -std=c++17 -Wall -Wextra -Wpedantic \
  experiments/X-9609-eleven-defect-mitm/verify.cpp \
  -o /tmp/x9609-verify

/tmp/x9609-verify
```

## Scope

This is exact finite arithmetic, but it proves only the frozen eleven-defect layer when combined with `T-9605`'s mathematical reductions. It supplies no positive cycle, divergent orbit, or Collatz counterexample.