import Mathlib.Data.Fintype.Prod
import Mathlib.Tactic.NormNum

/-! Finite four-copy transfer and forced-return certificate for the real-width 99/50
binary valuation language. The real-slope interpolation and analytic transfer are written
arguments in FOUR_BRIDGE_BINARY_CYCLE_BOUND.md. No code generation is used in proofs. -/
namespace BinaryBridgeEnergy

set_option maxRecDepth 100000
set_option maxHeartbeats 10000000

abbrev Quad := Fin 2 × Fin 2 × Fin 2 × Fin 2

def vertices : List Quad :=
  [(0,0,0,0), (1,0,1,0), (1,0,0,1), (0,1,1,0), (0,1,0,1), (1,1,1,1)]

def pairEqual (q : Quad) : Prop :=
  (q.1 : Nat) + q.2.1.val = q.2.2.1.val + q.2.2.2.val

instance (q : Quad) : Decidable (pairEqual q) := inferInstanceAs (Decidable (_ = _))

theorem complete_six_states : ∀ q : Quad, q ∈ vertices ↔ pairEqual q := by decide

def coordLe (a b : Quad) : Bool :=
  decide (a.1 ≤ b.1 ∧ a.2.1 ≤ b.2.1 ∧ a.2.2.1 ≤ b.2.2.1 ∧ a.2.2.2 ≤ b.2.2.2)

def successors (up : Bool) (q : Quad) : List Quad :=
  vertices.filter (fun t => if up then coordLe q t else coordLe t q)

structure Counts where
  low : Nat
  middle : Nat
  high : Nat
  deriving DecidableEq, Repr

def unit (q : Quad) : Counts :=
  match q.1.val + q.2.1.val with
  | 0 => ⟨1,0,0⟩
  | 1 => ⟨0,1,0⟩
  | _ => ⟨0,0,1⟩

def plus (a b : Counts) : Counts :=
  ⟨a.low+b.low, a.middle+b.middle, a.high+b.high⟩

def histogram : List Quad → Counts
  | [] => ⟨0,0,0⟩
  | q :: qs => plus (unit q) (histogram qs)

def advance (up : Bool) (x : Counts) : Counts :=
  if up then ⟨x.low, 4*x.low+x.middle, x.low+x.middle+x.high⟩
  else ⟨x.low+x.middle+x.high, x.middle+4*x.high, x.high⟩

theorem basis_recursion : ∀ up : Bool, ∀ q : Quad, q ∈ vertices →
    histogram (successors up q) = advance up (unit q) := by decide

private theorem hist_append (a b : List Quad) :
    histogram (a ++ b) = plus (histogram a) (histogram b) := by
  induction a with
  | nil => simp [histogram, plus]
  | cons x a h => simp [histogram, plus, h, Nat.add_assoc]

private theorem linear (up : Bool) (a b : Counts) :
    advance up (plus a b) = plus (advance up a) (advance up b) := by
  cases up <;> simp [advance, plus] <;> omega

theorem full_recursion (up : Bool) (xs : List Quad) (h : ∀ q ∈ xs, q ∈ vertices) :
    histogram (xs.flatMap (successors up)) = advance up (histogram xs) := by
  induction xs with
  | nil => cases up <;> rfl
  | cons q qs ih =>
    rw [List.flatMap_cons, hist_append, basis_recursion up q (h q (by simp)),
      ih (fun q' hq' => h q' (by simp [hq'])), histogram, linear]

/- The middle slope is 46797/80000. A doubled denominator represents all its open
cell midpoints and endpoints by integers. -/
def den : Nat := 160000
def slope : Nat := 93594
def cap : Nat := 156800

def insertCut (x : Nat) : List Nat → List Nat
  | [] => [x]
  | y :: ys => if x == y then y :: ys else if x < y then x :: y :: ys else y :: insertCut x ys

def sortCuts : List Nat → List Nat
  | [] => []
  | x :: xs => insertCut x (sortCuts xs)

def cuts : List Nat :=
  sortCuts ([0,den] ++ (List.range 54).flatMap (fun i =>
    [((den - (i*slope)%den)%den), ((cap+den-(i*slope)%den)%den)]))

def faces : List Nat :=
  cuts.dropLast ++ (cuts.zip cuts.tail).map (fun ab => (ab.1+ab.2)/2)

theorem face_count : faces.length = 216 := by decide +kernel

def known (n e : Nat) : Bool :=
  (n == 12 && e == 388224) ||
  (n == 41 && e == 30840400948687284336) ||
  (n == 53 && e == 17778623164916750424132973)

def firstVisit (initiallyForced : Bool) : Nat → Nat → Nat → Counts → Bool
  | 0, _, _, _ => false
  | fuel+1, j, f, counts =>
    let raw := f+slope
    let up := decide (den ≤ raw)
    let f' := if up then raw-den else raw
    let counts' := advance up counts
    if cap < f' then
      if initiallyForced then known (j+1) counts'.low else decide (j+1 ≤ 52)
    else firstVisit initiallyForced fuel (j+1) f' counts'

def checkFace (f : Nat) : Bool := firstVisit (decide (cap < f)) 53 0 f ⟨1,0,0⟩

theorem all_faces : faces.all checkFace = true := by decide +kernel

theorem energy12 : (388224 : Nat)^1000 < 3^(999*12) := by decide +kernel
theorem energy41 : (30840400948687284336 : Nat)^1000 < 3^(999*41) := by decide +kernel
theorem energy53 : (17778623164916750424132973 : Nat)^1000 < 3^(999*53) := by decide +kernel

/- Each tag records the kind, date, and the integer part of the unwrapped cut shifted
by 54. The endpoints of the real-slope comparison have common denominator 10^6. -/
abbrev TaggedCut := Nat × (Nat × Nat × Nat)

def insertTagged (x : TaggedCut) : List TaggedCut → List TaggedCut
  | [] => [x]
  | y :: ys => if x.1 < y.1 then x :: y :: ys else y :: insertTagged x ys

def sortTagged : List TaggedCut → List TaggedCut
  | [] => []
  | x :: xs => insertTagged x (sortTagged xs)

def tagged (a : Nat) : List TaggedCut :=
  let d := 1000000
  let mk (k i shift : Nat) : TaggedCut :=
    let raw := 54*d + shift - i*a
    (raw % d, (k,i,raw/d))
  sortTagged ([(0,(2,0,0)), (d,(2,1,0))] ++
    (List.range 54).flatMap (fun i =>
      (if i == 0 then [] else [mk 0 i 0]) ++ [mk 1 i 980000]))

theorem endpoint_tags :
    (tagged 584961).map Prod.snd = (tagged 584964).map Prod.snd := by decide +kernel

theorem endpoint_strict :
    ((tagged 584961).map Prod.fst).Pairwise (· < ·) ∧
    ((tagged 584964).map Prod.fst).Pairwise (· < ·) := by decide +kernel

theorem bracket_lower : 2^1584961 < (3 : Nat)^1000000 := by decide +kernel
theorem bracket_upper : (3 : Nat)^1000000 < 2^1584964 := by decide +kernel

end BinaryBridgeEnergy

-- Integration adds an axiom report for every public and private theorem.
#print axioms BinaryBridgeEnergy.complete_six_states
#print axioms BinaryBridgeEnergy.basis_recursion
#print axioms BinaryBridgeEnergy.hist_append
#print axioms BinaryBridgeEnergy.linear
#print axioms BinaryBridgeEnergy.full_recursion
#print axioms BinaryBridgeEnergy.face_count
#print axioms BinaryBridgeEnergy.all_faces
#print axioms BinaryBridgeEnergy.energy12
#print axioms BinaryBridgeEnergy.energy41
#print axioms BinaryBridgeEnergy.energy53
#print axioms BinaryBridgeEnergy.endpoint_tags
#print axioms BinaryBridgeEnergy.endpoint_strict
#print axioms BinaryBridgeEnergy.bracket_lower
#print axioms BinaryBridgeEnergy.bracket_upper
