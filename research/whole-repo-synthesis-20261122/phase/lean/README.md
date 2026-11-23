# Finite ordinary phase estimate in Lean

This packet formalizes a finite estimate from **literal ordinary edge
equalities**, including the conversion to real logarithms and complex
integer-frequency phases. It does not prove Collatz convergence, an
asymptotic discrepancy theorem, or a Diophantine lower bound for the
rotation denominator.

For natural-number sequences `q` and `gap`, an integer frequency `h`, and
a length `N`, the final theorem requires:

- `q i > 0` for `i <= N`;
- the first `N` values `q 0, ..., q (N-1)` are distinct;
- `2 ^ gap i * q (i+1) = 3 * q i + 1` for every `i < N`.

No phase recurrence is supplied as an extra premise. The module derives
it from those ordinary equalities and proves, with
`e(t) = exp(2 pi I t)` and `H_N` the harmonic number,

\[
 \left|e(h\log_2 3)-1\right|
 \left|\sum_{i<N}e(h\log_2 q_i)\right|
 \le 2+\frac{2\pi|h|}{3\log2}H_N
 \le 2+\frac{2\pi|h|}{3\log2}(1+\log N).
\]

The proof includes the reciprocal rearrangement for distinct positive
integer denominators, the exact logarithmic edge identity, the summed
logarithmic error, integer-frequency exponential periodicity, and the
finite complex telescope. Oddness need not be imposed separately for
this algebraic estimate; an ordinary accelerated odd segment supplies
the displayed edge hypotheses. No global orbit or cycle claim is
inferred from them.

## Rebuild without changing the checkout

The required compiler is Lean 4.34.1. Mathlib is pinned at
`d13f23b723b8a846827a245b89c10fc7d3f11612`; the four direct imported
source files are additionally recorded in `imports.sha256`. Their
transitive compiled dependencies must already be available in that
checkout. The script does not install or rebuild Mathlib.

Run, substituting the paths of the existing pinned installations:

```bash
python3 build.py \
  --mathlib /absolute/path/to/mathlib4 \
  --lean /absolute/path/to/lean-4.34.1-linux/bin/lean \
  --lake /absolute/path/to/lean-4.34.1-linux/bin/lake \
  --output /absolute/path/outside/the/repository/phase-check
```

The output directory is required to be outside the repository. If
omitted, a fresh temporary directory is created. It receives compiled
objects, compiler logs, and `receipt.json`; the source checkout remains
unchanged. The script compiles only `ActualPhaseEstimate.lean` and its
separate audit module, with `autoImplicit=false` and warnings treated as
errors.

The audit prints the axiom dependencies of **every public definition
and theorem in this packet**. The driver checks exact audit coverage
and permits only `propext`, `Classical.choice`, and `Quot.sound`. A build
receipt is evidence of the listed finite formal statements only.
