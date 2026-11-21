/-
Shadow law. For `N = 3^k·m - c`, one ordinary step of `N` is one ordinary step of `m`
together with one step of the `3x-1` map on the constant.
-/
import Collatz.Closure

open CollatzReverseBasin

namespace CollatzClosure

/-- The `3x-1` shortcut map. -/
def S (c : Nat) : Nat := if c % 2 = 0 then c / 2 else (3*c - 1) / 2

/-- Even `m`: the constant takes one `3x-1` step; the exponent counts its odd steps. -/
theorem shadow_even (k j c : Nat) (hc : c < 3^k * (2*j)) :
    shortcut (3^k * (2*j) - c) = 3^(k + c % 2) * j - S c := by
  have e1 : 3^k * (2*j) = 2 * (3^k * j) := by grind
  have e2 : 3^(k+1) * j = 3 * (3^k * j) := by grind
  rw [e1] at hc ⊢
  rcases Nat.mod_two_eq_zero_or_one c with h | h
  · have hS : S c = c / 2 := by simp [S, h]
    rw [h, Nat.add_zero, hS]
    unfold shortcut
    generalize 3^k * j = Y at hc ⊢
    split <;> omega
  · have hS : S c = (3*c - 1) / 2 := by simp [S, h]
    rw [h, e2, hS]
    unfold shortcut
    generalize 3^k * j = Y at hc ⊢
    split <;> omega

/-- Odd `m`: the constant first absorbs `3^k`, then takes one `3x-1` step. -/
theorem shadow_odd (k m c : Nat) (hm : m % 2 = 1) (hc : c < 3^(k+1) * m) :
    shortcut (3^(k+1) * m - c) = 3^(k + (c + 3^k) % 2) * shortcut m - S (c + 3^k) := by
  have hs : 2 * shortcut m = 3*m + 1 := by unfold shortcut; split <;> omega
  have e0 : 3^(k+1) * m + 3^k = 3^k * (2 * shortcut m) := by
    rw [hs]; grind
  have e3 : 3^(k+1) * m - c = 3^k * (2 * shortcut m) - (c + 3^k) := by omega
  have hc' : c + 3^k < 3^k * (2 * shortcut m) := by omega
  rw [e3]
  exact shadow_even k (shortcut m) (c + 3^k) hc'

end CollatzClosure
