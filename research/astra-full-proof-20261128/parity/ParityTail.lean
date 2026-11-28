import Mathlib.Tactic

set_option autoImplicit false
set_option warningAsError true
set_option maxRecDepth 12000
set_option exponentiation.threshold 1000

namespace Collatz.FullProof.Parity

def step (n : ℕ) : ℕ := if n % 2 = 0 then n / 2 else (3 * n + 1) / 2

def run (n : ℕ) : ℕ → ℕ
  | 0 => n
  | t + 1 => run (step n) t

def count (n : ℕ) : ℕ → ℕ
  | 0 => 0
  | t + 1 => n % 2 + count (step n) t

def Nonconvergent (n : ℕ) : Prop := 0 < n ∧ ∀ t, run n t ≠ 1

theorem step_positive {n : ℕ} (hn : 0 < n) : 0 < step n := by
  unfold step
  split <;> omega

theorem next_nonconvergent {n : ℕ} (hn : Nonconvergent n) :
    Nonconvergent (step n) :=
  ⟨step_positive hn.1, fun t => hn.2 (t+1)⟩

-- The finite decision checks actual shortcut trajectories for all starts 1 through 64.
set_option maxRecDepth 10000 in
set_option maxHeartbeats 1000000 in
theorem small_range : ∀ n : Fin 65, n.val = 0 ∨ ∃ t : Fin 72, run n.val t.val = 1 := by
  decide

theorem bad_floor {n : ℕ} (hn : Nonconvergent n) : 65 ≤ n := by
  by_contra! h
  rcases small_range ⟨n,h⟩ with zero | ⟨t,hit⟩
  · exact (Nat.ne_of_gt hn.1) zero
  · exact hn.2 t.val hit

theorem native_product {n : ℕ} (hn : Nonconvergent n) (t : ℕ) :
    (2:ℚ)^t * (run n t : ℕ) ≤ (n:ℚ) * ((196:ℚ)/65)^(count n t) := by
  induction t generalizing n with
  | zero => simp [run, count]
  | succ t ih =>
    have hn' := ih (next_nonconvergent hn)
    have hs : (2:ℚ) * (step n : ℕ) ≤ (n:ℚ) * ((196:ℚ)/65)^(n%2) := by
      by_cases h : n%2=0
      · have eq : 2 * step n = n := by simp [step,h]; omega
        rw [h, pow_zero, mul_one]
        exact_mod_cast le_of_eq eq
      · have h1 : n%2=1 := by omega
        have eq : 2 * step n = 3*n+1 := by simp [step,h]; omega
        have hc : (2:ℚ) * (step n : ℕ) = 3 * (n:ℚ)+1 := by exact_mod_cast eq
        have hf : (65:ℚ) ≤ (n:ℚ) := by exact_mod_cast bad_floor hn
        rw [h1,pow_one,hc]
        linarith
    calc
      (2:ℚ)^(t+1) * (run n (t+1) : ℕ) = 2 * (2^t * (run (step n) t : ℕ)) := by
        simp only [run,pow_succ]
        ring
      _ ≤ 2 * ((step n : ℚ) * ((196:ℚ)/65)^(count (step n) t)) := by linarith
      _ = (2 * (step n : ℕ)) * ((196:ℚ)/65)^(count (step n) t) := by ring
      _ ≤ ((n:ℚ) * ((196:ℚ)/65)^(n%2)) * ((196:ℚ)/65)^(count (step n) t) :=
        mul_le_mul_of_nonneg_right hs (by positivity)
      _ = (n:ℚ) * ((196:ℚ)/65)^(count n (t+1)) := by rw [count,pow_add]; ring

theorem run_positive {n : ℕ} (hn : 0 < n) (t : ℕ) : 0 < run n t := by
  induction t generalizing n with
  | zero => exact hn
  | succ t ih => exact ih (step_positive hn)

private theorem threshold {q k : ℕ} {c : ℚ} (hk : 0 < k) (hc : 1 ≤ c)
    (cert : c^501 < (2:ℚ)^800) (h4 : (2:ℚ)^(4*k) ≤ c^q) :
    501*(5*k) < 1000*q := by
  by_contra! hf
  have eq : 200*q ≤ 501*k := by omega
  have hp : (2:ℚ)^((4*k)*200) ≤ c^(q*200) := by
    simpa only [← pow_mul] using pow_le_pow_left₀ (by positivity) h4 200
  have exp : q*200 ≤ 501*k := by omega
  have lower : (2:ℚ)^(800*k) ≤ c^(501*k) := by
    calc
      (2:ℚ)^(800*k) = 2^((4*k)*200) := by congr 1; omega
      _ ≤ c^(q*200) := hp
      _ ≤ c^(501*k) := pow_le_pow_right₀ hc exp
  rw [pow_mul,pow_mul] at lower
  exact (not_lt_of_ge lower) (pow_lt_pow_left₀ cert (by positivity) hk.ne')

theorem fifth_clock_needs_high_count {n k : ℕ} (hn : Nonconvergent n)
    (hk : 0 < k) (hx : n ≤ 2^k) :
    501*(5*k) < 1000*count n (5*k) := by
  let q := count n (5*k)
  let c := (196:ℚ)/65
  have hprod := native_product hn (5*k)
  have hstate : (1:ℚ) ≤ (run n (5*k) : ℕ) := by exact_mod_cast run_positive hn.1 (5*k)
  have hsource : (n:ℚ) ≤ (2:ℚ)^k := by exact_mod_cast hx
  have h1 : (2:ℚ)^(5*k) ≤ 2^k*c^q := by
    calc
      (2:ℚ)^(5*k) ≤ 2^(5*k)*(run n (5*k) : ℕ) := le_mul_of_one_le_right (by positivity) hstate
      _ ≤ (n:ℚ)*c^q := hprod
      _ ≤ 2^k*c^q := mul_le_mul_of_nonneg_right hsource (by positivity)
  have h4 : (2:ℚ)^(4*k) ≤ c^q := by
    apply le_of_mul_le_mul_left _ (by positivity : (0:ℚ)<2^k)
    rwa [← pow_add,show k+4*k=5*k by omega]
  have cert : c^501 < (2:ℚ)^800 := by
    change ((196:ℚ)/65)^501 < (2:ℚ)^800
    rw [div_pow, div_lt_iff₀ (by positivity)]
    exact_mod_cast (by decide : (196:ℕ)^501 < 2^800 * 65^501)
  exact threshold hk (by norm_num [c]) cert h4

/-- Reflecting a negative input for the plus map gives this minus shortcut on positives. -/
def minusStep (x : ℕ) : ℕ := if x%2=0 then x/2 else (3*x-1)/2

def minusRun (x : ℕ) : ℕ → ℕ
  | 0 => x
  | t+1 => minusRun (minusStep x) t

def minusCount (x : ℕ) : ℕ → ℕ
  | 0 => 0
  | t+1 => x%2 + minusCount (minusStep x) t

theorem minus_step_positive {x : ℕ} (hx : 0 < x) : 0 < minusStep x := by
  unfold minusStep
  split <;> omega

theorem minus_run_positive {x : ℕ} (hx : 0 < x) (t : ℕ) : 0 < minusRun x t := by
  induction t generalizing x with
  | zero => exact hx
  | succ t ih => exact ih (minus_step_positive hx)

theorem minus_product (x t : ℕ) (hx : 0 < x) :
    2^t*minusRun x t ≤ x*3^(minusCount x t) := by
  induction t generalizing x with
  | zero => simp [minusRun, minusCount]
  | succ t ih =>
    have h := ih (minusStep x) (minus_step_positive hx)
    have hs : 2*minusStep x ≤ x*3^(x%2) := by
      by_cases he : x%2=0
      · simp [minusStep, he]; omega
      · have ho : x%2=1 := by omega
        simp [minusStep,ho]; omega
    calc
      2^(t+1)*minusRun x (t+1) = 2*(2^t*minusRun (minusStep x) t) := by
        simp only [minusRun, pow_succ]
        ring
      _ ≤ 2*(minusStep x*3^(minusCount (minusStep x) t)) := Nat.mul_le_mul_left _ h
      _ = (2*minusStep x)*3^(minusCount (minusStep x) t) := by ring
      _ ≤ (x*3^(x%2))*3^(minusCount (minusStep x) t) := Nat.mul_le_mul_right _ hs
      _ = x*3^(minusCount x (t+1)) := by rw [minusCount,pow_add]; ring

/-- Every source in the reflected interval is in the upper tail, at every scale. -/
theorem reflected_arc_saturated {x k : ℕ} (hx : 0 < x) (hk : 0 < k) (h : x ≤ 2^k) :
    501*(5*k) < 1000*minusCount x (5*k) := by
  have hprod := minus_product x (5*k) hx
  have hp : 2^(5*k) ≤ 2^k*3^(minusCount x (5*k)) := by
    calc
      2^(5*k) ≤ 2^(5*k)*minusRun x (5*k) := Nat.le_mul_of_pos_right _ (minus_run_positive hx _)
      _ ≤ x*3^(minusCount x (5*k)) := hprod
      _ ≤ 2^k*3^(minusCount x (5*k)) := Nat.mul_le_mul_right _ h
  have h4 : (2:ℕ)^(4*k) ≤ 3^(minusCount x (5*k)) := by
    apply Nat.le_of_mul_le_mul_left _ (by positivity : 0 < (2:ℕ)^k)
    rwa [← pow_add,show k+4*k=5*k by omega]
  have cert : (3:ℚ)^501 < 2^800 := by
    exact_mod_cast (by decide : (3:ℕ)^501 < 2^800)
  exact threshold hk (by norm_num : (1:ℚ) ≤ 3) cert (by exact_mod_cast h4)

#print axioms reflected_arc_saturated
#print axioms small_range
#print axioms fifth_clock_needs_high_count

end Collatz.FullProof.Parity
