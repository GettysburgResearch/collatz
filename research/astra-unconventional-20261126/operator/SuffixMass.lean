import Mathlib.Data.Rat.Defs
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-! Terminal residue compatibility and the finite stopping-tree inequality.
A list is read backwards from the terminal positive integer. -/

namespace Collatz.SuffixMass

set_option autoImplicit false

def grade : List Bool → ℕ
  | [] => 0
  | false :: w => grade w
  | true :: w => grade w + 1

def offset : List Bool → ℤ
  | [] => 0
  | false :: w => offset w
  | true :: w => 3 * offset w + 2 ^ w.length

/-- Reverse even and odd shortcut steps, using exact integral preimages. -/
def fits : List Bool → ℤ → Prop
  | [], _ => True
  | false :: w, x => fits w (2*x)
  | true :: w, x => ∃ z : ℤ, 2*x=3*z+1 ∧ fits w z

private theorem cancel_two_pow {d : ℤ} (h : ℕ) (hd : (3 : ℤ) ∣ 2^h*d) : (3 : ℤ) ∣ d := by
  induction h with
  | zero => simpa using hd
  | succ h ih =>
    apply ih
    have hmul : (3 : ℤ) ∣ 2 * (2^h*d) := by
      simpa only [pow_succ, mul_right_comm, mul_comm, mul_assoc, mul_left_comm] using hd
    omega

/-- A whole word fits a terminal if and only if its one affine endpoint
congruence holds, even when intermediate odd divisibilities are required. -/
theorem fits_iff_residue (w : List Bool) (x : ℤ) :
    fits w x ↔ ∃ t : ℤ, 2^w.length*x=offset w+3^(grade w)*t := by
  induction w generalizing x with
  | nil => simp [fits, offset, grade]
  | cons e w ih =>
    cases e with
    | false =>
      simp only [fits, grade, offset, List.length_cons, pow_succ]
      rw [ih]
      constructor <;> rintro ⟨t, ht⟩ <;> refine ⟨t, ?_⟩ <;> linear_combination ht
    | true =>
      simp only [fits, grade, offset, List.length_cons, pow_succ]
      constructor
      · rintro ⟨z, hx, hz⟩
        obtain ⟨t, ht⟩ := (ih z).mp hz
        exact ⟨t, by linear_combination (2 : ℤ)^w.length * hx + 3 * ht⟩
      · rintro ⟨t, ht⟩
        have hd : (3 : ℤ) ∣ 2^w.length*(2*x-1) := by
          refine ⟨offset w+3^(grade w)*t, ?_⟩
          linear_combination ht
        obtain ⟨z, hz⟩ := cancel_two_pow _ hd
        refine ⟨z, by omega, (ih z).mpr ⟨t, ?_⟩⟩
        have hh : 3*(2^w.length*z) = 3*(offset w+3^(grade w)*t) := by
          linear_combination ht - (2 : ℤ)^w.length*hz
        omega

/-- A finite binary stopping tree. Skipped leaves carry zero terminal mass. -/
inductive Tree
  | skip
  | stop
  | split (even odd : Tree)

def mass : Tree → ℚ
  | .skip => 0
  | .stop => 1
  | .split even odd => mass even + mass odd / 3

def crosses (g m : ℚ) : Tree → Prop
  | .skip => True
  | .stop => g ≤ m
  | .split even odd => crosses g (m/2) even ∧ crosses g (3*m/2) odd

/-- The sum of ternary terminal disk masses at a prefix-free finite family
is bounded by the square of the starting gain divided by the barrier squared. -/
theorem stopped_mass (t : Tree) {g m : ℚ} (hg : 0 ≤ g) (hm : 0 ≤ m)
    (hc : crosses g m t) : mass t * g^2 ≤ m^2 := by
  induction t generalizing m with
  | skip => simp [mass, sq_nonneg]
  | stop =>
    change g ≤ m at hc
    simp only [mass, one_mul]
    nlinarith [mul_nonneg (sub_nonneg.mpr hc) (add_nonneg hm hg)]
  | split even odd ihe iho =>
    obtain ⟨he, ho⟩ := hc
    have h₀ := ihe (m := m/2) (by linarith) he
    have h₁ := iho (m := 3*m/2) (by linarith) ho
    change (mass even+mass odd/3)*g^2 ≤ m^2
    linarith only [h₀, h₁]

/-- At a strict unit-gain crossing, an initial reverse odd is already a
stop costing one third. All continuations after an even cost at most one quarter. -/
theorem strict_unit_mass (even : Tree) (he : crosses 1 (1/2) even) :
    mass (.split even .stop) ≤ 7/12 := by
  have h := stopped_mass even (by norm_num : 0 ≤ (1 : ℚ)) (by norm_num : 0 ≤ (1/2 : ℚ)) he
  norm_num [mass] at h ⊢
  linarith

/-- Integral reverse paths from a lower ascent state, recording the bit counts.
The factor b will be a nonnegative power of two on the hard family. -/
inductive AscentPath (i : ℕ) (b : ℤ) : ℤ → ℕ → ℕ → Prop
  | root : AscentPath i b (3^i*b-1) 0 0
  | even {x : ℤ} {e h : ℕ} : AscentPath i b x e h → AscentPath i b (2*x) (e+1) h
  | odd {x z : ℤ} {e h : ℕ} :
      AscentPath i b x e h → 3*z+1=2*x → AscentPath i b z e (h+1)

/-- Simultaneous tracking of the integral signed center through any chosen
prefix, including its last permitted odd inverse. -/
theorem signed_cut_prefix {i e h : ℕ} {b x : ℤ} (path : AscentPath i b x e h) (hh : h ≤ i) :
    ∃ A : ℤ, 1 ≤ A ∧ A ≤ 2^e ∧ x=2^(e+h)*3^(i-h)*b-A := by
  induction path with
  | root => exact ⟨1, by norm_num, by norm_num, by simp⟩
  | @even x e h _ ih =>
    obtain ⟨A, hA, hB, hx⟩ := ih hh
    refine ⟨2*A, by omega, ?_, ?_⟩
    · rw [pow_succ]
      omega
    · rw [show e+1+h = (e+h)+1 by omega, pow_succ, hx]
      ring
  | @odd x z e h _ he ih =>
    obtain ⟨A, hA, hB, hx⟩ := ih (by omega)
    let d : ℤ := 2^(e+(h+1))*3^(i-(h+1))*b
    have hr : i-h = (i-(h+1))+1 := by omega
    have hd : 3*d = 2*(x+A) := by
      unfold d
      rw [show e+(h+1)=(e+h)+1 by omega, hx, hr, pow_succ, pow_succ]
      ring
    exact ⟨d-z, by omega, by omega, by change z=d-(d-z); ring⟩

/-- The actual cut after i reverse odd steps belongs to a family determined
only by the even count and the bounded positive integral center. -/
theorem post_cut_class {i e : ℕ} {b x : ℤ} (path : AscentPath i b x e i) :
    ∃ A : ℤ, 1 ≤ A ∧ A ≤ 2^e ∧ x=2^(e+i)*b-A := by
  simpa using signed_cut_prefix path (le_refl i)

/-- Shifted formal forward values. A leading run of odd steps fixes zero. -/
inductive ForwardShift : ℕ → ℚ → Prop
  | root : ForwardShift 0 0
  | even {k : ℕ} {v : ℚ} : ForwardShift k v → ForwardShift k ((v+1)/2)
  | odd {k : ℕ} {v : ℚ} : ForwardShift k v → ForwardShift (k+1) (3*v/2)

/-- The signed forward correction after its first possible even is bounded
by the subsequent odd count alone, uniformly over the chosen word. -/
theorem forward_shift_band {k : ℕ} {v : ℚ} (h : ForwardShift k v) :
    0 ≤ v ∧ v ≤ (3/2 : ℚ)^k := by
  induction h with
  | root => norm_num
  | @even k v _ ih =>
    have hp : (1 : ℚ) ≤ (3/2 : ℚ)^k := one_le_pow₀ (by norm_num)
    constructor <;> linarith [ih.1, ih.2]
  | @odd k v _ ih =>
    rw [pow_succ]
    constructor <;> linarith [ih.1, ih.2]

/-- Shifted formal reverse values after e even and h odd inverses. -/
inductive ReverseShift (v : ℚ) : ℕ → ℕ → ℚ → Prop
  | root : ReverseShift v 0 0 v
  | even {e h : ℕ} {x : ℚ} : ReverseShift v e h x → ReverseShift v (e+1) h (2*x-1)
  | odd {e h : ℕ} {x : ℚ} : ReverseShift v e h x → ReverseShift v e (h+1) (2*x/3)

/-- The complete subtraction charged to the reverse even letters is bounded
only by their number, for arbitrary real-affine control words over ℚ. -/
theorem reverse_shift_charge {v x : ℚ} {e h : ℕ} (path : ReverseShift v e h x) :
    ∃ c : ℚ, 0 ≤ c ∧ c ≤ 2^e-1 ∧ x=2^e*(2/3 : ℚ)^h*v-c := by
  induction path with
  | root => exact ⟨0, by norm_num, by norm_num, by simp⟩
  | @even e h x _ ih =>
    obtain ⟨c, hc, hb, hx⟩ := ih
    refine ⟨2*c+1, by linarith, ?_, ?_⟩
    · rw [pow_succ]
      linarith
    · rw [pow_succ, hx]
      ring
  | @odd e h x _ ih =>
    obtain ⟨c, hc, hb, hx⟩ := ih
    refine ⟨2*c/3, by linarith, by linarith, ?_⟩
    rw [pow_succ, hx]
    ring

end Collatz.SuffixMass

#print axioms Collatz.SuffixMass.fits_iff_residue
#print axioms Collatz.SuffixMass.stopped_mass
#print axioms Collatz.SuffixMass.strict_unit_mass
#print axioms Collatz.SuffixMass.signed_cut_prefix
#print axioms Collatz.SuffixMass.post_cut_class

#print axioms Collatz.SuffixMass.forward_shift_band
#print axioms Collatz.SuffixMass.reverse_shift_charge
