import MarkedCylinders

namespace CollatzShell.MarkedCylinders
open Real ForwardSection

/-- At every ternary-unit row endpoint one of two successive positive
exponents makes a positive odd predecessor. The clock statement includes
every intermediate halving. -/
theorem odd_predecessor {u Q : Nat} (unit : u%3≠0) (qp : 0<Q) :
    ∃ e x : Nat, Q≤e ∧ e≤Q+1 ∧ 0<x ∧ x%2=1 ∧
      3*x+1=2^e*u ∧ orbit e x=u := by
  have wunit := unit_pad Q u unit
  have exp : ∃ e, Q≤e ∧ e≤Q+1 ∧ (2^e*u)%3=1 := by
    by_cases h : (2^Q*u)%3=1
    · exact ⟨Q,by omega,by omega,h⟩
    · refine ⟨Q+1,by omega,by omega,?_⟩
      rw [show 2^(Q+1)*u=2*(2^Q*u) by ring]; omega
  obtain ⟨e,ge,le,mod⟩ := exp
  obtain ⟨h,rfl⟩ := Nat.exists_eq_succ_of_ne_zero (by omega : e≠0)
  let v := 2^h*u
  have eqm : 2^(h+1)*u=2*v := by dsimp [v]; ring
  rw [eqm] at mod
  have vp : 0<v := by dsimp [v]; apply Nat.mul_pos (by positivity); omega
  let x := (2*v)/3
  have eq : 3*x+1=2*v := by dsimp [x]; omega
  have odd : x%2=1 := by omega
  have next : step x=v := by simp [step,odd]; omega
  refine ⟨h+1,x,ge,le,by omega,odd,eq.trans eqm.symm,?_⟩
  change orbit h (step x)=u
  rw [next]; exact orbit_pad h u

/-- A multiplicative error at most 2/K translates to an additive phase
error at most 1/Q at the chosen scales. -/
private theorem log_error {x M K Q : ℝ} (xp : 0<x) (mp : 0<M) (qp : 0<Q)
    (budget : 4*Q+2≤K) (upper : x≤M) (lower : K*(M-x)≤2*M) :
    |logb 2 x-logb 2 M|≤1/Q := by
  have lp : 0<Real.log 2 := Real.log_pos (by norm_num)
  have lo : logb 2 x≤logb 2 M := (logb_le_logb (by norm_num) xp mp).mpr upper
  rw [abs_of_nonpos (by linarith : logb 2 x-logb 2 M≤0)]
  have sel : 2*Q*(M-x)≤x := by
    nlinarith [mul_nonneg (sub_nonneg.mpr budget) (sub_nonneg.mpr upper)]
  have ub := Real.log_le_sub_one_of_pos (div_pos mp xp)
  have aux : M/x-1≤1/(2*Q) := by
    apply (le_div_iff₀ (by positivity)).mpr
    apply le_of_mul_le_mul_right (a:=x) _ xp
    field_simp; nlinarith only [sel]
  have diff : Real.log M-Real.log x≤1/(2*Q) := by rw [← Real.log_div mp.ne' xp.ne']; exact ub.trans aux
  have half := log_two_bounds.1
  change -(Real.log x/Real.log 2-Real.log M/Real.log 2)≤1/Q
  rw [show -(Real.log x/Real.log 2-Real.log M/Real.log 2)=(Real.log M-Real.log x)/Real.log 2 by ring]
  apply (div_le_iff₀ lp).mpr
  apply diff.trans
  calc 1/(2*Q) = (1/Q)*(1/2) := by ring
       _ ≤ _ := mul_le_mul_of_nonneg_left half (by positivity)

private theorem bernoulli (Q : Nat) : 1+(Q:ℝ)/2≤(3/2:ℝ)^Q := by
  induction Q with
  | zero => norm_num
  | succ Q ih => push_cast; rw [pow_succ]; linarith [show (0:ℝ)≤Q by positivity]

private theorem scale (Q : Nat) (hq : 5≤Q) : 4*Q+2≤2^Q := by
  induction Q, hq using Nat.le_induction with
  | base => decide
  | succ j h ih => rw [pow_succ]; omega


/-- One inverse row, including its ordinary path, normalized logarithmic
phase, geometric upper bound and the location of the postdescent endpoint. -/
private theorem row_entry (Q q s : Nat) (sq : s≤Q) (unit : q%3≠0) (big : 4*Q+2≤2^Q)
    (qp : 0<Q) (small : (q:ℝ)≤(3/2:ℝ)^Q) :
    ∃ x e u : Nat, 0<x ∧ x%2=1 ∧ Q≤e ∧ 2^Q*q≤u ∧ 3*x+1=2^e*u ∧
      orbit e x=u ∧ Hits u q ∧ x<2^(5*Q) ∧ ∃ E : ℤ,
        |height x-(height q-alpha-(s:ℝ)*alpha+E)|≤1/(Q:ℝ) := by
  let u := lift s (2^Q*q)
  obtain ⟨hit,ut,lo,hi⟩ := lift_spec s _ (unit_pad Q q unit)
  change orbit (4*s) u=2^Q*q at hit
  change u%3≠0 at ut
  change 16^s*(2^Q*q)+3^s ≤ 3^s*u+16^s at lo
  change 3^s*u ≤ 16^s*(2^Q*q) at hi
  obtain ⟨e,x,eq,eu,xp,xo,link,px⟩ := odd_predecessor ut qp
  have qpos : 0<q := by omega
  have upos : 0<u := by omega
  have Kpos : (0:ℝ)<2^Q := by positivity
  have Spos : (0:ℝ)<3^s := by positivity
  let G := (16/3:ℝ)^s
  let K := (2:ℝ)^Q
  let H := (2:ℝ)^e
  have gp : 0<G := by dsimp [G]; positivity
  have Gone : 1≤G := one_le_pow₀ (by norm_num)
  have hpos : 0<H := by dsimp [H]; positivity
  have hone : 1≤H := one_le_pow₀ (by norm_num)
  have kone : 1≤K := one_le_pow₀ (by norm_num)
  have qr : (1:ℝ)≤q := by exact_mod_cast qpos
  have li : 3*(x:ℝ)+1=H*u := by dsimp [H]; exact_mod_cast link
  have l : G*(K*q-1)+1≤u := by
    dsimp [G,K]; rw [div_pow]
    apply le_of_mul_le_mul_right (a:=(3:ℝ)^s) _ Spos
    have cold : (16:ℝ)^s*((2:ℝ)^Q*q)+3^s ≤ 3^s*u+16^s := by exact_mod_cast lo
    field_simp; linarith only [cold]
  have h : (u:ℝ)≤G*(K*q) := by
    dsimp [G,K]; rw [div_pow]
    apply le_of_mul_le_mul_right (a:=(3:ℝ)^s) _ Spos
    have hot : (3:ℝ)^s*u ≤ (16:ℝ)^s*((2:ℝ)^Q*q) := by exact_mod_cast hi
    field_simp; linarith only [hot]
  have uq : 2^Q*q≤u := by
    have kq : 1≤K*(q:ℝ) := one_le_mul_of_one_le_of_one_le kone qr
    have l' : K*(q:ℝ)≤(u:ℝ) := by nlinarith [mul_nonneg (sub_nonneg.mpr Gone) (sub_nonneg.mpr kq)]
    dsimp [K] at l'; exact_mod_cast l'
  let M := H*G*(K*q)/3
  have mp : 0<M := by dsimp [M]; positivity
  have xl : (x:ℝ)≤M := by dsimp [M]; nlinarith [mul_le_mul_of_nonneg_left h hpos.le]
  have B : (4:ℝ)*Q+2≤K := by dsimp [K]; exact_mod_cast big
  have pl : K*(M-x)≤2*M := by
    have qg : H*G≤H*G*(q:ℝ) := by nlinarith [mul_nonneg (mul_nonneg hpos.le gp.le) (sub_nonneg.mpr qr)]
    have gh : 1≤H*G := one_le_mul_of_one_le_of_one_le hone Gone
    dsimp only [M]
    nlinarith [mul_nonneg Kpos.le (sub_nonneg.mpr (mul_le_mul_of_nonneg_left l hpos.le)),
      mul_nonneg Kpos.le (sub_nonneg.mpr qg), mul_nonneg Kpos.le (sub_nonneg.mpr hone)]
  have logerr := log_error (x:=(x:ℝ)) (M:=M) (K:=K) (Q:=(Q:ℝ))
    (by positivity) mp (by positivity) B xl pl
  let E : ℤ := (Q:ℤ)+e+4*s
  have lv : logb 2 M=height q-alpha-(s:ℝ)*alpha+E := by
    have cz : (q:ℝ)≠0 := by positivity
    have h16 : logb 2 (16:ℝ)=4 := by rw [show (16:ℝ)=2^4 by norm_num,logb_pow,logb_two]; norm_num
    have hG : logb 2 G=(s:ℝ)*(4-alpha) := by
      dsimp only [G,alpha]; rw [logb_pow,logb_div (by norm_num) (by norm_num),h16]
    dsimp only [M]; rw [logb_div (by positivity) (by norm_num),
      logb_mul (mul_ne_zero hpos.ne' gp.ne') (mul_ne_zero Kpos.ne' cz),
      logb_mul hpos.ne' gp.ne',logb_mul Kpos.ne' cz,hG]
    dsimp only [H,K,height,alpha,E]; rw [logb_pow,logb_pow,logb_two]; push_cast; ring
  have bound : (x:ℝ)<(2:ℝ)^(5*Q) := by
    have gq : G≤(16/3:ℝ)^Q := pow_le_pow_right₀ (by norm_num) sq
    have hp : H≤(2:ℝ)^(Q+1) := pow_le_pow_right₀ (by norm_num) eu
    have tot : H*G*(K*(q:ℝ))≤(2:ℝ)^(Q+1)*(16/3:ℝ)^Q*(K*(3/2:ℝ)^Q) :=
      mul_le_mul (mul_le_mul hp gq gp.le (by positivity))
        (mul_le_mul_of_nonneg_left small Kpos.le) (by positivity) (by positivity)
    have powid : (2:ℝ)^(Q+1)*(16/3:ℝ)^Q*(K*(3/2:ℝ)^Q)=2*(2:ℝ)^(5*Q) := by
      dsimp only [K]; rw [pow_succ]; rw [pow_mul]
      rw [show (2:ℝ)^5=2*(16/3)*(2*(3/2)) by norm_num]; simp only [mul_pow]; ring
    rw [powid] at tot; dsimp only [M] at xl
    nlinarith [show (0:ℝ)<2^(5*Q) by positivity]
  refine ⟨x,e,u,xp,xo,eq,uq,link,px,Hits.trans ⟨4*s,hit⟩ ⟨Q,orbit_pad Q q⟩,by exact_mod_cast bound,E,?_⟩
  change |logb 2 (x:ℝ)-_|≤_; rwa [lv] at logerr

/-- Arbitrarily large marked representatives of the same fixed target. The
first return endpoint and original target remain individually specified. -/
theorem cofinal_marked_power_predecessors (q L : Nat) (unit : q%3≠0) :
    ∃ x e u : Nat, L<x ∧ Marked x ∧ x.log2+1≤5*e ∧
      3*x+1=2^e*u ∧ orbit e x=u ∧ Hits u q ∧ u^5≤4^5*x^4 ∧ q≤u := by
  let cutoff := 10+2*q+4*L
  obtain ⟨a,Q,qp,qn,cop,cost,near⟩ := rotation_grid (4^cutoff) (by positivity)
  have bigger : cutoff<Q := by
    by_contra! opp
    have h := Nat.pow_le_pow_right (by decide : 0<4) opp
    omega
  have big : 4*Q+2≤2^Q := scale Q (by dsimp [cutoff] at bigger; omega)
  have small : (q:ℝ)≤(3/2:ℝ)^Q := by
    have h : 2*q≤Q := by dsimp [cutoff] at bigger; omega
    have hr : 2*(q:ℝ)≤Q := by exact_mod_cast h
    linarith [bernoulli Q]
  have R (t : Nat) := row_entry Q q (min t Q) (Nat.min_le_right _ _) unit big qp small
  choose X e u hr using R
  have near' : |(Q:ℝ)*alpha-a|≤1/(Q:ℝ) := near.trans (by
    apply one_div_le_one_div_of_le (by positivity)
    have h : (Q:ℝ)≤((4^cutoff:Nat):ℝ) := by exact_mod_cast qn
    linarith)
  obtain ⟨s,sq,marked_section⟩ := section_of_inverse_row qp cop near' (height q-alpha) X
    (fun t _ => (hr t).1) (by
      intro t _; obtain ⟨xp,_,_,_,_,_,_,upper,_⟩ := hr t
      have digits := (Nat.log2_lt (Nat.ne_of_gt xp)).mpr upper
      exact_mod_cast (show (X t).log2+1≤5*Q by omega)) (by
      intro t tq; obtain ⟨_,_,_,_,_,_,_,_,E,hE⟩ := hr t
      exact ⟨E,by simpa only [Nat.min_eq_left tq] using hE⟩)
  obtain ⟨xp,xo,eq,uq,link,px,hit,bound,_⟩ := hr s
  have digits := (Nat.log2_lt (Nat.ne_of_gt xp)).mpr bound
  have bigq : 2^Q≤u s := by
    apply le_trans _ uq; exact Nat.le_mul_of_pos_right _ (by omega)
  have up : u s≤3*X s+1 := by rw [link]; exact Nat.le_mul_of_pos_left _ (by positivity)
  have xb : L<X s := by
    have h := Nat.lt_two_pow_self (n:=Q)
    dsimp [cutoff] at bigger
    omega
  have more : Q*5≤e s*5 := Nat.mul_le_mul_right _ eq
  have d : (X s).log2+1≤5*e s := by omega
  have cl : X s<2^(5*e s) := (Nat.log2_lt xp.ne').mp (by omega)
  have target_le : q≤u s := (Nat.le_mul_of_pos_left _ (by positivity : 0<2^Q)).trans uq
  exact ⟨X s,e s,u s,xb,⟨xo,marked_section⟩,d,link,px,hit,inverse_power_cost xp cl link (Nat.le_refl _),target_le⟩

/-- The cofinal sparse-source test for global convergence. Divisibility is
formulated by an existential clock so no valuation convention is required. -/
theorem universal_iff_marked_power : Universal ↔ ∀ x : Nat,
    Marked x → (∃ e u : Nat, x.log2+1≤5*e ∧ 3*x+1=2^e*u) → Basin x := by
  constructor
  · intro all x marked _; exact all x (by have := marked.1; omega)
  · intro all; apply universal_of_units; intro q unit
    obtain ⟨x,e,u,_,marked,exponent,link,px,hit,_,_⟩ := cofinal_marked_power_predecessors q 0 unit
    exact (basin_at_hit (Hits.trans ⟨e,px⟩ hit)).mp (all x marked ⟨e,u,exponent,link⟩)

#print axioms cofinal_marked_power_predecessors
#print axioms universal_iff_marked_power
#print axioms odd_predecessor
end CollatzShell.MarkedCylinders
