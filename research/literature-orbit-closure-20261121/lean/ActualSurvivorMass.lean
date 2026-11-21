module

public import BandAbsorption
public import FiniteResolvent

@[expose] public section

/-!
# The quadratic transport test for actual marked survivors

Incoming mass is defined from the original source atoms and actual complete
marked returns. It is the supremum of its finite source sums; no distribution
is replaced at an endpoint. The closing estimate remains an explicit premise.
-/

namespace CollatzShell.ForwardSection

open CollatzHarmonic CollatzFiniteResolvent Finset

def Survives (n k : ℕ) : Prop := ∀ j ≤ k, returns n j ≠ 1

noncomputable def incomingTerm (a : ℕ → ℝ) (k y n : ℕ) : ℝ := by
  classical
  exact if Marked n ∧ Survives n k ∧ returns n k = y then a n else 0

noncomputable def incoming (a : ℕ → ℝ) (k y : ℕ) : ℝ :=
  ⨆ E : Finset ℕ, ∑ n ∈ E, incomingTerm a k y n

theorem incomingTerm_bounds {a : ℕ → ℝ} (ha : ∀ n, 0 ≤ a n) (k y n : ℕ) :
    0 ≤ incomingTerm a k y n ∧ incomingTerm a k y n ≤ a n := by
  classical
  unfold incomingTerm
  split <;> simp_all

theorem incoming_finite_bound {a : ℕ → ℝ} {S : ℝ}
    (ha : FiniteMass a S) (k y : ℕ) (E : Finset ℕ) :
    ∑ n ∈ E, incomingTerm a k y n ≤ S := by
  calc
    _ ≤ ∑ n ∈ E, a n := sum_le_sum (fun n _ ↦ (incomingTerm_bounds ha.1 k y n).2)
    _ ≤ S := ha.2 E

theorem incoming_bdd {a : ℕ → ℝ} {S : ℝ}
    (ha : FiniteMass a S) (k y : ℕ) :
    BddAbove (Set.range (fun E : Finset ℕ ↦ ∑ n ∈ E, incomingTerm a k y n)) := by
  refine ⟨S, ?_⟩
  rintro z ⟨E,rfl⟩
  exact incoming_finite_bound ha k y E

theorem incoming_bounds {a : ℕ → ℝ} {S : ℝ}
    (ha : FiniteMass a S) (k y : ℕ) :
    0 ≤ incoming a k y ∧ incoming a k y ≤ S := by
  constructor
  · have h := le_ciSup (incoming_bdd ha k y) (∅ : Finset ℕ)
    simpa only [sum_empty,incoming] using h
  · exact ciSup_le (incoming_finite_bound ha k y)

/-- One fixed surviving ordinary source is still present, with its original
mass, in the entire incoming fiber over its actual return endpoint. -/
theorem source_atom_le_incoming {a : ℕ → ℝ} {S : ℝ}
    (ha : FiniteMass a S) {n k : ℕ} (hn : Marked n) (alive : Survives n k) :
    a n ≤ incoming a k (returns n k) := by
  classical
  have h := le_ciSup (incoming_bdd ha k (returns n k)) ({n} : Finset ℕ)
  simpa only [sum_singleton,incomingTerm,hn,alive,and_self,eq_self_iff_true,
    ite_true,incoming] using h

noncomputable def survivorBudget (a : ℕ → ℝ) (k y : ℕ) : ℝ :=
  budget (fun j ↦ incoming a j y) k

/-- An exact finite-horizon extraction for an actual ordinary source. -/
theorem actual_survivor_budget {a : ℕ → ℝ} {S L : ℝ}
    (ha : FiniteMass a S) (hL : 0 ≤ L) {n k : ℕ}
    (hn : Marked n) (alive : Survives n k)
    (transport : coefficient 0 * incoming a k (returns n k) ≤
      L * survivorBudget a k (returns n k)) :
    ((k : ℝ)+1)*((k : ℝ)+2)*a n ≤ 16*L*S := by
  have hS : 0 ≤ S := by simpa using ha.2 ∅
  exact survivor_atom_bound_cleared (fun j ↦ incoming a j (returns n k)) k S (a n) L
    hS hL (fun j _ ↦ incoming_bounds ha j (returns n k))
    (source_atom_le_incoming ha hn alive) transport

theorem survives_of_not_basin {n : ℕ} (bad : ¬ Basin n) (k : ℕ) : Survives n k := by
  intro j _ hit
  have path := return_iterate_hit n j
  rw [← returns_eq_iterate] at path
  exact bad (by simpa only [hit, Hits, Basin] using path)

/-- A hypothetical counterexample forces the full quadratic lower scale at
every finite return depth for the same original source. -/
theorem counterexample_forces_quadratic {a : ℕ → ℝ} {S : ℝ}
    (ha : FiniteMass a S) (L : ℕ → ℝ) (hL : ∀ k, 0 ≤ L k)
    (transport : ∀ k y, coefficient 0 * incoming a k y ≤
      L k * survivorBudget a k y)
    {n : ℕ} (hn : Marked n) (bad : ¬ Basin n) (k : ℕ) :
    ((k : ℝ)+1)*((k : ℝ)+2)*a n ≤ 16*L k*S :=
  actual_survivor_budget ha (hL k) hn (survives_of_not_basin bad k) (transport k _)

/-- It suffices to save an arbitrarily small factor of the quadratic scale
along a subsequence.  The actual incoming fibers are constructed above;
the displayed transport improvement is the remaining mathematical premise. -/
theorem collatz_of_quadratic_slice_saving {a : ℕ → ℝ} {S : ℝ}
    (ha : FiniteMass a S) (positive : ∀ n, Marked n → 0 < a n)
    (L : ℕ → ℝ) (hL : ∀ k, 0 ≤ L k)
    (transport : ∀ k y, coefficient 0 * incoming a k y ≤
      L k * survivorBudget a k y)
    (saving : ∀ ε : ℝ, 0 < ε → ∃ k : ℕ,
      16*L k*S < ((k : ℝ)+1)*((k : ℝ)+2)*ε) :
    Universal := by
  apply collatz_iff_marked.mpr
  intro n hn
  by_contra bad
  obtain ⟨k,hk⟩ := saving (a n) (positive n hn)
  have lower := counterexample_forces_quadratic ha L hL transport hn bad k
  exact (not_lt_of_ge lower) hk

end CollatzShell.ForwardSection
