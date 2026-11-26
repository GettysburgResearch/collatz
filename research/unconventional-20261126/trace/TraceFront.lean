import Mathlib.Topology.Algebra.Ring.Real
import Mathlib.Topology.Order.MonotoneConvergence
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.FieldSimp

open Filter Set
open scoped Topology

namespace Collatz.TraceFront

/-- An unnormalized moving row. At old sites each new contribution is
nonnegative and costs at most the common harmonic-mass increment.
The one new leftmost site may carry a different birth value. -/
structure Rows where
  mass : ℕ → ℝ
  row : ℕ → ℤ → ℝ
  cap : ℝ
  cap_nonneg : 0 ≤ cap
  mass_pos : ∀ i, 0 < mass i
  mass_mono : Monotone mass
  mass_bdd : BddAbove (range mass)
  row_nonneg : ∀ i s, 0 ≤ row i s
  row_bound : ∀ i s, row i s ≤ cap * mass i
  before : ∀ (i : ℕ) (s : ℤ), s < -(i : ℤ) → row i s = 0
  old_lower : ∀ (i : ℕ) (s : ℤ), -(i : ℤ) ≤ s → row i s ≤ row (i+1) s
  old_upper : ∀ (i : ℕ) (s : ℤ), -(i : ℤ) ≤ s →
    row (i+1) s ≤ row i s + cap * (mass (i+1) - mass i)
  birth : Tendsto (fun i : ℕ => row i (-(i : ℤ))) atTop (𝓝 0)

noncomputable def Rows.total (g : Rows) : ℝ := ⨆ i, g.mass i

noncomputable def Rows.profile (g : Rows) (s : ℤ) : ℝ := ⨆ i, g.row i s

theorem Rows.mass_le_total (g : Rows) (i : ℕ) : g.mass i ≤ g.total :=
  le_ciSup g.mass_bdd i

theorem Rows.total_pos (g : Rows) : 0 < g.total :=
  (g.mass_pos 0).trans_le (g.mass_le_total 0)

theorem Rows.tendsto_mass (g : Rows) : Tendsto g.mass atTop (𝓝 g.total) :=
  tendsto_atTop_ciSup g.mass_mono g.mass_bdd

theorem Rows.row_mono (g : Rows) (s : ℤ) : Monotone (fun i => g.row i s) := by
  apply monotone_nat_of_le_succ
  intro i
  by_cases h : -(i : ℤ) ≤ s
  · exact g.old_lower i s h
  · rw [g.before i s (lt_of_not_ge h)]
    exact g.row_nonneg _ _

theorem Rows.row_bdd (g : Rows) (s : ℤ) : BddAbove (range (fun i => g.row i s)) := by
  refine ⟨g.cap * g.total, ?_⟩
  rintro _ ⟨i, rfl⟩
  exact (g.row_bound _ _).trans (mul_le_mul_of_nonneg_left (g.mass_le_total _) g.cap_nonneg)

theorem Rows.old_segment (g : Rows) {m i : ℕ} (mi : m ≤ i) (s : ℤ)
    (hs : -(m : ℤ) ≤ s) :
    g.row i s ≤ g.row m s + g.cap * (g.mass i - g.mass m) := by
  induction i, mi using Nat.le_induction with
  | base => simp
  | succ i mi ih =>
    have hsi : -(i : ℤ) ≤ s := by omega
    have step := g.old_upper i s hsi
    linarith

/-- The entire integer-indexed row, including sheets born after the
anchor time, converges uniformly. All inputs are explicit hypotheses. -/
theorem Rows.profile_uniform (g : Rows) {ε : ℝ} (he : 0 < ε) :
    ∃ m : ℕ, ∀ i ≥ m, ∀ s : ℤ, |g.profile s - g.row i s| < ε := by
  have hm : Tendsto (fun i => g.cap * (g.total - g.mass i)) atTop (𝓝 0) := by
    simpa using (tendsto_const_nhds (x := g.cap)).mul ((tendsto_const_nhds (x := g.total)).sub g.tendsto_mass)
  have he3 : 0 < ε/3 := by linarith
  obtain ⟨m₁, hm₁⟩ := eventually_atTop.1 (hm.eventually_lt_const he3)
  obtain ⟨m₂, hm₂⟩ := eventually_atTop.1 (g.birth.eventually_lt_const he3)
  refine ⟨max m₁ m₂, ?_⟩
  intro i hi s
  have hle : g.row i s ≤ g.profile s := le_ciSup (g.row_bdd s) i
  rw [abs_of_nonneg (sub_nonneg.mpr hle)]
  have upper : g.profile s ≤ g.row i s + 2*ε/3 := by
    apply ciSup_le
    intro j
    by_cases hji : j ≤ i
    · have hrow := g.row_mono s hji
      linarith
    have hij : i ≤ j := by omega
    have hsmall := hm₁ i (by omega)
    by_cases hs : -(i : ℤ) ≤ s
    · have seg := g.old_segment hij s hs
      have hcap := mul_le_mul_of_nonneg_left (g.mass_le_total j) g.cap_nonneg
      linarith
    by_cases hsj : s < -(j : ℤ)
    · rw [g.before j s hsj]
      linarith [g.row_nonneg i s]
    let r := (-s).toNat
    have hr : (r : ℤ) = -s := by
      dsimp [r]
      omega
    have hir : i ≤ r := by omega
    have hrj : r ≤ j := by omega
    have hsite : -(r : ℤ) = s := by omega
    have seg := g.old_segment hrj s hsite.le
    have born := hm₂ r (by omega)
    change g.row r (-(r : ℤ)) < ε/3 at born
    rw [hsite] at born
    have hmass := g.mass_mono hir
    have hcap := mul_le_mul_of_nonneg_left (g.mass_le_total j) g.cap_nonneg
    have hcap' := mul_le_mul_of_nonneg_left hmass g.cap_nonneg
    linarith [g.row_nonneg i s]
  linarith


/-- The limiting row vanishes uniformly at its far left. -/
theorem Rows.profile_left (g : Rows) {ε : ℝ} (he : 0 < ε) :
    ∃ m : ℕ, ∀ s : ℤ, s < -(m : ℤ) → |g.profile s| < ε := by
  obtain ⟨m, hm⟩ := g.profile_uniform he
  refine ⟨m, fun s hs => ?_⟩
  simpa only [g.before m s hs, sub_zero] using hm m le_rfl s

/-- Division by the changing canonical mass preserves convergence,
uniformly over every depth relative to the orbit clock. -/
theorem Rows.normalized_uniform (g : Rows) {ε : ℝ} (he : 0 < ε) :
    ∃ m : ℕ, ∀ i ≥ m, ∀ s : ℤ,
      |g.profile s / g.total - g.row i s / g.mass i| < ε := by
  have ht := g.total_pos
  have hε : 0 < ε*g.total/2 := by positivity
  obtain ⟨m₁, hm₁⟩ := g.profile_uniform hε
  have hlim : Tendsto (fun i => g.cap * (g.total - g.mass i)) atTop (𝓝 0) := by
    simpa using (tendsto_const_nhds (x := g.cap)).mul
      ((tendsto_const_nhds (x := g.total)).sub g.tendsto_mass)
  obtain ⟨m₂, hm₂⟩ := eventually_atTop.1 (hlim.eventually_lt_const hε)
  refine ⟨max m₁ m₂, ?_⟩
  intro i hi s
  have h₁ := hm₁ i (by omega) s
  have h₂ := hm₂ i (by omega)
  have hm := g.mass_pos i
  have hn : 0 ≤ g.row i s / g.mass i := div_nonneg (g.row_nonneg _ _) hm.le
  have hc : g.row i s / g.mass i ≤ g.cap := (div_le_iff₀ hm).2 (g.row_bound _ _)
  have hinc : 0 ≤ g.total - g.mass i := sub_nonneg.2 (g.mass_le_total i)
  have bound := mul_le_mul_of_nonneg_right hc hinc
  have split : g.profile s / g.total - g.row i s / g.mass i =
      ((g.profile s - g.row i s) -
        (g.row i s / g.mass i) * (g.total - g.mass i)) / g.total := by
    field_simp
    ring
  rw [split, abs_div, abs_of_pos ht, div_lt_iff₀ ht]
  apply lt_of_le_of_lt (abs_sub _ _)
  rw [abs_of_nonneg (mul_nonneg hn hinc)]
  linarith

end Collatz.TraceFront


#print axioms Collatz.TraceFront.Rows.mass_le_total

#print axioms Collatz.TraceFront.Rows.total_pos

#print axioms Collatz.TraceFront.Rows.tendsto_mass

#print axioms Collatz.TraceFront.Rows.row_mono

#print axioms Collatz.TraceFront.Rows.row_bdd

#print axioms Collatz.TraceFront.Rows.old_segment

#print axioms Collatz.TraceFront.Rows.profile_uniform

#print axioms Collatz.TraceFront.Rows.profile_left

#print axioms Collatz.TraceFront.Rows.normalized_uniform
