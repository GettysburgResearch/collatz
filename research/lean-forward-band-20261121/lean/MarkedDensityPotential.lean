import InverseDensityPotential

/-!
The inverse-density upper envelope is needed only on the forced marked
section.  The threshold barrier propagates a small final normalized value
backwards through the whole ordinary odd segment.  No continuity from a
dyadic ray to its neighboring integers is assumed.
-/

namespace CollatzShell.InverseDensityPotential

open ForwardSection

theorem odd_orbit_unit {n : Nat} (hn : OddUnit n) (k : Nat) :
    OddUnit (oddOrbit n k) := by
  cases k with
  | zero => exact hn
  | succ k => exact odd_step_unit (oddOrbit n k)

theorem odd_orbit_add (n i j : Nat) :
    oddOrbit n (i+j) = oddOrbit (oddOrbit n i) j := by
  induction j with
  | zero => rfl
  | succ j ih => change oddStep (oddOrbit n (i+j)) = _; rw [ih]; rfl

theorem odd_orbit_succ_start (n k : Nat) :
    oddOrbit n (k+1) = oddOrbit (oddStep n) k := by
  rw [show k+1=1+k by omega, odd_orbit_add]
  rfl

/-- A public odd-clock version of the forced visit, proved from the imported
descent-or-section theorem.  Only existence is needed for this argument. -/
theorem marked_odd_visit (n : Nat) (hn : OddUnit n) :
    ∃ k : Nat, Marked (oddOrbit n k) := by
  induction n using Nat.strong_induction_on with
  | h n ih =>
    obtain ⟨i, _, drop | inBand⟩ := descent_or_section n hn.2.1
    · have hi := odd_orbit_unit hn i
      have less : oddOrbit n i < n := by omega
      obtain ⟨j, mark⟩ := ih _ less hi
      refine ⟨i+j, ?_⟩
      rw [odd_orbit_add]
      exact mark
    · exact ⟨i, (odd_orbit_unit hn i).2.1, inBand⟩

theorem positive_marked_odd_return (n : Nat) (_hn : OddUnit n) :
    ∃ k : Nat, 0 < k ∧ Marked (oddOrbit n k) := by
  obtain ⟨j, mark⟩ := marked_odd_visit (oddStep n) (odd_step_unit n)
  refine ⟨j+1, by omega, ?_⟩
  rw [odd_orbit_succ_start]
  exact mark

theorem normalized_threshold_barrier
    {n q k x y c : ℝ} (hn : 0 < n) (hq : 0 < q)
    (hk : 2 ≤ k) (hc : 0 < c) (edge : k*q = 3*n+1)
    (transfer : 3*x+k*c ≤ k*y) (large : 2*c ≤ x/n) : 2*c ≤ y/q := by
  have hx : 2*c*n ≤ x := (le_div_iff₀ hn).mp large
  have hkc : 2*c ≤ k*c := mul_le_mul_of_nonneg_right hk hc.le
  have heq := congrArg (fun a : ℝ => 2*c*a) edge
  have hmul : k*(2*c*q) ≤ k*y := by nlinarith
  apply (le_div_iff₀ hq).mpr
  by_contra h
  have contrary := mul_lt_mul_of_pos_left (lt_of_not_ge h)
    (by linarith : 0 < k)
  exact (not_lt_of_ge hmul) contrary

theorem normalized_predecessor_small
    {F : Nat → ℝ} {c : ℝ} (hc : 0 < c)
    (transfer : AdditiveTransfer F c) {n : Nat} (hn : OddUnit n)
    (small : normalized F (oddStep n) < 2*c) : normalized F n < 2*c := by
  by_contra h
  have hq := odd_step_unit n
  have hk : (2:ℝ) ≤ (2:ℝ)^twos (3*n+1) := by
    exact_mod_cast Nat.le_self_pow
      (by have := odd_step_exponent_pos hn.2.1; omega : twos (3*n+1) ≠ 0) 2
  have edge : (2:ℝ)^twos (3*n+1)*(oddStep n:ℝ) = 3*(n:ℝ)+1 := by
    exact_mod_cast odd_step_split n
  have barrier := normalized_threshold_barrier
    (by exact_mod_cast hn.1) (by exact_mod_cast hq.1) hk hc edge
    (transfer n hn) (by simpa [normalized] using le_of_not_gt h)
  exact (not_lt_of_ge barrier) small

/-- Smallness is required only at the final endpoint of the segment. -/
theorem normalized_segment_increases
    {F : Nat → ℝ} {c : ℝ} (hc : 0 < c)
    (transfer : AdditiveTransfer F c) {n : Nat} (hn : OddUnit n)
    (k : Nat) (small : normalized F (oddOrbit n k) < 2*c) :
    normalized F n ≤ normalized F (oddOrbit n k) ∧
    (0 < k → normalized F n < normalized F (oddOrbit n k)) := by
  induction k with
  | zero => exact ⟨le_rfl, by omega⟩
  | succ k ih =>
    have hprev := odd_orbit_unit hn k
    have prevSmall : normalized F (oddOrbit n k) < 2*c :=
      normalized_predecessor_small hc transfer hprev small
    have earlier := ih prevSmall
    have last := normalized_increases hc transfer hprev prevSmall
    exact ⟨(earlier.1.trans_lt last).le, fun _ => earlier.1.trans_lt last⟩

def MarkedSublinear (F : Nat → ℝ) : Prop :=
  ∀ ε : ℝ, 0 < ε → ∃ M : Nat,
    ∀ n : Nat, M ≤ n → OddUnit n → Marked n → normalized F n < ε

theorem odd_orbit_inherits
    {P : Nat → Prop}
    (backward : ∀ n, OddUnit n → P (oddStep n) → P n)
    (n k : Nat) (hn : OddUnit n) (h : P (oddOrbit n k)) : P n := by
  induction k generalizing n with
  | zero => exact h
  | succ k ih =>
    apply backward n hn
    apply ih (oddStep n) (odd_step_unit n)
    simpa only [odd_orbit_succ_start] using h

/-- The finite-superlevel argument needs decay only at actual marked states.
Intermediate odd states may have no supplied upper bound. -/
theorem all_marked_units_of_floor
    {F : Nat → ℝ} {c : ℝ} {N : Nat} {P : Nat → Prop}
    (hc : 0 < c)
    (positive : ∀ n, OddUnit n → Marked n → 0 < normalized F n)
    (sublinear : MarkedSublinear F) (transfer : AdditiveTransfer F c)
    (small : ∀ n, N ≤ n → OddUnit n → Marked n → normalized F n < 2*c)
    (base : ∀ n, OddUnit n → Marked n → n < N → P n)
    (backward : ∀ n, OddUnit n → P (oddStep n) → P n) :
    ∀ n, OddUnit n → Marked n → P n := by
  classical
  intro n hn mark
  by_contra bad
  obtain ⟨M, hM⟩ := sublinear (normalized F n) (positive n hn mark)
  let S := (Finset.range M).filter
    (fun m => OddUnit m ∧ Marked m ∧ ¬ P m ∧ normalized F n ≤ normalized F m)
  have bounded : ∀ m, OddUnit m → Marked m →
      normalized F n ≤ normalized F m → m < M := by
    intro m hm marked ge
    by_contra h
    exact (not_lt_of_ge ge) (hM m (by omega) hm marked)
  have member : n ∈ S := by
    simp only [S, Finset.mem_filter, Finset.mem_range]
    exact ⟨bounded n hn mark le_rfl, hn, mark, bad, le_rfl⟩
  obtain ⟨m, hm, maximal⟩ := S.exists_max_image (normalized F) ⟨n, member⟩
  have data : OddUnit m ∧ Marked m ∧ ¬ P m ∧ normalized F n ≤ normalized F m :=
    (Finset.mem_filter.mp hm).2
  obtain ⟨k, kp, marked⟩ := positive_marked_odd_return m data.1
  have nextUnit := odd_orbit_unit data.1 k
  have nextBad : ¬ P (oddOrbit m k) := by
    intro h
    exact data.2.2.1 (odd_orbit_inherits backward m k data.1 h)
  have high : N ≤ oddOrbit m k := by
    by_contra h
    exact nextBad (base _ nextUnit marked (by omega))
  have endpointSmall := small _ high nextUnit marked
  have increase := (normalized_segment_increases hc transfer data.1 k endpointSmall).2 kp
  have nextGe := data.2.2.2.trans increase.le
  have nextMember : oddOrbit m k ∈ S := by
    simp only [S, Finset.mem_filter, Finset.mem_range]
    exact ⟨bounded _ nextUnit marked nextGe, nextUnit, marked, nextBad, nextGe⟩
  exact (not_lt_of_ge (maximal _ nextMember)) increase

/-- Every positive ordinary source hits one finite part of the marked band,
provided only the marked-band upper envelope. -/
theorem finite_marked_absorbing_floor
    {F : Nat → ℝ} {c : ℝ} (hc : 0 < c)
    (positive : ∀ n, OddUnit n → Marked n → 0 < normalized F n)
    (sublinear : MarkedSublinear F) (transfer : AdditiveTransfer F c) :
    ∃ N : Nat, ∀ n : Nat, 0 < n →
      ∃ q : Nat, OddUnit q ∧ Marked q ∧ q < N ∧ Hits n q := by
  obtain ⟨N, hN⟩ := sublinear (2*c) (by positivity)
  let P : Nat → Prop := fun n => ∃ q, OddUnit q ∧ Marked q ∧ q < N ∧ Hits n q
  have all : ∀ n, OddUnit n → Marked n → P n := by
    refine all_marked_units_of_floor (P := P) hc positive sublinear transfer hN ?_ ?_
    · intro n hn marked hsmall
      exact ⟨n, hn, marked, hsmall, 0, rfl⟩
    · intro n hn hnext
      rcases hnext with ⟨q, hq, marked, hqN, hit⟩
      have first : Hits n (oddStep n) := by
        simpa [oddOrbit] using odd_orbit_hit hn.2.1 1
      exact ⟨q, hq, marked, hqN, first.trans hit⟩
  refine ⟨N, ?_⟩
  intro n hn
  obtain ⟨a, ha, hit⟩ := hits_odd_unit n hn
  obtain ⟨k, marked⟩ := marked_odd_visit a ha
  have hu := odd_orbit_unit ha k
  obtain ⟨q, hq, mq, hqN, hitq⟩ := all _ hu marked
  exact ⟨q, hq, mq, hqN, hit.trans ((odd_orbit_hit ha.2.1 k).trans hitq)⟩

theorem universal_of_marked_inverse_envelope_and_base
    {F : Nat → ℝ} {c : ℝ} {N : Nat}
    (hc : 0 < c)
    (positive : ∀ n, OddUnit n → Marked n → 0 < normalized F n)
    (sublinear : MarkedSublinear F) (transfer : AdditiveTransfer F c)
    (small : ∀ n, N ≤ n → OddUnit n → Marked n → normalized F n < 2*c)
    (base : ∀ n, OddUnit n → Marked n → n < N → Basin n) : Universal := by
  have all : ∀ n, OddUnit n → Marked n → Basin n :=
    all_marked_units_of_floor hc positive sublinear transfer small base
      (fun n hn h => (basin_at_hit (by
        simpa [oddOrbit] using odd_orbit_hit hn.2.1 1)).mpr h)
  intro n hn
  obtain ⟨a, ha, hit⟩ := hits_odd_unit n hn
  obtain ⟨k, marked⟩ := marked_odd_visit a ha
  have hu := odd_orbit_unit ha k
  exact (basin_at_hit (hit.trans (odd_orbit_hit ha.2.1 k))).mpr (all _ hu marked)

end CollatzShell.InverseDensityPotential

#print axioms CollatzShell.InverseDensityPotential.normalized_segment_increases
#print axioms CollatzShell.InverseDensityPotential.finite_marked_absorbing_floor
#print axioms CollatzShell.InverseDensityPotential.universal_of_marked_inverse_envelope_and_base
