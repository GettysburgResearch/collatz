import SourceDeletion

namespace Collatz.MinimumFailure

open Collatz.SourceDeletion

/-- Membership in the actual positive basin of 1, using the shortcut map. -/
def Good (n : Nat) : Prop := ∃ h, run h n = 1

theorem good_one : Good 1 := ⟨0, rfl⟩

theorem good_step (n : Nat) : Good (step n) ↔ Good n := by
  constructor
  · rintro ⟨h, hh⟩
    exact ⟨h+1, hh⟩
  · rintro ⟨h, hh⟩
    cases h with
    | zero =>
      have hn : n=1 := hh
      rw [hn]
      exact ⟨1, by decide⟩
    | succ h => exact ⟨h, hh⟩

theorem good_run (h n : Nat) : Good (run h n) ↔ Good n := by
  induction h generalizing n with
  | zero => rfl
  | succ h ih => exact (ih (step n)).trans (good_step n)

noncomputable def label (n : Nat) : Nat := by
  classical
  exact if Good n then 1 else 0

theorem label_step (n : Nat) : label (step n) = label n := by
  classical
  by_cases h : Good n
  · have hs : Good (step n) := (good_step n).mpr h
    simp only [label, ite_eq_left h, ite_eq_left hs]
  · have hs : ¬Good (step n) := fun hs => h ((good_step n).mp hs)
    simp only [label, ite_eq_right h, ite_eq_right hs]

theorem label_one : label 1 = 1 := by simp [label, good_one]

theorem label_eq_one (n : Nat) : label n=label 1 ↔ Good n := by
  classical
  rw [label_one]
  simp only [label]
  by_cases h : Good n <;> simp [h]

/-- Minimality is over all positive odd integers, including multiples of 3. -/
structure LeastDiscordance (q : Nat) : Prop where
  positive : 0<q
  odd : q%2=1
  different : label q ≠ label (3*q)
  below : ∀ v, 0<v → v%2=1 → v<q → label v=label (3*v)

theorem exists_least_discordance
    (bad : ∃ n, 0<n ∧ ¬Good n) : ∃ q, LeastDiscordance q := by
  classical
  have exists_difference : ∃ q, 0<q ∧ q%2=1 ∧ label q≠label (3*q) := by
    by_contra no_difference
    obtain ⟨n, hn, hbad⟩ := bad
    have all_safe : ∀ v, 0<v → v%2=1 → v<n → label v=label (3*v) := by
      intro v hv ho _
      by_contra different
      exact no_difference ⟨v,hv,ho,different⟩
    have eq := all_below label label_step n all_safe n hn (by omega)
    exact hbad ((label_eq_one n).mp eq)
  let q := Nat.find exists_difference
  have property := Nat.find_spec exists_difference
  refine ⟨q, property.1, property.2.1, property.2.2, ?_⟩
  intro v hv ho less
  by_contra different
  have le : q≤v := Nat.find_min' exists_difference ⟨hv,ho,different⟩
  omega

theorem good_below {q : Nat} (least : LeastDiscordance q)
    (n : Nat) (hn : 0<n) (hnq : n≤q) : Good n := by
  apply (label_eq_one n).mp
  exact all_below label label_step q least.below n hn hnq

theorem good_cutoff {q : Nat} (least : LeastDiscordance q)
    (n : Nat) (hn : 0<n) (cost : 8*n+1<9*q) : Good n := by
  apply (label_eq_one n).mp
  exact all_below_cutoff label label_step q least.below n hn cost

theorem upper_bad {q : Nat} (least : LeastDiscordance q) : ¬Good (3*q) := by
  intro upper
  have lower := good_below least q least.positive (by omega)
  exact least.different (((label_eq_one q).mpr lower).trans
    ((label_eq_one (3*q)).mpr upper).symm)

/-- Every smaller odd multiple of 3 is in the basin, while 3q is not. -/
theorem smaller_triples_good {q : Nat} (least : LeastDiscordance q)
    (v : Nat) (hv : 0<v) (ho : v%2=1) (less : v<q) : Good (3*v) := by
  have lower := good_below least v hv (by omega)
  apply (label_eq_one (3*v)).mp
  exact (least.below v hv ho less).symm.trans ((label_eq_one v).mpr lower)

/-- The minimum also excludes every smaller even multiple of 3. -/
theorem smaller_multiples_good {q : Nat} (least : LeastDiscordance q) :
    ∀ n, 0<n → n%3=0 → n<3*q → Good n := by
  intro n
  induction n using Nat.strong_induction_on with
  | h n ih =>
    intro hn hthree less
    by_cases even : n%2=0
    · have half : Good (n/2) := ih (n/2) (by omega) (by omega) (by omega) (by omega)
      apply (good_step n).mp
      rw [show step n=n/2 by unfold step; split <;> omega]
      exact half
    · have hnodd : n%2=1 := by omega
      have eq : 3*(n/3)=n := by omega
      have h := smaller_triples_good least (n/3) (by omega) (by omega) (by omega)
      rwa [eq] at h

/-- This applies to every positive counterexample N, not just the least one. -/
theorem counterexample_bound {q : Nat} (least : LeastDiscordance q)
    (n : Nat) (hn : 0<n) (bad : ¬Good n) : 9*q≤8*n+1 := by
  by_contra no_bound
  exact bad (good_cutoff least n hn (by omega))

theorem exclude_seven_mod_eight {q : Nat} (least : LeastDiscordance q) : q%8≠7 := by
  intro residue
  let k := q/8
  have eq : q=8*k+7 := by dsimp [k]; omega
  have paths := seven_mod_eight k
  have small : Good (6*k+5) := good_below least _ (by omega) (by omega)
  have endpoint : Good (step (6*k+5)) := (good_step _).mpr small
  rw [← paths.1] at endpoint
  have upper : Good (3*q) := by rw [eq]; exact (good_run 3 _).mp endpoint
  exact upper_bad least upper

/-- A fully formal necessary shape of any failure of positive Collatz. -/
theorem counterexample_reduction (bad : ∃ n, 0<n ∧ ¬Good n) :
    ∃ q, LeastDiscordance q ∧ Good q ∧ ¬Good (3*q) ∧ q%8≠7 ∧
      (∀ n, 0<n → 8*n+1<9*q → Good n) ∧
      (∀ v, 0<v → v%2=1 → v<q → Good (3*v)) ∧
      (∀ n, 0<n → n%3=0 → n<3*q → Good n) := by
  obtain ⟨q,least⟩ := exists_least_discordance bad
  exact ⟨q,least,good_below least q least.positive (by omega),upper_bad least,
    exclude_seven_mod_eight least,good_cutoff least,smaller_triples_good least,
    smaller_multiples_good least⟩

#print axioms good_one
#print axioms good_step
#print axioms good_run
#print axioms label_step
#print axioms label_one
#print axioms label_eq_one
#print axioms exists_least_discordance
#print axioms good_below
#print axioms good_cutoff
#print axioms upper_bad
#print axioms smaller_triples_good
#print axioms smaller_multiples_good
#print axioms counterexample_bound
#print axioms exclude_seven_mod_eight
#print axioms counterexample_reduction

end Collatz.MinimumFailure
