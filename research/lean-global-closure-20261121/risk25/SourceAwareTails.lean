import Std

/-!
Finite arithmetic for source-aware triadic tail constructions.

The complete original/complementary carries are processed together.  The
module proves a no-cancellation theorem for the terminal choice `-x-1`
and full-denominator resets for every terminal value congruent to `-x`
modulo three, after the blocks `011` and `100`.

There is no universal Collatz, rationality, or triadic-existence premise
or conclusion.  The ordinary-source interpretation uses the explicit
finite affine identity supplied to `negative_anchor_identity` and to
`calibrated_anchor_reset`.
-/

namespace Collatz.SourceAwareTails

structure Carries where
  u : Int
  p : Int
  c : Int
  d : Int
  seenOdd : Bool
  seenEven : Bool
  deriving Repr

def initial : Carries := ⟨1, 1, 0, 0, false, false⟩

/-- `odd = true` is an original odd source, not an odd complementary source. -/
def advance (s : Carries) (odd : Bool) : Carries :=
  if odd then
    ⟨2 * s.u, 3 * s.p, 3 * s.c + s.u, s.d, true, s.seenEven⟩
  else
    ⟨2 * s.u, s.p, s.c, 3 * s.d + s.u, s.seenOdd, true⟩

def run : List Bool → Carries → Carries
  | [], s => s
  | e :: w, s => run w (advance s e)

def trace (w : List Bool) : Carries := run w initial

structure Good (s : Carries) : Prop where
  powerUnit : s.u % 3 ≠ 0
  original : s.seenOdd = true → s.p % 3 = 0 ∧ s.c % 3 ≠ 0
  complementary : s.seenEven = true → s.d % 3 ≠ 0
  shiftedSum : s.seenOdd = true → s.seenEven = true →
    (s.c + s.d + s.u) % 3 ≠ 0

theorem good_initial : Good initial := by
  constructor
  · decide
  · simp [initial]
  · simp [initial]
  · simp [initial]

theorem good_advance (s : Carries) (e : Bool) (h : Good s) :
    Good (advance s e) := by
  have hu := h.powerUnit
  cases e with
  | false =>
    constructor
    · simp only [advance, Bool.false_eq_true, ↓reduceIte]
      omega
    · intro ho
      simp only [advance, Bool.false_eq_true, ↓reduceIte] at ho ⊢
      exact h.original ho
    · intro _
      simp only [advance, Bool.false_eq_true, ↓reduceIte]
      omega
    · intro ho _
      simp only [advance, Bool.false_eq_true, ↓reduceIte] at ho ⊢
      have hc := (h.original ho).2
      omega
  | true =>
    constructor
    · simp only [advance, ↓reduceIte]
      omega
    · intro _
      simp only [advance, ↓reduceIte]
      constructor <;> omega
    · intro he
      simp only [advance, ↓reduceIte] at he ⊢
      exact h.complementary he
    · intro _ he
      simp only [advance, ↓reduceIte] at he ⊢
      have hd := h.complementary he
      omega

theorem good_run (w : List Bool) (s : Carries) (h : Good s) :
    Good (run w s) := by
  induction w generalizing s with
  | nil => simpa only [run] using h
  | cons e w ih =>
    exact ih (advance s e) (good_advance s e h)

theorem good_trace (w : List Bool) : Good (trace w) :=
  good_run w initial good_initial

/-- The numerator obtained by using the actual integer terminal anchor
`-x-1`, after eliminating `2^K*x` with the original affine identity. -/
def negativeNumerator (s : Carries) (n : Int) : Int :=
  -(s.p * n + s.c + s.d + s.u)

theorem negative_anchor_identity (s : Carries) (n x : Int)
    (hsource : s.u * x = s.p * n + s.c) :
    negativeNumerator s n = -s.u * (x + 1) - s.d := by
  simp only [negativeNumerator, Int.mul_add, Int.mul_one, Int.neg_mul]
  omega

/-- This holds for every finite word containing both parities.
The represented denominator therefore has no cancellable factor three. -/
theorem negativeNumerator_unit (s : Carries) (n : Int)
    (h : Good s) (ho : s.seenOdd = true) (he : s.seenEven = true) :
    negativeNumerator s n % 3 ≠ 0 := by
  have hp := (h.original ho).1
  have hm : (s.p * n) % 3 = 0 := by
    rw [Int.mul_emod, hp]
    simp
  have hs := h.shiftedSum ho he
  unfold negativeNumerator
  omega

theorem negativeNumerator_trace_unit (w : List Bool) (n : Int)
    (ho : (trace w).seenOdd = true) (he : (trace w).seenEven = true) :
    negativeNumerator (trace w) n % 3 ≠ 0 :=
  negativeNumerator_unit (trace w) n (good_trace w) ho he

/-- A general source-aware affine terminal value `a*x+b`. -/
def affineNumerator (s : Carries) (n a b : Int) : Int :=
  a * (s.p * n + s.c) + b * s.u - s.d

theorem affine_anchor_identity (s : Carries) (n x a b : Int)
    (hsource : s.u * x = s.p * n + s.c) :
    affineNumerator s n a b = s.u * (a * x + b) - s.d := by
  unfold affineNumerator
  rw [← hsource, Int.mul_add]
  simp [Int.mul_comm, Int.mul_left_comm]

/-- The failure extends to the full affine congruence class `a=b=-1 mod 3`. -/
theorem affineNumerator_unit (s : Carries) (n a b : Int)
    (h : Good s) (ho : s.seenOdd = true) (he : s.seenEven = true)
    (ha : a % 3 = 2) (hb : b % 3 = 2) :
    affineNumerator s n a b % 3 ≠ 0 := by
  have hp := (h.original ho).1
  have hs := h.shiftedSum ho he
  have hm : (s.p * n) % 3 = 0 := by
    rw [Int.mul_emod, hp]
    simp
  have hc : (s.p * n + s.c) % 3 = s.c % 3 := by omega
  have hleft : (a * (s.p * n + s.c)) % 3 = (2 * (s.c % 3)) % 3 := by
    rw [Int.mul_emod, ha, hc]
  have hright : (b * s.u) % 3 = (2 * (s.u % 3)) % 3 := by
    rw [Int.mul_emod, hb]
  unfold affineNumerator
  omega

/-- The numerator from a terminal value `z`, before reducing powers of three. -/
def terminalNumerator (s : Carries) (z : Int) : Int := s.u * z - s.d

/-- The cycle-calibrated reflection `h(x)=3-x`, after using the original
source identity to eliminate the current ordinary integer. -/
def reflectionNumerator (s : Carries) (n : Int) : Int :=
  3 * s.u - s.p * n - s.c - s.d

theorem reflection_anchor_identity (s : Carries) (n x : Int)
    (hsource : s.u * x = s.p * n + s.c) :
    reflectionNumerator s n = terminalNumerator s (3 - x) := by
  simp only [reflectionNumerator, terminalNumerator, Int.mul_sub]
  have hu : s.u * 3 = 3 * s.u := Int.mul_comm _ _
  omega

/-- One denominator power is introduced by an alternating two-letter
block, and the reflection numerator acquires exactly the matching factor. -/
theorem reflection_pair01 (s : Carries) (n : Int) :
    reflectionNumerator (advance (advance s false) true) n =
      3 * reflectionNumerator s n := by
  simp only [reflectionNumerator, advance, Bool.false_eq_true, ↓reduceIte]
  have hm : (3 * s.p) * n = 3 * (s.p * n) := Int.mul_assoc _ _ _
  omega

theorem reflection_pair10 (s : Carries) (n : Int) :
    reflectionNumerator (advance (advance s true) false) n =
      3 * reflectionNumerator s n := by
  simp only [reflectionNumerator, advance, Bool.false_eq_true, ↓reduceIte]
  have hm : (3 * s.p) * n = 3 * (s.p * n) := Int.mul_assoc _ _ _
  omega

/-- The finite arithmetic core for every cycle-calibrated rule local
modulo three.  A polynomial with integer coefficients and values
`h(1)=2`, `h(2)=1` supplies `htail` at any source unit modulo three. -/
theorem calibrated_anchor_reset (s : Carries) (n x z : Int)
    (hp : s.p % 3 = 0)
    (hsource : s.u * x = s.p * n + s.c)
    (htail : (z + x) % 3 = 0)
    (hcarry : (s.c + s.d) % 3 ≠ 0) :
    terminalNumerator s z % 3 ≠ 0 := by
  have hm : (s.p * n) % 3 = 0 := by
    rw [Int.mul_emod, hp]
    simp
  have hz : (s.u * (z + x)) % 3 = 0 := by
    rw [Int.mul_emod, htail]
    simp
  rw [Int.mul_add, hsource] at hz
  unfold terminalNumerator
  omega

def block011 (s : Carries) : Carries :=
  advance (advance (advance s false) true) true

def block100 (s : Carries) : Carries :=
  advance (advance (advance s true) false) false

theorem block011_carry_sum (s : Carries) :
    (block011 s).c + (block011 s).d = 9 * s.c + 3 * s.d + 11 * s.u := by
  simp only [block011, advance, Bool.false_eq_true, ↓reduceIte]
  omega

theorem block100_carry_sum (s : Carries) :
    (block100 s).c + (block100 s).d = 3 * s.c + 9 * s.d + 11 * s.u := by
  simp only [block100, advance, Bool.false_eq_true, ↓reduceIte]
  omega

theorem block011_reset (s : Carries) (n x z : Int)
    (hu : s.u % 3 ≠ 0)
    (hsource : (block011 s).u * x = (block011 s).p * n + (block011 s).c)
    (htail : (z + x) % 3 = 0) :
    terminalNumerator (block011 s) z % 3 ≠ 0 := by
  apply calibrated_anchor_reset (block011 s) n x z
  · simp only [block011, advance, Bool.false_eq_true, ↓reduceIte]
    omega
  · exact hsource
  · exact htail
  · rw [block011_carry_sum]
    omega

theorem block100_reset (s : Carries) (n x z : Int)
    (hu : s.u % 3 ≠ 0)
    (hsource : (block100 s).u * x = (block100 s).p * n + (block100 s).c)
    (htail : (z + x) % 3 = 0) :
    terminalNumerator (block100 s) z % 3 ≠ 0 := by
  apply calibrated_anchor_reset (block100 s) n x z
  · simp only [block100, advance, Bool.false_eq_true, ↓reduceIte]
    omega
  · exact hsource
  · exact htail
  · rw [block100_carry_sum]
    omega

/-- The cycle-calibrated affine rule is a concrete instance. -/
theorem reflection_block011_reset (s : Carries) (n x : Int)
    (hu : s.u % 3 ≠ 0)
    (hsource : (block011 s).u * x = (block011 s).p * n + (block011 s).c) :
    terminalNumerator (block011 s) (3 - x) % 3 ≠ 0 := by
  exact block011_reset s n x (3 - x) hu hsource (by omega)

theorem reflection_block100_reset (s : Carries) (n x : Int)
    (hu : s.u % 3 ≠ 0)
    (hsource : (block100 s).u * x = (block100 s).p * n + (block100 s).c) :
    terminalNumerator (block100 s) (3 - x) % 3 ≠ 0 := by
  exact block100_reset s n x (3 - x) hu hsource (by omega)

/-! The actual integer source supplies the affine identity; it is not an
additional assumption about unknown infinite behavior. -/

structure SourceState where
  x : Int
  book : Carries
  deriving Repr

def actualAdvance (s : SourceState) : SourceState :=
  if s.x % 2 = 0 then
    ⟨s.x / 2, advance s.book false⟩
  else
    ⟨(3 * s.x + 1) / 2, advance s.book true⟩

def actualRun : Nat → SourceState → SourceState
  | 0, s => s
  | k + 1, s => actualRun k (actualAdvance s)

def actualTrace (k : Nat) (n : Int) : SourceState :=
  actualRun k ⟨n, initial⟩

theorem actualAdvance_good (s : SourceState) (h : Good s.book) :
    Good (actualAdvance s).book := by
  unfold actualAdvance
  split
  · exact good_advance s.book false h
  · exact good_advance s.book true h

theorem actualAdvance_identity (s : SourceState) (n : Int)
    (hsource : s.book.u * s.x = s.book.p * n + s.book.c) :
    (actualAdvance s).book.u * (actualAdvance s).x =
      (actualAdvance s).book.p * n + (actualAdvance s).book.c := by
  unfold actualAdvance
  split
  · rename_i heven
    have hx : 2 * (s.x / 2) = s.x := by omega
    simp only [advance, Bool.false_eq_true, ↓reduceIte]
    calc
      (2 * s.book.u) * (s.x / 2) = s.book.u * (2 * (s.x / 2)) := by
        simp [Int.mul_comm, Int.mul_left_comm]
      _ = s.book.u * s.x := by rw [hx]
      _ = s.book.p * n + s.book.c := hsource
  · rename_i hodd
    have hx : 2 * ((3 * s.x + 1) / 2) = 3 * s.x + 1 := by omega
    simp only [advance, ↓reduceIte]
    calc
      (2 * s.book.u) * ((3 * s.x + 1) / 2) =
          s.book.u * (2 * ((3 * s.x + 1) / 2)) := by
        simp [Int.mul_comm, Int.mul_assoc]
      _ = s.book.u * (3 * s.x + 1) := by rw [hx]
      _ = 3 * (s.book.u * s.x) + s.book.u := by
        simp [Int.mul_add, Int.mul_comm, Int.mul_left_comm, Int.mul_assoc]
      _ = 3 * (s.book.p * n + s.book.c) + s.book.u := by rw [hsource]
      _ = (3 * s.book.p) * n + (3 * s.book.c + s.book.u) := by
        simp [Int.mul_add, Int.mul_assoc, Int.add_assoc]

theorem actualRun_good (k : Nat) (s : SourceState) (h : Good s.book) :
    Good (actualRun k s).book := by
  induction k generalizing s with
  | zero => exact h
  | succ k ih => exact ih (actualAdvance s) (actualAdvance_good s h)

theorem actualRun_identity (k : Nat) (s : SourceState) (n : Int)
    (hsource : s.book.u * s.x = s.book.p * n + s.book.c) :
    (actualRun k s).book.u * (actualRun k s).x =
      (actualRun k s).book.p * n + (actualRun k s).book.c := by
  induction k generalizing s with
  | zero => exact hsource
  | succ k ih => exact ih (actualAdvance s) (actualAdvance_identity s n hsource)

theorem actualTrace_good (k : Nat) (n : Int) : Good (actualTrace k n).book :=
  actualRun_good k ⟨n, initial⟩ good_initial

theorem actualTrace_identity (k : Nat) (n : Int) :
    (actualTrace k n).book.u * (actualTrace k n).x =
      (actualTrace k n).book.p * n + (actualTrace k n).book.c := by
  exact actualRun_identity k ⟨n, initial⟩ n (by simp [initial])

/-- An all-prefix theorem for the actual integer map, with no source
identity hypothesis: after both parities have occurred, the numerator
of the pulled-back binary-complement terminal anchor is a unit at three. -/
theorem actual_negative_anchor_unit (k : Nat) (n : Int)
    (ho : (actualTrace k n).book.seenOdd = true)
    (he : (actualTrace k n).book.seenEven = true) :
    (-(actualTrace k n).book.u * ((actualTrace k n).x + 1) -
        (actualTrace k n).book.d) % 3 ≠ 0 := by
  rw [← negative_anchor_identity (actualTrace k n).book n
    (actualTrace k n).x (actualTrace_identity k n)]
  exact negativeNumerator_unit (actualTrace k n).book n
    (actualTrace_good k n) ho he

#print axioms good_trace
#print axioms negativeNumerator_trace_unit
#print axioms affineNumerator_unit
#print axioms calibrated_anchor_reset
#print axioms reflection_pair01
#print axioms reflection_pair10
#print axioms block011_reset
#print axioms block100_reset
#print axioms reflection_block011_reset
#print axioms reflection_block100_reset
#print axioms actualTrace_identity
#print axioms actual_negative_anchor_unit

end Collatz.SourceAwareTails
