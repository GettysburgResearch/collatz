import CycleWordAlgebra
import Mathlib.Data.Finset.Card
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity

/-!
# Exact finite compression for the global orbit count

The whole chronological carry is retained. The high-clock implication
and finite injection charge are proved here; the binomial asymptotic
and the infinite scale recursion are written in GLOBAL_ORBIT_COUNT.md.
-/

namespace CollatzShell.OrbitCounting

open Collatz.HighVariance.CycleWordAlgebra

set_option autoImplicit false

/-- A coarse but clock-exact bound for every complete shortcut carry. -/
theorem carry_lt_clock_product (w : List Bool) :
    carry w < 2 ^ w.length * 3 ^ ones w := by
  induction w with
  | nil => simp [carry, ones]
  | cons b w ih =>
    have h2 : 0 < 2 ^ w.length := by positivity
    have h3 : 0 < 3 ^ ones w := by positivity
    cases b with
    | false =>
      simp only [carry, Bool.false_eq_true, ite_false, mul_zero, zero_add,
        ones, List.length_cons, pow_succ]
      nlinarith
    | true =>
      simp only [carry, ite_true, mul_one, ones, List.length_cons,
        Nat.add_comm 1, pow_succ]
      nlinarith

/-- A complete word whose binary clock is large relative to the original
height sends that same source into a smaller height range. -/
theorem high_clock_compresses {w : List Bool} {n q X K m : Nat}
    (hm : ones w = m)
    (he : 2 ^ w.length * q = 3 ^ m * n + carry w)
    (hn : n ≤ X) (hX : X < 2 ^ (K + 1))
    (hclock : K ≤ w.length) (hscale : 8 * 3 ^ m ≤ X) :
    q < 3 * 3 ^ m ∧ 2 * q < X := by
  have h2 : 0 < 2 ^ w.length := by positivity
  have h3 : 0 < 3 ^ m := by positivity
  have hpow : 2 ^ (K + 1) ≤ 2 ^ (w.length + 1) := by
    exact Nat.pow_le_pow_right (by decide) (Nat.add_le_add_right hclock 1)
  have hn2 : n < 2 * 2 ^ w.length := by
    have hh := lt_of_le_of_lt hn hX
    have := lt_of_lt_of_le hh hpow
    simpa [pow_succ, Nat.mul_comm] using this
  have hn3 : 3 ^ m * n < 3 ^ m * (2 * 2 ^ w.length) :=
    Nat.mul_lt_mul_of_pos_left hn2 h3
  have hc := carry_lt_clock_product w
  rw [hm] at hc
  have hp : 2 ^ w.length * q < 2 ^ w.length * (3 * 3 ^ m) := by
    nlinarith
  have hq : q < 3 * 3 ^ m := (Nat.mul_lt_mul_left h2).mp hp
  exact ⟨hq, by omega⟩

/-- The high lane is charged injectively to a supplied lower set.
The image can cross arbitrarily large intermediate heights. Each word,
source, endpoint, full carry and both clocks remain explicit. -/
theorem high_lane_card_le (S lower : Finset Nat) (X K m : Nat)
    (word : Nat → List Bool) (endpoint : Nat → Nat)
    (hsrc : ∀ n ∈ S, n ≤ X)
    (hX : X < 2 ^ (K + 1)) (hscale : 8 * 3 ^ m ≤ X)
    (hones : ∀ n ∈ S, ones (word n) = m)
    (hclock : ∀ n ∈ S, K ≤ (word n).length)
    (he : ∀ n ∈ S,
      2 ^ (word n).length * endpoint n = 3 ^ m * n + carry (word n))
    (hclosed : ∀ n ∈ S, 2 * endpoint n < X → endpoint n ∈ lower)
    (hinj : ∀ n ∈ S, ∀ n' ∈ S, endpoint n = endpoint n' → n = n') :
    S.card ≤ lower.card := by
  apply Finset.card_le_card_of_injOn endpoint
  · intro n hn
    exact hclosed n hn (high_clock_compresses (hones n hn) (he n hn)
      (hsrc n hn) hX (hclock n hn) hscale).2
  · exact hinj

end CollatzShell.OrbitCounting
