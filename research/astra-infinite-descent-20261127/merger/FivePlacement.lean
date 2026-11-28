import FiveWindow

/-! A dual first-visit certificate for the ordinary multiplication-by-five
comparison in every sufficiently high relative interval. -/
set_option autoImplicit false
set_option warningAsError true

namespace Collatz.FivePlacement
open TwoGapRouting FirstArrival FiveRouting FiveLadder

def Rows (members : ℕ → Prop) (source : ℕ → ℕ → Prop) (H g : ℕ) : Prop :=
  ∀w : ℕ, w%3≠0 → ∀c : ℕ, ∃x : ℕ, 0<x ∧ source c x ∧
    ∀i, members i → Dual H g (x+i) w

def Placement (members : ℕ → Prop) (source : ℕ → ℕ → Prop) (d M Q : ℕ) (δ : ℝ) : Prop :=
  ∃C K : ℝ, ∃G : ℕ, 0<C ∧ 0<K ∧ ∀ y : ℕ, y%3≠0 → ∀X : ℝ, C*y≤X →
    ∀c τ ρ : ℕ, ∃x D a : ℕ, 0<x ∧ source c x ∧ X≤x ∧
      (x:ℝ)+d≤(1+δ)*X ∧ (∀i, members i → Flight D a (x+i) y) ∧
      a≤G ∧ (2:ℝ)^D*y≤K*X ∧ D ≡ τ [MOD M] ∧ a ≡ ρ [MOD Q]

private theorem marked {m : ℕ} (mp : 0<m) (x u : ℕ) :
    (x+(m-1)*u)+u ≡ x [MOD m] := by
  have e : m-1+1=m := by omega
  rw [Nat.add_assoc,show (m-1)*u+u=(m-1+1)*u by ring,e]
  simp [Nat.ModEq]

/-- A fixed finite native return bank can be followed by the simultaneous
marked phase ladder without any distributional or ordinary-density input. -/
theorem of_rows {members : ℕ → Prop} {source : ℕ → ℕ → Prop} {H g : ℕ}
    (zero : members 0) (rows : Rows members source H g) (d M Q : ℕ) (mp : 0<M) (qp : 0<Q)
    (δ : ℝ) (positive : 0<δ) : Placement members source d M Q δ := by
  let η:=min (δ/8) 1
  have ep : 0<η := lt_min (by positivity) (by norm_num)
  have ed : η≤δ/8 := min_le_left _ _
  have eOne : η≤1 := min_le_right _ _
  have ep1 : 0<1+η := by linarith
  obtain ⟨P,V,J,pp,vp,window⟩:=FiveWindow.visitors M Q mp qp η ep
  let A : ℝ:=2^H/3^g
  have ap : 0<A := by dsimp [A]; positivity
  have ratio : A*(3:ℝ)^g=2^H := by dsimp [A]; field_simp
  let C:=A*P+((2:ℝ)^H+d)/η+2^H+2
  let K:=V*3^g*(1+η)^2
  have cp : 0<C := by dsimp [C]; positivity
  have kp : 0<K := by dsimp [K]; positivity
  refine ⟨C,K,g+J,cp,kp,?_⟩
  intro y yu X high c τ ρ
  have yr : 1≤(y:ℝ) := by exact_mod_cast (show 0<y by omega)
  have yp : 0<(y:ℝ) := by linarith
  have cx : C≤X := (le_mul_of_one_le_right cp.le yr).trans high
  have xp : 0<X := cp.trans_le cx
  have margin : 0≤((2:ℝ)^H+d)/η := by positivity
  have prod : 0≤A*P := by positivity
  have powH : 0<(2:ℝ)^H := by positivity
  have c1 : A*P≤C := by dsimp [C]; linarith
  have c2 : ((2:ℝ)^H+d)/η≤C := by dsimp [C]; linarith
  have c3 : (2:ℝ)^H<C := by dsimp [C]; linarith
  have allowance : (2:ℝ)^H+d≤η*X := by
    have h:=(div_le_iff₀ ep).mp (c2.trans cx); linarith
  let Z:=(1+η)*X/A
  have az : A*Z=(1+η)*X := by dsimp [Z]; field_simp
  have enough : P*y≤Z := by
    apply (mul_le_mul_iff_right₀ ap).mp
    calc
      A*(P*y) = (A*P)*y := by ring
      _ ≤ C*y := mul_le_mul_of_nonneg_right c1 yp.le
      _ ≤ X := high
      _ ≤ A*Z := by rw [az]; nlinarith [mul_pos ep xp]
  obtain ⟨w,m,j,_,wu,wl,wh,flight,jb,speed,tm,jm⟩:=
    window y yu Z enough (τ+(M-1)*H) (ρ+(Q-1)*g)
  obtain ⟨x,xp',xc,arms⟩:=rows w wu c
  obtain ⟨meet,grade,_,_⟩:=arms 0 zero
  simp only [Nat.add_zero] at meet grade
  have lower:=MergerThreshold.forward_lower H x
  have upper:=FirstArrival.affine_upper H x
  rw [meet,grade] at lower upper
  have lr : (3:ℝ)^g*x≤2^H*w := by exact_mod_cast (show 3^g*x≤2^H*w by omega)
  have ur : (2:ℝ)^H*w≤3^g*(x+2^H) := by exact_mod_cast upper
  have powG : 0<(3:ℝ)^g := by positivity
  have midlow : (x:ℝ)≤A*w := by
    apply (mul_le_mul_iff_left₀ powG).mp
    nlinarith only [lr,congrArg (fun z:ℝ => z*w) ratio]
  have midhi : A*w≤(x:ℝ)+2^H := by
    apply (mul_le_mul_iff_left₀ powG).mp
    nlinarith only [ur,congrArg (fun z:ℝ => z*w) ratio]
  have xl : X≤(x:ℝ) := by
    have low:=mul_le_mul_of_nonneg_left wl ap.le
    rw [az] at low
    linarith [show 0≤(d:ℝ) by positivity]
  have landed : A*w≤(1+η)^2*X := by
    calc
      A*w ≤ A*((1+η)*Z) := mul_le_mul_of_nonneg_left wh.le ap.le
      _ = (1+η)*(A*Z) := by ring
      _ = _ := by rw [az]; ring
  have width : (1+η)^2+η≤1+δ := by
    nlinarith only [mul_nonneg ep.le (sub_nonneg.mpr eOne),ed]
  have xh : (x:ℝ)+d≤(1+δ)*X := by
    have bound:=mul_le_mul_of_nonneg_right width xp.le
    nlinarith only [midlow,landed,allowance,bound,powH]
  have guard : 2^H*y<x := by
    exact_mod_cast ((mul_lt_mul_of_pos_right c3 yp).trans_le (high.trans xl))
  have all (i : ℕ) (hi : members i) : Flight (H+m) (g+j) (x+i) y :=
    preattach (arms i hi) flight (by omega)
  have timeMark : H+m ≡ τ [MOD M] := by
    rw [Nat.add_comm]
    exact (tm.add_right H).trans (marked mp τ H)
  have gradeMark : g+j ≡ ρ [MOD Q] := by
    rw [Nat.add_comm]
    exact (jm.add_right g).trans (marked qp ρ g)
  refine ⟨x,H+m,g+j,xp',xc,xl,xh,all,by omega,?_,timeMark,gradeMark⟩
  have scaled : (2:ℝ)^H*w≤3^g*((1+η)^2*X) := by
    nlinarith only [mul_le_mul_of_nonneg_left landed powG.le,congrArg (fun z:ℝ => z*w) ratio]
  have st:=mul_le_mul_of_nonneg_left speed powH.le
  have sk:=mul_le_mul_of_nonneg_left scaled vp.le
  dsimp [K]; rw [pow_add]; nlinarith only [st,sk]

/-- Both ordinary inputs x,5x first reach the two supplied targets y,5y
at an identical near-fast physical clock and odd grade. The lower source
has arbitrary prescribed ternary trits and the actual native low binary
class. Both time and grade residues are freely chosen. -/
theorem five_queries (s M Q : ℕ) (mp : 0<M) (qp : 0<Q) (δ : ℝ) (positive : 0<δ) :
    Placement (fun i => i=0) (fun c x => x ≡ c [MOD 3^s] ∧ x%64=49) 0 M Q δ := by
  let H:=54*3^s+11
  have rows : Rows (fun i => i=0) (fun c x => x ≡ c [MOD 3^s] ∧ x%64=49) H 4 := by
    intro w wu c
    obtain ⟨x,e,xp,eh,ef,_,res,num,physical⟩:=FiveRouting.route s H w c (le_refl H) wu
    have h1 : 6≤H := by omega
    have p : 2^e=64*2^(e-6) := by rw [show e=6+(e-6) by omega,pow_add]; norm_num
    have h : 2^H=64*2^(H-6) := by rw [show H=6+(H-6) by omega,pow_add]; norm_num
    rw [p,h] at num
    have factored : 81*x+63+448*2^(e-6)=64*(2^(H-6)*w) := by nlinarith only [num]
    have f : x%64=49 := by omega
    exact ⟨x,xp,⟨res,f⟩,by rintro _ rfl; simpa using physical⟩
  exact of_rows (members:=fun i => i=0) rfl rows 0 M Q mp qp δ positive

#print axioms of_rows
#print axioms five_queries
end Collatz.FivePlacement
