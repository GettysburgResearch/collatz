import Mathlib.Data.Nat.ModEq
import Mathlib.Data.Nat.GCD.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-! Sum of the ternary cylinder sizes at the first normalized inverse
slope crossing. The alphabet is the two ordinary inverse shortcuts. A
nonintegral odd inverse rejects the ordinary target. -/
namespace InverseBudget

/-- Interpret false as doubling and true as the inverse odd shortcut. -/
def run : List Bool → Nat → Option Nat
  | [],y => some y
  | false::w,y => run w (2*y)
  | true::w,y => if y%3=2 then run w ((2*y-1)/3) else none

def grade : List Bool → Nat
  | [] => 0
  | false::w => grade w
  | true::w => grade w+1

def offset : List Bool → Nat
  | [] => 0
  | false::w => offset w
  | true::w => 2^w.length+3*offset w

/-- The exact ordinary affine equation for an arbitrary legal inverse
shortcut word. -/
theorem equation (w : List Bool) (y x : Nat) (legal : run w y=some x) :
    2^w.length*y=3^(grade w)*x+offset w := by
  induction w generalizing y with
  | nil => simpa [run,grade,offset] using legal
  | cons bit w ih =>
    cases bit with
    | false =>
      have re:=ih (2*y) legal
      change 2^(w.length+1)*y=3^(grade w)*x+offset w
      rw [←re,pow_succ]; ring
    | true =>
      unfold run at legal
      split at legal
      next bit =>
        have mid : 3*((2*y-1)/3)+1=2*y := by omega
        have re:=ih ((2*y-1)/3) legal
        change 2^(w.length+1)*y=3^(grade w+1)*x+(2^w.length+3*offset w)
        rw [pow_succ,pow_succ]; nlinarith only [re,congrArg (fun n : Nat => 2^w.length*n) mid]
      next => contradiction

/-- All ordinary targets accepting the same word lie in one ternary
residue. There is no restriction on clocks or consecutive doublings. -/
theorem one_class (w : List Bool) (y z x t : Nat) (hy : run w y=some x) (hz : run w z=some t) :
    y ≡ z [MOD 3^(grade w)] := by
  have eq : 2^w.length*y ≡ 2^w.length*z [MOD 3^(grade w)] := by
    rw [equation w y x hy,equation w z t hz]; simp [Nat.ModEq]
  exact Nat.ModEq.cancel_left_of_coprime (((show Nat.Coprime 3 2 by decide).pow_left _).pow_right _) eq

/-- Overcount the first-crossing cylinders as classes modulo 3^D.
Earlier crossings prune both continuation branches. -/
def charge (F D : Nat) : Nat → Nat → Nat → Nat
  | 0,v,d => if F*2^v≤3^d then 3^(D-d) else 0
  | n+1,v,d => if F*2^v≤3^d then 3^(D-d) else
      charge F D n (v+1) d+charge F D n (v+1) (d+1)

private theorem leaf (F D v d : Nat) (hd : d≤D) (stop : F*2^v≤3^d) :
    4^v*F^2*3^(D-d)≤3^(D+d) := by
  have sq:=Nat.pow_le_pow_left stop 2
  have b : (4:Nat)^v=(2^v)^2 := by rw [←pow_mul,show v*2=2*v by ring,pow_mul]; rfl
  calc
    4^v*F^2*3^(D-d) = (F*2^v)^2*3^(D-d) := by rw [b]; ring
    _ ≤ (3^d)^2*3^(D-d) := Nat.mul_le_mul_right _ sq
    _ = _ := by rw [←pow_mul,←pow_add]; congr 1; omega

/-- The two prospective branch weights are 1/4 and 3/4. Equivalently,
4^v F² times the total charged number of residues is at most 3^(D+d).
All quantities are ordinary natural numbers. -/
theorem quadratic (F D n v d : Nat) (room : d+n≤D) :
    4^v*F^2*charge F D n v d≤3^(D+d) := by
  induction n generalizing v d with
  | zero =>
    simp only [charge]; split
    next h => exact leaf F D v d (by omega) h
    next => simp
  | succ n ih =>
    simp only [charge]; split
    next h => exact leaf F D v d (by omega) h
    next =>
      have l:=ih (v+1) d (by omega)
      have r:=ih (v+1) (d+1) (by omega)
      rw [pow_succ] at l r
      rw [show D+(d+1)=D+d+1 by omega,pow_succ (3:Nat) (D+d)] at r
      nlinarith only [l,r]

theorem root_bound (F h : Nat) : F^2*charge F h h 0 0≤3^h := by
  simpa using quadratic F h h 0 0 (by omega)

#print axioms equation
#print axioms one_class
#print axioms root_bound
end InverseBudget
