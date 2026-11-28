import FiveLadder
import PhaseMultiples

/-! Near-fast first visits preserving the comparison of y and 5y.
Both grade and physical clock are independently marked. -/
set_option autoImplicit false
set_option warningAsError true

namespace Collatz.FiveWindow
open TwoGapRouting FiveRouting FiveLadder

private theorem calibrate {P T A y ε : ℝ} (pp : 0<P) (tp : 0<T) (ep : 0<ε) (yp : 1≤y)
    (cal : 64*(1+ε)≤ε*P) (loss : P*(T*y)≤P*A+64*T) : T*y≤(1+ε)*A := by
  have one : 0<1+ε := by linarith
  have a : P*(T*y-A)≤64*T := by linarith only [loss]
  have r : P*((1+ε)*(T*y-A))≤P*(ε*(T*y)) := by
    calc
      _ = (1+ε)*(P*(T*y-A)) := by ring
      _ ≤ (1+ε)*(64*T) := mul_le_mul_of_nonneg_left a one.le
      _ = (64*(1+ε))*T := by ring
      _ ≤ (ε*P)*T := mul_le_mul_of_nonneg_right cal tp.le
      _ ≤ (ε*P)*T*y := le_mul_of_one_le_right (by positivity) yp
      _ = _ := by ring
  have h:=le_of_mul_le_mul_left r pp
  nlinarith only [h]

private theorem slack_nat {L y x S g : ℕ} (lp : 20≤L) (yu : y%3≠0)
    (slack : 2^S*weight L y≤3^g*weight L x) :
    2^L*(2^S*y)≤2^L*(3^g*x)+64*2^S := by
  have start : 64≤2^L := (by decide : 64≤2^20).trans (Nat.pow_le_pow_right (by decide) lp)
  have enough:=Nat.le_mul_of_pos_right (2^L) (show 0<y by omega)
  have sum : weight L y+64=2^L*y := by dsimp [weight]; omega
  have le : weight L x≤2^L*x := Nat.sub_le _ _
  have a:=congrArg (fun k:ℕ => 2^S*k) sum
  have b:=Nat.mul_le_mul_left (3^g) le
  nlinarith only [a,b,slack]

def Visitors (δ : ℝ) (M Q : ℕ) : Prop :=
  ∃ P K : ℝ, ∃G : ℕ, 0<P ∧ 0<K ∧ ∀y : ℕ, y%3≠0 → ∀X : ℝ, P*y≤X →
    ∀τ ρ : ℕ, ∃z m g : ℕ, 0<z ∧ z%3≠0 ∧ X≤z ∧ (z:ℝ)<(1+δ)*X ∧
      Flight m g z y ∧ g≤G ∧ (2:ℝ)^m*y≤K*z ∧ m ≡ τ [MOD M] ∧ g ≡ ρ [MOD Q]

theorem visitors (M Q : ℕ) (mp : 0<M) (qp : 0<Q) (δ : ℝ) (positive : 0<δ) :
    Visitors δ M Q := by
  let ε:=min (1:ℝ) (δ/4)
  have ep : 0<ε := lt_min (by norm_num) (by positivity)
  have small : ε≤1 := min_le_left _ _
  have width : ε≤δ/4 := min_le_right _ _
  have square : (1+ε)^2≤1+δ := by nlinarith [mul_nonneg ep.le (sub_nonneg.mpr small)]
  let k:=2*Q+1
  have kp : 0<k := by dsimp [k]; omega
  have km : k ≡ 1 [MOD Q] := by dsimp [k]; simp [Nat.ModEq]
  obtain ⟨J,mesh⟩:=PhaseNet.pow_ratio_net_multiples k Q M kp qp mp km ε ep
  obtain ⟨N,nLarge⟩:=exists_nat_gt (64*(1+ε)/ε)
  let L:=N+20
  have lp : 20≤L := by dsimp [L]; omega
  have pow : (N:ℝ)≤(2:ℝ)^L := by
    exact_mod_cast (show N≤2^L by have h : L<2^L:=Nat.lt_two_pow_self; dsimp [L] at h ⊢; omega)
  have cal : 64*(1+ε)≤ε*(2:ℝ)^L := by
    have h:=(div_lt_iff₀ ep).mp nLarge
    nlinarith only [mul_le_mul_of_nonneg_left pow ep.le,h]
  let B:=(L+54)*(Q*J)
  refine ⟨2^B,(1+ε)*3^(k*J),k*J,by positivity,by positivity,?_⟩
  intro y yu X onset τ ρ
  have yp : 0<y := by omega
  have yr : 1≤(y:ℝ) := by exact_mod_cast yp
  have ypositive : 0<(y:ℝ) := by positivity
  have base : (1:ℝ)≤2^B := one_le_pow₀ (by norm_num)
  have yx : (y:ℝ)≤X := (le_mul_of_one_le_left ypositive.le base).trans onset
  have xp : 0<X := ypositive.trans_le yx
  have enlarge : X≤(1+ε)*X := by linarith [mul_pos ep xp]
  let u:=(1+ε)*X/y
  have has : 1≤u := by dsimp [u]; apply (le_div_iff₀ ypositive).mpr; simpa using yx.trans enlarge
  obtain ⟨j,m,jb,gm,tm,below,above⟩:=mesh ρ τ u has
  let g:=k*j
  obtain ⟨a,S,au,sb,physical,upper,slack⟩:=seed L Q j y lp qp yu
  change Flight S g a y at physical
  change 3^g*a≤2^S*y at upper
  change 2^S*weight L y≤3^g*weight L a at slack
  have sB : S≤B := sb.trans (Nat.mul_le_mul_left _ (Nat.mul_le_mul_left Q jb))
  have three : 0<(3:ℝ)^g := by positivity
  have threeOne : 1≤(3:ℝ)^g := one_le_pow₀ (by norm_num)
  have bot : ((1+ε)*X)*3^g≤(2:ℝ)^m*y :=
    (div_le_div_iff₀ ypositive three).mp below.le
  have top : (2:ℝ)^m*y < ((1+ε)^2*X)*3^g := by
    have h:=(div_lt_iff₀ three).mp above
    dsimp [u] at h
    calc
      _ < ((1+ε)*((1+ε)*X/y)*3^g)*y := mul_lt_mul_of_pos_right h ypositive
      _ = _ := by field_simp
  have sPow : (2:ℝ)^S≤2^m := by
    apply (mul_le_mul_iff_left₀ ypositive).mp
    calc
      (2:ℝ)^S*y ≤ 2^B*y := mul_le_mul_of_nonneg_right (pow_le_pow_right₀ (by norm_num) sB) ypositive.le
      _ ≤ X := onset
      _ ≤ (1+ε)*X := enlarge
      _ ≤ (1+ε)*X*3^g := le_mul_of_one_le_right (by positivity) threeOne
      _ ≤ _ := bot
  have sm : S≤m := (pow_le_pow_iff_right₀ (by norm_num : 1<(2:ℝ))).mp sPow
  let lift:=m-S
  let z:=2^lift*a
  have lg : lift+S=m := by dsimp [lift]; omega
  have ap : 0<a := by omega
  have zp : 0<z := by dsimp [z]; positivity
  have fl : Flight m g z y := by
    simpa only [lg,Nat.zero_add] using (flight_halves lift a ap).join physical
  have zr : (z:ℝ)=2^lift*a := by dsimp [z]; norm_cast
  have scale : (2:ℝ)^m=2^lift*2^S := by rw [←lg,pow_add]
  have ru : (3:ℝ)^g*a≤2^S*y := by exact_mod_cast upper
  have rl : (2:ℝ)^L*(2^S*y)≤2^L*(3^g*a)+64*2^S := by exact_mod_cast slack_nat lp yu slack
  have low:=calibrate (by positivity : 0<(2:ℝ)^L) (by positivity : 0<(2:ℝ)^S) ep yr cal rl
  have liftPositive : 0≤(2:ℝ)^lift := by positivity
  have slow : (2:ℝ)^m*y≤(1+ε)*(3^g*z) := by
    rw [zr,scale]; nlinarith only [mul_le_mul_of_nonneg_left low liftPositive]
  have fast : (3:ℝ)^g*z≤2^m*y := by
    rw [zr,scale]; nlinarith only [mul_le_mul_of_nonneg_left ru liftPositive]
  have gb : g≤k*J := Nat.mul_le_mul_left k jb
  refine ⟨z,m,g,zp,unit_pow_mul lift au,?_,?_,fl,gb,?_,tm,gm⟩
  · apply (mul_le_mul_iff_left₀ (mul_pos (show 0<1+ε by positivity) three)).mp
    nlinarith only [bot,slow]
  · apply lt_of_lt_of_le _ (mul_le_mul_of_nonneg_right square xp.le)
    apply (mul_lt_mul_iff_left₀ three).mp
    nlinarith only [fast,top]
  · have p : (3:ℝ)^g≤3^(k*J) := pow_le_pow_right₀ (by norm_num) gb
    have z0 : 0≤(z:ℝ) := by positivity
    have a:=mul_le_mul_of_nonneg_right (mul_le_mul_of_nonneg_left p (show 0≤1+ε by positivity)) z0
    nlinarith only [a,slow]

#print axioms visitors
end Collatz.FiveWindow
