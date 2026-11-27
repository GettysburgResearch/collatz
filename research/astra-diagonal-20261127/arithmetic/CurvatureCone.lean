import Mathlib.Data.Int.Basic

namespace Collatz.Diagonal.CurvatureCone

/-- High-interval return words. The last two words cross a mixed boundary. -/
inductive Column | single | double | ds | sd deriving DecidableEq, Repr
open Column

/-- Source residue, output residue, terminal carry and lifted middle carry. -/
structure Row where
  src : Int
  dst : Int
  carry : Int
  mid : Int
deriving DecidableEq, Repr

/-- Residue rows of the full one-column return maps, with modulus four at both ends. -/
def rows : Column → List Row
  | .single => [⟨1,1,1,0⟩, ⟨1,3,1,0⟩, ⟨2,1,2,0⟩, ⟨2,2,2,0⟩, ⟨2,3,2,0⟩]
  | .double => [⟨1,1,7,0⟩, ⟨1,2,7,0⟩, ⟨1,3,7,0⟩, ⟨2,1,10,0⟩, ⟨2,2,10,0⟩, ⟨2,2,14,0⟩, ⟨2,3,10,0⟩, ⟨3,1,5,0⟩, ⟨3,3,5,0⟩]
  | .ds => [⟨1,1,29,7⟩, ⟨1,1,37,7⟩, ⟨1,2,37,7⟩, ⟨1,3,29,7⟩, ⟨1,3,37,7⟩, ⟨2,1,38,10⟩, ⟨2,1,46,10⟩, ⟨2,1,58,14⟩, ⟨2,2,46,10⟩, ⟨2,2,58,14⟩, ⟨2,3,38,10⟩, ⟨2,3,46,10⟩, ⟨2,3,58,14⟩, ⟨3,1,23,5⟩, ⟨3,3,23,5⟩]
  | .sd => [⟨1,1,29,7⟩, ⟨1,1,37,7⟩, ⟨1,2,37,7⟩, ⟨1,3,29,7⟩, ⟨1,3,37,7⟩, ⟨2,1,38,10⟩, ⟨2,1,46,10⟩, ⟨2,1,58,14⟩, ⟨2,2,46,10⟩, ⟨2,2,58,14⟩, ⟨2,2,74,14⟩, ⟨2,3,38,10⟩, ⟨2,3,46,10⟩, ⟨2,3,58,14⟩]

/-- Use the ordinary odd-part valuation up to the first relevant cutoff. -/
private def lo (n : Nat) : Nat :=
  if n%2=1 then 1 else if n%4=2 then 2 else if n%8=4 then 4 else 0

private def edge (single : Bool) (n : Nat) : Option Nat := do
  let b := lo n
  if !(b==1 || b==2) then none else
  if single then
    let z := (3*n+b)/4
    if (3*n+b)%4==0 && (lo z==b || (2*lo z==b)) then some z else none
  else
    let m := (3*n+b)/2
    let c := lo m
    let z := (3*m+c)/4
    if (c==b || c==2*b) && (3*m+c)%4==0 && (lo z==1 || lo z==2) &&
        (2*lo z==c || lo z==c) then some z else none

private def den : Column → Nat | .single => 4 | .double => 8 | _ => 32
private def num : Column → Nat | .single => 3 | .double => 9 | _ => 27

private def calcRow (t : Column) (n : Nat) : Option Row := do
  let fst := t == .single || t == .sd
  let z ← edge fst n
  let y ← match t with
    | .ds => edge true z
    | .sd => edge false z
    | _ => some z
  let mid := if t == .ds then 8*z-9*n else if t == .sd then
    8*((3*z+lo z)/2)-9*n else 0
  return ⟨n%4,y%4,den t*y-num t*n,mid⟩

private def generated (t : Column) : List Row :=
  ((List.range (4*den t)).filterMap fun n => calcRow t (4*den t+n)).eraseDups

private def sameRows (t : Column) : Bool :=
  (generated t).all ((rows t).contains ·) && (rows t).all ((generated t).contains ·)

set_option maxRecDepth 20000 in
set_option maxHeartbeats 2000000 in
/-- Kernel decision on the complete source residue intervals for each return. -/
theorem physicalRowTables : (sameRows .single && sameRows .double &&
    sameRows .ds && sameRows .sd) = true := by decide

abbrev State := Int × Int × Int

/-- Finite positive-height predecessor classes in the backwards induction. -/
def danger : Nat → List State
  | 0 => [(1,1,1), (1,2,1), (2,2,1), (3,1,2), (3,2,2), (4,2,2)]
  | 1 => [(1,1,1), (1,1,3), (1,2,1), (1,2,2), (1,2,3), (1,3,2), (2,2,1), (2,3,2), (3,1,2), (3,2,2), (4,2,2)]
  | 2 => [(1,1,1), (1,1,3), (1,2,1), (1,2,2), (1,2,3), (1,3,2), (2,1,1), (2,2,1), (2,3,1), (2,3,2), (3,1,2), (3,2,2), (4,2,2)]
  | 3 => [(1,1,1), (1,1,3), (1,2,1), (1,2,3), (1,3,2), (2,2,1), (3,1,2), (3,2,2), (4,2,2)]
  | 4 => [(1,1,1), (1,2,1), (1,3,2), (2,2,1), (3,1,2), (3,2,2), (4,2,2)]
  | _ => []

private def unsafeRows (sign : Int) (t : Column) (h : Int) (bad : List State)
    (a b c : Row) : Bool :=
  let n : Int := num t
  let d : Int := den t
  let v := n*h+a.carry-2*b.carry+c.carry
  let out := sign*(v/d)
  let compatible := (v-d*(a.dst-2*b.dst+c.dst))%(4*d)==0
  let middleBad := (t==.sd || t==.ds) && sign*(9*h+a.mid-2*b.mid+c.mid)≤0
  compatible && (middleBad || out≤0 || bad.contains (out,a.dst,b.dst))

private def unsafeStart (sign : Int) (t u v : Column) (bad : List State)
    (h x y : Int) : Bool :=
  let z := (h-x+2*y)%4
  ((rows t).filter fun a => a.src==x).any fun a =>
    ((rows u).filter fun b => b.src==y).any fun b =>
      ((rows v).filter fun c => c.src==z).any fun c => unsafeRows sign t h bad a b c

private def checkSigned (sign : Int) (t u v : Column) (source dest : List State) : Bool :=
  (List.range 10).all fun i =>
    ([1,2,3] : List Int).all fun x =>
      ([1,2,3] : List Int).all fun y =>
        let h : Int := i+1
        unsafeStart sign t u v dest (sign*h) x y == source.contains (h,x,y)

/-- Check the full reduced range of positive heights. The unbounded exclusion beyond
ten is the scalar reverseCutoff theorem in the companion module. -/
def verifies (t u v : Column) (source dest : Nat) : Bool :=
  checkSigned 1 t u v (danger source) (danger dest)

set_option maxRecDepth 20000
set_option maxHeartbeats 4000000

/-- All ordinary single/double backwards steps for both return lengths. -/
theorem ordinaryCone :
    (verifies .double .double .double 1 0 &&
     verifies .double .double .double 2 1 &&
     verifies .single .single .single 0 2 &&
     verifies .double .double .double 2 2) = true := by decide

/-- The two split orientations, including lifted midpoint and their preceding double. -/
theorem splitCone :
    (verifies .ds .ds .sd 3 2 && verifies .double .double .double 1 3 &&
     verifies .ds .sd .sd 4 2 && verifies .double .double .double 1 4) = true := by decide

/-- Signed-height predecessor classes for the negative midpoint cone. -/
def negativeDanger : Nat → List State
  | 0 => [(2,1,2), (4,2,2)]
  | 1 => [(2,1,2)]
  | 2 => [(2,2,3)]
  | 3 => [(3,1,3), (3,2,3)]
  | 4 => [(2,1,2), (3,1,1), (3,2,1)]
  | 5 => []
  | _ => []

private def neg (t u v : Column) (a b : Nat) : Bool :=
  checkSigned (-1) t u v (negativeDanger a) (negativeDanger b)

/-- All backwards edges required by the two negative ordinary and two split blocks. -/
theorem negativeCone :
    (neg .single .single .single 0 4 &&
     neg .single .single .single 1 0 &&
     neg .single .single .single 5 5 &&
     neg .double .double .double 0 0 &&
     neg .double .double .double 3 2 &&
     neg .double .double .double 4 3 &&
     neg .double .double .double 5 1 &&
     neg .double .double .double 5 5 &&
     neg .ds .ds .sd 2 0 &&
     neg .ds .sd .sd 1 0) = true := by decide

/-- Backward image through actual residue rows, with no cutoff on input height.
The target curvature fixes the input height whenever the numerator is a multiple of n. -/
private def preimages (t u v : Column) (target : State)
    (accept : State → Bool → Bool) : Bool :=
  let (h,x,y) := target
  let z := (2*y-x+h)%4
  let n : Int := num t
  let d : Int := den t
  ((rows t).filter (·.dst == x)).all fun a =>
    ((rows u).filter (·.dst == y)).all fun b =>
      ((rows v).filter (·.dst == z)).all fun c =>
        let w := d*h-a.carry+2*b.carry-c.carry
        let ih := w/n
        let real := w%n==0 && (ih-a.src+2*b.src-c.src)%4==0
        !real || accept (ih,a.src,b.src) (a.carry==b.carry && b.carry==c.carry)

private def diagonal : List State := [(0,1,1),(0,2,2),(0,3,3)]

private def sameCarryEntry (t u v : Column) : Bool := diagonal.all fun s =>
  preimages t u v s fun a e => diagonal.contains a && e

/-- At any unit or composite step, equal-residue zero targets have only
equal-residue zero predecessors, with identical three carries. -/
theorem diagonalEntry :
    (sameCarryEntry .single .single .single && sameCarryEntry .double .double .double &&
     sameCarryEntry .ds .ds .sd && sameCarryEntry .ds .sd .sd) = true := by decide

/-- Sets used to eliminate the central states outside the synchronized zero pair. -/
private def basin : Nat → List State
  | 0 => [(-4,2,2), (-2,1,2), (0,1,2), (0,1,3), (0,3,1), (0,3,2), (0,3,3), (1,1,1), (1,2,1), (2,2,1), (3,1,2), (3,2,2), (4,2,2)]
  | 1 => [(-4,2,2), (-2,1,2), (0,1,1), (0,1,2), (0,2,2), (0,3,2), (0,3,3), (1,1,1), (1,1,3), (1,2,1), (1,2,2), (1,2,3), (1,3,2), (2,2,1), (2,3,2), (3,1,2), (3,2,2), (4,2,2)]
  | 2 => [(-4,2,2), (-2,1,2), (0,1,1), (0,1,2), (0,2,2), (0,3,2), (0,3,3), (1,1,1), (1,1,3), (1,2,1), (1,2,2), (1,2,3), (1,3,2), (2,1,1), (2,2,1), (2,3,1), (2,3,2), (3,1,2), (3,2,2), (4,2,2)]
  | 3 => [(-2,1,2), (0,1,1), (0,2,2), (1,1,1), (1,2,1), (2,2,1), (3,1,2), (3,2,2), (4,2,2)]
  | 4 => [(-2,1,2), (1,1,1), (1,2,1), (2,2,1), (3,1,2), (3,2,2), (4,2,2)]
  | 5 => [(0,1,2), (0,3,2), (1,1,1), (1,1,3), (1,2,1), (1,2,2), (1,2,3), (1,3,2), (2,2,1), (3,1,2), (3,2,2), (4,2,2)]
  | 6 => [(0,1,1), (0,2,2), (1,1,1), (1,1,3), (1,2,1), (1,2,2), (1,2,3), (1,3,2), (2,2,1), (2,3,2), (3,1,2), (3,2,2), (4,2,2)]
  | 7 => [(0,1,1), (0,2,2), (1,1,1), (1,2,1), (2,2,1), (3,1,2), (3,2,2), (4,2,2)]
  | 8 => [(1,1,1), (1,2,1), (2,2,1), (3,1,2), (3,2,2), (4,2,2)]
  | 9 => [(0,1,1), (0,2,2), (0,3,3), (1,1,1), (1,1,3), (1,2,1), (1,2,2), (1,2,3), (1,3,2), (2,1,1), (2,2,1), (2,3,1), (3,1,2), (3,2,2), (4,2,2)]
  | 10 => [(1,1,1), (1,1,3), (1,2,1), (1,2,2), (1,2,3), (1,3,2), (2,2,1), (3,1,2), (3,2,2), (4,2,2)]
  | 11 => [(1,1,1), (1,2,1), (2,2,1), (4,2,2)]
  | 12 => [(1,1,1), (1,1,3), (1,2,1), (1,2,2), (1,2,3), (1,3,2), (2,2,1), (4,2,2)]
  | 13 => [(1,1,1), (1,2,1), (2,2,1)]
  | 14 => [(1,1,1), (1,1,3), (1,2,1), (1,2,2), (1,2,3), (1,3,2)]
  | 15 => [(1,2,2), (1,3,2)]
  | 16 => []
  | _ => []

private def covers (t : Column) (src dst : Nat) : Bool :=
  (basin dst).all fun s => preimages t t t s fun q _ => (basin src).contains q

private def coverOrdinary (path : List Nat) (next : Nat) : Bool := match path with
  | [a,b,c,d] => covers .double b a && covers .double c b && covers .single d c &&
      (basin d).all fun s => !(basin 0).contains s || (basin next).contains s
  | [a,b,c,d,e] => covers .double b a && covers .double c b && covers .double d c &&
      covers .single e d &&
      (basin e).all fun s => !(basin 0).contains s || (basin next).contains s
  | _ => false

/-- Both ordinary lengths reduce stage 1 of the outside-state induction. -/
theorem outsideStage1 :
    (coverOrdinary [0,1,2,3] 4 &&
     coverOrdinary [0,1,2,2,3] 4) = true := by decide

/-- Both ordinary lengths reduce stage 2 of the outside-state induction. -/
theorem outsideStage2 :
    (coverOrdinary [4,5,6,7] 8 &&
     coverOrdinary [4,5,6,9,7] 8) = true := by decide

/-- Both ordinary lengths reduce stage 3 of the outside-state induction. -/
theorem outsideStage3 :
    (coverOrdinary [8,10,10,11] 11 &&
     coverOrdinary [8,10,10,10,11] 11) = true := by decide

/-- Both ordinary lengths reduce stage 4 of the outside-state induction. -/
theorem outsideStage4 :
    (coverOrdinary [11,12,12,13] 13 &&
     coverOrdinary [11,12,12,12,13] 13) = true := by decide

/-- Both ordinary lengths reduce stage 5 of the outside-state induction. -/
theorem outsideStage5 :
    (coverOrdinary [13,14,15,16] 16 &&
     coverOrdinary [13,14,15,15,16] 16) = true := by decide

end Collatz.Diagonal.CurvatureCone
