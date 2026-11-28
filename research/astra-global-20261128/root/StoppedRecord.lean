import CofactorDescent
import PinClock

/-! Counted mergers preserve the actual first-stop record after explicit height clearance.
The analytic frequency of mergers is not an assumption of any declaration here.
The final estimate concerns the native unshifted survival mark, not the shifted cofactor mark.
-/
set_option autoImplicit false
set_option warningAsError true

namespace Collatz.StoppedRecord
open CoreBranching PinClock
open Collatz.CofactorDescent (odds)

def CountedMerge (t x y : ℕ) : Prop :=
  run t x=run t y ∧ odds t x=odds t y

def FirstAt (A : ℕ→Prop) (x s : ℕ) : Prop :=
  A (run s x) ∧ ∀ j<s,¬A (run j x)

def nativeMark (s x : ℕ) : ℚ :=
  (3:ℚ)^(odds s x)*(x:ℚ)/((2:ℚ)^s*(run s x:ℚ))

def nativeWeight (x : ℕ) : ℚ :=
  if x%2=0 then 1 else (3*(x:ℚ))/(3*(x:ℚ)+1)

def productMark : ℕ→ℕ→ℚ
  | 0,_ => 1
  | s+1,x => nativeWeight x*productMark s (step x)

theorem odds_add (a b x : ℕ) : odds (a+b) x=odds a x+odds b (run a x) := by
  induction a generalizing x with
  | zero => simp only [zero_add,odds,run]
  | succ a ih =>
    simp only [Nat.succ_add,odds,run,ih]
    omega

theorem merged_state (t s x y : ℕ) (hm : CountedMerge t x y) (hs : t≤s) :
    run s x=run s y := by
  obtain ⟨r,rfl⟩ := Nat.exists_eq_add_of_le hs
  rw [run_add,run_add,hm.1]

theorem merged_counts (t s x y : ℕ) (hm : CountedMerge t x y) (hs : t≤s) :
    odds s x=odds s y := by
  obtain ⟨r,rfl⟩ := Nat.exists_eq_add_of_le hs
  rw [odds_add,odds_add,hm.1,hm.2]

theorem source_le_dyadic_state (s x : ℕ) : x≤2^s*run s x := by
  induction s generalizing x with
  | zero => simp only [pow_zero,one_mul,run,le_refl]
  | succ s ih =>
    have he : x≤2*step x := by unfold step; split <;> omega
    calc
      x≤2*step x := he
      _≤2*(2^s*run s (step x)) := Nat.mul_le_mul_left 2 (ih (step x))
      _=2^(s+1)*run (s+1) x := by rw [run,pow_succ];ring

theorem run_pos (s x : ℕ) (hx : 0<x) : 0<run s x := by
  have h := source_le_dyadic_state s x
  by_contra hn
  have hz : run s x=0 := by omega
  rw [hz,mul_zero] at h
  omega

private theorem native_weight_calibration (x : ℕ) :
    nativeWeight x*(2*(step x:ℚ))=(3:ℚ)^(x%2)*(x:ℚ) := by
  by_cases hx : x%2=0
  · have hs : 2*step x=x := by simp only [step,hx,ite_true];omega
    simp only [nativeWeight,hx,ite_true,pow_zero,one_mul]
    exact_mod_cast hs
  · have ho : x%2=1 := by omega
    have hs : 2*step x=3*x+1 := by simp only [step,hx,ite_false];omega
    have hs' : 2*(step x:ℚ)=3*(x:ℚ)+1 := by exact_mod_cast hs
    simp only [nativeWeight,ho,pow_one,hs']
    exact div_mul_cancel₀ _ (by positivity)

/-- The fraction is the actual product of odd-step corrections; even edges have weight one. -/
theorem product_mark_calibration (s x : ℕ) :
    productMark s x*(2:ℚ)^s*(run s x:ℚ)=(3:ℚ)^(odds s x)*(x:ℚ) := by
  induction s generalizing x with
  | zero => simp only [productMark,pow_zero,one_mul,run,odds]
  | succ s ih =>
    calc
      _=(2*nativeWeight x)*(productMark s (step x)*(2:ℚ)^s*(run s (step x):ℚ)) := by
        simp only [productMark,run,pow_succ]
        ring
      _=(2*nativeWeight x)*((3:ℚ)^(odds s (step x))*(step x:ℚ)) := by rw [ih]
      _=(3:ℚ)^(odds s (step x))*(nativeWeight x*(2*(step x:ℚ))) := by ring
      _=(3:ℚ)^(odds s (step x))*((3:ℚ)^(x%2)*(x:ℚ)) := by rw [native_weight_calibration]
      _=_ := by rw [odds,pow_add];ring

theorem native_mark_eq_product (s x : ℕ) (hx : 0<x) : nativeMark s x=productMark s x := by
  have hr : (0:ℚ)<run s x := by exact_mod_cast run_pos s x hx
  unfold nativeMark
  apply (div_eq_iff (by positivity : (2:ℚ)^s*(run s x:ℚ)≠0)).mpr
  have hc := product_mark_calibration s x
  nlinarith only [hc]

/-- Every physical input up to the stated date stays above the stopping set. -/
theorem height_clearance (B t x j : ℕ) (hx : 2^t*B<x) (hj : j≤t) :
    B<run j x := by
  by_contra hn
  have hjx : run j x≤B := by omega
  have hpow : 2^j≤2^t := Nat.pow_le_pow_right (by decide) hj
  have h := (source_le_dyadic_state j x).trans
    ((Nat.mul_le_mul_left (2^j) hjx).trans (Nat.mul_le_mul_right B hpow))
  omega

theorem target_at_iff (A : ℕ→Prop) (B t x y s : ℕ)
    (hA : ∀ z,A z→z≤B) (hx : 2^t*B<x) (hy : 2^t*B<y)
    (hm : CountedMerge t x y) : A (run s x)↔A (run s y) := by
  by_cases hs : t≤s
  · rw [merged_state t s x y hm hs]
  · have hs' : s≤t := by omega
    have hxc := height_clearance B t x s hx hs'
    have hyc := height_clearance B t y s hy hs'
    constructor
    · intro h; exact False.elim (by have := hA _ h;omega)
    · intro h; exact False.elim (by have := hA _ h;omega)

/-- Misses and every exact first-hit date agree, without assuming that either path stops. -/
theorem first_at_iff (A : ℕ→Prop) (B t x y s : ℕ)
    (hA : ∀ z,A z→z≤B) (hx : 2^t*B<x) (hy : 2^t*B<y)
    (hm : CountedMerge t x y) : FirstAt A x s↔FirstAt A y s := by
  have he := target_at_iff A B t x y
  constructor
  · rintro ⟨ha,hpre⟩
    refine ⟨(he s hA hx hy hm).mp ha,?_⟩
    intro j hj hjA
    exact hpre j hj ((he j hA hx hy hm).mpr hjA)
  · rintro ⟨ha,hpre⟩
    refine ⟨(he s hA hx hy hm).mpr ha,?_⟩
    intro j hj hjA
    exact hpre j hj ((he j hA hx hy hm).mp hjA)

theorem never_hits_iff (A : ℕ→Prop) (B t x y : ℕ)
    (hA : ∀ z,A z→z≤B) (hx : 2^t*B<x) (hy : 2^t*B<y)
    (hm : CountedMerge t x y) :
    (∀ s,¬A (run s x))↔(∀ s,¬A (run s y)) := by
  constructor
  · intro h s hs
    exact h s ((target_at_iff A B t x y s hA hx hy hm).mpr hs)
  · intro h s hs
    exact h s ((target_at_iff A B t x y s hA hx hy hm).mp hs)

/-- The actual first date, odd count, landing and final word are all preserved together. -/
theorem full_first_record (A : ℕ→Prop) (B t ell x y s : ℕ)
    (hA : ∀ z,A z→z≤B) (hx : 2^(t+ell)*B<x) (hy : 2^(t+ell)*B<y)
    (hm : CountedMerge t x y) (hf : FirstAt A x s) :
    FirstAt A y s ∧ odds s x=odds s y ∧ run s x=run s y ∧
      parityPrefix ell (run (s-ell) x)=parityPrefix ell (run (s-ell) y) := by
  have hpow : 2^t≤2^(t+ell) := Nat.pow_le_pow_right (by decide) (by omega)
  have hx' : 2^t*B<x := (Nat.mul_le_mul_right B hpow).trans_lt hx
  have hy' : 2^t*B<y := (Nat.mul_le_mul_right B hpow).trans_lt hy
  have hs : t+ell<s := by
    by_contra hn
    have hc := height_clearance B (t+ell) x s hx (by omega)
    have ha := hA _ hf.1
    omega
  refine ⟨(first_at_iff A B t x y s hA hx' hy' hm).mp hf,
    merged_counts t s x y hm (by omega),merged_state t s x y hm (by omega),?_⟩
  rw [merged_state t (s-ell) x y hm (by omega)]

private theorem multiplier_source_le (s x : ℕ) :
    3^(odds s x)*x≤2^s*run s x := by
  induction s generalizing x with
  | zero => simp only [odds,pow_zero,one_mul,run,le_refl]
  | succ s ih =>
    have he : 3^(x%2)*x≤2*step x := by
      have hm : x%2<2 := Nat.mod_lt x (by decide)
      interval_cases h : x%2
      · simp only [h,pow_zero,one_mul,step,ite_true];omega
      · simp only [h,pow_one,step];split <;> omega
    calc
      _=3^(odds s (step x))*(3^(x%2)*x) := by rw [odds,pow_add];ring
      _≤3^(odds s (step x))*(2*step x) := Nat.mul_le_mul_left _ he
      _=2*(3^(odds s (step x))*step x) := by ring
      _≤2*(2^s*run s (step x)) := Nat.mul_le_mul_left 2 (ih _)
      _=2^(s+1)*run (s+1) x := by rw [run,pow_succ];ring

theorem native_mark_bounds (s x : ℕ) (hx : 0<x) :
    0<nativeMark s x ∧ nativeMark s x≤1 := by
  have hr : (0:ℚ)<run s x := by exact_mod_cast run_pos s x hx
  have hn : (0:ℚ)<x := by exact_mod_cast hx
  have hd : (0:ℚ)<2^s*(run s x:ℚ) := by positivity
  have hmul : (3:ℚ)^(odds s x)*(x:ℚ)≤(2:ℚ)^s*(run s x:ℚ) := by
    exact_mod_cast multiplier_source_le s x
  constructor
  · unfold nativeMark;positivity
  · exact (div_le_one hd).mpr hmul

/-- A merged native mark has exactly the original-source ratio. -/
theorem native_mark_source_ratio (t s x y : ℕ) (hm : CountedMerge t x y) (hs : t≤s) :
    nativeMark s y*(x:ℚ)=nativeMark s x*(y:ℚ) := by
  unfold nativeMark
  rw [merged_counts t s x y hm hs,merged_state t s x y hm hs]
  ring

/-- Quantitative continuity for bounded-Lipschitz mark tests at the true physical sources. -/
theorem native_mark_shift_bound (t s x d : ℕ) (hx : 0<x)
    (hm : CountedMerge t x (x+d)) (hs : t≤s) :
    0≤nativeMark s (x+d)-nativeMark s x ∧
      nativeMark s (x+d)-nativeMark s x≤(d:ℚ)/(x+d:ℕ) := by
  have hn : (0:ℚ)<(x+d:ℕ) := by exact_mod_cast (show 0<x+d by omega)
  have hb := native_mark_bounds s (x+d) (by omega)
  have hr := native_mark_source_ratio t s x (x+d) hm hs
  have he : nativeMark s (x+d)-nativeMark s x=
      (d:ℚ)/(x+d:ℕ)*nativeMark s (x+d) := by
    rw [div_mul_eq_mul_div]
    apply (eq_div_iff hn.ne').mpr
    push_cast at hr ⊢
    nlinarith
  rw [he]
  have hq : (0:ℚ)≤(d:ℚ)/(x+d:ℕ) := by positivity
  exact ⟨mul_nonneg hq hb.1.le,by simpa only [mul_one] using mul_le_mul_of_nonneg_left hb.2 hq⟩

end Collatz.StoppedRecord
