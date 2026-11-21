# Dyadic-band descent: exact offset certificates

**Checkpoint 1. Full Collatz remains OPEN.** This work builds directly on
PR173 at `fa0c9e2a2851e6324391e39c17afcb5913185aec`. Its ordinary shortcut
map, forced narrow section, and first-return dynamics are unchanged.

## Verified result at this checkpoint

Let `p(t,r)` count the odd inputs during the first `t` shortcut steps of `r`.
Lean checks the exact identity

\[
T^t(2^t q+r)=3^{p(t,r)}q+T^t(r).
\]

For a contracting prefix `3^p < 2^t` and a positive ordinary quotient `q`,
strict descent is equivalent to the explicit threshold

\[
q\ge 1+\left\lfloor
\frac{\max(T^t(r)-r,0)}{2^t-3^p}
\right\rfloor.
\]

This retains the affine correction. The finite evaluator `accepts` is proved
both sound and complete for actual strict descent of this lifted input.
Accepting one positive quotient certifies every larger quotient.

An actual descent of the offset at clock `t` therefore certifies strict
descent of every `2^d+r` with `d >= t`. More generally, a supplied convergence
certificate for a fixed positive offset gives strict descent on its entire
ray of sufficiently large dyadic lifts; the offset `r=1` is handled by the
actual two-step cycle.

These conclusions are **strict descent**, not convergence of every lifted
input. They do not assert that the smaller endpoint is marked. The remaining
work is to produce descending marked endpoints and cover every marked source.

## Lean and provenance

- [OffsetDescent.lean](OffsetDescent.lean): exact affine transport, threshold,
  sound and complete finite checker, terminal-cycle padding, and dyadic rays.
- [SOURCES.json](SOURCES.json): exact upstream source hashes and toolchain pins.

`OffsetDescent.lean` was compiled with Lean 4.34.1, mathlib at
`d13f23b723b8a846827a245b89c10fc7d3f11612`, and warnings treated as errors.
Its printed principal axiom closures are subsets of `propext`,
`Classical.choice`, and `Quot.sound`. No conjectural axiom or admitted proof
is used. The source dependency is PR173's unchanged `ShellCover.lean`.

From that pinned, built mathlib checkout, compile `ShellCover.lean` first,
put its output directory on `LEAN_PATH`, and run:

```bash
lake env lean -j1 -R /absolute/path/to/this/directory \
  -DwarningAsError=true /absolute/path/to/this/directory/OffsetDescent.lean
```

This checkpoint is research progress toward the full theorem, not a completed
proof. Subsequent marked-return and phase arguments are developed separately
and are not claimed as part of this checkpoint.
