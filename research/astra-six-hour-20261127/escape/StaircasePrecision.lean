import StaircasePade
import Mathlib.Algebra.Ring.Parity

/-! Exact binary order of every nonempty finite Padé remainder tail on the
native parameter range. Odd numerator/denominator witnesses keep the
statement entirely over the rationals. -/

namespace StaircasePrecision

open StaircaseAffine StaircasePade Polynomial

def AtLeast (k : ℕ) (q : ℚ) : Prop :=
  ∃ m d : ℤ, Odd d ∧ q = (2:ℚ)^k * m / d

def Exact (k : ℕ) (q : ℚ) : Prop :=
  ∃ m d : ℤ, Odd m ∧ Odd d ∧ q = (2:ℚ)^k * m / d

private theorem odd_nz {d : ℤ} (hd : Odd d) : (d : ℚ) ≠ 0 := by
  have h := Int.odd_iff.mp hd
  have hd' : d ≠ 0 := by omega
  exact_mod_cast hd'

theorem exact_nonzero {k : ℕ} {q : ℚ} (h : Exact k q) : q ≠ 0 := by
  obtain ⟨m,d,hm,hd,rfl⟩ := h
  exact div_ne_zero (mul_ne_zero (pow_ne_zero _ (by norm_num)) (odd_nz hm)) (odd_nz hd)

theorem exact_atLeast {k : ℕ} {q : ℚ} (h : Exact k q) : AtLeast k q := by
  obtain ⟨m,d,_,hd,hq⟩ := h
  exact ⟨m,d,hd,hq⟩

theorem lower {j k : ℕ} {q : ℚ} (hj : j ≤ k) (h : AtLeast k q) : AtLeast j q := by
  obtain ⟨l,rfl⟩ := Nat.exists_eq_add_of_le hj
  obtain ⟨m,d,hd,rfl⟩ := h
  refine ⟨2^l*m, d, hd, ?_⟩
  push_cast
  rw [pow_add]
  ring

theorem mul_exact {i j : ℕ} {q r : ℚ} (hq : Exact i q) (hr : Exact j r) :
    Exact (i+j) (q*r) := by
  obtain ⟨m,d,hm,hd,rfl⟩ := hq
  obtain ⟨n,e,hn,he,rfl⟩ := hr
  refine ⟨m*n,d*e,hm.mul hn,hd.mul he,?_⟩
  push_cast
  rw [pow_add]
  ring

theorem one_exact : Exact 0 1 := by
  exact ⟨1,1,by decide,by decide,by norm_num⟩

theorem pow_exact {i : ℕ} {q : ℚ} (hq : Exact i q) (j : ℕ) :
    Exact (i*j) (q^j) := by
  induction j with
  | zero => simpa using one_exact
  | succ j ih => simpa [Nat.mul_succ, pow_succ] using mul_exact ih hq

theorem add_lower {k : ℕ} {q r : ℚ} (hq : AtLeast k q) (hr : AtLeast k r) :
    AtLeast k (q+r) := by
  obtain ⟨m,d,hd,rfl⟩ := hq
  obtain ⟨n,e,he,rfl⟩ := hr
  refine ⟨m*e+n*d,d*e,hd.mul he,?_⟩
  push_cast
  field_simp [odd_nz hd, odd_nz he]

theorem exact_add_higher {k : ℕ} {q r : ℚ} (hq : Exact k q) (hr : AtLeast (k+1) r) :
    Exact k (q+r) := by
  obtain ⟨m,d,hm,hd,rfl⟩ := hq
  obtain ⟨n,e,he,rfl⟩ := hr
  refine ⟨m*e+2*n*d,d*e,(hm.mul he).add_even ((even_two.mul_right n).mul_right d),hd.mul he,?_⟩
  push_cast
  rw [pow_succ]
  field_simp [odd_nz hd, odd_nz he]

theorem one_sub_higher {q : ℚ} (hq : AtLeast 1 q) : Exact 0 (1-q) := by
  obtain ⟨m,d,hd,rfl⟩ := hq
  refine ⟨d-2*m,d,hd.sub_even (even_two.mul_right m),hd,?_⟩
  push_cast
  simp only [pow_one, pow_zero, one_mul]
  field_simp [odd_nz hd]

theorem zero_lower (k : ℕ) : AtLeast k 0 := by
  exact ⟨0,1,by decide,by simp⟩

theorem sum_lower {n k : ℕ} (f : ℕ → ℚ)
    (h : ∀ i < n, AtLeast k (f i)) : AtLeast k (∑ i ∈ Finset.range n, f i) := by
  induction n with
  | zero => simpa using zero_lower k
  | succ n ih =>
    rw [Finset.sum_range_succ]
    exact add_lower (ih (fun i hi => h i (by omega))) (h n (by omega))

theorem prod_unit {n : ℕ} (f : ℕ → ℚ)
    (h : ∀ i < n, Exact 0 (f i)) : Exact 0 (∏ i ∈ Finset.range n, f i) := by
  induction n with
  | zero => simpa using one_exact
  | succ n ih =>
    rw [Finset.prod_range_succ]
    exact mul_exact (ih (fun i hi => h i (by omega))) (h n (by omega))

theorem surviving_filter_unit {v n t : ℕ} {a : ℚ} (hv : 0 < v) (hn : n < t)
    (ha : Exact v a) : Exact 0 ((filterPoly a n).eval (a^t)) := by
  rw [filterPoly, eval_prod]
  apply prod_unit
  intro j hj
  simp only [eval_sub, eval_one, eval_mul, eval_C, eval_X]
  obtain ⟨k,hk⟩ := Nat.exists_eq_add_of_le (show j+1 ≤ t by omega)
  have hk' : 0 < k := by omega
  rw [hk, pow_add a (j+1) k, inv_mul_cancel_left₀ (pow_ne_zero _ (exact_nonzero ha))]
  exact one_sub_higher (lower (by nlinarith) (exact_atLeast (pow_exact ha k)))

theorem term_exact {v w j : ℕ} {a z : ℚ} (ha : Exact v a) (hz : Exact w z) :
    Exact (w*j + v*tri j) (term a z j) := by
  exact mul_exact (pow_exact hz j) (pow_exact ha (tri j))

theorem surviving_block_exact {v w n t : ℕ} (m : ℕ) {a z : ℚ}
    (hv : 0 < v) (ht : n < t) (ha : Exact v a) (hz : Exact w z) :
    Exact (w*(m+t)+v*tri (m+t)) (block a z m t (filterPoly a n)) := by
  rw [block_eq a z (exact_nonzero ha) (exact_nonzero hz)]
  simpa using mul_exact (surviving_filter_unit hv ht ha) (term_exact (j := m+t) ha hz)

theorem tri_mono : Monotone tri := by
  apply monotone_nat_of_le_succ
  intro n
  simp [tri]

theorem remainder_order {v w n : ℕ} (m N : ℕ) {a z : ℚ} (hv : 0 < v) (hw : 0 < w)
    (ha : Exact v a) (hz : Exact w z) :
    Exact (w*(m+(n+1))+v*tri (m+(n+1)))
      (∑ t ∈ Finset.range (N+1), block a z m (n+1+t) (filterPoly a n)) := by
  rw [Finset.sum_range_succ']
  simp only [Nat.add_zero]
  rw [add_comm (∑ k ∈ Finset.range N, block a z m (n+1+(k+1)) (filterPoly a n))]
  apply exact_add_higher (surviving_block_exact m hv (by omega) ha hz)
  apply sum_lower
  intro i _
  apply lower _ (exact_atLeast (surviving_block_exact m hv (show n < n+1+(i+1) by omega) ha hz))
  have hp := tri_mono (show m+(n+1) ≤ m+(n+1+(i+1)) by omega)
  have hq := Nat.mul_le_mul_left v hp
  have hw' := Nat.mul_lt_mul_of_pos_left (show m+(n+1) < m+(n+1+(i+1)) by omega) hw
  omega

theorem native_parameter (v p : ℕ) : Exact v ((2:ℚ)^v/3^p) := by
  refine ⟨1,3^p,by decide,(show Odd (3:ℤ) by decide).pow,?_⟩
  push_cast
  ring

end StaircasePrecision

#print axioms StaircasePrecision.exact_nonzero
#print axioms StaircasePrecision.surviving_filter_unit
#print axioms StaircasePrecision.surviving_block_exact
#print axioms StaircasePrecision.remainder_order
#print axioms StaircasePrecision.native_parameter
