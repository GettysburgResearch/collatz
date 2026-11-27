import FixedGapClock

/-! An unconditional two-clock cone and a separate implication from a specified
external balanced router. All other inputs, including the three-adic potential,
are ordinary kernel proofs. -/
namespace Collatz.ClockCone
open Collatz.TwoGapRouting Collatz.FixedGapClock

private def value (r : ℕ) := if r=7 then 3 else if r=5 then 2 else if r=1 ∨ r=4 then 1 else 0
private def potential (n : ℕ) := value (n%9)

private def exponent : ℕ → ℕ
  | 1 | 4 | 10 | 13 | 22 => 2
  | 2 | 8 | 17 | 20 | 26 => 1
  | 5 | 11 | 14 => 3
  | 7 | 16 | 19 => 4
  | 23 => 5
  | 25 => 6
  | _ => 0

private theorem table : ∀ R : Fin 27, let r:=R.val; let e:=exponent r
    let z:=(2^e*r-1)/3
    r%3≠0 → 0<e ∧ 3*z+1=2^e*r ∧ z%3≠0 ∧ e+potential z≤3+potential r := by
  decide +kernel

private theorem one (y : ℕ) (unit : y%3≠0) :
    ∃ z e, z%3≠0 ∧ run e z=y ∧ odds e z=1 ∧ e+potential z≤3+potential y := by
  let r:=y%27
  let k:=y/27
  let e:=exponent r
  let v:=(2^e*r-1)/3
  let z:=9*(2^e*k)+v
  have dec : y=r+27*k := (Nat.mod_add_div _ _).symm
  have ru : r%3≠0 := by dsimp [r]; omega
  obtain ⟨ep,eq,vu,cost⟩:=table ⟨r,Nat.mod_lt _ (by decide)⟩ ru
  change 3*v+1=2^e*r at eq
  change e+potential v≤3+potential r at cost
  have zy : 3*z+1=2^e*y := by dsimp [z]; rw [dec]; nlinarith only [eq]
  obtain ⟨rz,oz,_⟩:=gap e z y ep zy
  have zp : potential z=potential v := by simp [potential,z]
  have yp : potential y=potential r := by
    unfold potential
    have h : y%9=r%9 := by dsimp [r]; omega
    rw [h]
  exact ⟨z,e,by dsimp [z]; change v%3≠0 at vu; omega,rz,oz,by omega⟩

private theorem pot_le (y : ℕ) : potential y≤3 := by
  unfold potential value
  split_ifs <;> omega

private theorem pad (r y : ℕ) (unit : y%3≠0) :
    ∃ z L, z%3≠0 ∧ run L z=y ∧ odds L z=r ∧ L+potential z≤3*r+potential y := by
  induction r generalizing y with
  | zero => exact ⟨y,0,unit,rfl,rfl,by simp⟩
  | succ r ih =>
    obtain ⟨w,e,wu,rw',ow,c⟩:=one y unit
    obtain ⟨z,L,zu,rz,oz,b⟩:=ih w wu
    obtain ⟨ra,oa⟩:=append L e z
    rw [rz,rw'] at ra
    rw [rz,oz,ow] at oa
    exact ⟨z,L+e,zu,ra,oa,by omega⟩

def Twin (s d D g y c : ℕ) : Prop :=
  ∃ x, 0<x ∧ x ≡ c [MOD 3^s] ∧ run D x=y ∧ run D (x+d)=y ∧
    odds D x=g ∧ odds D (x+d)=g

private theorem finish {s d B a L r D g y z c : ℕ} (core : Cover s d B a)
    (budget : B+L≤D) (grade : a+r=g) (unit : z%3≠0)
    (endpt : run L z=y) (weight : odds L z=r) : Twin s d D g y c := by
  obtain ⟨x,xp,xc,r1,r2,o1,o2⟩:=core (D-L) (by omega) z unit c
  obtain ⟨h1,w1⟩:=append (D-L) L x
  obtain ⟨h2,w2⟩:=append (D-L) L (x+d)
  have sum : D-L+L=D := by omega
  rw [sum,r1,endpt] at h1
  rw [sum,r2,endpt] at h2
  rw [sum,r1,o1,weight,grade] at w1
  rw [sum,r2,o2,weight,grade] at w2
  exact ⟨x,xp,xc,h1,h2,w1,w2⟩

/-- Both clocks can be prescribed simultaneously above this unconditional
slope-three line. The endpoint need only be a ternary unit. -/
theorem elementary_cone (s d : ℕ) : ∃ B a, B≤18*3^s*weight d+2*d+3 ∧
    ∀ r D y c, B+3*r+3≤D → y%3≠0 → Twin s d D (a+r) y c := by
  obtain ⟨B,a,core,bound⟩:=cover_bound d s
  refine ⟨B,a,bound,?_⟩
  intro r D y c budget unit
  obtain ⟨z,L,zu,rz,oz,b⟩:=pad r y unit
  have := pot_le y
  exact finish core (by omega) rfl zu rz oz

/-- Fixed-precision instance of Paper 37/v4 Theorem D used in the conditional
theorem. It is a proposition, never introduced as an axiom. -/
def BalancedNine (b : ℕ) : Prop :=
  ∀ y, y%2=1 → y%3≠0 → ∃ w, w%9=2 ∧ run (2*b) w=y ∧ odds (2*b) w=b

private theorem discount (b y : ℕ) (router : BalancedNine b)
    (yo : y%2=1) (yu : y%3≠0) : ∃ z, z%2=1 ∧ z%3≠0 ∧
      run (2*b+1) z=y ∧ odds (2*b+1) z=b+1 := by
  obtain ⟨w,wr,wy,wo⟩:=router y yo yu
  let z:=6*(w/9)+1
  have s : step z=w := by unfold step; dsimp [z]; split <;> omega
  have oz : z%2=1 := by dsimp [z]; omega
  refine ⟨z,oz,by dsimp [z]; omega,?_,?_⟩
  · simpa [run,s] using wy
  · change z%2+odds (2*b) (step z)=b+1
    rw [oz,s,wo]; omega

private theorem repeat_discount (b q y : ℕ) (router : BalancedNine b)
    (yo : y%2=1) (yu : y%3≠0) : ∃ z, z%2=1 ∧ z%3≠0 ∧
      run (q*(2*b+1)) z=y ∧ odds (q*(2*b+1)) z=q*(b+1) := by
  induction q generalizing y with
  | zero => exact ⟨y,yo,yu,by simp [run],by simp [odds]⟩
  | succ q ih =>
    obtain ⟨w,wo,wu,wy,ww⟩:=discount b y router yo yu
    obtain ⟨z,zo,zu,zw,zz⟩:=ih w wo wu
    obtain ⟨r,o⟩:=append (q*(2*b+1)) (2*b+1) z
    rw [zw,wy] at r
    rw [zw,zz,ww] at o
    exact ⟨z,zo,zu,by simpa [Nat.succ_mul] using r,by simpa [Nat.succ_mul] using o⟩

/-- The exact two-clock cone obtained from the explicitly named balanced
router. Writing r=q*(b+1)+t with 0≤t<b+1, its limiting clock per extra odd
departure is (2*b+1)/(b+1). -/
theorem discounted_cone (b s d : ℕ) (router : BalancedNine b) :
    ∃ B a, B≤18*3^s*weight d+2*d+3 ∧ ∀ q t D y c,
      B+q*(2*b+1)+3*t+3≤D → y%2=1 → y%3≠0 →
      Twin s d D (a+(q*(b+1)+t)) y c := by
  obtain ⟨B,a,core,bound⟩:=cover_bound d s
  refine ⟨B,a,bound,?_⟩
  intro q t D y c budget yo yu
  obtain ⟨w,_,wu,wy,ww⟩:=repeat_discount b q y router yo yu
  obtain ⟨z,L,zu,rz,oz,cost⟩:=pad t w wu
  have := pot_le w
  obtain ⟨r,o⟩:=append L (q*(2*b+1)) z
  rw [rz,wy] at r
  rw [rz,oz,ww] at o
  exact finish core (by omega) (by omega) zu r o

#print axioms elementary_cone
#print axioms discounted_cone
end Collatz.ClockCone
