import Std

namespace CollatzDecorationControl

def valuations : List Nat :=
  [1,2,1,1,2,2,1,2,2,1,2,2,1,2,1,2,1,2,1,2,2,1,2,1,2,1,2,2,1,2,2,1,2,1,2,1,2,1,2,2,2]

def signature (w : List Nat) : Nat × Nat :=
  w.foldl (fun (x : Nat × Nat) a => (3 * x.1 + 2 ^ x.2, x.2 + a)) (0, 0)

def denominator : Nat := 2 ^ valuations.sum - 3 ^ valuations.length
def numerator : Nat := (signature valuations).1
def reducedDen : Nat := denominator / Nat.gcd numerator denominator
def rootNumer : Nat := numerator / Nat.gcd numerator denominator

def trajectory (d x : Nat) : List Nat → List Nat
  | [] => [x]
  | a :: as => x :: trajectory d ((3*x+d) / 2^a) as

def exactEdges (d x : Nat) : List Nat → Bool
  | [] => true
  | a :: as => (3*x+d) % (2 ^ a) == 0 &&
    ((3*x+d)/(2 ^ a)) % 2 == 1 && exactEdges d ((3*x+d)/(2 ^ a)) as

set_option maxRecDepth 100000
set_option maxHeartbeats 600000

theorem arithmeticControl :
    valuations.length = 41 ∧ valuations.sum = 65 ∧
    denominator = 420491770248316829 ∧ numerator = 326313631156465704911 ∧
    Nat.gcd numerator denominator = 19 ∧
    reducedDen = 22131145802542991 ∧ rootNumer = 17174401639813984469 ∧
    rootNumer % 18 = reducedDen % 18 := by decide

theorem ordinaryDivisibilityFails : ¬ denominator ∣ numerator := by decide

theorem exactRationalCycle :
    exactEdges reducedDen rootNumer valuations = true ∧
    (trajectory reducedDen rootNumer valuations).getLast? = some rootNumer ∧
    (trajectory reducedDen rootNumer valuations).all
      (fun x => decide (rootNumer ≤ x ∧ 3*x < 8*rootNumer)) = true := by decide

def rankCycle : List Nat :=
  ((trajectory reducedDen rootNumer valuations).take valuations.length).map fun x =>
    if x < 2 * rootNumer then 4 * x else if x < 4 * rootNumer then 2 * x else x

def rank (x : Nat) := (rankCycle.filter (fun y => decide (y < x))).length

def isRotation : Bool :=
  (List.range valuations.length).all fun i =>
    let u := rankCycle.getD i 0
    let v := rankCycle.getD ((i+1) % valuations.length) 0
    (rank u + valuations.sum) % valuations.length == rank v

theorem rankControl : isRotation = true := by decide

#print axioms rankControl
#print axioms arithmeticControl
#print axioms ordinaryDivisibilityFails
#print axioms exactRationalCycle
end CollatzDecorationControl
