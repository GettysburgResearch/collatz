import SmoothCore
import Mathlib.Tactic.Linarith

namespace Collatz.AugmentedMerger
open Collatz.SourceDeletion Collatz.MinimumFailure

/-- Physical meeting at one clock, with the odd-count difference paying exactly
    for the difference in the two source exponents. -/
def Linked (w r s : Nat) : Prop :=
  ∃ h : Nat, run h (3^r*w)=run h (3^s*w) ∧
    r+odds h (3^r*w)=s+odds h (3^s*w)

theorem run_add (i j x : Nat) : run (i+j) x=run j (run i x) := by
  induction i generalizing x with
  | zero => simp [run]
  | succ i ih => simpa only [Nat.succ_add,run] using ih (step x)

theorem odds_add (i j x : Nat) : odds (i+j) x=odds i x+odds j (run i x) := by
  induction i generalizing x with
  | zero => simp [odds,run]
  | succ i ih =>
    simp only [Nat.succ_add,run,odds,ih]
    omega

theorem extend {w r s i : Nat} (meet : run i (3^r*w)=run i (3^s*w))
    (paid : r+odds i (3^r*w)=s+odds i (3^s*w)) (j : Nat) :
    run (i+j) (3^r*w)=run (i+j) (3^s*w) ∧
    r+odds (i+j) (3^r*w)=s+odds (i+j) (3^s*w) := by
  constructor
  · rw [run_add i j (3^r*w),run_add i j (3^s*w),meet]
  · rw [odds_add i j (3^r*w),odds_add i j (3^s*w),meet,←Nat.add_assoc,paid,Nat.add_assoc]

theorem linked_equivalence (w : Nat) : Equivalence (Linked w) where
  refl r := ⟨0,rfl,rfl⟩
  symm := by rintro r s ⟨h,m,p⟩; exact ⟨h,m.symm,p.symm⟩
  trans := by
    rintro r s t ⟨i,m,p⟩ ⟨j,n,q⟩
    obtain ⟨l,a⟩ := extend m p j
    obtain ⟨k,b⟩ := extend n q i
    rw [Nat.add_comm j i] at k b
    exact ⟨i+j,l.trans k,a.trans b⟩

/-- Doubling the base puts one identical even step on both arms. -/
theorem linked_double (w r s : Nat) : Linked (2*w) r s ↔ Linked w r s := by
  have even (j : Nat) : (3^j*(2*w))%2=0 := by rw [show 3^j*(2*w)=2*(3^j*w) by ring]; omega
  have halve (j : Nat) : step (3^j*(2*w))=3^j*w := by
    simp [step,show 3^j*(2*w)=2*(3^j*w) by ring]
  constructor
  · rintro ⟨i,m,p⟩
    obtain ⟨m',p'⟩ := extend m p 1
    refine ⟨i,?_,?_⟩
    · simpa only [run,halve] using m'
    · simpa only [odds,even,halve,Nat.add_zero] using p'
  · rintro ⟨i,m,p⟩
    refine ⟨i+1,?_,?_⟩
    · simpa only [run,halve] using m
    · simpa only [odds,even,halve,Nat.add_zero] using p

theorem first_tower_minimum {w r s : Nat} (tower : SmoothCore.FirstTower w r)
    (earlier : s<r) : ¬Linked w r s := by
  rintro ⟨h,m,_⟩
  apply tower.bad
  apply (good_run h _).mp
  rw [m]
  exact (good_run h _).mpr (tower.earlier s earlier)

/-- If two paths eventually agree at the same clock, and both hit one
    particular nonrepeating vertex, they hit that vertex at the same clock. -/
theorem synchronized_gate {x y z i j t : Nat}
    (noRepeat : Function.Injective (fun h => run h z))
    (gateX : run i x=z) (gateY : run j y=z) (same : run t x=run t y) : i=j := by
  have eq : run (t+i+j) x=run (t+i+j) y := by
    rw [show t+i+j=t+(i+j) by omega,run_add t (i+j) x,run_add t (i+j) y,same]
  have a : run (t+i+j) x=run (t+j) z := by
    rw [show t+i+j=i+(t+j) by omega,run_add,gateX]
  have b : run (t+i+j) y=run (t+i) z := by
    rw [show t+i+j=j+(t+i) by omega,run_add,gateY]
  rw [a,b] at eq
  have f := noRepeat eq
  omega

/-- Two sources with equal clock lag and equal grade difference relative
    to the same reference lie in one augmented class. -/
theorem linked_of_matched_lags {w y r s h k i j : Nat}
    (left : run h (3^r*w)=run k y) (right : run i (3^s*w)=run j y)
    (time : h+j=i+k)
    (grade : r+odds h (3^r*w)+odds j y=s+odds i (3^s*w)+odds k y) :
    Linked w r s := by
  refine ⟨h+j,?_,?_⟩
  · calc
      _ = run (k+j) y := by rw [run_add h j,run_add k j,left]
      _ = run (j+k) y := by rw [Nat.add_comm]
      _ = run (h+j) (3^s*w) := by rw [time,run_add j k,run_add i k,right]
  · have a := odds_add k j y
    have b := odds_add j k y
    rw [Nat.add_comm j k] at b
    have c : odds (h+j) (3^r*w)=odds h (3^r*w)+odds j (run k y) := by
      rw [odds_add,left]
    have d : odds (h+j) (3^s*w)=odds i (3^s*w)+odds k (run j y) := by
      rw [time,odds_add,right]
    rw [c,d]
    omega

private theorem repeated_equal {z a b : Nat} (meet : run a z=run b z) (n : Nat) :
    run (n*a) z=run (n*b) z ∧
      odds (n*a) z+n*odds b z=odds (n*b) z+n*odds a z := by
  induction n with
  | zero => simp
  | succ n ih =>
    obtain ⟨old,grade⟩ := ih
    have shift := congrArg (fun v => run (n*a) v) meet
    have shiftGrade := congrArg (fun v => odds (n*a) v) meet
    change run (n*a) (run a z)=run (n*a) (run b z) at shift
    change odds (n*a) (run a z)=odds (n*a) (run b z) at shiftGrade
    have current : run (a+n*a) z=run (b+n*a) z := by
      rw [run_add,run_add]; exact shift
    have currGrade : odds (a+n*a) z+odds b z=odds (b+n*a) z+odds a z := by
      rw [odds_add,odds_add,shiftGrade]; omega
    have tailGrade : odds (n*a+b) z+n*odds b z=odds (n*b+b) z+n*odds a z := by
      rw [odds_add,odds_add,old]; omega
    constructor
    · rw [Nat.succ_mul,Nat.succ_mul,Nat.add_comm (n*a),current,Nat.add_comm b,run_add,run_add,old]
    · rw [Nat.add_comm a (n*a),Nat.add_comm b (n*a)] at currGrade
      rw [Nat.succ_mul,Nat.succ_mul,Nat.succ_mul,Nat.succ_mul]
      omega

private theorem period_laps {L z : Nat} (lap : run L z=z) (n : Nat) :
    run (n*L) z=z ∧ odds (n*L) z=n*odds L z := by
  induction n with
  | zero => simp [run,odds]
  | succ n ih =>
    rw [Nat.succ_mul,run_add,odds_add,ih.1,ih.2,lap,Nat.succ_mul]
    exact ⟨rfl,rfl⟩

/-- Two times at the same phase of a periodic orbit have an exact odd-count
    rate. Any period suffices, including a multiple of its least period. -/
theorem phase_rate {L z a b : Nat} (lap : run L z=z) (meet : run a z=run b z) :
    L*odds a z+b*odds L z=L*odds b z+a*odds L z := by
  have grade := (repeated_equal meet L).2
  rw [Nat.mul_comm L a,Nat.mul_comm L b,(period_laps lap a).2,(period_laps lap b).2] at grade
  omega

/-- The cycle charge used for possibly nontrivial positive cycles. It is
    invariant even for non-first hits and for a non-minimal designated period. -/
theorem periodic_charge {w r s L z h k : Nat} (lap : run L z=z)
    (left : run h (3^r*w)=z) (right : run k (3^s*w)=z) (linked : Linked w r s) :
    L*(r+odds h (3^r*w))+odds L z*k=L*(s+odds k (3^s*w))+odds L z*h := by
  obtain ⟨t,m,p⟩ := linked
  obtain ⟨now,counts⟩ := extend m p (h+k)
  have c₁ : t+(h+k)=h+(t+k) := by omega
  have c₂ : t+(h+k)=k+(t+h) := by omega
  have same : run (t+k) z=run (t+h) z := by
    calc
      _ = run (t+(h+k)) (3^r*w) := by rw [c₁,run_add h (t+k),left]
      _ = run (t+(h+k)) (3^s*w) := now
      _ = _ := by rw [c₂,run_add,right]
  have grade : r+odds h (3^r*w)+odds (t+k) z=s+odds k (3^s*w)+odds (t+h) z := by
    calc
      _ = r+odds (t+(h+k)) (3^r*w) := by rw [c₁,odds_add h (t+k),left,Nat.add_assoc]
      _ = s+odds (t+(h+k)) (3^s*w) := counts
      _ = _ := by rw [c₂,odds_add,right,Nat.add_assoc]
  have rate := phase_rate lap same
  have scaled := congrArg (fun u : Nat => L*u) grade
  simp only [Nat.mul_add] at scaled ⊢
  simp only [Nat.add_mul] at rate
  rw [Nat.mul_comm (odds L z) k,Nat.mul_comm (odds L z) h]
  omega

private theorem cycle_score (n h : Nat) (cycle : n=1 ∨ n=2) :
    2*odds h n+n=h+run h n := by
  induction h generalizing n with
  | zero => simp [odds,run]
  | succ h ih =>
    rcases cycle with e|e <;> subst n
    · have score := ih 2 (Or.inr rfl)
      simp only [odds,run,show step 1=2 by decide,show 1%2=1 by decide]; omega
    · have score := ih 1 (Or.inl rfl)
      simp only [odds,run,show step 2=1 by decide,show 2%2=0 by decide]; omega

private theorem cycle_laps (d : Nat) : run (2*d) 1=1 ∧ odds (2*d) 1=d := by
  induction d with
  | zero => decide
  | succ d ih =>
    rw [show 2*(d+1)=2*d+2 by omega,run_add,odds_add,ih.1,ih.2]
    simp only [show run 2 1=1 by decide,show odds 2 1=1 by decide]
    exact ⟨trivial,trivial⟩

private theorem endpoint_score {x h : Nat} (hit : run h x=1) (a : Nat) :
    2*odds (h+a) x+h+1=2*odds h x+(h+a)+run (h+a) x := by
  rw [run_add,odds_add,hit]
  have eq := cycle_score 1 a (Or.inl rfl)
  omega

/-- A computable, exact criterion for augmented linkage from any pair of
    actual hits, including hits obtained after extra turns on the 1,2 cycle. -/
theorem linked_iff_hit_balance {w r s h k : Nat}
    (left : run h (3^r*w)=1) (right : run k (3^s*w)=1) :
    Linked w r s ↔ 2*(r+odds h (3^r*w))+k=2*(s+odds k (3^s*w))+h := by
  constructor
  · rintro ⟨t,m,p⟩
    obtain ⟨m',p'⟩ := extend m p (h+k)
    have a := endpoint_score left (t+k)
    have b := endpoint_score right (t+h)
    rw [show h+(t+k)=t+(h+k) by omega] at a
    rw [show k+(t+h)=t+(h+k) by omega] at b
    omega
  · intro eq
    let u := s+odds k (3^s*w)
    let v := r+odds h (3^r*w)
    have clk : h+2*u=k+2*v := by dsimp [u,v]; omega
    obtain ⟨mu,ou⟩ := cycle_laps u
    obtain ⟨mv,ov⟩ := cycle_laps v
    refine ⟨h+2*u,?_,?_⟩
    · calc
        _ = run (2*u) 1 := by rw [run_add,left]
        _ = run (2*v) 1 := mu.trans mv.symm
        _ = run (h+2*u) (3^s*w) := by rw [clk,run_add,right]
    · have a : odds (h+2*u) (3^r*w)=odds h (3^r*w)+u := by rw [odds_add,left,ou]
      have b : odds (h+2*u) (3^s*w)=odds k (3^s*w)+v := by rw [clk,odds_add,right,ov]
      rw [a,b]; dsimp [u,v]; omega

private theorem upper_pow (h n : Nat) (hn : 0<n) :
    2^h*run h n≤4^(odds h n)*n := by
  induction h generalizing n with
  | zero => simp [run,odds]
  | succ h ih =>
    have pos : 0<step n := by unfold step; split <;> omega
    have st : 2*step n≤4^(n%2)*n := by
      by_cases hz : n%2=0
      · simp [step,hz]; omega
      · have ho : n%2=1 := by omega
        simp [step,ho]; omega
    calc
      _ = 2*(2^h*run h (step n)) := by simp [run,pow_succ]; ring
      _ ≤ 2*(4^(odds h (step n))*step n) := Nat.mul_le_mul_left _ (ih _ pos)
      _ = 4^(odds h (step n))*(2*step n) := by ring
      _ ≤ 4^(odds h (step n))*(4^(n%2)*n) := Nat.mul_le_mul_left _ st
      _ = _ := by simp [odds,pow_add]; ring

private theorem four_pow (n : Nat) : 4^n=(2:Nat)^(2*n) := by rw [pow_mul]; rfl

/-- Finite ceiling for every augmented neighbor of a source with an actual
    hit. The earlier stopping certificate belongs only to the reference. -/
theorem good_reference_bound {w r s k : Nat} (hw : 0<w)
    (right : run k (3^s*w)=1) (linked : Linked w r s) :
    4^r * 2^k ≤ 4^(s+odds k (3^s*w))*3^r*w := by
  obtain ⟨t,meet,paid⟩ := linked
  have gy : Good (3^s*w) := ⟨k,right⟩
  have gx : Good (3^r*w) := (good_run t _).mp (meet ▸ (good_run t _).mpr gy)
  obtain ⟨h,hit⟩ := gx
  have balance := (linked_iff_hit_balance hit right).mp ⟨t,meet,paid⟩
  have powers := congrArg (fun v : Nat => (2:Nat)^v) balance
  simp only [pow_add,←four_pow] at powers
  have cap := upper_pow h (3^r*w) (Nat.mul_pos (Nat.pow_pos (by decide)) hw)
  rw [hit,Nat.mul_one] at cap
  apply Nat.le_of_mul_le_mul_left (c:=4^(odds h (3^r*w))) _ (Nat.pow_pos (by decide))
  calc
    _ = 4^(r+odds h (3^r*w))*2^k := by rw [pow_add]; ring
    _ = 4^(s+odds k (3^s*w))*2^h := by simpa only [pow_add] using powers
    _ ≤ 4^(s+odds k (3^s*w))*(4^(odds h (3^r*w))*(3^r*w)) := Nat.mul_le_mul_left _ cap
    _ = _ := by ring

theorem no_link_to_one (r : Nat) (hr : 0<r) : ¬Linked 1 r 0 := by
  intro link
  have cap := good_reference_bound (by decide : 0<1) (s:=0) (k:=0) (by decide) link
  simp only [odds,pow_zero,Nat.add_zero,Nat.one_mul,Nat.mul_one] at cap
  exact (Nat.not_le_of_lt (Nat.pow_lt_pow_left (by decide : 3<4) (by omega : r≠0))) cap

#print axioms linked_equivalence
#print axioms linked_double
#print axioms first_tower_minimum
#print axioms linked_of_matched_lags
#print axioms phase_rate
#print axioms periodic_charge
#print axioms synchronized_gate
#print axioms linked_iff_hit_balance
#print axioms good_reference_bound
#print axioms no_link_to_one
end Collatz.AugmentedMerger
