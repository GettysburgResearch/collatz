# Executable Lean route for the band-return attack

The imported results are the four byte-exact PR173 files at
`fa0c9e2a2851e6324391e39c17afcb5913185aec`, under `lean/vendor/`.
They retain their original flat imports and namespaces. See the source
record for repository provenance; `lean/vendor.sha256` checks
the local source bytes before compilation.

The toolchain is Lean **4.34.1**. Mathlib is pinned to
`d13f23b723b8a846827a245b89c10fc7d3f11612`, the upstream source's stated pin.
The build reuses an existing checkout and cache rather than installing
another toolchain or copying Mathlib into this repository.

## Build

Put the Lean 4.34.1 `bin` directory on `PATH` and set `MATHLIB_DIR` to the
pinned Mathlib checkout. From this directory, run:

```sh
MATHLIB_DIR=/absolute/path/to/mathlib4 bash lean/build.sh
```

This builds the necessary Mathlib imports and the compatible arithmetic
extraction `BandCore`, then compiles the exact local modules in order:

1. `ShellCover`
2. `ForwardSection`
3. `SectionDynamics`
4. `RisingReturns`

Generated Lean objects are kept in `lean/.build/`. The script puts that
directory, the local source directories, and Mathlib's full dependency
search path on `LEAN_PATH`. Every local Lean invocation treats warnings
as errors. No imported source is patched to make this route work.

Pass new flat module names as arguments in their dependency order, for
example:

```sh
MATHLIB_DIR=/absolute/path/to/mathlib4 bash lean/build.sh BandCertificates BandDescent
```

The initial local execution reused the existing Lean runtime and Mathlib
cache. Only three Mathlib modules needed compilation for the newly used
logarithm and Diophantine imports; that dependency build completed
successfully. The four exact vendor modules also compiled successfully
with warnings treated as errors. These local execution results are
separate from the final clean-commit publication check.

## Compatibility with the preceding core development

`BandCore.lean` copies the minimal orbit/count definitions, concatenation,
even-shift identity, high-bit lift, and affine lower bound from checkpoint2's
`OrbitLift.lean` and `Expansion.lean`. Their hashes are recorded in the
file and checked by `lean/core.sha256`. Changes are the namespace, naming
the ordinary map `step`, and renaming one local proof variable to avoid
shadowing that map. The proof assumptions are unchanged.

The preceding project's complete dependency chain intentionally installed
core substitutes for Mathlib's integer/natural notation, `ring` tactic, and
strong-induction name. Importing that chain together with Mathlib causes
a declaration collision, so this build uses the narrow extraction instead.
It does not modify either the original core files or the PR173 files.

`CollatzBandCertificates.core_orbit_eq_shell` is the explicit definitional bridge
between the extracted source-first orbit and PR173's clock-first orbit.
The new stopping-prefix and marked-family statements are expressed using
the actual PR173 definitions after that bridge.

## Interfaces used by the new work

The ordinary map and its orbit live in `CollatzShell`:

```lean
step : Nat → Nat
orbit : Nat → Nat → Nat  -- clock first, then initial value
Hits x y := ∃ t, orbit t x = y
Basin n := ∃ t, orbit t n = 1
Universal := ∀ n, 0 < n → Basin n
```

The new section interfaces live in `CollatzShell.ForwardSection`:

- `Marked n` asserts oddness and the exact dyadic-band inequality.
- `bounded_visit n hn` supplies a marked ordinary endpoint at a clock
  strictly below `4*n.sqrt+n.log2`.
- `returnTime n` is strictly positive; `next n` is the corresponding
  first positive marked return.
- `returnTime_min` compares that clock with any positive marked visit.
- `returns n k` iterates the induced return dynamics.
- `captures` places every marked ordinary endpoint into those dynamics.
- `collatz_iff_return_descent` is the exact equivalence between global
  convergence and eventual strict descent from every marked start above
  one. Its descent condition remains a proposition to prove.
- `arbitrarily_large_first_return` excludes unconditional contraction of
  each individual return in ordinary value.

The earlier core-only project uses a different namespace and a different
argument order for its orbit. New modules must state any bridge explicitly;
identically named concepts are not silently identified.

## New certificate result and its induction scope

`BandCertificates.lean` proves the following deterministic transport. If
an actual prefix satisfies `orbit t a < a`, its affine multiplier obeys
`3^oddCount(a,t) < 2^t`. Consequently every point of the binary cylinder

\[
a+2^t q\quad(q\ge0)
\]

has strict descent at the same ordinary clock. In particular, if `t <= d`,
then `2^d+a` strictly descends. A complete offset hit-to-one certificate
is sufficient, but a shorter stopping prefix already suffices.

For each fixed odd offset `a`, the explicit threshold `a <= d` ensures
that `2^d+a` is marked. Thus every certified odd offset above one supplies
an unbounded family of genuinely marked starts with actual ordinary
stopping certificates. This is an all-parameter result, not a finite scan.

Two induction distinctions remain explicit. A stopping endpoint need not
be marked, so ordinary descent alone does not instantiate PR173's marked
return-descent condition. Also, minimality among marked failures does not
supply an ordinary convergence floor below the marked start. The theorem
`basin_of_offset_stopping_floor` states the ordinary floor as a hypothesis;
it is not inferred from section membership or a certificate-weighted rank.

## Actual-state links for temporal marked frequency

`MarkPhase.lean` imports the newly checked `ReturnFourier` module. It makes
PR173's private marked-height estimate available through a credited public
proof and combines it with eventual escape of injective natural sequences.
Its public interfaces are:

- `marked_phase_small`: a marked integer has phase in
  `[0, 140/(log2(x)+1)]`.
- `injective_eventually_large`: an injective natural-valued sequence
  eventually leaves every fixed initial interval, without a monotonicity
  hypothesis.
- `marked_phase_eventually_small`: along such a sequence, every sufficiently
  late marked term has phase in any prescribed positive interval at zero.

These are pointwise state statements. The finite Fourier-kernel argument
that turns them into a temporal frequency bound is in the separately owned
`MarkFrequency.lean` module.
