import Mathlib.Logic.Function.Iterate
import Mathlib.Tactic.NormNum

/-! First-merger time slices on the actual positive shortcut graph. -/

namespace Collatz.OrdinaryAntichain

set_option autoImplicit false

def step (x : ℕ) : ℕ := if x % 2 = 0 then x / 2 else (3 * x + 1) / 2

def upper (x : ℕ) : ℕ := 3 * x - 1

private theorem step_even (k : ℕ) : step (2 * k) = k := by
  simp [step]

private theorem step_odd (k : ℕ) : step (2 * k + 1) = 3 * k + 2 := by
  simp [step]
  omega

/-- The same physical pair is distinct at three and equal at four. -/
theorem exact_four (u : ℕ) :
    let x := 3 + 16 * u
    step^[3] x ≠ step^[3] (upper x) ∧ step^[4] x = step^[4] (upper x) := by
  dsimp only
  have a₁ : step (3 + 16 * u) = 5 + 24 * u := by
    simpa only [show 3 + 16*u = 2*(1+8*u)+1 by omega,
      step_odd] using (show 3*(1+8*u)+2 = 5+24*u by omega)
  have a₂ : step (5 + 24 * u) = 8 + 36 * u := by
    rw [show 5+24*u = 2*(2+12*u)+1 by omega, step_odd]
    omega
  have a₃ : step (8 + 36 * u) = 4 + 18 * u := by
    rw [show 8+36*u = 2*(4+18*u) by omega, step_even]
  have a₄ : step (4 + 18 * u) = 2 + 9 * u := by
    rw [show 4+18*u = 2*(2+9*u) by omega, step_even]
  have b₀ : upper (3 + 16 * u) = 8 + 48 * u := by unfold upper; omega
  have b₁ : step (8 + 48 * u) = 4 + 24 * u := by
    rw [show 8+48*u = 2*(4+24*u) by omega, step_even]
  have b₂ : step (4 + 24 * u) = 2 + 12 * u := by
    rw [show 4+24*u = 2*(2+12*u) by omega, step_even]
  have b₃ : step (2 + 12 * u) = 1 + 6 * u := by
    rw [show 2+12*u = 2*(1+6*u) by omega, step_even]
  have b₄ : step (1 + 6 * u) = 2 + 9 * u := by
    rw [show 1+6*u = 2*(3*u)+1 by omega, step_odd]
    omega
  change step (step (step _)) ≠ step (step (step _)) ∧
    step (step (step (step _))) = step (step (step (step _)))
  rw [b₀, a₁, a₂, a₃, a₄, b₁, b₂, b₃, b₄]
  omega

private theorem persist {α : Type*} (f : α → α) {u v : α} {h k : ℕ}
    (eqh : f^[h] u = f^[h] v) (hle : h ≤ k) : f^[k] u = f^[k] v := by
  obtain ⟨d, rfl⟩ := Nat.exists_eq_add_of_le hle
  simp only [Nat.add_comm h d, Function.iterate_add_apply, eqh]

/-- For any deterministic map, an orbit of pairs can visit at most one
time in a slice that fuses after exactly a fixed positive number of steps. -/
theorem equal_merger_slice_clocks {α : Type*} (f : α → α) (u v : α) (h k t : ℕ)
    (fh : f^[t+1] (f^[h] u) = f^[t+1] (f^[h] v))
    (nh : f^[t] (f^[h] u) ≠ f^[t] (f^[h] v))
    (fk : f^[t+1] (f^[k] u) = f^[t+1] (f^[k] v))
    (nk : f^[t] (f^[k] u) ≠ f^[t] (f^[k] v)) : h = k := by
  rw [← Function.iterate_add_apply, ← Function.iterate_add_apply] at fh nh fk nk
  rcases lt_trichotomy h k with hlt | he | hgt
  · exact False.elim (nk (persist f fh (by omega)))
  · exact he
  · exact False.elim (nh (persist f fk (by omega)))

/-- Arbitrary ordinary common clocks, without restrictions on the grades. -/
theorem targets_unique (y u v h k : ℕ)
    (hh₁ : step^[h] y = 3 + 16*u) (hh₂ : step^[h] (upper y) = upper (3 + 16*u))
    (hk₁ : step^[k] y = 3 + 16*v) (hk₂ : step^[k] (upper y) = upper (3 + 16*v)) :
    h = k ∧ u = v := by
  have hu := exact_four u
  have hv := exact_four v
  have he : h = k := equal_merger_slice_clocks step y (upper y) h k 3
    (by simpa only [hh₁, hh₂] using hu.2) (by simpa only [hh₁, hh₂] using hu.1)
    (by simpa only [hk₁, hk₂] using hv.2) (by simpa only [hk₁, hk₂] using hv.1)
  subst k
  exact ⟨rfl, by omega⟩

#print axioms exact_four
#print axioms equal_merger_slice_clocks
#print axioms targets_unique

end Collatz.OrdinaryAntichain
