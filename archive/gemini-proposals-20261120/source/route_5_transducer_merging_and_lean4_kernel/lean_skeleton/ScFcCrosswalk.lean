/-!
# ScFcCrosswalk.lean
Lean 4.34.1 skeleton aligned with GettysburgResearch/collatz (PR #146 style).

Formalizes:
1. The shortcut Collatz map `T`.
2. The `SC*` + `FC*` least-counterexample crosswalk (`sc_fc_implies_collatz`).
3. Route 1's affine contraction lemma: for every `k : Nat`, `T^[3] (5 * (8 * k + 3) + 1) = 5 * k + 2 < 8 * k + 3`.

NOTE: This file does NOT prove the Collatz conjecture; it formalizes exact local
reductions and affine lemmas intended for `lake build` verification.
-/

namespace GettysburgCollatz

/-- Shortcut Collatz map T(n) = n/2 if even, (3n+1)/2 if odd. -/
def T (n : Nat) : Nat :=
  if n % 2 = 0 then n / 2 else (3 * n + 1) / 2

/-- Iterate T `j` times. -/
def T_iter : Nat → Nat → Nat
  | 0, n => n
  | j + 1, n => T_iter j (T n)

/-- Count of odd steps along the first `j` steps from `n`. -/
def oddCount : Nat → Nat → Nat
  | 0, _ => 0
  | j + 1, n => (if n % 2 = 1 then 1 else 0) + oddCount j (T n)

/-- Orbit of `n` eventually reaches 1. -/
def ReachesOne (n : Nat) : Prop :=
  ∃ k : Nat, T_iter k n = 1

/-- SC*: Every n > 1 admits a coefficient-subcritical step j >= 1 with 2^j > 3^(oddCount j n). -/
def SC_star : Prop :=
  ∀ n : Nat, 1 < n → ∃ j : Nat, 0 < j ∧ 3 ^ (oddCount j n) < 2 ^ j

/-- FC*: At the first coefficient-subcritical step j for n > 1, T^j(n) < n. -/
def FC_star : Prop :=
  ∀ n j : Nat, 1 < n → 0 < j →
    3 ^ (oddCount j n) < 2 ^ j →
    (∀ j' : Nat, 0 < j' → j' < j → 2 ^ j' ≤ 3 ^ (oddCount j' n)) →
    T_iter j n < n

/-- Helper: composition of T_iter. -/
theorem T_iter_add (a b n : Nat) : T_iter (a + b) n = T_iter b (T_iter a n) := by
  induction a generalizing n with
  | zero => simp [T_iter]
  | succ a ih =>
    simp only [Nat.succ_add, T_iter]
    exact ih (T n)

/-- Theorem 4.1 (Crosswalk): SC* and FC* together imply every positive integer reaches 1. -/
theorem sc_fc_implies_collatz (hSC : SC_star) (hFC : FC_star) :
    ∀ n : Nat, 0 < n → ReachesOne n := by
  intro n
  induction n using Nat.strong_induction_on with
  | h n ih =>
    intro hpos
    by_cases h1 : n = 1
    · subst h1
      exact ⟨0, rfl⟩
    · have hgt : 1 < n := by omega
      obtain ⟨j_any, hj_pos, hj_sub⟩ := hSC n hgt
      -- Existence of a least j >= 1 satisfying 3^(oddCount j n) < 2^j
      classical
      let P : Nat → Prop := fun j => 0 < j ∧ 3 ^ (oddCount j n) < 2 ^ j
      have hex : ∃ j, P j := ⟨j_any, hj_pos, hj_sub⟩
      let j0 := Nat.find hex
      have hj0 : P j0 := Nat.find_spec hex
      have hmin : ∀ j' : Nat, 0 < j' → j' < j0 → 2 ^ j' ≤ 3 ^ (oddCount j' n) := by
        intro j' hj'_pos hj'_lt
        have hnot : ¬ P j' := Nat.find_min hex hj'_lt
        by_contra hlt
        exact hnot ⟨hj'_pos, Nat.lt_of_not_ge hlt⟩
      have hdrop : T_iter j0 n < n := hFC n j0 hgt hj0.1 hj0.2 hmin
      have hdrop_pos : 0 < T_iter j0 n := by
        -- For every positive n, T^j(n) > 0
        clear hdrop hmin hj0 hex hgt h1 hSC hFC ih
        induction j0 generalizing n with
        | zero => exact hpos
        | succ k ihk =>
          apply ihk (T n)
          unfold T
          split <;> omega
      obtain ⟨k, hk⟩ := ih (T_iter j0 n) hdrop hdrop_pos
      refine ⟨j0 + k, ?_⟩
      rw [T_iter_add, hk]

/-- Lemma 1.4 (Route 1): For t = 8k + 3, T^3(5t + 1) = 5k + 2 < t. -/
theorem five_t_plus_1_mod8_eq3_contracts (k : Nat) :
    T_iter 3 (5 * (8 * k + 3) + 1) = 5 * k + 2 ∧ 5 * k + 2 < 8 * k + 3 := by
  constructor
  · have h0 : 5 * (8 * k + 3) + 1 = 40 * k + 16 := by omega
    rw [h0]
    simp [T_iter, T]
    omega
  · omega

end GettysburgCollatz
