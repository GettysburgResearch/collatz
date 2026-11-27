import TernaryPowerLift
import Mathlib.Data.Nat.ModEq
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.GCongr
import Mathlib.Tactic.SplitIfs

/-! Two Syracuse inverse gaps at an exactly specified shortcut clock. -/
namespace Collatz.TwoGapRouting

def step (n : ℕ) := if n % 2 = 0 then n / 2 else (3 * n + 1) / 2

def run : ℕ → ℕ → ℕ
  | 0, n => n
  | k + 1, n => run k (step n)

def odds : ℕ → ℕ → ℕ
  | 0, _ => 0
  | k + 1, n => n % 2 + odds k (step n)

theorem append (h k n : ℕ) :
    run (h+k) n = run k (run h n) ∧ odds (h+k) n = odds h n + odds k (run h n) := by
  induction h generalizing n with
  | zero => simp [run, odds]
  | succ h ih =>
    obtain ⟨r,o⟩ := ih (step n)
    simp only [Nat.succ_add, run, odds, r, o, Nat.add_assoc]
    exact ⟨True.intro,True.intro⟩

private theorem halves (h n : ℕ) :
    run h (2^h*n) = n ∧ odds h (2^h*n) = 0 := by
  induction h with
  | zero => simp [run, odds]
  | succ h ih =>
    have form : 2^(h+1)*n = 2*(2^h*n) := by ring
    have even : (2*(2^h*n))%2=0 := by omega
    have st : step (2*(2^h*n))=2^h*n := by simp [step, even]
    simpa only [form, run, odds, even, st, Nat.zero_add] using ih

theorem gap (e x y : ℕ) (pos : 0<e) (eq : 3*x+1=2^e*y) :
    run e x=y ∧ odds e x=1 ∧ x%2=1 := by
  obtain ⟨k,rfl⟩ := Nat.exists_eq_succ_of_ne_zero (by omega : e≠0)
  have form : 3*x+1=2*(2^k*y) := by rw [eq,pow_succ]; ring
  have odd : x%2=1 := by omega
  have st : step x=2^k*y := by unfold step; split <;> omega
  obtain ⟨r,o⟩ := halves k y
  simp [run, odds, st, odd, r, o]

private theorem unit_two (e : ℕ) : 2^e%3≠0 := by
  induction e with
  | zero => decide
  | succ e ih => rw [pow_succ,Nat.mul_mod]; omega

/-- A positive exponent within one *complete* period for each target unit. -/
theorem address (j b : ℕ) (unit : b%3≠0) :
    ∃ e : ℕ, 0<e ∧ e≤2*3^j ∧ 2^e ≡ b [MOD 3^(j+1)] := by
  let m := 3^(j+1)
  let p := 2*3^j
  obtain ⟨E,k,ep,eq⟩ := TernaryPowerLift.cofinal j b 1 unit
  obtain ⟨u,pu⟩ := TernaryPowerLift.period j
  have sp : 2^p ≡ 1 [MOD m] := by
    change 2^(2*3^j) ≡ 1 [MOD 3^(j+1)]
    rw [pu]; simp [Nat.ModEq]
  have pp : 0<p := by dsimp [p]; positivity
  let e := (E-1)%p+1
  have dec : E=e+p*((E-1)/p) := by
    have t:=Nat.mod_add_div (E-1) p
    dsimp [e]; omega
  have modE : 2^E ≡ 2^e [MOD m] := by
    rw [dec, pow_add, pow_mul]
    simpa using (Nat.ModEq.refl (2^e)).mul (sp.pow ((E-1)/p))
  have eb : 2^E ≡ b [MOD m] := by rw [eq]; simp [m,Nat.ModEq]
  refine ⟨e,by dsimp [e]; omega,?_,modE.symm.trans eb⟩
  have := Nat.mod_lt (E-1) pp
  dsimp [e]; omega

private theorem twice_le_pow (k : ℕ) : 2*k≤2^k := by
  induction k with
  | zero => decide
  | succ k ih =>
    cases k with
    | zero => decide
    | succ k => rw [pow_succ]; omega

/-- The affine equation includes both intermediate ordinary valuation gaps. -/
theorem replay (D e x y : ℕ) (ep : 0<e) (ed : e<D)
    (eq : 9*x+3+2^e=2^D*y) :
    run D x=y ∧ odds D x=2 ∧ x%2=1 := by
  let f := D-e
  let t := 2^f*y
  have ef : e+f=D := by dsimp [f]; omega
  have h : 3*(3*x+1)+2^e=2^e*t := by
    calc 3*(3*x+1)+2^e = 2^D*y := by omega
         _ = 2^e*t := by dsimp [t]; rw [← ef,pow_add]; ring
  have tm : t%3=1 := by
    have u:=unit_two e
    have z:=congrArg (fun n : ℕ => n%3) h
    simp only [Nat.add_mod, Nat.mul_mod (2^e) t, Nat.mul_mod (3:ℕ), Nat.mod_self,
      zero_mul, Nat.zero_mod, zero_add, Nat.mod_mod] at z
    rcases (show 2^e%3=1 ∨ 2^e%3=2 by omega) with a|a <;> rw [a] at z <;> omega
  let u:=t/3
  have ut : 3*u+1=t := by dsimp [u]; omega
  have xu : 3*x+1=2^e*u := by rw [← ut] at h; nlinarith
  obtain ⟨r,o,ox⟩:=gap e x u ep xu
  obtain ⟨s,a,_⟩:=gap f u y (by dsimp [f]; omega) ut
  obtain ⟨rr,oo⟩:=append e f x
  rw [ef,r,s] at rr
  rw [ef,r,o,a] at oo
  exact ⟨rr,oo,ox⟩

/-- For each actual ternary-unit endpoint and *every specified clock* above the
threshold, two odd departures suffice to prescribe an arbitrary ternary prefix
on an ordinary positive ancestor. The affine carry is retained. -/
theorem route (s D y c : ℕ) (clock : 6*3^s<D) (unit : y%3≠0) :
    ∃ x e : ℕ, 0<x ∧ 0<e ∧ e<D ∧ e≤6*3^s ∧
      x ≡ c [MOD 3^s] ∧ 9*x+3+2^e=2^D*y ∧
      run D x=y ∧ odds D x=2 ∧ x%2=1 := by
  let m:=3^s
  let r:=c%m
  let half:=2^(D-1)
  let A:=2^D*y-(3+9*r)
  have mp : 0<m := by dsimp [m]; positivity
  have rm : r<m := Nat.mod_lt _ mp
  have yc : 0<y := by omega
  have Dp : 0<D := by omega
  have tw : 2^D=2*half := by
    calc 2^D = 2^((D-1)+1) := by congr 1; omega
         _ = 2*half := by dsimp [half]; ring
  have big : 2*(D-1)≤half := twice_le_pow _
  change 6*m<D at clock
  have size : 2*half≤2^D*y := by rw [←tw]; exact Nat.le_mul_of_pos_right _ yc
  have As : A+(3+9*r)=2^D*y := by dsimp [A]; omega
  have am : A%3≠0 := by
    have pu:=unit_two D
    have z:=congrArg (fun n : ℕ => n%3) As
    change (A+(3+9*r))%3=(2^D*y)%3 at z
    rw [Nat.mul_mod (2^D) y] at z
    rcases (show 2^D%3=1 ∨ 2^D%3=2 by omega) with t|t <;>
      rcases (show y%3=1 ∨ y%3=2 by omega) with u|u <;> rw [t,u] at z <;> omega
  obtain ⟨e,ep,eb,addr⟩:=address (s+1) A am
  have eb' : e≤6*m := by dsimp [m]; rw [pow_succ] at eb; omega
  have eh : 2^e≤half := Nat.pow_le_pow_right (by decide : 0<2) (by omega)
  obtain ⟨v,vf⟩ := (Nat.modEq_iff_dvd' (show 2^e≤A by omega)).mp addr
  let x:=r+m*v
  have factor : 3^(s+1+1)*v=9*(m*v) := by dsimp [m]; ring
  have eq : 9*x+3+2^e=2^D*y := by dsimp [x]; omega
  have xp : 0<x := by omega
  have xc : x ≡ c [MOD 3^s] := by dsimp [x,r,m]; simp [Nat.ModEq]
  exact ⟨x,e,xp,ep,by omega,eb',xc,eq,replay D e x y ep (by omega) eq⟩

#print axioms address
#print axioms replay
#print axioms route

end Collatz.TwoGapRouting
