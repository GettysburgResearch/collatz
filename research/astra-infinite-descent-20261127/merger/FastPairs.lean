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

def MarkedVisitors (η : ℝ) (M Q : ℕ) : Prop :=
  ∃ P V : ℝ, ∃ J : ℕ, 0<P ∧ 0<V ∧ ∀b : ℕ, InverseSpreading.unitOdd b →
    ∀Z : ℝ, P*b≤Z → ∀t r : ℕ, ∃w m j : ℕ, 0<w ∧ w%3≠0 ∧ Z≤w ∧
      (w:ℝ)<(1+η)*Z ∧ CoreBranching.run m w=b ∧ PeakRigidity.grade m w=j ∧
      j≤J ∧ (2:ℝ)^m*b≤V*w ∧ m ≡ t [MOD M] ∧ j ≡ r [MOD Q]

theorem trivial_marks {η : ℝ} (oracle : Visitors η) : MarkedVisitors η 1 1 := by
  obtain ⟨P,V,J,pp,vp,all⟩:=oracle
  refine ⟨P,V,J,pp,vp,?_⟩
  intro b bu Z low t r
  obtain ⟨w,m,j,wp,wu,wl,wh,hit,grade,jb,speed⟩:=all b bu Z low
  exact ⟨w,m,j,wp,wu,wl,wh,hit,grade,jb,speed,Nat.modEq_one,Nat.modEq_one⟩

/-- A fixed-clock ordinary certificate on all the indicated offsets. The
source condition may impose both a binary cylinder and supplied trits. -/
def Rows (members : ℕ → Prop) (source : ℕ → ℕ → Prop) (H g : ℕ) : Prop :=
  ∀w : ℕ, w%3≠0 → ∀c : ℕ, ∃x : ℕ, 0<x ∧ source c x ∧
    ∀i, members i → run H (x+i)=w ∧ odds H (x+i)=g

def Relative (members : ℕ → Prop) (source : ℕ → ℕ → Prop) (d M Q : ℕ) (δ : ℝ) : Prop :=
  ∃ C K : ℝ, ∃ G : ℕ, 0<C ∧ 0<K ∧ ∀ y : ℕ, y%3≠0 → ∀ X : ℝ, C*y≤X →
    ∀c t r : ℕ, ∃ x D a : ℕ, 0<x ∧ source c x ∧ X≤x ∧
      (x:ℝ)+d≤(1+δ)*X ∧ (∀i, members i → First D (x+i) y ∧ odds D (x+i)=a) ∧
      a≤G ∧ (2:ℝ)^D*y≤K*X ∧ D ≡ t [MOD M] ∧ a ≡ r [MOD Q]

private theorem translated (v b M : ℕ) (mp : 0<M) :
    (v+(M-1)*b)+b ≡ v [MOD M] := by
  have eq : (M-1)*b+b=M*b := by
    calc (M-1)*b+b=(M-1+1)*b := by ring
         _ = _ := by rw [Nat.sub_add_cancel (by omega)]
  rw [Nat.add_assoc,eq]
  simp [Nat.ModEq]

/-- Transfer every arm through the same odd predecessor outside the target's
forward orbit. The scaling constants are uniform in the trits and both
requested time and grade residues. -/
theorem rows_of_marked_visitors {members : ℕ → Prop} {source : ℕ → ℕ → Prop}
    {H g M Q d : ℕ} (contains_zero : members 0) (rows : Rows members source H g)
    (mp : 0<M) (qp : 0<Q) (δ : ℝ) (positive : 0<δ)
    (visitors : ∀η : ℝ, 0<η → MarkedVisitors η M Q) : Relative members source d M Q δ := by
  let η:=min (δ/8) 1
  have ep : 0<η := lt_min (by positivity) (by norm_num)
  have ed : η≤δ/8 := min_le_left _ _
  have eOne : η≤1 := min_le_right _ _
  have ep1 : 0<1+η := by linarith
  obtain ⟨P,V,J,pP,pV,window⟩:=visitors η ep
  let A : ℝ := 2^H/3^g
  have apos : 0<A := by dsimp [A]; positivity
  have ratio : A*(3:ℝ)^g=2^H := by dsimp [A]; field_simp
  let C : ℝ:=1024*A*P+((2:ℝ)^H+d)/η+1
  let K : ℝ:=4096*V*3^g*(1+η)^2
  have cpos : 0<C := by dsimp [C]; positivity
  have kpos : 0<K := by dsimp [K]; positivity
  refine ⟨C,K,g+J+1,cpos,kpos,?_⟩
  intro y yu X large c t r
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
  obtain ⟨w,m,j,_,wu,wlo,whi,wrun,wgrade,jb,speed,mt,jr⟩:=
    window b ⟨bo,bu⟩ Z windowSize (t+(M-1)*(H+e)) (r+(Q-1)*(g+1))
  rw [runs] at wrun
  rw [grades] at wgrade
  obtain ⟨x,xp',xc,arms⟩:=rows w wu c
  obtain ⟨meet,grade⟩:=arms 0 contains_zero
  simp only [Nat.add_zero] at meet grade
  have lower:=MergerThreshold.forward_lower H x
  have hiNat:=FirstArrival.affine_upper H x
  rw [meet,grade] at lower hiNat
  have loNat : 3^g*x≤2^H*w := by omega
  have allVisits : ∀i, members i → First (H+m+e) (x+i) y ∧ odds (H+m+e) (x+i)=g+j+1 := by
    intro i hi
    obtain ⟨wAt,gAt⟩:=arms i hi
    obtain ⟨r1,g1⟩:=append H m (x+i)
    rw [wAt,wrun] at r1
    rw [wAt,gAt,wgrade] at g1
    have count:=(append (H+m) e (x+i)).2
    rw [r1,g1,ebOdd] at count
    exact ⟨FirstArrival.join r1 out leg,count⟩
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
  have clockMark : H+m+e ≡ t [MOD M] := by
    rw [show H+m+e=m+(H+e) by omega]
    exact (mt.add_right (H+e)).trans (translated t (H+e) M mp)
  have gradeMark : g+j+1 ≡ r [MOD Q] := by
    rw [show g+j+1=j+(g+1) by omega]
    exact (jr.add_right (g+1)).trans (translated r (g+1) Q qp)
  refine ⟨x,H+m+e,g+j+1,xp',xc,leftBound,rightBound,allVisits,by omega,?_,clockMark,gradeMark⟩
  have powe : (2:ℝ)^e≤1024 := by
    calc (2:ℝ)^e ≤ 2^10 := pow_le_pow_right₀ (by norm_num) eb
         _ = _ := by norm_num
  have mscale : (2:ℝ)^m*y≤4*(V*w) := by
    nlinarith only [mul_le_mul_of_nonneg_left yb (show 0≤(2:ℝ)^m by positivity),speed]
  have scaledW : (2:ℝ)^H*w ≤ 3^g*((1+η)^2*X) := by
    nlinarith only [mul_le_mul_of_nonneg_left wh gx.le,congrArg (fun t:ℝ => t*w) ratio]
  calc
    (2:ℝ)^(H+m+e)*y = 2^e*(2^H*(2^m*y)) := by rw [pow_add,pow_add]; ring
    _ ≤ 1024*(2^H*(4*(V*w))) := by
        apply mul_le_mul powe _ (by positivity) (by norm_num)
        exact mul_le_mul_of_nonneg_left mscale (by positivity)
    _ = (4096*V)*(2^H*w) := by ring
    _ ≤ (4096*V)*(3^g*((1+η)^2*X)) :=
      mul_le_mul_of_nonneg_left scaledW (by positivity)
    _ = K*X := by dsimp [K]; ring

theorem pairs_of_visitors (s d : ℕ) (δ : ℝ) (positive : 0<δ)
    (visitors : ∀η : ℝ, 0<η → Visitors η) : Pairs s d δ := by
  obtain ⟨H,g,core,_⟩:=cover_bound d s
  let members (i : ℕ) := i=0 ∨ i=d
  let source (c x : ℕ) := x ≡ c [MOD 3^s]
  have bank : Rows members source H g := by
    intro w wu c
    obtain ⟨x,xp,xc,left,right,lg,rg⟩:=core H (le_refl H) w wu c
    refine ⟨x,xp,xc,?_⟩
    intro i hi
    rcases hi with zero|eq
    · simpa [zero] using And.intro left lg
    · simpa [eq] using And.intro right rg
  obtain ⟨C,K,G,cp,kp,all⟩:=rows_of_marked_visitors (d:=d) (M:=1) (Q:=1)
    (show members 0 from Or.inl rfl) bank (by decide) (by decide) δ positive
    (fun η ep => trivial_marks (visitors η ep))
  refine ⟨C,K,G,cp,kp,?_⟩
  intro y yu X large c
  obtain ⟨x,D,a,xp,xc,low,high,visits,gb,speed,_,_⟩:=all y yu X large c 0 0
  obtain ⟨firstLeft,gradeLeft⟩:=visits 0 (Or.inl rfl)
  obtain ⟨firstRight,gradeRight⟩:=visits d (Or.inr rfl)
  simp only [Nat.add_zero] at firstLeft gradeLeft
  exact ⟨x,D,a,xp,xc,low,high,firstLeft,firstRight,gradeLeft,gradeRight,gb,speed⟩

/-- Unconditional simultaneous ordinary first arrivals for every ternary-unit
target in every sufficiently large specified relative interval. -/
theorem fast_pairs (s d : ℕ) (δ : ℝ) (positive : 0<δ) : Pairs s d δ :=
  pairs_of_visitors s d δ positive FastWindow.visitors

#print axioms rows_of_marked_visitors
#print axioms fast_pairs
#print axioms pairs_of_visitors
end Collatz.FastPairs
