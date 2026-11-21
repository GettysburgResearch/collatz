# ψ-closure route: the whole conjecture from one closure lemma, in dependency-free Lean

**Status: OPEN.** Collatz is not proved here. This packet is an attempt at a complete proof.
Every step except one named hypothesis, `OpenLemma`, is machine-checked. The attempts to
prove `OpenLemma` are recorded with the exact step where each stops.

## Map and normalization

Shortcut map on positive integers: `T(n) = n/2` for even `n`, `(3n+1)/2` for odd `n`.
`C` (Lean: `Basin`) is the set of positive integers whose `T`-orbit reaches 1.
`ψ(m) = 2m − 1`, so `T(ψ(m)) = 3m − 1`. `S` is the `3x−1` shortcut map:
`S(c) = c/2` for even `c`, `(3c−1)/2` for odd `c`.

## Machine-checked results

Lean 4.34.1, **no Mathlib, no other dependency**, no `sorry`; every theorem below depends
only on `propext`, `Classical.choice`, `Quot.sound`.

```
cd lean
lake build                                        # whole project, a few seconds
lake env lean -DwarningAsError=true Audit.lean    # axiom report
```

| Lean name | Statement |
|---|---|
| `collatz_of_open_lemma` | `OpenLemma → ∀ n > 0, n ∈ C` |
| `collatz_iff_open_lemma` | Collatz ⟺ `OpenLemma` |
| `collatz_iff_psi_forward` | Collatz ⟺ `C` is closed under `m ↦ 2m − 1` |
| `collatz_iff_three_minus_one_closure` | Collatz ⟺ `C` is closed under `x ↦ 3x − 1` |
| `basin_pow_two_pred` | `2^k q − 1 ∈ C ⟺ 3^k q − 1 ∈ C`, all `k`, all `q > 0` |
| `basin_pow_four_succ` | `4^i v + 1 ∈ C ⟺ 3^i v + 1 ∈ C`, all `i`, `v` |
| `first_layer_iff_pow_three` | the layer "`3m − 1` is a power of two" of the unrestricted closure ⟺ `∀ i, 3^i ∈ C` |
| `ladder_iff_pow_three` | the `x ↦ 3x − 1` orbit of 1 lies in `C` ⟺ `∀ i, 3^i ∈ C` |
| `fail_mod4_one/two/three/zero` | transport of a closure failure, by `m mod 4` |
| `shadow_even`, `shadow_odd` | `T(3^k m − c) = 3^{k'} T(m) − S(c*)`, with `c* = c` or `c + 3^{k−1}` |

`OpenLemma`: for every `k` with `4 ∤ k`, if `3(27k+1) − 1 ∈ C` then `27k+1 ∈ C`.

The two exponent families are proved by induction on the exponent. No bounded affine
certificate covers them, because their path lengths grow with the exponent.

## Dependencies and credit

`lean/Collatz/ReverseBasin146.lean` is PR #146's `ReverseBasin.lean` at head
`e238c63a5d57f96bb063b7472498d1977df51951`, byte for byte apart from replacing its Mathlib
import with a four-line Lean-core shim. `collatz_iff_open_lemma` is that file's
`collatz_iff_deep_reverse_binary` moved into ψ-coordinates. PR #146 also has the restricted
first layer (convergence of `3^(27j−1)`), in its Mathlib file; the unrestricted statement here
is proved independently in core Lean. The shadow law is the classical linearity of
`T`-iterates in the added multiple of a power of two, written for the form `3^k m − c`.
`lean/Collatz/Closure.lean` and `lean/Collatz/Shadow.lean` are new files.

## The attack and where it stops

The goal was to prove `OpenLemma`, which would finish the conjecture.

1. **Frame.** Collatz is closure of `C` under `x ↦ 3x − 1` (Lean). PR #146 shows the reverse
   implication on one sparse class already suffices; that is `OpenLemma`.
2. **Synchronous descent.** For `m ≡ 1 (mod 4)` a failure at `m` moves to a failure of the
   same relation at `(3m+1)/4 < m` (Lean, `fail_mod4_one`). On the class of `OpenLemma` this
   is exactly the excluded case `4 | k`. On the three remaining residues the relation leaves
   `3x − 1`: it becomes `3x − 2` at a smaller point, `x − 1` at a larger point, or `27x − 1`
   at `m/4` (Lean, `fail_mod4_two/three/zero`).
3. **Contradiction states.** Continuing the transport, a failure is refuted exactly when the
   two arms meet under ordinary steps on a whole residue class. Outside those classes the
   transported relation never returns to `3x − 1` at a smaller point of the class, so
   induction on size does not close.
4. **Induction on the member arm.** Ordering failures by the number of odd steps of the
   convergent arm, the first layer is the case where `3m − 1` is a power of two. That layer
   is equivalent to `∀ i, 3^i ∈ C` (Lean). No step in this packet proves that statement.
5. **Shadowing.** Along the orbit of `m`, the orbit of `3^k m − c` is `3^{k_t} T^t(m) − c_t`,
   where `c_t` follows the `3x−1` map and absorbs `3^{k−1}` at each odd step of `m` (Lean).
   When the convergent arm reaches 1 this gives `3^{k_t} T^t(m) = c_t + 1`, which is
   consistent with a non-convergent `m`; it yields no contradiction.

**First unsupported step:** `OpenLemma`. Its weakest sub-instance in the unrestricted form is
`∀ i, Basin (3^i)`.

## Evidence levels

- Lean theorems: as listed, checked by the two commands above on this branch.
- Items 3 and the last sentence of item 5 are written reasoning (PROPOSED), not Lean.
- Not run: any Mathlib build of PR #146's `HighBit.lean`; no numerical search was run for
  this packet.

## Handoff

A method that closes `OpenLemma` must in particular prove `∀ i, Basin (3^i)`; that
statement is ready as a Lean target through `first_layer_iff_pow_three` and
`ladder_iff_pow_three`. The Lean project is self-contained, so new lemmas can be added and
checked with `lake build` alone.
