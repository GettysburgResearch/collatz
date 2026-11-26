import MinimumFailure

/-! The e=6 upper-hit family supplies every edge below one ordinary boundary
on an arithmetic progression. -/
namespace Collatz.UpperBoundary
open Collatz.SourceDeletion Collatz.MinimumFailure

/-- For every row, the smaller query compares an odd integer to its successor. -/
theorem row (t : Nat) :
    run 7 (161 + 1536*t) = 103 + 972*t ∧
    run 9 (3*(161 + 1536*t)) = 26 + 243*t := by
  have lo := lift 7 161 (12*t)
  have hi := lift 9 483 (9*t)
  change run 7 (161 + 128*(12*t)) = 103 + 81*(12*t) at lo
  change run 9 (483 + 512*(9*t)) = 26 + 27*(9*t) at hi
  constructor
  · convert lo using 2 <;> ring
  · convert hi using 2 <;> ring

private theorem quarter (t : Nat) :
    run 2 (104 + 972*t) = 26 + 243*t := by
  have h := lift 2 104 (243*t)
  change run 2 (104 + 4*(243*t)) = 26 + 1*(243*t) at h
  convert h using 2 <;> ring

/-- Keep the two actual labels, including the upper label at the successor. -/
theorem exact_labels (t : Nat) :
    (Good (161 + 1536*t) ↔ Good (103 + 972*t)) ∧
    (Good (3*(161 + 1536*t)) ↔ Good (104 + 972*t)) := by
  obtain ⟨lo, hi⟩ := row t
  constructor
  · simpa only [lo] using (good_run 7 (161 + 1536*t)).symm
  · have a := (good_run 9 (3*(161 + 1536*t))).symm
    rw [hi, ← quarter t] at a
    exact a.trans (good_run 2 (104+972*t))

/-- A supplied canonical least reverse failure forces all earlier directed
successor comparisons on its own row. The failing successor comparison itself
is kept as part of the conclusion. -/
theorem boundary (k : Nat)
    (miss : ¬Good (161 + 1536*k)) (upper : Good (3*(161 + 1536*k)))
    (least : ∀ w, 0 < w → w % 48 = 17 → w < 161 + 1536*k → Good (3*w) → Good w) :
    (¬Good (103 + 972*k) ∧ Good (104 + 972*k)) ∧
    ∀ t, t < k → Good (104 + 972*t) → Good (103 + 972*t) := by
  obtain ⟨lo, hi⟩ := exact_labels k
  refine ⟨⟨fun g => miss (lo.mpr g), hi.mp upper⟩, ?_⟩
  intro t lt g
  exact (exact_labels t).1.mp (least _ (by omega) (by omega) (by omega)
    ((exact_labels t).2.mpr g))

private theorem halves (d u : Nat) : run d (2^d*u) = u := by
  induction d with
  | zero => simp [run]
  | succ d ih =>
    have e : 2^(d+1)*u = 2*(2^d*u) := by ring
    have s : step (2*(2^d*u)) = 2^d*u := by unfold step; split <;> omega
    rw [run, e, s, ih]

/-- A full interval on a fixed congruence class is already certified, with the
external quantitative floor written as its precise arithmetic consequence. -/
theorem filled_class (k t u : Nat)
    (lt : t < k) (digits : 104 + 972*t = 2^40*u)
    (least : ∀ w, 0 < w → w % 48 = 17 → w < 161 + 1536*k → Good (3*w) → Good w)
    (floorGood : ∀ n, 0 < n → 2^40*n < 161 + 1536*k → Good n) :
    Good (103 + 972*t) := by
  obtain ⟨lo, hi⟩ := exact_labels t
  apply lo.mp
  apply least _ (by omega) (by omega) (by omega)
  apply hi.mpr
  rw [digits]
  apply (good_run 40 _).mp
  rw [halves]
  apply floorGood u <;> omega

#print axioms row
#print axioms exact_labels
#print axioms boundary
#print axioms filled_class
end Collatz.UpperBoundary
