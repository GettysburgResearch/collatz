module

public import Mathlib.Algebra.Order.BigOperators.Group.Finset
public import Mathlib.Dynamics.PeriodicPts.Defs
public import Mathlib.Tactic

public section

namespace Collatz.CycleRotation

set_option autoImplicit false
open scoped BigOperators

variable {ι : Type*} [Fintype ι]

/-- A permutation of a finite positive cycle has a phase at which the rotated
height is no larger than the original height. No ratio or logarithm is assumed. -/
theorem permutation_seed [Nonempty ι] (σ : Equiv.Perm ι) (q : ι → ℕ) :
    ∃ i, q (σ i) ≤ q i := by
  classical
  by_contra! h
  obtain ⟨i⟩ := ‹Nonempty ι›
  have hs : (∑ j, q j) < ∑ j, q (σ j) :=
    Finset.sum_lt_sum (fun j _ => (h j).le) ⟨i, Finset.mem_univ i, h i⟩
  rw [Equiv.sum_comp σ q] at hs
  exact (lt_irrefl _ hs)

def weight (b : ι → Bool) : ℕ := ∑ i, if b i then 1 else 0

/-- A zero-to-one discrepancy is the direction that can enlarge a corrected
height ratio under a common shortcut clock. -/
def adverse (b c : ι → Bool) : ℕ :=
  ∑ i, if b i = false ∧ c i = true then 1 else 0

def hamming (b c : ι → Bool) : ℕ := ∑ i, if b i = c i then 0 else 1

/-- Equal binary weights balance the two directions of discrepancy exactly. -/
theorem equal_weight_hamming (b c : ι → Bool) (hw : weight b = weight c) :
    hamming b c = 2 * adverse b c := by
  classical
  have hs : hamming b c = adverse b c + adverse c b := by
    unfold hamming adverse
    rw [← Finset.sum_add_distrib]
    apply Finset.sum_congr rfl
    intro i _
    cases hb : b i <;> cases hc : c i <;> simp
  have hb : weight b + adverse b c = weight c + adverse c b := by
    unfold weight adverse
    rw [← Finset.sum_add_distrib, ← Finset.sum_add_distrib]
    apply Finset.sum_congr rfl
    intro i _
    cases hbi : b i <;> cases hci : c i <;> simp
  omega

/-- For every cyclic permutation, the charged mismatches are exactly half of
the Hamming distance, with no statistical or balance hypothesis on the word. -/
theorem permutation_hamming (σ : Equiv.Perm ι) (b : ι → Bool) :
    hamming b (fun i => b (σ i)) = 2 * adverse b (fun i => b (σ i)) := by
  apply equal_weight_hamming
  unfold weight
  exact (Equiv.sum_comp σ (fun i => if b i then 1 else 0)).symm

/-- A nonidentity rotation of a least-period deterministic cycle cannot meet
the original cycle at the same clock. This includes every actual Collatz cycle. -/
theorem primitive_rotation_ne {α : Type*} (f : α → α) (x : α) (N r k : ℕ)
    (hN : 0 < N) (hp : f^[N] x = x)
    (least : ∀ j, 0 < j → j < N → f^[j] x ≠ x)
    (hr : 0 < r) (hrN : r < N) : f^[k+r] x ≠ f^[k] x := by
  intro he
  have hx : Function.IsPeriodicPt f N x := hp
  have hy := hx.apply_iterate r
  have hh : f^[k] (f^[r] x) = f^[k] x := by
    simpa only [Function.iterate_add_apply] using he
  have hh' : f^[r] x = x :=
    (hy.iterate k).eq_of_apply_eq_same (hx.iterate k) hN hh
  exact least r hr hrN hh'

#print axioms permutation_seed
#print axioms equal_weight_hamming
#print axioms permutation_hamming
#print axioms primitive_rotation_ne

end Collatz.CycleRotation
