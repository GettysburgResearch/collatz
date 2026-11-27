import NativeDecay
import NativeTightness

/-!
The actual finite rational extinction criterion is equivalent to Collatz.
This proves the converse implication using reserve decay and finite old
source exhaustion.  It does not establish either equivalent statement.
-/
set_option autoImplicit false
set_option warningAsError true

namespace Collatz.NativeGate

theorem decayRatio_polynomial_bound (k : ℕ) :
    decayRatio^k ≤ 100/((k:ℚ)+100) := by
  induction k with
  | zero => norm_num
  | succ k ih =>
    have hk : (0:ℚ) ≤ k := by positivity
    have h1 : (0:ℚ) < (k:ℚ)+100 := by positivity
    have h2 : (0:ℚ) < (k:ℚ)+101 := by positivity
    calc
      decayRatio^(k+1) = decayRatio*decayRatio^k := by rw [pow_succ]; ring
      _ ≤ decayRatio*(100/((k:ℚ)+100)) :=
        mul_le_mul_of_nonneg_left ih decayRatio_range.1.le
      _ = 99/((k:ℚ)+100) := by norm_num [decayRatio]; ring
      _ ≤ 100/((k:ℚ)+101) := (div_le_div_iff₀ h1 h2).2 (by nlinarith)
      _ = 100/((k+1:ℕ)+100:ℚ) := by push_cast; ring

theorem reserve_small (L : ℕ) (hL : 0 < L) :
    reserve (4800*L) < (L:ℚ)⁻¹ := by
  have h1 := reserve_exponential_bound (4800*L)
  have h2 := decayRatio_polynomial_bound (4800*L)
  have hLq : (0:ℚ) < L := by exact_mod_cast hL
  have hp : (0:ℚ) < 4800*L+100 := by positivity
  have h3 : 48*(100/((4800*L:ℕ)+100:ℚ)) < (L:ℚ)⁻¹ := by
    push_cast
    apply (mul_lt_mul_iff_left₀ (mul_pos hLq hp)).mp
    field_simp
    nlinarith
  linarith

theorem covered_finite_certificate (L k : ℕ) (hL : 0 < L)
    (hsmall : reserve k < (L:ℚ)⁻¹)
    (hcover : ∀ x ∈ candidates k, ReachesOne x) :
    ∀ x, 0 < x → x ≤ L → ReachesOne x := by
  obtain ⟨j, hj⟩ := covered_eventual_mass k hcover
  have hm := hj L
  have hpow := native_cutoff (k+j+L)
  apply finite_certificate L (k+j+L) hL (by omega)
  linarith

theorem universal_implies_extinction (h : Universal) : Extinction := by
  intro L hL
  obtain ⟨n, hn, hm⟩ := universal_eventual_mass h (4800*L)
  refine ⟨n, ?_, lt_of_le_of_lt hm (reserve_small L hL)⟩
  have hpow := native_cutoff n
  omega

theorem collatz_iff_extinction : Universal ↔ Extinction :=
  ⟨universal_implies_extinction, extinction_implies_collatz⟩

#print axioms reserve_exponential_bound
#print axioms future_highMass_budget
#print axioms covered_finite_certificate
#print axioms collatz_iff_extinction

end Collatz.NativeGate
