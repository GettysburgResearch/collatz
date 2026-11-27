import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Algebra.GCDMonoid.Basic
import Mathlib.RingTheory.Coprime.Lemmas
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
For the shortcut branches, the centered integer numerator `2*n+q`
over a common denominator `q` has the same additive term on both
branches. A positive carry comparison controls the relative size of
closed cyclic phases with mismatching parity scripts.
-/

namespace Collatz.ShiftCenter

set_option autoImplicit false

def bit : Bool → ℕ
  | false => 0
  | true => 1

def grade : List Bool → ℕ
  | [] => 0
  | b :: bs => bit b + grade bs

def carry : List Bool → ℕ
  | [] => 0
  | _ :: bs => 3 ^ grade bs + 2 * carry bs

def raises : List (Bool × Bool) → ℕ
  | [] => 0
  | (a, b) :: bs => (if !a && b then 1 else 0) + raises bs

private theorem grade_le (w : List (Bool × Bool)) :
    grade (w.map Prod.snd) ≤ grade (w.map Prod.fst) + raises w := by
  induction w with
  | nil => simp [grade, raises]
  | cons p w ih =>
    obtain ⟨a, b⟩ := p
    cases a <;> cases b <;> simp [grade, bit, raises] at * <;> omega

/-- A directed mismatch controls every positive term of the second carry. -/
theorem carry_le (w : List (Bool × Bool)) :
    carry (w.map Prod.snd) ≤ 3 ^ raises w * carry (w.map Prod.fst) := by
  induction w with
  | nil => simp [carry]
  | cons p w ih =>
    obtain ⟨a, b⟩ := p
    have hg : 3 ^ grade (w.map Prod.snd) ≤
        3 ^ raises w * 3 ^ grade (w.map Prod.fst) := by
      rw [← pow_add]
      exact Nat.pow_le_pow_right (by decide) (by simpa [Nat.add_comm] using grade_le w)
    have bound : 3 ^ grade (w.map Prod.snd) + 2 * carry (w.map Prod.snd) ≤
        3 ^ raises w * (3 ^ grade (w.map Prod.fst) + 2 * carry (w.map Prod.fst)) := by
      nlinarith
    simp only [List.map_cons, carry]
    refine bound.trans (Nat.mul_le_mul_right _ ?_)
    apply Nat.pow_le_pow_right (by decide)
    simp [raises]

/-- A physical shortcut run in the centered numerator coordinate. -/
inductive Run (q : ℕ) : List Bool → ℕ → ℕ → Prop where
  | nil (x : ℕ) : Run q [] x x
  | cons {b : Bool} {w : List Bool} {x y z : ℕ}
      (edge : 2 * y = 3 ^ bit b * x + q)
      (tail : Run q w y z) : Run q (b :: w) x z

theorem unroll {q x y : ℕ} {w : List Bool} (run : Run q w x y) :
    2 ^ w.length * y = 3 ^ grade w * x + q * carry w := by
  induction run with
  | nil x => simp [grade, carry]
  | @cons b w x y z edge tail ih =>
    simp only [List.length_cons, grade, carry, pow_add, pow_succ]
    calc
      2 ^ w.length * 2 * z = 2 * (2 ^ w.length * z) := by ring
      _ = 2 * (3 ^ grade w * y + q * carry w) := by rw [ih]
      _ = 3 ^ grade w * (2 * y) + 2 * q * carry w := by ring
      _ = 3 ^ bit b * 3 ^ grade w * x + q * (3 ^ grade w + 2 * carry w) := by
        rw [edge]
        ring

/-- The estimate is for the actual closed coordinates and needs no order
or coprimality hypothesis on the shift. The two scripts may have unequal grades. -/
theorem closed_comparison {q x y : ℕ} (w : List (Bool × Bool))
    (first : Run q (w.map Prod.fst) x x)
    (second : Run q (w.map Prod.snd) y y)
    (grades : grade (w.map Prod.snd) ≤ grade (w.map Prod.fst))
    (positive : 3 ^ grade (w.map Prod.fst) < 2 ^ w.length) :
    y ≤ 3 ^ raises w * x := by
  have hx := unroll first
  have hy := unroll second
  simp only [List.length_map] at hx hy
  let D := 2 ^ w.length - 3 ^ grade (w.map Prod.fst)
  have hx' : D * x = q * carry (w.map Prod.fst) := by
    dsimp [D]
    rw [Nat.sub_mul]
    omega
  have hy' : D * y ≤ q * carry (w.map Prod.snd) := by
    have comp := Nat.mul_le_mul_right y (Nat.pow_le_pow_right (by decide : 0 < 3) grades)
    dsimp [D]
    rw [Nat.sub_mul]
    omega
  have hD : 0 < D := Nat.sub_pos_of_lt positive
  apply Nat.le_of_mul_le_mul_left _ hD
  calc
    D * y ≤ q * carry (w.map Prod.snd) := hy'
    _ ≤ q * (3 ^ raises w * carry (w.map Prod.fst)) := Nat.mul_le_mul_left _ (carry_le w)
    _ = 3 ^ raises w * (D * x) := by rw [hx']; ring
    _ = D * (3 ^ raises w * x) := by ring

/-- Every common forward word forces its full two-power into the initial
centered numerator difference. Both endpoints remain in the same integer lattice. -/
theorem common_run_divides {q x y x' y' : ℕ} {w : List Bool}
    (first : Run q w x x') (second : Run q w y y') :
    (2 : ℤ) ^ w.length ∣ (x : ℤ) - y := by
  have h₁ : (2 : ℤ) ^ w.length * x' = 3 ^ grade w * x + q * (carry w : ℤ) := by
    exact_mod_cast unroll first
  have h₂ : (2 : ℤ) ^ w.length * y' = 3 ^ grade w * y + q * (carry w : ℤ) := by
    exact_mod_cast unroll second
  have cop : IsCoprime ((2 : ℤ) ^ w.length) (3 ^ grade w) := by
    exact (show IsCoprime (2 : ℤ) 3 from ⟨-1, 1, by norm_num⟩).pow
  apply cop.dvd_of_dvd_mul_left
  exact ⟨(x' : ℤ) - y', by linear_combination h₂ - h₁⟩

/-- Physical growth with a common positive denominator, including contracting runs. -/
theorem growth {q x y : ℕ} {w : List Bool} (run : Run q w x y) :
    2 ^ w.length * (y + q) ≤ 3 ^ w.length * (x + q) := by
  induction run with
  | nil x => simp
  | @cons b w x y z edge tail ih =>
    have step : 2 * (y + q) ≤ 3 * (x + q) := by
      cases b <;> simp [bit] at edge <;> omega
    simp only [List.length_cons, pow_succ]
    calc
      2 ^ w.length * 2 * (z + q) = 2 * (2 ^ w.length * (z + q)) := by ring
      _ ≤ 2 * (3 ^ w.length * (y + q)) := Nat.mul_le_mul_left 2 ih
      _ = 3 ^ w.length * (2 * (y + q)) := by ring
      _ ≤ 3 ^ w.length * (3 * (x + q)) := Nat.mul_le_mul_left _ step
      _ = 3 ^ w.length * 3 * (x + q) := by ring

private theorem length_le_max {q x y x' y' : ℕ} {w : List Bool}
    (first : Run q w x x') (second : Run q w y y') (distinct : x ≠ y) :
    2 ^ w.length ≤ max x y := by
  rcases lt_or_gt_of_ne distinct with h | h
  · have hd := common_run_divides second first
    have pos : 0 < (y : ℤ) - x := by omega
    have hb := Int.le_of_dvd pos hd
    rw [max_eq_right h.le]
    exact_mod_cast (show (2 : ℤ) ^ w.length ≤ y by omega)
  · have hd := common_run_divides first second
    have pos : 0 < (x : ℤ) - y := by omega
    have hb := Int.le_of_dvd pos hd
    rw [max_eq_left h.le]
    exact_mod_cast (show (2 : ℤ) ^ w.length ≤ x by omega)

/-- Integer form of the paired clock inequality. Different prefix scripts are
allowed. From an initial bound of 2^K the next common word has length at most
K+(17/29)t, with 3^29 < 2^46 certified in the kernel. -/
theorem paired_clock {q a b x y x' y' K : ℕ} {u v w : List Bool}
    (firstPrefix : Run q u a x) (secondPrefix : Run q v b y)
    (time : v.length = u.length)
    (firstCommon : Run q w x x') (secondCommon : Run q w y y')
    (distinct : x ≠ y) (initial : max (a + q) (b + q) ≤ 2 ^ K) :
    29 * (u.length + w.length) ≤ 46 * u.length + 29 * K := by
  have ab := (max_le_iff.mp initial)
  have ax := (growth firstPrefix).trans (Nat.mul_le_mul_left _ ab.1)
  have by' := (growth secondPrefix).trans (Nat.mul_le_mul_left _ ab.2)
  rw [time] at by'
  have hx : 2 ^ u.length * x ≤ 3 ^ u.length * 2 ^ K :=
    (Nat.mul_le_mul_left _ (Nat.le_add_right x q)).trans ax
  have hy : 2 ^ u.length * y ≤ 3 ^ u.length * 2 ^ K :=
    (Nat.mul_le_mul_left _ (Nat.le_add_right y q)).trans by'
  have h : 2 ^ (u.length + w.length) ≤ 3 ^ u.length * 2 ^ K := by
    rw [pow_add]
    apply (Nat.mul_le_mul_left _ (length_le_max firstCommon secondCommon distinct)).trans
    rw [← Nat.mul_max_mul_left]
    exact max_le hx hy
  have bound : 3 ^ (u.length * 29) ≤ (2 : ℕ) ^ (46 * u.length) := by
    rw [Nat.mul_comm u.length, pow_mul, pow_mul]
    exact Nat.pow_le_pow_left (by norm_num) _
  have powered := Nat.pow_le_pow_left h 29
  rw [mul_pow, ← pow_mul, ← pow_mul, ← pow_mul] at powered
  have final := powered.trans (Nat.mul_le_mul_right (2 ^ (K * 29)) bound)
  rw [← pow_add] at final
  have result := (Nat.pow_le_pow_iff_right (by decide : 1 < 2)).mp final
  omega

#print axioms carry_le
#print axioms unroll
#print axioms closed_comparison
#print axioms common_run_divides
#print axioms growth
#print axioms paired_clock

end Collatz.ShiftCenter
