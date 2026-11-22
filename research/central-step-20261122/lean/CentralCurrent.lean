import InverseDensityPotential
import Mathlib.Algebra.BigOperators.Ring.Finset

/-!
Exact arithmetic and the finite pair-clock identity used by the central
boundary attack.  These results do not assert the missing canonical sibling
lower bound, any infinite analytic estimate, or universal convergence.
-/

namespace CollatzShell.CentralCurrent

open ForwardSection InverseDensityPotential Finset

/-- A unit-preserving family of distinct actual siblings. -/
def sibling (n : Nat) : Nat → Nat
  | 0 => n
  | j+1 => 64 * sibling n j + 21

private theorem sibling_equation (n j : Nat) :
    3 * sibling n j + 1 = 2^(6*j) * (3*n+1) := by
  induction j with
  | zero => simp [sibling]
  | succ j ih =>
    calc
      3 * sibling n (j+1) + 1 = 64 * (3 * sibling n j + 1) := by
        simp only [sibling]
        ring
      _ = 64 * (2^(6*j) * (3*n+1)) := by rw [ih]
      _ = 2^(6*(j+1)) * (3*n+1) := by
        rw [show 6*(j+1) = 6*j+6 by omega, pow_add]
        norm_num
        ring

/-- Every member is an odd ternary unit, the family is strictly increasing,
and every member has exactly the same accelerated ordinary successor. -/
theorem actual_sibling_family {n : Nat} (hn : OddUnit n) :
    (∀ j, OddUnit (sibling n j)) ∧ StrictMono (sibling n) ∧
    (∀ j, oddStep (sibling n j) = oddStep n) := by
  refine ⟨?_, ?_, ?_⟩
  · intro j
    induction j with
    | zero => exact hn
    | succ j ih =>
      rcases ih with ⟨hp, ho, hu⟩
      change 0 < 64 * sibling n j + 21 ∧
        (64 * sibling n j + 21) % 2 = 1 ∧
        (64 * sibling n j + 21) % 3 ≠ 0
      omega
  · apply strictMono_nat_of_lt_succ
    intro j
    simp only [sibling]
    omega
  · intro j
    change ordCompl[2] (3 * sibling n j + 1) = oddStep n
    rw [sibling_equation, ← odd_step_split n, ← Nat.mul_assoc, ← pow_add]
    apply Nat.ordCompl_pow_mul_of_not_dvd _ Nat.prime_two
    have ho := (odd_step_unit n).2.1
    omega

/-- Identical inverse-word lifting to the first sibling fails after depth
one. The equations retain the complete affine word constant; no asymptotic
leading term is substituted for an actual inverse word. -/
theorem no_identical_word_lift {r A q x y c : Nat} (hr : 2 ≤ r)
    (first : 3^r*x+c=2^A*q)
    (second : 3^r*y+c=2^A*(64*q+21)) : False := by
  have h9 : 9 ∣ 3^r := by
    have h := Nat.pow_dvd_pow 3 hr
    norm_num at h ⊢
    exact h
  have hx : 3^r*x % 9 = 0 := Nat.mod_eq_zero_of_dvd (dvd_mul_of_dvd_left h9 x)
  have hy : 3^r*y % 9 = 0 := Nat.mod_eq_zero_of_dvd (dvd_mul_of_dvd_left h9 y)
  have relation : 3^r*y = 64*(3^r*x)+63*c+21*2^A := by
    nlinarith [first, second]
  have residue := congrArg (fun z : Nat => z % 9) relation
  have h64 : (64*(3^r*x)) % 9 = 0 := by omega
  have h63 : (63*c) % 9 = 0 := by omega
  simp only [Nat.add_mod, Nat.mod_mod, h64, h63, hy,
    Nat.zero_add, Nat.zero_mod] at residue
  have hpow : 2^A % 3 ≠ 0 := by
    intro h
    have hp : 3 ∣ 2^A := Nat.dvd_of_mod_eq_zero h
    have h2 : 3 ∣ 2 := (Nat.prime_three.dvd_of_dvd_pow hp)
    omega
  omega

/-- Finite-source pair-clock identity.  The two adjacent offsets differ
exactly by pairs with the same ordinary clock. This is the algebraic core
of the infinite boundary formula, not a formalization of its limits. -/
theorem pair_clock_split {α : Type*} (S : Finset α) (h : α → Int) (w : α → ℝ) :
    let past := ∑ x ∈ S, ∑ y ∈ S, if h x < h y then w x*w y else 0
    let sync := ∑ x ∈ S, ∑ y ∈ S, if h x = h y then w x*w y else 0
    let inclusive := ∑ x ∈ S, ∑ y ∈ S, if h x ≤ h y then w x*w y else 0
    2*past = (∑ x ∈ S, w x)^2-sync ∧
      2*inclusive = (∑ x ∈ S, w x)^2+sync := by
  dsimp
  let p : ℝ := ∑ x ∈ S, ∑ y ∈ S, if h x < h y then w x*w y else 0
  let e : ℝ := ∑ x ∈ S, ∑ y ∈ S, if h x = h y then w x*w y else 0
  have swap : (∑ x ∈ S, ∑ y ∈ S, if h y < h x then w x*w y else 0) = p := by
    rw [Finset.sum_comm]
    apply sum_congr rfl
    intro x hx
    apply sum_congr rfl
    intro y hy
    by_cases hh : h x < h y <;> simp [hh, mul_comm]
  have total : (∑ x ∈ S, w x)^2 = p+e+p := by
    rw [pow_two, sum_mul_sum]
    have point (x y : α) : w x*w y =
        (if h x < h y then w x*w y else 0) +
        (if h x = h y then w x*w y else 0) +
        (if h y < h x then w x*w y else 0) := by
      rcases lt_trichotomy (h x) (h y) with hh | hh | hh
      · simp [hh, ne_of_lt hh, not_lt_of_ge (le_of_lt hh)]
      · simp [hh]
      · simp [hh, ne_of_gt hh, not_lt_of_ge (le_of_lt hh)]
    calc
      (∑ x ∈ S, ∑ y ∈ S, w x*w y) =
          ∑ x ∈ S, ∑ y ∈ S,
            ((if h x < h y then w x*w y else 0) +
             (if h x = h y then w x*w y else 0) +
             (if h y < h x then w x*w y else 0)) := by
        apply sum_congr rfl
        intro x hx
        apply sum_congr rfl
        intro y hy
        exact point x y
      _ = p+e+(∑ x ∈ S, ∑ y ∈ S, if h y < h x then w x*w y else 0) := by
        simp only [sum_add_distrib]
        rfl
      _ = p+e+p := by rw [swap]
  have inc : (∑ x ∈ S, ∑ y ∈ S, if h x ≤ h y then w x*w y else 0) = p+e := by
    have point (x y : α) : (if h x ≤ h y then w x*w y else 0) =
        (if h x < h y then w x*w y else 0) +
        (if h x = h y then w x*w y else 0) := by
      rcases lt_trichotomy (h x) (h y) with hh | hh | hh
      · simp [hh, le_of_lt hh, ne_of_lt hh]
      · simp [hh]
      · simp [not_le_of_gt hh, ne_of_gt hh, not_lt_of_ge (le_of_lt hh)]
    simp_rw [point, sum_add_distrib]
    rfl
  change 2*p = (∑ x ∈ S, w x)^2-e ∧ _
  rw [inc]
  constructor <;> linarith

#print axioms actual_sibling_family
#print axioms no_identical_word_lift
#print axioms pair_clock_split

end CollatzShell.CentralCurrent
