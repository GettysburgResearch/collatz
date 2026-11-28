import AffineOrbit
import Mathlib.Logic.Function.Iterate

/-! Exact arithmetic, decidable forward closure and actual capture by the least-odd
rounding of a native Collatz output. The seed density is a separate written theorem. -/
set_option autoImplicit false
set_option warningAsError true

namespace Collatz.RoundedOrbitCapture

open Collatz.PoweredAffine

/-- Least odd integer at least the native odd-branch output on an odd source. -/
def rounded (n : ℕ) : ℕ := 2 * ((3 * n + 1) / 4) + 1

/-- All rounded successors are odd and strictly larger.  The two additional
inequalities control the growth of the closed seed set at every later depth. -/
theorem rounded_arithmetic (n : ℕ) :
    rounded n % 2 = 1 ∧ n < rounded n ∧
      3 * n ≤ 2 * rounded n ∧ 2 * rounded n ≤ 3 * n + 3 := by
  unfold rounded
  omega

/-- The actual change on an odd departure is either zero or exactly one. -/
theorem rounded_native_error (n : ℕ) (hn : n % 2 = 1) :
    rounded n = step n ∨ rounded n = step n + 1 := by
  have h := odd_step hn
  unfold rounded
  omega

/-- Distinct odd inputs have distinct successors, even after rounding. -/
theorem rounded_odd_injective {m n : ℕ} (hm : m % 2 = 1) (hn : n % 2 = 1)
    (heq : rounded m = rounded n) : m = n := by
  unfold rounded at heq
  omega

private theorem iterate_lower (y t : ℕ) : y + t ≤ rounded^[t] y := by
  induction t with
  | zero => simp
  | succ t ih =>
    rw [Function.iterate_succ_apply']
    have h := (rounded_arithmetic (rounded^[t] y)).2.1
    omega

/-- Unfolded growth bounds used in counting the whole forward closure. -/
theorem rounded_iterate_bounds (y t : ℕ) :
    3 ^ t * y ≤ 2 ^ t * rounded^[t] y ∧
      2 ^ t * (rounded^[t] y + 3) ≤ 3 ^ t * (y + 3) := by
  induction t with
  | zero => simp
  | succ t ih =>
    rw [Function.iterate_succ_apply']
    have h := (rounded_arithmetic (rounded^[t] y)).2.2
    constructor
    · calc
        3 ^ (t + 1) * y = 3 * (3 ^ t * y) := by ring
        _ ≤ 3 * (2 ^ t * rounded^[t] y) := Nat.mul_le_mul_left _ ih.1
        _ = 2 ^ t * (3 * rounded^[t] y) := by ring
        _ ≤ 2 ^ t * (2 * rounded (rounded^[t] y)) := Nat.mul_le_mul_left _ h.1
        _ = 2 ^ (t + 1) * rounded (rounded^[t] y) := by ring
    · calc
        2 ^ (t + 1) * (rounded (rounded^[t] y) + 3) =
            2 ^ t * (2 * (rounded (rounded^[t] y) + 3)) := by ring
        _ ≤ 2 ^ t * (3 * (rounded^[t] y + 3)) := Nat.mul_le_mul_left _ (by omega)
        _ = 3 * (2 ^ t * (rounded^[t] y + 3)) := by ring
        _ ≤ 3 * (3 ^ t * (y + 3)) := Nat.mul_le_mul_left _ ih.2
        _ = 3 ^ (t + 1) * (y + 3) := by ring

/-- A decidable bounded search on the two ordinary integers specifying a seed and a date. -/
def InClosure (seed : ℕ → Bool) (n : ℕ) : Prop :=
  ∃ y : Fin (n + 1), seed y = true ∧ ∃ t : Fin (n + 1), rounded^[(t : ℕ)] (y : ℕ) = n

instance (seed : ℕ → Bool) (n : ℕ) : Decidable (InClosure seed n) := by
  unfold InClosure
  infer_instance

/-- This finite search is exactly the unrestricted forward closure. -/
theorem inClosure_iff (seed : ℕ → Bool) (n : ℕ) :
    InClosure seed n ↔ ∃ y t : ℕ, seed y = true ∧ rounded^[t] y = n := by
  constructor
  · rintro ⟨y, hy, t, ht⟩
    exact ⟨y, t, hy, ht⟩
  · rintro ⟨y, t, hy, ht⟩
    have lower := iterate_lower y t
    exact ⟨⟨y, by omega⟩, hy, ⟨t, by omega⟩, ht⟩

private theorem closure_next {seed : ℕ → Bool} {n : ℕ} (hn : InClosure seed n) :
    InClosure seed (rounded n) := by
  obtain ⟨y, t, hy, ht⟩ := (inClosure_iff seed n).mp hn
  exact (inClosure_iff _ _).mpr ⟨y, t + 1, hy, by rw [Function.iterate_succ_apply', ht]⟩

private theorem closure_odd {seed : ℕ → Bool} {n : ℕ}
    (oddSeed : ∀ y, seed y = true → y % 2 = 1) (hn : InClosure seed n) : n % 2 = 1 := by
  obtain ⟨y, t, hy, rfl⟩ := (inClosure_iff seed n).mp hn
  cases t with
  | zero => exact oddSeed y hy
  | succ t => rw [Function.iterate_succ_apply']; exact (rounded_arithmetic _).1

def modified (seed : ℕ → Bool) (n : ℕ) : ℕ :=
  if InClosure seed n then rounded n else step n

/-- For any decidable odd seeds above a barrier, the actual constructed map
preserves all even edges and all edges through the barrier; its error is at most one. -/
theorem modified_native_rule (seed : ℕ → Bool) (barrier n : ℕ)
    (hseed : ∀ y, seed y = true → y % 2 = 1 ∧ barrier < y) :
    ((n % 2 = 0 ∨ n ≤ barrier) → modified seed n = step n) ∧
      (modified seed n = step n ∨ modified seed n = step n + 1) := by
  by_cases hn : InClosure seed n
  · have hodd := closure_odd (fun y hy => (hseed y hy).1) hn
    obtain ⟨y, t, hy, ht⟩ := (inClosure_iff _ _).mp hn
    have hlower := iterate_lower y t
    have hyb := (hseed y hy).2
    rw [modified, ite_eq_left hn]
    exact ⟨by omega, rounded_native_error n hodd⟩
  · simp [modified, hn]

/-- On the whole computed closure the modified orbit equals the rounded orbit
at every date, remains in the closure, and grows at least one per step. -/
theorem closure_orbit {seed : ℕ → Bool} {n : ℕ} (hn : InClosure seed n) (t : ℕ) :
    (modified seed)^[t] n = rounded^[t] n ∧
      InClosure seed ((modified seed)^[t] n) ∧ n + t ≤ (modified seed)^[t] n := by
  have actual (k : ℕ) : (modified seed)^[k] n = rounded^[k] n ∧
      InClosure seed ((modified seed)^[k] n) := by
    induction k with
    | zero => exact ⟨rfl, hn⟩
    | succ k ih =>
      rw [Function.iterate_succ_apply', Function.iterate_succ_apply', modified, ite_eq_left ih.2]
      exact ⟨congrArg rounded ih.1, closure_next ih.2⟩
  obtain ⟨heq, hcl⟩ := actual t
  exact ⟨heq, hcl, heq ▸ iterate_lower n t⟩

private theorem native_iterate (n t : ℕ) : orbit n t = step^[t] n := by
  induction t generalizing n with
  | zero => rfl
  | succ t ih => exact ih (step n)

/-- A genuine hit suffices for unbounded growth of the actual modified trajectory,
including paths that entered the rounded closure at an earlier date. -/
theorem true_hit_forces_escape {seed : ℕ → Bool} {n date : ℕ}
    (hit : InClosure seed (orbit n date)) :
    ∀ k, (modified seed)^[date] n + k ≤ (modified seed)^[date + k] n := by
  have alternative (t : ℕ) : InClosure seed ((modified seed)^[t] n) ∨
      (modified seed)^[t] n = step^[t] n := by
    induction t with
    | zero => exact Or.inr rfl
    | succ t ih =>
      rw [Function.iterate_succ_apply', Function.iterate_succ_apply']
      by_cases h : InClosure seed ((modified seed)^[t] n)
      · exact Or.inl (by simpa [modified, h] using closure_next h)
      · exact Or.inr (by rw [modified, ite_eq_right h, ih.resolve_left h])
  have captured : InClosure seed ((modified seed)^[date] n) :=
    (alternative date).elim id (fun heq => by rw [heq, ← native_iterate]; exact hit)
  intro k
  rw [Nat.add_comm date k, Function.iterate_add_apply]
  exact (closure_orbit captured k).2.2

end Collatz.RoundedOrbitCapture
