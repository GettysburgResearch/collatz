import MarkFrequency
import Mathlib.NumberTheory.Harmonic.Bounds
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Bounds
import Mathlib.Data.Finset.Max

/-!
Uniform finite estimates for distinct ordinary Collatz states.

The input is injectivity only on the `N` observed states, not on the whole
infinite orbit.  The endpoint state at time `N` is allowed to repeat.  The
harmonic budget and elementary character separation turn the qualitative
PR178 occupation argument into an explicit finite inequality.  No random
start, predecessor-density, or ordinary escape-rate hypothesis is used.
For odd sources these are ordinary accelerated Collatz prefixes.  The
algebraic lemmas also allow positive even sources for the extended map;
ordinary even-source applications first remove the initial powers of two.
-/

namespace CollatzShell.ForwardSection.AnalyticCoupling

open Finset ReturnFourier MarkPhase MarkFrequency

/-- Among `N` distinct positive integers, the reciprocal sum is at most `H_N`. -/
theorem reciprocal_set_harmonic (s : Finset Nat)
    (hp : ∀ x ∈ s, 0 < x) :
    (∑ x ∈ s, 1 / (x : ℝ)) ≤ (harmonic s.card : ℝ) := by
  revert hp
  induction s using Finset.induction_on_max with
  | empty => simp
  | insert a s hmax ih =>
    intro hp
    have ha : a ∉ s := by
      intro h
      exact (lt_irrefl a) (hmax a h)
    have hs : ∀ x ∈ s, 0 < x := by
      intro x hx
      exact hp x (mem_insert_of_mem hx)
    have sub : insert a s ⊆ Icc 1 a := by
      intro x hx
      refine mem_Icc.mpr ⟨hp x hx, ?_⟩
      rcases mem_insert.mp hx with rfl | hx
      · exact le_rfl
      · exact (hmax x hx).le
    have card : s.card + 1 ≤ a := by
      simpa [card_insert_of_notMem ha] using card_le_card sub
    have denom : (s.card : ℝ) + 1 ≤ a := by exact_mod_cast card
    have term : 1 / (a : ℝ) ≤ 1 / ((s.card : ℝ) + 1) :=
      one_div_le_one_div_of_le (by positivity) denom
    calc
      _ = (∑ x ∈ s, 1 / (x : ℝ)) + 1 / (a : ℝ) := by
        rw [sum_insert ha]
        ring
      _ ≤ (harmonic s.card : ℝ) + 1 / ((s.card : ℝ) + 1) :=
        add_le_add (ih hs) term
      _ = _ := by simp [card_insert_of_notMem ha, harmonic_succ, one_div]

private theorem odd_positive {n : Nat} (hn : 0 < n) (j : Nat) :
    0 < oddOrbit n j := by
  cases j with
  | zero => exact hn
  | succ j => exact Nat.ordCompl_pos 2 (by omega)

/-- Exact finite harmonic budget for one actual, nonrepeating odd prefix. -/
theorem odd_prefix_reciprocal_harmonic (n N : Nat) (hn : 0 < n)
    (hi : Set.InjOn (oddOrbit n) (↑(range N) : Set Nat)) :
    (∑ j ∈ range N, 1 / (oddOrbit n j : ℝ)) ≤ (harmonic N : ℝ) := by
  let s := (range N).image (oddOrbit n)
  have card : s.card = N := by simpa [s] using card_image_of_injOn hi
  have positive : ∀ x ∈ s, 0 < x := by
    intro x hx
    obtain ⟨j, _, rfl⟩ := mem_image.mp hx
    exact odd_positive hn j
  have h := reciprocal_set_harmonic s positive
  rw [card] at h
  simpa [s, sum_image hi] using h

/-- The reciprocal error is logarithmic, with a uniform constant and horizon. -/
theorem odd_prefix_reciprocal_log (n N : Nat) (hn : 0 < n)
    (hi : Set.InjOn (oddOrbit n) (↑(range N) : Set Nat)) :
    (∑ j ∈ range N, 1 / (oddOrbit n j : ℝ)) ≤ 1 + Real.log N :=
  (odd_prefix_reciprocal_harmonic n N hn hi).trans (harmonic_le_one_add_log N)

/-- The same finite harmonic budget controls the full height/valuation
identity before the integer cocycle is removed by characters. -/
theorem odd_prefix_log_cocycle_harmonic (n N : Nat) (hn : 0 < n)
    (hi : Set.InjOn (oddOrbit n) (↑(range N) : Set Nat)) :
    ∃ E : ℝ, 0 ≤ E ∧ E ≤ (harmonic N : ℝ) ∧
      height (oddOrbit n N) = height n + (N : ℝ) * alpha -
        (∑ j ∈ range N, (twos (3 * oddOrbit n j + 1) : ℝ)) + E := by
  obtain ⟨E, hE, budget, equation⟩ := actual_log_cocycle n N hn
  exact ⟨E, hE, budget.trans (odd_prefix_reciprocal_harmonic n N hn hi), equation⟩

/-- A distinct prefix ending at or above its source cannot accumulate more
than `N*log₂3 + H_N` halvings.  This keeps the actual integer cocycle. -/
theorem odd_prefix_valuation_bound (n N : Nat) (hn : 0 < n)
    (hi : Set.InjOn (oddOrbit n) (↑(range N) : Set Nat))
    (hend : n ≤ oddOrbit n N) :
    (∑ j ∈ range N, (twos (3 * oddOrbit n j + 1) : ℝ)) ≤
      (N : ℝ) * alpha + (harmonic N : ℝ) := by
  obtain ⟨E, _, budget, equation⟩ := odd_prefix_log_cocycle_harmonic n N hn hi
  have heights : height n ≤ height (oddOrbit n N) :=
    Real.logb_le_logb_of_le (by norm_num) (by exact_mod_cast hn) (by exact_mod_cast hend)
  linarith

/-- Finite Fourier control with the exact extremal reciprocal budget. -/
theorem odd_prefix_fourier_harmonic (n k N : Nat) (hn : 0 < n)
    (hi : Set.InjOn (oddOrbit n) (↑(range N) : Set Nat)) :
    ‖1 - character k alpha‖ *
        ‖∑ j ∈ range N, character k (height (oddOrbit n j))‖ ≤
      2 + 4 * Real.pi * k * (harmonic N : ℝ) := by
  exact (odd_prefix_fourier n k N hn).trans (add_le_add le_rfl
    (mul_le_mul_of_nonneg_left (odd_prefix_reciprocal_harmonic n N hn hi)
      (by positivity)))

/-- A quantitative separation from resonance, using only integer powers of
two and three.  The deliberately conservative constant simplifies later bounds. -/
theorem character_gap_budget (k : Nat) (hk : 0 < k) :
    1 ≤ ((4 : ℝ)^k + 1) * ‖1 - character k alpha‖ := by
  let a : Nat := ⌊(k : ℝ) * alpha + 1 / 2⌋₊
  let d : ℝ := (k : ℝ) * alpha - a
  have kp : (0 : ℝ) < k := by exact_mod_cast hk
  have alpha_pos : 0 < alpha := lt_trans (by norm_num) rotation_bounds.1
  have ap : 0 ≤ (k : ℝ) * alpha + 1 / 2 := by
    positivity
  have roundlo := Nat.floor_le ap
  have roundhi := Nat.lt_floor_add_one ((k : ℝ) * alpha + 1 / 2)
  have half : |d| ≤ 1 / 2 := by
    dsimp [d, a]
    exact abs_le.mpr ⟨by linarith, by linarith⟩
  have separated : 1 / (((4^k : Nat) : ℝ) + 1) < |d| := by
    by_contra h
    have near : |(k : ℝ) * alpha - (a : ℝ)| ≤
        1 / (((4^k : Nat) : ℝ) + 1) := le_of_not_gt h
    have impossible := grid_barrier (N := 4^k) (by positivity) hk near
    omega
  have phase : character 1 d = character k alpha := by
    dsimp [d]
    rw [character_sub_nat]
    unfold character
    congr 2
    push_cast
    ring
  have trig : ‖1 - character k alpha‖ = 2 * |Real.sin (Real.pi * d)| := by
    rw [← phase, norm_sub_rev]
    unfold character
    rw [show (((2 * Real.pi * (1 : Nat) * d : ℝ) : ℂ) * Complex.I) =
        Complex.I * ((2 * Real.pi * d : ℝ) : ℂ) by push_cast; ring]
    rw [Complex.norm_exp_I_mul_ofReal_sub_one]
    simp only [show 2 * Real.pi * d / 2 = Real.pi * d by ring,
      Real.norm_eq_abs, abs_mul]
    norm_num
  have argbound : |Real.pi * d| ≤ Real.pi / 2 := by
    rw [abs_mul, abs_of_pos Real.pi_pos]
    nlinarith [mul_le_mul_of_nonneg_left half Real.pi_pos.le]
  have chord := Real.mul_abs_le_abs_sin argbound
  have algeb : 2 / Real.pi * |Real.pi * d| = 2 * |d| := by
    rw [abs_mul, abs_of_pos Real.pi_pos]
    field_simp [Real.pi_ne_zero]
  rw [algeb] at chord
  have lower : 4 * |d| ≤ ‖1 - character k alpha‖ := by rw [trig]; linarith
  have qpos : (0 : ℝ) < (4 : ℝ)^k + 1 := by positivity
  have sep : 1 < ((4 : ℝ)^k + 1) * |d| := by
    have h := (div_lt_iff₀ (by positivity :
      (0 : ℝ) < ((4^k : Nat) : ℝ) + 1)).mp separated
    push_cast at h
    nlinarith only [h]
  have mul := mul_le_mul_of_nonneg_left lower qpos.le
  nlinarith only [sep, mul]

/-- A common explicit bound for all positive frequencies at most `K`. -/
noncomputable def fourierBudget (K N : Nat) : ℝ :=
  ((4 : ℝ)^K + 1) * (2 + 4 * Real.pi * K * (harmonic N : ℝ))

theorem fourierBudget_nonneg (K N : Nat) : 0 ≤ fourierBudget K N := by
  have h : (0 : ℝ) ≤ (harmonic N : ℝ) := by simp only [harmonic]; positivity
  dsimp [fourierBudget]
  positivity

/-- Explicit finite Fourier bound.  The source and observation horizon are
uniform; only distinctness of the observed states is needed. -/
theorem odd_prefix_fourier_explicit (n k N K : Nat) (hn : 0 < n)
    (hi : Set.InjOn (oddOrbit n) (↑(range N) : Set Nat))
    (hk : 0 < k) (hK : k ≤ K) :
    ‖∑ j ∈ range N, character k (height (oddOrbit n j))‖ ≤ fourierBudget K N := by
  let F := ‖∑ j ∈ range N, character k (height (oddOrbit n j))‖
  have fn : 0 ≤ F := norm_nonneg _
  have harmonic_nonneg : (0 : ℝ) ≤ (harmonic N : ℝ) := by
    simp only [harmonic]
    positivity
  have gap := mul_le_mul_of_nonneg_right (character_gap_budget k hk) fn
  have base := mul_le_mul_of_nonneg_left (odd_prefix_fourier_harmonic n k N hn hi)
    (show 0 ≤ (4 : ℝ)^k + 1 by positivity)
  have kk : (k : ℝ) ≤ K := by exact_mod_cast hK
  have power : (4 : ℝ)^k ≤ (4 : ℝ)^K := pow_le_pow_right₀ (by norm_num) hK
  calc
    F ≤ ((4 : ℝ)^k + 1) * (2 + 4 * Real.pi * k * (harmonic N : ℝ)) := by
      nlinarith only [gap, base]
    _ ≤ fourierBudget K N := by
      dsimp [fourierBudget]
      gcongr

/-- The explicit bound has logarithmic horizon dependence for fixed frequency. -/
theorem odd_prefix_fourier_log (n k N : Nat) (hn : 0 < n)
    (hi : Set.InjOn (oddOrbit n) (↑(range N) : Set Nat)) (hk : 0 < k) :
    ‖∑ j ∈ range N, character k (height (oddOrbit n j))‖ ≤
      ((4 : ℝ)^k + 1) * (2 + 4 * Real.pi * k * (1 + Real.log N)) := by
  apply (odd_prefix_fourier_explicit n k N k hn hi hk le_rfl).trans
  dsimp [fourierBudget]
  gcongr
  exact harmonic_le_one_add_log N

/-- Absolute Fourier bounds give an absolute finite kernel-sum bound. -/
theorem kernel_sum_absolute (n K N : Nat) (F : ℝ) (hF : 0 ≤ F)
    (freq : ∀ k, 0 < k → k < K →
      ‖∑ j ∈ range N, character k (height (oddOrbit n j))‖ ≤ F) :
    (∑ j ∈ range N, kernel K (height (oddOrbit n j))) ≤
      (K : ℝ) * N + (K : ℝ)^2 * F := by
  by_cases hN : N = 0
  · simp [hN]
    positivity
  have nr : (0 : ℝ) < N := by exact_mod_cast Nat.pos_of_ne_zero hN
  have fq : ∀ k, 0 < k → k < K →
      ‖∑ j ∈ range N, character k (height (oddOrbit n j))‖ ≤ F / N * N := by
    intro k hk hK
    simpa only [div_mul_cancel₀ _ nr.ne'] using freq k hk hK
  have h := kernel_sum_bound n K N (F / N) (div_nonneg hF nr.le) fq
  simpa only [mul_assoc, div_mul_cancel₀ _ nr.ne'] using h

/-- A marked state above an explicit height cutoff has a uniformly large
nonnegative kernel. -/
theorem marked_kernel_above (x B K : Nat) (hm : Marked x) (hx : 2^B ≤ x)
    (hBK : 1120 * Real.pi * (K : ℝ) ≤ (B : ℝ) + 1) :
    (K : ℝ)^2 ≤ 4 * kernel K (height x) := by
  have xp : 0 < x := by have := hm.1; omega
  have lb : B ≤ x.log2 := (Nat.le_log2 xp.ne').mpr hx
  have lr : (B : ℝ) + 1 ≤ (x.log2 : ℝ) + 1 := by exact_mod_cast Nat.succ_le_succ lb
  obtain ⟨pl, pu⟩ := marked_phase_small hm
  rw [← kernel_sub_nat K (height x) x.log2]
  apply kernel_large
  intro r hr
  have rr : (r : ℝ) ≤ K := by exact_mod_cast hr.le
  have coeff : 4 * Real.pi * (r : ℝ) * (140 / ((x.log2 : ℝ) + 1)) ≤ 1 / 2 := by
    apply (le_div_iff₀ (by norm_num : (0 : ℝ) < 2)).mpr
    have den : (0 : ℝ) < (x.log2 : ℝ) + 1 := by positivity
    rw [show 4 * Real.pi * (r : ℝ) * (140 / ((x.log2 : ℝ) + 1)) * 2 =
      (1120 * Real.pi * r) / ((x.log2 : ℝ) + 1) by ring]
    apply (div_le_one den).mpr
    calc 1120 * Real.pi * (r : ℝ) ≤ 1120 * Real.pi * K := by gcongr
         _ ≤ (B : ℝ) + 1 := hBK
         _ ≤ _ := lr
  calc
    _ ≤ 4 * Real.pi * r * |height x - (x.log2 : ℝ)| := character_change _ _
    _ = 4 * Real.pi * r * (height x - (x.log2 : ℝ)) := by rw [abs_of_nonneg pl]
    _ ≤ 4 * Real.pi * r * (140 / ((x.log2 : ℝ) + 1)) := by gcongr
    _ ≤ _ := coeff

/-- Replacing the qualitative exceptional time interval by a finite set of
small integer values makes the counting bound uniform in the source. -/
theorem kernel_count_finite_values (f : Nat → Nat) (y : Nat → ℝ)
    (P : Nat → Prop) [DecidablePred P] (K N A : Nat)
    (hi : Set.InjOn f (↑(range N) : Set Nat))
    (large : ∀ j ∈ range N, A ≤ f j → P j → (K : ℝ)^2 ≤ 4 * kernel K (y j)) :
    (K : ℝ)^2 * (((range N).filter P).card : ℝ) ≤
      (K : ℝ)^2 * A + 4 * (∑ j ∈ range N, kernel K (y j)) := by
  classical
  let m := (range N).filter P
  let lo := m.filter (fun j => f j < A)
  let hiSet := m.filter (fun j => ¬ f j < A)
  have lowinj : Set.InjOn f (↑lo : Set Nat) := by
    intro i hi' j hj' h
    exact hi (mem_filter.mp (mem_filter.mp hi').1).1
      (mem_filter.mp (mem_filter.mp hj').1).1 h
  have lowimage : lo.image f ⊆ range A := by
    intro x hx
    obtain ⟨j, hj, rfl⟩ := mem_image.mp hx
    exact mem_range.mpr (mem_filter.mp hj).2
  have low : lo.card ≤ A := by
    have h := card_le_card lowimage
    simpa [card_image_of_injOn lowinj] using h
  have subhi : hiSet ⊆ range N := by
    intro j hj
    exact (mem_filter.mp (mem_filter.mp hj).1).1
  have high : (K : ℝ)^2 * (hiSet.card : ℝ) ≤
      4 * (∑ j ∈ range N, kernel K (y j)) := by
    calc
      _ = ∑ j ∈ hiSet, (K : ℝ)^2 := by simp [mul_comm]
      _ ≤ ∑ j ∈ hiSet, 4 * kernel K (y j) := by
        apply sum_le_sum
        intro j hj
        obtain ⟨jm, jl⟩ := mem_filter.mp hj
        exact large j (mem_filter.mp jm).1 (by omega) (mem_filter.mp jm).2
      _ = 4 * (∑ j ∈ hiSet, kernel K (y j)) := by rw [mul_sum]
      _ ≤ _ := mul_le_mul_of_nonneg_left
        (sum_le_sum_of_subset_of_nonneg subhi
          (by intro j _ _; exact kernel_nonneg _ _)) (by norm_num)
  have split : (m.card : ℝ) = (lo.card : ℝ) + (hiSet.card : ℝ) := by
    exact_mod_cast (card_filter_add_card_filter_not (s := m) (fun j => f j < A)).symm
  change (K : ℝ)^2 * (m.card : ℝ) ≤ _
  rw [split, mul_add]
  exact add_le_add
    (mul_le_mul_of_nonneg_left (by exact_mod_cast low) (sq_nonneg _)) high

/-- Uniform finite marked-occupation inequality.  The free parameters `B,K`
can be selected from the observation horizon, independently of the source. -/
theorem marked_visits_finite_bound (n N B K : Nat) (hn : 0 < n)
    (hi : Set.InjOn (oddOrbit n) (↑(range N) : Set Nat))
    (hBK : 1120 * Real.pi * (K : ℝ) ≤ (B : ℝ) + 1) :
    (K : ℝ)^2 * (markedVisits n N : ℝ) ≤
      (K : ℝ)^2 * (2 : ℝ)^B + 4 * K * N +
        4 * (K : ℝ)^2 * fourierBudget K N := by
  have count := kernel_count_finite_values (oddOrbit n)
    (fun j => height (oddOrbit n j)) (fun j => Marked (oddOrbit n j)) K N (2^B) hi
    (by intro j _ hj hm; exact marked_kernel_above _ B K hm hj hBK)
  have mean := kernel_sum_absolute n K N (fourierBudget K N)
    (fourierBudget_nonneg K N)
    (by intro k hk hK; exact odd_prefix_fourier_explicit n k N K hn hi hk hK.le)
  change (K : ℝ)^2 * (markedVisits n N : ℝ) ≤ _ at count
  push_cast at count
  nlinarith only [count, mean]

set_option exponentiation.threshold 1024 in
set_option maxRecDepth 4096 in
/-- At the first marked hit of this ordinary source, the canonical band
offset already exceeds the original source.  All eight displayed states
are odd, so these seven shortcut steps are also seven odd-only steps.
The check reduces exact natural-number arithmetic inside the kernel. -/
theorem first_marked_offset_above_source :
    let n : Nat := 2^601 - 1
    let x := orbit 7 n
    x = 3^7 * 2^594 - 1 ∧ x.log2 = 605 ∧ Marked x ∧
      n < x - 2^x.log2 ∧
      (∀ t : Fin 7, ¬ Marked (orbit t n)) ∧
      (∀ t : Fin 8, orbit t n % 2 = 1) := by
  decide

#print axioms reciprocal_set_harmonic
#print axioms odd_prefix_reciprocal_log
#print axioms odd_prefix_log_cocycle_harmonic
#print axioms odd_prefix_valuation_bound
#print axioms character_gap_budget
#print axioms odd_prefix_fourier_log
#print axioms marked_visits_finite_bound
#print axioms first_marked_offset_above_source

end CollatzShell.ForwardSection.AnalyticCoupling
