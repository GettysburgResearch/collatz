# H-frontier claim inventory addendum: Iterations 13--15

This append-only ledger supplements `CLAIM_INVENTORY.md`, whose original
`D/L/T/R/Q-9500` entries remain unchanged.  All theorem-level claims below are
`PROPOSED` pending independent reconstruction.  Source-dependent claims retain
that label explicitly.

## Packet files

- [`claims/ITERATION_13.md`](claims/ITERATION_13.md) — `T-9520`, `L-9531`,
  `R-9511`, `Q-9515`.
- [`claims/ITERATION_14.md`](claims/ITERATION_14.md) — `L-9532`, `T-9522` and
  the Tao bounded-surplus/logarithmic-band consequences recorded there.
- [`claims/ITERATION_14B.md`](claims/ITERATION_14B.md) — `T-9523`.
- [`claims/ITERATION_15.md`](claims/ITERATION_15.md) — `L-9533`--`L-9535`,
  `T-9524`, `R-9512`, `Q-9517`.

## Status table

| ID | Title | Status | Main dependency / caveat |
| --- | --- | --- | --- |
| `T-9520` | Architecture-level ordinary extraction | PROPOSED | nested positive seed sets; exact H cylinders |
| `L-9531` | H-native constant expanding ghost family | PROPOSED | exact H block maps |
| `R-9511` | Compatibility plus expansion does not extract an integer | PROPOSED | consequence of `L-9531` |
| `Q-9515` | Full H least-root decision | IDEA | boundedness/stabilization versus divergence |
| `L-9532` | Bounded supercritical surplus forces linear orbit size | PROPOSED | exact shortcut affine identity |
| `T-9522` | Fixed surplus bands are logarithmically time-null | PROPOSED / SOURCE-DEPENDENT | Tao Theorem 1.3; PR #77 divergence |
| `T-9523` | Every divergent Collatz spine is logarithmically sparse | PROPOSED / SOURCE-DEPENDENT | Tao Theorem 1.3 |
| `L-9533` | Tao transport for moving exceptional families | PROPOSED / SOURCE-DEPENDENT | Tao Theorem 1.3 |
| `L-9534` | Side-branch logarithmic sparsity and correction-product comparison | PROPOSED / SOURCE-DEPENDENT | `L-9533`; exact product identity |
| `T-9524` | Correction products are negligible at physical records | PROPOSED / SOURCE-DEPENDENT | `L-9534` |
| `L-9535` | Exact raw parity-approximation deficiency | PROPOSED | elementary affine/surplus identities |
| `R-9512` | Fixed-root inverse-tree mass does not invoke Tao | PROPOSED | quantifier/scope audit |
| `Q-9517` | Diagonal high-first-hit basin harmonic mass | IDEA | sufficient contradiction target |

## Latest Lane-A frontier

Subject to the imported source claims and the current PR #77 status, an
all-time coefficient-supercritical ordinary orbit must satisfy:

```text
x_k -> infinity;
D_k -> infinity in natural density one;
mean D_k >= (8/9) log_3 k - O_n(1);
liminf D_k/k = 0 (source-qualified López--Stoll);
spine and odd side branches have logarithmic density zero;
log P_r = o(log x_r) at physical records;
max_(k<=K) D_k >= (1-o(1)) log_3 K;
every raw parity approximant has exact exponent below one.
```

No contradiction is claimed.  The three exact remaining routes are:

1. prove `Q-9517`, producing positive logarithmic mass in a diagonal moving
   high-first-hit inverse basin;
2. prove PR #81 `SC*`, the cofinal escape of canonical supercritical sources;
3. construct derived rational approximants that beat the exact deficiency in
   `L-9535` by a uniform positive height margin.

## Report

- [`../../reports/gpt56-h-01/2026-08-01-17-tao-side-branch-record-bank.md`](../../reports/gpt56-h-01/2026-08-01-17-tao-side-branch-record-bank.md)
