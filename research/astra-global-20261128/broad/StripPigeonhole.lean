import Mathlib.Data.Fintype.Pigeonhole
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Data.Fintype.Card
import Mathlib.Data.Fintype.BigOperators
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-! Finite scalar interpolation by explicit integer-box counting. -/
set_option autoImplicit false
set_option warningAsError true

namespace Collatz.StripPigeonhole
open scoped BigOperators

def colCount (s : ℕ) : ℕ := 4*s+1
def equations (s : ℕ) : ℕ := 3*s-1
def coefficientBound (s H : ℕ) : ℕ := (2*colCount s*H)^3

private theorem box_count (s H : ℕ) (hs : 0<s) (hH : 0<H) :
    (colCount s*H*coefficientBound s H+1)^(equations s)<
      (coefficientBound s H+1)^(colCount s) := by
  let m := colCount s
  let r := equations s
  let K := 2*m*H
  let B := K^3
  have hm : 0<m := by dsimp [m,colCount]; omega
  have hK : 1<K := by dsimp [K]; nlinarith [Nat.mul_pos hm hH]
  have hB : 0<B := by dsimp [B]; positivity
  have hr : 0<r := by dsimp [r,equations]; omega
  have hcount : r<3*(m-r) := by dsimp [r,m,colCount,equations]; omega
  have hmr : r≤m := by dsimp [r,m,colCount,equations]; omega
  have hdiff : K^r<B^(m-r) := by
    dsimp only [B]
    rw [←pow_mul]
    exact pow_lt_pow_right₀ hK hcount
  have hprod : m*H*B+1≤K*B := by dsimp [K]; nlinarith [Nat.mul_pos (Nat.mul_pos hm hH) hB]
  change (m*H*B+1)^r<(B+1)^m
  calc
    _ ≤ (K*B)^r := Nat.pow_le_pow_left hprod r
    _ = K^r*B^r := mul_pow _ _ _
    _ < B^(m-r)*B^r := Nat.mul_lt_mul_of_pos_right hdiff (by positivity)
    _ = B^m := by rw [←pow_add,Nat.sub_add_cancel hmr]
    _ ≤ _ := Nat.pow_le_pow_left (by omega) m

/-- The normalized convolution matrix has a bounded nonzero integer kernel vector. -/
theorem small_kernel (s H : ℕ) (hs : 0<s) (hH : 0<H)
    (A : Fin (equations s) → Fin (colCount s) → ℕ) (hA : ∀ i j,A i j≤H) :
    ∃ q : Fin (colCount s) → ℤ,
      (∃ k,q k≠0) ∧ (∀ k,|q k|≤(coefficientBound s H:ℤ)) ∧
      ∀ i, (∑ j,(A i j:ℤ)*q j)=0 := by
  classical
  let m := colCount s
  let r := equations s
  let B := coefficientBound s H
  let image (x : Fin m → Fin (B+1)) (i : Fin r) : Fin (m*H*B+1) :=
    ⟨∑ j,A i j*(x j).val,by
      have h := Finset.sum_le_sum (s:=Finset.univ) (f:=fun j : Fin m => A i j*(x j).val)
          (g:=fun _ => H*B) (fun j _ => Nat.mul_le_mul (hA i j) (by have := (x j).isLt; omega))
      simp only [Finset.sum_const,Finset.card_univ,Fintype.card_fin,nsmul_eq_mul] at h
      rw [←Nat.mul_assoc] at h
      exact Nat.lt_succ_of_le h⟩
  have hcard : Fintype.card (Fin r → Fin (m*H*B+1))<Fintype.card (Fin m → Fin (B+1)) := by
    simpa only [Fintype.card_pi_const,Fintype.card_fin] using box_count s H hs hH
  obtain ⟨x,y,hne,he⟩ := Fintype.exists_ne_map_eq_of_card_lt image hcard
  let q (k : Fin m) : ℤ := (x k).val-(y k).val
  refine ⟨q,?_,?_,?_⟩
  · by_contra! h
    apply hne
    funext k
    apply Fin.ext
    have hk := h k
    dsimp only [q] at hk
    omega
  · intro k
    have hx := (x k).isLt
    have hy := (y k).isLt
    dsimp only [q]
    rw [abs_le]
    omega
  · intro i
    have hz := congrArg Fin.val (congrFun he i)
    change (∑ j,A i j*(x j).val)=(∑ j,A i j*(y j).val) at hz
    have hi : (∑ j,(A i j:ℤ)*(x j).val)=(∑ j,(A i j:ℤ)*(y j).val) := by
      have hi := congrArg (fun z : ℕ => (z:ℤ)) hz
      simpa only [Nat.cast_sum,Nat.cast_mul] using hi
    simp only [q,mul_sub,Finset.sum_sub_distrib,hi,sub_self]

end Collatz.StripPigeonhole
