import Mathlib.Algebra.BigOperators.Group.Finset.Sigma
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Ring.Rat
import Mathlib.Logic.Function.Iterate

namespace AstraNine.WindowOccupation

/-- A finite record of one-letter state/action mass during a stored plan. -/
def occupancy {σ α : Type*} (flow : ℕ → σ → α → ℚ) (length : ℕ)
    (state : σ) (action : α) : ℚ :=
  ∑ j ∈ Finset.range length, flow j state action

private theorem sum_succ_conservation (mass : ℕ → ℚ) (n : ℕ) :
    (∑ j ∈ Finset.range n, mass (j+1)) + mass 0 =
    (∑ j ∈ Finset.range n, mass j) + mass n := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [Finset.sum_range_succ, Finset.sum_range_succ, add_right_comm _ (mass (n+1)) (mass 0), ih]

/-- A closed block plan yields a stationary one-step occupation flow for
exactly the supplied finite transition kernel. Actions may depend on the
actual position and all previously stored decisions. -/
theorem stationary_occupation {σ α : Type*} [Fintype σ] [Fintype α]
    (flow : ℕ → σ → α → ℚ) (mass : ℕ → σ → ℚ) (K : σ → α → σ → ℚ)
    (n : ℕ) (depart : ∀ j < n, ∀ s, ∑ e, flow j s e = mass j s)
    (arrive : ∀ j < n, ∀ t, ∑ s, ∑ e, flow j s e * K s e t = mass (j+1) t)
    (closed : mass n = mass 0) (t : σ) :
    (∑ s, ∑ e, occupancy flow n s e * K s e t) = ∑ e, occupancy flow n t e := by
  have outgoing : (∑ e, occupancy flow n t e) = ∑ j ∈ Finset.range n, mass j t := by
    unfold occupancy
    rw [Finset.sum_comm]
    exact Finset.sum_congr rfl (fun j hj => depart j (Finset.mem_range.mp hj) t)
  have incoming : (∑ s, ∑ e, occupancy flow n s e * K s e t) =
      ∑ j ∈ Finset.range n, mass (j+1) t := by
    unfold occupancy
    simp only [Finset.sum_mul]
    calc
      (∑ s, ∑ e, ∑ j ∈ Finset.range n, flow j s e * K s e t) =
          ∑ s, ∑ j ∈ Finset.range n, ∑ e, flow j s e * K s e t := by
            apply Finset.sum_congr rfl
            intro s _
            rw [Finset.sum_comm]
      _ = ∑ j ∈ Finset.range n, ∑ s, ∑ e, flow j s e * K s e t := by
            rw [Finset.sum_comm]
      _ = _ := Finset.sum_congr rfl (fun j hj => arrive j (Finset.mem_range.mp hj) t)
  rw [incoming, outgoing]
  have eqn := sum_succ_conservation (fun j => mass j t) n
  have hc := congrFun closed t
  rw [hc] at eqn
  exact add_right_cancel eqn

/-- Mixing the stationary flows before dividing by the state marginal
preserves exactly the stationarity equation. -/
theorem mix_stationary {σ α : Type*} [Fintype σ] [Fintype α]
    (f g : σ → α → ℚ) (K : σ → α → σ → ℚ) (u v : ℚ)
    (hf : ∀ t, ∑ s, ∑ e, f s e * K s e t = ∑ e, f t e)
    (hg : ∀ t, ∑ s, ∑ e, g s e * K s e t = ∑ e, g t e) (t : σ) :
    (∑ s, ∑ e, (u*f s e+v*g s e)*K s e t) = ∑ e, (u*f t e+v*g t e) := by
  simp only [add_mul, mul_assoc, Finset.sum_add_distrib, ← Finset.mul_sum, hf, hg]

/-- Exact first arrival, distinct from an arbitrary inverse return. -/
def FirstHit {α : Type*} (f : α → α) (target x : α) (t : ℕ) : Prop :=
  f^[t] x = target ∧ ∀ j < t, f^[j] x ≠ target

/-- Reaching an off-cycle target and then its first hit adds the genuine
clock. The first part may include arbitrary intermediate states. -/
theorem first_hit_add {α : Type*} (f : α → α) (one target x : α)
    {s t : ℕ} (row : f^[s] x = target)
    (off : ∀ r, f^[r] one ≠ target) (tail : FirstHit f one target t) :
    FirstHit f one x (s+t) := by
  constructor
  · rw [Nat.add_comm, Function.iterate_add_apply, row, tail.1]
  · intro j hj hit
    by_cases hjs : j < s
    · apply off (s-j)
      rw [← hit, ← Function.iterate_add_apply, Nat.sub_add_cancel (Nat.le_of_lt hjs), row]
    · have hsj : s ≤ j := by omega
      apply tail.2 (j-s) (by omega)
      rw [← row, ← Function.iterate_add_apply, Nat.sub_add_cancel hsj, hit]

end AstraNine.WindowOccupation
