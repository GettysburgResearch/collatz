/-
Fourth-Jacobian inverse pressure: exact finite identities and ordinary
counterexamples to finite-period power-weight contraction.

This file proves no Collatz convergence assertion. There are no open
mathematical hypotheses in its theorems. Infinite-series interpretations
and real-degree interpolation are stated separately in the adjacent note.
-/
import Collatz.Closure

open CollatzReverseBasin

namespace CollatzInversePressure

def quadratic (x : Rat) : Rat := (x+1)*(x+2)

def inverseAffine (a : Nat) (x : Rat) : Rat := ((2 : Rat)^a*x-1)/3

def restoredTerm (a : Nat) (x : Rat) : Rat :=
  81*(1/16 : Rat)^a * quadratic (inverseAffine a x)

private theorem geometric_product_two (a : Nat) :
    (1/16 : Rat)^a * (2 : Rat)^a = (1/8 : Rat)^a := by
  induction a with
  | zero => simp
  | succ a ih => simp only [Rat.pow_succ]; grind

private theorem geometric_product_four (a : Nat) :
    (1/16 : Rat)^a * ((2 : Rat)^a)^2 = (1/4 : Rat)^a := by
  induction a with
  | zero => simp only [Rat.pow_zero]; grind
  | succ a ih => simp only [Rat.pow_succ]; grind

theorem restored_term_expansion (a : Nat) (x : Rat) :
    restoredTerm a x =
      9*x^2*(1/4 : Rat)^a + 63*x*(1/8 : Rat)^a + 90*(1/16 : Rat)^a := by
  have h2 := geometric_product_two a
  have h4 := geometric_product_four a
  unfold restoredTerm quadratic inverseAffine
  grind

def partialRestored : Nat → Rat → Rat
  | 0, _ => 0
  | n+1, x => partialRestored n x + restoredTerm (n+1) x

/-- Exact finite sum, with all tail terms retained. -/
theorem partial_restored_identity (n : Nat) (x : Rat) :
    partialRestored n x = 3*quadratic x
      - 3*x^2*(1/4 : Rat)^n - 9*x*(1/8 : Rat)^n - 6*(1/16 : Rat)^n := by
  induction n with
  | zero => simp only [partialRestored, Rat.pow_zero]; unfold quadratic; grind
  | succ n ih =>
    rw [partialRestored, ih, restored_term_expansion]
    simp only [Rat.pow_succ]
    grind

/-- Multiplication by5/27 converts the81/16^a weights to15/16^a. -/
theorem partial_probability_identity (n : Nat) (x : Rat) :
    (5/27 : Rat)*partialRestored n x = (5/9 : Rat)*quadratic x
      - (5/9 : Rat)*x^2*(1/4 : Rat)^n
      - (5/3 : Rat)*x*(1/8 : Rat)^n - (10/9 : Rat)*(1/16 : Rat)^n := by
  rw [partial_restored_identity]
  grind

/-! Ordinary positive paths, not only affine words. -/

inductive OneRun : Nat → Nat → Nat → Prop where
  | zero (n : Nat) (positive : 0<n) (odd : n%2=1) : OneRun 0 n n
  | step {k n m z : Nat} (positive : 0<n) (odd : n%2=1)
      (edge : 3*n+1=2*m) (tail : OneRun k m z) : OneRun (k+1) n z

def iterate : Nat → Nat → Nat
  | 0, n => n
  | k+1, n => iterate k (shortcut n)

theorem one_run_sound {k n m : Nat} (h : OneRun k n m) : iterate k n = m := by
  induction h with
  | zero n _ _ => rfl
  | @step k n m z hp ho he ht ih =>
    have hs : shortcut n = m := by unfold shortcut; split <;> omega
    simpa only [iterate, hs] using ih

/-- An arbitrary run is realized by positive ordinary integers. -/
theorem ordinary_one_runs (k t : Nat) (ht : 0<t) :
    OneRun k (2^(k+1)*t-1) (2*3^k*t-1) := by
  induction k generalizing t with
  | zero =>
    simp only [Nat.zero_add, Nat.pow_one, Nat.pow_zero, Nat.mul_one]
    exact OneRun.zero _ (by omega) (by omega)
  | succ k ih =>
    have hp : 0 < 2^(k+1)*t := Nat.mul_pos (Nat.pow_pos (by omega)) ht
    have ht3 : 0 < 3*t := by omega
    have tail := ih (3*t) ht3
    have he1 : 2^(k+1+1)*t = 2*(2^(k+1)*t) := by grind
    have he2 : 2*3^k*(3*t)-1 = 2*3^(k+1)*t-1 := by grind
    have he3 : 3*(2*(2^(k+1)*t)-1)+1 = 2*(2^(k+1)*(3*t)-1) := by
      have : 2^(k+1)*(3*t) = 3*(2^(k+1)*t) := by grind
      omega
    rw [he1, ← he2]
    exact OneRun.step (by omega) (by omega) he3 tail

private theorem cubic_margin (t : Nat) :
    81*(4*t+3)^3 = 16*(6*t+5)^3 + 1728*t^3 + 3024*t^2 + 1548*t + 187 := by
  grind

theorem power_margin (t p : Nat) (hp : p<4) :
    16*(6*t+5)^p < 81*(4*t+3)^p := by
  have cases : p=0 ∨ p=1 ∨ p=2 ∨ p=3 := by omega
  rcases cases with h | h | h | h
  · subst p; simp
  · subst p; simp only [Nat.pow_one]; omega
  · subst p
    have eq : 81*(4*t+3)^2 = 16*(6*t+5)^2 + 720*t^2 + 984*t + 329 := by grind
    omega
  · subst p
    have eq := cubic_margin t
    omega

/-- Every positive finite-period coefficient has a legal expanding column
for each integral power0,1,2,3. Only one predecessor is needed. -/
theorem finite_period_power_counterexample
    (M : Nat) (hM : 0<M) (c : Nat → Rat) (hc : ∀ r, 0<c r)
    (p : Nat) (hp : p<4) :
    ∃ n m : Nat, 0<n ∧ 0<m ∧ n%2=1 ∧ m%2=1 ∧
      3*n+1=2*m ∧ n%M=m%M ∧
      16*(c (m%M)*(m : Rat)^p) < 81*(c (n%M)*(n : Rat)^p) := by
  cases M with
  | zero => omega
  | succ t =>
    have hnmod : (4*t+3)%(t+1)=t := by
      rw [show 4*t+3=(t+1)*3+t by omega, Nat.mul_add_mod_self_left]
      exact Nat.mod_eq_of_lt (by omega)
    have hmmod : (6*t+5)%(t+1)=t := by
      rw [show 6*t+5=(t+1)*5+t by omega, Nat.mul_add_mod_self_left]
      exact Nat.mod_eq_of_lt (by omega)
    refine ⟨4*t+3, 6*t+5, by omega, by omega, by omega, by omega,
      by omega, by rw [hnmod, hmmod], ?_⟩
    rw [hnmod, hmmod]
    have hnat := power_margin t p hp
    have hrat : 16*((6*t+5 : Nat) : Rat)^p < 81*((4*t+3 : Nat) : Rat)^p := by
      simpa using (Rat.natCast_lt_natCast.mpr hnat)
    have hmul := Rat.mul_lt_mul_of_pos_left hrat (hc t)
    grind

/-! Infinite ordinary one-step predecessor family of1. -/

def rootPredecessor : Nat → Nat
  | 0 => 1
  | k+1 => 4*rootPredecessor k+1

theorem root_predecessor_positive (k : Nat) : 0 < rootPredecessor k := by
  cases k <;> simp [rootPredecessor] <;> omega

theorem root_predecessor_odd (k : Nat) : rootPredecessor k%2=1 := by
  cases k <;> simp [rootPredecessor] <;> omega

theorem root_predecessor_identity (k : Nat) :
    3*rootPredecessor k+1=4^(k+1) := by
  induction k with
  | zero => rfl
  | succ k ih => simp only [rootPredecessor, Nat.pow_succ]; omega

theorem root_predecessor_lower (k : Nat) : 4^k ≤ rootPredecessor k := by
  induction k with
  | zero => exact Nat.le_refl _
  | succ k ih => simp only [rootPredecessor, Nat.pow_succ]; omega

theorem root_predecessor_mod_three (k : Nat) :
    rootPredecessor k%3=(k+1)%3 := by
  induction k with
  | zero => rfl
  | succ k ih => simp only [rootPredecessor]; omega

theorem root_predecessor_budget_subsequence (k : Nat) :
    (rootPredecessor (3*k)+1)%4=2 ∧ (rootPredecessor (3*k)+1)%3=2 := by
  have h3 := root_predecessor_mod_three (3*k)
  have h4 : (rootPredecessor (3*k)+1)%4=2 := by
    cases k with
    | zero => decide
    | succ k =>
      have he : 3*(k+1)=(3*k+2)+1 := by omega
      rw [he, rootPredecessor]
      omega
  omega

theorem root_weight_lower_cleared (k p : Nat) (hp : 4≤p) :
    256^(k+1) ≤ 256*(rootPredecessor k)^p := by
  have he : 256^k = (4^k)^4 := by
    calc
      256^k = ((4 : Nat)^4)^k := rfl
      _ = 4^(4*k) := (Nat.pow_mul _ _ _).symm
      _ = 4^(k*4) := by rw [Nat.mul_comm 4 k]
      _ = (4^k)^4 := Nat.pow_mul _ _ _
  have h1 := Nat.pow_le_pow_left (root_predecessor_lower k) 4
  have h2 := Nat.pow_le_pow_right (root_predecessor_positive k) hp
  have h3 : 256^k ≤ (rootPredecessor k)^p := by omega
  have h4 := Nat.mul_le_mul_left 256 h3
  simpa [Nat.pow_succ, Nat.mul_comm] using h4

def rootPressureTerm (k p : Nat) : Rat :=
  81*(rootPredecessor k : Rat)^p / (256 : Rat)^(k+1)

theorem root_pressure_term_lower (k p : Nat) (hp : 4≤p) :
    (81/256 : Rat) ≤ rootPressureTerm k p := by
  apply Rat.not_lt.mp
  intro hbad
  have hd : 0 < (256 : Rat)^(k+1) := Rat.pow_pos (by decide)
  have hbad' := (Rat.div_lt_iff hd).mp hbad
  have hcast : (256 : Rat)^(k+1) ≤ 256*(rootPredecessor k : Rat)^p := by
    simpa using (Rat.natCast_le_natCast.mpr (root_weight_lower_cleared k p hp))
  grind

def rootPressureSum (p : Nat) : Nat → Rat
  | 0 => 0
  | k+1 => rootPressureSum p k + rootPressureTerm k p

/-- Every finite cutoff grows at least linearly; this is an all-cutoff
statement, not an observed finite numerical pattern. -/
theorem root_pressure_sum_lower (p N : Nat) (hp : 4≤p) :
    (N : Rat)*(81/256 : Rat) ≤ rootPressureSum p N := by
  induction N with
  | zero => simp [rootPressureSum]
  | succ N ih =>
    have hterm := root_pressure_term_lower N p hp
    simp only [rootPressureSum]
    have hcast : ((N+1 : Nat) : Rat) = (N : Rat)+1 := by simp
    rw [hcast]
    grind

/-! The reset that defeats a single ternary-run charge. -/

def resetEndpoint : Nat → Nat
  | 0 => 1
  | k+1 => 9*resetEndpoint k+4

def resetSource (k : Nat) : Nat := 2*9^k-1

theorem reset_endpoint_identity (k : Nat) :
    3*9^k = 2*resetEndpoint k+1 := by
  induction k with
  | zero => rfl
  | succ k ih => simp only [resetEndpoint, Nat.pow_succ]; omega

theorem reset_endpoint_odd (k : Nat) : resetEndpoint k%2=1 := by
  induction k with
  | zero => rfl
  | succ k ih => simp only [resetEndpoint]; omega

theorem reset_budget_identity (k : Nat) :
    0<resetSource k ∧ resetSource k%2=1 ∧
    3*resetSource k+1=4*resetEndpoint k ∧ resetEndpoint k%2=1 ∧
    (resetEndpoint k+1)%3=2 ∧ resetSource k+1=2*3^(2*k) := by
  have hpow : 0 < (9 : Nat)^k := Nat.pow_pos (by decide)
  have he := reset_endpoint_identity k
  have ho := reset_endpoint_odd k
  have hpowers : (9 : Nat)^k = 3^(2*k) := by rw [Nat.pow_mul]
  unfold resetSource
  omega

def binaryResetSource : Nat → Nat
  | 0 => 1
  | k+1 => 64*binaryResetSource k+105

def binaryResetEndpoint (k : Nat) : Nat := 2*64^k-1

theorem binary_reset_source_identity (k : Nat) :
    3*binaryResetSource k+5=8*64^k := by
  induction k with
  | zero => rfl
  | succ k ih => simp only [binaryResetSource, Nat.pow_succ]; omega

theorem binary_reset_source_budgets (k : Nat) :
    0<binaryResetSource k ∧ (binaryResetSource k+1)%4=2 ∧
    (binaryResetSource k+1)%3=2 := by
  induction k with
  | zero => decide
  | succ k ih => simp only [binaryResetSource]; omega

/-- The a=2 inverse step erases an arbitrarily large binary run budget
without changing either ternary run budget. -/
theorem binary_reset_budget_identity (k : Nat) :
    0<binaryResetSource k ∧ binaryResetSource k%2=1 ∧
    0<binaryResetEndpoint k ∧ binaryResetEndpoint k%2=1 ∧
    3*binaryResetSource k+1=4*binaryResetEndpoint k ∧
    (binaryResetSource k+1)%4=2 ∧ (binaryResetSource k+1)%3=2 ∧
    binaryResetEndpoint k+1=2^(6*k+1) ∧
    (binaryResetEndpoint k+1)%3=2 := by
  have hpow : 0 < (64 : Nat)^k := Nat.pow_pos (by decide)
  have hpow3 : (64 : Nat)^k%3=1 := by
    induction k with
    | zero => rfl
    | succ k ih => rw [Nat.pow_succ]; omega
  have he := binary_reset_source_identity k
  have hb := binary_reset_source_budgets k
  have hpowers : (64 : Nat)^k=2^(6*k) := by rw [Nat.pow_mul]
  have he2 : 2^(6*k+1)=2*64^k := by rw [Nat.pow_succ]; omega
  unfold binaryResetEndpoint
  omega

end CollatzInversePressure
