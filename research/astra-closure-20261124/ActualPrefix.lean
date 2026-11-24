import ActualCarry

/-! A fixed-source inequality with the ordinary multiplicative correction retained exactly. -/
namespace Collatz.StrictCarry.Actual
open Collatz.CarryTowerRoundTen.ActualScalar
open Collatz.StrictCarry

set_option autoImplicit false

noncomputable def correction (q n : ℕ) : ℝ :=
  ∑ i ∈ Finset.range n, Real.log (1 + 1/(3*(orbit q i : ℝ)))

private theorem physical_step (q : ℕ) (hq : 0 < q) :
    Real.log (oddMap q) + (gap q : ℝ)*Real.log 2 =
      Real.log q + Real.log 3 + Real.log (1+1/(3*(q : ℝ))) := by
  have h : (q : ℝ) > 0 := by exact_mod_cast hq
  have hu : (oddMap q : ℝ) > 0 := by exact_mod_cast oddMap_pos q
  have eq : (2 : ℝ)^(gap q) * oddMap q = (q : ℝ)*3*(1+1/(3*(q : ℝ))) := by
    have hx : (2 : ℝ)^(gap q) * oddMap q = 3*(q : ℝ)+1 := by exact_mod_cast complete_step q
    rw [hx]
    field_simp
  have hx := congrArg Real.log eq
  rw [Real.log_mul (by positivity) hu.ne', Real.log_pow,
    Real.log_mul (by positivity) (by positivity), Real.log_mul h.ne' (by norm_num)] at hx
  linarith

theorem physical_prefix (q n : ℕ) (hq : 0 < q) :
    Real.log (orbit q n) + ((∑ i ∈ Finset.range n, gap (orbit q i) : ℕ) : ℝ)*Real.log 2 =
    Real.log q + (n : ℝ)*Real.log 3 + correction q n := by
  induction n with
  | zero => simp [orbit, correction]
  | succ n ih =>
    have hs := physical_step (orbit q n) (orbit_pos q n hq)
    rw [Finset.sum_range_succ]
    change Real.log (oddMap (orbit q n)) + _ = _
    simp only [correction, Finset.sum_range_succ, Nat.cast_add, Nat.cast_succ] at ih ⊢
    linarith

/-- The ordinary log expansion retains an additive charge on every strict edge.
The physical correction is a finite sum on the same orbit. -/
theorem strict_physical_prefix (q n : ℕ) (hq : 0 < q) (ho : Odd q) :
    let J := ∑ i ∈ Finset.range n, strictEdge (carry (orbit q i)) (carry (orbit q (i+1)))
    let B := ∑ i ∈ Finset.range n, canonical (orbit q i)
    (Real.log (orbit q n) - Real.log q - correction q n)*Real.log 3 +
      (J : ℝ)*(Real.log 4 - Real.log 3)*Real.log 2 +
      2*Real.log (carry q + 1 : ℕ)*Real.log 2 ≤
    ((n : ℝ)*Real.log 3 - (B : ℝ)*Real.log 2)*Real.log 3 +
      2*Real.log (carry (orbit q n) + 1 : ℕ)*Real.log 2 := by
  dsimp only
  let J := ∑ i ∈ Finset.range n, strictEdge (carry (orbit q i)) (carry (orbit q (i+1)))
  let B := ∑ i ∈ Finset.range n, canonical (orbit q i)
  let A := ∑ i ∈ Finset.range n, gap (orbit q i)
  have hc : (4 : ℝ)^J*3^B*(carry q+1 : ℕ)^2 ≤
      3^J*3^A*(carry (orbit q n)+1 : ℕ)^2 := by
    exact_mod_cast (by simpa [J,B,A,orbit] using actual_interval_slack q 0 n hq ho :
      4^J*3^B*(carry q+1)^2 ≤ 3^J*3^A*(carry (orbit q n)+1)^2)
  have hl := Real.log_le_log (by positivity) hc
  repeat rw [Real.log_mul (by positivity) (by positivity)] at hl
  simp only [Real.log_pow] at hl
  have hd := mul_le_mul_of_nonneg_right hl (Real.log_nonneg (by norm_num : (1:ℝ) ≤ 2))
  have hp := congrArg (fun x : ℝ => x * Real.log 3) (physical_prefix q n hq)
  change (Real.log (orbit q n) - Real.log q - correction q n)*Real.log 3 +
      (J : ℝ)*(Real.log 4 - Real.log 3)*Real.log 2 +
      2*Real.log (carry q + 1 : ℕ)*Real.log 2 ≤
    ((n : ℝ)*Real.log 3 - (B : ℝ)*Real.log 2)*Real.log 3 +
      2*Real.log (carry (orbit q n) + 1 : ℕ)*Real.log 2
  change (Real.log (orbit q n) + (A : ℝ)*Real.log 2)*Real.log 3 = _ at hp
  push_cast at hd ⊢
  nlinarith only [hp,hd]

#print axioms physical_prefix
#print axioms strict_physical_prefix
end Collatz.StrictCarry.Actual
