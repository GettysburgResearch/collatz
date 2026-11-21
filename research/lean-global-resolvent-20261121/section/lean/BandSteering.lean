import ForwardSection

/-!
Inverse steering into the actual inverse-logarithmic forward section.
The input is a ternary unit at most 2^Q; the chosen inverse root has
height below 2^(5Q) and a phase allowing Q binary inverse generations.
-/

namespace CollatzShell.ForwardSection.Band

open Real

noncomputable section

set_option maxHeartbeats 800000

/-- Unbounded rational-approximation scales; no bounded-partial-quotient
assumption is made. -/
def GoodScale (Q : Nat) : Prop :=
  16 ≤ Q ∧ ∃ a : Nat, a.Coprime Q ∧ |(Q:ℝ)*alpha-a| ≤ 1/(Q:ℝ)

theorem goodScale_cofinal (K : Nat) : ∃ Q, K ≤ Q ∧ GoodScale Q := by
  let L := max 16 K
  let N := 4^L
  obtain ⟨a,Q,qp,qn,cop,sep,err⟩ := rotation_grid N (by dsimp [N]; positivity)
  have lq : L < Q := (Nat.pow_lt_pow_iff_right (by decide : 1 < 4)).mp
    (show 4^L < 4^Q by dsimp [N] at sep; omega)
  have kr : K ≤ Q := (le_max_right 16 K).trans lq.le
  have q16 : 16 ≤ Q := (le_max_left 16 K).trans lq.le
  refine ⟨Q,kr,q16,a,cop,err.trans ?_⟩
  exact one_div_le_one_div_of_le (by exact_mod_cast qp)
    (by exact_mod_cast (show Q ≤ N+1 by omega))

/-- A rational grid with a one-cell buffer, as in the forward steering
proof. This local copy avoids depending on an upstream private theorem. -/
private theorem grid_point {a Q : Nat} (qp : 0<Q) (cop : a.Coprime Q) (y : ℝ) :
    ∃ j : Nat, j<Q ∧ ∃ z : ℤ,
      1≤Q*(y+j*((a:ℝ)/Q)-z) ∧ Q*(y+j*((a:ℝ)/Q)-z)≤2 := by
  let F := ⌊(Q:ℝ)*y⌋
  let R := 1-F
  obtain ⟨u,hu⟩ := Int.mod_coprime cop
  let J := (u*R)%(Q:ℤ)
  have qz : (0:ℤ)<Q := by exact_mod_cast qp
  have jl : 0≤J := Int.emod_nonneg _ qz.ne'
  have ju : J<Q := Int.emod_lt_of_pos _ qz
  let j := J.toNat
  have je : (j:ℤ)=J := Int.toNat_of_nonneg jl
  have modj : (a:ℤ)*j ≡ R [ZMOD ↑Q] := by
    rw [je]
    calc (a:ℤ)*J ≡ a*(u*R) [ZMOD ↑Q] := (Int.mod_modEq _ _).mul_left _
         _ ≡ R [ZMOD ↑Q] := by simpa [mul_assoc] using hu.mul_right R
  obtain ⟨z,hz⟩ := Int.modEq_iff_dvd.mp modj.symm
  have eq : (a:ℝ)*j-(1-(F:ℝ))=Q*(z:ℝ) := by exact_mod_cast hz
  have fl : (F:ℝ)≤Q*y := Int.floor_le _
  have fu : (Q:ℝ)*y<F+1 := Int.lt_floor_add_one _
  have qr : (Q:ℝ)≠0 := by positivity
  have alg : (Q:ℝ)*(y+j*((a:ℝ)/Q)-z)=Q*y+(a:ℝ)*j-Q*z := by field_simp
  exact ⟨j,by exact_mod_cast (je.trans_lt ju),z,by rw [alg]; linarith,by rw [alg]; linarith⟩

/-- The inverse rotation, buffered to absorb both later integer errors. -/
theorem inverse_grid {Q : Nat} (hQ : GoodScale Q) (y : ℝ) :
    ∃ p<Q, ∃ Z : ℤ,
      1/(2*(Q:ℝ)) ≤ y+p*(4-alpha)-Q*alpha-Z ∧
      y+p*(4-alpha)-Q*alpha-Z ≤ 7/(2*(Q:ℝ)) := by
  obtain ⟨q16,a,cop,err⟩ := hQ
  have qp : 0<Q := by omega
  have qr : (0:ℝ)<Q := by exact_mod_cast qp
  let theta := y-(Q:ℝ)*alpha
  obtain ⟨p,pq,z,gl,gu⟩ := grid_point qp cop (-theta+7/(2*(Q:ℝ)))
  have pr : (0:ℝ)≤p := by positivity
  have perturb : |(p:ℝ)*((Q:ℝ)*alpha-a)| ≤ 1 := by
    rw [abs_mul,abs_of_nonneg pr]
    calc _ ≤ p*(1/(Q:ℝ)) := mul_le_mul_of_nonneg_left err pr
         _ ≤ 1 := by rw [mul_one_div]; exact (div_le_one qr).mpr (by exact_mod_cast pq.le)
  have algebra : (Q:ℝ)*(y+p*(4-alpha)-Q*alpha-((4*(p:ℤ)-z):ℤ)) =
      7/2-Q*((-theta+7/(2*(Q:ℝ)))+p*((a:ℝ)/Q)-z)-p*(Q*alpha-a) := by
    dsimp [theta]
    push_cast
    field_simp
    ring
  refine ⟨p,pq,4*(p:ℤ)-z,?_,?_⟩
  · apply (div_le_iff₀ (by positivity : (0:ℝ)<2*Q)).mpr
    have h : 1/2 ≤ (Q:ℝ)*(y+p*(4-alpha)-Q*alpha-((4*(p:ℤ)-z):ℤ)) := by
      rw [algebra]; linarith [(abs_le.mp perturb).2]
    linarith
  · apply (le_div_iff₀ (by positivity : (0:ℝ)<2*Q)).mpr
    have h : (Q:ℝ)*(y+p*(4-alpha)-Q*alpha-((4*(p:ℤ)-z):ℤ)) ≤ 7/2 := by
      rw [algebra]; linarith [(abs_le.mp perturb).1]
    linarith

/-- A multiplicative interval of relative width 1/y costs at most 4/y
in binary logarithmic phase. -/
theorem log_error {F y z : ℝ} (fp : 0<F) (hy : 2≤y) (zp : 0<z)
    (lo : F*(1-1/y)≤z) (hi : z≤F) :
    ∃ e : ℝ, 0≤e ∧ e≤4/y ∧ logb 2 z=logb 2 F-e := by
  have yp : 0<y := by linarith
  let v := z/F
  have vp : 0<v := div_pos zp fp
  have vu : v≤1 := (div_le_one fp).mpr hi
  have vl : 1-1/y≤v := (le_div_iff₀ fp).mpr (by nlinarith [lo])
  have vy : (1:ℝ)/y≤1/2 := one_div_le_one_div_of_le (by norm_num) hy
  have vh : 1/2≤v := by linarith
  have lpos : 0<log 2 := log_pos (by norm_num)
  have lnon : log v≤0 := log_nonpos vp.le vu
  have llow := one_sub_inv_le_log_of_pos vp
  have enon : 0≤-logb 2 v := by unfold logb; exact neg_nonneg.mpr (div_nonpos_of_nonpos_of_nonneg lnon lpos.le)
  have frac : 1/v-1 ≤ 2/y := by
    have h : 1-v≤1/y := by linarith
    have inv : 1/v≤2 := (div_le_iff₀ vp).mpr (by linarith)
    calc 1/v-1 = (1-v)/v := by field_simp
         _ ≤ (1/y)/v := div_le_div_of_nonneg_right h vp.le
         _ = (1/v)/y := by ring
         _ ≤ 2/y := div_le_div_of_nonneg_right inv yp.le
  have eup : -logb 2 v≤4/y := by
    unfold logb
    rw [← neg_div]
    apply (div_le_iff₀ lpos).mpr
    calc -log v ≤ 1/v-1 := by rw [one_div]; linarith
         _ ≤ 2/y := frac
         _ = (4/y)*(1/2) := by ring
         _ ≤ _ := mul_le_mul_of_nonneg_left log_two_bounds.1 (by positivity)
  refine ⟨-logb 2 v,enon,eup,?_⟩
  have zeq : z=F*v := by dsimp [v]; field_simp
  rw [zeq,logb_mul fp.ne' vp.ne']
  ring

theorem lift_ge (p y : Nat) (hu : y%3≠0) : y ≤ lift p y := by
  induction p with
  | zero => rfl
  | succ p ih =>
    obtain ⟨_,unit,lower,_⟩ := lift_spec p y hu
    obtain ⟨_,_,bound,_⟩ := inv4_spec (lift p y) unit
    have pos : 0<lift p y := by omega
    change y ≤ inv4 (lift p y)
    omega

theorem lift_upper (p y : Nat) (hu : y%3≠0) : lift p y ≤ 8^p*y := by
  induction p with
  | zero => simp [lift]
  | succ p ih =>
    have unit := (lift_spec p y hu).2.1
    have bound := (inv4_spec (lift p y) unit).2.2.2
    change inv4 (lift p y) ≤ 8^(p+1)*y
    rw [pow_succ]
    nlinarith only [bound, ih]

theorem lift_phase {p y : Nat} (hu : y%3≠0) (hy : 2≤y) :
    ∃ e : ℝ, 0≤e ∧ e≤4/(y:ℝ) ∧
      height (lift p y)=height y+p*(4-alpha)-e := by
  obtain ⟨_,_,lower,upper⟩ := lift_spec p y hu
  let F : ℝ := ((16:ℝ)/3)^p*y
  have fp : 0<F := by
    dsimp [F]
    have yp : (0:ℝ)<y := by exact_mod_cast (show 0<y by omega)
    positivity
  have yp : (0:ℝ)<y := by exact_mod_cast (show 0<y by omega)
  have zp : (0:ℝ)<lift p y := by exact_mod_cast (show 0<lift p y by have := lift_ge p y hu; omega)
  have br : (3:ℝ)^p*(lift p y:ℝ) ≤ 16^p*y := by exact_mod_cast upper
  have lr : (16:ℝ)^p*y+3^p ≤ 3^p*(lift p y:ℝ)+16^p := by exact_mod_cast lower
  have bp : (0:ℝ)<3^p := by positivity
  have hi : (lift p y:ℝ)≤F := by
    dsimp [F]; rw [div_pow,div_mul_eq_mul_div]
    exact (le_div_iff₀ bp).mpr (by nlinarith only [br])
  have lo : F*(1-1/(y:ℝ))≤(lift p y:ℝ) := by
    dsimp [F]; rw [div_pow]
    field_simp
    nlinarith only [lr, show (0:ℝ)≤3^p by positivity]
  obtain ⟨e,el,eu,eq⟩ := log_error fp (by exact_mod_cast hy) zp lo hi
  have form : logb 2 F=height y+p*(4-alpha) := by
    dsimp only [F]
    rw [logb_mul (by positivity) yp.ne',logb_pow,logb_div (by norm_num) (by norm_num)]
    have sixteen : logb 2 16=4 := by
      rw [show (16:ℝ)=2^4 by norm_num,logb_pow,logb_two]; norm_num
    rw [sixteen]
    unfold height alpha
    ring
  exact ⟨e,el,eu,by simpa only [height,form] using eq⟩

theorem scale_error {Q : Nat} (hq : 8≤Q) : 16*Q≤2^Q := by
  induction Q, hq using Nat.le_induction with
  | base => decide
  | succ Q hQ ih => rw [pow_succ]; nlinarith

/-- A single ordinary inverse root, common to all fan leaves, already has
the phase needed to make all of them marked. -/
theorem steered_root_with_clock {Q a : Nat} (hQ : GoodScale Q) (hu : a%3≠0) (ha : a≤2^Q) :
    ∃ z : Nat, z%3≠0 ∧ 2^Q≤z ∧ z<2^(5*Q) ∧
      (∃ d : Nat, Q≤d ∧ d<5*Q ∧ orbit d z=a) ∧
      ∃ Z : ℤ, 1/(4*(Q:ℝ))≤height z-Q*alpha-Z ∧
        height z-Q*alpha-Z≤7/(2*(Q:ℝ)) := by
  have q16 := hQ.1
  have qp : 0<Q := by omega
  have qr : (0:ℝ)<Q := by exact_mod_cast qp
  have ap : 0<a := by omega
  let y := 2^Q*a
  have yu : y%3≠0 := unit_pad Q a hu
  have yl : 2^Q≤y := by dsimp [y]; exact Nat.le_mul_of_pos_right _ ap
  have y2 : 2≤y := (show 2≤2^Q from Nat.le_self_pow (by omega) 2).trans yl
  have yup : y≤2^(2*Q) := by
    calc y ≤ 2^Q*2^Q := Nat.mul_le_mul_left _ ha
         _ = _ := by rw [←pow_add]; congr 1; omega
  obtain ⟨p,pq,Z,pl,pu⟩ := inverse_grid hQ (height y)
  let z := lift p y
  have zu : z%3≠0 := (lift_spec p y yu).2.1
  have zy : y≤z := lift_ge p y yu
  have zlo : 2^Q≤z := yl.trans zy
  have zhi : z<2^(5*Q) := by
    calc z ≤ 8^p*y := lift_upper p y yu
         _ ≤ 8^p*2^(2*Q) := Nat.mul_le_mul_left _ yup
         _ = 2^(3*p+2*Q) := by rw [show (8:Nat)=2^3 by decide,←pow_mul,←pow_add]
         _ < _ := (Nat.pow_lt_pow_iff_right (by decide : 1<2)).mpr (by omega)
  obtain ⟨e,el,eu,phase⟩ := lift_phase (p:=p) yu y2
  have ey : e≤1/(4*(Q:ℝ)) := by
    calc e ≤ 4/(y:ℝ) := eu
         _ ≤ 4/((2^Q:Nat):ℝ) := div_le_div_of_nonneg_left (by norm_num) (by positivity) (by exact_mod_cast yl)
         _ ≤ _ := by
           apply (div_le_div_iff₀ (by positivity : (0:ℝ)<(2^Q:Nat)) (by positivity : (0:ℝ)<4*Q)).mpr
           exact_mod_cast (show 4*(4*Q)≤1*2^Q by have := scale_error (Q:=Q) (by omega); omega)
  refine ⟨z,zu,zlo,zhi,?_,Z,?_,?_⟩
  · refine ⟨4*p+Q,by omega,by omega,?_⟩
    rw [orbit_add,(lift_spec p y yu).1]
    exact orbit_pad Q a
  · change 1/(4*(Q:ℝ))≤height (lift p y)-Q*alpha-Z
    rw [phase]
    have eq : 1/(2*(Q:ℝ))-1/(4*Q)=1/(4*Q) := by field_simp; ring
    linarith
  · change height (lift p y)-Q*alpha-Z≤7/(2*(Q:ℝ))
    rw [phase]
    linarith

theorem steered_root {Q a : Nat} (hQ : GoodScale Q) (hu : a%3≠0) (ha : a≤2^Q) :
    ∃ z : Nat, z%3≠0 ∧ 2^Q≤z ∧ z<2^(5*Q) ∧ Hits z a ∧
      ∃ Z : ℤ, 1/(4*(Q:ℝ))≤height z-Q*alpha-Z ∧
        height z-Q*alpha-Z≤7/(2*(Q:ℝ)) := by
  obtain ⟨z,zu,zlo,zhi,⟨d,_,_,hit⟩,phase⟩ := steered_root_with_clock hQ hu ha
  exact ⟨z,zu,zlo,zhi,⟨d,hit⟩,phase⟩

#print axioms goodScale_cofinal
#print axioms steered_root_with_clock
#print axioms steered_root

end

end CollatzShell.ForwardSection.Band
