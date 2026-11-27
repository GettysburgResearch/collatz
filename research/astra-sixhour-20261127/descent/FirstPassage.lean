import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum
import Mathlib.Data.Rat.Lemmas

/-! Coefficient first passage on actual positive shortcut trajectories.
The formal statements apply to every input, including zero. -/
namespace Collatz.FirstPassage

def step (n : ℕ) : ℕ := if n % 2 = 0 then n / 2 else (3*n + 1) / 2

def run (n : ℕ) : ℕ → ℕ
  | 0 => n
  | h+1 => run (step n) h

def factor (n : ℕ) : ℚ := if n % 2 = 0 then 1/2 else 3/2

def mult (n : ℕ) : ℕ → ℚ
  | 0 => 1
  | h+1 => factor n * mult (step n) h

def odds (n : ℕ) : ℕ → ℕ
  | 0 => 0
  | h+1 => n % 2 + odds (step n) h

def Low (n h : ℕ) : Prop := ∀ j ≤ h, mult n h ≤ mult n j

private theorem factor_pos (n : ℕ) : 0 < factor n := by
  unfold factor
  split <;> norm_num

private theorem mult_pos (n h : ℕ) : 0 < mult n h := by
  induction h generalizing n with
  | zero => norm_num [mult]
  | succ h ih => exact mul_pos (factor_pos n) (ih (step n))

private theorem one_clock (n : ℕ) :
    factor n * (n : ℚ) ≤ step n ∧ (step n : ℚ) ≤ factor n * n + 1/2 := by
  by_cases he : n % 2 = 0
  · have h : 2 * (n/2) = n := by omega
    have hq : (2 : ℚ) * ((n/2 : ℕ) : ℚ) = n := by exact_mod_cast h
    simp only [factor,step,he,ite_true]
    constructor <;> linarith
  · have h : 2 * ((3*n+1)/2) = 3*n+1 := by omega
    have hq : (2 : ℚ) * (((3*n+1)/2 : ℕ) : ℚ) = 3*n+1 := by exact_mod_cast h
    simp only [factor,step,he,ite_false]
    constructor <;> linarith

/-- Exact grade and clock determine the physical leading coefficient. -/
theorem mult_eq_grade (n h : ℕ) : mult n h = (3:ℚ)^(odds n h) / 2^h := by
  induction h generalizing n with
  | zero => norm_num [mult,odds]
  | succ h ih =>
    rw [mult,odds,ih,pow_add,pow_succ]
    have parity : n%2=0 ∨ n%2=1 := by omega
    rcases parity with hp|hp <;> simp [factor,hp] <;> ring

/-- On a coefficient minimum the affine correction is at most h/2,
irrespective of the size of the source or of its earlier peaks. -/
theorem endpoint_enclosure (n h : ℕ) (record : Low n h) :
    mult n h * n ≤ run n h ∧
    (run n h : ℚ) ≤ mult n h * n + (h:ℚ)/2 := by
  induction h generalizing n with
  | zero => simp [run,mult]
  | succ h ih =>
    have tail : Low (step n) h := by
      intro j hj
      have hz := record (j+1) (Nat.succ_le_succ hj)
      exact (mul_le_mul_iff_right₀ (factor_pos n)).mp hz
    have tm := tail 0 (Nat.zero_le h)
    change mult (step n) h ≤ 1 at tm
    obtain ⟨a,b⟩ := ih (step n) tail
    obtain ⟨s,t⟩ := one_clock n
    have pos := (mult_pos (step n) h).le
    change factor n * mult (step n) h * n ≤ run (step n) h ∧
      (run (step n) h : ℚ) ≤ factor n * mult (step n) h * n + ((h+1:ℕ):ℚ)/2
    push_cast
    have s' := mul_le_mul_of_nonneg_left s pos
    have t' := mul_le_mul_of_nonneg_left t pos
    constructor <;> nlinarith

/-- Equal-clock, equal-grade partners at coefficient minima must be
near one another, even if their starting interval is translated. -/
theorem partner_distance {x y h : ℕ} (hx : Low x h) (hy : Low y h)
    (meeting : run x h = run y h) (grade : odds x h = odds y h) :
    mult x h * |(x:ℚ)-y| ≤ (h:ℚ)/2 := by
  have equal : mult y h = mult x h := by simp only [mult_eq_grade,grade]
  obtain ⟨a,b⟩ := endpoint_enclosure x h hx
  obtain ⟨c,d⟩ := endpoint_enclosure y h hy
  rw [equal] at c d
  rw [meeting] at a b
  by_cases hxy : (y:ℚ) ≤ x
  · rw [abs_of_nonneg (sub_nonneg.mpr hxy)]
    linarith
  · rw [abs_of_nonpos (sub_nonpos.mpr (le_of_not_ge hxy))]
    linarith

/-- The pair of ordinary endpoint integers lies in a thin strip about
the line determined by its two physical leading coefficients. -/
theorem paired_strip {n a h k : ℕ} (hx : Low n h) (hy : Low (a*n) k) :
    |mult n h * run (a*n) k - (a:ℚ)*mult (a*n) k * run n h| ≤
      (mult n h*k + (a:ℚ)*mult (a*n) k*h)/2 := by
  obtain ⟨lx,ux⟩ := endpoint_enclosure n h hx
  obtain ⟨ly,uy⟩ := endpoint_enclosure (a*n) k hy
  push_cast at ly uy
  have px := (mult_pos n h).le
  have py := mul_nonneg (Nat.cast_nonneg (α := ℚ) a) (mult_pos (a*n) k).le
  have a₁ := mul_le_mul_of_nonneg_left lx py
  have a₂ := mul_le_mul_of_nonneg_left ux py
  have b₁ := mul_le_mul_of_nonneg_left ly px
  have b₂ := mul_le_mul_of_nonneg_left uy px
  have hx0 := mul_nonneg px (Nat.cast_nonneg (α := ℚ) k)
  have hy0 := mul_nonneg py (Nat.cast_nonneg (α := ℚ) h)
  rw [abs_le]
  constructor <;> nlinarith

#print axioms mult_eq_grade
#print axioms endpoint_enclosure
#print axioms partner_distance
#print axioms paired_strip

end Collatz.FirstPassage
