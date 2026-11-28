import Mathlib.Logic.Function.Iterate
import Lean.Elab.Tactic.Omega

/-! A finite kernel for the genuine minimum and its next parity.
The all-time minimum premise is explicit; it is not a stopping oracle. -/

namespace Collatz.NativeMinimum

def shortcut (n : ℕ) : ℕ := if n % 2 = 0 then n / 2 else (3 * n + 1) / 2

private theorem shortcut_even {n : ℕ} (h : n % 2 = 0) :
    shortcut n = n / 2 := by simp [shortcut, h]

private theorem shortcut_odd {n : ℕ} (h : n % 2 = 1) :
    shortcut n = (3 * n + 1) / 2 := by simp [shortcut, h]

theorem minimum_is_odd {m : ℕ} (hm : 0 < m) (h : m ≤ shortcut m) :
    m % 2 = 1 := by
  by_cases he : m % 2 = 0
  · rw [shortcut_even he] at h
    omega
  · omega

theorem two_step_non_descent_iff {m : ℕ} (hm : 0 < m) :
    (m ≤ shortcut m ∧ m ≤ shortcut (shortcut m)) ↔
      m = 1 ∨ m % 4 = 3 := by
  constructor
  · rintro ⟨h1, h2⟩
    have hodd := minimum_is_odd hm h1
    by_cases h3 : m % 4 = 3
    · exact Or.inr h3
    · have h4 : m % 4 = 1 := by omega
      have ht : shortcut m = (3 * m + 1) / 2 := by simp [shortcut, hodd]
      have hteven : shortcut m % 2 = 0 := by rw [ht]; omega
      rw [shortcut_even hteven, ht] at h2
      exact Or.inl (by omega)
  · rintro (rfl | h3)
    · decide
    · have hodd : m % 2 = 1 := by omega
      have ht : shortcut m = (3 * m + 1) / 2 := by simp [shortcut, hodd]
      have htodd : shortcut m % 2 = 1 := by rw [ht]; omega
      constructor
      · rw [ht]; omega
      · rw [shortcut_odd htodd, ht]
        omega

theorem minimum_second_parity {m : ℕ} (hm : 0 < m)
    (lower : ∀ t : ℕ, m ≤ shortcut^[t] m) :
    shortcut m % 2 = 0 ↔ m = 1 := by
  have h1 : m ≤ shortcut m := by simpa using lower 1
  have h2 : m ≤ shortcut (shortcut m) := by
    simpa [Function.iterate_succ_apply] using lower 2
  rcases (two_step_non_descent_iff hm).mp ⟨h1, h2⟩ with h | h
  · subst m
    decide
  · have hodd : m % 2 = 1 := by omega
    have htodd : shortcut m % 2 = 1 := by simp [shortcut, hodd]; omega
    constructor
    · intro hzero
      omega
    · intro hone
      omega

theorem postminimum_orbit {n m a : ℕ} (hit : shortcut^[a] n = m) (j : ℕ) :
    shortcut^[a + j] n = shortcut^[j] m := by
  rw [Nat.add_comm a j, Function.iterate_add_apply shortcut j a n, hit]

theorem second_parity_zero_iff_reaches_one {n m a : ℕ} (hm : 0 < m)
    (hit : shortcut^[a] n = m)
    (lower : ∀ t : ℕ, m ≤ shortcut^[t] n) :
    shortcut^[a + 1] n % 2 = 0 ↔ ∃ t : ℕ, shortcut^[t] n = 1 := by
  have ownlower : ∀ j : ℕ, m ≤ shortcut^[j] m := by
    intro j
    have hj := lower (a + j)
    rw [postminimum_orbit hit j] at hj
    exact hj
  have hnext : shortcut^[a + 1] n = shortcut m := by
    simpa using postminimum_orbit hit 1
  rw [hnext, minimum_second_parity hm ownlower]
  constructor
  · intro h
    exact ⟨a, hit.trans h⟩
  · rintro ⟨t, ht⟩
    have h := lower t
    rw [ht] at h
    omega

end Collatz.NativeMinimum
