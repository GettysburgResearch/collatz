module

public import Mathlib.Data.Nat.Basic
public import Mathlib.Tactic.Linarith
public import Mathlib.Tactic.Positivity
public import Mathlib.Tactic.Ring

/-! Affine prefix slopes certify the actual first shortcut descent for all
large enough positive sources, with a word-independent horizon cutoff. -/
@[expose] public section

namespace OrdinaryExcursionFloor

def shortcut (x : ℕ) : ℕ := if x % 2 = 0 then x / 2 else (3*x+1)/2

def orbit (n : ℕ) : ℕ → ℕ
  | 0 => n
  | j+1 => shortcut (orbit n j)

def oddCount (n : ℕ) : ℕ → ℕ
  | 0 => 0
  | j+1 => if orbit n j % 2 = 0 then oddCount n j else oddCount n j + 1

def offset (n : ℕ) : ℕ → ℕ
  | 0 => 0
  | j+1 => if orbit n j % 2 = 0 then offset n j else 3*offset n j + 2^j

theorem double_shortcut (x : ℕ) :
    2*shortcut x = if x % 2 = 0 then x else 3*x+1 := by
  by_cases h : x%2=0
  · simp only [shortcut, h, ↓reduceIte]
    omega
  · simp only [shortcut, h, ↓reduceIte]
    omega

theorem affine_clock (n j : ℕ) :
    2^j * orbit n j = 3^(oddCount n j)*n + offset n j := by
  induction j with
  | zero => simp [orbit, oddCount, offset]
  | succ j ih =>
    rw [pow_succ 2, orbit, Nat.mul_assoc, double_shortcut]
    by_cases h : orbit n j % 2 = 0
    · simpa only [h, ↓reduceIte, oddCount, offset] using ih
    · simp only [h, ↓reduceIte, oddCount, offset, pow_succ]
      calc
        2^j*(3*orbit n j+1) = 3*(2^j*orbit n j)+2^j := by ring
        _ = _ := by rw [ih]; ring

theorem offset_bound (n j : ℕ) : offset n j + 2^j ≤ 3^j := by
  induction j with
  | zero => simp [offset]
  | succ j ih =>
    simp only [offset, pow_succ 2, pow_succ 3]
    split <;> omega

theorem rises_of_prefix_slope {n i : ℕ} (hn : 0<n)
    (h : 2^i < 3^(oddCount n i)) : n < orbit n i := by
  have hs := Nat.mul_lt_mul_of_pos_right h hn
  have ha := affine_clock n i
  exact Nat.lt_of_mul_lt_mul_left (show 2^i*n<2^i*orbit n i by omega)

theorem descends_of_terminal_slope {n k : ℕ}
    (h : 3^(oddCount n k) < 2^k) (hsize : offset n k < n) : orbit n k < n := by
  have hs := Nat.mul_le_mul_right n (Nat.succ_le_of_lt h)
  have ha := affine_clock n k
  rw [Nat.succ_mul] at hs
  exact Nat.lt_of_mul_lt_mul_left (show 2^k*orbit n k<2^k*n by omega)

/-- A single explicit cutoff works for every parity word of length k.
The two slope tests involve only the actual finite parity prefix. -/
theorem first_strict_descent {n k : ℕ}
    (hsize : 3^k < n+2^k)
    (hproper : ∀ i, 0<i → i<k → 2^i < 3^(oddCount n i))
    (hfinal : 3^(oddCount n k) < 2^k) :
    (∀ i, 0<i → i<k → n < orbit n i) ∧ orbit n k < n := by
  have hb := offset_bound n k
  have hsmall : offset n k < n := by omega
  refine ⟨fun i hi hik ↦ rises_of_prefix_slope (by omega) (hproper i hi hik),
    descends_of_terminal_slope hfinal hsmall⟩

end OrdinaryExcursionFloor

#print axioms OrdinaryExcursionFloor.double_shortcut
#print axioms OrdinaryExcursionFloor.affine_clock
#print axioms OrdinaryExcursionFloor.offset_bound
#print axioms OrdinaryExcursionFloor.rises_of_prefix_slope
#print axioms OrdinaryExcursionFloor.descends_of_terminal_slope
#print axioms OrdinaryExcursionFloor.first_strict_descent
