import CollatzGlobal.Coverage

open CollatzReverseBasin

namespace CollatzGlobal

private theorem shortcut_even_value (u : Nat) : shortcut (2*u)=u := by
  simp [shortcut]

private theorem shortcut_odd_pred (u : Nat) (hu : 0<u) :
    shortcut (2*u-1)=3*u-1 := by
  unfold shortcut
  split <;> omega

/-- Exact finite rising word in ordinary integers. -/
theorem ordinary_odd_rise (b u : Nat) (hu : 0<u) :
    orbit (2^b*u-1) b = 3^b*u-1 := by
  induction b generalizing u with
  | zero => simp [orbit]
  | succ b ih =>
    have hv : 0<2^b*u := Nat.mul_pos (Nat.two_pow_pos b) hu
    have heq : 2^(b+1)*u = 2*(2^b*u) := by rw [Nat.pow_succ]; grind
    rw [heq, orbit, shortcut_odd_pred _ hv]
    have heq2 : 3*(2^b*u)-1 = 2^b*(3*u)-1 := by grind
    rw [heq2, ih (3*u) (by omega)]
    rw [Nat.pow_succ]
    grind

private theorem power_two_halvings (a t : Nat) :
    orbit (2^(a+t)) t = 2^a := by
  induction t generalizing a with
  | zero => simp [orbit]
  | succ t ih =>
    have eq : 2^(a+(t+1)) = 2*(2^(a+t)) := by
      rw [show a+(t+1)=(a+t)+1 by omega,Nat.pow_succ]
      grind
    rw [eq, orbit, shortcut_even_value]
    exact ih a

theorem ordinary_power_two_orbit (a t : Nat) (ht : t≤a) :
    orbit (2^a) t = 2^(a-t) := by
  have h := power_two_halvings (a-t) t
  have e : a-t+t=a := by omega
  rwa [e] at h

theorem ordinary_odd_rise_partial (b t : Nat) (ht : t≤b) :
    orbit (2^b-1) t = 3^t*2^(b-t)-1 := by
  have eq : 2^t*2^(b-t)=2^b := by rw [← Nat.pow_add]; congr 1; omega
  have h := ordinary_odd_rise t (2^(b-t)) (Nat.two_pow_pos _)
  rwa [eq] at h

/-- Prefixes for the entire singular rank-five family in psi coordinates. -/
theorem singular_psi_prefixes (m q a : Nat)
    (hm : 3*m=16*q+1) (hq : 3*q+1=16*2^a) :
    orbit (3*m-1) 5 = 2^(a+3) ∧
    orbit m 3 = 2^(a+5)-1 ∧
    (∀ t : Fin 5, 0<t.val → orbit (3*m-1) t.val < orbit m t.val) := by
  have hp := Nat.two_pow_pos a
  have qpos : 0<q := by omega
  have qodd : q%2=1 := by omega
  have s0 : 3*m-1=16*q := by omega
  have mstep : shortcut m=8*q+1 := by unfold shortcut; split <;> omega
  have r2 : shortcut (8*q+1)=12*q+2 := by unfold shortcut; split <;> omega
  have r3 : shortcut (12*q+2)=6*q+1 := by unfold shortcut; split <;> omega
  have r4 : shortcut (6*q+1)=9*q+2 := by unfold shortcut; split <;> omega
  have sq : shortcut q=8*2^a := by unfold shortcut; split <;> omega
  have s16 : shortcut (16*q)=8*q := by simpa [← Nat.mul_assoc] using shortcut_even_value (8*q)
  have s8 : shortcut (8*q)=4*q := by simpa [← Nat.mul_assoc] using shortcut_even_value (4*q)
  have s4 : shortcut (4*q)=2*q := by simpa [← Nat.mul_assoc] using shortcut_even_value (2*q)
  have s2 : shortcut (2*q)=q := shortcut_even_value q
  constructor
  · simp only [s0,orbit,s16,s8,s4,s2,sq]
    rw [Nat.pow_add]
    simp
    grind
  constructor
  · simp only [orbit,mstep,r2,r3]
    rw [Nat.pow_add]
    simp
    omega
  · intro t ht
    have hsmall := t.isLt
    have cases : t.val=1 ∨ t.val=2 ∨ t.val=3 ∨ t.val=4 := by omega
    rcases cases with h | h | h | h <;>
      simp only [h,s0,orbit,mstep,r2,r3,r4,s16,s8,s4,s2] <;> omega

/-- Every member of this infinite algebraic family is a certified source and
an actual finite psi residual; no same-goal forward return can act on it. -/
theorem singular_psi_residual (m q a : Nat)
    (hm : 3*m=16*q+1) (hq : 3*q+1=16*2^a) :
    orbit (3*m-1) (a+8) = 1 ∧ FinitePsiResidual m (a+8) := by
  obtain ⟨hs,hr,hearly⟩ := singular_psi_prefixes m q a hm hq
  have hmpos : 0<m := by omega
  have hspos : 0<3*m-1 := by have := Nat.two_pow_pos a; omega
  constructor
  · rw [show a+8=5+(a+3) by omega,orbit_add,hs]
    rw [ordinary_power_two_orbit (a+3) (a+3) (by omega)]
    simp
  · intro t ht htd hreturn
    unfold PsiReturn at hreturn
    have ordered : orbit (3*m-1) t < orbit m t := by
      by_cases hsmall : t<5
      · exact hearly ⟨t,hsmall⟩ ht
      · let v := t-5
        have tv : t=5+v := by dsimp [v]; omega
        have vbound : v≤a+3 := by dsimp [v]; omega
        have source : orbit (3*m-1) t=2^(a+3-v) := by
          rw [tv,orbit_add,hs,ordinary_power_two_orbit _ _ vbound]
        have target : orbit m t=3^(v+2)*2^(a+3-v)-1 := by
          rw [show t=3+(v+2) by omega,orbit_add,hr]
          rw [ordinary_odd_rise_partial (a+5) (v+2) (by omega)]
          have eq : a+5-(v+2)=a+3-v := by omega
          rw [eq]
        rw [source,target,Nat.pow_add]
        have htwo : 0<2^(a+3-v) := Nat.two_pow_pos _
        have hthree : 0<3^v := Nat.pow_pos (by decide)
        have hmul : 2^(a+3-v) ≤ 3^v*2^(a+3-v) := by
          have h := Nat.mul_le_mul_right (2^(a+3-v)) (show 1≤3^v by omega)
          simpa using h
        have eq : (3^v*3^2)*2^(a+3-v)=9*(3^v*2^(a+3-v)) := by grind
        rw [eq]
        omega
    have hpositive := orbit_positive hspos t
    omega


/-- The exact rank-five parameter equation supplies both a complete ordinary
source certificate and a residual missed by every fixed negative guard. -/
theorem rank_five_psi_residual (M e : Nat) (he : 5≤e)
    (h : 243*M+22=8*2^e) :
    orbit (3*(27*M+1)-1) (e+3)=1 ∧
    FinitePsiResidual (27*M+1) (e+3) ∧ M%2048≠2047 := by
  let a := e-5
  let q := (81*M+2)/16
  have heq : e=a+5 := by dsimp [a]; omega
  have epow : 2^e=32*2^a := by rw [heq,Nat.pow_add]; simp; grind
  rw [epow] at h
  have qeq : 81*M+2=16*q := by dsimp [q]; omega
  have hm : 3*(27*M+1)=16*q+1 := by omega
  have hq : 3*q+1=16*2^a := by omega
  have answer := singular_psi_residual (27*M+1) q a hm hq
  have clock : a+8=e+3 := by omega
  rw [clock] at answer
  exact ⟨answer.1,answer.2,rank_five_parameter_misses_negative_guard M e (by rwa [epow])⟩


/-- Integral recurrence for the entire original exponent progression; division
is used only in two fixed, kernel-evaluated integer constants. -/
def hardParameter : Nat → Nat
  | 0 => (8*2^119-22)/243
  | j+1 => 2^162*hardParameter j + (22*(2^162-1))/243

theorem hard_parameter_equation (j : Nat) :
    243*hardParameter j+22=8*2^(119+162*j) := by
  induction j with
  | zero => decide
  | succ j ih =>
    have carry : 243*((22*(2^162-1))/243)+22=22*2^162 := by decide
    calc
      243*hardParameter (j+1)+22 = 2^162*(243*hardParameter j+22) := by
        rw [hardParameter]
        grind
      _ = 2^162*(8*2^(119+162*j)) := by rw [ih]
      _ = 8*2^(119+162*(j+1)) := by
        have he : 119+162*(j+1)=162+(119+162*j) := by omega
        rw [he,Nat.pow_add]
        grind

theorem hard_parameter_large (j : Nat) : j < hardParameter j := by
  induction j with
  | zero => decide
  | succ j ih =>
    have factor : 0<2^162 := Nat.two_pow_pos _
    have carry : 0<(22*(2^162-1))/243 := by decide
    have hmul : hardParameter j ≤ 2^162*hardParameter j := by
      have h := Nat.mul_le_mul_right (hardParameter j) (show 1≤2^162 by omega)
      simpa using h
    rw [hardParameter]
    omega

/-- Cofinal family of actual certified residuals missed by all bounded-witness
same-goal forward returns and by every one of the eight negative guards. -/
theorem hard_psi_family (j : Nat) :
    let M := hardParameter j
    let e := 119+162*j
    j<M ∧ M%4=2 ∧
    orbit (3*(27*M+1)-1) (e+3)=1 ∧
    FinitePsiResidual (27*M+1) (e+3) ∧ M%2048≠2047 := by
  dsimp
  have h := hard_parameter_equation j
  have result := rank_five_psi_residual (hardParameter j) (119+162*j) (by omega) h
  exact ⟨hard_parameter_large j,rank_five_parameter_mod_four _ _ h,
    result.1,result.2.1,result.2.2⟩

end CollatzGlobal
