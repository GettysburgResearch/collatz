import OrdinaryDerivative

/-! Finite modular squaring carries the logarithmic unit to every original
positive integer in the stated bands. Compare PR197, LogTowerCore.lean,
for the earlier normalized-power method at a different clock and gap. -/
namespace Collatz.OrdinaryPower
open Collatz.SourceDeletion Collatz.MinimumFailure Collatz.OrdinaryDerivative

set_option maxRecDepth 20000
set_option maxHeartbeats 2000000
set_option exponentiation.threshold 10000

private def deriv : Nat → Nat
  | 0 => (3^162-1)/8
  | s+1 => deriv s + 2^(s+2)*(deriv s)^2

private def digit : Nat → Nat
  | 0 => ((3^162-1)/8)%2^64
  | s+1 => (digit s + 2^(s+2)*(digit s)^2)%2^64

private theorem expansion (s : Nat) : (3^162:Nat)^(2^s)=1+2^(s+3)*deriv s := by
  induction s with
  | zero => decide
  | succ s ih =>
    rw [pow_succ (2:Nat) s,pow_mul,ih,deriv]
    rw [show s+1+3=(s+2)+2 by omega,show s+3=(s+2)+1 by omega,pow_add,pow_succ]
    ring

private theorem agreement (s : Nat) : deriv s ≡ digit s [MOD 2^64] := by
  induction s with
  | zero => simp [deriv,digit,Nat.ModEq]
  | succ s ih =>
    change (deriv s+2^(s+2)*(deriv s)^2)%2^64 =
        ((digit s+2^(s+2)*(digit s)^2)%2^64)%2^64
    rw [Nat.mod_mod]
    exact ih.add ((ih.pow 2).mul_left _)

private theorem stable (s : Nat) (large : 62≤s) : deriv s ≡ derivativeResidue [MOD 2^64] := by
  obtain ⟨t,rfl⟩:=Nat.exists_eq_add_of_le large
  clear large
  induction t with
  | zero =>
    have eqn : digit 62=derivativeResidue := by decide +kernel
    simpa only [Nat.add_zero,eqn] using agreement 62
  | succ t ih =>
    apply Nat.ModEq.trans _ ih
    change deriv (62+t)+2^(62+t+2)*(deriv (62+t))^2 ≡ deriv (62+t) [MOD 2^64]
    exact Nat.add_modEq_left_iff.mpr (dvd_mul_of_dvd_left (pow_dvd_pow 2 (by omega)) _)

private theorem linear_unit (s d v : Nat) (high : 64≤s) :
    ∃ u, (1+2^s*d)^v=1+2^s*u ∧ u ≡ v*d [MOD 2^64] := by
  induction v with
  | zero => exact ⟨0,by simp,by simp [Nat.ModEq]⟩
  | succ v ih =>
    obtain ⟨u,eu,cu⟩:=ih
    refine ⟨u+d+2^s*u*d,by rw [pow_succ,eu];ring,?_⟩
    rw [Nat.succ_mul]
    apply Nat.ModEq.trans _ (cu.add_right d)
    exact Nat.add_modEq_left_iff.mpr <| dvd_mul_of_dvd_left
      (dvd_mul_of_dvd_left (pow_dvd_pow 2 high) _) _

theorem normalized_unit (r v : Nat) (large : 43≤r) :
    ∃ u, 3^(162*(2^(2*r)*v))=1+2^(2*r+3)*u ∧ u ≡ v*derivativeResidue [MOD 2^64] := by
  obtain ⟨u,eu,cu⟩:=linear_unit (2*r+3) (deriv (2*r)) v (by omega)
  refine ⟨u,?_,cu.trans ((stable (2*r) (by omega)).mul_left _)⟩
  rw [show 162*(2^(2*r)*v)=162*2^(2*r)*v by ring,pow_mul,pow_mul,expansion,eu]

theorem all_in_band (r v : Nat) (large : 43≤r) (unit : 3^r*v ≡ 1 [MOD 2^64]) :
    let s:=162*(2^(2*r)*v)
    run (2*r+67) (3^(11+s)-1)=run (2*r+67) (3^(6+s)-1) := by
  obtain ⟨u,eqn,con⟩:=normalized_unit r v large
  apply physical_log_meeting r _ u large eqn
  have a:=con.mul_left (3^r)
  have b:=unit.mul_right derivativeResidue
  simpa only [←Nat.mul_assoc,Nat.one_mul] using a.trans (by simpa only [Nat.mul_assoc,Nat.one_mul] using b)

theorem negative_band (r v : Nat) (large : 43≤r) (unit : 3^r*v ≡ 2^62-1 [MOD 2^62]) :
    let s:=162*(2^(2*r)*v)
    run (2*r+65) (3^(11+s)-1)=run (2*r+65) (3^(6+s)-1) := by
  obtain ⟨u,eqn,con⟩:=normalized_unit r v large
  apply negative_log_meeting r _ u large eqn
  have reduced := con.of_dvd (pow_dvd_pow 2 (by decide : 62≤64))
  have a:=reduced.mul_left (3^r)
  have b:=unit.mul_right derivativeResidue
  have neg : (2^62-1)*derivativeResidue ≡ negativeResidue [MOD 2^62] := by decide
  exact a.trans (by simpa only [Nat.mul_assoc] using b.trans neg)

private theorem odd_rotation (b k : Nat) (odd : b%2=1) :
    ∃ c : Nat, b^(2^(k+1))=1+2^(k+3)*c := by
  induction k with
  | zero =>
    have t : b^2%8=1 := by
      rw [Nat.pow_mod]
      rcases (show b%8=1 ∨ b%8=3 ∨ b%8=5 ∨ b%8=7 by omega) with v|v|v|v <;> rw [v]
    exact ⟨b^2/8,by change b^2 = 1+8*(b^2/8);omega⟩
  | succ k ih =>
    obtain ⟨c,e⟩:=ih
    refine ⟨c+2^(k+2)*c^2,?_⟩
    rw [pow_succ (2:Nat) (k+1),pow_mul,e,
      show k+1+3=(k+2)+2 by omega,show k+3=(k+2)+1 by omega,pow_add,pow_succ]
    ring

private theorem rotated_multiple (b k v : Nat) (odd : b%2=1) :
    b^(2^(k+1)*v) ≡ 1 [MOD 2^(k+3)] := by
  obtain ⟨c,e⟩:=odd_rotation b k odd
  have one : b^(2^(k+1)) ≡ 1 [MOD 2^(k+3)] := by rw [e];simp [Nat.ModEq]
  simpa only [pow_mul,one_pow] using one.pow v

private theorem factor_twos (b : Nat) (bp : 0<b) :
    ∃ a c : Nat, c%2=1 ∧ b=2^a*c := by
  induction b using Nat.strong_induction_on with
  | h b ih =>
    by_cases odd : b%2=1
    · exact ⟨0,b,odd,by simp⟩
    obtain ⟨a,c,co,e⟩:=ih (b/2) (by omega) (by omega)
    exact ⟨a+1,c,co,by rw [pow_succ,show 2^a*2*c=2*(2^a*c) by ring,←e];omega⟩

private theorem even_coordinates (b d : Nat) (bp : 0<b) (be : b%2=0) (hi : 63≤d) :
    ∃ r v : Nat, 43≤r ∧ b^(2^d)=2^(2*r)*v ∧ 3^r*v ≡ 1 [MOD 2^64] := by
  obtain ⟨a,c,co,e⟩:=factor_twos b bp
  have ap : 1≤a := by
    by_contra! f
    have az : a=0 := by omega
    rw [az,pow_zero,one_mul] at e
    omega
  obtain ⟨k,dk⟩:=Nat.exists_eq_add_of_le hi
  let r:=(2:Nat)^62*(2^k*a)
  let v:=c^(2^d)
  have cp : 1≤(2:Nat)^k := Nat.two_pow_pos k
  have large : 43≤r := calc
    43 ≤ (2:Nat)^62 := by decide
    _ ≤ r := by
      have mul := Nat.mul_le_mul cp ap
      change (2:Nat)^62≤2^62*(2^k*a)
      simpa only [Nat.one_mul,Nat.mul_one] using Nat.mul_le_mul_left (2^62) mul
  have dsplit : (2:Nat)^d=2^62*(2*2^k) := by rw [dk,pow_add];ring
  have re : a*(2:Nat)^d=2*r := by rw [dsplit];dsimp [r];ring
  have form : b^(2^d)=2^(2*r)*v := by rw [e,mul_pow,←pow_mul,re]
  have vr : v ≡ 1 [MOD 2^64] := by
    dsimp [v];rw [dsplit]
    exact rotated_multiple c 61 (2*2^k) co
  have rr : 3^r ≡ 1 [MOD 2^64] := rotated_multiple 3 61 (2^k*a) (by decide)
  have lock : 3^r*v ≡ 1 [MOD 2^64] := by simpa using rr.mul vr
  exact ⟨r,v,large,form,lock⟩

/-- Every positive even base, with no ternary restriction, at every
exponent divisible by 2^63. -/
theorem even_power (b d : Nat) (bp : 0<b) (be : b%2=0) (hi : 63≤d) :
    let m:=b^(2^d)
    ∃ r, 43≤r ∧ run (2*r+67) (3^(11+162*m)-1)=run (2*r+67) (3^(6+162*m)-1) := by
  obtain ⟨r,v,large,form,lock⟩:=even_coordinates b d bp be hi
  exact ⟨r,large,by rw [form];exact all_in_band r v large lock⟩

/-- The ordinary multiplier is supplied in advance. Both signs are funded
at the same earlier Mersenne exponent, five below the source. -/
theorem even_signed_multiple (b d c : Nat) (bp : 0<b) (be : b%2=0) (hi : 63≤d)
    (sign : c ≡ 1 [MOD 2^64] ∨ c ≡ 2^62-1 [MOD 2^62]) :
    let m:=b^(2^d)*c
    ∃ H, run H (3^(11+162*m)-1)=run H (3^(6+162*m)-1) := by
  obtain ⟨r,v,large,form,lock⟩:=even_coordinates b d bp be hi
  have mul : b^(2^d)*c=2^(2*r)*(v*c) := by rw [form,Nat.mul_assoc]
  rcases sign with pos|neg
  · refine ⟨2*r+67,?_⟩
    rw [mul]
    apply all_in_band _ _ large
    simpa only [Nat.mul_assoc,Nat.one_mul] using lock.mul pos
  · refine ⟨2*r+65,?_⟩
    rw [mul]
    apply negative_band _ _ large
    have short := lock.of_dvd (pow_dvd_pow 2 (by decide : 62≤64))
    simpa only [Nat.mul_assoc,Nat.one_mul] using short.mul neg

theorem odd_power (b d : Nat) (bo : b%2=1) (hi : 494≤d) :
    ∃ v, b^(2^d)=1+2^496*v ∧
      run 499 (3^(11+162*b^(2^d))-1)=run 499 (3^(2+162*b^(2^d))-1) := by
  obtain ⟨k,dk⟩:=Nat.exists_eq_add_of_le hi
  have ml : b^(2^d) ≡ 1 [MOD 2^496] := by
    rw [dk,pow_add];exact rotated_multiple b 493 (2^k) bo
  let v:=b^(2^d)/2^496
  have val : b^(2^d)=1+2^496*v := by
    change b^(2^d)%2^496=1%2^496 at ml
    exact (Nat.mod_add_div _ (2^496)).symm.trans (by rw [ml];rfl)
  let s:=162*(2^496*v)
  have sr : 3^s ≡ 1 [MOD 2^499] := by
    change (3:Nat)^(162*(2^496*v)) ≡ 1 [MOD 2^499]
    rw [show 162*(2^496*v)=2^497*(81*v) by ring]
    exact rotated_multiple 3 496 (81*v) (by decide)
  have eqn : 3^s=1+2^499*(3^s/2^499) := by
    change 3^s%2^499=1%2^499 at sr
    exact (Nat.mod_add_div _ (2^499)).symm.trans (by rw [sr];rfl)
  refine ⟨v,val,?_⟩
  rw [val,show 11+162*(1+2^496*v)=173+s by dsimp [s];ring,
    show 2+162*(1+2^496*v)=164+s by dsimp [s];ring]
  exact odd_anchor_meeting _ _ eqn

/-- Every degree divisible by 2^494 has the same 499-clock bound on
all ordinary odd bases. -/
theorem odd_degree_meeting (b n : Nat) (odd : b%2=1) (degree : 2^494∣n) :
    run 499 (3^(11+162*b^n)-1)=run 499 (3^(2+162*b^n)-1) := by
  obtain ⟨k,hk⟩:=degree
  have form : b^n=(b^k)^(2^494) := by rw [←pow_mul,hk,Nat.mul_comm k]
  have bo : (b^k)%2=1 := by rw [Nat.pow_mod,odd,one_pow];decide
  obtain ⟨_,_,a⟩:=odd_power (b^k) 494 bo (by decide)
  simpa only [form] using a

/-- The actual canonical parent is good at every supplied perfect power
under its bounded-branch floor. The proof works already at 2^63 for an
even base and 2^494 for an arbitrary base. -/
theorem power_parent (b d z : Nat) (degree : 494≤d ∨ (b%2=0 ∧ 63≤d))
    (shape : 81*z+271=128*2^(11+162*b^(2^d)))
    (floor : ∀ w, 0<w → 1024*w<243*z → Good w) : Good z := by
  by_cases bz : b=0
  · subst b
    rw [zero_pow (Nat.ne_of_gt (Nat.two_pow_pos d))] at shape
    have zz : z=3233 := by norm_num at shape;omega
    subst z
    exact ⟨107,by decide⟩
  by_cases bo : b%2=1
  · obtain ⟨v,_,meet⟩:=odd_power b d bo (by omega)
    exact floor_return _ _ _ 499 (by omega) (by omega) (by omega) shape floor meet
  · obtain ⟨r,_,meet⟩:=even_power b d (by omega) (by omega) (by omega)
    exact floor_return _ _ _ _ (by omega) (by omega) (by omega) shape floor meet

#print axioms normalized_unit
#print axioms all_in_band
#print axioms negative_band
#print axioms even_signed_multiple
#print axioms even_power
#print axioms odd_power
#print axioms odd_degree_meeting
#print axioms power_parent
end Collatz.OrdinaryPower
