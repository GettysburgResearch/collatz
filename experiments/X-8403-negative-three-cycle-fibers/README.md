# X-8403 — Negative-three-cycle fixed-weight pulse fibers

Experiment ID: `X-8403`  
Issue: #41  
Agent: `gpt56-complexity-01`  
Status: `EMPIRICAL / EXACT FINITE INTERFACE AUDIT`

## Questions

1. Do the two ordinary negative-three-cycle letters replay the advertised
   accelerated Collatz valuations exactly?
2. Does every fixed pulse count produce one common input radix and one common
   output multiplier?
3. Are the word cylinders distinct?
4. Do the first near-critical shapes have the claimed branch counts and exact
   integer multiplier inequalities?
5. How quickly does the least positive cylinder grow in the smallest six-branch
   chart?

## Exact letters

In the physical coordinate

```text
n=-5+2h,
```

the two exact two-odd-step blocks are

```text
A: h=8q    -> 9q,     valuations (1,2),
B: h=3+16q -> 3+9q,   valuations (2,2).
```

For a word of length `L` containing `b` letters `B`, the script reconstructs

```text
M=2^(3L+b),
N=9^L,
M F_w(h)=N h+C_w,
```

then computes the exact domain and output digits

```text
d_w=[-C_w N^(-1)]_M,
e_w=(N d_w+C_w)/M.
```

Every generated row is directly replayed both in the `h` coordinate and through
the advertised accelerated physical valuations.

## Frozen coverage

Complete branch generation and replay:

```text
(L,b)=(6,1):     6 branches
(L,b)=(12,2):   66 branches
(L,b)=(18,3):  816 branches
```

The near-critical exact comparisons are frozen for:

```text
(L,b)=(6,1),
(L,b)=(53,9),
(L,b)=(665,113).
```

The last chart has a `433`-bit branch count while satisfying

```text
2^2108 < 9^665 < 2^2109.
```

## Complete six-branch table

For `(L,b)=(6,1)`:

```text
M=2^19=524,288,
N=9^6=531,441.
```

| word | domain digit | output digit |
|---|---:|---:|
| `AAAAAB` | 360448 | 365367 |
| `AAAABA` | 471040 | 477468 |
| `AAABAA` | 267776 | 271431 |
| `AABAAA` | 366784 | 371790 |
| `ABAAAA` | 19416 | 19683 |
| `BAAAAA` | 349523 | 354294 |

## Exact finite minima

The least positive initial `h` surviving the first eight macro depths is:

| depth | classes | minimum positive `h` | bits |
|---:|---:|---:|---:|
| 1 | 6 | 19416 | 15 |
| 2 | 36 | 5726623059 | 33 |
| 3 | 216 | 134719124373504 | 47 |
| 4 | 1296 | 6621345703201609216 | 63 |
| 5 | 7776 | 2205800655210966882293952 | 81 |
| 6 | 46656 | 149782132437049025835992193216 | 97 |
| 7 | 279936 | 48083433279741938300363300079490387 | 116 |
| 8 | 1679616 | 544877977737345069246758429064839928000 | 129 |

These are complete finite minima, not an asymptotic nonexistence result.

## Replay

```bash
python3 -B experiments/X-8403-negative-three-cycle-fibers/run.py \
  --check-results \
  experiments/X-8403-negative-three-cycle-fibers/results/canonical.json
```

Expected ending:

```text
frozen result check passed
```

Canonical JSON SHA-256:

```text
b85bb5ee0e4ef2c59af21edfa7e689cff1ad71a7e8a2a2db055754341918c4bd
```

Semantic payload digest stored inside the JSON:

```text
b42ee3c1a1a8a9b8f962b43584ab31ac1c05fe13e62900500427dff69423384b
```

## Interpretation

`L-8405` proves the exact fixed-weight chart, and `T-8402` proves that such
charts can be made arbitrarily near-critical while retaining exponentially many
branches. Any nontrivial ordinary infinite path in a supercritical chart is an
unbounded Collatz trajectory.

The experiment does **not** construct that ordinary infinite path. The growing
finite minima are bounded evidence only; neither a compatible inverse limit nor
a modular lasso is an ordinary counterexample.
