import StripFinite
import StripSign
import PadeObserved

/-! A finite signed auxiliary on actual shortcut clocks, with no abstract tail hypotheses. -/
set_option autoImplicit false
set_option warningAsError true

namespace Collatz.StripObserved
open CoreBranching PinClock PinCriterion
open Collatz.PadeNative Collatz.PadeObserved Collatz.PadeValuations Collatz.StripFinite
open scoped BigOperators

def weight (k v : ℕ) : ℚ := (2:ℚ)^(k+v)/3^v

def nativeForm (x h : ℕ) (q : ℕ→ℤ) (v : ℕ→ℕ) : ℚ :=
  weightedHead q (fun k => weight k (v k)) h*(-((x:ℚ)+1))-
    weightedConstant q (fun k => weight k (v k)) (fun j => amplitude j x) h

private theorem weight_pos (k v : ℕ) : 0<weight k v := by unfold weight; positivity

private theorem weight_exact (k v : ℕ) : Exact (k+v:ℕ) (weight k v) := by
  refine ⟨(weight_pos k v).ne',?_⟩
  have h2 : padicValRat 2 (2:ℚ)=1 := padicValRat.self (by decide)
  have h3 : padicValRat 2 (3:ℚ)=0 := by
    rw [show (3:ℚ)=((3:ℕ):ℚ) by rfl,padicValRat.of_nat,
      padicValNat.eq_zero_of_not_dvd (by decide : ¬2∣3)]
    rfl
  rw [weight,padicValRat.div (by positivity) (by positivity),padicValRat.pow,padicValRat.pow,h2,h3]
  ring

private theorem native_tail (e x : ℕ) : AtLeast (clock e x)
    (-((x:ℚ)+1)-prefixSum (fun j => amplitude j x) e) := by
  have he := native_calibration e x
  have h : -((x:ℚ)+1)-prefixSum (fun j => amplitude j x) e =
      -(amplitude e x*((run (clock e x) x:ℚ)+1)) := by
    change -((x:ℚ)+1)-nativeSum e x= _
    linarith
  rw [h]
  have hv := amplitude_exact e x
  have hi : AtLeast 0 ((run (clock e x) x:ℚ)+1) := by
    simpa only [Int.cast_add,Int.cast_natCast,Int.cast_one] using
      int_atLeast_zero ((run (clock e x) x:ℤ)+1)
  have hp := atLeast_mul (Or.inr (le_of_eq hv.2.symm) : AtLeast (clock e x) (amplitude e x)) hi
  rcases hp with hp|hp
  · exact Or.inl (by rw [hp,neg_zero])
  · exact Or.inr (by rw [padicValRat.neg]; simpa only [add_zero] using hp)

/-- Exact row cancellation and explicit clock exponents suffice for finite dyadic precision. -/
theorem actual_precision (x M h e : ℕ) (q : ℕ→ℤ) (v : ℕ→ℕ) (hh : h<M)
    (hr : ∀ r<M-h-1,(∑ k∈Finset.range (h+1),(q k:ℚ)*weight k (v k)*amplitude (h+1+r-k) x)=0)
    (hstart : ∀ k≤h,e≤k+v k+clock M x)
    (htail : ∀ k≤h,∀ j<k,e≤k+v k+clock (M-k+j) x) :
    AtLeast e (nativeForm x h q v) := by
  apply finite_precision q (fun k => weight k (v k)) (fun j => amplitude j x) M h hh _ e hr
  · intro k hk
    have hw := weight_exact k (v k)
    have hw' : AtLeast (k+v k:ℕ) (weight k (v k)) := Or.inr (le_of_eq hw.2.symm)
    rcases atLeast_mul hw' (native_tail M x) with h0|hv
    · exact Or.inl h0
    · right
      exact (by exact_mod_cast hstart k hk : (e:ℤ)≤(k+v k:ℕ)+(clock M x:ℤ)).trans hv
  · intro k hk j hj
    have hw := exact_mul (weight_exact k (v k)) (amplitude_exact (M-k+j) x)
    right
    rw [hw.2]
    exact_mod_cast htail k hk j hj

private theorem prefix_mono (x a b : ℕ) (hab : a≤b) :
    prefixSum (fun j => amplitude j x) a≤prefixSum (fun j => amplitude j x) b := by
  obtain ⟨c,rfl⟩ := Nat.exists_eq_add_of_le hab
  unfold prefixSum
  rw [Finset.sum_range_add]
  exact le_add_of_nonneg_right (Finset.sum_nonneg (fun j _ => by unfold amplitude; positivity))

/-- Real nonvanishing uses the first active column, its sign and observed positive partial sums. -/
theorem actual_form_neg (x h k B : ℕ) (q : ℕ→ℤ) (v : ℕ→ℕ)
    (hB : 0<B) (hk : k≤h) (hzero : ∀ j<k,q j=0) (hfirst : 0<q k)
    (hcoef : ∀ j≤h,|q j|≤(B:ℤ))
    (hd : ∀ j<h,4*(B:ℚ)*weight (j+1) (v (j+1))≤weight j (v j)) :
    nativeForm x h q v<0 := by
  let a (j : ℕ) : ℚ := (x:ℚ)+1+prefixSum (fun t => amplitude t x) (h-j+1)
  have ha (j : ℕ) : 0<a j := by
    have hs := prefix_mono x 0 (h-j+1) (Nat.zero_le _)
    simp only [prefixSum,Finset.range_zero,Finset.sum_empty] at hs
    dsimp [a,prefixSum]
    linarith [show 0≤(x:ℚ) by positivity]
  have hle (j : ℕ) : a (j+1)≤a j := by
    dsimp only [a]
    linarith only [prefix_mono x (h-(j+1)+1) (h-j+1) (by omega)]
  have hp := Collatz.StripSign.eval_pos q (fun j => weight j (v j)*a j) B h k hB hk hzero hfirst hcoef
    (fun j => mul_pos (weight_pos _ _) (ha j)) (fun j hj => by
      rw [←mul_assoc]
      exact mul_le_mul (hd j hj) (hle j) (ha _).le (weight_pos _ _).le)
  have he : nativeForm x h q v= -(∑ j∈Finset.range (h+1),(q j:ℚ)*(weight j (v j)*a j)) := by
    simp only [nativeForm,weightedHead,weightedConstant,Finset.sum_mul,←Finset.sum_sub_distrib,
      ←Finset.sum_neg_distrib]
    apply Finset.sum_congr rfl
    intro j _
    dsimp [a]
    ring
  rw [he]
  linarith

end Collatz.StripObserved
