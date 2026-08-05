# X-9615 — Depth-fifteen two-sided pulse phase floor

This exact certificate supports `T-9611`.

It exhausts the complete depth-fifteen boundary phase table:

```text
past suffixes:     32,768
future prefixes:   32,768
ordered CRT pairs: 1,073,741,824
```

The finite computation is a source/output **phase certificate**, not a cycle-period or orbit-prefix search. Once the phase floor is certified, the theorem applies to every macro ordering and every repetition length in the declared fixed-weight family.

Two independent implementations are supplied:

- `run.cpp` uses the closed affine word formula;
- `verify.cpp` reconstructs source cylinders by iterative local residue lifting and imports no generator module.

Both also check every exact parameter inequality for `244<=a<=375`, its 28 monotone endpoint rows, and the first failure of this depth-fifteen inequality at `a=376,b_0=77`.

Replay from the repository root:

```bash
g++ -O3 -std=c++17 -Wall -Wextra -Wpedantic \
  experiments/X-9615-depth15-phase-floor/run.cpp \
  -o /tmp/x9615-run

g++ -O3 -std=c++17 -Wall -Wextra -Wpedantic \
  experiments/X-9615-depth15-phase-floor/verify.cpp \
  -o /tmp/x9615-verify

/tmp/x9615-run --check-results \
  experiments/X-9615-depth15-phase-floor/results/canonical.json

/tmp/x9615-verify \
  experiments/X-9615-depth15-phase-floor/results/canonical.json
```

Expected output:

```text
X-9615 canonical results match
all independent X-9615 depth-15 phase checks passed
```

Frozen file SHA-256 values:

```text
run.cpp
773b700985e98822028d31d80d80b98372519c3f3163b1d8dbb16c383a7432cf

verify.cpp
d891c5d95cccc5d8cb8a8a2eb7b1e05cd08f9ae83687ef04d6db16434a2abfc3

canonical.json
9c10234f19e6486501510e29afd20f70efcd379303f3cae47fdceb6dd838175b
```

The exact result is

```text
H_15 = 874,917,472,129,210,216,448.
```

No cycle, divergent seed, or `K-####` object is produced.
