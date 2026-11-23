import Mathlib.Topology.Algebra.InfiniteSum.ENNReal
import Mathlib.Topology.Algebra.InfiniteSum.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

/-!
An abstract least excessive majorant cannot contain a nonnegative
subharmonic spike that fits strictly inside its obstacle slack.

The countable-kernel lemmas justify subtraction under the parent sum from
the same finite excessive majorant. No Collatz convergence hypothesis is
present. The analytic construction of that majorant is an explicit input.
-/

namespace CollatzPotential

structure LeastMajorant {ι : Type*}
    (P : (ι → ℝ) → ι → ℝ) (b V : ι → ℝ) : Prop where
  obstacle_nonneg : ∀ x, 0 ≤ b x
  above : ∀ x, b x ≤ V x
  excessive : ∀ x, P V x ≤ V x
  /-- Only dominated competitors are needed. For a real-valued `tsum`
  kernel they are automatically summable when the parent sum of `V` is
  summable; no nonsummable real `tsum` is treated as an actual zero sum. -/
  minimal : ∀ W : ι → ℝ,
    (∀ x, b x ≤ W x) → (∀ x, W x ≤ V x) →
    (∀ x, P W x ≤ W x) → ∀ x, V x ≤ W x

theorem no_slack_subharmonic {ι : Type*}
    {P : (ι → ℝ) → ι → ℝ} {b V φ : ι → ℝ} {δ : ℝ}
    (hV : LeastMajorant P b V) (hδ : 0 < δ)
    (nonneg : ∀ x, 0 ≤ φ x)
    (subharmonic : ∀ x, φ x ≤ P φ x)
    (slack : ∀ x, δ * φ x ≤ V x - b x)
    (subtract : ∀ x,
      P (fun y => V y - δ * φ y) x = P V x - δ * P φ x) :
    ∀ x, φ x = 0 := by
  let W : ι → ℝ := fun x => V x - δ * φ x
  have above : ∀ x, b x ≤ W x := by
    intro x
    dsimp [W]
    linarith [slack x]
  have excessive : ∀ x, P W x ≤ W x := by
    intro x
    change P (fun y => V y - δ * φ y) x ≤ V x - δ * φ x
    rw [subtract x]
    have hs := mul_le_mul_of_nonneg_left (subharmonic x) hδ.le
    linarith [hV.excessive x]
  have below : ∀ x, W x ≤ V x := by
    intro x
    dsimp [W]
    exact sub_le_self _ (mul_nonneg hδ.le (nonneg x))
  have minimal := hV.minimal W above below excessive
  intro x
  have hm := minimal x
  dsimp [W] at hm
  have nonpos : φ x ≤ 0 := by nlinarith
  exact le_antisymm nonpos (nonneg x)

theorem relative_slack_bound {v p ε : ℝ}
    (hε : 0 < ε) (hv : 1 + ε ≤ v) (hp : p ≤ v) :
    ε / (1 + ε) * p ≤ v - 1 := by
  have den : 0 < 1 + ε := by linarith
  rw [show ε / (1 + ε) * p = (ε * p) / (1 + ε) by ring]
  apply (div_le_iff₀ den).mpr
  have scaled := mul_le_mul_of_nonneg_left hp hε.le
  nlinarith

noncomputable def unitObstacle {ι : Type*} (unit : ι → Prop) : ι → ℝ := by
  classical
  exact fun x => if unit x then 1 else 0

/-- A killed fixed point supported a positive distance above the unit
obstacle vanishes. Its support can be an entire inverse boundary, rather
than one inverse ray. -/
theorem no_killed_fixed_point {ι : Type*}
    {P : (ι → ℝ) → ι → ℝ} {unit : ι → Prop} {V φ : ι → ℝ} {ε : ℝ}
    (hV : LeastMajorant P (unitObstacle unit) V) (hε : 0 < ε)
    (nonneg : ∀ x, 0 ≤ φ x) (dominated : ∀ x, φ x ≤ V x)
    (parent_nonneg : ∀ x, 0 ≤ P φ x)
    (fixed : ∀ x, unit x ∧ 1 + ε < V x → P φ x = φ x)
    (support : ∀ x, ¬ (unit x ∧ 1 + ε < V x) → φ x = 0)
    (subtract : ∀ x,
      P (fun y => V y - (ε / (1 + ε)) * φ y) x =
        P V x - (ε / (1 + ε)) * P φ x) :
    ∀ x, φ x = 0 := by
  classical
  apply no_slack_subharmonic hV (by positivity : 0 < ε / (1 + ε)) nonneg
  · intro x
    by_cases hx : unit x ∧ 1 + ε < V x
    · exact (fixed x hx).ge
    · rw [support x hx]
      exact parent_nonneg x
  · intro x
    by_cases hx : unit x ∧ 1 + ε < V x
    · simp only [unitObstacle, ite_eq_left hx.1]
      exact relative_slack_bound hε hx.2.le (dominated x)
    · rw [support x hx, mul_zero]
      exact sub_nonneg.mpr (hV.above x)
  · exact subtract

noncomputable def kernelTransfer {ι : Type*} (K : ι → ι → ℝ)
    (f : ι → ℝ) (x : ι) : ℝ := ∑' y, K x y * f y

theorem kernel_dominated_summable {ι : Type*}
    {K : ι → ι → ℝ} {V φ : ι → ℝ}
    (kernel_nonneg : ∀ x y, 0 ≤ K x y)
    (nonneg : ∀ x, 0 ≤ φ x) (dominated : ∀ x, φ x ≤ V x)
    (summable : ∀ x, Summable (fun y => K x y * V y)) :
    ∀ x, Summable (fun y => K x y * φ y) := by
  intro x
  exact Summable.of_nonneg_of_le
    (fun y => mul_nonneg (kernel_nonneg x y) (nonneg y))
    (fun y => mul_le_mul_of_nonneg_left (dominated y) (kernel_nonneg x y))
    (summable x)

/-- The usual minimum property over summable competitors supplies the
restricted interface. Its use is safe for `Real.tsum`: every competitor
between a nonnegative obstacle and `V` has an actual finite parent sum. -/
theorem kernel_least_of_summable_minimal {ι : Type*}
    {K : ι → ι → ℝ} {b V : ι → ℝ}
    (kernel_nonneg : ∀ x y, 0 ≤ K x y)
    (summable : ∀ x, Summable (fun y => K x y * V y))
    (obstacle_nonneg : ∀ x, 0 ≤ b x)
    (above : ∀ x, b x ≤ V x)
    (excessive : ∀ x, kernelTransfer K V x ≤ V x)
    (minimal : ∀ W : ι → ℝ,
      (∀ x, b x ≤ W x) →
      (∀ x, Summable (fun y => K x y * W y)) →
      (∀ x, kernelTransfer K W x ≤ W x) → ∀ x, V x ≤ W x) :
    LeastMajorant (kernelTransfer K) b V := by
  refine ⟨obstacle_nonneg, above, excessive, ?_⟩
  intro W hbelow habove hsuper
  apply minimal W hbelow
  · exact kernel_dominated_summable kernel_nonneg
      (fun x => (obstacle_nonneg x).trans (hbelow x)) habove summable
  · exact hsuper

theorem kernel_dominated_subtract {ι : Type*}
    {K : ι → ι → ℝ} {V φ : ι → ℝ}
    (kernel_nonneg : ∀ x y, 0 ≤ K x y)
    (nonneg : ∀ x, 0 ≤ φ x) (dominated : ∀ x, φ x ≤ V x)
    (summable : ∀ x, Summable (fun y => K x y * V y)) (δ : ℝ) :
    ∀ x, kernelTransfer K (fun y => V y - δ * φ y) x =
      kernelTransfer K V x - δ * kernelTransfer K φ x := by
  intro x
  have hs := kernel_dominated_summable kernel_nonneg nonneg dominated summable x
  unfold kernelTransfer
  calc
    (∑' y, K x y * (V y - δ * φ y)) =
        ∑' y, (K x y * V y - δ * (K x y * φ y)) := by
      apply tsum_congr
      intro y
      ring
    _ = (∑' y, K x y * V y) - ∑' y, δ * (K x y * φ y) :=
      (summable x).tsum_sub (hs.mul_left δ)
    _ = (∑' y, K x y * V y) - δ * ∑' y, K x y * φ y := by
      rw [tsum_mul_left]

/-- Countable positive kernels need no extra subtraction axiom once the
excessive envelope's parent sums are summable. -/
theorem kernel_no_killed_fixed_point {ι : Type*}
    {K : ι → ι → ℝ} {unit : ι → Prop} {V φ : ι → ℝ} {ε : ℝ}
    (kernel_nonneg : ∀ x y, 0 ≤ K x y)
    (summable : ∀ x, Summable (fun y => K x y * V y))
    (hV : LeastMajorant (kernelTransfer K) (unitObstacle unit) V)
    (hε : 0 < ε)
    (nonneg : ∀ x, 0 ≤ φ x) (dominated : ∀ x, φ x ≤ V x)
    (fixed : ∀ x, unit x ∧ 1 + ε < V x → kernelTransfer K φ x = φ x)
    (support : ∀ x, ¬ (unit x ∧ 1 + ε < V x) → φ x = 0) :
    ∀ x, φ x = 0 := by
  apply no_killed_fixed_point hV hε nonneg dominated
  · intro x
    exact tsum_nonneg (fun y => mul_nonneg (kernel_nonneg x y) (nonneg y))
  · exact fixed
  · exact support
  · exact kernel_dominated_subtract kernel_nonneg nonneg dominated summable _

end CollatzPotential

#print axioms CollatzPotential.LeastMajorant
#print axioms CollatzPotential.unitObstacle
#print axioms CollatzPotential.kernelTransfer
#print axioms CollatzPotential.no_slack_subharmonic
#print axioms CollatzPotential.relative_slack_bound
#print axioms CollatzPotential.no_killed_fixed_point
#print axioms CollatzPotential.kernel_dominated_summable
#print axioms CollatzPotential.kernel_least_of_summable_minimal
#print axioms CollatzPotential.kernel_dominated_subtract
#print axioms CollatzPotential.kernel_no_killed_fixed_point
