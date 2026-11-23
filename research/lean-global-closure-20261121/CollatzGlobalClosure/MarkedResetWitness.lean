/-! A fully explicit ordinary trajectory between two marks that increases
both binary length and trailing-one depth.  Kernel reduction checks all
arithmetic; no native evaluator or additional axiom is used. -/

namespace CollatzMarkedResetWitness

def step (n : Nat) : Nat := if n%2=0 then n/2 else (3*n+1)/2
def orbit : Nat → Nat → Nat
  | 0,n => n
  | k+1,n => orbit k (step n)
def Marked (n : Nat) : Prop :=
  n%2=1 ∧ (n.log2+1)*(n-2^n.log2)≤70*2^n.log2

instance (n : Nat) : Decidable (Marked n) :=
  inferInstanceAs (Decidable (_ ∧ _))

def source : Nat := (2^525*3073-5)/3
def target : Nat := 2^512*3^11*3073-1

set_option maxRecDepth 100000 in
set_option maxHeartbeats 1000000 in
set_option exponentiation.threshold 2048 in
theorem exact_reset_pair :
    1<source ∧ Marked source ∧ Marked target ∧
    orbit 13 source=target ∧ source<target ∧
    source.log2=535 ∧ target.log2=541 ∧
    source%4=1 ∧ target+1=2^512*(3^11*3073) ∧
    (3^11*3073)%2=1 := by decide

end CollatzMarkedResetWitness

#print axioms CollatzMarkedResetWitness.exact_reset_pair
