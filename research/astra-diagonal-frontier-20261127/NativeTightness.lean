import NativeTransfer

/-!
The unbounded future's new source mass is charged to the reserve at one
fixed native clock.  Finitely many old sources can then be handled
individually, without changing their ordinary representatives.
-/
set_option autoImplicit false
set_option warningAsError true

namespace Collatz.NativeGate

def highMass (cutoff k : ℕ) : ℚ :=
  ∑ x ∈ candidates k, if cutoff < x then (x:ℚ)⁻¹ else 0

theorem highMass_nonnegative (cutoff k : ℕ) : 0 ≤ highMass cutoff k := by
  unfold highMass
  apply Finset.sum_nonneg
  intro x _
  split_ifs <;> positivity

theorem highMass_step (cutoff k : ℕ) :
    highMass cutoff (k+1) ≤ highMass cutoff k+births k := by
  unfold highMass births
  rw [sum_children, ← Finset.sum_add_distrib]
  apply Finset.sum_le_sum
  intro x _
  have h0 : (0:ℚ) ≤ (x:ℚ)⁻¹ := by positivity
  have h1 : (0:ℚ) ≤ ((x+2^k:ℕ):ℚ)⁻¹ := by positivity
  split_ifs <;> linarith

theorem highMass_reserve_step (cutoff k : ℕ) :
    highMass cutoff (k+1)+reserve (k+1) ≤ highMass cutoff k+reserve k := by
  have h := highMass_step cutoff k
  have hb := births_le_budget k
  have hr := reserve_decreases k
  linarith

theorem highMass_initial (k : ℕ) : highMass (2^k) k = 0 := by
  unfold highMass
  apply Finset.sum_eq_zero
  intro x hx
  have h := (candidate_bounds hx).2.1
  simp only [show ¬ 2^k < x by omega, ite_false]

theorem future_highMass_budget (k n : ℕ) :
    highMass (2^k) (k+n)+reserve (k+n) ≤ reserve k := by
  induction n with
  | zero => simp [highMass_initial]
  | succ n ih =>
    have h := highMass_reserve_step (2^k) (k+n)
    rw [show k+(n+1) = (k+n)+1 by omega]
    linarith

theorem future_highMass (k n : ℕ) : highMass (2^k) (k+n) ≤ reserve k := by
  have h := future_highMass_budget k n
  have hr := reserve_nonnegative (k+n)
  linarith

theorem gate_mono {x k n : ℕ} (h : Gate n x) (hkn : k ≤ n) : Gate k x := by
  intro j hj
  exact h j (by omega)

theorem odds_add (x k n : ℕ) : odds x (k+n) = odds x k+odds (orbit x k) n := by
  induction n with
  | zero => simp [odds]
  | succ n ih =>
    rw [show k+(n+1) = (k+n)+1 by omega]
    simp only [odds, orbit_add, ih]
    omega

theorem one_even_clock (n : ℕ) : orbit 1 (2*n) = 1 ∧ odds 1 (2*n) = n := by
  induction n with
  | zero => simp [orbit, odds]
  | succ n ih =>
    rw [show 2*(n+1) = 2*n+2 by omega, orbit_add, odds_add, ih.1, ih.2]
    norm_num [orbit, odds, step]

theorem reachesOne_fails_gate {x : ℕ} (h : ReachesOne x) : ∃ k, ¬ Gate k x := by
  obtain ⟨k, hk⟩ := h
  let t := 7*odds x k+1
  refine ⟨k+2*t, ?_⟩
  intro hg
  have hgate := hg (k+2*t) (by omega)
  rw [odds_add, hk, (one_even_clock t).2] at hgate
  dsimp [t] at hgate
  omega

theorem finite_gate_failure (s : Finset ℕ)
    (h : ∀ x ∈ s, ∃ k, ¬ Gate k x) : ∃ k, ∀ x ∈ s, ¬ Gate k x := by
  induction s using Finset.induction_on with
  | empty => exact ⟨0, by simp⟩
  | @insert a s ha ih =>
    obtain ⟨i, hi⟩ := h a (by simp)
    obtain ⟨j, hj⟩ := ih (fun x hx => h x (by simp [hx]))
    refine ⟨i+j, ?_⟩
    intro x hx hg
    rcases Finset.mem_insert.mp hx with rfl | hx
    · exact hi (gate_mono hg (by omega))
    · exact hj x hx (gate_mono hg (by omega))

theorem low_sources_exhausted (k n : ℕ) (hn : k ≤ n)
    (hdead : ∀ x ∈ candidates k, ¬ Gate n x) : mass n = highMass (2^k) n := by
  unfold mass highMass
  apply Finset.sum_congr rfl
  intro x hx
  have hp := (candidate_bounds hx).1
  have hg := (candidate_bounds hx).2.2
  have hlarge : 2^k < x := by
    by_contra hsmall
    have hmem : x ∈ candidates k := by
      simp only [candidates, Finset.mem_filter, Finset.mem_range]
      exact ⟨by omega, hp, gate_mono hg hn⟩
    exact hdead x hmem hg
  simp only [hlarge, ite_true]

theorem covered_eventual_mass (k : ℕ)
    (h : ∀ x ∈ candidates k, ReachesOne x) :
    ∃ j, ∀ n, mass (k+j+n) ≤ reserve k := by
  obtain ⟨j, hj⟩ := finite_gate_failure (candidates k) (fun x hx =>
    reachesOne_fails_gate (h x hx))
  refine ⟨j, ?_⟩
  intro n
  rw [low_sources_exhausted k (k+j+n) (by omega) (by
    intro x hx hg
    exact hj x hx (gate_mono hg (by omega)))]
  simpa only [Nat.add_assoc] using future_highMass k (j+n)

theorem universal_eventual_mass (h : Universal) (k : ℕ) :
    ∃ n, k ≤ n ∧ mass n ≤ reserve k := by
  obtain ⟨j, hj⟩ := covered_eventual_mass k
    (fun x hx => h x (candidate_bounds hx).1)
  exact ⟨k+j, by omega, by simpa using hj 0⟩

end Collatz.NativeGate
