import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic.Ring

/-!
An unbounded ordinary control for four bounded-grade neighbours.
The Collatz shortcut grading counts odd departures, including the initial
state if it is odd. No bounded-cycle property is imposed on the source.
-/

namespace FourMarks

def shortcut (x : ℕ) : ℕ := if x % 2 = 0 then x/2 else (3*x+1)/2

def run : ℕ → ℕ → ℕ × ℕ
  | 0, x => (x,0)
  | n+1, x =>
    let (y,k) := run n (shortcut x)
    (y,k+x%2)

/-- The recorded parity bits are required on the actual source. -/
def Follows : List Bool → ℕ → ℕ → Prop
  | [], x, y => x=y
  | false::w, x, y => x%2=0 ∧ Follows w (x/2) y
  | true::w, x, y => x%2=1 ∧ Follows w ((3*x+1)/2) y

theorem follows_run {w : List Bool} {x y : ℕ} (h : Follows w x y) :
    run w.length x=(y,w.count true) := by
  induction w generalizing x with
  | nil => simpa [Follows,run] using h
  | cons b w ih =>
    cases b
    · obtain ⟨hb,hh⟩ := h
      simp [run,shortcut,hb,ih hh]
    · obtain ⟨hb,hh⟩ := h
      simp [run,shortcut,hb,ih hh]

theorem run_add (m n x : ℕ) :
    run (m+n) x = ((run n (run m x).1).1,(run n (run m x).1).2+(run m x).2) := by
  induction m generalizing x with
  | zero => simp [run]
  | succ m ih =>
    rw [Nat.succ_add]
    simp only [run,ih]
    cases run m (shortcut x) with
    | mk y k => simp [Nat.add_assoc]

theorem run_power (a : ℕ) : run a (2^a)=(1,0) := by
  induction a with
  | zero => rfl
  | succ a ih => simp [run,shortcut,pow_succ,ih]

def parameter : ℕ → ℕ
  | 0 => 151
  | n+1 => 262144*parameter n+184471

def source (n : ℕ) : ℕ := 1024*parameter n+711

theorem parameter_power (n : ℕ) : 27*parameter n+19=2^(18*n+12) := by
  induction n with
  | zero => decide
  | succ n ih =>
    rw [show 18*(n+1)+12=(18*n+12)+18 by omega,pow_add,← ih]
    simp only [parameter]
    ring

theorem source_power (n : ℕ) : 27*source n+259=2^(18*n+22) := by
  rw [show 18*n+22=(18*n+12)+10 by omega,pow_add,←parameter_power]
  simp only [source]
  ring

private theorem prefix_minus (v : ℕ) :
    Follows [false,true,true,false,false,false,false,false,true]
      (1024*v+711-1) (54*v+38) := by
  simp only [Follows]
  omega

private theorem prefix_plus (v : ℕ) :
    Follows [false,false,false,true,false,true,true]
      (1024*v+711+1) (216*v+152) := by
  simp only [Follows]
  omega

private theorem prefix_double (v : ℕ) :
    Follows [true,false,false,true,false,false,false,false,false,true]
      (2*(1024*v+711)-1) (54*v+38) := by
  simp only [Follows]
  omega

private theorem prefix_triple (v : ℕ) :
    Follows [true,false,false,false,false,false,false,false,true]
      (3*(1024*v+711)) (54*v+38) := by
  simp only [Follows]
  omega

/-- At this unbounded family the four actual marks reach one with grades
    three, three, three and two. -/
theorem four_hits (n : ℕ) :
    run (18*n+22) (source n-1) = (1,3) ∧
    run (18*n+22) (source n+1) = (1,3) ∧
    run (18*n+23) (2*source n-1) = (1,3) ∧
    run (18*n+22) (3*source n) = (1,2) := by
  let v := parameter n
  have hpow : 27*v+19=2^(18*n+12) := parameter_power n
  have pa : 54*v+38=2^(18*n+13) := by
    rw [show 18*n+13=18*n+12+1 by omega,pow_succ,←hpow]
    ring
  have pb : 216*v+152=2^(18*n+15) := by
    rw [show 18*n+15=(18*n+12)+3 by omega,pow_add,←hpow]
    ring
  have hm : run 9 (source n-1) = (54*v+38,3) := follows_run (prefix_minus v)
  have hp : run 7 (source n+1) = (216*v+152,3) := follows_run (prefix_plus v)
  have hd : run 10 (2*source n-1) = (54*v+38,3) := follows_run (prefix_double v)
  have ht : run 9 (3*source n) = (54*v+38,2) := follows_run (prefix_triple v)
  constructor
  · rw [show 18*n+22=9+(18*n+13) by omega,run_add,hm]
    simp [pa,run_power]
  constructor
  · rw [show 18*n+22=7+(18*n+15) by omega,run_add,hp]
    simp [pb,run_power]
  constructor
  · rw [show 18*n+23=10+(18*n+13) by omega,run_add,hd]
    simp [pa,run_power]
  · rw [show 18*n+22=9+(18*n+13) by omega,run_add,ht]
    simp [pa,run_power]

#print axioms source_power
#print axioms four_hits

end FourMarks
