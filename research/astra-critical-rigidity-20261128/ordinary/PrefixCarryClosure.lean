import SignedReturnRouter
import AdjacentWordClosure

/-! Extend physically supplied adjacent calendars to an equal-grade loop. -/

set_option autoImplicit false
namespace Collatz.PrefixCarryClosure
open Collatz.PoweredAffine Collatz.SignedReturnRouter

private theorem ones_append (u v : List Bool) : ones (u++v)=ones u+ones v := by
  induction u with
  | nil => simp [ones]
  | cons b u ih => simp [ones, ih, Nat.add_assoc]

private theorem numerator_bound (w : List Bool) :
    numerator w ≤ 2^w.length * 3^ones w := by
  induction w with
  | nil => decide
  | cons bit w ih =>
    have hp : (3:Nat)^ones w≤2^w.length*3^ones w := by
      nth_rewrite 1 [←one_mul (3^ones w)]
      exact Nat.mul_le_mul_right _ (Nat.two_pow_pos _)
    cases bit <;> simp only [numerator,ones,List.length_cons,Bool.false_eq_true,↓reduceIte,
      mul_zero,zero_add,mul_one,Nat.add_comm 1 (ones w),pow_succ] <;> nlinarith only [ih,hp]

private theorem word_increment (w : List Bool) (x t : Rat) :
    (2:Rat)^w.length*(evalWord w (x+t)-evalWord w x)=(3:Rat)^ones w*t := by
  have h := word_affine w (x+t)
  have k := word_affine w x
  nlinarith only [h,k]

private def oriented_graph (u v : List Bool) (j : Nat) (x y : Nat) (shift a : Int)
    (len : u.length=v.length) (grades : j+ones u=ones v)
    (entry : (x:Int)-y=shift)
    (hu : Realizes x u) (hv : Realizes y v)
    (terminal : a=(3:Int)^j*(orbit x u.length:Int)-(orbit y v.length:Int)) :
    Route 0 shift j a where
  lower := u
  upper := v
  lengths := len
  grades := by omega
  graph z := by
    have eq : (x:Rat)-y=shift := by exact_mod_cast entry
    have atEnd : (a:Rat)=(3:Rat)^j*(orbit x u.length:Rat)-(orbit y v.length:Rat) := by
      exact_mod_cast terminal
    have vu := word_increment u x (z-x)
    have vv := word_increment v y (z-x)
    rw [show (x:Rat)+(z-x)=z by ring,evalWord_actual hu] at vu
    rw [show (y:Rat)+(z-x)=z-shift by linarith only [eq],evalWord_actual hv,←len,←grades,pow_add] at vv
    simp only [pow_zero,one_mul]
    apply mul_left_cancel₀ (show (2:Rat)^u.length≠0 by positivity)
    calc (2:Rat)^u.length*evalWord v (z-shift) =
             (3:Rat)^j*((2:Rat)^u.length*(evalWord u z-(orbit x u.length:Rat)))+
               2^u.length*(orbit y v.length:Rat) := by rw [vu,←len]; nlinarith only [vv]
         _ = _ := by rw [atEnd]; ring

private theorem shift_bound (u v : List Bool) (j : Nat) (x y : Nat) (shift a : Int)
    (len : u.length=v.length) (grades : j+ones u=ones v)
    (entry : (x:Int)-y=shift) (sign : shift=1 ∨ shift= -1)
    (hu : Realizes x u) (hv : Realizes y v)
    (terminal : a=(3:Int)^j*(orbit x u.length:Int)-(orbit y v.length:Int)) :
    a.natAbs≤3^(ones v+1) := by
  have U : (2:Int)^u.length*(orbit x u.length:Int)=(3:Int)^ones u*x+numerator u := by
    exact_mod_cast actual_word_affine hu
  have V : (2:Int)^u.length*(orbit y v.length:Int)=(3:Int)^ones v*y+numerator v := by
    rw [len]
    exact_mod_cast actual_word_affine hv
  have gradePow : (3:Int)^j*3^ones u=3^ones v := by rw [←pow_add,grades]
  have ledger : (2:Int)^u.length*a = (3:Int)^ones v*shift+
      3^j*(numerator u:Int)-(numerator v:Int) := by
    calc _ = (3:Int)^j*((2:Int)^u.length*(orbit x u.length:Int))-
             (2:Int)^u.length*(orbit y v.length:Int) := by rw [terminal]; ring
         _ = _ := by rw [U,V,←entry,←gradePow]; ring
  have A : (numerator u:Int)≤(2:Int)^u.length*3^ones u := by exact_mod_cast numerator_bound u
  have B : (numerator v:Int)≤(2:Int)^u.length*3^ones v := by rw [len]; exact_mod_cast numerator_bound v
  have Au : (3:Int)^j*(numerator u:Int)≤(2:Int)^u.length*3^ones v := by
    calc _ ≤ (3:Int)^j*((2:Int)^u.length*3^ones u) := mul_le_mul_of_nonneg_left A (by positivity)
         _ = _ := by rw [←gradePow]; ring
  have Av : 0≤(3:Int)^j*(numerator u:Int) := by positivity
  have Bv : 0≤(numerator v:Int) := by positivity
  have tp : 0<(2:Int)^u.length := by positivity
  have kp : 0<(3:Int)^ones v := by positivity
  have tk : (3:Int)^ones v≤(2:Int)^u.length*3^ones v := by
    calc _ = (1:Int)*3^ones v := by ring
         _ ≤ _ := mul_le_mul_of_nonneg_right (by omega) (by positivity)
  have upper : a≤3*(3:Int)^ones v := by
    apply (mul_le_mul_iff_right₀ tp).mp
    rcases sign with h|h <;> rw [h] at ledger <;> nlinarith only [ledger,tk,Au,Bv,tp,kp,Av,B]
  have lower : -(3*(3:Int)^ones v)≤a := by
    apply (mul_le_mul_iff_right₀ tp).mp
    rcases sign with h|h <;> rw [h] at ledger <;> nlinarith only [ledger,tk,Au,Bv,tp,kp,Av,B]
  have castpow : ((3^(ones v+1):Nat):Int)=3*(3:Int)^ones v := by push_cast; rw [pow_succ]; ring
  omega

private theorem pos_level_unit (j : Nat) (a : Int) (A B : Nat)
    (terminal : a=(3:Int)^j*(A:Int)-(B:Int)) (unit : B%3≠0) :
    j=0 ∨ a%3≠0 := by
  cases j with
  | zero => exact Or.inl rfl
  | succ j =>
    right
    rw [terminal,pow_succ]
    have h : ((A:Int) * (3:Int)^j) * 3 = (3:Int)^j * 3 * A := by ring
    rw [←h]
    omega

private theorem oriented_completion (u v : List Bool) (x y : Nat) (shift : Int)
    (len : u.length=v.length) (comp : ones u≤ones v)
    (entry : (x:Int)-y=shift) (sign : shift=1 ∨ shift= -1)
    (hu : Realizes x u) (hv : Realizes y v) (different : orbit x u.length≠orbit y v.length)
    (unit : orbit y v.length%3≠0) :
    ∃ r : Route 0 shift 0 shift, (∃ tail, r.lower=u++tail) ∧ (∃ tail, r.upper=v++tail) ∧
      r.cost≤ones u+ones v+(ones v-ones u)+18*(ones v+1)+14 := by
  let j := ones v-ones u
  let a := (3:Int)^j*(orbit x u.length:Int)-(orbit y v.length:Int)
  have grades : j+ones u=ones v := by dsimp [j]; omega
  have ur := pos_level_unit j a _ _ rfl unit
  have nz : a≠0 := by
    rcases ur with h|h
    · dsimp [a]; rw [h,pow_zero,one_mul]; omega
    · omega
  have bound := shift_bound u v j x y shift a len grades entry sign hu hv rfl
  let head := oriented_graph u v j x y shift a len grades entry hu hv rfl
  have hj : j≤ones v+1 := by omega
  have reset : ∃ t : Route j a 0 shift, t.cost≤j+18*(ones v+1)+14 := by
    rcases sign with h|h
    · rw [h]
      obtain ⟨t,ht⟩ := reset_to_adjacent j (ones v+1) a nz (by omega) hj bound ur
      exact ⟨t,by omega⟩
    · rw [h]
      exact reset_to_reverse j (ones v+1) a nz (by omega) hj bound ur
  obtain ⟨t,ht⟩ := reset
  have headCost : head.cost=ones u+ones v := rfl
  exact ⟨head.thenRoute t,⟨t.lower,rfl⟩,⟨t.upper,rfl⟩,by simp only [Route.then_cost,headCost]; omega⟩

/-- An integral affine route automatically forces all the upper parities
whenever its lower word is realized on the stated initial line. -/
theorem route_replays {i j : Nat} {a b : Int} (r : Route i a j b)
    (x y : Nat) (entry : (y:Int)=(3:Int)^i*x-a) (hu : Realizes x r.lower) :
    Realizes y r.upper ∧ (orbit y r.upper.length:Int)=(3:Int)^j*(orbit x r.lower.length:Int)-b := by
  have entryQ : (y:Rat)=(3:Rat)^i*x-a := by exact_mod_cast entry
  have e := r.graph (x:Rat)
  rw [←entryQ,evalWord_actual hu] at e
  have q := word_affine r.upper (y:Rat)
  rw [e] at q
  let d := (3:Int)^j*(orbit x r.lower.length:Int)-b
  have Z : (2:Int)^r.upper.length*d=(3:Int)^ones r.upper*y+numerator r.upper := by
    dsimp [d]
    exact_mod_cast q
  have dpos : 0≤d := by
    have hn : 0≤(3:Int)^ones r.upper*y+numerator r.upper := by positivity
    rw [←Z] at hn
    exact nonneg_of_mul_nonneg_right hn (by positivity : (0:Int)<2^r.upper.length)
  let n := d.toNat
  have nd : (n:Int)=d := Int.toNat_of_nonneg dpos
  have term : 3^ones r.upper*y+numerator r.upper=2^r.upper.length*n := by
    have zn : (3:Int)^ones r.upper*y+numerator r.upper=(2:Int)^r.upper.length*n := by
      rw [nd,Z]
    exact_mod_cast zn
  have hv := (Collatz.AdjacentWordClosure.realizes_iff_dvd r.upper y).2 ⟨n,term⟩
  have eNat := actual_word_affine hv
  rw [term] at eNat
  have h := Nat.eq_of_mul_eq_mul_left (Nat.two_pow_pos _) eNat
  exact ⟨hv,by rw [h]; exact nd⟩

/-- Any physical nonmerged prefix starting on an adjacent pair with
ternary-unit endpoints extends to a loop in the same orientation. -/
theorem complete_adjacent_prefix (u v : List Bool) (b : Nat)
    (len : u.length=v.length) (hu : Realizes (b+1) u) (hv : Realizes b v)
    (different : orbit (b+1) u.length≠orbit b v.length)
    (unitU : orbit (b+1) u.length%3≠0) (unitV : orbit b v.length%3≠0) :
    ∃ r : Route 0 1 0 1, (∃ tail, r.lower=u++tail) ∧ (∃ tail, r.upper=v++tail) ∧
      r.cost≤20*(ones u+ones v)+32 := by
  by_cases comp : ones u≤ones v
  · obtain ⟨r,hU,hV,hc⟩ := oriented_completion u v (b+1) b 1 len comp
      (by omega) (Or.inl rfl) hu hv different unitV
    exact ⟨r,hU,hV,by omega⟩
  · obtain ⟨r,hV,hU,hc⟩ := oriented_completion v u b (b+1) (-1) len.symm (by omega)
      (by omega) (Or.inr rfl) hv hu (Ne.symm different) unitU
    exact ⟨r.swapZero,hU,hV,by rw [Route.swap_cost]; omega⟩

/-- Returning to translation one forces the ordered native correction
equation, in the natural-number normalization with both sides nonnegative. -/
theorem return_carry (r : Route 0 1 0 1) :
    ones r.lower=ones r.upper ∧
      numerator r.lower+3^(ones r.lower)=numerator r.upper+2^r.lower.length := by
  have grade : ones r.lower=ones r.upper := by have := r.grades; omega
  have e := r.graph 1
  norm_num at e
  have eqL := word_affine r.lower 1
  have eqU := word_affine r.upper 0
  rw [←r.lengths,e] at eqU
  have q : (numerator r.lower:Rat)+3^ones r.lower=(numerator r.upper:Rat)+2^r.lower.length := by
    nlinarith only [eqL,eqU]
  exact ⟨grade,by exact_mod_cast q⟩

private theorem odd_step_unit (n : Nat) (odd : n%2=1) : step n%3≠0 := by
  have := odd_step odd
  omega

private theorem orbit_unit (n k : Nat) (unit : n%3≠0) : orbit n k%3≠0 := by
  induction k generalizing n with
  | zero => exact unit
  | succ k ih =>
    apply ih
    by_cases even : n%2=0
    · have := even_step even; omega
    · exact odd_step_unit n (by omega)

/-- Replace only the prescribed first OO by EO to obtain a true adjacent
prefix with identical endpoints at every later date. Close it by explicit
calendars and bound the equal final grades. -/
theorem close_positive_source_suffix (s G : Nat) (u v : List Bool)
    (odd : s%2=1) (len : u.length=v.length)
    (hu : Realizes (step s) u) (hv : Realizes (step (3*s)) v)
    (different : orbit (step s) u.length≠orbit (step (3*s)) v.length)
    (budget : ones u+ones v+2≤G) :
    ∃ (tailU tailV : List Bool), let U := false::(u++tailU); let V := true::(v++tailV)
      U.length=V.length ∧ 1≤ones U ∧ ones U=ones V ∧ ones U≤16*(G+1) ∧
      numerator U+3^ones U=numerator V+2^U.length := by
  have odd3 : 3*s%2=1 := by omega
  have half := odd_step odd
  have e : step (3*s+1)=step s := by unfold step at *; split_ifs at * <;> omega
  have U : Realizes (3*s+1) (false::u) := ⟨by simp; omega,by simpa only [e] using hu⟩
  have V : Realizes (3*s) (true::v) := ⟨odd3,hv⟩
  have ud := orbit_unit (step s) u.length (odd_step_unit s odd)
  have vd := orbit_unit (step (3*s)) v.length (odd_step_unit (3*s) odd3)
  obtain ⟨r,⟨tailU,tu⟩,⟨tailV,tv⟩,hc⟩ := complete_adjacent_prefix (false::u) (true::v) (3*s)
    (by simp [len]) U V (by simpa only [List.length_cons,orbit,e] using different)
    (by simpa only [List.length_cons,orbit,e] using ud) (by exact vd)
  obtain ⟨graded,carry⟩ := return_carry r
  have lengths := r.lengths
  have budget' : ones r.lower+ones r.upper≤20*(ones u+ones v+1)+32 := by
    simpa [Route.cost,ones,Nat.add_assoc,Nat.add_comm,Nat.add_left_comm] using hc
  have lo : 1≤ones r.upper := by rw [tv]; simp [ones]
  have ub : ones r.lower≤16*(G+1) := by omega
  simp only [List.cons_append] at tu tv
  refine ⟨tailU,tailV,?_⟩
  dsimp only
  rw [←tu,←tv]
  exact ⟨lengths,by omega,graded,ub,carry⟩


#print axioms route_replays
#print axioms complete_adjacent_prefix
#print axioms return_carry
#print axioms close_positive_source_suffix
end Collatz.PrefixCarryClosure
