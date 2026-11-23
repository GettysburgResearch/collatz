import MarkedDensityPotential

/-!
An ordinary obstruction to treating a compact, spatially weighted Green
estimate as a compact resolvent on the same weighted space.  Every source
below is a positive odd unit reaching 5 in one accelerated step and 1 in
two.  Thus the obstruction requires no escaping or unproved orbit.

The Banach-space compactness statement is proved in POTENTIAL_ATTACK.md.
This module checks the complete arithmetic ladder and its exact finite-mass
pushforward, together with the vanishing-input / fixed-output graph witness.
-/

namespace CollatzShell.CriticalPotential

open ForwardSection InverseDensityPotential

def ladder : Nat → Nat
  | 0 => 13
  | j+1 => 64 * ladder j + 21

theorem ladder_unit (j : Nat) : OddUnit (ladder j) := by
  induction j with
  | zero => norm_num [ladder, OddUnit]
  | succ j ih =>
    rcases ih with ⟨hp, ho, hu⟩
    change 0 < 64 * ladder j + 21 ∧
      (64 * ladder j + 21) % 2 = 1 ∧ (64 * ladder j + 21) % 3 ≠ 0
    omega

theorem ladder_equation (j : Nat) :
    3 * ladder j + 1 = 2^(6*j+3) * 5 := by
  induction j with
  | zero => norm_num [ladder]
  | succ j ih =>
    calc
      3 * ladder (j+1) + 1 = 64 * (3 * ladder j + 1) := by
        simp only [ladder]
        ring
      _ = 64 * (2^(6*j+3) * 5) := by rw [ih]
      _ = 2^(6*(j+1)+3) * 5 := by
        rw [show 6*(j+1)+3 = (6*j+3)+6 by omega, pow_add]
        norm_num
        ring

theorem ladder_cofinal (j : Nat) : j + 13 ≤ ladder j := by
  induction j with
  | zero => simp [ladder]
  | succ j ih =>
    simp only [ladder]
    omega

theorem odd_step_ladder (j : Nat) : oddStep (ladder j) = 5 := by
  change ordCompl[2] (3 * ladder j + 1) = 5
  rw [ladder_equation]
  exact Nat.ordCompl_pow_mul_of_not_dvd (6*j+3) Nat.prime_two (by decide)

theorem odd_step_five : oddStep 5 = 1 := by
  change ordCompl[2] (2^4) = 1
  exact Nat.ordCompl_self_pow Nat.prime_two

theorem odd_step_one : oddStep 1 = 1 := by
  change ordCompl[2] (2^2) = 1
  exact Nat.ordCompl_self_pow Nat.prime_two

theorem ladder_reaches_one (j : Nat) : oddOrbit (ladder j) 2 = 1 := by
  simp only [oddOrbit, odd_step_ladder, odd_step_five]

theorem ladder_tail_one (j k : Nat) : oddOrbit (ladder j) (k+2) = 1 := by
  induction k with
  | zero => exact ladder_reaches_one j
  | succ k ih =>
    change oddStep (oddOrbit (ladder j) (k+2)) = 1
    rw [ih, odd_step_one]

theorem ladder_nonperiodic (j k : Nat) (positive : 0 < k) :
    oddOrbit (ladder j) k ≠ ladder j := by
  have large := ladder_cofinal j
  cases k with
  | zero => omega
  | succ k =>
    cases k with
    | zero => simp only [oddOrbit, odd_step_ladder]; omega
    | succ k =>
      rw [show k+1+1 = k+2 by omega, ladder_tail_one]
      omega

noncomputable def push (a : Nat →₀ ℝ) : Nat →₀ ℝ :=
  a.mapDomain oddStep

noncomputable def weightedSize (w : Nat → ℝ) (a : Nat →₀ ℝ) : ℝ :=
  a.sum (fun n x => w n * |x|)

theorem weighted_single (w : Nat → ℝ) (n : Nat) :
    weightedSize w (Finsupp.single n 1) = w n := by
  simp [weightedSize]

theorem push_ladder_atom (j : Nat) :
    push (Finsupp.single (ladder j) 1) = Finsupp.single 5 1 := by
  simp [push, odd_step_ladder]

/-- These are the finite-support graph pairs witnessing nonclosability in
every spatial weight vanishing at infinity. The limit in the output is the
same nonzero mass at 5, although the input size tends to zero. -/
theorem vanishing_input_fixed_output
    (w : Nat → ℝ)
    (tail : ∀ ε : ℝ, 0 < ε → ∃ M : Nat, ∀ n, M ≤ n → w n < ε) :
    (∀ j : Nat, push (Finsupp.single (ladder j) 1) = Finsupp.single 5 1) ∧
    (∀ ε : ℝ, 0 < ε → ∃ J : Nat, ∀ j, J ≤ j →
      weightedSize w (Finsupp.single (ladder j) 1) < ε) := by
  refine ⟨push_ladder_atom, ?_⟩
  intro ε positive
  obtain ⟨M, hM⟩ := tail ε positive
  refine ⟨M, ?_⟩
  intro j hj
  rw [weighted_single]
  apply hM
  have := ladder_cofinal j
  omega

/-- Even the necessary boundedness inequality for individual source atoms
fails. The obstruction lives in the certified convergent basin of 1. -/
theorem no_weighted_push_bound
    (w : Nat → ℝ) (positive : ∀ n, 0 < w n)
    (tail : ∀ ε : ℝ, 0 < ε → ∃ M : Nat, ∀ n, M ≤ n → w n < ε) :
    ¬ ∃ C : ℝ, 0 ≤ C ∧ ∀ a : Nat →₀ ℝ,
      weightedSize w (push a) ≤ C * weightedSize w a := by
  rintro ⟨C, hC, bound⟩
  have denom : 0 < C+1 := by linarith
  have eps : 0 < w 5 / (C+1) := div_pos (positive 5) denom
  obtain ⟨M, hM⟩ := tail (w 5 / (C+1)) eps
  have small : w (ladder M) < w 5 / (C+1) :=
    hM _ (by have := ladder_cofinal M; omega)
  have short : (C+1) * w (ladder M) < w 5 := by
    simpa only [mul_comm] using (lt_div_iff₀ denom).mp small
  have b := bound (Finsupp.single (ladder M) 1)
  rw [push_ladder_atom, weighted_single, weighted_single] at b
  have pos := positive (ladder M)
  nlinarith

#print axioms ladder_unit
#print axioms ladder_equation
#print axioms ladder_cofinal
#print axioms odd_step_ladder
#print axioms odd_step_five
#print axioms odd_step_one
#print axioms ladder_reaches_one
#print axioms ladder_tail_one
#print axioms ladder_nonperiodic
#print axioms weighted_single
#print axioms push_ladder_atom
#print axioms vanishing_input_fixed_output
#print axioms no_weighted_push_bound

end CollatzShell.CriticalPotential
