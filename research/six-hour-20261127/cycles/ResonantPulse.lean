import Mathlib.Algebra.Ring.GeomSum
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity
import Lean.Elab.Tactic.Omega

/-! Exact support of positive periodic pulses at roots of unity. -/

namespace ResonantPulse

variable {K : Type*} [Field K]
variable {ι : Type*}

def pulse (x : K) (period repeats : ℕ) : K :=
  ∑ j ∈ Finset.range repeats, x ^ (period * j)

theorem pulse_at_root (x : K) (period repeats order : ℕ)
    (ho : x ^ period = 1 ↔ order ∣ period) (h : x ^ (period * repeats) = 1) :
    pulse x period repeats = if order ∣ period then (repeats : K) else 0 := by
  split
  · next hdiv => simp [pulse, pow_mul, ho.mpr hdiv]
  · next hnd =>
      simp only [pulse, pow_mul]
      have hzero := geom_sum_mul (x ^ period) repeats
      rw [← pow_mul, h, sub_self] at hzero
      exact (mul_eq_zero.mp hzero).resolve_right (sub_ne_zero.mpr (fun he => hnd (ho.mp he)))

def activeWeight (s : Finset ι) (w t m : ι → ℕ) (order : ℕ) : ℕ :=
  ∑ i ∈ s, if order ∣ t i then w i * m i else 0

theorem weighted_at_order (x : K) (s : Finset ι) (w t m : ι → ℕ) (order n : ℕ)
    (horder : ∀ j : ℕ, x ^ j = 1 ↔ order ∣ j)
    (hall : x ^ n = 1) (hperiod : ∀ i ∈ s, t i * m i = n) :
    ∑ i ∈ s, (w i : K) * pulse x (t i) (m i) = (activeWeight s w t m order : K) := by
  classical
  simp only [activeWeight, Nat.cast_sum]
  apply Finset.sum_congr rfl
  intro i hi
  rw [pulse_at_root x (t i) (m i) order (horder _) (by simpa only [hperiod i hi] using hall)]
  split <;> simp_all

theorem activeWeight_pos (s : Finset ι) (w t m : ι → ℕ) (order : ℕ)
    (hw : ∀ i ∈ s, 0 < w i) (hm : ∀ i ∈ s, 0 < m i) :
    0 < activeWeight s w t m order ↔ ∃ i ∈ s, order ∣ t i := by
  constructor
  · intro ha
    by_contra! hn
    have hz : activeWeight s w t m order = 0 := by
      apply Finset.sum_eq_zero
      intro i hi
      simp [hn i hi]
    omega
  · rintro ⟨i, hi, hd⟩
    have hle := Finset.single_le_sum (f := fun j => if order ∣ t j then w j * m j else 0)
      (fun j _ => Nat.zero_le _) hi
    have hp := Nat.mul_pos (hw i hi) (hm i hi)
    simp [hd] at hle
    exact hp.trans_le hle

theorem residual_at_order [CharZero K] (x : K) (s : Finset ι) (w t m : ι → ℕ) (order n shift : ℕ)
    (horder : ∀ j : ℕ, x ^ j = 1 ↔ order ∣ j)
    (hall : x ^ n = 1) (hperiod : ∀ i ∈ s, t i * m i = n)
    (hw : ∀ i ∈ s, 0 < w i) (hm : ∀ i ∈ s, 0 < m i) :
    (x ^ shift - 1) * (∑ i ∈ s, (w i : K) * pulse x (t i) (m i)) ≠ 0 ↔
      ¬ order ∣ shift ∧ ∃ i ∈ s, order ∣ t i := by
  have hleft : x ^ shift ≠ 1 ↔ ¬ order ∣ shift := not_congr (horder shift)
  have hright : (activeWeight s w t m order : K) ≠ 0 ↔ ∃ i ∈ s, order ∣ t i := by
    rw [Nat.cast_ne_zero, ← Nat.pos_iff_ne_zero, activeWeight_pos s w t m order hw hm]
  rw [weighted_at_order x s w t m order n horder hall hperiod, mul_ne_zero_iff,
      sub_ne_zero, hleft, hright]

#print axioms pulse_at_root
#print axioms weighted_at_order
#print axioms activeWeight_pos
#print axioms residual_at_order

end ResonantPulse
