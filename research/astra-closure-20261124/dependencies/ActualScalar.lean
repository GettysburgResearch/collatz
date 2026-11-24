import Mathlib.Tactic
import Mathlib.Analysis.SpecificLimits.Normed
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Data.Nat.Factorization.Basic
import Mathlib.Topology.Algebra.InfiniteSum.Real

/-! The actual odd Collatz scalar. No custom axioms or abstract orbit input. -/
namespace Collatz.CarryTowerRoundTen.ActualScalar

set_option autoImplicit false

def gap (q : ℕ) : ℕ := (3 * q + 1).factorization 2
def oddMap (q : ℕ) : ℕ := (3 * q + 1) / 2 ^ gap q

def orbit (q : ℕ) : ℕ → ℕ
  | 0 => q
  | i + 1 => oddMap (orbit q i)

theorem oddMap_pos (q : ℕ) : 0 < oddMap q := by
  simpa [oddMap, gap] using Nat.ordCompl_pos 2 (show 3 * q + 1 ≠ 0 by omega)

theorem oddMap_odd (q : ℕ) : Odd (oddMap q) := by
  apply Nat.odd_iff.mpr
  apply Nat.two_dvd_ne_zero.mp
  simpa [oddMap, gap] using
    Nat.not_dvd_ordCompl Nat.prime_two (show 3 * q + 1 ≠ 0 by omega)

theorem complete_step (q : ℕ) : 2 ^ gap q * oddMap q = 3 * q + 1 := by
  simpa [oddMap, gap] using Nat.ordProj_mul_ordCompl_eq_self (3 * q + 1) 2

theorem gap_pos (q : ℕ) (hq : Odd q) : 1 ≤ gap q := by
  have hm := Nat.odd_iff.mp hq
  have hd : 2 ∣ 3 * q + 1 := by omega
  exact (Nat.prime_two.dvd_iff_one_le_factorization (by omega)).mp hd

theorem orbit_pos (q i : ℕ) (hq : 0 < q) : 0 < orbit q i := by
  cases i with
  | zero => exact hq
  | succ i => exact oddMap_pos (orbit q i)

theorem orbit_odd (q i : ℕ) (hq : Odd q) : Odd (orbit q i) := by
  cases i with
  | zero => exact hq
  | succ i => exact oddMap_odd (orbit q i)

theorem orbit_shift (q i : ℕ) : orbit (oddMap q) i = orbit q (i + 1) := by
  induction i with
  | zero => rfl
  | succ i ih => simp only [orbit, ih]

noncomputable def term (q i : ℕ) : ℝ := (gap (orbit q i) : ℝ) / 3 ^ (i + 1)
noncomputable def prefixSum (q n : ℕ) : ℝ := ∑ i ∈ Finset.range n, term q i
noncomputable def scalar (q : ℕ) : ℝ := ∑' i, term q i
noncomputable def logTwo (q : ℕ) : ℝ := Real.log q / Real.log 2
noncomputable def envelope (q : ℕ) : ℝ := 1 + logTwo q / 3

theorem term_nonneg (q i : ℕ) : 0 ≤ term q i := by unfold term; positivity

theorem term_shift (q i : ℕ) : term q (i + 1) = term (oddMap q) i / 3 := by
  simp only [term, orbit_shift, pow_succ]
  field_simp

theorem partial_succ (q n : ℕ) :
    prefixSum q (n + 1) = ((gap q : ℝ) + prefixSum (oddMap q) n) / 3 := by
  unfold prefixSum
  rw [Finset.sum_range_succ']
  simp only [term_shift]
  rw [← Finset.sum_div]
  have ht0 : term q 0 = (gap q : ℝ) / 3 := by simp [term, orbit]
  rw [ht0]
  ring

theorem logTwo_nonneg (q : ℕ) (hq : 0 < q) : 0 ≤ logTwo q := by
  apply div_nonneg
  · apply Real.log_nonneg
    exact_mod_cast hq
  · exact le_of_lt (Real.log_pos (by norm_num : (1 : ℝ) < 2))

theorem logarithmic_step (q : ℕ) (hq : 0 < q) :
    (gap q : ℝ) + logTwo (oddMap q) ≤ 2 + logTwo q := by
  have hqR : (0 : ℝ) < q := by exact_mod_cast hq
  have huR : (0 : ℝ) < oddMap q := by exact_mod_cast oddMap_pos q
  have he : (2 : ℝ) ^ gap q * (oddMap q : ℝ) = 3 * (q : ℝ) + 1 := by
    exact_mod_cast complete_step q
  have hbound : (2 : ℝ) ^ gap q * (oddMap q : ℝ) ≤ 4 * (q : ℝ) := by
    rw [he]
    have hq1 : (1 : ℝ) ≤ q := by exact_mod_cast hq
    linarith
  have hl := Real.log_le_log (mul_pos (pow_pos (by norm_num) _) huR) hbound
  rw [Real.log_mul (by positivity) huR.ne', Real.log_pow,
      Real.log_mul (by norm_num) hqR.ne'] at hl
  have hfour : Real.log (4 : ℝ) = 2 * Real.log 2 := by
    have h := Real.log_pow (2 : ℝ) 2
    norm_num at h
    exact h
  rw [hfour] at hl
  have htwo : (0 : ℝ) < Real.log 2 := Real.log_pos (by norm_num)
  unfold logTwo
  apply (mul_le_mul_iff_of_pos_right htwo).mp
  field_simp
  linarith

theorem envelope_step (q : ℕ) (hq : 0 < q) :
    ((gap q : ℝ) + envelope (oddMap q)) / 3 ≤ envelope q := by
  have hg := logarithmic_step q hq
  have hu := logTwo_nonneg (oddMap q) (oddMap_pos q)
  unfold envelope
  linarith

theorem partial_le_envelope (q n : ℕ) (hq : 0 < q) :
    prefixSum q n ≤ envelope q := by
  induction n generalizing q with
  | zero =>
    have h := logTwo_nonneg q hq
    simp only [prefixSum, Finset.range_zero, Finset.sum_empty, envelope]
    linarith
  | succ n ih =>
    rw [partial_succ]
    have hi := ih (oddMap q) (oddMap_pos q)
    have hs := envelope_step q hq
    linarith

theorem scalar_summable (q : ℕ) (hq : 0 < q) : Summable (term q) := by
  apply summable_of_sum_range_le (term_nonneg q)
  intro n
  exact partial_le_envelope q n hq

theorem scalar_upper (q : ℕ) (hq : 0 < q) : scalar q ≤ 1 + logTwo q / 3 := by
  exact (scalar_summable q hq).tsum_le_of_sum_range_le (fun n => partial_le_envelope q n hq)

theorem scalar_recurrence (q : ℕ) (hq : 0 < q) :
    scalar (oddMap q) = 3 * scalar q - gap q := by
  have hs := (scalar_summable q hq).tsum_eq_zero_add
  simp only [term_shift] at hs
  have hsum : (∑' i, term (oddMap q) i / 3) = scalar (oddMap q) / 3 := by
    simp only [div_eq_mul_inv, tsum_mul_right, scalar]
  rw [hsum] at hs
  have ht0 : term q 0 = (gap q : ℝ) / 3 := by simp [term, orbit]
  rw [ht0] at hs
  change scalar q = (gap q : ℝ) / 3 + scalar (oddMap q) / 3 at hs
  linarith

theorem baseline_sum : (∑' i : ℕ, (1 : ℝ) / 3 ^ (i + 1)) = 1 / 2 := by
  have hi : ∀ i : ℕ, (1 : ℝ) / 3 ^ (i + 1) = (1 / 3 : ℝ) ^ i * (1 / 3) := by
    intro i
    simp [pow_succ, mul_comm]
  simp_rw [hi]
  rw [tsum_mul_right, tsum_geometric_of_lt_one (by norm_num) (by norm_num)]
  norm_num

theorem baseline_summable : Summable (fun i : ℕ => (1 : ℝ) / 3 ^ (i + 1)) := by
  have hs := (summable_geometric_of_lt_one (by norm_num : (0 : ℝ) ≤ 1 / 3)
      (by norm_num : (1 / 3 : ℝ) < 1)).mul_right (1 / 3)
  convert hs using 1
  ext i
  simp [pow_succ, mul_comm]

theorem scalar_lower (q : ℕ) (hq : 0 < q) (hodd : Odd q) : 1 / 2 ≤ scalar q := by
  rw [← baseline_sum]
  apply Summable.tsum_le_tsum _ baseline_summable (scalar_summable q hq)
  intro i
  unfold term
  apply div_le_div_of_nonneg_right
  · exact_mod_cast gap_pos (orbit q i) (orbit_odd q i hodd)
  · positivity

theorem half_scalar_step (q : ℕ) (hq : 0 < q) (hodd : Odd q)
    (hh : scalar q = 1 / 2) : gap q = 1 ∧ scalar (oddMap q) = 1 / 2 := by
  have hs := scalar_recurrence q hq
  have hl := scalar_lower (oddMap q) (oddMap_pos q) (oddMap_odd q)
  have hg := gap_pos q hodd
  have hgr : (gap q : ℝ) ≤ 1 := by rw [hh] at hs; linarith
  have hgn : gap q ≤ 1 := by exact_mod_cast hgr
  have hg1 : gap q = 1 := by omega
  refine ⟨hg1, ?_⟩
  rw [hh, hg1] at hs
  norm_num at hs
  linarith

theorem not_all_gaps_one (q : ℕ) : ¬ (∀ i : ℕ, gap (orbit q i) = 1) := by
  intro hall
  have he : ∀ i : ℕ, 2 ^ i * (orbit q i + 1) = 3 ^ i * (q + 1) := by
    intro i
    induction i with
    | zero => simp [orbit]
    | succ i ih =>
      have hs := complete_step (orbit q i)
      rw [hall i] at hs
      norm_num only [pow_one] at hs
      have hm := congrArg (fun n : ℕ => 2 ^ i * n) hs
      simp only [orbit, pow_succ]
      nlinarith
  let i := q + 1
  have hd : 2 ^ i ∣ 3 ^ i * (q + 1) := ⟨orbit q i + 1, (he i).symm⟩
  have hc : Nat.Coprime (2 ^ i) (3 ^ i) := Nat.Coprime.pow i i (by decide)
  have hdiv : 2 ^ i ∣ q + 1 := hc.dvd_of_dvd_mul_left hd
  have hle := Nat.le_of_dvd (show 0 < q + 1 by omega) hdiv
  have hlt : q + 1 < 2 ^ i := Nat.lt_two_pow_self
  omega

theorem scalar_strict_lower (q : ℕ) (hq : 0 < q) (hodd : Odd q) :
    1 / 2 < scalar q := by
  by_contra hn
  have hh : scalar q = 1 / 2 := le_antisymm (le_of_not_gt hn) (scalar_lower q hq hodd)
  have ho : ∀ i : ℕ, scalar (orbit q i) = 1 / 2 := by
    intro i
    induction i with
    | zero => exact hh
    | succ i ih =>
      exact (half_scalar_step (orbit q i) (orbit_pos q i hq) (orbit_odd q i hodd) ih).2
  apply not_all_gaps_one q
  intro i
  exact (half_scalar_step (orbit q i) (orbit_pos q i hq) (orbit_odd q i hodd) (ho i)).1

/-- Exact finite prefix plus the actual tail scalar. -/
theorem scalar_tail (q n : ℕ) (hq : 0 < q) :
    scalar q = prefixSum q n + scalar (orbit q n) / 3 ^ n := by
  induction n generalizing q with
  | zero => simp [prefixSum, orbit]
  | succ n ih =>
    rw [partial_succ, ← orbit_shift, pow_succ]
    have ht := ih (oddMap q) (oddMap_pos q)
    have hs := scalar_recurrence q hq
    have hm := congrArg (fun x : ℝ => x * 3 ^ n) hs
    field_simp at ht ⊢
    nlinarith

theorem scalar_tail_lower (q n : ℕ) (hq : 0 < q) (hodd : Odd q) :
    prefixSum q n + (1 / 2 : ℝ) / 3 ^ n < scalar q := by
  have hp : (0 : ℝ) < 3 ^ n := by positivity
  calc
    _ < prefixSum q n + scalar (orbit q n) / 3 ^ n := by
      have hl := div_lt_div_of_pos_right
        (scalar_strict_lower (orbit q n) (orbit_pos q n hq) (orbit_odd q n hodd))
        hp
      linarith
    _ = scalar q := (scalar_tail q n hq).symm

theorem scalar_tail_upper (q n : ℕ) (hq : 0 < q) :
    scalar q ≤ prefixSum q n + (1 + logTwo (orbit q n) / 3) / 3 ^ n := by
  rw [scalar_tail q n hq]
  have hp : (0 : ℝ) ≤ 3 ^ n := by positivity
  have hu := div_le_div_of_nonneg_right
    (scalar_upper (orbit q n) (orbit_pos q n hq)) hp
  linarith

theorem gap_one : gap 1 = 2 := by
  change (2 ^ 2 : ℕ).factorization 2 = 2
  rw [Nat.prime_two.factorization_pow]
  norm_num

theorem oddMap_one : oddMap 1 = 1 := by norm_num [oddMap, gap_one]

theorem scalar_one : scalar 1 = 1 := by
  have h := scalar_recurrence 1 (by norm_num)
  rw [oddMap_one, gap_one] at h
  norm_num at h
  linarith

noncomputable def logPotential (q : ℕ) : ℝ := Real.log q - scalar q * Real.log 2

theorem logPotential_lower (q : ℕ) (hq : 0 < q) : -Real.log 2 ≤ logPotential q := by
  have hs := scalar_upper q hq
  have htwo : (0 : ℝ) < Real.log 2 := Real.log_pos (by norm_num)
  have hlog : (0 : ℝ) ≤ Real.log q := Real.log_nonneg (by exact_mod_cast hq)
  have hmul := mul_le_mul_of_nonneg_right hs (le_of_lt htwo)
  unfold logTwo at hmul
  field_simp at hmul
  unfold logPotential
  nlinarith

theorem logPotential_step (q : ℕ) (hq : 3 ≤ q) (hh : 1 ≤ scalar q) :
    logPotential (oddMap q) ≤ logPotential q + Real.log (5 / 6 : ℝ) := by
  have hqR : (0 : ℝ) < q := by exact_mod_cast (show 0 < q by omega)
  have huR : (0 : ℝ) < oddMap q := by exact_mod_cast oddMap_pos q
  have he : (2 : ℝ) ^ gap q * (oddMap q : ℝ) = 3 * (q : ℝ) + 1 := by
    exact_mod_cast complete_step q
  have hbound : (2 : ℝ) ^ gap q * (oddMap q : ℝ) ≤ (10 / 3) * (q : ℝ) := by
    rw [he]
    have hq3 : (3 : ℝ) ≤ q := by exact_mod_cast hq
    linarith
  have hl := Real.log_le_log (mul_pos (pow_pos (by norm_num) _) huR) hbound
  rw [Real.log_mul (by positivity) huR.ne', Real.log_pow,
      Real.log_mul (by norm_num) hqR.ne'] at hl
  have hratio : Real.log (10 / 3 : ℝ) = 2 * Real.log 2 + Real.log (5 / 6 : ℝ) := by
    rw [show (10 / 3 : ℝ) = 2 ^ 2 * (5 / 6) by norm_num,
      Real.log_mul (by norm_num) (by norm_num), Real.log_pow]
    norm_num
  rw [hratio] at hl
  have hs := scalar_recurrence q (by omega)
  have htwo : (0 : ℝ) < Real.log 2 := Real.log_pos (by norm_num)
  have hc : 0 ≤ (scalar q - 1) * Real.log 2 :=
    mul_nonneg (by linarith) htwo.le
  unfold logPotential
  rw [hs]
  nlinarith

theorem scalar_orbit_integer (q i : ℕ) (hq : 0 < q)
    (hi : ∃ z : ℤ, scalar q = z) : ∃ z : ℤ, scalar (orbit q i) = z := by
  induction i with
  | zero => exact hi
  | succ i ih =>
    rcases ih with ⟨z, hz⟩
    refine ⟨3 * z - (gap (orbit q i) : ℤ), ?_⟩
    change scalar (oddMap (orbit q i)) = _
    rw [scalar_recurrence (orbit q i) (orbit_pos q i hq), hz]
    push_cast
    ring

theorem integral_scalar_ge_one (q : ℕ) (hq : 0 < q) (hodd : Odd q)
    (hi : ∃ z : ℤ, scalar q = z) : 1 ≤ scalar q := by
  rcases hi with ⟨z, hz⟩
  have hlow := scalar_lower q hq hodd
  have hzR : (0 : ℝ) < z := by rw [← hz]; linarith
  have hzZ : (0 : ℤ) < z := by exact_mod_cast hzR
  have hz1 : (1 : ℤ) ≤ z := by omega
  rw [hz]
  exact_mod_cast hz1

def Converges (q : ℕ) : Prop := ∃ i : ℕ, orbit q i = 1

/-- Integer scalar arithmetic forces an actual iterate of the defined map to one. -/
theorem integer_scalar_converges (q : ℕ) (hq : 0 < q) (hodd : Odd q)
    (hi : ∃ z : ℤ, scalar q = z) : Converges q := by
  by_contra hn
  have havoid : ∀ i, orbit q i ≠ 1 := by simpa [Converges] using hn
  have hthree : ∀ i, 3 ≤ orbit q i := by
    intro i
    have hp := orbit_pos q i hq
    have ho := Nat.odd_iff.mp (orbit_odd q i hodd)
    have ha := havoid i
    omega
  have hinteger : ∀ i, 1 ≤ scalar (orbit q i) := by
    intro i
    exact integral_scalar_ge_one (orbit q i) (orbit_pos q i hq)
      (orbit_odd q i hodd) (scalar_orbit_integer q i hq hi)
  have hdec : ∀ i : ℕ, logPotential (orbit q i) ≤
      logPotential q + (i : ℝ) * Real.log (5 / 6 : ℝ) := by
    intro i
    induction i with
    | zero => simp [orbit]
    | succ i ih =>
      have hs := logPotential_step (orbit q i) (hthree i) (hinteger i)
      change logPotential (oddMap (orbit q i)) ≤ _
      push_cast
      linarith
  have hneg : Real.log (5 / 6 : ℝ) < 0 := Real.log_neg (by norm_num) (by norm_num)
  obtain ⟨n, hn⟩ := exists_nat_gt ((logPotential q + Real.log 2) /
    (-Real.log (5 / 6 : ℝ)))
  have hlarge : logPotential q + Real.log 2 <
      (n : ℝ) * (-Real.log (5 / 6 : ℝ)) := by
    exact (div_lt_iff₀ (by linarith)).mp hn
  have hlower := logPotential_lower (orbit q n) (orbit_pos q n hq)
  have hupper := hdec n
  linarith

/-- A supplied ternary denominator clears along the actual orbit. -/
theorem triadic_scalar_converges (q : ℕ) (hq : 0 < q) (hodd : Odd q)
    (a : ℤ) (r : ℕ) (ha : scalar q = (a : ℝ) / 3 ^ r) : Converges q := by
  induction r generalizing q a with
  | zero =>
    apply integer_scalar_converges q hq hodd
    exact ⟨a, by simpa using ha⟩
  | succ r ih =>
    have hu : scalar (oddMap q) =
        ((a - (gap q : ℤ) * 3 ^ r : ℤ) : ℝ) / 3 ^ r := by
      rw [scalar_recurrence q hq, ha]
      push_cast
      rw [pow_succ]
      field_simp
    rcases ih (oddMap q) (oddMap_pos q) (oddMap_odd q)
      (a - (gap q : ℤ) * 3 ^ r) hu with ⟨i, hi⟩
    refine ⟨i + 1, ?_⟩
    rw [← orbit_shift]
    exact hi

theorem scalar_triadic_of_iterate_one (q n : ℕ) (hq : 0 < q)
    (h : orbit q n = 1) : ∃ a : ℤ, scalar q = (a : ℝ) / 3 ^ n := by
  induction n generalizing q with
  | zero =>
    have hq1 : q = 1 := h
    subst q
    exact ⟨1, by norm_num [scalar_one]⟩
  | succ n ih =>
    have hu : orbit (oddMap q) n = 1 := by rw [orbit_shift]; exact h
    rcases ih (oddMap q) (oddMap_pos q) hu with ⟨a, ha⟩
    refine ⟨a + (gap q : ℤ) * 3 ^ n, ?_⟩
    have hs := scalar_recurrence q hq
    rw [ha] at hs
    push_cast
    rw [pow_succ]
    field_simp at hs ⊢
    nlinarith

/-- Full actual-map equivalence; the right-hand arithmetic is not asserted universally. -/
theorem converges_iff_triadic (q : ℕ) (hq : 0 < q) (hodd : Odd q) :
    Converges q ↔ ∃ a : ℤ, ∃ r : ℕ, scalar q = (a : ℝ) / 3 ^ r := by
  constructor
  · rintro ⟨r, hr⟩
    rcases scalar_triadic_of_iterate_one q r hq hr with ⟨a, ha⟩
    exact ⟨a, r, ha⟩
  · rintro ⟨a, r, ha⟩
    exact triadic_scalar_converges q hq hodd a r ha

end Collatz.CarryTowerRoundTen.ActualScalar
