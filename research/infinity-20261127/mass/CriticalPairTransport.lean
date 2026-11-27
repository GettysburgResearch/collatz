import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-! Exact common-middle translation for two distinct physical rational words.
A state (k,v) stores the signed numerator v over denominator 3^k. -/
set_option autoImplicit false
set_option warningAsError true

namespace CriticalPairTransport

def grade : List Bool → Nat
  | [] => 0
  | b :: w => grade w + if b then 1 else 0

def offset : List Bool → Int
  | [] => 0
  | b :: w => (if b then 3 ^ grade w else 0) + 2 * offset w

def source (w : List Bool) (y : Int) : Int :=
  2 ^ w.length * y - offset w

def step (z : Nat × Int) : Nat × Int :=
  if z.2 % 2 = 0 then (z.1, z.2 / 2)
  else match z.1 with
  | 0 => (0, (3*z.2+1)/2)
  | k+1 => (k, (z.2+3^k)/2)

def run : Nat → Nat × Int → Nat × Int
  | 0, z => z
  | j+1, z => run j (step z)

theorem grade_append (u v : List Bool) : grade (u++v) = grade u + grade v := by
  induction u with
  | nil => simp [grade]
  | cons b u ih => cases b <;> (simp [grade, ih]; all_goals omega)

theorem offset_append (u v : List Bool) :
    offset (u++v) = 3^grade v * offset u + 2^u.length * offset v := by
  induction u with
  | nil => simp [offset]
  | cons b u ih =>
    cases b <;> simp [offset, ih, grade_append, pow_add, pow_succ] <;> ring

private theorem three_pow_mod_two (k : Nat) : (3:Int)^k % 2 = 1 := by
  induction k with
  | zero => decide
  | succ k ih => rw [pow_succ, Int.mul_emod, ih]; rfl

theorem source_even (w : List Bool) (y : Int) :
    source (false::w) y = 2 * source w y := by
  simp [source, offset, pow_succ]
  ring

theorem source_odd (w : List Bool) (y : Int) :
    source (true::w) y = 2*source w y - 3^grade w := by
  simp [source, offset, pow_succ]
  ring

/-- Executing the actual reduced-power step at every prescribed clock gives
the ordinary target. A unit input remains reduced until it is ordinary. -/
theorem physical_word (w : List Bool) (y : Int) :
    run w.length (grade w, source w y) = (0, y) := by
  induction w with
  | nil => simp [grade, source, offset, run]
  | cons b w ih =>
    cases b
    · simp [grade, source_even, run, step, ih]
    · simpa [grade, source_odd, run, step, three_pow_mod_two] using ih

/-- The two physical words share the entire middle including its terminal
zeros. On the two final ticks branch one clears then halves, while branch
two halves then clears. The numerator translation contains no middle offset. -/
theorem common_middle_translation (u v w : List Bool) (q : Int)
    (sameClock : v.length = u.length) :
    source (v++w++[false,true]) (3*q) - source (u++w++[true,false]) q =
      2^(u.length+w.length)*(8*q-1) -
        3^(grade w+1)*(offset v-offset u) := by
  simp [source, offset_append, grade_append, sameClock, grade, offset, pow_add]
  ring

/-- With equal-grade heads, this is a translation between actual sources of
the same denominator and full physical length. -/
theorem physical_pair (u v w : List Bool) (q : Int)
    (sameClock : v.length=u.length) (sameGrade : grade v=grade u) :
    let a := source (u++w++[true,false]) q
    let d := 2^(u.length+w.length)*(8*q-1) -
      3^(grade w+1)*(offset v-offset u)
    let k := grade u + grade w + 1
    let n := u.length + w.length + 2
    run n (k,a) = (0,q) ∧ run n (k,a+d) = (0,3*q) := by
  dsimp only
  have h₁ := physical_word (u++w++[true,false]) q
  have h₂ := physical_word (v++w++[false,true]) (3*q)
  have h := common_middle_translation u v w q sameClock
  have ha : source (u++w++[true,false]) q +
      (2^(u.length+w.length)*(8*q-1) - 3^(grade w+1)*(offset v-offset u)) =
      source (v++w++[false,true]) (3*q) := by omega
  rw [ha]
  constructor
  · simpa [grade_append,grade,Nat.add_assoc] using h₁
  · simpa [grade_append,grade,sameGrade,sameClock,Nat.add_assoc] using h₂

/-- Each point of the normalized interval permits a bounded next residual,
using one of the four actual four-gap digits. -/
theorem carry_digit (x : Rat) (low : 65/49 ≤ x) (high : x ≤ 103/49) :
    ∃ c : Nat, (c=65 ∨ c=73 ∨ c=85 ∨ c=103) ∧
      65/49 ≤ (81*x-c)/32 ∧ (81*x-c)/32 ≤ 103/49 := by
  by_cases h₁ : x ≤ (65+32*(103/49:Rat))/81
  · exact ⟨65, by decide, by norm_num at *; constructor <;> linarith⟩
  by_cases h₂ : x ≤ (73+32*(103/49:Rat))/81
  · exact ⟨73, by decide, by norm_num at *; constructor <;> linarith⟩
  by_cases h₃ : x ≤ (85+32*(103/49:Rat))/81
  · exact ⟨85, by decide, by norm_num at *; constructor <;> linarith⟩
  · exact ⟨103, by decide, by norm_num at *; constructor <;> linarith⟩

#print axioms physical_word
#print axioms common_middle_translation
#print axioms physical_pair
#print axioms carry_digit
end CriticalPairTransport
