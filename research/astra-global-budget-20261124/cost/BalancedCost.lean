import Mathlib.Data.Nat.ModEq
import Mathlib.Data.Nat.GCD.Basic
import Mathlib.Data.Fintype.Pigeonhole
import Mathlib.Tactic

namespace Collatz.BalancedCost

def step (x : ℕ) : ℕ :=
  if x % 2 = 0 then x / 2 else (3 * x + 1) / 2

def word : ℕ → ℕ → List ℕ
  | 0, _ => []
  | h+1, x => (x % 2) :: word h (step x)

theorem sameWord {h x y : ℕ} (hw : word h x = word h y) :
    x ≡ y [MOD 2^h] := by
  induction h generalizing x y with
  | zero => exact Nat.modEq_one
  | succ h ih =>
    obtain ⟨hb, ht⟩ := List.cons.inj hw
    have he := (ih ht).mul_left' 2
    have hm : 2 * 2^h = 2^(h+1) := by rw [pow_succ]; omega
    rw [hm] at he
    by_cases hx : x % 2 = 0
    · have hy : y % 2 = 0 := hb ▸ hx
      have xeq : 2 * step x = x := by simp [step, hx]; omega
      have yeq : 2 * step y = y := by simp [step, hy]; omega
      rwa [xeq, yeq] at he
    · have hy : y % 2 ≠ 0 := by rwa [← hb]
      have xeq : 2 * step x = 3*x + 1 := by simp [step, hx]; omega
      have yeq : 2 * step y = 3*y + 1 := by simp [step, hy]; omega
      rw [xeq, yeq] at he
      have hc : Nat.Coprime (2^(h+1)) 3 := (show Nat.Coprime 2 3 by decide).pow_left _
      exact Nat.ModEq.cancel_left_of_coprime hc (he.add_right_cancel' 1)

def orbit : ℕ → ℕ → ℕ
  | 0, x => x
  | t+1, x => step (orbit t x)

theorem growth (t x : ℕ) : 2^t * (orbit t x + 1) ≤ 3^t * (x+1) := by
  induction t with
  | zero => simp [orbit]
  | succ t ih =>
    have hs (z : ℕ) : 2 * (step z + 1) ≤ 3 * (z + 1) := by
      unfold step
      split <;> omega
    simp only [orbit, pow_succ]
    calc
      2^t * 2 * (step (orbit t x) + 1) = 2^t * (2 * (step (orbit t x) + 1)) := by ring
      _ ≤ 2^t * (3 * (orbit t x + 1)) := Nat.mul_le_mul_left _ (hs _)
      _ = 3 * (2^t * (orbit t x + 1)) := by ring
      _ ≤ 3 * (3^t * (x+1)) := Nat.mul_le_mul_left _ ih
      _ = _ := by ring

/-- Any dictionary with D names for the actual h-step windows starting at the
first D+1 clocks forces an ordinary collision under the displayed height bound. -/
theorem dictionaryCollision {x h D : ℕ} (name : Fin (D+1) → Fin D)
    (names : ∀ i j, name i = name j →
      word h (orbit i.val x) = word h (orbit j.val x))
    (budget : (x+1)*3^D ≤ 2^h*2^D) :
    ∃ i j : Fin (D+1), i ≠ j ∧ orbit i.val x = orbit j.val x := by
  obtain ⟨i, j, hn, he⟩ := Fintype.exists_ne_map_eq_of_card_lt name (by simp)
  have small (a : Fin (D+1)) : orbit a.val x < 2^h := by
    have ha : a.val ≤ D := by omega
    have hmul := Nat.mul_le_mul_right (3^(D-a.val)) (growth a.val x)
    have hpow : 3^a.val * 3^(D-a.val) = 3^D := by
      rw [← pow_add, Nat.add_sub_of_le ha]
    have hpow' : 2^a.val * 2^(D-a.val) = 2^D := by
      rw [← pow_add, Nat.add_sub_of_le ha]
    have h2 : 2^(D-a.val) ≤ 3^(D-a.val) := Nat.pow_le_pow_left (by decide) _
    have final : (orbit a.val x+1)*2^D ≤ 2^h*2^D := calc
      _ = (2^a.val*(orbit a.val x+1))*2^(D-a.val) := by rw [← hpow']; ring
      _ ≤ (2^a.val*(orbit a.val x+1))*3^(D-a.val) := Nat.mul_le_mul_left _ h2
      _ ≤ (3^a.val*(x+1))*3^(D-a.val) := hmul
      _ = (x+1)*3^D := by rw [← hpow]; ring
      _ ≤ _ := budget
    have := Nat.le_of_mul_le_mul_right final (by positivity)
    omega
  exact ⟨i, j, hn, (sameWord (names i j he)).eq_of_lt_of_lt (small _) (small _)⟩

/-- Every five steps grow by less than a factor eight, setting the concrete
threshold for dictionaries with h+1 entries. -/
theorem balancedBudget {x k : ℕ} (hx : x+1 ≤ 2^(2*k-1)) (hk : 0 < k) :
    (x+1)*3^(5*k+1) ≤ 2^(5*k)*2^(5*k+1) := by
  have h0 : 3^(5*k) ≤ 2^(8*k) := by
    rw [pow_mul, pow_mul]
    exact Nat.pow_le_pow_left (by decide) _
  have hh : 2 * (x+1) ≤ 2^(2*k) := calc
    _ ≤ 2 * 2^(2*k-1) := Nat.mul_le_mul_left 2 hx
    _ = _ := by
      rw [mul_comm 2, ← pow_succ, show 2*k-1+1=2*k by omega]
  have hbound : 2*((x+1)*3^(5*k+1)) ≤ 2*(2^(5*k)*2^(5*k+1)) := calc
    _ = (2*(x+1))*3^(5*k)*3 := by rw [pow_succ]; ring
    _ ≤ 2^(2*k)*2^(8*k)*3 := Nat.mul_le_mul_right 3 (Nat.mul_le_mul hh h0)
    _ ≤ 2^(2*k)*2^(8*k)*4 := Nat.mul_le_mul_left _ (by decide)
    _ = _ := by
      rw [← pow_add, show 2*k+8*k=5*k+5*k by omega, pow_add, pow_succ]
      ring
  omega

/-- An affine carry improvement which is divisible by the complete odd
coefficient measures the exact decrease of its ordinary source. -/
theorem carryGain {x y z t p C C' d : ℕ}
    (physical : 2^t*z = 3^p*x+C) (candidate : 2^t*z = 3^p*y+C')
    (gain : C' = C + 3^p*d) (hy : 0 < y) :
    x = y+d ∧ d < x := by
  have h : 3^p*x = 3^p*(y+d) := by
    rw [Nat.mul_add]
    omega
  have hh := Nat.eq_of_mul_eq_mul_left (by positivity : 0 < 3^p) h
  omega

/-- Source-specific time bound for *any* preterminal prefix with at most
A excess odd steps measured by 2p-t. The growth hypothesis follows on
physical paths all of whose odd inputs are at least 3. -/
theorem gradeCutoff {x b p t A : ℕ} (hx : x < 2^b)
    (growthBound : (2:ℚ)^t ≤ x*(10/3:ℚ)^p) (grade : 2*p ≤ t+A) :
    t < 8*(b+A) := by
  have hs : (4:ℚ)^t ≤ (x:ℚ)^2*(10/3:ℚ)^(t+A) := calc
    _ = ((2:ℚ)^t)^2 := by rw [← pow_mul, Nat.mul_comm t 2, pow_mul]; norm_num
    _ ≤ ((x:ℚ)*(10/3:ℚ)^p)^2 := by gcongr
    _ = (x:ℚ)^2*(10/3:ℚ)^(2*p) := by rw [mul_pow, Nat.mul_comm 2 p, pow_mul]
    _ ≤ _ := by gcongr; norm_num
  have hratio : (6/5:ℚ)^t ≤ (x:ℚ)^2*(10/3:ℚ)^A := by
    have hmul : (6/5:ℚ)^t*(10/3:ℚ)^t ≤ ((x:ℚ)^2*(10/3:ℚ)^A)*(10/3:ℚ)^t := by
      rw [← mul_pow, show (6/5:ℚ)*(10/3)=4 by norm_num, pow_add] at *
      linarith
    exact le_of_mul_le_mul_right hmul (by positivity)
  by_contra! late
  have hl : (2:ℚ)^(2*(b+A)) ≤ (6/5:ℚ)^t := calc
    _ ≤ ((6/5:ℚ)^4)^(2*(b+A)) := by gcongr; norm_num
    _ = (6/5:ℚ)^(8*(b+A)) := by rw [← pow_mul]; congr 1; omega
    _ ≤ _ := by gcongr; norm_num
  have upper : (x:ℚ)^2*(10/3:ℚ)^A < (2:ℚ)^(2*(b+A)) := calc
    _ < ((2:ℚ)^b)^2*(10/3:ℚ)^A := by
      have hcast : (x:ℚ) < (2:ℚ)^b := by exact_mod_cast hx
      gcongr
    _ ≤ ((2:ℚ)^b)^2*(4:ℚ)^A := by gcongr; norm_num
    _ = _ := by
      rw [show (4:ℚ)=2^2 by norm_num, ← pow_mul, ← pow_mul, ← pow_add]
      congr 1
      omega
  linarith

#print axioms sameWord
#print axioms growth
#print axioms dictionaryCollision
#print axioms balancedBudget
#print axioms carryGain
#print axioms gradeCutoff

end Collatz.BalancedCost
