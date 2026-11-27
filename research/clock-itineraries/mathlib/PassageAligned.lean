module

public import PassageBinaryRays
public import PassageRouting
import all PassageRouting
import all TowerFrontierAffine
import all FiberTransport
import all TernaryItinerary
import Mathlib.Tactic

public section
namespace Collatz.Itinerary.PassageAligned

open TowerFrontier PassageRouting
set_option autoImplicit false

def odds (h n : ℕ) := (track h n 0).2

private theorem tracked (h n g : ℕ) : track h n g=(run h n,odds h n+g) := by
  have eq := TowerFrontier.transport h n 0 g 0
  simpa only [Nat.mul_zero,Nat.add_zero,Nat.zero_add,FiberTransport.track_value,odds] using eq

private theorem extend (h f n : ℕ) :
    odds (h+f) n=odds h n+odds f (run h n) := by
  apply Eq.trans (congrArg Prod.snd (TowerFrontier.track_add h f n 0))
  rw [tracked h n 0,tracked]
  simp [Nat.add_comm]

private theorem laps (r : ℕ) : run (2*r) 1=1 ∧ odds (2*r) 1=r := by
  induction r with
  | zero => decide
  | succ r ih =>
    rw [Nat.mul_succ,run_add,extend,ih.1,ih.2]
    have a : run 2 1=1 := by decide
    have b : odds 2 1=1 := by decide
    exact ⟨a,by rw [b]⟩

private theorem return_count (d : ℕ) (back : run d 1=1) : d=2*odds d 1 := by
  obtain ⟨_,count⟩ := laps (d/2)
  by_cases even : d%2=0
  · have eq : 2*(d/2)=d := by omega
    rw [eq] at count
    omega
  · have eq : d=2*(d/2)+1 := by omega
    rw [eq,run_add,(laps (d/2)).1] at back
    contradiction

private theorem clock_balance {j x h : ℕ} (same : track (j+h) x 0=track h 1 0) :
    ∃ H, FirstLow H x 1 ∧ H=j+2*odds H x := by
  have both : track (j+2*h) x 0=track (2*h) 1 0 := by
    conv => lhs; rw [show j+2*h=(j+h)+h by omega,TowerFrontier.track_add,same]
    conv => rhs; rw [show 2*h=h+h by omega,TowerFrontier.track_add]
  have endHit : run (j+2*h) x=1 := by
    have a := congrArg Prod.fst both
    simpa only [FiberTransport.track_value,(laps h).1] using a
  have endCount : odds (j+2*h) x=h := (congrArg Prod.snd both).trans (laps h).2
  have existsHit : ∃ t, run t x=1 := ⟨_,endHit⟩
  classical
  let H := Nat.find existsHit
  have first : run H x=1 := Nat.find_spec existsHit
  have earlier (k : ℕ) (hk : k<H) : 1<run k x := by
    have ne : run k x≠1 := Nat.find_min existsHit hk
    have zrun (l : ℕ) : run l 0=0 := by
      induction l with
      | zero => rfl
      | succ l ih => simpa [run,step] using ih
    have pos : run k x≠0 := by
      intro z
      have eq : H=k+(H-k) := by omega
      rw [eq,run_add,z,zrun] at first
      contradiction
    omega
  let d := j+2*h-H
  have le : H≤j+2*h := Nat.find_min' existsHit endHit
  have total : H+d=j+2*h := by dsimp only [d]; omega
  rw [←total,run_add,first] at endHit
  rw [←total,extend,first] at endCount
  have := return_count d endHit
  exact ⟨H,⟨first,earlier⟩,by omega⟩

private theorem odd_cost {h x m : ℕ} (hit : FirstLow h x 1)
    (floor : ∀ j<h, (run j x)%2≠0 → m≤run j x) :
    2^h*m^(odds h x)≤x*(3*m+1)^(odds h x) := by
  induction h generalizing x with
  | zero => change x=1 ∧ _ at hit; simp [odds,track,hit.1]
  | succ h ih =>
    have tail : FirstLow h (step x) 1 := ⟨hit.1,fun j hj => hit.2 (j+1) (by omega)⟩
    have next := ih tail (fun j hj => floor (j+1) (by omega))
    have cnt : odds (h+1) x=odds h (step x)+x%2 := by
      unfold odds
      rw [track]
      split <;> rename_i e
      · simp [step,e]
      · have o : x%2=1 := by omega
        rw [tracked]; simp [step,o,odds]
    rw [cnt,pow_succ 2 h]
    by_cases e : x%2=0
    · have eq : 2*step x=x := by rw [step,if_pos e]; omega
      rw [e,Nat.add_zero]
      calc
        _ = 2*(2^h*m^(odds h (step x))) := by ring
        _ ≤ 2*(step x*(3*m+1)^(odds h (step x))) := Nat.mul_le_mul_left _ next
        _ = _ := by rw [←Nat.mul_assoc,eq]
    · have o : x%2=1 := by omega
      have rule : 2*step x=3*x+1 := by rw [step,if_neg e]; omega
      have minx : m≤x := floor 0 (by omega) e
      have eq : 2*m*step x≤(3*m+1)*x := by
        rw [show 2*m*step x=m*(2*step x) by ring,rule]
        nlinarith only [minx]
      rw [o,pow_succ,pow_succ]
      calc
        _ = (2*m)*(2^h*m^(odds h (step x))) := by ring
        _ ≤ (2*m)*(step x*(3*m+1)^(odds h (step x))) := Nat.mul_le_mul_left _ next
        _ ≤ _ := by
          rw [←Nat.mul_assoc,show x*((3*m+1)^(odds h (step x))*(3*m+1))=
            ((3*m+1)*x)*(3*m+1)^(odds h (step x)) by ring]
          exact Nat.mul_le_mul_right _ eq

/-- A profile merger of a leading binary integer with its root, preserving
the clock offset j and the odd count, permits at most three odd departures
before the integer first reaches one. The comparison clock is unrestricted. -/
theorem root_profile_barrier {j x : ℕ} (upper : x<2^(j+1))
    (aligned : ∃ h, track (j+h) x 0=track h 1 0) :
    ∃ H, FirstLow H x 1 ∧ H=j+2*odds H x ∧ odds H x≤3 := by
  obtain ⟨h,eq⟩ := aligned
  obtain ⟨H,hit,bal⟩ := clock_balance eq
  let q := odds H x
  have lhs : 2^H*3^q=2^j*12^q := by
    rw [show H=j+2*q from bal,pow_add,pow_mul]
    rw [show (2:ℕ)^2=4 by decide,show (12:ℕ)=4*3 by decide,mul_pow]; ring
  have bound := odd_cost (m:=3) hit (fun i hi odd => by have := hit.2 i hi; omega)
  change 2^H*3^q≤x*10^q at bound
  rw [lhs] at bound
  have strict := bound.trans_lt (Nat.mul_lt_mul_of_pos_right upper (Nat.pow_pos (by decide)))
  rw [pow_succ (2:ℕ) j,Nat.mul_assoc] at strict
  have ratio := Nat.lt_of_mul_lt_mul_left strict
  have bad (r : ℕ) : 2*10^(4+r)≤12^(4+r) := by
    induction r with
    | zero => decide
    | succ r ih =>
      rw [Nat.add_succ,pow_succ,pow_succ]
      calc
        _ = (2*10^(4+r))*10 := by ring
        _ ≤ 12^(4+r)*10 := Nat.mul_le_mul_right _ ih
        _ ≤ _ := Nat.mul_le_mul_left _ (by decide)
  refine ⟨H,hit,bal,?_⟩
  change q≤3
  by_contra! large
  have contra := bad (q-4)
  rw [show 4+(q-4)=q by omega] at contra
  omega

/-- Waiting arbitrarily long for this profile equality at the root gives
exactly the same decision as testing four small comparison clocks. -/
theorem four_clocks {j x : ℕ} (upper : x<2^(j+1)) :
    (∃ h, track (j+h) x 0=track h 1 0) ↔
      ∃ q≤3, track (j+2*q) x 0=(1,q) := by
  constructor
  · intro aligned
    obtain ⟨H,hit,bal,bound⟩ := root_profile_barrier upper aligned
    exact ⟨odds H x,bound,by rw [←bal,tracked,hit.1,Nat.add_zero]⟩
  · rintro ⟨q,_,found⟩
    refine ⟨2*q,?_⟩
    rw [found,tracked,(laps q).1,(laps q).2,Nat.add_zero]

private def inverseGrade : ℕ → ℕ → ℕ → List ℕ
  | 0,0,b => [b]
  | 0,_+1,_ => []
  | h+1,0,b => inverseGrade h 0 (2*b)
  | h+1,q+1,b => inverseGrade h (q+1) (2*b) ++
      (if b%3=2 then inverseGrade h q ((2*b-1)/3) else [])

private theorem inverse_size (h q b : ℕ) :
    (inverseGrade h q b).length≤h.choose q := by
  induction h generalizing q b with
  | zero => cases q <;> simp [inverseGrade]
  | succ h ih =>
    cases q with
    | zero => simpa [inverseGrade] using ih 0 (2*b)
    | succ q =>
      simp only [inverseGrade,List.length_append,Nat.choose_succ_succ]
      split
      · exact (Nat.add_le_add (ih _ _) (ih _ _)).trans_eq (Nat.add_comm ..)
      · exact (ih _ _).trans (Nat.le_add_left _ _)

private theorem inverse_mem (h x : ℕ) : x∈inverseGrade h (odds h x) (run h x) := by
  induction h with
  | zero => simp [inverseGrade,odds,track,run]
  | succ h ih =>
    let y := run h x
    have final : run (h+1) x=step y := run_add h 1 x
    have count : odds (h+1) x=odds h x+y%2 := by
      rw [extend]
      change odds h x+odds 1 y=odds h x+y%2
      simp only [odds,track]
      split <;> omega
    rw [final,count]
    by_cases even : y%2=0
    · have pre : 2*step y=y := by rw [step,if_pos even]; omega
      rw [even,Nat.add_zero]
      cases e : odds h x with
      | zero => simpa only [inverseGrade,pre] using e ▸ ih
      | succ q =>
        apply List.mem_append_left
        simpa only [pre,e] using ih
    · have first : y%2=1 := by omega
      have sx : step y=(3*y+1)/2 := by rw [step,if_neg even]
      have pre : (2*step y-1)/3=y := by rw [sx]; omega
      have res : step y%3=2 := by rw [sx]; omega
      rw [first,inverseGrade,if_pos res,pre]
      exact List.mem_append_right _ ih

private theorem three_visits_five {H j x : ℕ} (first : FirstLow H x 1) (time : H=j+6)
    (count : odds H x=3) (upper : x<2^(j+1)) :
    run (j+2) x=5 ∧ odds (j+2) x=2 := by
  have small : ∃ k<H, run k x=3 ∨ run k x=5 := by
    by_contra! avoid
    have bound := odd_cost (m:=7) first (fun k hk odd => by
      have := first.2 k hk; have := avoid k hk; omega)
    rw [count,time,pow_add 2 j 6] at bound
    have strict := bound.trans_lt (Nat.mul_lt_mul_of_pos_right upper
      (by decide : 0<(3*7+1)^3))
    rw [pow_succ (2:ℕ) j] at strict
    simp only [Nat.mul_assoc] at strict
    have falseBound := Nat.lt_of_mul_lt_mul_left strict
    norm_num at falseBound
  obtain ⟨k,kh,smallVal⟩ := small
  have visit : ∃ u<H, run u x=5 := by
    rcases smallVal with three | five
    · have five : run (k+1) x=5 := by rw [run_add,three]; decide
      refine ⟨k+1,?_,five⟩
      by_contra! no
      have same : k+1=H := by omega
      rw [same,first.1] at five
      contradiction
    · exact ⟨k,kh,five⟩
  obtain ⟨u,uh,hit⟩ := visit
  have five : FirstLow 4 5 1 := by unfold FirstLow; decide
  have endTime : u+4=H := by
    by_contra ne
    rcases lt_or_gt_of_ne ne with early | late
    · have bad := first.2 (u+4) early
      rw [run_add,hit,five.1] at bad
      omega
    · have bad := five.2 (H-u) (by omega)
      have reach := first.1
      rw [show H=u+(H-u) by omega,run_add,hit] at reach
      omega
  have pos : u=j+2 := by omega
  subst u
  have cost : odds 4 5=1 := by decide
  rw [←endTime,extend,hit,cost] at count
  exact ⟨hit,by omega⟩

/-- The complete list of candidates has quadratic size in the binary
depth, even if the comparison clock is allowed to depend on the start. -/
theorem polynomial_cover (j : ℕ) : ∃ xs : List ℕ,
    xs.length ≤ (j.choose 0)+(j+2).choose 1+(j+4).choose 2+(j+2).choose 2 ∧
    ∀ x<2^(j+1), (∃ h, track (j+h) x 0=track h 1 0) → x∈xs := by
  let row := fun q => inverseGrade (j+2*q) q 1
  refine ⟨row 0++row 1++row 2++inverseGrade (j+2) 2 5,?_,?_⟩
  · simp only [List.length_append]
    exact Nat.add_le_add (Nat.add_le_add (Nat.add_le_add
      (by simpa [row] using inverse_size j 0 1) (inverse_size (j+2) 1 1))
        (inverse_size (j+4) 2 1)) (inverse_size (j+2) 2 5)
  · intro x upper aligned
    obtain ⟨H,first,bal,small⟩ := root_profile_barrier upper aligned
    simp only [List.mem_append]
    by_cases three : odds H x=3
    · have visit := three_visits_five first (by omega) three upper
      have mem := inverse_mem (j+2) x
      rw [visit.1,visit.2] at mem
      exact Or.inr mem
    · let q := odds H x
      have mem := inverse_mem H x
      rw [first.1] at mem
      have hq : H=j+2*q := bal
      change x∈inverseGrade H q 1 at mem
      rw [hq] at mem
      change x∈row q at mem
      have small' : q≤2 := by dsimp only [q]; omega
      interval_cases q <;> tauto

#print axioms root_profile_barrier
#print axioms four_clocks
#print axioms polynomial_cover
end Collatz.Itinerary.PassageAligned
