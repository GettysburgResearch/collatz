import MarkedDensityPotential
import Mathlib.Algebra.Order.BigOperators.Ring.Finset
import Mathlib.Topology.Algebra.InfiniteSum.Basic

/-!
Finite arithmetic and energy core for the ordinary contact analysis.
The canonical analytic inputs are hypotheses, never new axioms.  The
infinite first-contact construction and the general Lp residue theorem
are written in ORDINARY_BOUNDARY.md.
-/

namespace CollatzShell.OrdinaryBoundary

open ForwardSection InverseDensityPotential Finset Filter

def parentsOfSeventeen : Nat → Nat
  | 0 => 11
  | j+1 => 64 * parentsOfSeventeen j + 21

theorem parents_unit (j : Nat) : OddUnit (parentsOfSeventeen j) := by
  induction j with
  | zero => norm_num [parentsOfSeventeen, OddUnit]
  | succ j ih =>
    rcases ih with ⟨hp, ho, hu⟩
    change 0 < 64 * parentsOfSeventeen j + 21 ∧
      (64 * parentsOfSeventeen j + 21) % 2 = 1 ∧
      (64 * parentsOfSeventeen j + 21) % 3 ≠ 0
    omega

theorem parents_equation (j : Nat) :
    3 * parentsOfSeventeen j + 1 = 2^(6*j+1) * 17 := by
  induction j with
  | zero => norm_num [parentsOfSeventeen]
  | succ j ih =>
    calc
      3 * parentsOfSeventeen (j+1) + 1 =
          64 * (3 * parentsOfSeventeen j + 1) := by
        simp only [parentsOfSeventeen]
        ring
      _ = 64 * (2^(6*j+1) * 17) := by rw [ih]
      _ = 2^(6*(j+1)+1) * 17 := by
        rw [show 6*(j+1)+1 = (6*j+1)+6 by omega, pow_add]
        norm_num
        ring

theorem parents_strictMono : StrictMono parentsOfSeventeen := by
  apply strictMono_nat_of_lt_succ
  intro j
  simp only [parentsOfSeventeen]
  omega

theorem parents_odd_step (j : Nat) : oddStep (parentsOfSeventeen j) = 17 := by
  change ordCompl[2] (3 * parentsOfSeventeen j + 1) = 17
  rw [parents_equation]
  exact Nat.ordCompl_pow_mul_of_not_dvd (6*j+1) Nat.prime_two (by decide)

theorem seventeen_in_basin : Basin 17 := by
  exact ⟨9, by decide⟩

theorem seven_eleven_seventeen : oddStep 7 = 11 ∧ oddStep 11 = 17 := by
  constructor
  · change ordCompl[2] (2^1 * 11) = 11
    exact Nat.ordCompl_pow_mul_of_not_dvd 1 Nat.prime_two (by decide)
  · change ordCompl[2] (2^1 * 17) = 17
    exact Nat.ordCompl_pow_mul_of_not_dvd 1 Nat.prime_two (by decide)

/-- Any critical excessive majorant bounded below by one is outside
the threshold-two contact set at the concrete convergent root 17. -/
theorem seventeen_not_contact (V : Nat → ℝ)
    (floor : 1 ≤ V 7)
    (edgeSeven : 3 * V 7 ≤ 2 * V 11)
    (edgeEleven : 3 * V 11 ≤ 2 * V 17) :
    (9 : ℝ) / 4 ≤ V 17 ∧ 2 < V 17 := by
  constructor <;> linarith

/-- The finite quadratic core of the occupation-dominated source bound.
The factor B is the exact upper bound on total original occupation at
this endpoint divided by its ordinary harmonic reference mass. -/
theorem occupation_quadratic_bound {ι : Type*} (S : Finset ι)
    (w f : ι → ℝ) (nu B : ℝ)
    (hw : ∀ i ∈ S, 0 ≤ w i) (hn : 0 < nu)
    (reference : ∑ i ∈ S, w i ≤ B * nu) :
    (∑ i ∈ S, w i * f i)^2 / nu ≤
      B * ∑ i ∈ S, w i * (f i)^2 := by
  have cost_nonneg : 0 ≤ ∑ i ∈ S, w i * (f i)^2 :=
    sum_nonneg (fun i hi => mul_nonneg (hw i hi) (sq_nonneg _))
  have cs := sum_sq_le_sum_mul_sum_of_sq_le_mul S
    hw
    (fun i hi => mul_nonneg (hw i hi) (sq_nonneg (f i)))
    (fun i _ => show (w i * f i)^2 ≤ w i * (w i * (f i)^2) by nlinarith [sq_nonneg (w i * f i)])
  apply (div_le_iff₀ hn).mpr
  calc
    (∑ i ∈ S, w i * f i)^2 ≤
        (∑ i ∈ S, w i) * ∑ i ∈ S, w i * (f i)^2 := cs
    _ ≤ (B * nu) * ∑ i ∈ S, w i * (f i)^2 :=
      mul_le_mul_of_nonneg_right reference cost_nonneg
    _ = (B * ∑ i ∈ S, w i * (f i)^2) * nu := by ring

/-- The canonical immigration weight charges a uniform positive amount
for every harmonic first-contact atom, regardless of its height. -/
theorem contact_atom_cost (x h nu d gamma : ℝ)
    (hh : 0 < h) (hd : 0 < d)
    (floor : gamma ≤ x * h) (domination : h ≤ nu)
    (immigration : (3*x+1)*d = h) :
    3*gamma ≤ nu^2 / d := by
  apply (le_div_iff₀ hd).mpr
  have hn : 0 < nu := lt_of_lt_of_le hh domination
  have hf : 3*gamma*d ≤ 3*x*h*d := by nlinarith [mul_nonneg (sub_nonneg.mpr floor) hd.le]
  have he : 3*x*h*d + h*d = h^2 := by nlinarith [congrArg (fun z : ℝ => z*h) immigration]
  nlinarith [mul_nonneg hh.le hd.le, sq_nonneg (nu-h)]

theorem finite_contact_cost {ι : Type*} (S : Finset ι)
    (cost : ι → ℝ) (gamma : ℝ)
    (lower : ∀ i ∈ S, 3*gamma ≤ cost i) :
    (S.card : ℝ) * (3*gamma) ≤ ∑ i ∈ S, cost i := by
  simpa using sum_le_sum lower

/-- A sequence of distinct first-contact atoms has divergent immigration
energy as soon as each atom obeys the uniform cost bound. Distinctness is
needed when identifying this sequence with a subset of the global cutset;
the analytic sequence conclusion itself only uses the displayed bound. -/
theorem contact_cost_not_summable (cost : Nat → ℝ) (gamma : ℝ)
    (positive : 0 < gamma) (lower : ∀ j, 3*gamma ≤ cost j) :
    ¬ Summable cost := by
  intro hs
  have hlim : 3*gamma ≤ 0 :=
    ge_of_tendsto hs.tendsto_atTop_zero (Eventually.of_forall lower)
  linarith

#print axioms parents_unit
#print axioms parents_equation
#print axioms parents_strictMono
#print axioms parents_odd_step
#print axioms seventeen_in_basin
#print axioms seven_eleven_seventeen
#print axioms seventeen_not_contact
#print axioms occupation_quadratic_bound
#print axioms contact_atom_cost
#print axioms finite_contact_cost
#print axioms contact_cost_not_summable

end CollatzShell.OrdinaryBoundary
