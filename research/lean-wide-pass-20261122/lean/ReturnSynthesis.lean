import MarkFrequency
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Bounds

/-! A finite, source-uniform bound for actual marked returns.

The reciprocal, Fourier, and Fejér estimates are imported from PR178 at
75f2f9aad4d3f80aaa1f8718e229faa04ee5770e.  Unlike the earlier eventual
frequency theorem, the exceptional states here are counted within the
given finite prefix.  No source-dependent eventual horizon is used.

The finite source sum retains each original weight, including collisions.
No theorem below asserts disappearance of the surviving source mass.
-/

namespace CollatzShell.ForwardSection.ReturnSynthesis

open Finset ReturnFourier MarkPhase MarkFrequency

private theorem circle_chord_lower (u : ℝ) (hu : |u| ≤ 1 / 2) :
    4 * |u| ≤ ‖1 - character 1 u‖ := by
  have hp : |Real.pi * u| ≤ Real.pi / 2 := by
    rw [abs_mul, abs_of_pos Real.pi_pos]
    nlinarith [Real.pi_pos]
  have h := Real.mul_abs_le_abs_sin hp
  rw [abs_mul, abs_of_pos Real.pi_pos] at h
  have cancel : 2 / Real.pi * (Real.pi * |u|) = 2 * |u| := by
    field_simp
  rw [cancel] at h
  rw [norm_sub_rev]
  unfold character
  norm_num only [Nat.cast_one, mul_one]
  rw [show ((2 * Real.pi * u : ℝ) : ℂ) * Complex.I =
      Complex.I * ((2 * Real.pi * u : ℝ) : ℂ) by ring]
  rw [Complex.norm_exp_I_mul_ofReal_sub_one]
  rw [show (2 * Real.pi * u) / 2 = Real.pi * u by ring]
  norm_num only [Real.norm_eq_abs, abs_mul, abs_of_pos (by norm_num : (0 : ℝ) < 2)]
  linarith

/-- Elementary exponential separation of the actual rotation frequencies.
It uses only integer power separation, not a Diophantine approximation axiom. -/
theorem explicit_frequency_separation (k K : Nat) (hk : 0 < k) (hK : k ≤ K) :
    1 / (((4^K : Nat) : ℝ) + 1) ≤ ‖1 - character k alpha‖ := by
  let a : Nat := ⌊(k : ℝ) * alpha + 1 / 2⌋₊
  have positive : 0 ≤ (k : ℝ) * alpha + 1 / 2 := by
    have al : 0 < alpha := lt_trans (by norm_num) rotation_bounds.1
    positivity
  have alow : (a : ℝ) ≤ (k : ℝ) * alpha + 1 / 2 := Nat.floor_le positive
  have ahigh : (k : ℝ) * alpha + 1 / 2 < (a : ℝ) + 1 := Nat.lt_floor_add_one _
  have near : |(k : ℝ) * alpha - a| ≤ 1 / 2 := by
    apply abs_le.mpr
    constructor <;> linarith
  have separate : 1 / (((4^k : Nat) : ℝ) + 1) < |(k : ℝ) * alpha - a| := by
    by_contra h
    have impossible := grid_barrier (N := 4^k) (by positivity) hk (le_of_not_gt h)
    omega
  have id : character 1 ((k : ℝ) * alpha - a) = character k alpha := by
    rw [character_sub_nat]
    unfold character
    congr 1
    push_cast
    ring
  have chord := circle_chord_lower _ near
  rw [id] at chord
  have pw : (4^k : Nat) ≤ 4^K := Nat.pow_le_pow_right (by decide) hK
  have denom : (((4^k : Nat) : ℝ) + 1) ≤ ((4^K : Nat) : ℝ) + 1 := by
    exact_mod_cast Nat.add_le_add_right pw 1
  have hrec := one_div_le_one_div_of_le
    (by positivity : (0 : ℝ) < ((4^k : Nat) : ℝ) + 1) denom
  exact hrec.trans (separate.le.trans (by nlinarith [abs_nonneg ((k : ℝ) * alpha - a)]))

/-- A marked state above an explicit height has the required Fejér mass. -/
theorem marked_kernel_of_height (K D x : Nat) (hm : Marked x)
    (hd : D ≤ x.log2)
    (guard : 1120 * Real.pi * (K : ℝ) ≤ (D : ℝ) + 1) :
    (K : ℝ)^2 ≤ 4 * kernel K (height x) := by
  obtain ⟨pl, pu⟩ := marked_phase_small hm
  have dr : (D : ℝ) ≤ (x.log2 : ℝ) := by exact_mod_cast hd
  have den : 0 < (x.log2 : ℝ) + 1 := by positivity
  have coeff : 0 ≤ 4 * Real.pi * (K : ℝ) := by positivity
  have width : 4 * Real.pi * (K : ℝ) *
      (height x - (x.log2 : ℝ)) ≤ 1 / 2 := by
    have h := mul_le_mul_of_nonneg_left pu coeff
    have factor : 4 * Real.pi * (K : ℝ) *
        (140 / ((x.log2 : ℝ) + 1)) ≤ 1 / 2 := by
      apply (le_div_iff₀ (by norm_num : (0 : ℝ) < 2)).mpr
      have g : 1120 * Real.pi * (K : ℝ) ≤ (x.log2 : ℝ) + 1 := by linarith
      have g' := (div_le_one den).mpr g
      calc _ = (1120 * Real.pi * (K : ℝ)) / ((x.log2 : ℝ) + 1) := by ring
           _ ≤ 1 := g'
    exact h.trans factor
  rw [← kernel_sub_nat K (height x) x.log2]
  apply kernel_large
  intro r hr
  have rr : (r : ℝ) ≤ K := by exact_mod_cast hr.le
  calc
    ‖character r (height x - (x.log2 : ℝ)) - 1‖ ≤
        4 * Real.pi * r * |height x - (x.log2 : ℝ)| := character_change _ _
    _ = 4 * Real.pi * r * (height x - (x.log2 : ℝ)) := by rw [abs_of_nonneg pl]
    _ ≤ 4 * Real.pi * K * (height x - (x.log2 : ℝ)) :=
      mul_le_mul_of_nonneg_right
        (mul_le_mul_of_nonneg_left rr (by positivity)) pl
    _ ≤ 1 / 2 := width

/-- Count low states by finite injectivity, without an eventual escape clock. -/
theorem marked_kernel_finite_cutoff (n N K D : Nat)
    (hi : Set.InjOn (oddOrbit n) (↑(range N) : Set Nat))
    (guard : 1120 * Real.pi * (K : ℝ) ≤ (D : ℝ) + 1) :
    (K : ℝ)^2 * (markedVisits n N : ℝ) ≤
      (K : ℝ)^2 * (2^D : Nat) +
        4 * (∑ j ∈ range N, kernel K (height (oddOrbit n j))) := by
  let m := (range N).filter (fun j => Marked (oddOrbit n j))
  let lo := m.filter (fun j => oddOrbit n j < 2^D)
  let hiSet := m.filter (fun j => ¬oddOrbit n j < 2^D)
  have subset : lo ⊆ range N := by
    intro j hj
    exact (mem_filter.mp (mem_filter.mp hj).1).1
  have loinj : Set.InjOn (oddOrbit n) (↑lo : Set Nat) := by
    intro i hi' j hj' eq
    exact hi (subset hi') (subset hj') eq
  have locard : lo.card ≤ 2^D := by
    have sub : lo.image (oddOrbit n) ⊆ range (2^D) := by
      intro x hx
      obtain ⟨j, hj, rfl⟩ := mem_image.mp hx
      exact mem_range.mpr (mem_filter.mp hj).2
    have h := card_le_card sub
    rw [card_image_of_injOn loinj, card_range] at h
    exact h
  have subhi : hiSet ⊆ range N := by
    intro j hj
    exact (mem_filter.mp (mem_filter.mp hj).1).1
  have high : (K : ℝ)^2 * (hiSet.card : ℝ) ≤
      4 * (∑ j ∈ range N, kernel K (height (oddOrbit n j))) := by
    calc
      _ = ∑ j ∈ hiSet, (K : ℝ)^2 := by simp [mul_comm]
      _ ≤ ∑ j ∈ hiSet, 4 * kernel K (height (oddOrbit n j)) := by
        apply sum_le_sum
        intro j hj
        obtain ⟨jm, jl⟩ := mem_filter.mp hj
        have hm := (mem_filter.mp jm).2
        have xp : 0 < oddOrbit n j := by have := hm.1; omega
        have hd : D ≤ (oddOrbit n j).log2 :=
          (Nat.le_log2 xp.ne').mpr (by omega)
        exact marked_kernel_of_height K D _ hm hd guard
      _ = 4 * (∑ j ∈ hiSet, kernel K (height (oddOrbit n j))) := by rw [mul_sum]
      _ ≤ _ := mul_le_mul_of_nonneg_left
        (sum_le_sum_of_subset_of_nonneg subhi
          (by intro j _ _; exact kernel_nonneg _ _)) (by norm_num)
  have split : (m.card : ℝ) = (lo.card : ℝ) + (hiSet.card : ℝ) := by
    exact_mod_cast
      (card_filter_add_card_filter_not (s := m) (fun j => oddOrbit n j < 2^D)).symm
  change (K : ℝ)^2 * (m.card : ℝ) ≤ _
  rw [split, mul_add]
  exact add_le_add
    (mul_le_mul_of_nonneg_left (by exact_mod_cast locard) (sq_nonneg _)) high

/-- An absolute bound on each relevant Fourier coefficient bounds the kernel. -/
theorem kernel_sum_absolute (n K N : Nat) (A : ℝ) (hA : 0 ≤ A)
    (freq : ∀ k, 0 < k → k < K →
      ‖∑ j ∈ range N, character k (height (oddOrbit n j))‖ ≤ A) :
    (∑ j ∈ range N, kernel K (height (oddOrbit n j))) ≤
      (K : ℝ) * N + (K : ℝ)^2 * A := by
  by_cases hz : N = 0
  · subst N
    simpa using mul_nonneg (sq_nonneg (K : ℝ)) hA
  have np : (0 : ℝ) < N := by exact_mod_cast (show 0 < N by omega)
  have h := kernel_sum_bound n K N (A / N) (div_nonneg hA np.le)
    (by intro k hk hK; simpa [np.ne'] using freq k hk hK)
  simpa [div_eq_mul_inv, np.ne', mul_assoc] using h

/-- Explicit finite return estimate, retaining the frequency separation.

The cutoffs `D`, `B`, and `K` are free.  `γ` is a lower bound on the
finitely many nonzero rotation frequencies; it is independent of the source.
-/
theorem marked_visits_finite_bound (n N K D B : Nat) (hn : 0 < n)
    (hi : Set.InjOn (oddOrbit n) (↑(range N) : Set Nat))
    (guard : 1120 * Real.pi * (K : ℝ) ≤ (D : ℝ) + 1)
    (γ : ℝ) (hγ : 0 < γ)
    (sep : ∀ k, 0 < k → k < K → γ ≤ ‖1 - character k alpha‖) :
    (K : ℝ)^2 * (markedVisits n N : ℝ) ≤
      (K : ℝ)^2 * (2^D : Nat) + 4 * (K : ℝ) * N +
        4 * (K : ℝ)^2 *
          ((2 + 4 * Real.pi * K * ((B : ℝ) + (N : ℝ) / (B + 1))) / γ) := by
  let A : ℝ :=
    (2 + 4 * Real.pi * K * ((B : ℝ) + (N : ℝ) / (B + 1))) / γ
  have apos : 0 ≤ A := by dsimp [A]; positivity
  have freq : ∀ k, 0 < k → k < K →
      ‖∑ j ∈ range N, character k (height (oddOrbit n j))‖ ≤ A := by
    intro k hk hK
    have h := injective_prefix_fourier n k N B hn hi
    have kr : (k : ℝ) ≤ K := by exact_mod_cast hK.le
    have budget : 0 ≤ (B : ℝ) + (N : ℝ) / (B + 1) := by positivity
    have lower := mul_le_mul_of_nonneg_right (sep k hk hK)
      (norm_nonneg (∑ j ∈ range N, character k (height (oddOrbit n j))))
    have upper :
        2 + 4 * Real.pi * k * ((B : ℝ) + (N : ℝ) / (B + 1)) ≤
        2 + 4 * Real.pi * K * ((B : ℝ) + (N : ℝ) / (B + 1)) := by
      exact add_le_add le_rfl
        (mul_le_mul_of_nonneg_right
          (mul_le_mul_of_nonneg_left kr (by positivity)) budget)
    apply (le_div_iff₀ hγ).mpr
    simpa [mul_comm] using lower.trans (h.trans upper)
  have count := marked_kernel_finite_cutoff n N K D hi guard
  have kernelBound := kernel_sum_absolute n K N A apos freq
  have combined := count.trans
    (add_le_add le_rfl (mul_le_mul_of_nonneg_left kernelBound (by norm_num)))
  dsimp [A] at combined
  nlinarith only [combined]

/-- The finite source-uniform estimate with every frequency premise discharged. -/
theorem marked_visits_explicit_bound (n N K D B : Nat) (hn : 0 < n)
    (hi : Set.InjOn (oddOrbit n) (↑(range N) : Set Nat))
    (guard : 1120 * Real.pi * (K : ℝ) ≤ (D : ℝ) + 1) :
    (K : ℝ)^2 * (markedVisits n N : ℝ) ≤
      (K : ℝ)^2 * (2^D : Nat) + 4 * (K : ℝ) * N +
        4 * (K : ℝ)^2 *
          (((4^K : Nat) : ℝ) + 1) *
          (2 + 4 * Real.pi * K * ((B : ℝ) + (N : ℝ) / (B + 1))) := by
  have h := marked_visits_finite_bound n N K D B hn hi guard
    (1 / (((4^K : Nat) : ℝ) + 1)) (by positivity)
    (by intro k hk hK; exact explicit_frequency_separation k K hk hK.le)
  have den : (((4^K : Nat) : ℝ) + 1) ≠ 0 := by positivity
  simp only [div_div_eq_mul_div, div_one] at h
  nlinarith only [h]

/-- Original source weights at one odd clock.  Equal endpoints are counted
with all their weights, exactly as under the actual pushforward measure. -/
noncomputable def markedSourceMass (S : Finset Nat) (w : Nat → ℝ) (j : Nat) : ℝ :=
  ∑ n ∈ S, if Marked (oddOrbit n j) then w n else 0

theorem marked_source_occupation_identity (S : Finset Nat) (w : Nat → ℝ) (N : Nat) :
    (∑ j ∈ range N, markedSourceMass S w j) =
      ∑ n ∈ S, w n * (markedVisits n N : ℝ) := by
  unfold markedSourceMass markedVisits
  rw [sum_comm]
  apply sum_congr rfl
  intro n _
  rw [← sum_filter]
  simp [mul_comm]

/-- A common finite visit estimate passes to arbitrary original source
weights.  There is no fresh-source replacement and no loss at collisions. -/
theorem weighted_marked_occupation_bound (S : Finset Nat) (w : Nat → ℝ)
    (N : Nat) (A C : ℝ)
    (hw : ∀ n ∈ S, 0 ≤ w n)
    (bound : ∀ n ∈ S, A * (markedVisits n N : ℝ) ≤ C) :
    A * (∑ j ∈ range N, markedSourceMass S w j) ≤
      C * (∑ n ∈ S, w n) := by
  rw [marked_source_occupation_identity, mul_sum, mul_sum]
  apply sum_le_sum
  intro n hn
  have h := mul_le_mul_of_nonneg_left (bound n hn) (hw n hn)
  nlinarith only [h]

#print axioms marked_kernel_of_height
#print axioms explicit_frequency_separation
#print axioms marked_kernel_finite_cutoff
#print axioms kernel_sum_absolute
#print axioms marked_visits_finite_bound
#print axioms marked_visits_explicit_bound
#print axioms marked_source_occupation_identity
#print axioms weighted_marked_occupation_bound

end CollatzShell.ForwardSection.ReturnSynthesis
