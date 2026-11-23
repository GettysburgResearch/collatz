import Mathlib.Algebra.Polynomial.Roots
import Mathlib.Data.Fintype.Pi
import Mathlib.Algebra.Order.Archimedean.Basic
import Mathlib.Tactic

/-!
An elementary finite-window reconstruction of the Pólya/Bézivin rationality
mechanism for the weighted actual parity series. No polynomial recurrence is
asserted for an arbitrary Collatz orbit: its existence is an explicit premise.
-/

namespace CollatzProfound.ParityRecurrence

open Polynomial
open scoped BigOperators

/-- A finite family of polynomials cannot keep vanishing at increasing natural
arguments through its nonzero members. -/
theorem finite_choice_eventually_zero
    {ι : Type*} [Fintype ι] (P : ι → ℚ[X]) (choice : ℕ → ι)
    (N₀ : ℕ) (heval : ∀ n, N₀ ≤ n → (P (choice n)).eval (n : ℚ) = 0) :
    ∃ N : ℕ, ∀ n, N ≤ n → P (choice n) = 0 := by
  classical
  have hbound : ∀ i, ∃ N : ℕ, ∀ n, N ≤ n → (P i).eval (n : ℚ) = 0 → P i = 0 := by
    intro i
    by_cases hp : P i = 0
    · exact ⟨0, fun _ _ _ => hp⟩
    · obtain ⟨b, hb⟩ := (P i).exists_max_root hp
      obtain ⟨N, hN⟩ := exists_nat_gt b
      refine ⟨N, ?_⟩
      intro n hn hz
      have hnb : b < (n : ℚ) := hN.trans_le (Nat.cast_le.mpr hn)
      exact False.elim (not_lt_of_ge (hb (n : ℚ) hz) hnb)
  choose bound hbound using hbound
  refine ⟨max N₀ (Finset.univ.sup bound), ?_⟩
  intro n hn
  have hN₀ : N₀ ≤ n := (le_max_left _ _).trans hn
  have hchoice : bound (choice n) ≤ n :=
    (Finset.le_sup (f := bound) (Finset.mem_univ (choice n))).trans
      ((le_max_right _ _).trans hn)
  exact hbound (choice n) n hchoice (heval n hN₀)

/-- Finite normalized windows turn any eventual polynomial-coefficient
recurrence into one nonzero constant-coefficient recurrence. -/
theorem constant_recurrence_of_finite_normalized_windows
    {ι : Type*} [Fintype ι] (d : ℕ)
    (b scale : ℕ → ℚ) (choice : ℕ → ι) (window : ι → Fin (d + 1) → ℚ)
    (hscale : ∀ n, scale n ≠ 0)
    (hwindow : ∀ n (j : Fin (d + 1)), scale n * b (n + j) = window (choice n) j)
    (P : Fin (d + 1) → ℚ[X]) (hP : ∃ j, P j ≠ 0)
    (N₀ : ℕ)
    (hrec : ∀ n, N₀ ≤ n → ∑ j, (P j).eval (n : ℚ) * b (n + j) = 0) :
    ∃ c : Fin (d + 1) → ℚ, (∃ j, c j ≠ 0) ∧
      ∃ N : ℕ, ∀ n, N ≤ n → ∑ j, c j * b (n + j) = 0 := by
  classical
  let Q : ι → ℚ[X] := fun i => ∑ j, C (window i j) * P j
  have heval : ∀ n, N₀ ≤ n → (Q (choice n)).eval (n : ℚ) = 0 := by
    intro n hn
    simp only [Q, eval_finsetSum, eval_mul, eval_C]
    calc
      ∑ j, window (choice n) j * (P j).eval (n : ℚ) =
          scale n * ∑ j, (P j).eval (n : ℚ) * b (n + j) := by
        rw [Finset.mul_sum]
        apply Finset.sum_congr rfl
        intro j _
        rw [← hwindow n j]
        ring
      _ = 0 := by rw [hrec n hn, mul_zero]
  obtain ⟨N, hN⟩ := finite_choice_eventually_zero Q choice N₀ heval
  obtain ⟨j₀, hj₀⟩ := hP
  have hcoeff : ∃ r, (P j₀).coeff r ≠ 0 := by
    by_contra h
    push Not at h
    exact hj₀ (Polynomial.ext fun r => by simpa using h r)
  obtain ⟨r, hr⟩ := hcoeff
  refine ⟨fun j => (P j).coeff r, ⟨j₀, hr⟩, N, ?_⟩
  intro n hn
  have hc := congrArg (fun p : ℚ[X] => p.coeff r) (hN n hn)
  simp only [Q, finsetSum_coeff, coeff_C_mul, coeff_zero] at hc
  have hmul : scale n * (∑ j, (P j).coeff r * b (n + j)) = 0 := by
    calc
      scale n * (∑ j, (P j).coeff r * b (n + j)) =
          ∑ j, window (choice n) j * (P j).coeff r := by
        rw [Finset.mul_sum]
        apply Finset.sum_congr rfl
        intro j _
        rw [← hwindow n j]
        ring
      _ = 0 := hc
  exact (mul_eq_zero.mp hmul).resolve_left (hscale n)

/-- Number of odd symbols before the given clock. -/
def oddCount (e : ℕ → Bool) : ℕ → ℕ
  | 0 => 0
  | n + 1 => oddCount e n + if e n then 1 else 0

/-- The coefficient used by the actual parity series. -/
def parityCoeff (e : ℕ → Bool) (n : ℕ) : ℚ :=
  (if e n then 1 else 0) / (3 : ℚ) ^ oddCount e (n + 1)

theorem oddCount_le (e : ℕ → Bool) (n : ℕ) : oddCount e n ≤ n := by
  induction n with
  | zero => simp [oddCount]
  | succ n ih =>
      simp only [oddCount]
      split <;> omega

theorem oddCount_add (e : ℕ → Bool) (n k : ℕ) :
    oddCount e (n + k) = oddCount e n + oddCount (fun j => e (n + j)) k := by
  induction k with
  | zero => simp [oddCount]
  | succ k ih => simp [oddCount, ih, Nat.add_assoc]

/-- The actual weighted parity coefficients have finitely many normalized
windows of each fixed length; no orbit regularity is assumed here. -/
theorem parity_finite_normalized_windows (e : ℕ → Bool) (d : ℕ) :
    ∃ (choice : ℕ → (Fin (d + 1) → Bool × Fin (d + 2)))
      (window : (Fin (d + 1) → Bool × Fin (d + 2)) → Fin (d + 1) → ℚ),
      ∀ n (j : Fin (d + 1)),
        (3 : ℚ) ^ oddCount e n * parityCoeff e (n + j) = window (choice n) j := by
  classical
  let choice : ℕ → (Fin (d + 1) → Bool × Fin (d + 2)) := fun n j =>
    (e (n + j), ⟨oddCount (fun k => e (n + k)) (j + 1), by
      have h := oddCount_le (fun k => e (n + k)) (j + 1)
      have hj := j.isLt
      omega⟩)
  let window : (Fin (d + 1) → Bool × Fin (d + 2)) → Fin (d + 1) → ℚ :=
    fun v j => (if (v j).1 then 1 else 0) / (3 : ℚ) ^ (v j).2.val
  refine ⟨choice, window, ?_⟩
  intro n j
  change (3 : ℚ) ^ oddCount e n *
      ((if e (n + j) then 1 else 0) / (3 : ℚ) ^ oddCount e (n + j + 1)) =
    (if e (n + j) then 1 else 0) /
      (3 : ℚ) ^ oddCount (fun k => e (n + k)) (j + 1)
  rw [Nat.add_assoc, oddCount_add, pow_add]
  have hp : (3 : ℚ) ^ oddCount e n ≠ 0 := pow_ne_zero _ (by norm_num)
  have hq : (3 : ℚ) ^ oddCount (fun k => e (n + k)) (j + 1) ≠ 0 :=
    pow_ne_zero _ (by norm_num)
  field_simp

/-- For every actual binary itinerary, a polynomial-coefficient recurrence
for its weighted parity coefficients implies a constant-coefficient one.
The recurrence premise itself is not proved for arbitrary Collatz inputs. -/
theorem parity_constant_recurrence (e : ℕ → Bool) (d : ℕ)
    (P : Fin (d + 1) → ℚ[X]) (hP : ∃ j, P j ≠ 0)
    (N₀ : ℕ)
    (hrec : ∀ n, N₀ ≤ n →
      ∑ j, (P j).eval (n : ℚ) * parityCoeff e (n + j) = 0) :
    ∃ c : Fin (d + 1) → ℚ, (∃ j, c j ≠ 0) ∧
      ∃ N : ℕ, ∀ n, N ≤ n → ∑ j, c j * parityCoeff e (n + j) = 0 := by
  obtain ⟨choice, window, hwindow⟩ := parity_finite_normalized_windows e d
  exact constant_recurrence_of_finite_normalized_windows d
    (parityCoeff e) (fun n => (3 : ℚ) ^ oddCount e n) choice window
    (fun n => pow_ne_zero _ (by norm_num)) hwindow P hP N₀ hrec

end CollatzProfound.ParityRecurrence
