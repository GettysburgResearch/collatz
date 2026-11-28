import PinClock
import DiscountedParity

/-! Pointwise equivalence between convergence and the maximum pin depth at each arity.
The final bound remains an open universal assertion. -/
set_option autoImplicit false
set_option warningAsError true

namespace PinCriterion

open CoreBranching PinClock Collatz.DiscountedParity

def evenCount : ℕ → ℕ → ℕ
  | 0, _ => 0
  | k+1, n => (if n%2=0 then 1 else 0) + evenCount k (step n)

def clock : ℕ → ℕ → ℕ
  | 0, n => twos (n+1)
  | e+1, n => (twos (n+1)+1) + clock e (afterEven n)

theorem clock_greedy (e n : ℕ) :
    twos (code (word (greedy e n)) n) = clock e n := by
  rw [valuation_code]
  induction e generalizing n with
  | zero => rfl
  | succ e ih =>
    simp only [greedy, word, depth_addRun, ite_true, clock]
    rw [ih]

theorem evenCount_add (a b n : ℕ) :
    evenCount (a+b) n = evenCount a n + evenCount b (run a n) := by
  induction a generalizing n with
  | zero => simp [evenCount, run]
  | succ a ih => simp only [Nat.succ_add, evenCount, run, ih, Nat.add_assoc]

theorem first_block (g n : ℕ) (hg : twos (n+1)=g) :
    evenCount g n=0 ∧ evenCount (g+1) n=1 := by
  induction g generalizing n with
  | zero =>
    have he : n%2=0 := by
      by_contra ho
      have := odd_twos ho
      omega
    simp [evenCount, he]
  | succ g ih =>
    have ho : n%2≠0 := by
      intro he
      have := even_twos he
      omega
    have hnext : twos (step n+1)=g := by
      have := odd_twos ho
      omega
    obtain ⟨h0,h1⟩ := ih (step n) hnext
    exact ⟨by simpa only [evenCount, ho, ite_false, Nat.zero_add] using h0,
      by simpa only [evenCount, ho, ite_false, Nat.zero_add] using h1⟩

theorem clock_evenCount (e n : ℕ) : evenCount (clock e n) n=e := by
  induction e generalizing n with
  | zero => exact (first_block _ n rfl).1
  | succ e ih =>
    rw [clock, evenCount_add, (first_block _ n rfl).2, run_add]
    change 1+evenCount (clock e (afterEven n)) (afterEven n)=e+1
    rw [ih]
    omega

private theorem even_clock_succ (e n : ℕ) (h : n%2=0) :
    clock (e+1) n = clock e (step n)+1 := by
  simp [clock, even_twos h, afterEven, run, Nat.add_comm]

private theorem odd_clock (e n : ℕ) (h : n%2≠0) :
    clock e n = clock e (step n)+1 := by
  cases e <;> simp only [clock, odd_twos h, afterEven_odd h] <;> omega

theorem clock_dominates (k n : ℕ) : k ≤ clock (evenCount k n) n := by
  induction k generalizing n with
  | zero => exact Nat.zero_le _
  | succ k ih =>
    have hnext := ih (step n)
    by_cases he : n%2=0
    · simp only [evenCount, he, ite_true, Nat.one_add, even_clock_succ _ _ he]
      omega
    · simp only [evenCount, he, ite_false, Nat.zero_add, odd_clock _ _ he]
      omega

theorem rank_times_three (k n : ℕ) :
    rank k n * (3:ℚ)^(evenCount k n)=(51/32:ℚ)^k := by
  induction k generalizing n with
  | zero => simp [rank, evenCount]
  | succ k ih =>
    have hnext := ih (step n)
    by_cases h : n%2=0
    · simp only [rank, weight, evenCount, h, ite_true, Nat.one_add, pow_succ]
      nlinarith
    · simp only [rank, weight, evenCount, h, ite_false, Nat.zero_add, pow_succ]
      nlinarith

/-- A bound at fixed arity for every arity is equivalent to actual convergence of
this ordinary input. No uniform bound across sources is assumed. -/
theorem bounded_greedy_iff (n : ℕ) (hn : 0<n) :
    (∃ B : ℚ, ∀ e, (51/32:ℚ)^(twos (code (word (greedy e n)) n))≤B*3^e)
      ↔ Converges n := by
  rw [←bounded_rank_iff n hn]
  constructor
  · rintro ⟨B,bound⟩
    refine ⟨B,fun k => ?_⟩
    have hclock := bound (evenCount k n)
    rw [clock_greedy] at hclock
    have hpow := pow_le_pow_right₀ (by norm_num : (1:ℚ)≤51/32) (clock_dominates k n)
    have hprod : rank k n*(3:ℚ)^evenCount k n ≤ B*3^evenCount k n := by
      rw [rank_times_three]
      exact hpow.trans hclock
    exact (mul_le_mul_iff_of_pos_right (by positivity : (0:ℚ)<3^evenCount k n)).mp hprod
  · rintro ⟨B,bound⟩
    refine ⟨B,fun e => ?_⟩
    rw [clock_greedy, ←rank_times_three (clock e n) n, clock_evenCount]
    exact mul_le_mul_of_nonneg_right (bound _) (by positivity)

#print axioms clock_greedy
#print axioms clock_evenCount
#print axioms clock_dominates
#print axioms bounded_greedy_iff

end PinCriterion
