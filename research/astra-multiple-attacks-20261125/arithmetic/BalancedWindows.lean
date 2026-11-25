import Mathlib.Tactic.Ring

namespace BalancedWindows

def step (x : ℤ) : ℤ :=
  if x % 2 = 0 then x / 2 else (3*x+1) / 2

def run : ℕ → ℤ → ℤ
  | 0, x => x
  | n+1, x => run n (step x)

def bits : ℕ → ℤ → List Bool
  | 0, _ => []
  | n+1, x => decide (x % 2 ≠ 0) :: bits n (step x)

def ones : List Bool → ℕ
  | [] => 0
  | b :: w => (if b then 1 else 0) + ones w

def carry : List Bool → ℤ
  | [] => 0
  | b :: w => (if b then 3^(ones w) else 0) + 2 * carry w

/-- A physical word supplies the two ordinary endpoints, with the
    parity update imposed independently at each shortcut step. -/
inductive Trace : List Bool → ℤ → ℤ → Prop
  | nil (x) : Trace [] x x
  | cons {b w x y z} (h : 2*y = if b then 3*x+1 else x)
      (t : Trace w y z) : Trace (b :: w) x z

theorem physical_trace (n : ℕ) (x : ℤ) : Trace (bits n x) x (run n x) := by
  induction n generalizing x with
  | zero => exact .nil x
  | succ n ih =>
    apply Trace.cons _ (ih (step x))
    by_cases h : x % 2 = 0 <;> simp [step, h] <;> omega

theorem trace_identity {w x z} (t : Trace w x z) :
    2^w.length * z = 3^(ones w) * x + carry w := by
  induction t with
  | nil => simp [ones, carry]
  | @cons b w x y z h t ih =>
    rw [List.length_cons, pow_succ]
    calc
      2^w.length * 2 * z = 2 * (2^w.length * z) := by ring
      _ = 2 * (3^(ones w) * y + carry w) := by rw [ih]
      _ = 3^(ones w) * (2*y) + 2 * carry w := by ring
      _ = _ := by
        rw [h]
        cases b <;> simp [carry, ones, pow_add]
        ring

/-- Arithmetic consequence of landing on a fixed rational line in the
    one-window Subspace Theorem argument. -/
theorem line_divisibility {w x z} (t : Trace w x z) (a b : ℤ)
    (line : b * carry w = a * 3^(ones w) * x) :
    (2 : ℤ)^w.length ∣ (a+b)*x := by
  have h : (2 : ℤ)^w.length ∣ 3^(ones w) * ((a+b)*x) := by
    refine ⟨b*z, ?_⟩
    calc
      _ = b*(3^(ones w)*x)+ a*3^(ones w)*x := by ring
      _ = b*(3^(ones w)*x+carry w) := by rw [← line]; ring
      _ = _ := by rw [← trace_identity t]; ring
  have dn := Int.natAbs_dvd_natAbs.mpr h
  simp only [Int.natAbs_pow, Int.natAbs_mul] at dn ⊢
  apply Int.natAbs_dvd_natAbs.mp
  simp only [Int.natAbs_pow, Int.natAbs_mul]
  exact (Nat.Coprime.pow w.length (ones w) (by decide : Nat.Coprime 2 3)).dvd_of_dvd_mul_left dn

/-- No grade equality is required for the full two-window discrepancy.
    The expression is the difference of the two normalized carries plus
    the initial displacement, cleared by both powers of three. -/
theorem all_word_divisibility {w v x y X Y} (l : Trace w x X)
    (r : Trace v y Y) (hlen : v.length = w.length) :
    (2 : ℤ)^w.length ∣
      3^(ones w)*3^(ones v)*(y-x) +
      3^(ones w)*carry v - 3^(ones v)*carry w := by
  have hl := trace_identity l
  have hr := trace_identity r
  rw [hlen] at hr
  refine ⟨3^(ones w)*Y - 3^(ones v)*X, ?_⟩
  calc
    _ = 3^(ones w)*(3^(ones v)*y+carry v) -
          3^(ones v)*(3^(ones w)*x+carry w) := by ring
    _ = _ := by rw [← hr, ← hl]; ring

structure Chunk where
  left : List Bool
  right : List Bool
  equalLength : right.length = left.length
  equalWeight : ones right = ones left

def ticks : List Chunk → ℕ
  | [] => 0
  | c :: cs => c.left.length + ticks cs

def grade : List Chunk → ℕ
  | [] => 0
  | c :: cs => ones c.left + grade cs

/-- Clears the denominators of the sparse sum. Identical chunks
    contribute zero at their own position. -/
def error : List Chunk → ℤ
  | [] => 0
  | c :: cs =>
    3^(grade cs)*(carry c.right-carry c.left) + 2^c.left.length * error cs

inductive Paired : List Chunk → ℤ → ℤ → ℤ → ℤ → Prop
  | nil (x y) : Paired [] x y x y
  | cons {c cs x y u v X Y}
      (l : Trace c.left x u) (r : Trace c.right y v)
      (t : Paired cs u v X Y) : Paired (c :: cs) x y X Y

/-- Two actual graded words have one cleared finite-place discrepancy. -/
theorem paired_identity {cs x y X Y} (t : Paired cs x y X Y) :
    2^(ticks cs)*(Y-X) = 3^(grade cs)*(y-x) + error cs := by
  induction t with
  | nil => simp [ticks, grade, error]
  | @cons c cs x y u v X Y l r t ih =>
    have hr := trace_identity r
    rw [c.equalLength, c.equalWeight] at hr
    have hd : 2^c.left.length*(v-u) =
        3^(ones c.left)*(y-x)+(carry c.right-carry c.left) := by
      rw [mul_sub, hr, trace_identity l]; ring
    simp only [ticks, grade, error, pow_add]
    calc
      _ = 2^c.left.length*(2^(ticks cs)*(Y-X)) := by ring
      _ = 3^(grade cs)*(2^c.left.length*(v-u)) + 2^c.left.length*error cs := by
        rw [ih]; ring
      _ = _ := by rw [hd]; ring

theorem dyadic_divisibility {cs x y X Y} (t : Paired cs x y X Y) :
    (2 : ℤ)^(ticks cs) ∣ 3^(grade cs)*(y-x) + error cs :=
  ⟨Y-X, (paired_identity t).symm⟩

#print axioms physical_trace
#print axioms line_divisibility
#print axioms trace_identity
#print axioms all_word_divisibility
#print axioms paired_identity
#print axioms dyadic_divisibility

end BalancedWindows
