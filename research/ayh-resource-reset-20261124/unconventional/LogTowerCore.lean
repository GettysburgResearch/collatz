import LogTowerData
import Mathlib.Data.Nat.ModEq
import Mathlib.Tactic.Linarith

/-! Recover the post-peak unit on a supplied thin multiplicative family by
finite integer squaring. No p-adic logarithm is assumed. -/
set_option maxRecDepth 40000
set_option maxHeartbeats 4000000
set_option exponentiation.threshold 10000
namespace LogTower
open CollatzReverseBasin WordRank LogTowerData

private def B : Nat → Nat
  | 0 => (A-1)/8
  | n+1 => B n+2^(n+2)*(B n)^2

private theorem derivative (n : Nat) : A^(2^n)=1+2^(n+3)*B n := by
  induction n with
  | zero => decide
  | succ n ih =>
    rw [pow_succ (2:Nat) n,pow_mul,ih,B]
    rw [show n+1+3=n+3+1 by omega,pow_succ (2:Nat) (n+3),
        show n+3=n+2+1 by omega,pow_succ (2:Nat) (n+2)]
    ring

private theorem computed (n : Nat) : B n ≡ normResidue n [MOD 2^K] := by
  induction n with
  | zero => simp [B,normResidue,Nat.ModEq]
  | succ n ih =>
    unfold B normResidue
    change (B n+2^(n+2)*(B n)^2)%2^K=(_%2^K)%2^K
    rw [Nat.mod_mod]
    exact ih.add ((ih.pow 2).mul_left _)

private theorem stable (n : Nat) (large : 2955≤n) : B n ≡ seedB [MOD 2^K] := by
  obtain ⟨t,ht⟩ : ∃ t, n=2955+t := ⟨n-2955,by omega⟩
  subst n
  clear large
  induction t with
  | zero => simpa only [Nat.add_zero,finite_unit.1] using computed 2955
  | succ t ih =>
    change B (2955+t)+2^(2955+t+2)*(B (2955+t))^2 ≡ seedB [MOD 2^K]
    apply Nat.ModEq.trans _ ih
    apply Nat.add_modEq_left_iff.mpr
    exact dvd_mul_of_dvd_left (pow_dvd_pow 2 (show K≤2955+t+2 by unfold K; omega)) _

/-- First-order expansion of the ordinary dyadic power quotient. -/
private theorem expand_at (h e v b : Nat) (large : h≤e) : ∃ u : Nat,
    (1+2^e*b)^v=1+2^e*u ∧ u ≡ v*b [MOD 2^h] := by
  induction v with
  | zero => exact ⟨0,by simp,by simp [Nat.ModEq]⟩
  | succ v ih =>
    obtain ⟨g,hg,cg⟩:=ih
    refine ⟨g+b+2^e*g*b,by rw [pow_succ,hg]; ring,?_⟩
    rw [Nat.succ_mul]
    apply Nat.ModEq.trans _ (cg.add_right b)
    exact Nat.add_modEq_left_iff.mpr (dvd_mul_of_dvd_left
      (dvd_mul_of_dvd_left (pow_dvd_pow 2 large) g) b)

private theorem rotation (n : Nat) : ∃ c : Nat, 3^(2^(n+1))=1+2^(n+3)*c := by
  induction n with
  | zero => exact ⟨1,by decide⟩
  | succ n ih =>
    obtain ⟨c,ec⟩:=ih
    refine ⟨c+2^(n+2)*c^2,?_⟩
    rw [pow_succ (2:Nat) (n+1),pow_mul,ec,
        show n+1+3=n+3+1 by omega,pow_succ (2:Nat) (n+3),
        show n+3=n+2+1 by omega,pow_succ (2:Nat) (n+2)]; ring

theorem rotation_multiple (h v : Nat) : 3^(2^(h+1)*v) ≡ 1 [MOD 2^(h+3)] := by
  obtain ⟨c,eq⟩:=rotation h
  rw [pow_mul,eq]
  have base : 1+2^(h+3)*c ≡ 1 [MOD 2^(h+3)] := by simp [Nat.ModEq]
  simpa only [one_pow] using base.pow v

/-- For the actual exponent m=4^r u₀, its normalized power ratio is
congruent to the product of the integer derivative and u₀. -/
theorem normalized (r u₀ : Nat) (large : 2955≤2*r) : ∃ u : Nat,
    3^(162*(4^r*u₀))=1+2^(2*r+3)*u ∧ u ≡ u₀*seedB [MOD 2^K] := by
  have klt : K≤2*r+3 := by unfold K; omega
  obtain ⟨u,hu,cu⟩:=expand_at K (2*r+3) u₀ (B (2*r)) klt
  refine ⟨u,?_,cu.trans ((stable (2*r) large).mul_left u₀)⟩
  rw [show (4:Nat)^r=2^(2*r) by rw [pow_mul]; rfl,
      show 162*(2^(2*r)*u₀)=162*2^(2*r)*u₀ by ring,pow_mul,pow_mul]
  change (A^(2^(2*r)))^u₀=_
  rwa [derivative]

/-- A finite integer representative of the derivative at any chosen
precision; no fixed terminal modulus is involved. -/
def dyadicUnit (h : Nat) := B h

private theorem stable_at (k t : Nat) : B (k+t) ≡ dyadicUnit k [MOD 2^k] := by
  induction t with
  | zero => rfl
  | succ t ih =>
    change B (k+t)+2^(k+t+2)*(B (k+t))^2 ≡ dyadicUnit k [MOD 2^k]
    apply Nat.ModEq.trans _ ih
    exact Nat.add_modEq_left_iff.mpr (dvd_mul_of_dvd_left (pow_dvd_pow 2 (by omega)) _)

/-- The normalized exponent map at all finite dyadic precisions. -/
theorem normalized_at (h s v : Nat) (large : h≤s) : ∃ u : Nat,
    A^(2^s*v)=1+2^(s+3)*u ∧ u ≡ v*dyadicUnit h [MOD 2^h] := by
  obtain ⟨u,eq,con⟩:=expand_at h (s+3) v (B s) (by omega)
  have stable : B s ≡ dyadicUnit h [MOD 2^h] := by
    have ex : h+(s-h)=s := by omega
    exact ex ▸ stable_at h (s-h)
  exact ⟨u,by rw [pow_mul,derivative,eq],con.trans (stable.mul_left _)⟩

/-- Both perturbed 119-clock anchor traces retain their real, positive
integer trajectories, including the lower reference of denominator 3^52. -/
private theorem plus_pred (x y : Nat) (hy : 0<y) : x+(y-1)=x+y-1 := by omega

theorem anchor_lift (u q : Nat) (eq : 3^52*u=1+2^119*q) :
    run 119 (u-1)=1+q ∧ run 119 (3^63*u-1)=1+3^71*q := by
  obtain ⟨ea,ac,ap,t1,c1,t2,c2⟩:=anchors
  have mod : 3^52*u ≡ 3^52*a [MOD 2^119] := by rw [eq,ea]; simp [Nat.ModEq]
  have cu : u ≡ a [MOD 2^119] := Nat.ModEq.cancel_left_of_coprime (by decide) mod
  change u%2^119=a%2^119 at cu
  rw [Nat.mod_eq_of_lt ac] at cu
  let b:=u/2^119
  have ub : u=2^119*b+a := calc
    u = u%2^119 + 2^119*b := (Nat.mod_add_div _ _).symm
    _ = _ := by rw [cu]; ring
  have qb : q=3^52*b+a0 := by
    have id : 1+2^119*q=1+2^119*(3^52*b+a0) := calc
      _ = 3^52*u := eq.symm
      _ = 3^52*(2^119*b)+3^52*a := by rw [ub]; ring
      _ = _ := by rw [ea]; ring
    exact Nat.eq_of_mul_eq_mul_left (by positivity : 0<(2:Nat)^119) (Nat.add_left_cancel id)
  obtain ⟨l1,_⟩:=liftPrefix 119 b (a-1)
  obtain ⟨l2,_⟩:=liftPrefix 119 (3^63*b) (3^63*a-1)
  have u1 : 2^119*b+(a-1)=u-1 := by rw [plus_pred _ _ ap,←ub]
  have u2 : 2^119*(3^63*b)+(3^63*a-1)=3^63*u-1 := by
    have prod : 2^119*(3^63*b)+3^63*a=3^63*u := calc
      _ = 3^63*(2^119*b+a) := by ring
      _ = 3^63*u := congrArg (fun n : Nat => 3^63*n) ub.symm
    exact (plus_pred _ _ (Nat.mul_pos (Nat.pow_pos (by decide : 0<(3:Nat))) ap)).trans
      (congrArg (fun n : Nat => n-1) prod)
  rw [u1,c1,t1] at l1
  rw [u2,c2,t2] at l2
  rw [l1,l2,qb]; constructor <;> ring

theorem laps (r u : Nat) : run (2*r) (1+4^r*u)=1+3^r*u := by
  induction r generalizing u with
  | zero => simp [run]
  | succ r ih =>
    let x:=4^r*u
    have e1 : shortcut (1+4*x)=2+6*x := by unfold shortcut; split <;> omega
    have e2 : shortcut (2+6*x)=1+3*x := by unfold shortcut; split <;> omega
    have val : 1+4^(r+1)*u=1+4*x := by dsimp [x]; ring
    rw [show 2*(r+1)=2+2*r by omega,runAdd,val]
    change run (2*r) (shortcut (shortcut (1+4*x)))=_
    rw [e1,e2,show 1+3*x=1+4^r*(3*u) by dsimp [x]; ring,ih]; ring

theorem terminal_lift (u : Nat) (mod : u ≡ seedU [MOD 2^K]) :
    run K (1+u)=run K (1+3^71*u) := by
  change u%2^K=seedU%2^K at mod
  rw [Nat.mod_eq_of_lt finite_unit.2.2.1] at mod
  let q:=u/2^K
  have eq : u=2^K*q+seedU := calc
    _ = u%2^K+2^K*q := (Nat.mod_add_div _ _).symm
    _ = _ := by rw [mod]; ring
  obtain ⟨left,_⟩:=liftPrefix K q (1+seedU)
  obtain ⟨right,_⟩:=liftPrefix K (3^71*q) (1+3^71*seedU)
  rw [terminal.1,terminal.2,pow_add] at left
  rw [show 1+u=2^K*q+(1+seedU) by rw [eq]; ring,left,
      show 1+3^71*u=2^K*(3^71*q)+(1+3^71*seedU) by rw [eq]; ring,right]
  ring


#print axioms normalized_at
#print axioms normalized
#print axioms terminal_lift
end LogTower
