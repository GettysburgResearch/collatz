import StripObserved

/-! Clear all ternary denominators and compare the resulting nonzero integer with its binary divisor. -/
set_option autoImplicit false
set_option warningAsError true

namespace Collatz.StripInteger
open CoreBranching PinClock PinCriterion
open Collatz.PadeNative Collatz.PadeValuations Collatz.StripFinite Collatz.StripObserved
open scoped BigOperators

private def Integral (z : ℚ) : Prop := ∃ a : ℤ,(a:ℚ)=z

private theorem integral_sum (f : ℕ→ℚ) (n : ℕ) (hf : ∀ j<n,Integral (f j)) :
    Integral (∑ j∈Finset.range n,f j) := by
  induction n with
  | zero => exact ⟨0,by simp⟩
  | succ n ih =>
    obtain ⟨a,ha⟩ := ih (fun j hj => hf j (by omega))
    obtain ⟨b,hb⟩ := hf n (by omega)
    exact ⟨a+b,by rw [Int.cast_add,ha,hb,Finset.sum_range_succ]⟩

private theorem integral_unit (A t u : ℕ) (hu : u≤A) :
    Integral ((3:ℚ)^A*(2^t/3^u)) := by
  refine ⟨2^t*3^(A-u),?_⟩
  simp only [Int.cast_mul,Int.cast_pow,Int.cast_ofNat]
  rw [show A=(A-u)+u by omega] at ⊢
  rw [Nat.add_sub_cancel,pow_add]
  field_simp

/-- Explicit denominator test for every term in the native auxiliary. -/
theorem native_cleared (x h A : ℕ) (q : ℕ→ℤ) (v : ℕ→ℕ)
    (hA : ∀ k≤h,∀ j≤h-k,v k+(clock j x-j)≤A) :
    ∃ z : ℤ,(z:ℚ)=3^A*nativeForm x h q v := by
  have hhead : Integral ((3:ℚ)^A*weightedHead q (fun k => weight k (v k)) h) := by
    rw [weightedHead,Finset.mul_sum]
    apply integral_sum
    intro k hk
    have hkv := hA k (by omega) 0 (by omega)
    obtain ⟨z,hz⟩ := integral_unit A (k+v k) (v k) (by omega)
    exact ⟨q k*z,by rw [Int.cast_mul,hz,weight]; ring⟩
  have hconst : Integral ((3:ℚ)^A*weightedConstant q (fun k => weight k (v k))
      (fun j => amplitude j x) h) := by
    rw [weightedConstant,Finset.mul_sum]
    apply integral_sum
    intro k hk
    rw [prefixSum,←mul_assoc,Finset.mul_sum]
    apply integral_sum
    intro j hj
    obtain ⟨z,hz⟩ := integral_unit A (k+v k+clock j x) (v k+(clock j x-j))
      (hA k (by omega) j (by omega))
    refine ⟨q k*z,?_⟩
    rw [Int.cast_mul,hz,weight,amplitude,pow_add,pow_add]
    ring
  obtain ⟨r,hr⟩ := hhead
  obtain ⟨c,hc⟩ := hconst
  exact ⟨r*(-((x:ℤ)+1))-c,by rw [Int.cast_sub,Int.cast_mul,Int.cast_neg,Int.cast_add,
    Int.cast_natCast,Int.cast_one,hr,hc,nativeForm]; ring⟩

private theorem integral_lower (F : ℤ) (e : ℕ) (hn : F≠0) (hv : AtLeast e (F:ℚ)) :
    (2:ℤ)^e≤|F| := by
  have h := hv.resolve_left (by exact_mod_cast hn)
  rw [padicValRat.of_int] at h
  have h' : e≤padicValInt 2 F := by exact_mod_cast h
  have hd := padicValInt_dvd (p:=2) F
  have hdiv : (2:ℤ)^e∣F := (pow_dvd_pow _ h').trans hd
  have hl := Int.natAbs_le_of_dvd_ne_zero hdiv hn
  simpa only [Int.natCast_natAbs,abs_of_nonneg (by positivity : 0≤(2:ℤ)^e)]
    using (show ((Int.natAbs ((2:ℤ)^e):ℕ):ℤ)≤(F.natAbs:ℤ) by exact_mod_cast hl)

/-- A nonzero integral form and its source-size lower bound, on the actual integer orbit. -/
theorem actual_integer_barrier (x M h e A B k : ℕ) (q : ℕ→ℤ) (v : ℕ→ℕ) (hh : h<M)
    (hr : ∀ r<M-h-1,(∑ j∈Finset.range (h+1),(q j:ℚ)*weight j (v j)*amplitude (h+1+r-j) x)=0)
    (hstart : ∀ j≤h,e≤j+v j+clock M x)
    (htail : ∀ i≤h,∀ j<i,e≤i+v i+clock (M-i+j) x)
    (hA : ∀ i≤h,∀ j≤h-i,v i+(clock j x-j)≤A)
    (hB : 0<B) (hk : k≤h) (hzero : ∀ j<k,q j=0) (hfirst : 0<q k)
    (hcoef : ∀ j≤h,|q j|≤(B:ℤ))
    (hd : ∀ j<h,4*(B:ℚ)*weight (j+1) (v (j+1))≤weight j (v j)) :
    ∃ F : ℤ,(F:ℚ)=3^A*nativeForm x h q v ∧ F<0 ∧ (2:ℤ)^e≤|F| := by
  obtain ⟨F,hF⟩ := native_cleared x h A q v hA
  have hn := actual_form_neg x h k B q v hB hk hzero hfirst hcoef hd
  have hneg : (F:ℚ)<0 := by rw [hF]; exact mul_neg_of_pos_of_neg (by positivity) hn
  have hp := actual_precision x M h e q v hh hr hstart htail
  have hs : AtLeast 0 ((3:ℚ)^A) := by
    simpa only [Int.cast_pow,Int.cast_ofNat] using int_atLeast_zero ((3:ℤ)^A)
  have hv : AtLeast e (F:ℚ) := by
    rw [hF]
    simpa only [zero_add] using atLeast_mul hs hp
  have hn' : F<0 := by exact_mod_cast hneg
  exact ⟨F,hF,hn',integral_lower F e (ne_of_lt hn') hv⟩

end Collatz.StripInteger
