# Cycle lane: the moving-prime obstruction

The main written result is in [MOVING_PRIME_CYCLE_ATTEMPT.md](MOVING_PRIME_CYCLE_ATTEMPT.md).
For every finite set of primes and every positive real floor, it constructs
primitive positive rational shortcut cycles above that floor which are
integral at every prescribed prime. Every state retains the same full,
nontrivial reduced denominator. This defeats the attempted replacement of
all distinguished denominator ideals by a fixed finite set of local tests,
even after imposing a large real minimum and the strict positive-cycle cone.

The construction does **not** exclude positive integer cycles. An adaptive
argument inspecting all factors of each actual denominator is untouched.
The written closing attempt identifies the missing general-word identity
and records why the cyclic integer-lattice reformulation supplies no such
identity by itself.

## Exact finite Lean result

[lean/BalancedCycleUnit.lean](lean/BalancedCycleUnit.lean) proves, for

    C(A,p) = Σ i < p, 2^(A*i/p) * 3^(p-1-i),
    D(A,p) = 2^A - 3^p,

that `Nat.Coprime (C A p) (D A p)` follows from `1 ≤ A`, `0 < p`,
`Nat.Coprime A p`, and `3^p < 2^A`. It then deduces that `D > 1`
implies `D ∤ C`.

The proof formalizes the actual floor exponents and their modular
permutation. It constructs the Bézout unit inside `ZMod D`, proves both
power relations, factors the literal numerator into a unit power and a
geometric sum, and exhibits that sum as a unit. The top theorem has no
supplied-root, supplied-permutation, factorization, or integer-cycle
hypothesis. It retains the complete denominator, including prime powers.

This is the finite balanced family underlying the written construction.
It does not formalize the infinite prime selection, rational dynamical
realization, all-rotation real floor, or exact primitive period. It does
not extend balanced coprimality to arbitrary parity words. The balanced
S-unit observation itself is credited to PR185 in the written note.

There are **8 theorems and 1 definition**. The exhaustive
[lean/BalancedCycleAudit.lean](lean/BalancedCycleAudit.lean) lists all nine
public declarations, including `carry`. Fresh compilation used
`-DwarningAsError=true`, Lean 4.34.1 at
`5045d0056413266e57c625dcd7c365b10e377c52`, and Mathlib at
`d13f23b723b8a846827a245b89c10fc7d3f11612`. All nine depend only on
`propext`, `Classical.choice`, and `Quot.sound`. There is no `sorry`,
extra axiom, or `native_decide`. Compiled objects were kept outside the
repository. [cycles-receipt.json](../../../reports/2026-11-23-high-variance/cycles-receipt.json) binds the exact sources and audit.

To reproduce, compile `BalancedCycleUnit.lean` into a fresh output
directory using the pinned Lean and Mathlib, add that directory plus
Mathlib's and its packages' `.lake/build/lib/lean` directories to
`LEAN_PATH`, and compile `BalancedCycleAudit.lean` with the same strict
option. The audit import is the freshly built local module. Exact commands and dependency
paths are recorded in [cycles-lean-replay.md](../../../reports/2026-11-23-high-variance/cycles-lean-replay.md); the local
`lean-toolchain` and `mathlib-revision` pin the dependencies.

## Exact controls and independent review

[check_moving_prime_controls.py](check_moving_prime_controls.py) checks two
constructed rational cycles, not a cycle census. It checks every odd
rotation, exact valuation gaps, the full denominator, the prescribed
prime exclusions, and the simultaneous real lower bound. Normal and
optimized Python runs produce identical
[moving_prime_controls.json](moving_prime_controls.json); checks remain
active under `python -O`.

| Prescribed primes | Prescribed floor | Odd count p | Shortcut period A | Integer part of minimum |
|---|---:|---:|---:|---:|
| 2, 3 | 1 | 97 | 156 | 14 |
| 2, 3, 5 | 2 | 3089 | 4900 | 264 |

These controls illustrate the formulas. The theorem for every finite
prime set and every real floor is supplied by the written proof, not
inferred from these examples.

The independent merger-lane reviewer checked Sections 1–4 of the written
proof at SHA256
`a6e8585f188899c08fd450d50fbbf85b53382bb5a4f6fea6440367d8c36bb3b1`.
The review explicitly checked every rotation, the absence of nonunit
cancellation, the uniform real floor, the elementary cyclotomic prime
selection, the strict cone, and primitivity. Its scope excludes the
unresolved general-word proposal in Section 5.
