import FirstArrival
import SharpClock
import FastWindow

/-! Physical first-hit pairs with fixed additive separation in every
sufficiently large relative interval, uniformly over every ternary-unit
target and every class of the lower source. -/
set_option autoImplicit false
set_option warningAsError true

namespace Collatz.FastPairs
open TwoGapRouting FixedGapClock FirstArrival

private theorem runs (h n : ℕ) : CoreBranching.run h n=run h n := by
  induction h generalizing n with
  | zero => rfl
  | succ h ih => exact ih (step n)

private theorem grades (h n : ℕ) : PeakRigidity.grade h n=odds h n := by
  induction h with
  | zero => rfl
  | succ h ih =>
    change PeakRigidity.grade h n+CoreBranching.run h n%2=odds (h+1) n
    rw [ih,runs,(append h 1 n).2]
    simp [odds]

private theorem branch_size {b e y : ℕ} (clock : e≤10) (leg : First e b y)
    (grade : odds e b=1) : (b:ℝ)≤1024*y ∧ (y:ℝ)≤4*b := by
  have l:=MergerThreshold.forward_lower e b
  have u:=SharpClock.physical_height e b
  rw [leg.1,grade] at l u
  have big : 2^e≤1024 := by
    calc (2:ℕ)^e ≤ 2^10 := Nat.pow_le_pow_right (by decide) clock
         _ = _ := by decide
  have small:=Nat.one_le_two_pow (n:=e)
  have m:=Nat.mul_le_mul_right y big
  have t:=Nat.mul_le_mul_right y small
  constructor
  · exact_mod_cast (show b≤1024*y by simp at l; omega)
  · exact_mod_cast (show y≤4*b by simp at u; omega)

def Visitors (η : ℝ) : Prop :=
  ∃ P Q : ℝ, ∃ J : ℕ, 0<P ∧ 0<Q ∧ ∀ b : ℕ, InverseSpreading.unitOdd b →
    ∀ Z : ℝ, P*b≤Z → ∃ w m j : ℕ, 0<w ∧ w%3≠0 ∧ Z≤w ∧
      (w:ℝ)<(1+η)*Z ∧ CoreBranching.run m w=b ∧
      PeakRigidity.grade m w=j ∧ j≤J ∧ (2:ℝ)^m*b≤Q*w

/-- The exponential time bound is equivalent to an additive overhead of
log₂ K above log₂(X/y). The same source meets all conclusions. -/
def Pairs (s d : ℕ) (δ : ℝ) : Prop :=
  ∃ C K : ℝ, ∃ G : ℕ, 0<C ∧ 0<K ∧ ∀ y : ℕ, y%3≠0 → ∀ X : ℝ, C*y≤X →
    ∀c : ℕ, ∃ x D a : ℕ, 0<x ∧ x ≡ c [MOD 3^s] ∧ X≤x ∧
      (x:ℝ)+d≤(1+δ)*X ∧ First D x y ∧ First D (x+d) y ∧
      odds D x=a ∧ odds D (x+d)=a ∧ a≤G ∧ (2:ℝ)^D*y≤K*X

theorem pairs_of_visitors (s d : ℕ) (δ : ℝ) (positive : 0<δ)
    (visitors : ∀η : ℝ, 0<η → Visitors η) : Pairs s d δ := by
  let η:=min (δ/8) 1
  have ep : 0<η := lt_min (by positivity) (by norm_num)
  have ed : η≤δ/8 := min_le_left _ _
  have eOne : η≤1 := min_le_right _ _
  have ep1 : 0<1+η := by linarith
  obtain ⟨P,Q,J,pP,pQ,window⟩:=visitors η ep
  obtain ⟨H,g,core,_⟩:=cover_bound d s
  let A : ℝ := 2^H/3^g
  have apos : 0<A := by dsimp [A]; positivity
  have ratio : A*(3:ℝ)^g=2^H := by dsimp [A]; field_simp
  let C : ℝ:=1024*A*P+((2:ℝ)^H+d)/η+1
  let K : ℝ:=4096*Q*3^g*(1+η)^2
  have cpos : 0<C := by dsimp [C]; positivity
  have kpos : 0<K := by dsimp [K]; positivity
  refine ⟨C,K,g+J+1,cpos,kpos,?_⟩
  intro y yu X large c
  have yp : 1≤(y:ℝ) := by exact_mod_cast (show 1≤y by omega)
  have ypositive : 0<(y:ℝ) := by linarith
  have cx : C≤X := (le_mul_of_one_le_right cpos.le yp).trans large
  have xp : 0<X := cpos.trans_le cx
  obtain ⟨b,e,bo,bu,_,eb,out,leg,ebOdd⟩:=branch y yu
  obtain ⟨byUpper,yb⟩:=branch_size eb leg ebOdd
  let Z:=(1+η)*X/A
  have az : A*Z=(1+η)*X := by dsimp [Z]; field_simp
  have c1 : 1024*A*P≤C := by
    dsimp [C]
    linarith [show 0≤((2:ℝ)^H+d)/η by positivity]
  have c2 : ((2:ℝ)^H+d)/η≤C := by
    dsimp [C]
    linarith [show 0≤1024*A*P by positivity]
  have allowance : (2:ℝ)^H+d≤η*X := by
    have h:=(div_le_iff₀ ep).mp (c2.trans cx)
    linarith
  have windowSize : P*b≤Z := by
    apply (mul_le_mul_iff_right₀ apos).mp
    calc
      A*(P*b) ≤ A*(P*(1024*y)) :=
        mul_le_mul_of_nonneg_left (mul_le_mul_of_nonneg_left byUpper pP.le) apos.le
      _ = (1024*A*P)*y := by ring
      _ ≤ C*y := mul_le_mul_of_nonneg_right c1 ypositive.le
      _ ≤ X := large
      _ ≤ A*Z := by rw [az]; nlinarith only [mul_pos ep xp]
  obtain ⟨w,m,j,_,wu,wlo,whi,wrun,wgrade,jb,speed⟩:=window b ⟨bo,bu⟩ Z windowSize
  rw [runs] at wrun
  rw [grades] at wgrade
  obtain ⟨x,xp',xc,left,right,lg,rg,loNat,hiNat⟩:=
    attach (c:=c) core (le_refl H) wu wrun out leg
  rw [wgrade,ebOdd] at lg rg
  have lo : (3:ℝ)^g*x≤(2:ℝ)^H*w := by exact_mod_cast loNat
  have hi : (2:ℝ)^H*w≤(3:ℝ)^g*(x+2^H) := by exact_mod_cast hiNat
  have gx : 0<(3:ℝ)^g := by positivity
  have midlo : (x:ℝ)≤A*w := by
    apply (mul_le_mul_iff_left₀ gx).mp
    nlinarith only [lo,congrArg (fun t:ℝ => t*w) ratio]
  have midhi : A*w≤(x:ℝ)+2^H := by
    apply (mul_le_mul_iff_left₀ gx).mp
    nlinarith only [hi,congrArg (fun t:ℝ => t*w) ratio]
  have leftBound : X≤(x:ℝ) := by
    have low:=mul_le_mul_of_nonneg_left wlo apos.le
    rw [az] at low
    nlinarith only [low,midhi,allowance,show 0≤(d:ℝ) by positivity]
  have wh : A*w≤(1+η)^2*X := by
    calc A*w ≤ A*((1+η)*Z) := mul_le_mul_of_nonneg_left whi.le apos.le
         _ = (1+η)*(A*Z) := by ring
         _ = _ := by rw [az]; ring
  have width : (1+η)^2+η≤1+δ := by
    nlinarith only [mul_nonneg ep.le (sub_nonneg.mpr eOne),ed]
  have rightBound : (x:ℝ)+d≤(1+δ)*X := by
    have t:=mul_le_mul_of_nonneg_right width xp.le
    nlinarith only [midlo,wh,allowance,t,show 0≤(2:ℝ)^H by positivity]
  refine ⟨x,H+m+e,g+j+1,xp',xc,leftBound,rightBound,left,right,lg,rg,by omega,?_⟩
  have powe : (2:ℝ)^e≤1024 := by
    calc (2:ℝ)^e ≤ 2^10 := pow_le_pow_right₀ (by norm_num) eb
         _ = _ := by norm_num
  have mscale : (2:ℝ)^m*y≤4*(Q*w) := by
    nlinarith only [mul_le_mul_of_nonneg_left yb (show 0≤(2:ℝ)^m by positivity),speed]
  have scaledW : (2:ℝ)^H*w ≤ 3^g*((1+η)^2*X) := by
    nlinarith only [mul_le_mul_of_nonneg_left wh gx.le,congrArg (fun t:ℝ => t*w) ratio]
  calc
    (2:ℝ)^(H+m+e)*y = 2^e*(2^H*(2^m*y)) := by rw [pow_add,pow_add]; ring
    _ ≤ 1024*(2^H*(4*(Q*w))) := by
        apply mul_le_mul powe _ (by positivity) (by norm_num)
        exact mul_le_mul_of_nonneg_left mscale (by positivity)
    _ = (4096*Q)*(2^H*w) := by ring
    _ ≤ (4096*Q)*(3^g*((1+η)^2*X)) :=
      mul_le_mul_of_nonneg_left scaledW (by positivity)
    _ = K*X := by dsimp [K]; ring

/-- Unconditional simultaneous ordinary first arrivals for every ternary-unit
target in every sufficiently large specified relative interval. -/
theorem fast_pairs (s d : ℕ) (δ : ℝ) (positive : 0<δ) : Pairs s d δ :=
  pairs_of_visitors s d δ positive FastWindow.visitors

#print axioms fast_pairs
#print axioms pairs_of_visitors
end Collatz.FastPairs
