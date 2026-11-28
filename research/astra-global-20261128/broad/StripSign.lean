import PadeArithmetic
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Tactic.Positivity

/-! A finite signed sum retains the sign of its first nonzero integer coefficient
when consecutive positive weights are sufficiently separated. -/
set_option autoImplicit false
set_option warningAsError true

namespace Collatz.StripSign
open scoped BigOperators

private theorem tail_series (w : ℕ→ℚ) (hw : ∀ j,0≤w j) (a L : ℕ)
    (hd : ∀ j<L-1,2*w (a+j+1)≤w (a+j)) :
    (∑ j ∈ Finset.range L,w (a+j))≤2*w a := by
  induction L generalizing a with
  | zero => simp only [Finset.range_zero,Finset.sum_empty]; linarith [hw a]
  | succ L ih =>
    cases L with
    | zero =>
      change (∑ j∈Finset.range 1,w (a+j))≤2*w a
      rw [Finset.sum_range_one,Nat.add_zero]
      linarith [hw a]
    | succ L =>
      rw [Finset.sum_range_succ']
      have h0 := hd 0 (by omega)
      simp only [add_zero] at h0
      have hi := ih (a+1) (fun j hj => by
        have hx := hd (j+1) (by omega)
        simpa only [show a+(j+1)=a+1+j by omega] using hx)
      have he : (fun j : ℕ => w (a+(j+1)))=(fun j => w (a+1+j)) := by
        funext j
        congr 1
        omega
      rw [he]
      change (∑ j∈Finset.range (L+1),w (a+1+j))+w a≤2*w a
      linarith

/-- A strictly positive first coefficient decides the sign of the finite evaluation. -/
theorem eval_pos (q : ℕ→ℤ) (w : ℕ→ℚ) (B h k : ℕ)
    (hB : 0<B) (hk : k≤h) (hzero : ∀ j<k,q j=0) (hfirst : 0<q k)
    (hcoef : ∀ j≤h,|q j|≤(B:ℤ)) (hw : ∀ j,0<w j)
    (hd : ∀ j<h,4*(B:ℚ)*w (j+1)≤w j) :
    0<∑ j ∈ Finset.range (h+1),(q j:ℚ)*w j := by
  let f (j : ℕ) : ℚ := (q j:ℚ)*w j
  have hpre : (∑ j ∈ Finset.range k,f j)=0 := by
    apply Finset.sum_eq_zero
    intro j hj
    simp [f,hzero j (Finset.mem_range.mp hj)]
  have hcut : (∑ j ∈ Finset.range (h+1),f j)=
      f k+∑ j ∈ Finset.range (h-k),f (k+1+j) := by
    rw [show h+1=(k+1)+(h-k) by omega,Finset.sum_range_add,Finset.sum_range_succ,hpre,zero_add]
  have hf : w k≤f k := by
    have hc : (1:ℚ)≤q k := by exact_mod_cast (show (1:ℤ)≤q k by omega)
    simpa only [one_mul] using mul_le_mul_of_nonneg_right hc (hw k).le
  change 0<∑ j ∈ Finset.range (h+1),f j
  rw [hcut]
  by_cases hlast : k=h
  · subst k
    simpa only [Nat.sub_self,Finset.sum_range_zero,add_zero] using (hw h).trans_le hf
  have hkh : k<h := by omega
  have hB' : (1:ℚ)≤B := by exact_mod_cast (show 1≤B by omega)
  have hhalf (j : ℕ) (hj : j<h) : 2*w (j+1)≤w j := by
    have he := hd j hj
    nlinarith only [he,mul_nonneg (sub_nonneg.mpr hB') (hw (j+1)).le,hw (j+1)]
  have hau := tail_series w (fun i => (hw i).le) (k+1) (h-k)
    (fun j hj => hhalf _ (by omega))
  have hbound :
      |∑ j ∈ Finset.range (h-k),f (k+1+j)|≤2*(B:ℚ)*w (k+1) := by
    calc
      _ ≤ ∑ j ∈ Finset.range (h-k),|f (k+1+j)| := Finset.abs_sum_le_sum_abs _ _
      _ ≤ ∑ j ∈ Finset.range (h-k),(B:ℚ)*w (k+1+j) := by
        apply Finset.sum_le_sum
        intro j hj
        have hc := hcoef (k+1+j) (by have := Finset.mem_range.mp hj; omega)
        dsimp only [f]
        rw [abs_mul,abs_of_nonneg (hw _).le]
        exact mul_le_mul_of_nonneg_right (by exact_mod_cast hc) (hw _).le
      _ ≤ (B:ℚ)*(2*w (k+1)) := by
        rw [←Finset.mul_sum]
        exact mul_le_mul_of_nonneg_left hau (by positivity)
      _ = _ := by ring
  have hlow := (abs_le.mp hbound).1
  have hstrict := hd k hkh
  linarith [hw k]

end Collatz.StripSign
