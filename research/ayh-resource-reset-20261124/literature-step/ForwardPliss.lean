import Mathlib.Data.Int.LeastGreatest
import Mathlib.Data.Finset.Card
import Mathlib.Data.Finset.Range
import Mathlib.Tactic.Linarith
import Mathlib.Tactic

/-! A forward integer form of the Pliss selection argument.  Its records may
depend on the entire future.  No stopping-time or source-measure claim is made. -/
namespace CollatzForwardPliss

open scoped Classical

def FutureRecord (W : ℕ → ℤ) (s : ℕ) : Prop :=
  ∀ t, s ≤ t → W s ≤ W t

/-- Linear lower growth makes every integer tail attain its minimum. -/
theorem tail_minimum_exists (W : ℕ → ℤ) (C : ℤ)
    (lower : ∀ t : ℕ, (t : ℤ) - C ≤ W t) :
    ∃ M : ℕ → ℤ,
      (∀ s, ∃ t, s ≤ t ∧ W t = M s) ∧
      (∀ s t, s ≤ t → M s ≤ W t) := by
  have ex : ∀ s, ∃ v : ℤ,
      (∃ t, s ≤ t ∧ W t = v) ∧ (∀ t, s ≤ t → v ≤ W t) := by
    intro s
    obtain ⟨v, hv, least⟩ := Int.exists_least_of_bdd
      (P := fun v => ∃ t, s ≤ t ∧ W t = v)
      (by
        refine ⟨-C, ?_⟩
        rintro v ⟨t, _, rfl⟩
        have h := lower t
        omega)
      ⟨W s, s, le_rfl, rfl⟩
    exact ⟨v, hv, fun t ht => least (W t) ⟨t, ht, rfl⟩⟩
  choose M attain least using ex
  exact ⟨M, attain, least⟩

/-- A finite quantitative bound for all-future records.  It counts ordinary
time indices, and supplies no distribution for an input chosen at such a time. -/
theorem forward_record_count (W : ℕ → ℤ) (C A : ℤ)
    (hA : 0 ≤ A) (lower : ∀ t : ℕ, (t : ℤ) - C ≤ W t)
    (upper_step : ∀ t, W (t+1) ≤ W t + A) (N : ℕ) :
    (N : ℤ) - C - W 0 ≤
      A * (((Finset.range N).filter (FutureRecord W)).card : ℤ) := by
  classical
  obtain ⟨M, attain, least⟩ := tail_minimum_exists W C lower
  have mono : ∀ s, M s ≤ M (s+1) := by
    intro s
    obtain ⟨t, ht, eq⟩ := attain (s+1)
    rw [← eq]
    exact least s t (by omega)
  have jump : ∀ s, M (s+1) - M s ≤ if FutureRecord W s then A else 0 := by
    intro s
    obtain ⟨t, ht, eq⟩ := attain s
    by_cases hst : t = s
    · subst t
      have hr : FutureRecord W s := by
        intro v hv
        rw [eq]
        exact least s v hv
      rw [ite_eq_left hr]
      have next := least (s+1) (s+1) le_rfl
      have up := upper_step s
      omega
    · have same_le : M (s+1) ≤ M s := by
        rw [← eq]
        exact least (s+1) t (by omega)
      have same := mono s
      split_ifs <;> omega
  have telescoping : ∀ T : ℕ, M T - M 0 ≤
      A * (((Finset.range T).filter (FutureRecord W)).card : ℤ) := by
    intro T
    induction T with
    | zero => simp
    | succ T ih =>
      have hj := jump T
      by_cases hr : FutureRecord W T
      · have fresh : T ∉ (Finset.range T).filter (FutureRecord W) := by simp
        simp only [Finset.range_add_one, Finset.filter_insert, ite_eq_left hr,
          Finset.card_insert_of_notMem fresh, Nat.cast_add, Nat.cast_one]
        rw [ite_eq_left hr] at hj
        linarith
      · simp only [Finset.range_add_one, Finset.filter_insert, ite_eq_right hr]
        rw [ite_eq_right hr] at hj
        linarith
  have terminal : (N : ℤ) - C ≤ M N := by
    obtain ⟨t, ht, eq⟩ := attain N
    have h := lower t
    omega
  have initial : M 0 ≤ W 0 := least 0 0 le_rfl
  have bound := telescoping N
  omega

/-- The normalization used by the Collatz odd-count separation: if
8*d(t) >= t-C and d has increments at most one, then at least
(N-2*C)/15 time indices start a uniformly biased infinite future. -/
theorem parity_excess_record_count (d : ℕ → ℤ) (C : ℤ)
    (initial : d 0 = 0) (lower : ∀ t : ℕ, (t : ℤ) - C ≤ 8 * d t)
    (increment : ∀ t, d (t+1) ≤ d t + 1) (N : ℕ) :
    (N : ℤ) - 2*C ≤
      15 * (((Finset.range N).filter
        (fun s => ∀ b : ℕ, (b : ℤ) ≤ 16 * (d (s+b) - d s))).card : ℤ) := by
  classical
  let W : ℕ → ℤ := fun t => 16*d t - t
  have low : ∀ t : ℕ, (t : ℤ) - 2*C ≤ W t := by
    intro t
    dsimp [W]
    have h := lower t
    omega
  have up : ∀ t, W (t+1) ≤ W t + 15 := by
    intro t
    dsimp [W]
    have h := increment t
    omega
  have main := forward_record_count W (2*C) 15 (by decide) low up N
  have rec_eq : FutureRecord W =
      (fun s => ∀ b : ℕ, (b : ℤ) ≤ 16 * (d (s+b) - d s)) := by
    funext s
    apply propext
    constructor
    · intro hs b
      have h := hs (s+b) (by omega)
      dsimp [W] at h
      omega
    · intro hs t ht
      have h := hs (t-s)
      have st : s+(t-s)=t := by omega
      rw [st] at h
      dsimp [W]
      have cast : ((t-s : ℕ) : ℤ) = (t : ℤ) - s := by omega
      rw [cast] at h
      omega
  rw [rec_eq] at main
  simpa [W, initial] using main

#print axioms tail_minimum_exists
#print axioms forward_record_count
#print axioms parity_excess_record_count

end CollatzForwardPliss
