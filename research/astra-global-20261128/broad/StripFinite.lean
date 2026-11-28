import PadeValuations
import Mathlib.Algebra.BigOperators.Ring.Finset

/-! Finite convolution and dyadic precision for an auxiliary on translated event clocks. -/
set_option autoImplicit false
set_option warningAsError true

namespace Collatz.StripFinite
open Collatz.PadeValuations
open scoped BigOperators

def prefixSum (p : ℕ→ℚ) (j : ℕ) : ℚ := ∑ i∈Finset.range j,p i

def weightedHead (q : ℕ→ℤ) (w : ℕ→ℚ) (h : ℕ) : ℚ :=
  ∑ k∈Finset.range (h+1),(q k:ℚ)*w k

def weightedConstant (q : ℕ→ℤ) (w p : ℕ→ℚ) (h : ℕ) : ℚ :=
  ∑ k∈Finset.range (h+1),(q k:ℚ)*w k*prefixSum p (h-k+1)

theorem tail_split (p : ℕ→ℚ) (M h k : ℕ) (hh : h<M) (hk : k≤h) :
    prefixSum p M=prefixSum p (h-k+1)+
      (∑ r∈Finset.range (M-h-1),p (h+1+r-k))+
      ∑ j∈Finset.range k,p (M-k+j) := by
  have hright : (M-k)+k=M := by omega
  have hmid : (h-k+1)+(M-h-1)=M-k := by omega
  have hs := Finset.sum_range_add p (M-k) k
  rw [hright] at hs
  have ht := Finset.sum_range_add p (h-k+1) (M-h-1)
  rw [hmid] at ht
  unfold prefixSum
  rw [hs,ht]
  congr 1
  congr 1
  apply Finset.sum_congr rfl
  intro i hi
  congr 1
  omega

/-- The remaining terms use only the actual input, the selected weights and the last finite window. -/
theorem finite_certificate (q : ℕ→ℤ) (w p : ℕ→ℚ) (M h : ℕ) (hh : h<M) (y : ℚ)
    (hr : ∀ r<M-h-1,(∑ k∈Finset.range (h+1),(q k:ℚ)*w k*p (h+1+r-k))=0) :
    weightedHead q w h*y-weightedConstant q w p h =
      weightedHead q w h*(y-prefixSum p M)+
      ∑ k∈Finset.range (h+1),(q k:ℚ)*w k*(∑ j∈Finset.range k,p (M-k+j)) := by
  have hs : weightedHead q w h*prefixSum p M-weightedConstant q w p h=
      ∑ k∈Finset.range (h+1),(q k:ℚ)*w k*(∑ j∈Finset.range k,p (M-k+j)) := by
    calc
      _ = ∑ k∈Finset.range (h+1),(q k:ℚ)*w k*(prefixSum p M-prefixSum p (h-k+1)) := by
        simp only [weightedHead,weightedConstant,Finset.sum_mul,mul_sub,Finset.sum_sub_distrib]
      _ = ∑ k∈Finset.range (h+1),(q k:ℚ)*w k*
          ((∑ r∈Finset.range (M-h-1),p (h+1+r-k))+
            ∑ j∈Finset.range k,p (M-k+j)) := by
        apply Finset.sum_congr rfl
        intro k hk
        rw [tail_split p M h k hh (by have := Finset.mem_range.mp hk; omega)]
        ring
      _ = _ := by
        simp only [mul_add,Finset.sum_add_distrib,Finset.mul_sum]
        rw [Finset.sum_comm (s:=Finset.range (h+1)) (t:=Finset.range (M-h-1))]
        rw [Finset.sum_eq_zero (fun r hr' => hr r (Finset.mem_range.mp hr')),zero_add]
  rw [mul_sub]
  linarith

theorem atLeast_add {e : ℤ} {x y : ℚ} (hx : AtLeast e x) (hy : AtLeast e y) :
    AtLeast e (x+y) := by
  rcases hx with rfl|hx
  · simpa only [zero_add] using hy
  rcases hy with rfl|hy
  · rw [add_zero]; exact Or.inr hx
  by_cases hn : x+y=0
  · exact Or.inl hn
  · exact Or.inr ((le_min hx hy).trans (padicValRat.min_le_padicValRat_add hn))

theorem atLeast_sum (e : ℤ) (f : ℕ→ℚ) (L : ℕ)
    (hf : ∀ i<L,AtLeast e (f i)) : AtLeast e (∑ i∈Finset.range L,f i) := by
  induction L with
  | zero => exact Or.inl (by simp)
  | succ L ih =>
    rw [Finset.sum_range_succ]
    exact atLeast_add (ih (fun i hi => hf i (by omega))) (hf L (by omega))

theorem atLeast_mul {a b : ℤ} {x y : ℚ} (hx : AtLeast a x) (hy : AtLeast b y) :
    AtLeast (a+b) (x*y) := by
  by_cases h0 : x=0
  · exact Or.inl (by rw [h0,zero_mul])
  by_cases h1 : y=0
  · exact Or.inl (by rw [h1,mul_zero])
  right
  rw [padicValRat.mul h0 h1]
  exact add_le_add (hx.resolve_left h0) (hy.resolve_left h1)

theorem int_atLeast_zero (z : ℤ) : AtLeast 0 (z:ℚ) := by
  right
  rw [padicValRat.of_int]
  positivity

/-- Finite divisibility after exact middle-row cancellation. -/
theorem finite_precision (q : ℕ→ℤ) (w p : ℕ→ℚ) (M h : ℕ) (hh : h<M) (y : ℚ) (e : ℤ)
    (hr : ∀ r<M-h-1,(∑ k∈Finset.range (h+1),(q k:ℚ)*w k*p (h+1+r-k))=0)
    (htarget : ∀ k≤h,AtLeast e (w k*(y-prefixSum p M)))
    (htail : ∀ k≤h,∀ j<k,AtLeast e (w k*p (M-k+j))) :
    AtLeast e (weightedHead q w h*y-weightedConstant q w p h) := by
  rw [finite_certificate q w p M h hh y hr,weightedHead,Finset.sum_mul]
  apply atLeast_add
  · apply atLeast_sum
    intro k hk
    simpa only [add_zero,zero_add,mul_assoc] using
      atLeast_mul (int_atLeast_zero (q k)) (htarget k (by omega))
  · apply atLeast_sum
    intro k hk
    rw [Finset.mul_sum]
    apply atLeast_sum
    intro j hj
    simpa only [add_zero,zero_add,mul_assoc] using
      atLeast_mul (int_atLeast_zero (q k)) (htail k (by omega) j hj)

end Collatz.StripFinite
