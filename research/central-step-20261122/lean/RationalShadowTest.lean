import Mathlib.Tactic.NormNum
import Mathlib.Tactic.IntervalCases
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

/-!
An exact obstruction to a proposed universal rational-shadow bridge.

The common odd denominator is 2187. The source shadow is -6005/2187;
the target shadow is eight times it plus nineteen, namely -6487/2187.
The source has a complete rational word [2,2,2,2,2,2,1] to 1 and then
gap 2 forever. Every nonempty odd-prefix coefficient contracts. The
target stays negative, enters the -7,-10,-5 cycle, and every nonempty
ordinary-prefix coefficient expands.

These are rational shadows, not positive integer counterexamples. No
complete positive integer source lift or universal Collatz claim occurs
in this module.
-/

namespace CollatzCentral.RationalShadowTest

def numeratorStep (d h : Int) : Int :=
  if h % 2 = 0 then h / 2 else (3*h+d)/2

def numeratorOrbit (d : Int) : Nat → Int → Int
  | 0, h => h
  | k+1, h => numeratorStep d (numeratorOrbit d k h)

def numeratorOdds (d : Int) : Nat → Int → Nat
  | 0, _ => 0
  | k+1, h => numeratorOdds d k h +
      if numeratorOrbit d k h % 2 = 0 then 0 else 1

private theorem orbit_add (d h : Int) (a b : Nat) :
    numeratorOrbit d (a+b) h =
      numeratorOrbit d b (numeratorOrbit d a h) := by
  induction b with
  | zero => simp [numeratorOrbit]
  | succ b ih =>
    change numeratorStep d (numeratorOrbit d (a+b) h) =
      numeratorStep d (numeratorOrbit d b (numeratorOrbit d a h))
    exact congrArg (numeratorStep d) ih

private theorem odds_add (d h : Int) (a b : Nat) :
    numeratorOdds d (a+b) h =
      numeratorOdds d a h + numeratorOdds d b (numeratorOrbit d a h) := by
  induction b with
  | zero => simp [numeratorOdds]
  | succ b ih =>
    change numeratorOdds d (a+b) h +
        (if numeratorOrbit d (a+b) h % 2 = 0 then 0 else 1) =
      numeratorOdds d a h + (numeratorOdds d b (numeratorOrbit d a h) +
        (if numeratorOrbit d b (numeratorOrbit d a h) % 2 = 0 then 0 else 1))
    rw [ih, orbit_add]
    omega

def sourceEdges : List (Int × Nat × Int) :=
  [(-6005,2,-3957), (-3957,2,-2421), (-2421,2,-1269),
   (-1269,2,-405), (-405,2,243), (243,2,729), (729,1,2187)]

def gapEdge (edge : Int × Nat × Int) : Prop :=
  0 < edge.2.1 ∧ edge.2.1 ≤ 4 ∧
  edge.1 % 2 = 1 ∧ edge.2.2 % 2 = 1 ∧
  3*edge.1+2187 = (2:Int)^edge.2.1*edge.2.2 ∧
  numeratorOrbit 2187 edge.2.1 edge.1 = edge.2.2 ∧
  numeratorOdds 2187 edge.2.1 edge.1 = 1

/-- Each listed gap is the exact accelerated rational gap, with no omitted
parity condition; the terminal rational state 1 subsequently has gap 2. -/
theorem source_certificate :
    (∀ edge ∈ sourceEdges, gapEdge edge) ∧
    gapEdge (2187,2,2187) ∧
    numeratorOrbit 2187 13 (-6005) = 2187 ∧
    numeratorOdds 2187 13 (-6005) = 7 := by
  constructor
  · intro edge member
    simp [sourceEdges] at member
    rcases member with rfl | rfl | rfl | rfl | rfl | rfl | rfl <;>
      unfold gapEdge <;> decide
  · unfold gapEdge
    decide

/-- The seven finite prefixes and every subsequent prefix through the
terminal gap-2 cycle have strictly contracting coefficients 3^r/2^A. -/
theorem source_all_prefix_contract :
    (∀ j : Nat, 1 ≤ j → j ≤ 6 → 3^j < 2^(2*j)) ∧
    (∀ k : Nat, 3^(7+k) < 2^(13+2*k)) := by
  constructor
  · intro j lower upper
    interval_cases j <;> norm_num
  · intro k
    have compare : 3^k ≤ 4^k := Nat.pow_le_pow_left (by decide : 3 ≤ 4) k
    have positive : 0 < 4^k := Nat.pow_pos (by decide : 0 < 4)
    simp only [pow_add, pow_mul]
    norm_num
    nlinarith

private theorem target_entry :
    numeratorOrbit 2187 9 (-6487) = -15309 ∧
    numeratorOdds 2187 9 (-6487) = 7 := by decide

private theorem target_cycle :
    numeratorOrbit 2187 3 (-15309) = -15309 ∧
    numeratorOdds 2187 3 (-15309) = 2 := by decide

private theorem cycle_repeat (k : Nat) :
    numeratorOrbit 2187 (3*k) (-15309) = -15309 ∧
    numeratorOdds 2187 (3*k) (-15309) = 2*k := by
  induction k with
  | zero => simp [numeratorOrbit, numeratorOdds]
  | succ k ih =>
    rw [show 3*(k+1)=3*k+3 by omega, orbit_add, odds_add, ih.1, ih.2]
    rw [target_cycle.1, target_cycle.2]
    constructor <;> omega

private theorem cycle_remainder (r : Nat) (small : r < 3) :
    numeratorOdds 2187 r (-15309) = (if r=0 then 0 else 1) := by
  interval_cases r <;> decide

private theorem target_tail_count (k r : Nat) (small : r < 3) :
    numeratorOdds 2187 (9+3*k+r) (-6487) =
      7+2*k+(if r=0 then 0 else 1) := by
  rw [odds_add, odds_add, target_entry.1, target_entry.2,
      orbit_add, target_entry.1, (cycle_repeat k).1,
      (cycle_repeat k).2, cycle_remainder r small]

private theorem target_tail_coeff (k r : Nat) (small : r < 3) :
    2^(9+3*k+r) < 3^(7+2*k+(if r=0 then 0 else 1)) := by
  have compare : 8^k ≤ 9^k := Nat.pow_le_pow_left (by decide : 8 ≤ 9) k
  have positive : 0 < 8^k := Nat.pow_pos (by decide : 0 < 8)
  interval_cases r <;>
    simp only [pow_add, pow_mul] <;> norm_num <;> nlinarith

/-- The actual common-denominator rational orbit has expanding coefficient
at EVERY positive ordinary clock, including all repetitions of its cycle. -/
theorem target_all_prefix_expand (j : Nat) (positive : 0 < j) :
    2^j < 3^(numeratorOdds 2187 j (-6487)) := by
  by_cases early : j < 9
  · interval_cases j <;> decide
  · let k := (j-9)/3
    let r := (j-9)%3
    have small : r < 3 := Nat.mod_lt _ (by decide)
    have clock : j = 9+3*k+r := by
      have division := Nat.mod_add_div (j-9) 3
      dsimp [k,r]
      omega
    rw [clock, target_tail_count k r small]
    exact target_tail_coeff k r small

/-- The twelve explicit ordinary states certify the entry into the negative
cycle -7,-10,-5 and the affine relation of the two starting shadows. -/
theorem target_state_certificate :
    (8*(-6005)+19*2187 : Int) = -6487 ∧
    (List.range 12).map (fun j => numeratorOrbit 2187 j (-6487)) =
      [-6487,-8637,-11862,-5931,-7803,-10611,-14823,-21141,
       -30618,-15309,-21870,-10935] ∧
    numeratorOrbit 2187 12 (-6487) = -15309 := by
  decide

#print axioms source_certificate
#print axioms source_all_prefix_contract
#print axioms target_all_prefix_expand
#print axioms target_state_certificate

end CollatzCentral.RationalShadowTest
