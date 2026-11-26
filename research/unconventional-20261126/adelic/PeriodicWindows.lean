import Mathlib.Tactic.Ring
import Mathlib.Algebra.Ring.Int.Parity

/-! Finite algebra for periodic-window surgery. An integer affine segment clears the
    dyadic clock. Reference values are numerators over one common denominator D.
    The analytic Subspace Theorem and its asymptotic consequences are not formalized. -/
namespace PeriodicWindows

structure Segment where
  clock : ℕ
  grade : ℕ
  carry : ℤ
  deriving DecidableEq, Repr

def identity : Segment := ⟨0, 0, 0⟩
def letter : Bool → Segment
  | false => ⟨1, 0, 0⟩
  | true => ⟨1, 1, 1⟩

def join (s t : Segment) : Segment :=
  ⟨s.clock + t.clock, s.grade + t.grade,
    3 ^ t.grade * s.carry + 2 ^ s.clock * t.carry⟩

def word : List Bool → Segment
  | [] => identity
  | b :: w => join (letter b) (word w)

def Holds (s : Segment) (x y : ℤ) : Prop :=
  (2 : ℤ) ^ s.clock * y = 3 ^ s.grade * x + s.carry

def T (x : ℤ) : ℤ := if x % 2 = 0 then x / 2 else (3*x+1) / 2

def itinerary : ℕ → ℤ → List Bool
  | 0, _ => []
  | n+1, x => decide (x % 2 ≠ 0) :: itinerary n (T x)

def orbit : ℕ → ℤ → ℤ
  | 0, x => x
  | n+1, x => orbit n (T x)

theorem holds_join {s t : Segment} {x y z : ℤ}
    (hs : Holds s x y) (ht : Holds t y z) : Holds (join s t) x z := by
  change 2 ^ (s.clock + t.clock) * z = 3 ^ (s.grade + t.grade) * x + _
  rw [pow_add, pow_add, mul_assoc, ht]
  unfold Holds at hs
  change _ = _ + (3 ^ t.grade * s.carry + 2 ^ s.clock * t.carry)
  calc
    _ = 3 ^ t.grade * (2 ^ s.clock * y) + 2 ^ s.clock * t.carry := by ring
    _ = _ := by rw [hs]; ring

theorem actual_trace (n : ℕ) (x : ℤ) : Holds (word (itinerary n x)) x (orbit n x) := by
  induction n generalizing x with
  | zero => simp [itinerary, orbit, word, identity, Holds]
  | succ n ih =>
      apply holds_join _ (ih (T x))
      by_cases h : x % 2 = 0 <;> simp [Holds, letter, T, h] <;> omega

/-- Exact numerator added when the old and new reference phases differ. -/
def defect (s : Segment) (D u v : ℤ) : ℤ :=
  3 ^ s.grade * u + D * s.carry - 2 ^ s.clock * v

theorem shifted_segment {s : Segment} {x y : ℤ} (h : Holds s x y) (D u v : ℤ) :
    2 ^ s.clock * (D * y - v) =
      3 ^ s.grade * (D * x - u) + defect s D u v := by
  unfold Holds at h
  unfold defect
  calc
    _ = D * (2 ^ s.clock * y) - 2 ^ s.clock * v := by ring
    _ = _ := by rw [h]; ring

/-- Composition simultaneously tracks the preceding dyadic and following ternary clocks. -/
theorem defect_join (s t : Segment) (D u v w : ℤ) :
    defect (join s t) D u w =
      3 ^ t.grade * defect s D u v + 2 ^ s.clock * defect t D v w := by
  simp only [defect, join, pow_add]
  ring

/-- Zero contribution on a correctly followed rational phase. -/
theorem genuine_zero (s : Segment) (D u v : ℤ)
    (h : 2 ^ s.clock * v = 3 ^ s.grade * u + D * s.carry) : defect s D u v = 0 := by
  unfold defect
  rw [h, sub_self]

/-- For a legal prefix followed by a wrong letter, the complete shifted numerator
    has precisely its prefix dyadic factor. This includes an arbitrary remaining
    substantive word and an arbitrary integral terminal reference. -/
theorem mismatch_factor (p suffix : Segment) (b : Bool) (D u v z : ℤ)
    (hprefix : defect p D u v = 0)
    (hwrong : Odd (3 ^ (letter b).grade * v + D * (letter b).carry)) :
    ∃ a : ℤ, Odd a ∧
      defect (join p (join (letter b) suffix)) D u z = 2 ^ p.clock * a := by
  let a := defect (join (letter b) suffix) D v z
  refine ⟨a, ?_, ?_⟩
  · have h3 : Odd ((3 : ℤ)^suffix.grade) := (show Odd (3 : ℤ) by decide).pow
    obtain ⟨j, hj⟩ := h3.mul hwrong
    refine ⟨j + D * suffix.carry - 2 ^ suffix.clock * z, ?_⟩
    change defect (join (letter b) suffix) D v z = _
    have hb : (letter b).clock = 1 := by cases b <;> rfl
    unfold defect join
    simp only [hb, pow_add, pow_one]
    calc
      _ = 3 ^ suffix.grade * (3 ^ (letter b).grade * v + D * (letter b).carry) +
            2 * (D * suffix.carry - 2 ^ suffix.clock * z) := by ring
      _ = _ := by rw [hj]; ring
  · rw [defect_join p (join (letter b) suffix) D u v z, hprefix, mul_zero, zero_add]

/-- A window in which all errors cancel has its full clock dividing the initial
    shifted numerator.  This is the rank-one case of the written proof. -/
theorem no_defect_divides {s : Segment} {x y : ℤ} (h : Holds s x y) (D u v : ℤ)
    (hz : defect s D u v = 0) : (2 : ℤ)^s.clock ∣ D*x-u := by
  have hh := shifted_segment h D u v
  rw [hz, add_zero] at hh
  have dvd : (2 : ℤ)^s.clock ∣ (3 : ℤ)^s.grade * (D*x-u) := ⟨D*y-v, hh.symm⟩
  have dn := Int.natAbs_dvd_natAbs.mpr dvd
  simp only [Int.natAbs_mul, Int.natAbs_pow] at dn
  apply Int.natAbs_dvd_natAbs.mp
  simp only [Int.natAbs_pow]
  exact (Nat.Coprime.pow s.clock s.grade (by decide : Nat.Coprime 2 3)).dvd_of_dvd_mul_left dn

#print axioms actual_trace
#print axioms shifted_segment
#print axioms defect_join
#print axioms genuine_zero
#print axioms mismatch_factor
#print axioms no_defect_divides
end PeriodicWindows
