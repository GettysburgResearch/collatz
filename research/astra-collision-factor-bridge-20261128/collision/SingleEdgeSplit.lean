import Mathlib.Logic.Function.Iterate
import Lean.Elab.Tactic.Omega

/-! The actual one-edge map, unchanged first-hit set, and exact cycle
rescaling. The limiting collision and Brownian statements remain written. -/

namespace Collatz.SingleEdgeSplit

/-- The actual native shortcut, stated locally to keep this finite kernel small. -/
def shortcut (n : ℕ) : ℕ := if n % 2 = 0 then n / 2 else (3 * n + 1) / 2

def splitAt (q n : ℕ) : ℕ := if n = q then 2 * q else shortcut n

theorem splitAt_unchanged {q n : ℕ} (hn : n ≠ q) :
    splitAt q n = shortcut n := by simp [splitAt, hn]

theorem splitAt_even {q : ℕ} (hq : q % 2 = 1) (n : ℕ) :
    splitAt q (2 * n) = n := by
  have hn : 2 * n ≠ q := by omega
  simp [splitAt, hn, shortcut]

/-- A change at one vertex cannot affect a prefix before its first visit. -/
theorem iterate_eq_before_hit {α : Type*} (F G : α → α) (q x : α)
    (same : ∀ y, y ≠ q → G y = F y) (t : ℕ)
    (avoid : ∀ i < t, F^[i] x ≠ q) : G^[t] x = F^[t] x := by
  induction t with
  | zero => rfl
  | succ t ih =>
    have hi : G^[t] x = F^[t] x := ih (fun i h => avoid i (by omega))
    rw [Function.iterate_succ_apply', Function.iterate_succ_apply', hi]
    exact same _ (avoid t (by omega))

/-- First visits to the edited vertex are preserved in both directions. -/
theorem splitAt_hit_iff (q x : ℕ) :
    (∃ t, (splitAt q)^[t] x = q) ↔ (∃ t, shortcut^[t] x = q) := by
  classical
  constructor
  · rintro ⟨t, ht⟩
    by_contra h
    have h' : ∀ i, shortcut^[i] x ≠ q := fun i hi => h ⟨i, hi⟩
    have he := iterate_eq_before_hit shortcut (splitAt q) q x
      (fun y hy => splitAt_unchanged hy) t (fun i _ => h' i)
    exact h' t (he.symm.trans ht)
  · rintro ⟨t, ht⟩
    by_contra h
    have h' : ∀ i, (splitAt q)^[i] x ≠ q := fun i hi => h ⟨i, hi⟩
    have he := iterate_eq_before_hit (splitAt q) shortcut q x
      (fun y hy => (splitAt_unchanged hy).symm) t (fun i _ => h' i)
    exact h' t (he.symm.trans ht)

theorem splitAt_two_cycle {q : ℕ} (hq : q % 2 = 1) :
    splitAt q q = 2 * q ∧ splitAt q (2 * q) = q := by
  exact ⟨by simp [splitAt], splitAt_even hq q⟩

private theorem one_or_two (t : ℕ) : shortcut^[t] 1 = 1 ∨ shortcut^[t] 1 = 2 := by
  induction t with
  | zero => simp
  | succ t ih =>
    rw [Function.iterate_succ_apply']
    rcases ih with h | h <;> simp [h, shortcut]

/-- The new q,2q cycle has exactly the native phases of 1,2. -/
theorem splitAt_scaled_cycle {q : ℕ} (hq : q % 2 = 1) (t : ℕ) :
    (splitAt q)^[t] q = q * shortcut^[t] 1 := by
  induction t with
  | zero => simp
  | succ t ih =>
    rw [Function.iterate_succ_apply', Function.iterate_succ_apply', ih]
    rcases one_or_two t with h | h
    · simp [h, shortcut, splitAt, Nat.mul_comm]
    · simpa [h, shortcut, Nat.mul_comm] using splitAt_even hq q

theorem five_genuine_tail :
    shortcut 5 = 8 ∧ shortcut 8 = 4 ∧ shortcut 4 = 2 ∧
      shortcut 2 = 1 ∧ shortcut^[4] 5 = 1 := by
  decide

theorem five_modified_return : (splitAt 5)^[4] 5 = 5 := by
  decide

/-- After an actual first visit to five, the two tails differ by the
factor five from the genuine first-one date onward. -/
theorem five_eventual_rescaling (n a t : ℕ)
    (hit : shortcut^[a] n = 5)
    (avoid : ∀ i < a, shortcut^[i] n ≠ 5) :
    (splitAt 5)^[4 + t + a] n = 5 * shortcut^[4 + t + a] n := by
  have hu : (splitAt 5)^[a] n = 5 :=
    (iterate_eq_before_hit shortcut (splitAt 5) 5 n
      (fun y hy => splitAt_unchanged hy) a avoid).trans hit
  rw [Function.iterate_add_apply (splitAt 5) (4 + t) a n,
    Function.iterate_add_apply shortcut (4 + t) a n, hu, hit]
  rw [Nat.add_comm 4 t, Function.iterate_add_apply (splitAt 5) t 4 5,
    Function.iterate_add_apply shortcut t 4 5,
    five_modified_return, five_genuine_tail.2.2.2.2]
  exact splitAt_scaled_cycle (by decide) t

theorem finite_table_preserved {q R n : ℕ} (hq : R < q) (hn : n ≤ R) :
    splitAt q n = shortcut n := by
  apply splitAt_unchanged
  omega

def unitFive (n : ℕ) : ℕ := if n = 5 then 9 else shortcut n

theorem unitFive_unchanged {n : ℕ} (hn : n ≠ 5) :
    unitFive n = shortcut n := by simp [unitFive, hn]

theorem unitFive_unit_change : unitFive 5 = shortcut 5 + 1 := by decide

theorem unitFive_period : unitFive^[10] 5 = 5 := by decide

theorem unitFive_least_period :
    ∀ t : Fin 10, t.val ≠ 0 → unitFive^[t.val] 5 ≠ 5 := by decide

theorem unitFive_hit_iff (x : ℕ) :
    (∃ t, unitFive^[t] x = 5) ↔ (∃ t, shortcut^[t] x = 5) := by
  classical
  constructor
  · rintro ⟨t, ht⟩
    by_contra h
    have h' : ∀ i, shortcut^[i] x ≠ 5 := fun i hi => h ⟨i, hi⟩
    have he := iterate_eq_before_hit shortcut unitFive 5 x
      (fun y hy => unitFive_unchanged hy) t (fun i _ => h' i)
    exact h' t (he.symm.trans ht)
  · rintro ⟨t, ht⟩
    by_contra h
    have h' : ∀ i, unitFive^[i] x ≠ 5 := fun i hi => h ⟨i, hi⟩
    have he := iterate_eq_before_hit unitFive shortcut 5 x
      (fun y hy => (unitFive_unchanged hy).symm) t (fun i _ => h' i)
    exact h' t (he.symm.trans ht)

end Collatz.SingleEdgeSplit
