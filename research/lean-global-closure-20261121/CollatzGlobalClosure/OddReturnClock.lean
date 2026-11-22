import CollatzGlobalClosure.InverseBudget
import CollatzGlobalClosure.MergerClockRigidity

/-!
# An odd-count budget for a multiplicative return

If an actual ordinary trajectory sends `m*n` back to `n`, the exact
quotient theorem bounds the source using the number of odd inputs, not
its possibly much larger total shortcut clock.  The multiplier-five
case supplies the odd-clock estimate needed by the asynchronous channel
calculation.  No convergence or harmonic-reference hypothesis is used.
-/

set_option autoImplicit false

namespace CollatzOddReturnClock

open CollatzEndpointSteering CollatzInverseBudget CollatzMergerClockRigidity

/-- The only arithmetic nonresonance needed for this return is inequality
of its total dyadic denominator and its leading ternary numerator. -/
theorem return_odd_count_bound
    (h n m : Nat) (positive : 0<n)
    (nonresonant : 2^h≠m*3^(odds h (m*n)))
    (hit : orbit h (m*n)=n) : n<m*9^(odds h (m*n)) := by
  let a := odds h (m*n)
  let v := n/3^a
  have affine := actual_affine_identity h (m*n)
  rw [hit] at affine
  have numerator : m*3^a≤2^h := by
    by_cases small : 2^h<m*3^a
    · have strict := Nat.mul_lt_mul_of_pos_right small positive
      have form : 3^(odds h (m*n))*(m*n)=(m*3^a)*n := by
        dsimp [a]
        ac_rfl
      rw [form] at affine
      omega
    · omega
  have strictNumerator : m*3^a+1≤2^h := by
    change 2^h≠m*3^a at nonresonant
    omega
  have quotient := normalized_quotient h (m*n)
  rw [hit] at quotient
  have lower : 2^h*v≤m*n := by
    have bound := Nat.div_mul_le_self (m*n) (2^h)
    rw [← quotient] at bound
    simpa only [v,a,Nat.mul_comm] using bound
  have upper : n<3^a*(v+1) := by
    have modulus : 0<3^a := Nat.pow_pos (by decide)
    have remainder := Nat.mod_lt n modulus
    have decomposition := Nat.mod_add_div n (3^a)
    dsimp [v]
    rw [Nat.mul_add,Nat.mul_one]
    omega
  have multiplier : 0<m := by
    by_cases zero : m=0
    · subst m
      have zeroSource : ∀ k : Nat, orbit k 0=0 := by
        intro k
        induction k with
        | zero => rfl
        | succ k ih => simpa [orbit,step] using ih
      simp only [Nat.zero_mul] at hit
      rw [zeroSource h] at hit
      omega
    · omega
  have upperTimes := Nat.mul_lt_mul_of_pos_left upper multiplier
  have denominatorTimes := Nat.mul_le_mul_right v strictNumerator
  have upperForm : m*(3^a*(v+1))=(m*3^a)*v+m*3^a := by grind
  rw [upperForm] at upperTimes
  rw [Nat.add_mul,Nat.one_mul] at denominatorTimes
  have smallQuotient : v<m*3^a := by omega
  have finalScale := Nat.mul_le_mul_left (3^a) (show v+1≤m*3^a by omega)
  have finalForm : 3^a*(m*3^a)=m*9^a := by
    rw [show (9:Nat)=3*3 by decide,Nat.mul_pow]
    ac_rfl
  rw [finalForm] at finalScale
  exact Nat.lt_of_lt_of_le upper finalScale

theorem coprime_factor_return_odd_count_bound
    (h n m d : Nat) (positive : 0<n)
    (nontrivial : 1<d) (factor : d∣m) (two : Nat.Coprime d 2)
    (hit : orbit h (m*n)=n) : n<m*9^(odds h (m*n)) := by
  apply return_odd_count_bound h n m positive _ hit
  intro equation
  have coprime : Nat.Coprime d (2^h) := two.pow_right h
  have divides : d∣2^h := by
    obtain ⟨k,factor⟩ := factor
    refine ⟨k*3^(odds h (m*n)),?_⟩
    rw [equation,factor]
    ac_rfl
  have := coprime.eq_one_of_dvd divides
  omega

/-- Any ordinary return from five times a positive source uses more than
log base nine of `n/5` odd inputs, even if its halving runs are unbounded. -/
theorem five_return_odd_count_bound
    (h n : Nat) (positive : 0<n) (hit : orbit h (5*n)=n) :
    n<5*9^(odds h (5*n)) := by
  exact coprime_factor_return_odd_count_bound h n 5 5 positive
    (by decide) (Nat.dvd_refl _) (by decide) hit

theorem no_five_return_within_odd_budget
    (h J n : Nat) (positive : 0<n) (large : 5*9^J≤n)
    (budget : odds h (5*n)≤J) : orbit h (5*n)≠n := by
  intro hit
  have bound := five_return_odd_count_bound h n positive hit
  have powers : 9^(odds h (5*n))≤9^J :=
    Nat.pow_le_pow_of_le (by decide) budget
  have scaled := Nat.mul_le_mul_left 5 powers
  omega

end CollatzOddReturnClock

#print axioms CollatzOddReturnClock.return_odd_count_bound
#print axioms CollatzOddReturnClock.coprime_factor_return_odd_count_bound
#print axioms CollatzOddReturnClock.five_return_odd_count_bound
#print axioms CollatzOddReturnClock.no_five_return_within_odd_budget
