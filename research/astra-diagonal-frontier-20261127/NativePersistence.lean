import NativeCriterion

/-!
The actual principal-source mass is unconditionally Cauchy. Its possible
nonzero remainder consists exactly of sources passing every native gate.
The finite set of persistent old sources is not a decidable certificate.
No rate for the exhaustion of the other old sources is supplied.
-/
set_option autoImplicit false
set_option warningAsError true

namespace Collatz.NativeGate

def Permanent (x : ℕ) : Prop := ∀ k, Gate k x

noncomputable def permanentSources (k : ℕ) : Finset ℕ := by
  classical
  exact (candidates k).filter Permanent

noncomputable def permanentMass (k : ℕ) : ℚ :=
  ∑ x ∈ permanentSources k, (x:ℚ)⁻¹

theorem permanent_not_reachesOne {x : ℕ} (h : Permanent x) : ¬ ReachesOne x := by
  intro hx
  obtain ⟨k, hk⟩ := reachesOne_fails_gate hx
  exact hk (h k)

theorem permanentSources_subset {k n : ℕ} (hkn : k ≤ n) :
    permanentSources k ⊆ candidates n := by
  classical
  intro x hx
  have hx' := Finset.mem_filter.mp (show x ∈ (candidates k).filter Permanent from hx)
  have hb := candidate_bounds hx'.1
  have hpow : 2^k ≤ 2^n := Nat.pow_le_pow_right (by omega) hkn
  simp only [candidates, Finset.mem_filter, Finset.mem_range]
  exact ⟨by omega, hb.1, hx'.2 n⟩

theorem permanentMass_nonnegative (k : ℕ) : 0 ≤ permanentMass k := by
  unfold permanentMass
  exact Finset.sum_nonneg (fun x _ => by positivity)

theorem permanentMass_le_mass {k n : ℕ} (hkn : k ≤ n) :
    permanentMass k ≤ mass n := by
  unfold permanentMass mass
  exact Finset.sum_le_sum_of_subset_of_nonneg (permanentSources_subset hkn)
    (fun x _ _ => by positivity)

theorem atom_le_permanentMass {x k : ℕ} (hx : 0 < x)
    (hk : x ≤ 2^k) (hp : Permanent x) : (x:ℚ)⁻¹ ≤ permanentMass k := by
  classical
  unfold permanentMass
  apply Finset.single_le_sum (f := fun i : ℕ => (i:ℚ)⁻¹)
    (fun i _ => inv_nonneg.mpr (Nat.cast_nonneg i))
  apply Finset.mem_filter.mpr
  constructor
  · simp only [candidates, Finset.mem_filter, Finset.mem_range]
    exact ⟨by omega, hx, hp k⟩
  · exact hp

theorem permanentMass_mono : Monotone permanentMass := by
  classical
  intro k n hkn
  unfold permanentMass
  apply Finset.sum_le_sum_of_subset_of_nonneg
  · intro x hx
    have hp := (Finset.mem_filter.mp
      (show x ∈ (candidates k).filter Permanent from hx)).2
    exact Finset.mem_filter.mpr ⟨permanentSources_subset hkn hx, hp⟩
  · intro x _ _
    positivity

theorem finite_temporary_exhaustion (k : ℕ) :
    ∃ j, ∀ n, ∀ x ∈ candidates k,
      Gate (k+j+n) x → Permanent x := by
  classical
  let temporary := (candidates k).filter (fun x => ¬ Permanent x)
  have hf : ∀ x ∈ temporary, ∃ j, ¬ Gate j x := by
    intro x hx
    have hp : ¬ ∀ j, Gate j x := (Finset.mem_filter.mp hx).2
    exact not_forall.mp hp
  obtain ⟨j, hj⟩ := finite_gate_failure temporary hf
  refine ⟨j, ?_⟩
  intro n x hx hg
  by_contra hp
  exact hj x (Finset.mem_filter.mpr ⟨hx, hp⟩) (gate_mono hg (by omega))

theorem mass_le_permanent_add_high (k n : ℕ) (hkn : k ≤ n)
    (hstable : ∀ x ∈ candidates k, Gate n x → Permanent x) :
    mass n ≤ permanentMass k + highMass (2^k) n := by
  classical
  let low := (candidates n).filter (fun x => x ≤ 2^k)
  have hsubset : low ⊆ permanentSources k := by
    intro x hx
    obtain ⟨hxn, hsmall⟩ := Finset.mem_filter.mp hx
    have hb := candidate_bounds hxn
    have hxk : x ∈ candidates k := by
      simp only [candidates, Finset.mem_filter, Finset.mem_range]
      exact ⟨by omega, hb.1, gate_mono hb.2.2 hkn⟩
    exact Finset.mem_filter.mpr ⟨hxk, hstable x hxk hb.2.2⟩
  have hlow : (∑ x ∈ low, (x:ℚ)⁻¹) ≤ permanentMass k := by
    exact Finset.sum_le_sum_of_subset_of_nonneg hsubset (fun x _ _ => by positivity)
  have hsplit : mass n = (∑ x ∈ low, (x:ℚ)⁻¹) + highMass (2^k) n := by
    simp only [mass, low, highMass, Finset.sum_filter, ← Finset.sum_add_distrib]
    apply Finset.sum_congr rfl
    intro x _
    by_cases hx : x ≤ 2^k
    · simp [hx, Nat.not_lt.mpr hx]
    · simp [hx, Nat.lt_of_not_ge hx]
  linarith

/-- Every fixed old-source cutoff approximates the entire eventual mass.
The onset is obtained by exhausting a finite collection of nonpermanent
sources; its existence is unconditional, but no computable bound is asserted. -/
theorem eventual_permanent_sandwich (k : ℕ) :
    ∃ j, ∀ n,
      permanentMass k ≤ mass (k+j+n) ∧
      mass (k+j+n) ≤ permanentMass k + reserve k := by
  obtain ⟨j, hj⟩ := finite_temporary_exhaustion k
  refine ⟨j, ?_⟩
  intro n
  constructor
  · exact permanentMass_le_mass (by omega)
  · have h := mass_le_permanent_add_high k (k+j+n) (by omega) (hj n)
    have ht := future_highMass k (j+n)
    rw [← Nat.add_assoc] at ht
    linarith

/-- The actual rational masses are Cauchy, whether or not Collatz is true. -/
theorem mass_rational_cauchy (L : ℕ) (hL : 0 < L) :
    ∃ N, ∀ n ≥ N, ∀ m ≥ N, |mass n - mass m| < (L:ℚ)⁻¹ := by
  let k := 4800*L
  obtain ⟨j, hj⟩ := eventual_permanent_sandwich k
  refine ⟨k+j, ?_⟩
  intro n hn m hm
  have hnn : k+j+(n-(k+j)) = n := by omega
  have hmm : k+j+(m-(k+j)) = m := by omega
  have h1 := hj (n-(k+j))
  have h2 := hj (m-(k+j))
  rw [hnn] at h1
  rw [hmm] at h2
  have hs : reserve k < (L:ℚ)⁻¹ := reserve_small L hL
  exact abs_lt.mpr ⟨by linarith, by linarith⟩

theorem permanentMass_tail (k n : ℕ) :
    permanentMass n ≤ permanentMass k + reserve k := by
  obtain ⟨j, hj⟩ := eventual_permanent_sandwich k
  have h1 := permanentMass_le_mass (show n ≤ k+j+n by omega)
  have h2 := (hj n).2
  linarith

theorem permanentMass_bound (k : ℕ) : permanentMass k ≤ 9 := by
  have h1 := permanentMass_le_mass (show k ≤ k by omega)
  have h2 := envelope_budget k
  have h3 := reserve_nonnegative k
  have h4 : 0 ≤ ∑ j ∈ Finset.range k, deaths j :=
    Finset.sum_nonneg (fun j _ => deaths_nonnegative j)
  linarith

theorem permanentMass_finite_certificate (L k : ℕ) (hL : 0 < L)
    (hsmall : permanentMass k + reserve k < (L:ℚ)⁻¹) :
    ∀ x, 0 < x → x ≤ L → ReachesOne x := by
  obtain ⟨j, hj⟩ := eventual_permanent_sandwich k
  have hm := (hj L).2
  have hpow := native_cutoff (k+j+L)
  apply finite_certificate L (k+j+L) hL (by omega)
  linarith

theorem universal_iff_permanentMass_zero :
    Universal ↔ ∀ k, permanentMass k = 0 := by
  classical
  constructor
  · intro h k
    unfold permanentMass
    apply Finset.sum_eq_zero
    intro x hx
    obtain ⟨hc, hp⟩ := Finset.mem_filter.mp
      (show x ∈ (candidates k).filter Permanent from hx)
    exact False.elim (permanent_not_reachesOne hp (h x (candidate_bounds hc).1))
  · intro h x hx
    apply permanentMass_finite_certificate x (4800*x) hx
    · rw [h, zero_add]
      exact reserve_small x hx
    · exact hx
    · exact le_rfl

end Collatz.NativeGate
