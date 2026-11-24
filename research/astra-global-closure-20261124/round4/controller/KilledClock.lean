import Mathlib.Basic.Real.Basic
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Tactic

/-!
Finite moment and common-clock interfaces for ordinary source counts.

The first four declarations adapt the uncompiled candidate in PR201,
3c9e444e3f2f2e457b25cd827dc9a29f981e9de2, KilledMoment.lean.
The final declarations select one clock for a complete fixed family and
retain its actual source-count bounds. No probability estimate, mixing
assertion, or Collatz closure premise is installed as an axiom.
-/
set_option autoImplicit false
namespace Collatz.KilledClock

theorem sqrt_majorant_certificate :
    (1/2 : ℚ) ≤ (71/100)^2 ∧
    (3/2 : ℚ) ≤ (123/100)^2 ∧
    ((71/100 : ℚ) + 123/100)/2 = 97/100 ∧
    (97/100 : ℚ) < 1 := by
  norm_num

theorem survival_block (p : ℕ → ℝ)
    (hp : ∀ i, p (i+1) ≤ p i) (n k : ℕ) :
    p (n+k) ≤ p n := by
  induction k with
  | zero => simp
  | succ k ih =>
    rw [Nat.add_succ]
    exact (hp (n+k)).trans ih

theorem killed_moment_block (m p : ℕ → ℝ) (c b : ℝ)
    (hc0 : 0 ≤ c) (hc1 : c < 1) (hb : 0 ≤ b)
    (hp0 : ∀ i, 0 ≤ p i)
    (hp : ∀ i, p (i+1) ≤ p i)
    (hr : ∀ i, m (i+1) ≤ c*m i+b*p i)
    (n k : ℕ) :
    m (n+k) ≤ c^k*m n + (b/(1-c))*p n := by
  have hd : 0 < 1-c := sub_pos.mpr hc1
  have hcoef : c*(b/(1-c))+b = b/(1-c) := by
    field_simp [ne_of_gt hd]; ring
  induction k with
  | zero =>
    have hnon : 0 ≤ (b/(1-c))*p n :=
      mul_nonneg (div_nonneg hb (le_of_lt hd)) (hp0 n)
    simp only [Nat.add_zero, pow_zero, one_mul]
    linarith
  | succ k ih =>
    have hstep := hr (n+k)
    have hmon := survival_block p hp n k
    calc
      m (n+(k+1)) = m ((n+k)+1) := by rw [Nat.add_assoc]
      _ ≤ c*m (n+k)+b*p (n+k) := hstep
      _ ≤ c*(c^k*m n+(b/(1-c))*p n)+b*p n :=
        add_le_add (mul_le_mul_of_nonneg_left ih hc0)
          (mul_le_mul_of_nonneg_left hmon hb)
      _ = (c^k*c)*m n+(c*(b/(1-c))+b)*p n := by ring
      _ = c^(k+1)*m n+(b/(1-c))*p n := by rw [pow_succ, hcoef]

theorem green_charge (K a p m v : ℝ)
    (hK : 0 ≤ K) (h : v ≤ K*(p+m))
    (hp : p ≤ a) (hm : m ≤ a) :
    v ≤ 2*K*a := by
  calc
    v ≤ K*(p+m) := h
    _ ≤ K*(a+a) := mul_le_mul_of_nonneg_left (add_le_add hp hm) hK
    _ = 2*K*a := by ring

/-- The clock is selected for the sum over the whole family, before
choosing any source or applying an arbitrary eventual-color filter. -/
theorem common_clock {ι ρ : Type*} (I : Finset ι) (R : Finset ρ)
    (hne : I.Nonempty) (cost : ι → ρ → ℝ) (B : ℝ)
    (budget : ∑ i ∈ I, ∑ r ∈ R, cost i r ≤ (I.card : ℝ)*B) :
    ∃ i ∈ I, ∑ r ∈ R, cost i r ≤ B := by
  by_contra! h
  obtain ⟨i, hi⟩ := hne
  have strict : ∑ _i ∈ I, B < ∑ i ∈ I, ∑ r ∈ R, cost i r :=
    Finset.sum_lt_sum (fun j hj => le_of_lt (h j hj)) ⟨i, hi, h i hi⟩
  simp only [Finset.sum_const, nsmul_eq_mul] at strict
  linarith

/-- Preserve the original source multiplicities at that common clock.
The count may already restrict to any selected subpopulation, provided
its displayed finite bound holds at every eligible clock. -/
theorem common_source_clock {ι ρ : Type*} (I : Finset ι) (R : Finset ρ)
    (hne : I.Nonempty) (cost : ι → ρ → ℝ) (count : ι → ℝ)
    (B C E : ℝ) (hC : 0 ≤ C)
    (budget : ∑ i ∈ I, ∑ r ∈ R, cost i r ≤ (I.card : ℝ)*B)
    (transfer : ∀ i ∈ I, count i ≤ C*(∑ r ∈ R, cost i r)+E) :
    ∃ i ∈ I, count i ≤ C*B+E := by
  obtain ⟨i, hi, hcost⟩ := common_clock I R hne cost B budget
  exact ⟨i, hi, (transfer i hi).trans
    (add_le_add (mul_le_mul_of_nonneg_left hcost hC) le_rfl)⟩

#print axioms sqrt_majorant_certificate
#print axioms survival_block
#print axioms killed_moment_block
#print axioms green_charge
#print axioms common_clock
#print axioms common_source_clock
end Collatz.KilledClock
