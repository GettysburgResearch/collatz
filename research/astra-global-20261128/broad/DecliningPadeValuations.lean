import DecliningPadeIntegral
import PadeValuations

/-! Leading valuation for a finite decreasing clock, including the varying physical tail depths. -/
set_option autoImplicit false
set_option warningAsError true

namespace Collatz.DecliningPadeValuations
open Collatz.PadeArithmetic Collatz.FinitePade Collatz.DecliningPadeCoefficients
open Collatz.DecliningPadeIntegral Collatz.PadeValuations
open Collatz.PadeIntegral (qBase zBase)
open scoped BigOperators

def downClock (h b j : ℕ) : ℤ := (j:ℤ)*(b+1)-h*(tri j:ℤ)

def rawExponent (h b n m : ℕ) : ℤ :=
  (2*(n:ℤ)+m+1)*(b+1)-h*(n+1)*(n+m)

def reducedExponent (h b n m : ℕ) : ℤ :=
  rawExponent h b n m-commonExponent h n m

def weightPower (h b n m k : ℕ) : ℤ :=
  ((n:ℤ)-k)*((b:ℤ)+1-h*((n:ℤ)+k+m))

private theorem binary_val : padicValRat 2 (2:ℚ)=1 := padicValRat.self (by decide : 1<2)

private theorem odd_exact {z : ℤ} (hz : Odd z) : Exact 0 (z:ℚ) := by
  obtain ⟨u,hu⟩ := hz
  have hn : z≠0 := by omega
  have hd : ¬(2:ℤ) ∣ z := by intro ⟨j,hj⟩; omega
  refine ⟨by exact_mod_cast hn,?_⟩
  rw [padicValRat.of_int,padicValInt.eq_zero_of_not_dvd hd]
  rfl

private theorem three_val : padicValRat 2 (3:ℚ)=0 := (odd_exact (by decide : Odd (3:ℤ))).2

theorem down_pos (h : ℕ) : 0<qDown h := by unfold qDown; positivity

theorem down_val (h : ℕ) : padicValRat 2 (qDown h)=h := by
  rw [qDown,padicValRat.pow,padicValRat.div (by decide) (by decide),binary_val,three_val]
  ring

theorem down_term_exact (h b j : ℕ) : Exact (downClock h b j) (term (qDown h) (zBase b) j) := by
  have hp := down_pos h
  have hz := zBase_pos b
  unfold term
  refine ⟨by positivity,?_⟩
  rw [padicValRat.div (by positivity) (by positivity),padicValRat.pow,padicValRat.pow,
    down_val,zBase_val,downClock]
  ring

theorem down_scale_exact (h b n m : ℕ) :
    Exact ((n:ℤ)*(b+1)+h*(tri m:ℤ)-commonExponent h n m) (reducedScale h b n m) := by
  simp only [reducedScale,clearing,Int.cast_mul,Int.cast_pow,Int.cast_ofNat]
  refine ⟨by positivity,?_⟩
  rw [padicValRat.div (by positivity) (by positivity),
    padicValRat.mul (by positivity) (by positivity),padicValRat.pow,padicValRat.pow,
    padicValRat.pow,binary_val,three_val]
  push_cast
  ring

theorem down_poly_exact (h n t : ℕ) (hh : 0<h) (ht : n<t) :
    Exact ((h:ℤ)*((tri (n+1):ℤ)-n*t)) ((padePoly n (qDown h)).eval (((qDown h)^t)⁻¹)) := by
  have hq := (down_pos h).ne'
  induction n with
  | zero =>
    simp only [padePoly_zero,Polynomial.eval_one,tri_succ,tri_zero,Nat.cast_zero,
      add_zero,zero_mul,sub_zero,mul_zero]
    exact ⟨one_ne_zero,padicValRat.one⟩
  | succ n ih =>
    rw [padePoly_succ,Polynomial.eval_mul,Polynomial.eval_sub,Polynomial.eval_one,
      Polynomial.eval_mul,Polynomial.eval_C,Polynomial.eval_X]
    let u := (qDown h)^(n+1)*((qDown h)^t)⁻¹
    let e := (h:ℤ)*((n:ℤ)+1-t)
    have hu : Exact e (-u) := by
      refine ⟨neg_ne_zero.mpr (mul_ne_zero (pow_ne_zero _ hq) (inv_ne_zero (pow_ne_zero _ hq))),?_⟩
      rw [padicValRat.neg]
      dsimp only [u,e]
      rw [padicValRat.mul (pow_ne_zero _ hq) (inv_ne_zero (pow_ne_zero _ hq)),
        padicValRat.pow,padicValRat.inv,padicValRat.pow,down_val]
      push_cast
      ring
    have he : e<0 := by
      have h' : 0<(h:ℤ) := by exact_mod_cast hh
      have ht' : (n:ℤ)+1<t := by exact_mod_cast ht
      exact mul_neg_of_pos_of_neg h' (by omega)
    have hf : Exact e (1-u) := by
      rw [sub_eq_add_neg,add_comm]
      exact exact_add_higher hu (Or.inr (by rwa [padicValRat.one]))
    have hs := exact_mul (ih (by omega)) hf
    have ha : (h:ℤ)*((tri (n+1):ℤ)-n*t)+e=h*((tri (n+1+1):ℤ)-(n+1:ℕ)*t) := by
      rw [tri_succ (n+1)]
      dsimp only [e]
      push_cast
      ring
    simpa only [ha,u] using hs

private theorem twice_int (j : ℕ) : 2*(tri j:ℤ)+j=(j:ℤ)*j := by exact_mod_cast twice_tri j

theorem down_leading_exact (h b n m : ℕ) (hh : 0<h) :
    Exact (reducedExponent h b n m)
      (reducedScale h b n m*leading n m (qDown h) (zBase b)) := by
  have h0 := down_scale_exact h b n m
  have h1 := down_term_exact h b (n+m+1)
  have h2 := down_poly_exact h n (n+1) hh (by omega)
  have hs := exact_mul h0 (exact_mul h1 h2)
  have he : (n:ℤ)*(b+1)+h*(tri m:ℤ)-commonExponent h n m+
      (downClock h b (n+m+1)+h*((tri (n+1):ℤ)-n*(n+1:ℕ)))=reducedExponent h b n m := by
    unfold downClock reducedExponent rawExponent
    have ha := congrArg (fun u : ℤ => (h:ℤ)*u) (twice_int (n+m+1))
    have hb := congrArg (fun u : ℤ => (h:ℤ)*u) (twice_int (n+1))
    have hc := congrArg (fun u : ℤ => (h:ℤ)*u) (twice_int m)
    push_cast at ha hb ⊢
    nlinarith only [ha,hb,hc]
  simpa only [leading,he] using hs

theorem down_weight_exact (h b n m k : ℕ) (hh : 0<h) (hk : k≤n)
    (hb : h*(2*n+m)≤b+1) :
    Exact (weightPower h b n m k) (reducedTerm h b n m k 0:ℚ) := by
  let u := b*(m+k)+h*((n-k)*(n+m))
  have ho := odd_exact ((normalized_odd h n k hh hk).mul ((show Odd (3:ℤ) by decide).pow (n:=u)))
  have he : h*(n+k+m)≤b+1 := (Nat.mul_le_mul_left h (by omega)).trans hb
  have ha : weightPower h b n m k=(((n-k)*(b+1-h*(n+k+m)):ℕ):ℤ) := by
    rw [weightPower,Nat.cast_mul,Nat.cast_sub hk,Nat.cast_sub he]
    push_cast
    ring
  rw [ha]
  let e := (n-k)*(b+1-h*(n+k+m))
  have hp : Exact (e:ℤ) ((2:ℚ)^e) :=
    ⟨by positivity,by rw [padicValRat.pow,binary_val,mul_one]⟩
  have hs := exact_mul hp ho
  have hz : (reducedTerm h b n m k 0:ℚ)=2^e*((normalized h n k*3^u:ℤ):ℚ) := by
    simp only [reducedTerm,reducedTwo,threeIndex,tri_zero,Nat.mul_zero,Nat.sub_zero,
      add_zero,Int.cast_mul,Int.cast_pow,Int.cast_ofNat]
    dsimp only [e,u]
    ring
  simpa only [add_zero,←hz] using hs

/-- Each physical tail has an explicit positive gap from the first surviving term. -/
theorem down_tail_gap (h b n m k : ℕ) (hk : k≤n) :
    weightPower h b n m k+downClock h b (n+m+k+2)-reducedExponent h b n m =
      (b:ℤ)+1-h*(2*(n:ℤ)+m+1)+h*((tri (n-k+1):ℤ)+(n-k:ℕ)) := by
  unfold weightPower downClock reducedExponent rawExponent commonExponent
  have ha := congrArg (fun u : ℤ => (h:ℤ)*u) (twice_int (n+m+k+2))
  have hb := congrArg (fun u : ℤ => (h:ℤ)*u) (twice_int (n-k+1))
  have hc := congrArg (fun u : ℤ => (h:ℤ)*u) (twice_int m)
  push_cast [Nat.cast_sub hk] at ha hb ⊢
  nlinarith only [ha,hb,hc]

theorem down_weighted_tail (h b n m k : ℕ) (hh : 0<h) (hk : k≤n)
    (hb : h*(2*n+m+1)<b+1) (x : ℚ) (hx : AtLeast (downClock h b (n+m+k+2)) x) :
    Higher (reducedExponent h b n m) ((reducedTerm h b n m k 0:ℚ)*x) := by
  by_cases hz : x=0
  · exact Or.inl (by rw [hz,mul_zero])
  have hli : h*(2*n+m)≤b+1 := (Nat.mul_le_mul_left h (show 2*n+m≤2*n+m+1 by omega)).trans hb.le
  have hu := down_weight_exact h b n m k hh hk hli
  have hv := hx.resolve_left hz
  have hg := down_tail_gap h b n m k hk
  have hpos : (h:ℤ)*(2*(n:ℤ)+m+1)<(b:ℤ)+1 := by exact_mod_cast hb
  have hnn : 0≤(h:ℤ)*((tri (n-k+1):ℤ)+(n-k:ℕ)) := by positivity
  right
  rw [padicValRat.mul hu.1 hz,hu.2]
  omega

theorem down_finite_exact (h b n m : ℕ) (hh : 0<h) (hb : h*(2*n+m+1)<b+1) (y : ℚ)
    (ht : ∀ k≤n,AtLeast (downClock h b (n+m+k+2)) (y-partialSum (qDown h) (zBase b) (n+m+k+2))) :
    Exact (reducedExponent h b n m) ((reducedHead h b n m:ℚ)*y-(reducedConstant h b n m:ℚ)) := by
  have hli : h*(2*n+m)≤b+1 := (Nat.mul_le_mul_left h (show 2*n+m≤2*n+m+1 by omega)).trans hb.le
  have he := scaled_finite_identity n m (qDown h) (zBase b) y (reducedScale h b n m)
    (down_pos h).ne' (zBase_pos b).ne'
  rw [reduced_scale_head h b n m hli,reduced_scale_constant h b n m hli] at he
  rw [he]
  apply exact_add_higher (down_leading_exact h b n m hh)
  apply higher_sum
  intro k hk
  rw [reduced_scale_raw h b n m k (by omega) hli]
  exact down_weighted_tail h b n m k hh (by omega) hb _ (ht k (by omega))

/-- The unscaled form has this nonnegative integer exponent throughout the admissible range. -/
def rawNat (h b n m : ℕ) : ℕ := (2*n+m+1)*(b+1)-h*((n+1)*(n+m))

theorem rawNat_cast (h b n m : ℕ) (hb : h*(2*n+m+1)<b+1) :
    (rawNat h b n m:ℤ)=rawExponent h b n m := by
  have ha : h*(n+m)≤b+1 := (Nat.mul_le_mul_left h (by omega)).trans hb.le
  have hc : h*((n+1)*(n+m))≤(2*n+m+1)*(b+1) := by
    calc
      _ = (n+1)*(h*(n+m)) := by ring
      _ ≤ _ := Nat.mul_le_mul (by omega) ha
  rw [rawNat,Nat.cast_sub hc,rawExponent]
  push_cast
  ring

theorem down_integer_lower (h b n m : ℕ) (hh : 0<h) (hb : h*(2*n+m+1)<b+1) (y : ℤ)
    (ht : ∀ k≤n,AtLeast (downClock h b (n+m+k+2)) ((y:ℚ)-partialSum (qDown h) (zBase b) (n+m+k+2))) :
    (2:ℤ)^(rawNat h b n m) ≤
      (2:ℤ)^(commonExponent h n m)*|reducedHead h b n m*y-reducedConstant h b n m| := by
  let D := commonExponent h n m
  let F := (2:ℤ)^D*(reducedHead h b n m*y-reducedConstant h b n m)
  have he := down_finite_exact h b n m hh hb y ht
  have h2 : Exact (D:ℤ) ((2:ℚ)^D) :=
    ⟨by positivity,by rw [padicValRat.pow,binary_val,mul_one]⟩
  have hr : (D:ℤ)+reducedExponent h b n m=(rawNat h b n m:ℤ) := by
    rw [rawNat_cast h b n m hb,reducedExponent]
    dsimp only [D]
    ring
  have hf : Exact (rawNat h b n m) (F:ℚ) := by
    simpa only [F,Int.cast_mul,Int.cast_pow,Int.cast_ofNat,Int.cast_sub,hr] using exact_mul h2 he
  have hn : F≠0 := by exact_mod_cast hf.1
  have hv := hf.2
  rw [padicValRat.of_int] at hv
  have hv' : padicValInt 2 F=rawNat h b n m := by exact_mod_cast hv
  have hd := padicValInt_dvd (p:=2) F
  rw [hv'] at hd
  have hx := Int.natAbs_le_of_dvd_ne_zero hd hn
  have hlow : (2:ℤ)^(rawNat h b n m)≤|F| := by
    simpa only [Int.natCast_natAbs,abs_of_nonneg (by positivity : 0≤(2:ℤ)^rawNat h b n m)]
      using (show ((Int.natAbs ((2:ℤ)^rawNat h b n m):ℕ):ℤ)≤(F.natAbs:ℤ) by exact_mod_cast hx)
  simpa only [F,D,abs_mul,abs_of_nonneg (by positivity : 0≤(2:ℤ)^commonExponent h n m)] using hlow

end Collatz.DecliningPadeValuations
