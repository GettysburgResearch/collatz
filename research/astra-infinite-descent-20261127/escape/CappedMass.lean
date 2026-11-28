import TwoGapRouting
import Mathlib.Algebra.BigOperators.Ring.Finset

/-! An explicit five-trit certificate for total genuine finite inverse-word
mass with every gap at most six. The table inequality itself is evaluated
in the Lean kernel. -/
set_option autoImplicit false
set_option warningAsError true
set_option maxRecDepth 30000
namespace CappedMass
open Finset Collatz.TwoGapRouting

/-- The 243 nonnegative 10-bit entries in increasing residue order. -/
private def packed : ℕ := 310899513283293319091333240852572990493861824023493837950458487346511760212175413811957448696663047476652382527115711751133655882520108412282574417084532468309878145350377071449380965349329492032645273181792505684277463367615276329327968899049685767620788857324646962924902574052388952380032303796759582244520434136791462380573440698897316249746278233761682283421824199560542241383068162218350799591601875799120910751093370399956433009940879214729008799951266907988677716760924285565784198444548231744612178364412122477325823330274845192450523154959891514598378724379042785963302678609313002382954993341225350556775215449540465239071917628257971110599036081651415218534099124252413167920726323799596385669062726092677218422390961152

def potential (y : ℕ) : ℕ := (packed >>> (10*(y%243)))%1024

def allowed (e y : ℕ) : Prop := (2^e*y)%9=4 ∨ (2^e*y)%9=7

instance (e y : ℕ) : Decidable (allowed e y) := inferInstanceAs (Decidable (_ ∨ _))

def op (f : ℕ → ℕ) (y : ℕ) : ℕ :=
  ∑i∈range 6, if allowed (i+1) y then 3*2^(6-(i+1))*f (2^(i+1)*y/3) else 0

/-- Dividing by 64^d yields the sum of the original multipliers over all
unit-terminal d-gap words formed from exponents one through six. -/
def numerator : ℕ → ℕ → ℕ
  | 0,y => if y%3=0 then 0 else 1
  | d+1,y => op (numerator d) y

private theorem row0 : ∀b : Fin 27, 48*potential (0+b)≤op potential (0+b) := by decide +kernel
private theorem row1 : ∀b : Fin 27, 48*potential (27+b)≤op potential (27+b) := by decide +kernel
private theorem row2 : ∀b : Fin 27, 48*potential (54+b)≤op potential (54+b) := by decide +kernel
private theorem row3 : ∀b : Fin 27, 48*potential (81+b)≤op potential (81+b) := by decide +kernel
private theorem row4 : ∀b : Fin 27, 48*potential (108+b)≤op potential (108+b) := by decide +kernel
private theorem row5 : ∀b : Fin 27, 48*potential (135+b)≤op potential (135+b) := by decide +kernel
private theorem row6 : ∀b : Fin 27, 48*potential (162+b)≤op potential (162+b) := by decide +kernel
private theorem row7 : ∀b : Fin 27, 48*potential (189+b)≤op potential (189+b) := by decide +kernel
private theorem row8 : ∀b : Fin 27, 48*potential (216+b)≤op potential (216+b) := by decide +kernel
private theorem row9 : ∀b : Fin 27, 48*potential (243+b)≤op potential (243+b) := by decide +kernel
private theorem row10 : ∀b : Fin 27, 48*potential (270+b)≤op potential (270+b) := by decide +kernel
private theorem row11 : ∀b : Fin 27, 48*potential (297+b)≤op potential (297+b) := by decide +kernel
private theorem row12 : ∀b : Fin 27, 48*potential (324+b)≤op potential (324+b) := by decide +kernel
private theorem row13 : ∀b : Fin 27, 48*potential (351+b)≤op potential (351+b) := by decide +kernel
private theorem row14 : ∀b : Fin 27, 48*potential (378+b)≤op potential (378+b) := by decide +kernel
private theorem row15 : ∀b : Fin 27, 48*potential (405+b)≤op potential (405+b) := by decide +kernel
private theorem row16 : ∀b : Fin 27, 48*potential (432+b)≤op potential (432+b) := by decide +kernel
private theorem row17 : ∀b : Fin 27, 48*potential (459+b)≤op potential (459+b) := by decide +kernel
private theorem row18 : ∀b : Fin 27, 48*potential (486+b)≤op potential (486+b) := by decide +kernel
private theorem row19 : ∀b : Fin 27, 48*potential (513+b)≤op potential (513+b) := by decide +kernel
private theorem row20 : ∀b : Fin 27, 48*potential (540+b)≤op potential (540+b) := by decide +kernel
private theorem row21 : ∀b : Fin 27, 48*potential (567+b)≤op potential (567+b) := by decide +kernel
private theorem row22 : ∀b : Fin 27, 48*potential (594+b)≤op potential (594+b) := by decide +kernel
private theorem row23 : ∀b : Fin 27, 48*potential (621+b)≤op potential (621+b) := by decide +kernel
private theorem row24 : ∀b : Fin 27, 48*potential (648+b)≤op potential (648+b) := by decide +kernel
private theorem row25 : ∀b : Fin 27, 48*potential (675+b)≤op potential (675+b) := by decide +kernel
private theorem row26 : ∀b : Fin 27, 48*potential (702+b)≤op potential (702+b) := by decide +kernel

private theorem local_table (r : Fin 729) : 48*potential r≤op potential r := by
  have pick (a : ℕ) (ha : a<27) : ∀b : Fin 27, 48*potential (27*a+b)≤op potential (27*a+b) := by
    match a,ha with
    | 0, _ => exact row0
    | 1, _ => exact row1
    | 2, _ => exact row2
    | 3, _ => exact row3
    | 4, _ => exact row4
    | 5, _ => exact row5
    | 6, _ => exact row6
    | 7, _ => exact row7
    | 8, _ => exact row8
    | 9, _ => exact row9
    | 10, _ => exact row10
    | 11, _ => exact row11
    | 12, _ => exact row12
    | 13, _ => exact row13
    | 14, _ => exact row14
    | 15, _ => exact row15
    | 16, _ => exact row16
    | 17, _ => exact row17
    | 18, _ => exact row18
    | 19, _ => exact row19
    | 20, _ => exact row20
    | 21, _ => exact row21
    | 22, _ => exact row22
    | 23, _ => exact row23
    | 24, _ => exact row24
    | 25, _ => exact row25
    | 26, _ => exact row26
    | k+27, h => omega
  have division:=Nat.mod_add_div r.val 27
  obtain hyp:=pick (r.val/27) (by omega) ⟨r.val%27,Nat.mod_lt _ (by decide)⟩
  simpa only [show 27*(r.val/27)+r.val%27=r.val by omega] using hyp

private theorem local_range (r : Fin 243) : potential r≤1000 ∧
    (r.val%3=0 → potential r=0) ∧ (r.val%3≠0 → 52≤potential r) := by decide +revert +kernel

private theorem range_bound (y : ℕ) : potential y≤1000 ∧
    (y%3=0 → potential y=0) ∧ (y%3≠0 → 52≤potential y) := by
  have result:=local_range ⟨y%243,Nat.mod_lt _ (by decide)⟩
  have mod3 : y%243%3=y%3 := by omega
  simpa only [potential,Nat.mod_mod,mod3] using result

theorem one_level (y : ℕ) : 48*potential y≤op potential y := by
  let r:=y%729
  have mod243 : r%243=y%243 := by dsimp [r]; omega
  have py : potential r=potential y := by simp only [potential,mod243]
  have operatorEq : op potential r=op potential y := by
    unfold op
    apply sum_congr rfl
    intro i _
    have md : (2^(i+1)*r)%729=(2^(i+1)*y)%729 := by simp [r,Nat.mul_mod]
    have nine : (2^(i+1)*r)%9=(2^(i+1)*y)%9 := by omega
    have child : (2^(i+1)*r/3)%243=(2^(i+1)*y/3)%243 := by
      rw [←Nat.mod_mul_right_div_self,←Nat.mod_mul_right_div_self]
      exact congrArg (·/3) md
    simp only [allowed,nine,potential,child]
    rfl
  have result:=local_table ⟨r,Nat.mod_lt _ (by decide)⟩
  simpa only [py,operatorEq] using result

private theorem scale (c : ℕ) (f : ℕ → ℕ) (y : ℕ) :
    op (fun z => c*f z) y=c*op f y := by
  unfold op
  rw [mul_sum]
  apply sum_congr rfl
  intro i _
  split <;> simp [Nat.mul_left_comm]

private theorem mono (y : ℕ) {f g : ℕ → ℕ} (h : ∀n, f n≤g n) : op f y≤op g y := by
  unfold op
  apply Finset.sum_le_sum
  intro i _
  split
  · exact Nat.mul_le_mul_left _ (h _)
  · rfl

theorem transfer (d y : ℕ) : 48^d*potential y≤1000*numerator d y := by
  induction d generalizing y with
  | zero =>
    obtain ⟨upper,z,_⟩:=range_bound y
    by_cases nz : y%3=0
    · simp [numerator,nz,z nz]
    · simpa [numerator,nz] using upper
  | succ d ih =>
    calc
      _=48^d*(48*potential y) := by rw [pow_succ]; ring
      _≤48^d*op potential y := Nat.mul_le_mul_left _ (one_level y)
      _=op (fun z => 48^d*potential z) y := (scale _ _ _).symm
      _≤op (fun z => 1000*numerator d z) y := mono y ih
      _=_ := scale _ _ _

theorem unit_mass (d y : ℕ) (yu : y%3≠0) : 52*48^d≤1000*numerator d y := by
  have low: 52≤potential y := (range_bound y).2.2 yu
  have weighted:=Nat.mul_le_mul_right (48^d) low
  exact weighted.trans (by simpa only [Nat.mul_comm (potential y)] using transfer d y)

theorem ordinary_gap (y e : ℕ) (ep : 0<e) (ok : allowed e y) :
    let z:=2^e*y/3
    z%3≠0 ∧ run e z=y ∧ odds e z=1 ∧ z%2=1 := by
  dsimp only
  have eq : 3*(2^e*y/3)+1=2^e*y := by unfold allowed at ok; omega
  have unit : (2^e*y/3)%3≠0 := by unfold allowed at ok; omega
  exact ⟨unit,gap e _ y ep eq⟩

#print axioms one_level
#print axioms transfer
#print axioms unit_mass
#print axioms ordinary_gap
end CappedMass
