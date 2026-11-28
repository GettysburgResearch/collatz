import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Positivity

/-! Exact rational triangular observables on the doubling-log circles. -/
set_option autoImplicit false
set_option warningAsError true

namespace Collatz.CyclicTent
open scoped BigOperators

/-- Number of multiples of `m` in `(d,d+L]`, written over the rationals. -/
def hits (m L d : ℕ) : ℚ := ((d+L)/m:ℕ) - ((d/m:ℕ) : ℚ)

/-- Unnormalized circular convolution of two length-`L` intervals. -/
def tent (m L d : ℕ) : ℚ := ∑ u ∈ Finset.range L, hits m L (d+u)

theorem hits_bounds (m L d : ℕ) (hm : 0<m) :
    ((L/m:ℕ) : ℚ) ≤ hits m L d ∧ hits m L d ≤ ((L/m:ℕ) : ℚ)+1 := by
  unfold hits
  rw [Nat.add_div hm]
  split <;> simp only [Nat.cast_add, Nat.cast_one, Nat.cast_zero] <;> constructor <;> linarith

theorem hits_nonneg (m L d : ℕ) (hm : 0<m) : 0 ≤ hits m L d :=
  (Nat.cast_nonneg _).trans (hits_bounds m L d hm).1

theorem tent_nonneg (m L d : ℕ) (hm : 0<m) : 0≤tent m L d :=
  Finset.sum_nonneg fun u _ => hits_nonneg m L (d+u) hm

theorem hits_period (m L d : ℕ) (hm : 0<m) : hits m L (d+m) = hits m L d := by
  unfold hits
  rw [show d+m+L=d+L+m by omega, Nat.add_div_right _ hm, Nat.add_div_right _ hm]
  simp only [Nat.cast_add,Nat.cast_one]
  ring

theorem tent_period (m L d : ℕ) (hm : 0<m) : tent m L (d+m)=tent m L d := by
  unfold tent
  apply Finset.sum_congr rfl
  intro i _
  rw [show d+m+i=d+i+m by omega,hits_period _ _ _ hm]

theorem tent_step (m L d : ℕ) (hm : 0<m) :
    |tent m L (d+1)-tent m L d|≤1 := by
  have right := Finset.sum_range_succ (fun u => hits m L (d+u)) L
  have left := Finset.sum_range_succ' (fun u => hits m L (d+u)) L
  have shift : tent m L (d+1) + hits m L d = tent m L d + hits m L (d+L) := by
    unfold tent
    have hsum : (∑ u ∈ Finset.range L, hits m L (d+1+u)) =
        ∑ u ∈ Finset.range L, hits m L (d+(u+1)) := by
      apply Finset.sum_congr rfl
      intro u _
      rw [show d+1+u=d+(u+1) by omega]
    rw [hsum]
    simpa only [Nat.add_zero] using left.symm.trans right
  have ha := hits_bounds m L d hm
  have hb := hits_bounds m L (d+L) hm
  rw [abs_le]
  constructor <;> linarith [ha.1,ha.2,hb.1,hb.2]

private theorem div_triple (a m : ℕ) (hm : 0<m) :
    a/m = a/(3*m)+(a+m)/(3*m)+(a+2*m)/(3*m) := by
  simp only [Nat.mul_comm 3 m, ← Nat.div_div_eq_div_mul]
  rw [Nat.add_div_right _ hm, show a+2*m=a+m*2 by omega, Nat.add_mul_div_left _ _ hm]
  omega

theorem hits_triple (m L d : ℕ) (hm : 0<m) : hits m L d =
    hits (3*m) L d + hits (3*m) L (d+m) + hits (3*m) L (d+2*m) := by
  have hstart : ((d/m:ℕ) : ℚ) = ((d/(3*m):ℕ):ℚ)+((d+m)/(3*m):ℕ)+((d+2*m)/(3*m):ℕ) := by
    exact_mod_cast div_triple d m hm
  have hend : (((d+L)/m:ℕ) : ℚ) = (((d+L)/(3*m):ℕ):ℚ)+((d+L+m)/(3*m):ℕ)+((d+L+2*m)/(3*m):ℕ) := by
    exact_mod_cast div_triple (d+L) m hm
  unfold hits
  rw [show d+m+L=d+L+m by omega, show d+2*m+L=d+L+2*m by omega,hstart,hend]
  ring

theorem tent_triple (m L d : ℕ) (hm : 0<m) : tent m L d =
    tent (3*m) L d + tent (3*m) L (d+m) + tent (3*m) L (d+2*m) := by
  unfold tent
  rw [← Finset.sum_add_distrib,← Finset.sum_add_distrib]
  apply Finset.sum_congr rfl
  intro i _
  rw [show d+m+i=d+i+m by omega,show d+2*m+i=d+i+2*m by omega]
  exact hits_triple m L (d+i) hm

private theorem hits_two (L d : ℕ) : hits 2 L d + hits 2 L (d+1) = L := by
  have hstart : d/2 +(d+1)/2 = d := by omega
  have hend : (d+L)/2 +(d+1+L)/2 = d+L := by omega
  have hc : ((d/2:ℕ):ℚ)+((d+1)/2:ℕ) = d := by exact_mod_cast hstart
  have hd : (((d+L)/2:ℕ):ℚ)+((d+1+L)/2:ℕ) = (d:ℚ)+L := by exact_mod_cast hend
  unfold hits
  linarith

theorem tent_two_bound (L d : ℕ) : 2*tent 2 L d≤(L:ℚ)^2+1 := by
  have hsum : tent 2 L d + tent 2 L (d+1) = (L:ℚ)^2 := by
    unfold tent
    rw [← Finset.sum_add_distrib]
    calc
      _ = ∑ _u∈Finset.range L,(L:ℚ) := by
        apply Finset.sum_congr rfl
        intro u _
        rw [show d+1+u=d+u+1 by omega]
        exact hits_two L (d+u)
      _ = _ := by simp [pow_two]
  have hs := (abs_le.mp (tent_step 2 L d (by decide))).1
  linarith

theorem tent_peak (m L d : ℕ) (hm : 0<m) (hcenter : m ∣ d+L) : (L:ℚ) ≤ tent m L d := by
  obtain ⟨q,hq⟩ := hcenter
  have hol : (d+L)/m=q := by rw [hq,Nat.mul_div_right _ hm]
  calc
    (L:ℚ) = ∑ _u∈Finset.range L,(1:ℚ) := by simp
    _ ≤ _ := by
      apply Finset.sum_le_sum
      intro u hu
      have hu' := Finset.mem_range.mp hu
      have hlow : (d+u)/m < q := (Nat.div_lt_iff_lt_mul hm).2 (by rw [Nat.mul_comm q m,←hq]; omega)
      have hhigh : q≤(d+u+L)/m := by rw [←hol]; exact Nat.div_le_div_right (by omega)
      unfold hits
      have hnat : (d+u)/m + 1 ≤ (d+u+L)/m := by omega
      have hrat : (((d+u)/m:ℕ):ℚ)+1 ≤ ((d+u+L)/m:ℕ) := by exact_mod_cast hnat
      linarith

end Collatz.CyclicTent
