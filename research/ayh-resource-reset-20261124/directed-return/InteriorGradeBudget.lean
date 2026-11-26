import Mathlib

/-! Finite width and packing identities for a native four-trit pair. -/

namespace Collatz.InteriorGradeBudget

/-- At positive signed width, the two complementary parity lifts preserve
twice the current width, including a child that first ties at zero. -/
theorem two_lift_width (w : ℕ) (hw : 0 < w) (lo hi : Bool) :
    (w + hi.toNat - lo.toNat) +
      (w + (!hi).toNat - (!lo).toNat) = 2 * w := by
  cases lo <;> cases hi <;> simp <;> omega

/-- The sum over all length-n continuations pays each stopping hist with
its full number of lifts. New bits are prepended to the stored history. -/
def stoppedSum (value : List Bool → ℕ) (stop : List Bool → Bool)
    (hist : List Bool) : ℕ → ℕ
  | 0 => value hist
  | n + 1 =>
    if stop hist then 2 ^ (n+1) * value hist
    else stoppedSum value stop (false :: hist) n +
         stoppedSum value stop (true :: hist) n

theorem stoppedSum_fair (value : List Bool → ℕ) (stop : List Bool → Bool)
    (hsplit : ∀ p, value (false :: p) + value (true :: p) = 2 * value p)
    (n : ℕ) (hist : List Bool) :
    stoppedSum value stop hist n = 2 ^ n * value hist := by
  induction n generalizing hist with
  | zero => simp [stoppedSum]
  | succ n ih =>
    simp only [stoppedSum]
    split
    · rfl
    · rw [ih, ih, ← Nat.mul_add, hsplit, pow_succ]
      ring

/-- Strictly increasing exponents in a single residue modulo four are
at least four grades apart. -/
theorem residue_spacing (a b : ℤ) (hab : a < b) (hmod : a % 4 = b % 4) :
    a + 4 ≤ b := by omega

/-- Ordered, strictly interior four-grade intervals leave at least one
unit of unallocated width even when the offspring list is empty. -/
theorem strict_pack (L U : ℤ) (hLU : L < U) (a : ℕ → ℤ) (n : ℕ)
    (hlo : 0 < n → L < a 0)
    (hhi : ∀ i < n, a i + 4 < U)
    (hsep : ∀ i, i+1 < n → a i + 4 ≤ a (i+1)) :
    4 * (n : ℤ) + 1 ≤ U - L := by
  cases n with
  | zero => simp; omega
  | succ k =>
    have lower (i : ℕ) (hi : i ≤ k) : a 0 + 4 * (i : ℤ) ≤ a i := by
      induction i with
      | zero => simp
      | succ i ih =>
        have h1 := ih (by omega)
        have h2 := hsep i (by omega)
        push_cast
        omega
    have h1 := lower k (by omega)
    have h2 := hlo (by omega)
    have h3 := hhi k (by omega)
    push_cast
    omega

/-- A contiguous run of spatial blocks shares its intermediate rays. -/
theorem released_telescope (g : ℕ → ℤ) (i n : ℕ) :
    ∑ j ∈ Finset.range n, (g (i+j+1) - g (i+j)) = g (i+n) - g i := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [Finset.sum_range_succ, ih]
    have he : i + (n+1) = i+n+1 := by omega
    rw [he]
    ring

/-- Trimming both sides by a full lookahead plus one covers all
lookahead increments on the outside rays and on the old pair. -/
theorem released_budget (L U A B L' U' A' B' H : ℤ)
    (ha : L+H+1 ≤ A) (hb : B ≤ U-H-1)
    (hnew : B' - A' ≤ B-A+H) (hold : U-L-H ≤ U'-L') :
    B'-A'+2 ≤ U'-L' := by omega

/-- Upward variation equals the endpoint increment plus downward variation. -/
theorem released_variation (g : ℕ → ℤ) (n : ℕ) :
    ∑ j ∈ Finset.range n, max (g (j+1) - g j) 0 =
    g n - g 0 + ∑ j ∈ Finset.range n, max (g j - g (j+1)) 0 := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [Finset.sum_range_succ, Finset.sum_range_succ, ih]
    rcases le_total (g n) (g (n+1)) with h | h
    · rw [max_eq_left (by omega), max_eq_right (by omega)]
      omega
    · rw [max_eq_right (by omega), max_eq_left (by omega)]
      omega

end Collatz.InteriorGradeBudget

#print axioms Collatz.InteriorGradeBudget.two_lift_width
#print axioms Collatz.InteriorGradeBudget.stoppedSum_fair
#print axioms Collatz.InteriorGradeBudget.residue_spacing
#print axioms Collatz.InteriorGradeBudget.strict_pack

#print axioms Collatz.InteriorGradeBudget.released_telescope
#print axioms Collatz.InteriorGradeBudget.released_budget

#print axioms Collatz.InteriorGradeBudget.released_variation
