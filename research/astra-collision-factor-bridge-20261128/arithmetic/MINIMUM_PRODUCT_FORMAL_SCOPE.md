# Finite native minimum-product kernel

Date: 2026-11-28. [MinimumProduct.lean](MinimumProduct.lean) supplies the
exact integer arithmetic used by
[CRITICAL_TAIL_WITHOUT_PACKING.md](../collision/CRITICAL_TAIL_WITHOUT_PACKING.md).
It defines the genuine shortcut map, its finite native iterates, and the
number of odd departures recursively. Its four public roots prove:

1. the one-step cap
   \(2T(n)m^{n\bmod2}\le n(3m+1)^{n\bmod2}\) when \(m\le n\);
2. for a finite prefix all of whose departed states are at least \(m\),
   \[
   2^s m^{a_s(n)}T^s(n)\le n(3m+1)^{a_s(n)};
   \]
3. when the source is \(m>0\) and all states through the endpoint are
   at least \(m\),
   \[
   2^s m^{a_s(m)}\le(3m+1)^{a_s(m)};
   \]
4. for such a finite minimum with \(m\ge3\),
   \[
   2^s3^{a_s(m)}\le10^{a_s(m)}.
   \]

The last result is the exact arithmetic behind
\(a_s(m)\ge s\log2/\log(10/3)\). The logarithmic conversion, Gaussian
clock laws, critical signed inequalities, and universal-convergence
consequence remain written proofs. Every lower-state premise is explicit
and finite; the module assumes no oracle for finding an all-time minimum.

The [completed receipt](../../../reports/astra-collision-factor-bridge-20261128/arithmetic/minimum-product-lean.json)
records a fresh source compilation and a separate import/type/axiom audit
of all four roots on 2026-11-28 at 11:42:15 UTC. Lean 4.34.1 and Mathlib
commit `d13f23b723b8a846827a245b89c10fc7d3f11612` were used. Only
`Quot.sound` and `propext` occur in the root audit. The compiler treated
warnings as errors, and source stability was checked across the run.

Source SHA256:
`e2874bd79b99bafef976cfbdaa20b7910ff51055c6ff7ff66abef19973da8f1a`.
Runner SHA256:
`e9ab1dfa3e5b88f5d5ca017a433eb0d4cd660874787b331ecc32772747972c4f`.

Reproduce using

```sh
python -X utf8 -B research/astra-collision-factor-bridge-20261128/arithmetic/check_minimum_product.py --lean /workspace/scratch/102b17af18c9/toolchains/lean-4.34.1-linux/bin/lean --mathlib /workspace/scratch/f139035b63c2/mathlib4 --receipt reports/astra-collision-factor-bridge-20261128/arithmetic/minimum-product-lean.json
```

The runner reuses the pinned compiled dependency cache; this is not a
cold rebuild of Mathlib or an independent LeanChecker replay.
