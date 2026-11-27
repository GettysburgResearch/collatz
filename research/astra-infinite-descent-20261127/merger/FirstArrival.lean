import FixedGapClock
import Threshold

/-! First arrivals at a supplied target, including periodic targets. -/
namespace Collatz.FirstArrival
open Collatz.TwoGapRouting Collatz.FixedGapClock

def Future (a b : ℕ) : Prop := ∃ i, run i a=b
def First (D x y : ℕ) : Prop := run D x=y ∧ ∀ i<D, run i x≠y

private theorem ordered (y a b e j k : ℕ) (jk : j≤k) (ja : run j y=a)
    (kb : run k y=b) (ay : run e a=y) (by' : run e b=y) : a=b := by
  have pj:=(append j e y).1
  have pk:=(append k e y).1
  rw [ja,ay] at pj
  rw [kb,by'] at pk
  let d:=k-j
  have dec : k=j+d := by dsimp [d]; omega
  have rr:=(append (j+e) d y).1
  rw [show j+e+d=k+e by omega,pj,pk] at rr
  have s:=(append d j y).1
  rw [show d+j=k by omega,kb,←rr,ja] at s
  exact s.symm

private theorem unique {y a b e : ℕ} (aa : Future y a) (bb : Future y b)
    (ay : run e a=y) (by' : run e b=y) : a=b := by
  obtain ⟨j,ja⟩:=aa
  obtain ⟨k,kb⟩:=bb
  rcases le_total j k with h|h
  · exact ordered _ _ _ _ _ _ h ja kb ay by'
  · exact (ordered _ _ _ _ _ _ h kb ja by' ay).symm

private theorem short (y : ℕ) (unit : y%3≠0) :
    ∃e z, 0<e ∧ e≤4 ∧ z%3≠0 ∧ 3*z+1=2^e*y := by
  let k:=y/9
  have row : y=9*k+1 ∨ y=9*k+2 ∨ y=9*k+4 ∨ y=9*k+5 ∨ y=9*k+7 ∨ y=9*k+8 := by dsimp [k]; omega
  rcases row with h|h|h|h|h|h
  · exact ⟨2,12*k+1,by decide,by decide,by omega,by norm_num; omega⟩
  · exact ⟨1,6*k+1,by decide,by decide,by omega,by norm_num; omega⟩
  · exact ⟨2,12*k+5,by decide,by decide,by omega,by norm_num; omega⟩
  · exact ⟨3,24*k+13,by decide,by decide,by omega,by norm_num; omega⟩
  · exact ⟨4,48*k+37,by decide,by decide,by omega,by norm_num; omega⟩
  · exact ⟨1,6*k+5,by decide,by decide,by omega,by norm_num; omega⟩

private theorem halves (h n : ℕ) : run h (2^h*n)=n := by
  induction h with
  | zero => simp [run]
  | succ h ih =>
    have form : 2^(h+1)*n=2*(2^h*n) := by ring
    have st : step (2*(2^h*n))=2^h*n := by simp [step]
    simpa only [form,run,st] using ih

private theorem first_gap (e z y : ℕ) (ep : 0<e) (yu : y%3≠0)
    (eq : 3*z+1=2^e*y) (away : ¬ Future y z) : First e z y := by
  obtain ⟨rz,_,oz⟩:=gap e z y ep eq
  refine ⟨rz,?_⟩
  intro i il hit
  cases i with
  | zero => exact away ⟨0,by simpa [run] using hit.symm⟩
  | succ i =>
    let k:=e-(i+1)
    have kp : 0<k := by dsimp [k]; omega
    have ex : 2^e*y=2*(2^i*(2^k*y)) := by
      rw [show e=(i+k)+1 by dsimp [k]; omega,pow_succ,pow_add]; ring
    have st : step z=2^i*(2^k*y) := by unfold step; split <;> omega
    change run i (step z)=y at hit
    rw [st,halves] at hit
    have big : 1<2^k := Nat.one_lt_two_pow (by omega)
    have := Nat.mul_lt_mul_of_pos_right big (show 0<y by omega)
    omega

/-- Every ternary-unit target has a unit odd predecessor outside its own
forward orbit. Its complete ordinary leg has one odd departure, length at
most ten, and reaches the target for the first time on its last step. -/
theorem branch (y : ℕ) (unit : y%3≠0) : ∃ z e, z%2=1 ∧ z%3≠0 ∧
    0<e ∧ e≤10 ∧ ¬Future y z ∧ First e z y ∧ odds e z=1 := by
  obtain ⟨e,z,ep,eb,zu,eq⟩:=short y unit
  obtain ⟨ry,oz,odd⟩:=gap e z y ep eq
  by_cases inside : Future y z
  · let w:=64*z+21
    have eqw : 3*w+1=2^(e+6)*y := by dsimp [w]; rw [pow_add]; norm_num; nlinarith
    obtain ⟨wy,ow,wo⟩:=gap (e+6) w y (by omega) eqw
    have six : run 6 w=3*z+1 := by
      have st : step w=2^5*(3*z+1) := by unfold step; dsimp [w]; split <;> omega
      change run 5 (step w)=3*z+1
      rw [st,halves]
    have ar:=(append 6 e w).1
    rw [show 6+e=e+6 by omega,wy,six] at ar
    have out : ¬Future y w := by
      rintro ⟨t,tw⟩
      have rr:=(append t 6 y).1
      rw [tw,six] at rr
      have ident:=unique inside ⟨t+6,rr⟩ ry ar.symm
      omega
    exact ⟨w,e+6,wo,by dsimp [w]; omega,by omega,by omega,out,first_gap _ _ _ (by omega) unit eqw out,ow⟩
  · exact ⟨z,e,odd,zu,ep,by omega,inside,first_gap _ _ _ ep unit eq inside,oz⟩

theorem join {h e x z y : ℕ} (meet : run h x=z) (away : ¬ Future y z) (leg : First e z y) :
    First (h+e) x y := by
  have all:=(append h e x).1
  rw [meet,leg.1] at all
  refine ⟨all,?_⟩
  intro i il hit
  by_cases early : i≤h
  · have r:=(append i (h-i) x).1
    rw [show i+(h-i)=h by omega,meet,hit] at r
    exact away ⟨h-i,r.symm⟩
  · have r:=(append h (i-h) x).1
    rw [show h+(i-h)=i by omega,hit,meet] at r
    exact leg.2 _ (by omega) r.symm

/-- All sufficiently large specified common *first* clocks, including for
periodic y. The grade is independent of the clock, endpoint and source class. -/
theorem first_twins (s d : ℕ) : ∃ B a, B≤18*3^s*weight d+2*d+13 ∧
    ∀D, B≤D → ∀ y, y%3≠0 → ∀c, ∃x, 0<x ∧ x ≡ c [MOD 3^s] ∧
      First D x y ∧ First D (x+d) y ∧ odds D x=a ∧ odds D (x+d)=a := by
  obtain ⟨B,a,core,bound⟩:=cover_bound d s
  refine ⟨B+10,a+1,by omega,?_⟩
  intro D budget y unit c
  obtain ⟨z,e,_,zu,_,eb,out,leg,oc⟩:=branch y unit
  obtain ⟨x,xp,xc,l,r,ol,orr⟩:=core (D-e) (by omega) z zu c
  have total : D-e+e=D := by omega
  have a1 := (append (D-e) e x).2
  have a2 := (append (D-e) e (x+d)).2
  rw [total,l,ol,oc] at a1
  rw [total,r,orr,oc] at a2
  exact ⟨x,xp,xc,total ▸ join l out leg,total ▸ join r out leg,a1,a2⟩

/-- The fixed-clock carry incurs an absolute error bounded solely by that
clock, uniformly in the endpoint and its odd count. -/
theorem affine_upper (h n : ℕ) :
    2^h*run h n≤3^(odds h n)*(n+2^h) := by
  induction h generalizing n with
  | zero => simp [run,odds]
  | succ h ih =>
    have a:=Nat.mul_le_mul_left 2 (ih (step n))
    change 2^(h+1)*run h (step n)≤3^(n%2+odds h (step n))*(n+2^(h+1))
    rw [pow_add (3:ℕ) (n%2) (odds h (step n)),pow_succ (2:ℕ) h]
    by_cases ev : n%2=0
    · rw [ev,pow_zero,Nat.one_mul]
      have eq : 2*step n=n := by unfold step; split <;> omega
      have extra:=congrArg (fun v:ℕ => 3^(odds h (step n))*v) eq
      nlinarith only [a,extra]
    · have o : n%2=1 := by omega
      have eq : 2*step n=3*n+1 := by unfold step; split <;> omega
      have extra:=congrArg (fun v:ℕ => 3^(odds h (step n))*v) eq
      have big:=Nat.mul_le_mul_left (3^(odds h (step n))) (Nat.one_le_two_pow (n:=h))
      rw [o,pow_one]
      nlinarith only [a,extra,big,Nat.zero_le ((3:ℕ)^(odds h (step n))*2^h)]

/-- A genuine ladder witness w at a specified endpoint b can be joined to
both starts. The integer bounds are the scaled form of
(2^H/3^g)*w-2^H ≤ x ≤ (2^H/3^g)*w. -/
theorem attach {s d B g H L e y b w c : ℕ} (core : Cover s d B g)
    (clock : B≤H) (wu : w%3≠0) (wb : run L w=b) (away : ¬Future y b)
    (leg : First e b y) :
    ∃x, 0<x ∧ x ≡ c [MOD 3^s] ∧
      First (H+L+e) x y ∧ First (H+L+e) (x+d) y ∧
      odds (H+L+e) x=g+odds L w+odds e b ∧
      odds (H+L+e) (x+d)=g+odds L w+odds e b ∧
      3^g*x≤2^H*w ∧ 2^H*w≤3^g*(x+2^H) := by
  obtain ⟨x,xp,xc,l,r,ol,orr⟩:=core H clock w wu c
  have a1:=append H L x
  have a2:=append H L (x+d)
  rw [l,wb,ol] at a1
  rw [r,wb,orr] at a2
  have q1:=(append (H+L) e x).2
  have q2:=(append (H+L) e (x+d)).2
  rw [a1.1,a1.2] at q1
  rw [a2.1,a2.2] at q2
  have lower:=Collatz.MergerThreshold.forward_lower H x
  have upper:=affine_upper H x
  rw [ol,l] at lower upper
  exact ⟨x,xp,xc,join a1.1 away leg,join a2.1 away leg,q1,q2,by omega,upper⟩

#print axioms affine_upper
#print axioms attach
#print axioms branch
#print axioms first_twins
end Collatz.FirstArrival
