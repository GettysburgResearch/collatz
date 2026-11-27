import Mathlib.Data.Int.ModEq
import Mathlib.Data.Int.Basic
import Mathlib.Data.Nat.GCD.Basic
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-! Finite deterministic frequency escape in the two-site orientation walk. -/
namespace CollatzResearch.PairFrequency

/-- Small representatives eliminate the modular carry. -/
theorem small_step {g r : ℕ} {x y : ℤ} (hr : r ≤ 2)
    (hx : 20 * x.natAbs < g) (hy : 20 * y.natAbs < g)
    (h : (3 : ℤ) ^ r * y ≡ 4 * x [ZMOD (g : ℤ)]) :
    (3 : ℤ) ^ r * y = 4 * x := by
  have hd : (g : ℤ) ∣ 4*x - 3^r*y := Int.modEq_iff_dvd.mp h
  have hsum := Int.natAbs_sub_le (4*x) ((3:ℤ)^r*y)
  have habs : (4*x - 3^r*y).natAbs < (g : ℤ).natAbs := by
    obtain h0 | h1 | h2 : r = 0 ∨ r = 1 ∨ r = 2 := by omega
    all_goals subst r
    all_goals norm_num [Int.natAbs_mul] at hsum ⊢
    all_goals omega
  have hz := Int.eq_zero_of_dvd_of_natAbs_lt_natAbs hd habs
  omega

private theorem telescope (r : ℕ → ℕ) (z : ℕ → ℤ) (L : ℕ)
    (h : ∀ j < L, (3 : ℤ) ^ r j * z (j+1) = 4 * z j) :
    ∃ R : ℕ, (3 : ℤ)^R * z L = 4^L * z 0 := by
  induction L with
  | zero => exact ⟨0, by simp⟩
  | succ L ih =>
    obtain ⟨R, hR⟩ := ih (fun j hj => h j (by omega))
    refine ⟨R + r L, ?_⟩
    calc
      (3:ℤ)^(R + r L) * z (L+1) = 3^R * (3^(r L) * z (L+1)) := by ring
      _ = 3^R * (4 * z L) := by rw [h L (by omega)]
      _ = 4 * (3^R * z L) := by ring
      _ = 4^(L+1) * z 0 := by rw [hR, pow_succ]; ring

/-- Any such carry-free run forces the last integer frequency to absorb 4^L. -/
theorem terminal_dvd (r : ℕ → ℕ) (z : ℕ → ℤ) (L : ℕ)
    (h : ∀ j < L, (3 : ℤ) ^ r j * z (j+1) = 4 * z j) :
    4^L ∣ (z L).natAbs := by
  obtain ⟨R, he⟩ := telescope r z L h
  have hn := congrArg Int.natAbs he
  have eqn : 3^R * (z L).natAbs = 4^L * (z 0).natAbs := by
    simpa [Int.natAbs_mul] using hn
  have hc : (4^L).Coprime (3^R) :=
    ((by decide : Nat.Coprime 4 3).pow_left L).pow_right R
  exact hc.dvd_of_dvd_mul_left ⟨_, eqn⟩

/-- The segment has L+1 positions and L transition edges. -/
theorem large_phase {g L : ℕ} (r : ℕ → ℕ) (z : ℕ → ℤ)
    (hsize : g ≤ 4^L) (hz : z L ≠ 0)
    (hr : ∀ j < L, r j ≤ 2)
    (hstep : ∀ j < L, (3:ℤ) ^ r j * z (j+1) ≡ 4 * z j [ZMOD (g:ℤ)]) :
    ∃ j ≤ L, g ≤ 20 * (z j).natAbs := by
  by_contra! hall
  have hd := terminal_dvd r z L (fun j hj =>
    small_step (hr j hj) (hall j (by omega)) (hall (j+1) (by omega)) (hstep j hj))
  have hpos : 0 < (z L).natAbs := Int.natAbs_pos.mpr hz
  have hle := Nat.le_of_dvd hpos hd
  have hfinal := hall L le_rfl
  omega

#print axioms small_step
#print axioms terminal_dvd
#print axioms large_phase

end CollatzResearch.PairFrequency
