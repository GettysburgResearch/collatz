/-
Finite completeness for arbitrary bounded insertions/deletions between
two actual positive Collatz trajectories. No convergence or universal
edit-budget assumption is imported. Matching blocks may be arbitrarily
long in the input certificate; their length is proved bounded here.
-/
import Std

set_option autoImplicit false
set_option maxHeartbeats 2000000

namespace CollatzJointEdit

def shortcut (n : Nat) : Nat :=
  if n % 2 = 0 then n / 2 else (3*n+1)/2

def orbit (n : Nat) : Nat → Nat
  | 0 => n
  | k+1 => orbit (shortcut n) k

theorem orbit_add (x a b : Nat) : orbit x (a+b)=orbit (orbit x a) b := by
  induction a generalizing x with
  | zero => simp [orbit]
  | succ a ih => simpa [orbit,Nat.add_assoc,Nat.add_comm,Nat.add_left_comm] using ih (shortcut x)

theorem orbit_succ (x k : Nat) : orbit x (k+1)=shortcut (orbit x k) := by
  induction k generalizing x with
  | zero => rfl
  | succ k ih => simpa [orbit] using ih (shortcut x)

def SameRun (x y : Nat) : Nat → Prop
  | 0 => True
  | k+1 => x%2=y%2 ∧ SameRun (shortcut x) (shortcut y) k

instance (x y k : Nat) : Decidable (SameRun x y k) := by
  induction k generalizing x y with
  | zero => exact isTrue True.intro
  | succ k ih =>
      change Decidable (x%2=y%2 ∧ SameRun (shortcut x) (shortcut y) k)
      exact instDecidableAnd

theorem same_run_affine (x y k : Nat) (same : SameRun x y k) :
    ∃ p, (2:Int)^k*((orbit x k:Int)-(orbit y k:Int))=
      (3:Int)^p*((x:Int)-(y:Int)) := by
  induction k generalizing x y with
  | zero => exact ⟨0,by simp [orbit]⟩
  | succ k ih =>
      obtain ⟨parity,tail⟩ := same
      obtain ⟨p,eqn⟩ := ih _ _ tail
      by_cases even : x%2=0
      · have evenY : y%2=0 := by omega
        have edge : 2*((shortcut x:Int)-(shortcut y:Int))=(x:Int)-(y:Int) := by
          simp only [shortcut,even,evenY,ite_true]
          omega
        refine ⟨p,?_⟩
        simp only [orbit,Int.pow_succ]
        have scale := congrArg (fun z : Int => (3:Int)^p*z) edge
        grind
      · have oddX : x%2=1 := by omega
        have oddY : y%2=1 := by omega
        have notEvenY : ¬y%2=0 := by omega
        have edge : 2*((shortcut x:Int)-(shortcut y:Int))=
            3*((x:Int)-(y:Int)) := by
          simp only [shortcut,even,notEvenY,ite_false]
          omega
        refine ⟨p+1,?_⟩
        simp only [orbit,Int.pow_succ]
        have scale := congrArg (fun z : Int => (3:Int)^p*z) edge
        grind

theorem same_run_precision (x y k : Nat) (same : SameRun x y k) :
    2^k ∣ ((x:Int)-(y:Int)).natAbs := by
  obtain ⟨p,eqn⟩ := same_run_affine x y k same
  have mag := congrArg Int.natAbs eqn
  have transport : 2^k*((orbit x k:Int)-(orbit y k:Int)).natAbs=
      3^p*((x:Int)-(y:Int)).natAbs := by
    simpa [Int.natAbs_mul,Int.natAbs_pow] using mag
  have divides : 2^k ∣ 3^p*((x:Int)-(y:Int)).natAbs :=
    ⟨_,transport.symm⟩
  exact (Nat.Coprime.pow k p (by decide : Nat.Coprime 2 3)).dvd_of_dvd_mul_left divides

theorem same_run_injective (x y k : Nat) (same : SameRun x y k)
    (endpoint : orbit x k=orbit y k) : x=y := by
  obtain ⟨p,eqn⟩ := same_run_affine x y k same
  have positive : (0:Int)<3^p := Int.pow_pos (by decide)
  rw [endpoint] at eqn
  simp only [Int.sub_self,Int.mul_zero] at eqn
  have zero : (x:Int)-(y:Int)=0 := by
    have product := Int.mul_eq_zero.mp eqn.symm
    rcases product with h|h
    · omega
    · exact h
  omega

theorem same_run_clock (x y k N : Nat) (same : SameRun x y k)
    (distinct : x≠y) (hx : x<2^N) (hy : y<2^N) : k<N := by
  have positive : 0<((x:Int)-(y:Int)).natAbs := by omega
  have small : ((x:Int)-(y:Int)).natAbs<2^N := by omega
  have lower := Nat.le_of_dvd positive (same_run_precision x y k same)
  apply Classical.byContradiction
  intro bad
  have powers := Nat.pow_le_pow_right (by decide : 0<2) (show N≤k by omega)
  omega

theorem shortcut_le_double (x : Nat) : shortcut x≤2*x := by
  unfold shortcut
  split <;> omega

theorem orbit_height (x k N : Nat) (height : x<2^N) : orbit x k<2^(N+k) := by
  induction k generalizing x N with
  | zero => simpa [orbit] using height
  | succ k ih =>
      have step := shortcut_le_double x
      have taller : shortcut x<2^(N+1) := by rw [Nat.pow_succ]; omega
      simpa [orbit,Nat.add_assoc,Nat.add_comm,Nat.add_left_comm] using ih (shortcut x) (N+1) taller

theorem block_edit_height (x y k N : Nat) (same : SameRun x y k)
    (distinct : x≠y) (hx : x<2^N) (hy : y<2^N) :
    orbit x k<2^(2*N) ∧ orbit y k<2^(2*N) ∧
    shortcut (orbit x k)<2^(2*N) ∧ shortcut (orbit y k)<2^(2*N) := by
  have clock := same_run_clock x y k N same distinct hx hy
  have ax := orbit_height x k N hx
  have ay := orbit_height y k N hy
  have sx := shortcut_le_double (orbit x k)
  have sy := shortcut_le_double (orbit y k)
  have powers := Nat.pow_le_pow_right (by decide : 0<2) (show N+k+1≤2*N by omega)
  have smaller := Nat.pow_le_pow_right (by decide : 0<2) (show N+k≤2*N by omega)
  rw [Nat.pow_succ] at powers
  omega

/-- A first-merger alignment, normalized into same-parity blocks followed
by one unmatched actual shortcut step on either side. -/
inductive Repair : Nat → Nat → Nat → Nat → Prop where
  | done (x : Nat) : Repair x x 0 0
  | left {x y k t c : Nat} : x≠y → SameRun x y k →
      Repair (shortcut (orbit x k)) (orbit y k) t c →
      Repair x y (t+1) (k+1+c)
  | right {x y k t c : Nat} : x≠y → SameRun x y k →
      Repair (orbit x k) (shortcut (orbit y k)) t c →
      Repair x y (t+1) (k+1+c)

/-- Ungrouped literal alignment. Distinctness trims it at its first
ordinary meeting; matching columns have zero edit cost. -/
inductive Alignment : Nat → Nat → Nat → Nat → Prop where
  | done (x : Nat) : Alignment x x 0 0
  | left {x y t c : Nat} : x≠y → Alignment (shortcut x) y t c →
      Alignment x y (t+1) (c+1)
  | right {x y t c : Nat} : x≠y → Alignment x (shortcut y) t c →
      Alignment x y (t+1) (c+1)
  | common {x y t c : Nat} : x≠y → x%2=y%2 →
      Alignment (shortcut x) (shortcut y) t c → Alignment x y t (c+1)

theorem prepend_common {x y t c : Nat} (distinct : x≠y) (parity : x%2=y%2)
    (repair : Repair (shortcut x) (shortcut y) t c) : Repair x y t (c+1) := by
  generalize hx : shortcut x=u at repair
  generalize hy : shortcut y=v at repair
  cases repair with
  | done u =>
      have same : SameRun x y 1 := ⟨parity,True.intro⟩
      have equal : orbit x 1=orbit y 1 := by simpa [orbit] using hx.trans hy.symm
      exact False.elim (distinct (same_run_injective x y 1 same equal))
  | @left u v k t c _ same tail =>
      rw [←hx,←hy] at same tail
      have combined : SameRun x y (k+1) := ⟨parity,same⟩
      have result := Repair.left distinct combined tail
      simpa [orbit,Nat.add_assoc,Nat.add_comm,Nat.add_left_comm] using result
  | @right u v k t c _ same tail =>
      rw [←hx,←hy] at same tail
      have combined : SameRun x y (k+1) := ⟨parity,same⟩
      have result := Repair.right distinct combined tail
      simpa [orbit,Nat.add_assoc,Nat.add_comm,Nat.add_left_comm] using result

theorem alignment_normalizes {x y t c : Nat} (alignment : Alignment x y t c) :
    Repair x y t c := by
  induction alignment with
  | done x => exact Repair.done x
  | @left x y t c distinct _ ih =>
      have result := Repair.left (k:=0) distinct True.intro ih
      simpa [orbit,Nat.add_comm] using result
  | @right x y t c distinct _ ih =>
      have result := Repair.right (k:=0) distinct True.intro ih
      simpa [orbit,Nat.add_comm] using result
  | common distinct parity _ ih => exact prepend_common distinct parity ih

def budget (N : Nat) : Nat → Nat
  | 0 => 0
  | t+1 => N+budget (2*N) t

theorem budget_closed (N t : Nat) : budget N t=N*(2^t-1) := by
  induction t generalizing N with
  | zero => simp [budget]
  | succ t ih =>
      rw [budget,ih]
      have pos := Nat.pow_pos (by decide : 0<2) (n:=t)
      have closedStep : 2^(t+1)-1=1+2*(2^t-1) := by rw [Nat.pow_succ]; omega
      rw [closedStep,Nat.mul_add,Nat.mul_one]
      ac_rfl

theorem repair_clock {x y t c N : Nat} (repair : Repair x y t c)
    (hx : x<2^N) (hy : y<2^N) : c≤budget N t := by
  induction repair generalizing N with
  | done x => simp [budget]
  | @left x y k t c distinct same tail ih =>
      have clock := same_run_clock x y k N same distinct hx hy
      have heights := block_edit_height x y k N same distinct hx hy
      have rest := ih heights.2.2.1 heights.2.1
      simp only [budget]
      omega
  | @right x y k t c distinct same tail ih =>
      have clock := same_run_clock x y k N same distinct hx hy
      have heights := block_edit_height x y k N same distinct hx hy
      have rest := ih heights.1 heights.2.2.2
      simp only [budget]
      omega

theorem repair_ordinary {x y t c : Nat} (repair : Repair x y t c) :
    ∃ a b, a≤c ∧ b≤c ∧ orbit x a=orbit y b := by
  induction repair with
  | done x => exact ⟨0,0,by omega,by omega,rfl⟩
  | @left x y k t c distinct same tail ih =>
      obtain ⟨a,b,ha,hb,eqn⟩ := ih
      refine ⟨k+1+a,k+b,by omega,by omega,?_⟩
      calc
        orbit x (k+1+a)=orbit (orbit x (k+1)) a := orbit_add x (k+1) a
        _=orbit (shortcut (orbit x k)) a := by rw [orbit_succ]
        _=orbit (orbit y k) b := eqn
        _=orbit y (k+b) := (orbit_add y k b).symm
  | @right x y k t c distinct same tail ih =>
      obtain ⟨a,b,ha,hb,eqn⟩ := ih
      refine ⟨k+a,k+1+b,by omega,by omega,?_⟩
      calc
        orbit x (k+a)=orbit (orbit x k) a := orbit_add x k a
        _=orbit (shortcut (orbit y k)) b := eqn
        _=orbit (orbit y (k+1)) b := by rw [orbit_succ]
        _=orbit y (k+1+b) := (orbit_add y (k+1) b).symm

/-- The search scans every location in a proved finite common block,
then recursively tries an unmatched step on either side. -/
def seek (N : Nat) : Nat → Nat → Nat → Bool
  | 0,x,y => decide (x=y)
  | t+1,x,y =>
      if x=y then true else
      (List.range N).any fun k => decide (SameRun x y k) &&
        (seek (2*N) t (shortcut (orbit x k)) (orbit y k) ||
         seek (2*N) t (orbit x k) (shortcut (orbit y k)))

theorem seek_sound (N t x y : Nat) (accepted : seek N t x y=true) :
    ∃ e c, e≤t ∧ Repair x y e c := by
  induction t generalizing N x y with
  | zero =>
      have equal : x=y := by simpa [seek] using accepted
      subst y
      exact ⟨0,0,by omega,Repair.done x⟩
  | succ t ih =>
      by_cases equal : x=y
      · subst y
        exact ⟨0,0,by omega,Repair.done x⟩
      · have options : ∃ k, k<N ∧ SameRun x y k ∧
            (seek (2*N) t (shortcut (orbit x k)) (orbit y k)=true ∨
             seek (2*N) t (orbit x k) (shortcut (orbit y k))=true) := by
          simpa [seek,equal] using accepted
        obtain ⟨k,_,same,left|right⟩ := options
        · obtain ⟨e,c,he,repair⟩ := ih _ _ _ left
          exact ⟨e+1,k+1+c,by omega,Repair.left equal same repair⟩
        · obtain ⟨e,c,he,repair⟩ := ih _ _ _ right
          exact ⟨e+1,k+1+c,by omega,Repair.right equal same repair⟩

theorem seek_complete {x y e c N t : Nat} (repair : Repair x y e c)
    (hx : x<2^N) (hy : y<2^N) (funded : e≤t) : seek N t x y=true := by
  induction repair generalizing N t with
  | done x => cases t <;> simp [seek]
  | @left x y k e c distinct same tail ih =>
      cases t with
      | zero => omega
      | succ t =>
          have clock := same_run_clock x y k N same distinct hx hy
          have heights := block_edit_height x y k N same distinct hx hy
          have rest := ih heights.2.2.1 heights.2.1 (show e≤t by omega)
          simp only [seek,distinct,ite_false,List.any_eq_true]
          refine ⟨k,by simpa using clock,?_⟩
          simp [same,rest]
  | @right x y k e c distinct same tail ih =>
      cases t with
      | zero => omega
      | succ t =>
          have clock := same_run_clock x y k N same distinct hx hy
          have heights := block_edit_height x y k N same distinct hx hy
          have rest := ih heights.1 heights.2.2.2 (show e≤t by omega)
          simp only [seek,distinct,ite_false,List.any_eq_true]
          refine ⟨k,by simpa using clock,?_⟩
          simp [same,rest]

theorem seek_iff (N t x y : Nat) (hx : x<2^N) (hy : y<2^N) :
    seek N t x y=true ↔ ∃ e c, e≤t ∧ Repair x y e c := by
  constructor
  · exact seek_sound N t x y
  · rintro ⟨e,c,funded,repair⟩
    exact seek_complete repair hx hy funded

theorem budget_mono (N e t : Nat) (funded : e≤t) : budget N e≤budget N t := by
  rw [budget_closed,budget_closed]
  have powers := Nat.pow_le_pow_right (by decide : 0<2) funded
  exact Nat.mul_le_mul_left N (Nat.sub_le_sub_right powers 1)

theorem seek_ordinary (N t x y : Nat) (hx : x<2^N) (hy : y<2^N)
    (accepted : seek N t x y=true) :
    ∃ a b, a≤N*(2^t-1) ∧ b≤N*(2^t-1) ∧ orbit x a=orbit y b := by
  obtain ⟨e,c,funded,repair⟩ := seek_sound N t x y accepted
  obtain ⟨a,b,ha,hb,eqn⟩ := repair_ordinary repair
  have bounded := repair_clock repair hx hy
  have monotone := budget_mono N e t funded
  simp only [budget_closed] at bounded monotone
  exact ⟨a,b,by omega,by omega,eqn⟩

theorem seek_rejection_complete (N t x y : Nat) (hx : x<2^N) (hy : y<2^N)
    (rejected : seek N t x y=false) :
    ∀ e c, e≤t → ¬Repair x y e c := by
  intro e c funded repair
  have accepted := seek_complete repair hx hy funded
  rw [rejected] at accepted
  contradiction

theorem ordinary_alignment_clock {x y t c N : Nat} (alignment : Alignment x y t c)
    (hx : x<2^N) (hy : y<2^N) : c≤N*(2^t-1) := by
  have bound := repair_clock (alignment_normalizes alignment) hx hy
  simpa [budget_closed] using bound

theorem orbit_one_even (k : Nat) : orbit 1 (k+k)=1 := by
  induction k with
  | zero => rfl
  | succ k ih =>
      have clocks : k+1+(k+1)=(k+k)+2 := by omega
      rw [clocks,orbit_add,ih]
      decide

theorem complete_witness_transport (N t x y L : Nat)
    (hx : x<2^N) (hy : y<2^N) (accepted : seek N t x y=true)
    (sourceWitness : orbit y L=1) :
    ∃ K, K≤2*N*(2^t-1)+L ∧ orbit x K=1 := by
  obtain ⟨a,b,ha,hb,merger⟩ := seek_ordinary N t x y hx hy accepted
  have doubled : 2*N*(2^t-1)=2*(N*(2^t-1)) := by ac_rfl
  refine ⟨a+(L+b),by rw [doubled]; omega,?_⟩
  calc
    orbit x (a+(L+b))=orbit (orbit x a) (L+b) := orbit_add x a (L+b)
    _=orbit (orbit y b) (L+b) := by rw [merger]
    _=orbit y (b+(L+b)) := (orbit_add y b (L+b)).symm
    _=orbit y (L+(b+b)) := by congr 1; omega
    _=orbit (orbit y L) (b+b) := orbit_add y L (b+b)
    _=orbit 1 (b+b) := by rw [sourceWitness]
    _=1 := orbit_one_even b

#print axioms orbit_add
#print axioms orbit_succ
#print axioms same_run_affine
#print axioms same_run_precision
#print axioms same_run_injective
#print axioms same_run_clock
#print axioms shortcut_le_double
#print axioms orbit_height
#print axioms block_edit_height
#print axioms prepend_common
#print axioms alignment_normalizes
#print axioms budget_closed
#print axioms repair_clock
#print axioms repair_ordinary
#print axioms seek_sound
#print axioms seek_complete
#print axioms seek_iff
#print axioms budget_mono
#print axioms seek_ordinary
#print axioms seek_rejection_complete
#print axioms ordinary_alignment_clock
#print axioms orbit_one_even
#print axioms complete_witness_transport

end CollatzJointEdit
