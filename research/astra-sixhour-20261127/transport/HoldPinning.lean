import Mathlib.RingTheory.Coprime.Lemmas
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Ring

/-! Dyadic identification of the previous rank-zero hold's odd count. -/
namespace Collatz.HoldPinning

set_option autoImplicit false

private theorem nine_four (k : ℕ) : ∃ z : ℤ, (9 : ℤ)^k = 4*z+1 := by
  induction k with
  | zero => exact ⟨0, by norm_num⟩
  | succ k ih =>
    obtain ⟨z, hz⟩ := ih
    exact ⟨9*z+2, by rw [pow_succ,hz]; ring⟩

private theorem nine_even (k : ℕ) : ∃ z : ℤ, (9 : ℤ)^(2*k) = 16*z+1 := by
  induction k with
  | zero => exact ⟨0, by norm_num⟩
  | succ k ih =>
    obtain ⟨z,hz⟩ := ih
    refine ⟨81*z+5, ?_⟩
    rw [show 2*(k+1) = 2*k+2 by omega, pow_add, hz]
    ring

private theorem nine_factor (n : ℕ) (hn : 0 < n) :
    ∃ a b : ℤ, 0 < a ∧ a ≤ 8*n ∧ Odd b ∧ (9 : ℤ)^n - 1 = a*b := by
  induction n using Nat.strong_induction_on with
  | h n ih =>
    by_cases he : Even n
    · obtain ⟨k,hk⟩ := he
      have hk' : k < n := by omega
      obtain ⟨a,b,ha,hb,hodd,heq⟩ := ih k hk' (by omega)
      obtain ⟨z,hz⟩ := nine_four k
      refine ⟨2*a,b*(2*z+1), by omega, by omega, hodd.mul ⟨z,rfl⟩, ?_⟩
      rw [hk,pow_add]
      linear_combination (9^k+1)*heq + a*b*hz
    · have ho : Odd n := Nat.not_even_iff_odd.mp he
      obtain ⟨k,hk⟩ := ho
      obtain ⟨z,hz⟩ := nine_even k
      refine ⟨8,18*z+1,by norm_num,by omega,⟨9*z, by ring⟩,?_⟩
      rw [hk,pow_succ,hz]
      ring

private theorem dyadic_power_gap (k n : ℕ) (hn : 0 < n)
    (hd : (2 : ℤ)^k ∣ (3 : ℤ)^n - 1) : 2^k ≤ 8 * n := by
  obtain ⟨a,b,ha,hbound,hodd,heq⟩ := nine_factor n hn
  have hfact : (3^n - 1 : ℤ) * (3^n + 1) = 9^n - 1 := by
    rw [show (9 : ℤ) = 3^2 by norm_num, ← pow_mul, mul_comm 2 n, pow_mul]
    ring
  have hd' : (2 : ℤ)^k ∣ a*b := heq ▸ hfact ▸ hd.trans (dvd_mul_right _ _)
  have hda := (hodd.isCoprime_two.symm.pow_left (m := k)).dvd_of_dvd_mul_right hd'
  have hle := (Int.le_of_dvd ha hda).trans hbound
  exact_mod_cast hle

private theorem unequal_power_bound (k u v : ℕ) (h : v < u)
    (hd : (2 : ℤ)^k ∣ (3 : ℤ)^u - 3^v) : 2^k ≤ 8 * (u - v) := by
  have hu : u = v + (u - v) := by omega
  have he : (3 : ℤ)^u - 3^v = 3^v * (3^(u-v) - 1) := by
    conv_lhs => lhs; rw [hu, pow_add]
    ring
  rw [he] at hd
  have hc : IsCoprime ((2 : ℤ)^k) ((3 : ℤ)^v) :=
    ((show Odd (3 : ℤ) by decide).isCoprime_two.symm.pow_left (m := k)).pow_right (n := v)
  exact dyadic_power_gap k (u-v) (by omega) (hc.dvd_of_dvd_mul_left hd)

/-- Once the intervening segment is fixed, a sufficiently deep next rank-zero
hold identifies the preceding hold's odd count in its full clock budget. -/
theorem odd_count_unique (k H u v : ℕ) (a b : ℤ) (ha : Odd a)
    (hh : 8 * H < 2^k) (hu : u ≤ H) (hv : v ≤ H)
    (h1 : (2 : ℤ)^k ∣ a * 3^u + b) (h2 : (2 : ℤ)^k ∣ a * 3^v + b) :
    u = v := by
  have hdiff : (2 : ℤ)^k ∣ a * (3^u - 3^v) := by
    convert dvd_sub h1 h2 using 1
    ring
  have hclean := (ha.isCoprime_two.symm.pow_left (m := k)).dvd_of_dvd_mul_left hdiff
  rcases lt_trichotomy u v with h | h | h
  · have hrev : (2 : ℤ)^k ∣ (3 : ℤ)^v - 3^u := by simpa using dvd_neg.mpr hclean
    have hh' := unequal_power_bound k v u h hrev
    omega
  · exact h
  · have hh' := unequal_power_bound k u v h hclean
    omega

#print axioms odd_count_unique

end Collatz.HoldPinning
