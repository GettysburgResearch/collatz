import Std.Tactic

/-! Native shortcut pairs and the signed adjacent endpoint flux. -/

namespace AstraFullProof.EndpointFlux

def step (x : Nat) : Nat :=
  if x % 2 = 0 then x / 2 else (3 * x + 1) / 2

def oddCount : Nat → Nat → Nat
  | 0, _ => 0
  | t + 1, x => x % 2 + oddCount t (step x)

/-- The mass of the residue immediately below zero, less the zero-residue mass. -/
def charge (x : Nat) : Int :=
  (if x % 4 = 3 then 1 else 0) - (if x % 4 = 0 then 1 else 0)

theorem two_steps (x : Nat) :
    ((x % 2 + step x % 2 : Nat) : Int) - 1 = charge x := by
  unfold step charge
  split <;> split <;> split <;> omega

def flux : Nat → Nat → Int
  | 0, _ => 0
  | pairs + 1, x => charge x + flux pairs (step (step x))

theorem paired_count (pairs x : Nat) :
    (oddCount (2 * pairs) x : Int) - pairs = flux pairs x := by
  induction pairs generalizing x with
  | zero => rfl
  | succ p ih =>
    rw [show 2 * (p + 1) = (2 * p + 1) + 1 by omega]
    simp only [oddCount, flux]
    have localPair := two_steps x
    have tail := ih (step (step x))
    omega

theorem standard_pair (pairs : Nat) :
    flux pairs 1 = 0 ∧ flux pairs 2 = 0 := by
  induction pairs with
  | zero => decide
  | succ p ih =>
    change 0 + flux p 1 = 0 ∧ 0 + flux p 2 = 0
    omega

#print axioms two_steps
#print axioms paired_count
#print axioms standard_pair

end AstraFullProof.EndpointFlux
