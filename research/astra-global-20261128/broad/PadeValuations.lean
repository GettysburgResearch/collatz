import PadeIntegral
import Mathlib.NumberTheory.Padics.PadicVal.Basic

/-! Exact binary valuation of a finite Padé form from the native finite tail bounds. -/
set_option autoImplicit false
set_option warningAsError true

namespace Collatz.PadeValuations
open Collatz.PadeArithmetic Collatz.PadeIntegral Collatz.FinitePade
open scoped BigOperators

def Exact (e : ℤ) (x : ℚ) : Prop := x≠0 ∧ padicValRat 2 x=e

def Higher (e : ℤ) (x : ℚ) : Prop := x=0 ∨ e<padicValRat 2 x

def AtLeast (e : ℤ) (x : ℚ) : Prop := x=0 ∨ e≤padicValRat 2 x

def clockExponent (h b j : ℕ) : ℕ := j*(b+1)+h*tri j

def formExponent (h b n m : ℕ) : ℕ :=
  (2*n+m+1)*(b+1)+h*(n*(n+m)+tri (n+m+1))

theorem exact_mul {a b : ℤ} {x y : ℚ} (hx : Exact a x) (hy : Exact b y) :
    Exact (a+b) (x*y) := by
  exact ⟨mul_ne_zero hx.1 hy.1,by rw [padicValRat.mul hx.1 hy.1,hx.2,hy.2]⟩

theorem exact_add_higher {e : ℤ} {x y : ℚ} (hx : Exact e x) (hy : Higher e y) :
    Exact e (x+y) := by
  by_cases hy0 : y=0
  · simpa only [hy0,add_zero] using hx
  have hy := hy.resolve_left hy0
  have hn : x+y≠0 := by
    intro hxy
    have hz : y= -x := by linarith
    rw [hz,padicValRat.neg,hx.2] at hy
    omega
  exact ⟨hn,(padicValRat.add_eq_of_lt hn hx.1 hy0 (by simpa only [hx.2] using hy)).trans hx.2⟩

theorem higher_add {e : ℤ} {x y : ℚ} (hx : Higher e x) (hy : Higher e y) :
    Higher e (x+y) := by
  rcases hx with rfl | hx
  · simpa using hy
  rcases hy with rfl | hy
  · rw [add_zero]; exact Or.inr hx
  by_cases hn : x+y=0
  · exact Or.inl hn
  · exact Or.inr ((lt_min hx hy).trans_le (padicValRat.min_le_padicValRat_add hn))

theorem higher_sum (e : ℤ) (f : ℕ → ℚ) (n : ℕ)
    (h : ∀ k<n,Higher e (f k)) : Higher e (∑ k ∈ Finset.range n,f k) := by
  induction n with
  | zero => exact Or.inl (by simp)
  | succ n ih =>
    rw [Finset.sum_range_succ]
    exact higher_add (ih (fun k hk => h k (by omega))) (h n (by omega))

private theorem val_two : padicValRat 2 (2:ℚ)=1 := by
  exact padicValRat.self (by decide : 1<2)

private theorem odd_exact {a : ℤ} (ha : Odd a) : Exact 0 (a:ℚ) := by
  obtain ⟨k,hk⟩ := ha
  have hn : a≠0 := by omega
  have hd : ¬(2:ℤ) ∣ a := by intro ⟨j,hj⟩; omega
  refine ⟨by exact_mod_cast hn,?_⟩
  rw [padicValRat.of_int,padicValInt.eq_zero_of_not_dvd hd]
  rfl

private theorem val_three : padicValRat 2 (3:ℚ)=0 := (odd_exact (by decide : Odd (3:ℤ))).2

theorem qBase_pos (h : ℕ) : 0<qBase h := by dsimp [qBase]; positivity

theorem zBase_pos (b : ℕ) : 0<zBase b := by dsimp [zBase]; positivity

theorem qBase_val (h : ℕ) : padicValRat 2 (qBase h)= -(h:ℤ) := by
  rw [qBase,padicValRat.pow,padicValRat.div (by decide) (by decide),val_three,val_two]
  ring

theorem zBase_val (b : ℕ) : padicValRat 2 (zBase b)=b+1 := by
  rw [zBase,padicValRat.div (by positivity) (by positivity),padicValRat.pow,padicValRat.pow,val_three,val_two]
  push_cast
  ring

theorem scale_exact (h b n m : ℕ) :
    Exact (n*(b+1)+h*(n*(n+m)):ℕ) (scale h b n m:ℚ) := by
  simp only [scale,Int.cast_mul,Int.cast_pow,Int.cast_ofNat]
  refine ⟨by positivity,?_⟩
  rw [padicValRat.mul (by positivity) (by positivity),padicValRat.pow,padicValRat.pow,val_two,val_three]
  ring

theorem term_exact (h b j : ℕ) :
    Exact (clockExponent h b j) (term (qBase h) (zBase b) j) := by
  have hq := qBase_pos h
  have hz := zBase_pos b
  unfold term
  refine ⟨by positivity,?_⟩
  rw [padicValRat.div (by positivity) (by positivity),padicValRat.pow,padicValRat.pow,
    qBase_val,zBase_val,clockExponent]
  push_cast
  ring

theorem leading_poly_exact (h n t : ℕ) (hh : 0<h) (ht : n<t) :
    Exact 0 ((padePoly n (qBase h)).eval (((qBase h)^t)⁻¹)) := by
  have hq := (qBase_pos h).ne'
  induction n with
  | zero =>
    simp only [padePoly_zero,Polynomial.eval_one]
    exact ⟨one_ne_zero,padicValRat.one⟩
  | succ n ih =>
    rw [padePoly_succ,Polynomial.eval_mul,Polynomial.eval_sub,Polynomial.eval_one,
      Polynomial.eval_mul,Polynomial.eval_C,Polynomial.eval_X]
    have hval : 0<padicValRat 2 (-((qBase h)^(n+1)*((qBase h)^t)⁻¹)) := by
      rw [padicValRat.neg,padicValRat.mul (pow_ne_zero _ hq) (inv_ne_zero (pow_ne_zero _ hq)),
        padicValRat.inv,padicValRat.pow,padicValRat.pow,qBase_val]
      push_cast
      have ha : (n:ℤ)+1<t := by exact_mod_cast ht
      have hb : 0<(h:ℤ) := by exact_mod_cast hh
      nlinarith [mul_pos (sub_pos.mpr ha) hb]
    have hf := exact_add_higher (e:=0) (x:=1) ⟨one_ne_zero,padicValRat.one⟩ (Or.inr hval)
    simpa only [sub_eq_add_neg,zero_add] using exact_mul (ih (by omega)) hf

theorem leading_exact (h b n m : ℕ) (hh : 0<h) :
    Exact (formExponent h b n m)
      ((scale h b n m:ℚ)*leading n m (qBase h) (zBase b)) := by
  have hu := leading_poly_exact h n (n+1) hh (by omega)
  have hs := exact_mul (scale_exact h b n m) (exact_mul (term_exact h b (n+m+1)) hu)
  have he : ((n*(b+1)+h*(n*(n+m)):ℕ):ℤ)+(clockExponent h b (n+m+1):ℤ)+0 =
      (formExponent h b n m:ℤ) := by
    unfold formExponent clockExponent
    push_cast
    ring
  simpa only [leading,←add_assoc,he] using hs

theorem weight_exact (h b n m k : ℕ) (hh : 0<h) (hk : k≤n) :
    Exact ((n-k)*(b+1+h*(n+m)):ℕ) (integralTerm h b n m k 0:ℚ) := by
  rw [weight_factor,Int.cast_mul,Int.cast_pow,Int.cast_ofNat]
  have ha := odd_exact (weight_odd_factor h b n m k hh hk)
  let e := (n-k)*(b+1+h*(n+m))
  have ht : Exact (e:ℤ) ((2:ℚ)^e) := by
    exact ⟨by positivity,by rw [padicValRat.pow,val_two,mul_one]⟩
  simpa only [add_zero] using exact_mul ht ha

theorem tail_exponent_gap (h b n m k : ℕ) (hk : k≤n) :
    (n-k)*(b+1+h*(n+m))+clockExponent h b (n+m+k+2) =
      formExponent h b n m+(b+1)+h*(n+m+1+k+tri (k+1)) := by
  have hs := Nat.sub_add_cancel hk
  rw [clockExponent,formExponent,show n+m+k+2=(n+m+1)+(k+1) by omega,tri_add]
  calc
    _ = (n-k+k)*(b+1+h*(n+m))+
      (n+m+1)*(b+1)+(b+1)+h*(tri (n+m+1)+tri (k+1)+(n+m+1)+k) := by ring
    _ = _ := by rw [hs]; ring

theorem weighted_tail_higher (h b n m k : ℕ) (hh : 0<h) (hk : k≤n) (tail : ℚ)
    (ht : AtLeast (clockExponent h b (n+m+k+2)) tail) :
    Higher (formExponent h b n m) ((integralTerm h b n m k 0:ℚ)*tail) := by
  by_cases hz : tail=0
  · exact Or.inl (by rw [hz,mul_zero])
  have hv := ht.resolve_left hz
  have hw := weight_exact h b n m k hh hk
  have hg := tail_exponent_gap h b n m k hk
  have hlt : formExponent h b n m<(n-k)*(b+1+h*(n+m))+clockExponent h b (n+m+k+2) := by omega
  have hi : (formExponent h b n m:ℤ)<
      (((n-k)*(b+1+h*(n+m)):ℕ):ℤ)+(clockExponent h b (n+m+k+2):ℤ) := by exact_mod_cast hlt
  right
  rw [padicValRat.mul hw.1 hz,hw.2]
  omega

/-- Any rational target with the physical finite tails has this exact valuation. -/
theorem finite_form_exact (h b n m : ℕ) (hh : 0<h) (y : ℚ)
    (ht : ∀ k≤n,AtLeast (clockExponent h b (n+m+k+2))
      (y-partialSum (qBase h) (zBase b) (n+m+k+2))) :
    Exact (formExponent h b n m) ((integralHead h b n m:ℚ)*y-(integralConstant h b n m:ℚ)) := by
  have hi := scaled_finite_identity n m (qBase h) (zBase b) y (scale h b n m)
    (qBase_pos h).ne' (zBase_pos b).ne'
  rw [scale_head,scale_constant] at hi
  rw [hi]
  apply exact_add_higher (leading_exact h b n m hh)
  apply higher_sum
  intro k hk
  rw [scale_raw h b n m k (by omega)]
  exact weighted_tail_higher h b n m k hh (by omega) _ (ht k (by omega))

theorem integer_form_lower (h b n m : ℕ) (hh : 0<h) (y : ℤ)
    (ht : ∀ k≤n,AtLeast (clockExponent h b (n+m+k+2))
      ((y:ℚ)-partialSum (qBase h) (zBase b) (n+m+k+2))) :
    (2:ℤ)^(formExponent h b n m) ≤ |integralHead h b n m*y-integralConstant h b n m| := by
  let F := integralHead h b n m*y-integralConstant h b n m
  have he : Exact (formExponent h b n m) (F:ℚ) := by
    simpa only [F,Int.cast_sub,Int.cast_mul] using finite_form_exact h b n m hh y ht
  have hn : F≠0 := by exact_mod_cast he.1
  have hv := he.2
  rw [padicValRat.of_int] at hv
  have hv' : padicValInt 2 F=formExponent h b n m := by exact_mod_cast hv
  have hd := padicValInt_dvd (p:=2) F
  rw [hv'] at hd
  have hl := Int.natAbs_le_of_dvd_ne_zero hd hn
  change _≤|F|
  simpa only [Int.natCast_natAbs,abs_of_nonneg (by positivity : 0≤(2:ℤ)^formExponent h b n m)]
    using (show ((Int.natAbs ((2:ℤ)^formExponent h b n m):ℕ):ℤ)≤(F.natAbs:ℤ) by exact_mod_cast hl)

end Collatz.PadeValuations
