# ψ-closure route: the whole conjecture from one closure lemma, in dependency-free Lean

**Status: OPEN.** Collatz is not proved here. This packet is an attempt at a complete proof that
is honest about where it stops: every step except one named hypothesis is machine-checked.

## Map and normalization

Shortcut map on positive integers: `T(n) = n/2` for even `n`, `(3n+1)/2` for odd `n`.
`C` (Lean: `Basin`) is the set of positive integers whose `T`-orbit reaches 1.
`ψ(m) = 2m − 1`, so `T(ψ(m)) = 3m − 1`.

## What is machine-checked

Lean 4.34.1, **no Mathlib, no other dependency**, no `sorry`, standard axioms only.
Build: `cd lean && lake build` (seconds). Audit: `lake env lean -DwarningAsError=true Audit.lean`.

| Lean name | Statement | Evidence |
|---|---|---|
| `collatz_of_open_lemma` | `OpenLemma → ∀ n > 0, n ∈ C` | Lean |
| `collatz_iff_open_lemma` | Collatz ⟺ `OpenLemma` | Lean |
| `collatz_iff_psi_forward` | Collatz ⟺ `C` is closed under `ψ` | Lean |
| `basin_pow_two_pred` | `2^k q − 1 ∈ C ⟺ 3^k q − 1 ∈ C` for all `k`, `q > 0` | Lean |
| `basin_pow_four_succ` | `4^i v + 1 ∈ C ⟺ 3^i v + 1 ∈ C` for all `i`, `v` | Lean |
| `first_layer_iff_pow_three` | first layer of the lemma ⟺ every power of three is in `C` | Lean |
| `fail_mod4_one/two/three/zero` | transport of a closure failure by `m mod 4` | Lean |

`OpenLemma` is: for every `k` with `4 ∤ k`, if `3(27k+1) − 1 ∈ C` then `27k+1 ∈ C`.

## Dependencies

`lean/Collatz/ReverseBasin146.lean` is PR #146's `ReverseBasin.lean` at head
`e238c63a5d57f96bb063b7472498d1977df51951`, byte for byte apart from replacing its Mathlib
import with a four-line Lean-core shim. `collatz_iff_open_lemma` is that file's
`collatz_iff_deep_reverse_binary` moved into ψ-coordinates. Everything in
`lean/Collatz/Closure.lean` is new in this packet.

## First unsupported step

`OpenLemma` itself. See the sections below as they are added.
