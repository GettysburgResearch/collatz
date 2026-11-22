import Mathlib.Basic.Real.Basic
import Mathlib.Algebra.Order.BigOperators.Ring.Finset
import Mathlib.Algebra.BigOperators.Pi
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp

/-!
Exact finite algebra for a calibrated ordinary inverse-density horizon.
The marginal mixing and ordinary counting theorems remain explicit written
inputs. No infinite-depth estimate or universal Collatz assertion is made.
-/

namespace CollatzShell.FiniteSpikeClosure

open Finset

/-- A finite periodic row has an exact geometric remainder. This is the
algebra used to replace its entire exponent series by a finite rational row. -/
theorem geometric_block_identity (r : ℝ) (J : ℕ) :
    (1-r) * (∑ j ∈ range J, r^j) = 1-r^J := by
  induction J with
  | zero => simp
  | succ J ih =>
    rw [sum_range_succ, mul_add, ih, pow_succ]
    ring

/-- The explicit cutoff `6*d+3*t` pays the entire geometric valuation tail.
There is no unspecified asymptotic constant in this normalization. -/
theorem full_clock_tail_bound (d t : ℕ) :
    (3 : ℝ)^t * 9^d * (2/3 : ℝ)^(6*d+3*t) ≤ 1 := by
  have identity :
      (3 : ℝ)^t * 9^d * (2/3 : ℝ)^(6*d+3*t) =
        (64/81 : ℝ)^d * (8/9 : ℝ)^t := by
    rw [pow_add, pow_mul, pow_mul]
    calc
      (3 : ℝ)^t * 9^d * (((2/3 : ℝ)^6)^d * ((2/3 : ℝ)^3)^t) =
          (9*(2/3 : ℝ)^6)^d * (3*(2/3 : ℝ)^3)^t := by
            rw [mul_pow, mul_pow]
            ring
      _ = (64/81 : ℝ)^d * (8/9 : ℝ)^t := by norm_num
  rw [identity]
  have h₁ : (64/81 : ℝ)^d ≤ 1 := pow_le_one₀ (by norm_num) (by norm_num)
  have h₂ : (8/9 : ℝ)^t ≤ 1 := pow_le_one₀ (by norm_num) (by norm_num)
  calc
    (64/81 : ℝ)^d * (8/9 : ℝ)^t ≤ 1 * (8/9 : ℝ)^t :=
      mul_le_mul_of_nonneg_right h₁ (by positivity)
    _ ≤ 1 := by simpa using h₂

/-- Finite block errors of any nonnegative affine size accumulate within
an explicit quadratic budget. Hypotheses are needed only through `K`. -/
theorem affine_error_budget (f : ℕ → ℝ) (m K : ℕ) (hm : 0 < m)
    (B ε a b : ℝ) (he : 0 ≤ ε) (ha : 0 ≤ a) (hb : 0 ≤ b)
    (hbase : ∀ s, s ≤ K → s ≤ 2*m → f s ≤ B)
    (hstep : ∀ s, s ≤ K → 2*m < s →
      f s ≤ f (s-m) + ε*(a*(s : ℝ)+b))
    (s : ℕ) (hsK : s ≤ K) :
    (m : ℝ)*f s ≤ (m : ℝ)*B + ε*(s : ℝ)*(a*(s : ℝ)+b) := by
  revert hsK
  induction s using Nat.strong_induction_on with
  | h s ih =>
    intro hsK
    have hm0 : (0 : ℝ) ≤ m := Nat.cast_nonneg m
    have hs0 : (0 : ℝ) ≤ s := Nat.cast_nonneg s
    by_cases hs : s ≤ 2*m
    · have initial := mul_le_mul_of_nonneg_left (hbase s hsK hs) hm0
      have extra : 0 ≤ ε*(s : ℝ)*(a*(s : ℝ)+b) := by positivity
      linarith
    · have hlarge : 2*m < s := Nat.lt_of_not_ge hs
      have hms : m ≤ s := by omega
      have hsmall : s-m < s := by omega
      have prior := ih (s-m) hsmall ((Nat.sub_le s m).trans hsK)
      have oneStep := mul_le_mul_of_nonneg_left (hstep s hsK hlarge) hm0
      have slack : 0 ≤ a*ε*(m : ℝ)*((s-m : ℕ) : ℝ) := by positivity
      calc
        (m : ℝ)*f s ≤ (m : ℝ)*f (s-m) +
            (m : ℝ)*ε*(a*(s : ℝ)+b) := by nlinarith only [oneStep]
        _ ≤ (m : ℝ)*B + ε*((s-m : ℕ) : ℝ)*(a*((s-m : ℕ) : ℝ)+b) +
            (m : ℝ)*ε*(a*(s : ℝ)+b) := by linarith only [prior]
        _ = (m : ℝ)*B + ε*(s : ℝ)*(a*(s : ℝ)+b) -
            a*ε*(m : ℝ)*((s-m : ℕ) : ℝ) := by
              rw [Nat.cast_sub hms]
              ring
        _ ≤ (m : ℝ)*B + ε*(s : ℝ)*(a*(s : ℝ)+b) := sub_le_self _ slack

/-- Quartic calibration converts the actual finite error into a rational
inverse-square horizon bound. The error is not an unspecified constant. -/
theorem quartic_calibration {ε H : ℝ} (he : 0 ≤ ε) (hH : 1 ≤ H)
    (calibrated : H^4*ε ≤ 1) :
    ε*H*(5*H+4) ≤ 9/H^2 := by
  have hp : 0 < H := lt_of_lt_of_le zero_lt_one hH
  have hsq : 0 < H^2 := pow_pos hp 2
  apply (le_div_iff₀ hsq).2
  have poly : H*(5*H+4) ≤ 9*H^2 := by nlinarith
  have scaled := mul_le_mul_of_nonneg_left poly (mul_nonneg he hsq.le)
  have target : (ε*H*(5*H+4))*H^2 ≤ 9*(H^4*ε) := by
    nlinarith only [scaled]
  linarith

/-- The calibrated estimate holds at every finite depth through the same
horizon, with the physical block recurrence kept explicit. -/
theorem calibrated_horizon (f : ℕ → ℝ) (m K H : ℕ)
    (hm : 0 < m) (hH : 0 < H) (hKH : K ≤ H) (B ε : ℝ) (he : 0 ≤ ε)
    (calibrated : (H : ℝ)^4*ε ≤ 1)
    (hbase : ∀ s, s ≤ K → s ≤ 2*m → f s ≤ B)
    (hstep : ∀ s, s ≤ K → 2*m < s →
      f s ≤ f (s-m) + ε*(5*(s : ℝ)+4))
    (s : ℕ) (hsK : s ≤ K) :
    f s ≤ B + 9/((m : ℝ)*(H : ℝ)^2) := by
  have budget := affine_error_budget f m K hm B ε 5 4 he
    (by norm_num) (by norm_num) hbase hstep s hsK
  have hs0 : (0 : ℝ) ≤ s := Nat.cast_nonneg s
  have hH0 : (0 : ℝ) ≤ H := Nat.cast_nonneg H
  have hsHR : (s : ℝ) ≤ H := by exact_mod_cast hsK.trans hKH
  have poly : (s : ℝ)*(5*(s : ℝ)+4) ≤ (H : ℝ)*(5*(H : ℝ)+4) := by
    nlinarith
  have scaled := mul_le_mul_of_nonneg_left poly he
  have hH1 : (1 : ℝ) ≤ H := by exact_mod_cast hH
  have cert := quartic_calibration he hH1 calibrated
  have hmR : (0 : ℝ) < m := by exact_mod_cast hm
  have Hsq : (0 : ℝ) < (H : ℝ)^2 := by positivity
  have total : (m : ℝ)*f s ≤ (m : ℝ)*B + 9/(H : ℝ)^2 := by
    nlinarith only [budget, scaled, cert]
  apply (le_of_mul_le_mul_left (a := (m : ℝ)) ?_ hmR)
  have cancel : (m : ℝ)*(9/((m : ℝ)*(H : ℝ)^2)) = 9/(H : ℝ)^2 := by
    field_simp [hmR.ne', Hsq.ne']
  rw [mul_add, cancel]
  exact total

/-- One maximally calibrated horizon eventually dominates every fixed
polynomial by every fixed factor. The finite error sequence is chosen once;
the conclusion does not choose a new horizon for each polynomial. -/
theorem calibration_dominates_polynomials (E : ℕ → ℝ) (H : ℕ → ℕ)
    (rapid : ∀ r : ℕ, ∃ M : ℕ, ∀ m : ℕ, M ≤ m → E m * (m : ℝ)^r ≤ 1)
    (maximal : ∀ m k : ℕ, (k : ℝ)^4 * E m ≤ 1 → k ≤ H m)
    (B R : ℕ) :
    ∃ M : ℕ, ∀ m : ℕ, M ≤ m → R * m^B ≤ H m := by
  obtain ⟨M₀, control⟩ := rapid (4*(B+1))
  refine ⟨max M₀ R, ?_⟩
  intro m hm
  have hm₀ : M₀ ≤ m := (le_max_left M₀ R).trans hm
  have hmR : R ≤ m := (le_max_right M₀ R).trans hm
  have admitted : ((m^(B+1) : ℕ) : ℝ)^4 * E m ≤ 1 := by
    rw [Nat.cast_pow, ← pow_mul, Nat.mul_comm (B+1) 4, mul_comm]
    exact control m hm₀
  have large := maximal m (m^(B+1)) admitted
  calc
    R*m^B ≤ m*m^B := Nat.mul_le_mul_right _ hmR
    _ = m^(B+1) := by rw [pow_succ, Nat.mul_comm]
    _ ≤ H m := large

/-- Every finite obstacle iterate is bounded by the finite sum of ordinary
density iterates. Only the displayed finite sums and iterates must lie in the positive
operator domain; no invariant density, global majorant, population theorem,
or normalization factor enters. -/
theorem finite_obstacle_sum {α : Type*}
    (P : (α → ℝ) → (α → ℝ)) (domain : Set (α → ℝ))
    (hP : MonotoneOn P domain)
    (g : α → ℝ) (hg : ∀ x, g x ≤ 1)
    (D V : ℕ → α → ℝ)
    (Vmem : ∀ k, V k ∈ domain)
    (sum_mem : ∀ k, (∑ j ∈ range (k+1), D j) ∈ domain)
    (Psum : ∀ k, P (∑ j ∈ range (k+1), D j) =
      ∑ j ∈ range (k+1), P (D j))
    (Dzero : D 0 = fun _ => 1)
    (Dstep : ∀ j, D (j+1) = P (D j))
    (Dnonneg : ∀ j x, 0 ≤ D j x)
    (Vzero : V 0 = g)
    (Vstep : ∀ j x, V (j+1) x = max (g x) (P (V j) x))
    (k : ℕ) :
    V k ≤ ∑ j ∈ range (k+1), D j := by
  classical
  induction k with
  | zero =>
    intro x
    simp only [Nat.zero_add, sum_range_one, Dzero, Vzero]
    exact hg x
  | succ k ih =>
    intro x
    have mapped : P (∑ j ∈ range (k+1), D j) x =
        ∑ j ∈ range (k+1), D (j+1) x := by
      rw [Psum]
      simp only [Finset.sum_apply, ← Dstep]
    have split : (∑ j ∈ range (k+2), D j) x =
        (∑ j ∈ range (k+1), D (j+1) x) + 1 := by
      rw [sum_range_succ']
      simp only [Pi.add_apply, Finset.sum_apply, Dzero]
    have nonnegative : 0 ≤ ∑ j ∈ range (k+1), D (j+1) x :=
      sum_nonneg (fun j _ => Dnonneg (j+1) x)
    change V (k+1) x ≤ (∑ j ∈ range (k+2), D j) x
    rw [Vstep, split]
    apply max_le
    · linarith [hg x]
    · have transported := hP (Vmem k) (sum_mem k) ih x
      rw [mapped] at transported
      linarith

/-- A finite calibrated bound really extracts an ordinary ancestor when
violated. The finite-floor implication is supplied explicitly; this lemma
does not install the analytic estimate as an axiom. -/
theorem finite_floor_extraction (U : ℕ → ℕ) (unit : ℕ → Prop)
    (q b K : ℕ) (v bound : ℝ) (hbq : b ≤ q)
    (floor_bound :
      (∀ j, j ≤ K → ∀ n, unit n → (U^[j]) n = q → b ≤ n) → v ≤ bound)
    (spike : bound < v) :
    ∃ j, 0 < j ∧ j ≤ K ∧ ∃ n, unit n ∧ n < b ∧ (U^[j]) n = q := by
  classical
  by_contra none
  have allFloor : ∀ j, j ≤ K → ∀ n, unit n → (U^[j]) n = q → b ≤ n := by
    intro j hj n hn hit
    by_contra small
    have hnb : n < b := Nat.lt_of_not_ge small
    have hj0 : 0 < j := by
      by_contra zero
      have jzero : j = 0 := by omega
      simp only [jzero, Function.iterate_zero, id_eq] at hit
      omega
    exact none ⟨j, hj0, hj, n, hn, hnb, hit⟩
  exact (not_lt_of_ge (floor_bound allFloor)) spike

#print axioms geometric_block_identity
#print axioms full_clock_tail_bound
#print axioms affine_error_budget
#print axioms quartic_calibration
#print axioms calibrated_horizon
#print axioms calibration_dominates_polynomials
#print axioms finite_obstacle_sum
#print axioms finite_floor_extraction

end CollatzShell.FiniteSpikeClosure
