import Mathlib.Data.Nat.Factorization.Basic
import Mathlib.Dynamics.PeriodicPts.Lemmas
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Positivity

/-! Disjoint off-cycle entry branches at all periodic phases of the ordinary odd map. -/

namespace Collatz.SixHour.PeriodicSiblings

open Function

def syr (x : ℕ) : ℕ := ordCompl[2] (3 * x + 1)

/-- One of the first two larger siblings is a ternary unit. -/
def sibling (x : ℕ) : ℕ := if x % 3 = 1 then 4 * x + 1 else 16 * x + 5

theorem sibling_properties {x : ℕ} (hx : 0 < x) :
    x < sibling x ∧ sibling x ≤ 21 * x ∧ sibling x % 2 = 1 ∧ sibling x % 3 ≠ 0 := by
  unfold sibling
  split <;> omega

theorem sibling_next (x : ℕ) : syr (sibling x) = syr x := by
  unfold sibling syr
  split
  · rw [show 3 * (4 * x + 1) + 1 = 4 * (3 * x + 1) by ring, Nat.ordCompl_mul]
    have h : ordCompl[2] 4 = 1 := Nat.ordCompl_self_pow (k := 2) Nat.prime_two
    simp [h]
  · rw [show 3 * (16 * x + 5) + 1 = 16 * (3 * x + 1) by ring, Nat.ordCompl_mul]
    have h : ordCompl[2] 16 = 1 := Nat.ordCompl_self_pow (k := 4) Nat.prime_two
    simp [h]

theorem sibling_is_transient {x : ℕ} (h : x ∈ periodicPts syr) :
    sibling x ∉ periodicPts syr := by
  intro hs
  have he := (bijOn_periodicPts syr).injOn hs h (sibling_next x)
  unfold sibling at he
  split at he <;> omega

def reaches {α : Type*} (f : α → α) (u v : α) : Prop := ∃ n : ℕ, f^[n] u = v

theorem entry_branches_unique {α : Type*} {f : α → α} {u a b : α}
    (ha : a ∉ periodicPts f) (hb : b ∉ periodicPts f)
    (hfa : f a ∈ periodicPts f) (hfb : f b ∈ periodicPts f)
    (hua : reaches f u a) (hub : reaches f u b) : a = b := by
  obtain ⟨i, hi⟩ := hua
  obtain ⟨j, hj⟩ := hub
  rcases lt_trichotomy i j with hij | hij | hji
  · obtain ⟨k, hk⟩ := Nat.exists_eq_add_of_lt hij
    have h : f^[k] (f a) = b := by
      rw [← hi, ← Function.iterate_succ_apply' f i,
          ← Function.iterate_add_apply]
      convert hj using 2
      omega
    exact False.elim (hb (h ▸ (bijOn_periodicPts f).mapsTo.iterate k hfa))
  · simpa [hij] using hi.symm.trans (by simpa [hij] using hj)
  · obtain ⟨k, hk⟩ := Nat.exists_eq_add_of_lt hji
    have h : f^[k] (f b) = a := by
      rw [← hj, ← Function.iterate_succ_apply' f j,
          ← Function.iterate_add_apply]
      convert hi using 2
      omega
    exact False.elim (ha (h ▸ (bijOn_periodicPts f).mapsTo.iterate k hfb))

theorem sibling_basins_disjoint {x y u : ℕ}
    (hx : x ∈ periodicPts syr) (hy : y ∈ periodicPts syr)
    (hu : reaches syr u (sibling x)) (hv : reaches syr u (sibling y)) : x = y := by
  have ps (v : ℕ) (hp : v ∈ periodicPts syr) : syr (sibling v) ∈ periodicPts syr := by
    rw [sibling_next]
    exact (bijOn_periodicPts syr).mapsTo hp
  have he := entry_branches_unique (sibling_is_transient hx) (sibling_is_transient hy)
    (ps x hx) (ps y hy) hu hv
  exact (bijOn_periodicPts syr).injOn hx hy
    (by simpa only [sibling_next] using congrArg syr he)

/-- The unit sibling supplies a fixed fraction of the missing mass in one transfer step. -/
theorem sibling_transfer_floor {x z α : ℚ} (hx : 0 < x) (hz : 0 < z)
    (hzx : z ≤ 21 * x) (hα : 0 ≤ α) :
    (α / 7) * (1 - 3 * x / (3 * x + 1)) ≤ 3 * α / (3 * z + 1) := by
  have he : (1 - 3 * x / (3 * x + 1)) = 1 / (3 * x + 1) := by
    field_simp
    ring
  rw [he]
  have hp : 0 < 3 * z + 1 := by positivity
  have hq : 0 < 3 * x + 1 := by positivity
  field_simp
  nlinarith [mul_nonneg hα (sub_nonneg.mpr hzx)]

/-- Successive affine minorants multiply their contraction factors on an actual path. -/
theorem iterated_transfer_floor {u w W : ℕ → ℚ} {c : ℚ}
    (hw : ∀ j, 0 ≤ w j) (hW : W 0 = 1)
    (hWs : ∀ j, W (j + 1) = w j * W j)
    (hs : ∀ j, w j * u j + c * (1 - w j) ≤ u (j + 1)) (k : ℕ) :
    c + (u 0 - c) * W k ≤ u k := by
  induction k with
  | zero => simp [hW]
  | succ k ih =>
    rw [hWs]
    have hm := mul_le_mul_of_nonneg_left ih (hw k)
    linarith only [hs k, hm]

end Collatz.SixHour.PeriodicSiblings
