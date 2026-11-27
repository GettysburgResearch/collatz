import PhaseReturn
import GradedMinima

/-! All thirteen ordinary phase progressions. A finite packet checks real
upper and lower trajectories at their bases. The conclusion uses only the
height floor at the specific input under examination. -/
namespace Collatz.PhaseFamilies
open Collatz.SourceDeletion Collatz.MinimumFailure Collatz.PhaseReturn
set_option exponentiation.threshold 65536
set_option maxRecDepth 65536

structure Row where
  gap : Nat
  clock : Nat
  k : Nat
  hit : Nat

private def rows : List Row := [
  ⟨17,213,62,1153⟩,  ⟨23,147,39,675⟩,   ⟨24,1710,536,0⟩, ⟨25,1205,375,0⟩,
  ⟨26,1844,578,0⟩,  ⟨27,283,81,1426⟩,  ⟨28,1582,494,0⟩, ⟨29,1539,480,0⟩,
  ⟨30,330,95,2034⟩, ⟨31,545,163,0⟩,    ⟨33,811,247,0⟩,  ⟨37,1343,415,0⟩,
  ⟨48,1374,421,0⟩]

def row (i : Fin 13) : Row := rows.getD i.val ⟨0,0,0,0⟩

def base (r : Row) : Nat := (2^r.clock-15-2^(r.gap+2))/81

def source (r : Row) (t : Nat) : Nat := base r+2^r.clock*shift t

def Floor (z : Nat) : Prop := ∀ n, 0<n → 2^40*n<z → Good n

/-- An independently decidable ordinary base packet, including the
exceptional cases that use an actual hit in place of an initial contraction. -/
def BaseCheck (r : Row) : Prop :=
  1≤r.k ∧ base r%48=17 ∧ 81*base r+15+2^(r.gap+2)=2^r.clock ∧
  run r.clock (3*base r)=1 ∧ odds r.clock (3*base r)=3 ∧
  run r.clock (base r)=3^(2*r.k+2)-17 ∧ odds r.clock (base r)=2*r.k+6 ∧
  2^40*2^(3*r.k+1)<2^81*base r ∧
  (run r.hit (base r)=1 ∨ 2^40*(2^(3*r.k+1)-5)<base r)

instance (r : Row) : Decidable (BaseCheck r) := by unfold BaseCheck; infer_instance

set_option maxHeartbeats 9000000 in
theorem all_bases : ∀ i : Fin 13, BaseCheck (row i) := by decide

private theorem nonzero_visitor {k : Nat} (kp : 1≤k) : 0<2^(3*k+1)-5 := by
  have bound : 8≤(2:Nat)^(3*k+1) :=
    Nat.pow_le_pow_right (by decide : 0<(2:Nat)) (show 3≤_ by omega)
  omega

private theorem floor_progression (r : Row) (packet : BaseCheck r) (t : Nat)
    (floor : Floor (source r t)) : Good (source r t) := by
  obtain ⟨kp,_,shape,_,_,lo,oc,margin,small⟩ := packet
  have link := repeated_phase (z:=base r) (H:=r.clock) (k:=r.k) kp lo oc t
  cases t with
  | zero =>
    change Good (base r)
    rcases small with direct|cheap
    · exact ⟨r.hit,direct⟩
    · apply link.mpr
      exact floor _ (nonzero_visitor (by simpa using kp)) (by simpa [source,shift] using cheap)
  | succ t =>
    let d := t+1
    let w := 2^(3*(r.k+567*d)+1)-5
    have exp : 3*(r.k+567*d)+1=(3*r.k+1)+1701*d := by omega
    have price : 2^40*w<2^(1782*d)*base r := calc
      _ ≤ 2^40*2^(3*(r.k+567*d)+1) := Nat.mul_le_mul_left _ (Nat.sub_le _ _)
      _ = (2^40*2^(3*r.k+1))*2^(1701*d) := by rw [exp,pow_add,Nat.mul_assoc]
      _ < (2^81*base r)*2^(1701*d) := Nat.mul_lt_mul_of_pos_right margin (Nat.two_pow_pos _)
      _ = 2^(81+1701*d)*base r := by rw [pow_add]; ring
      _ ≤ _ := Nat.mul_le_mul_right _ (Nat.pow_le_pow_right (by decide : 0<(2:Nat))
                  (show 81+1701*d≤1782*d by dsimp [d]; omega))
    have lower : 2^(1782*d)*base r≤source r d := calc
      _ = base r+(81*base r)*shift d := by rw [←shift_eq]; ring
      _ ≤ _ := Nat.add_le_add_left (Nat.mul_le_mul_right _ (show 81*base r≤2^r.clock by rw [←shape]; exact (Nat.le_add_right _ 15).trans (Nat.le_add_right _ _))) _
    exact link.mpr (floor w (nonzero_visitor (by omega)) (price.trans_le lower))

/-- Every supplied parameter in each of the thirteen rows obeys the
ordinary least-height exclusion. -/
theorem closed_families (i : Fin 13) (t : Nat) :
    Floor (source (row i) t) → Good (source (row i) t) :=
  floor_progression _ (all_bases i) t

theorem prior26 : Good ((2^62-15-2^28)/81) := ⟨338,by decide⟩

private theorem pure (d : Nat) : run d (2^d)=1 ∧ odds d (2^d)=0 := by
  induction d with
  | zero => decide
  | succ d ih =>
    have stepP : step (2^d*2)=2^d := by unfold step; split <;> omega
    rw [pow_succ,run,odds,stepP,ih.1,ih.2]; omega

private theorem natOdds (h n u : Nat) : odds h (n+2^h*u)=odds h n := by
  have same := (Collatz.SignedBudget.signed_lift h (n:Int) (u:Int)).2
  have cast : ((n+2^h*u:Nat):Int)=(n:Int)+2^h*(u:Int) := by push_cast; rfl
  rw [←cast,(Collatz.SignedBudget.physical _ _).2,(Collatz.SignedBudget.physical _ _).2] at same
  exact same

/-- The supplied upper really reaches one after three odd inputs at every
parameter, and the parent has the stated rank-three exponential form. -/
theorem upper_families (i : Fin 13) (t : Nat) :
    let r := row i
    let z := source r t
    81*z+15+2^(r.gap+2)=2^(r.clock+1782*t) ∧
    run (r.clock+1782*t) (3*z)=1 ∧ odds (r.clock+1782*t) (3*z)=3 := by
  let r := row i
  obtain ⟨_,_,shape,hit,paid,_⟩ := all_bases i
  change 81*base r+15+2^(r.gap+2)=2^r.clock at shape
  change run r.clock (3*base r)=1 at hit
  change odds r.clock (3*base r)=3 at paid
  have form : 81*source r t+15+2^(r.gap+2)=2^(r.clock+1782*t) := calc
    _ = (81*base r+15+2^(r.gap+2))+2^r.clock*(81*shift t) := by unfold source; ring
    _ = 2^r.clock*(81*shift t+1) := by rw [shape]; ring
    _ = _ := by rw [shift_eq,pow_add]
  have rewrite : 3*source r t=3*base r+2^r.clock*(3*shift t) := by unfold source; ring
  have a := lift r.clock (3*base r) (3*shift t)
  have b := natOdds r.clock (3*base r) (3*shift t)
  rw [←rewrite,hit,paid] at a
  rw [←rewrite,paid] at b
  have val : run r.clock (3*source r t)=2^(1782*t) := by rw [a,←shift_eq]; ring
  obtain ⟨endV,endP⟩ := Collatz.RankTwoControl.append r.clock (1782*t) (3*source r t)
  rw [val,(pure _).1] at endV
  rw [b,val,(pure _).2] at endP
  exact ⟨form,endV,endP⟩

private theorem shift_three (t : Nat) : 3 ∣ shift t := by
  induction t with
  | zero => exact ⟨0,rfl⟩
  | succ t ih =>
    obtain ⟨v,eqn⟩ := ih
    refine ⟨2^1782*v+(2^1782-1)/243,?_⟩
    rw [shift,eqn]; ring

private def early : Nat → Nat → Bool
  | 0, _ => true
  | h+1, x => (1<x) && early h (step x)

set_option maxHeartbeats 9000000 in
private theorem early_bases : ∀ i : Fin 13,
    4≤(row i).clock ∧ early (row i).clock (3*base (row i))=true := by decide

private theorem before {H x : Nat} (e : early H x=true) (h : Nat) (lt : h<H) : 1<run h x := by
  induction H generalizing x h with
  | zero => omega
  | succ H ih =>
    simp only [early,Bool.and_eq_true,decide_eq_true_eq] at e
    cases h with
    | zero => exact e.1
    | succ h => exact ih e.2 h (by omega)

theorem canonical_families (i : Fin 13) (t : Nat) : source (row i) t%48=17 := by
  let r := row i
  obtain ⟨_,baseClass,_⟩ := all_bases i
  obtain ⟨v,eqn⟩ := shift_three t
  have left : 4≤r.clock := (early_bases i).1
  obtain ⟨d,clockEq⟩ := Nat.exists_eq_add_of_le left
  change (base r+2^r.clock*shift t)%48=17
  have prod : 2^r.clock*shift t=48*(2^d*v) := by rw [clockEq,pow_add,eqn]; ring
  rw [prod]
  change base r%48=17 at baseClass
  omega

theorem first_upper (i : Fin 13) (t h : Nat) (lt : h<(row i).clock+1782*t) :
    1<run h (3*source (row i) t) := by
  let r := row i
  have simpZ : 3*source r t=3*base r+2^r.clock*(3*shift t) := by unfold source; ring
  by_cases earlier : h<r.clock
  · obtain ⟨d,hd⟩ := Nat.exists_eq_add_of_le earlier.le
    have written : 3*source r t=3*base r+2^h*(2^d*(3*shift t)) := by
      rw [simpZ,hd,pow_add,Nat.mul_assoc]
    rw [written,lift]
    exact (before (early_bases i).2 h earlier).trans_le (Nat.le_add_right _ _)
  · obtain ⟨k,hk⟩ := Nat.exists_eq_add_of_le (show r.clock≤h by omega)
    obtain ⟨_,_,_,hit,paid,_⟩ := all_bases i
    change run r.clock (3*base r)=1 at hit
    change odds r.clock (3*base r)=3 at paid
    have a := lift r.clock (3*base r) (3*shift t)
    rw [←simpZ,hit,paid] at a
    have val : run r.clock (3*source r t)=2^(1782*t) := by rw [a,←shift_eq]; ring
    have le : k<1782*t := by change h<r.clock+1782*t at lt; omega
    obtain ⟨u,ku⟩ := Nat.exists_eq_add_of_le le
    have pow : (2:Nat)^(1782*t)=2^k+2^k*(2^(u+1)-1) := by
      have pos := Nat.two_pow_pos (u+1)
      rw [show 1782*t=k+(u+1) by omega,pow_add]
      rw [show 2^k+2^k*(2^(u+1)-1)=2^k*(1+(2^(u+1)-1)) by ring]
      congr 1; omega
    obtain ⟨v,_⟩ := Collatz.RankTwoControl.append r.clock k (3*source r t)
    rw [val,pow,lift,(pure _).1,(pure _).2] at v
    rw [hk,v]
    have up : 2≤(2:Nat)^(u+1) :=
      Nat.pow_le_pow_right (by decide : 0<(2:Nat)) (show 1≤u+1 by omega)
    norm_num at *

#print axioms all_bases
#print axioms closed_families
#print axioms prior26
#print axioms upper_families
#print axioms canonical_families
#print axioms first_upper
end Collatz.PhaseFamilies
