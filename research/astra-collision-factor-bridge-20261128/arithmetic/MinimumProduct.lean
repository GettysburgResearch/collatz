import Mathlib.Data.Nat.Basic
import Mathlib.Tactic.Ring
import Lean.Elab.Tactic.Omega

/-! Finite native arithmetic for the minimum-based critical grade bound.
All lower-state premises are explicit and finite. No minimum-finding
oracle, density law, logarithmic limit, or Collatz conclusion is assumed. -/

namespace Collatz.MinimumProduct

def shortcut (n : ℕ) : ℕ :=
  if n % 2 = 0 then n / 2 else (3 * n + 1) / 2

def state : ℕ → ℕ → ℕ
  | 0, n => n
  | s + 1, n => state s (shortcut n)

def oddCount : ℕ → ℕ → ℕ
  | 0, _ => 0
  | s + 1, n => n % 2 + oddCount s (shortcut n)

theorem native_step_cap (m n : ℕ) (h : m ≤ n) :
    2 * shortcut n * m ^ (n % 2) ≤ n * (3 * m + 1) ^ (n % 2) := by
  by_cases he : n % 2 = 0
  · simp only [shortcut, he, ite_true, pow_zero, mul_one]
    omega
  · have ho : n % 2 = 1 := by omega
    have hn : 2 * shortcut n = 3 * n + 1 := by
      simp only [shortcut, he, ite_false]
      omega
    rw [ho, pow_one, pow_one, hn]
    ring_nf
    omega

theorem finite_prefix_cap (m n s : ℕ)
    (lower : ∀ j, j < s → m ≤ state j n) :
    2 ^ s * m ^ oddCount s n * state s n ≤
      n * (3 * m + 1) ^ oddCount s n := by
  induction s generalizing n with
  | zero => simp [state, oddCount]
  | succ s ih =>
    have hstep := native_step_cap m n (by simpa [state] using lower 0 (by omega))
    have htail : ∀ j, j < s → m ≤ state j (shortcut n) := by
      intro j hj
      simpa [state] using lower (j + 1) (by omega)
    have hind := ih (shortcut n) htail
    simp only [state, oddCount]
    calc
      2 ^ (s + 1) * m ^ (n % 2 + oddCount s (shortcut n)) *
          state s (shortcut n) =
        (2 * m ^ (n % 2)) *
          (2 ^ s * m ^ oddCount s (shortcut n) * state s (shortcut n)) := by
            rw [pow_succ, pow_add]
            ring
      _ ≤ (2 * m ^ (n % 2)) *
          (shortcut n * (3 * m + 1) ^ oddCount s (shortcut n)) :=
        Nat.mul_le_mul_left _ hind
      _ = (2 * shortcut n * m ^ (n % 2)) *
          (3 * m + 1) ^ oddCount s (shortcut n) := by ring
      _ ≤ (n * (3 * m + 1) ^ (n % 2)) *
          (3 * m + 1) ^ oddCount s (shortcut n) :=
        Nat.mul_le_mul_right _ hstep
      _ = n * (3 * m + 1) ^ (n % 2 + oddCount s (shortcut n)) := by
        rw [pow_add]
        ring

theorem minimum_cap (m s : ℕ) (hm : 0 < m)
    (lower : ∀ j, j ≤ s → m ≤ state j m) :
    2 ^ s * m ^ oddCount s m ≤ (3 * m + 1) ^ oddCount s m := by
  have hp := finite_prefix_cap m m s (fun j hj => lower j (Nat.le_of_lt hj))
  have hend := lower s (Nat.le_refl s)
  have hmul : (2 ^ s * m ^ oddCount s m) * m ≤
      ((3 * m + 1) ^ oddCount s m) * m := by
    calc
      _ ≤ (2 ^ s * m ^ oddCount s m) * state s m :=
        Nat.mul_le_mul_left _ hend
      _ ≤ m * (3 * m + 1) ^ oddCount s m := hp
      _ = _ := by ring
  exact Nat.le_of_mul_le_mul_right hmul hm

theorem minimum_three_cap (m s : ℕ) (hm : 3 ≤ m)
    (lower : ∀ j, j ≤ s → m ≤ state j m) :
    2 ^ s * 3 ^ oddCount s m ≤ 10 ^ oddCount s m := by
  have hp := finite_prefix_cap 3 m s
    (fun j hj => hm.trans (lower j (Nat.le_of_lt hj)))
  have hend := lower s (Nat.le_refl s)
  have hmul : (2 ^ s * 3 ^ oddCount s m) * m ≤
      (10 ^ oddCount s m) * m := by
    calc
      _ ≤ (2 ^ s * 3 ^ oddCount s m) * state s m :=
        Nat.mul_le_mul_left _ hend
      _ ≤ m * (3 * 3 + 1) ^ oddCount s m := hp
      _ = _ := by ring
  exact Nat.le_of_mul_le_mul_right hmul (by omega : 0 < m)

end Collatz.MinimumProduct
