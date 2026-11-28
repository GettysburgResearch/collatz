import NativeTransfer

/-!
Exponential decay of the native reserve and an effective separation of
old ordinary sources from every later birth.  This is a finite rational
argument on the actual candidate sets, not a stationary source model.
-/
set_option autoImplicit false
set_option warningAsError true

namespace Collatz.NativeGate

def tilt : ℚ := 25/24
def decayRatio : ℚ := 99/100
def exponentialWeight (k x : ℕ) : ℚ := tilt^(7*odds x k)/tilt^(4*k)
def exponentialReserve (k : ℕ) : ℚ :=
  (∑ x ∈ candidates k, exponentialWeight k x)/(2:ℚ)^k

theorem tilt_positive : 0 < tilt := by norm_num [tilt]
theorem decayRatio_range : 0 < decayRatio ∧ decayRatio < 1 := by
  norm_num [decayRatio]

theorem exponentialWeight_positive (k x : ℕ) : 0 < exponentialWeight k x := by
  unfold exponentialWeight
  exact div_pos (pow_pos tilt_positive _) (pow_pos tilt_positive _)

theorem exponentialWeight_lift (k x : ℕ) :
    exponentialWeight k (x+2^k) = exponentialWeight k x := by
  have h := (cylinder_lift x k 1).1
  simp only [Nat.mul_one] at h
  simp only [exponentialWeight, h]

theorem exponentialWeight_next (k x : ℕ) :
    exponentialWeight (k+1) x =
      exponentialWeight k x * (tilt^(7*(orbit x k % 2))/tilt^4) := by
  unfold exponentialWeight
  rw [odds, Nat.mul_add, pow_add,
    show 4*(k+1) = 4*k+4 by omega, pow_add]
  ring

theorem exponential_children (k x : ℕ) :
    exponentialWeight (k+1) x + exponentialWeight (k+1) (x+2^k)
      ≤ 2*decayRatio*exponentialWeight k x := by
  have hp := sibling_parity k x
  have hp0 : orbit x k % 2 = 0 ∨ orbit x k % 2 = 1 := by omega
  have hw := (exponentialWeight_positive k x).le
  rw [exponentialWeight_next, exponentialWeight_next, exponentialWeight_lift]
  rcases hp0 with hp0 | hp0
  · have hp1 : orbit (x+2^k) k % 2 = 1 := by omega
    simp only [hp0, hp1]
    norm_num [tilt, decayRatio]
    nlinarith
  · have hp1 : orbit (x+2^k) k % 2 = 0 := by omega
    simp only [hp0, hp1]
    norm_num [tilt, decayRatio]
    nlinarith

theorem exponentialReserve_step (k : ℕ) :
    exponentialReserve (k+1) ≤ decayRatio*exponentialReserve k := by
  have hs : (∑ x ∈ candidates (k+1), exponentialWeight (k+1) x) ≤
      2*decayRatio*(∑ x ∈ candidates k, exponentialWeight k x) := by
    rw [sum_children, Finset.mul_sum]
    apply Finset.sum_le_sum
    intro x _
    have h0 := (exponentialWeight_positive (k+1) x).le
    have h1 := (exponentialWeight_positive (k+1) (x+2^k)).le
    have h := exponential_children k x
    split_ifs <;> linarith
  unfold exponentialReserve
  rw [pow_succ]
  have hp : (0:ℚ) < 2^k := by positivity
  apply (mul_le_mul_iff_left₀ (by positivity : (0:ℚ) < 2^k*2)).mp
  calc
    _ = ∑ x ∈ candidates (k+1), exponentialWeight (k+1) x := by field_simp
    _ ≤ _ := hs
    _ = _ := by field_simp

theorem exponentialReserve_bound (k : ℕ) : exponentialReserve k ≤ decayRatio^k := by
  induction k with
  | zero =>
    have hc : candidates 0 = {1} := by decide
    simp [exponentialReserve, exponentialWeight, odds, hc]
  | succ k ih =>
    calc
      exponentialReserve (k+1) ≤ decayRatio*exponentialReserve k :=
        exponentialReserve_step k
      _ ≤ decayRatio*decayRatio^k := mul_le_mul_of_nonneg_left ih decayRatio_range.1.le
      _ = decayRatio^(k+1) := by rw [pow_succ]; ring

theorem linear_le_tilt (d : ℕ) : (d:ℚ)+24 ≤ 24*tilt^d := by
  induction d with
  | zero => norm_num
  | succ d ih =>
    rw [pow_succ]
    have hp : (1:ℚ) ≤ tilt^d := by
      exact one_le_pow₀ (by norm_num [tilt])
    norm_num [tilt] at *
    nlinarith

theorem reserveWeight_le_exponential {k x : ℕ} (hx : x ∈ candidates k) :
    reserveWeight k x ≤ 48*exponentialWeight k x := by
  have hg := (candidate_bounds hx).2.2 k (by omega)
  obtain ⟨d, hd⟩ := Nat.exists_eq_add_of_le hg
  have he : exponentialWeight k x = tilt^d := by
    unfold exponentialWeight
    rw [hd, pow_add]
    have hne : tilt^(4*k) ≠ 0 := ne_of_gt (pow_pos tilt_positive _)
    field_simp
  have hdebt : debt k x = (d:ℚ) := by
    unfold debt
    have hc : (7:ℚ)*odds x k = 4*k+d := by exact_mod_cast hd
    linarith
  rw [reserveWeight, hdebt, he]
  have h := linear_le_tilt d
  linarith

theorem reserve_exponential_bound (k : ℕ) : reserve k ≤ 48*decayRatio^k := by
  have hs : (∑ x ∈ candidates k, reserveWeight k x) ≤
      48*(∑ x ∈ candidates k, exponentialWeight k x) := by
    rw [Finset.mul_sum]
    exact Finset.sum_le_sum (fun _ hx => reserveWeight_le_exponential hx)
  have hr : reserve k ≤ 48*exponentialReserve k := by
    unfold reserve exponentialReserve
    have hp : (0:ℚ) < 2^k := by positivity
    apply (mul_le_mul_iff_left₀ hp).mp
    calc
      _ = ∑ x ∈ candidates k, reserveWeight k x := by field_simp
      _ ≤ _ := hs
      _ = _ := by field_simp
  have he := exponentialReserve_bound k
  linarith

end Collatz.NativeGate
