import MovingOrigin

namespace Collatz.IteratedReturn
open Collatz.SourceDeletion Collatz.MinimumFailure Collatz.MovingOrigin

def source (a : Nat) := 89585+48*2^19*a
private def target (a : Nat) := 1121+48*3^8*a

private def left (a : Nat) := 204954140672*a+729593939
private def right (a : Nat) := 2564819559*a+9130222

def startIndex : Nat → Nat → Nat
  | 0, a => a
  | n+1, a => left (startIndex n a)

private theorem shift (n a : Nat) : right (startIndex n a)=startIndex n (right a) := by
  induction n with
  | zero => rfl
  | succ n ih =>
    change right (left (startIndex n a))=left (startIndex n (right a))
    rw [←ih]; dsimp [left,right]; ring

private theorem next_row (n a : Nat) :
    target (startIndex (n+1) a)=source (startIndex n (right a)) := by
  rw [←shift]
  change target (left (startIndex n a))=source (right (startIndex n a))
  dsimp [target,source,left,right]; ring

/-- For every prescribed number of real first-crossing replacements there
are unbounded positive ordinary sources for which all of them concatenate.
Each one preserves the canonical reverse orientation and saves eight odds
and nineteen clocks on the same supplied upper hit. -/
theorem prescribed_depth (n a : Nat) :
    let z := source (startIndex n a)
    a<z ∧ z%48=17 ∧ ∃ w, w%48=17 ∧ w≤z ∧ (0<n → w<z) ∧
      (Good z ↔ Good w) ∧
      ∀ H, run H (3*z)=1 → ∃ J, H=19*n+J ∧ run J (3*w)=1 ∧
        odds H (3*z)=8*n+odds J (3*w) := by
  induction n generalizing a with
  | zero =>
    dsimp only [startIndex]
    refine ⟨by unfold source; omega,by unfold source; omega,source a,
      by unfold source; omega,le_rfl,by omega,Iff.rfl,?_⟩
    intro H hit
    exact ⟨H,by omega,hit,by omega⟩
  | succ n ih =>
    obtain ⟨_,_,_,lt,_,_,_,_,equiv,consume⟩ := canonical_to_canonical (startIndex (n+1) a)
    change target (startIndex (n+1) a)<source (startIndex (n+1) a) at lt
    change Good (source (startIndex (n+1) a)) ↔ Good (target (startIndex (n+1) a)) at equiv
    change ∀ H, run H (3*source (startIndex (n+1) a))=1 → ∃ K, H=20+K ∧
      run (1+K) (3*target (startIndex (n+1) a))=1 ∧
      odds H (3*source (startIndex (n+1) a))=8+odds (1+K) (3*target (startIndex (n+1) a))
      at consume
    rw [next_row] at lt equiv consume
    obtain ⟨big,_,w,rem,le,_,labels,transfer⟩ := ih (right a)
    have aa : a<right a := by dsimp [right]; omega
    refine ⟨by omega,by dsimp [source]; omega,w,rem,by omega,fun _ => by omega,
      equiv.trans labels,?_⟩
    intro H hit
    obtain ⟨K,hk,terminal,counts⟩ := consume H hit
    obtain ⟨J,hj,targetHit,remaining⟩ := transfer (1+K) terminal
    exact ⟨J,by omega,targetHit,by omega⟩

/-- Each edge is the literal smaller-source pair certified in MovingOrigin. -/
def Rewrite : Nat → Nat → Nat → Prop
  | 0, x, y => x=y
  | n+1, x, y => ∃ a, x=source a ∧ Rewrite n (target a) y

private theorem edge_chain (n a : Nat) :
    ∃ y, y%48=17 ∧ Rewrite n (source (startIndex n a)) y := by
  induction n generalizing a with
  | zero => exact ⟨source a,by dsimp [source]; omega,rfl⟩
  | succ n ih =>
    obtain ⟨y,r,path⟩ := ih (right a)
    exact ⟨y,r,startIndex (n+1) a,rfl,(next_row n a).symm ▸ path⟩

/-- The high lift for an arbitrary chain pays binary precision on entry
and only ternary precision on exit. Both exponents are sharp affine slopes. -/
theorem translated_chain {n x y : Nat} (path : Rewrite n x y) (t : Nat) :
    Rewrite n (x+48*(2^19)^n*t) (y+48*(3^8)^n*t) := by
  induction n generalizing x t with
  | zero => change x=y at path; subst x; rfl
  | succ n ih =>
    obtain ⟨a,eq,tail⟩ := path
    subst x
    refine ⟨a+(2^19)^n*t,by unfold source; ring,?_⟩
    have moved := ih tail (3^8*t)
    convert moved using 1
    · dsimp only [target]; ring
    · ring

/-- Every depth has a terminal progression with no auxiliary coprime factor
in its modulus. This allows one three-adic discrete logarithm for entry. -/
theorem terminal_progression (n : Nat) :
    ∃ z w, w%48=17 ∧ ∀ t, Rewrite n
      (z+48*(2^19)^n*t) (w+48*(3^8)^n*t) := by
  obtain ⟨w,r,path⟩ := edge_chain n 0
  exact ⟨source (startIndex n 0),w,r,translated_chain path⟩

/-- The fixed rational center of the affine rewrite is -40337/517727.
Its positive numerator gives the terminal ternary congruence at every depth. -/
theorem centered_identity {n z w : Nat} (path : Rewrite n z w) :
    (2^19)^n*(517727*w+40337)=(3^8)^n*(517727*z+40337) := by
  induction n generalizing z with
  | zero => change z=w at path; subst z; simp
  | succ n ih =>
    obtain ⟨a,za,tail⟩ := path
    subst z
    have row : 2^19*(517727*target a+40337)=3^8*(517727*source a+40337) := by
      dsimp [target,source]; ring
    calc
      _=2^19*((2^19)^n*(517727*w+40337)) := by ring
      _=(3^8)^n*(2^19*(517727*target a+40337)) := by rw [ih tail]; ring
      _=_ := by rw [row]; ring

#print axioms centered_identity
#print axioms translated_chain
#print axioms terminal_progression
#print axioms prescribed_depth
end Collatz.IteratedReturn
