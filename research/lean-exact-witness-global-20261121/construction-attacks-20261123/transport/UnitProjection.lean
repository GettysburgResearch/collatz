import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Basic.Real.Basic
import Mathlib.Logic.Function.Iterate
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-!
Finite actual ordinary-source projection. The explicit factorization and
odd-step equation are certificate data; the theorems retain the same
shortcut map, ordinary source, and unit target. The infinite fiber power
sums and the analytic pressure comparison remain written scope.
-/

set_option autoImplicit false

namespace CollatzUnitProjection

def shortcut (n : Nat) : Nat :=
  if n % 2 = 0 then n / 2 else (3 * n + 1) / 2

def Reaches (n q : Nat) : Prop :=
  ∃ k : Nat, (shortcut^[k]) n = q

private theorem step_double (n : Nat) : shortcut (2 * n) = n := by
  simp [shortcut]

private theorem strip_halves (a m : Nat) :
    (shortcut^[a]) (2 ^ a * m) = m := by
  induction a with
  | zero => simp
  | succ a ih =>
    rw [Function.iterate_succ_apply]
    have heq : 2 ^ (a + 1) * m = 2 * (2 ^ a * m) := by ring
    rw [heq, step_double, ih]

private theorem halving_prefix (a k m : Nat) (hk : k ≤ a) :
    (shortcut^[k]) (2 ^ a * m) = 2 ^ (a - k) * m := by
  have ha : a = k + (a - k) := by omega
  have heq : 2 ^ a * m = 2 ^ k * (2 ^ (a - k) * m) := by
    conv_lhs => rw [ha, pow_add]
    ring
  rw [heq, strip_halves]

private theorem even_prefix (a k m : Nat) (hk : k < a) :
    ((shortcut^[k]) (2 ^ a * m)) % 2 = 0 := by
  rw [halving_prefix a k m (by omega)]
  obtain ⟨b, hb⟩ : ∃ b, a - k = b + 1 := ⟨a - k - 1, by omega⟩
  rw [hb, pow_succ]
  simp [Nat.mul_mod]

/-- Removing every initial halving retains any odd ordinary endpoint. -/
theorem odd_part_reaches (n m q a : Nat)
    (factor : n = 2 ^ a * m) (odd_target : q % 2 = 1)
    (hit : Reaches n q) : Reaches m q := by
  obtain ⟨k, hk⟩ := hit
  have hak : a ≤ k := by
    by_contra h
    have hp := even_prefix a k m (by omega)
    rw [← factor, hk, odd_target] at hp
    omega
  refine ⟨k - a, ?_⟩
  have hm : (shortcut^[a]) n = m := by rw [factor, strip_halves]
  rw [← hm, ← Function.iterate_add_apply]
  simpa [Nat.sub_add_cancel hak, Nat.add_comm] using hk

private theorem odd_step (m u a : Nat) (odd_source : m % 2 = 1)
    (edge : 3 * m + 1 = 2 ^ (a + 1) * u) :
    shortcut m = 2 ^ a * u := by
  have heq : 3 * m + 1 = 2 * (2 ^ a * u) := by
    rw [edge]
    ring
  simp [shortcut, odd_source, heq]

/-- A nonunit odd source cannot be the unit endpoint. Its entire first odd
acceleration can therefore be removed from the actual hitting path. -/
theorem nonunit_odd_successor_reaches (m u q a : Nat)
    (odd_source : m % 2 = 1) (nonunit_source : m % 3 = 0)
    (odd_target : q % 2 = 1) (unit_target : q % 3 ≠ 0)
    (edge : 3 * m + 1 = 2 ^ (a + 1) * u)
    (hit : Reaches m q) : Reaches u q := by
  obtain ⟨k, hk⟩ := hit
  cases k with
  | zero =>
    simp only [Function.iterate_zero, id_eq] at hk
    exact False.elim (unit_target (hk ▸ nonunit_source))
  | succ k =>
    rw [Function.iterate_succ_apply, odd_step m u a odd_source edge] at hk
    exact odd_part_reaches (2 ^ a * u) u q a rfl odd_target ⟨k, hk⟩

/-- The projection of a full positive ordinary ancestor is an ancestor of
the identical odd ternary-unit endpoint. -/
theorem full_source_projects (n m u q a b : Nat)
    (factor : n = 2 ^ a * m) (odd_source : m % 2 = 1)
    (nonunit_source : m % 3 = 0)
    (odd_target : q % 2 = 1) (unit_target : q % 3 ≠ 0)
    (edge : 3 * m + 1 = 2 ^ (b + 1) * u)
    (hit : Reaches n q) : Reaches u q :=
  nonunit_odd_successor_reaches m u q b odd_source nonunit_source
    odd_target unit_target edge (odd_part_reaches n m q a factor odd_target hit)

/-- Every integer odd successor of an odd multiple of three is a ternary unit. -/
theorem odd_successor_unit (m u e : Nat)
    (edge : 3 * m + 1 = 2 ^ e * u) : u % 3 ≠ 0 := by
  intro hu
  have hmod := congrArg (fun x : Nat => x % 3) edge
  simp [Nat.add_mod, Nat.mul_mod, hu] at hmod

/-- The exact projection height factor 5/3, including the sharp source 3. -/
theorem projected_height (n m u a b : Nat)
    (positive : 0 < m) (factor : n = 2 ^ a * m)
    (nonunit_source : m % 3 = 0)
    (edge : 3 * m + 1 = 2 ^ (b + 1) * u) : 3 * u ≤ 5 * n := by
  have hm : 3 ≤ m := by omega
  have ha : 1 ≤ 2 ^ a := Nat.one_le_pow a 2 (by omega)
  have hb : 1 ≤ 2 ^ b := Nat.one_le_pow b 2 (by omega)
  have hmn : m ≤ n := by rw [factor]; nlinarith
  have heq : 3 * m + 1 = 2 * (2 ^ b * u) := by rw [edge]; ring
  have htwo : 2 * u ≤ 3 * m + 1 := by nlinarith
  nlinarith

/-- Deduplicate the actual image and pay each full weighted fiber exactly
once. The quantitative fiber estimate is an explicit input to this finite
consumer, not an axiom asserting the written infinite bound. -/
theorem finite_projection_mass
    (G : Finset Nat) (p : Nat → Nat) (w v : Nat → Real) (C : Real)
    (fiber : ∀ u ∈ G.image p, ∑ n ∈ G.filter (fun n => p n = u), w n ≤ C * v u) :
    ∑ n ∈ G, w n ≤ C * ∑ u ∈ G.image p, v u := by
  classical
  calc
    _ = ∑ u ∈ G.image p, ∑ n ∈ G.filter (fun n => p n = u), w n := by
      symm
      exact Finset.sum_fiberwise_of_maps_to (fun n hn => Finset.mem_image_of_mem p hn) w
    _ ≤ ∑ u ∈ G.image p, C * v u := by
      exact Finset.sum_le_sum fiber
    _ = C * ∑ u ∈ G.image p, v u := by rw [Finset.mul_sum]

#print axioms odd_part_reaches
#print axioms nonunit_odd_successor_reaches
#print axioms full_source_projects
#print axioms odd_successor_unit
#print axioms projected_height
#print axioms finite_projection_mass

end CollatzUnitProjection
