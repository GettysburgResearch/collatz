import CollatzGlobal.Expansion

/-!
Global inverse-descent geometry. These statements rule out a proposed complete
inverse-return selector: even an unbounded dictionary cannot reduce every
certified odd ternary unit to a smaller certified odd ternary unit by an
ordinary forward path from the smaller input. Mixed forward/backward or
non-orbit certificate transformations are not ruled out.
-/

open CollatzReverseBasin CollatzClosure

namespace CollatzGlobal

theorem small_orbit_bound (n : Nat) (hn : n ≤ 2) (t : Nat) :
    orbit n t ≤ 2 := by
  induction t generalizing n with
  | zero => exact hn
  | succ t ih =>
    apply ih
    unfold shortcut
    split <;> omega

/-- A supplied terminating certificate bounds the entire ordinary forward
orbit, including every step after the first visit to one. -/
theorem basin_orbit_bounded {n : Nat} (hn : Basin n) :
    ∃ M : Nat, ∀ t : Nat, orbit n t ≤ M := by
  obtain ⟨d, hd⟩ := hn
  induction d generalizing n with
  | zero =>
    change n = 1 at hd
    subst n
    exact ⟨2, fun t => small_orbit_bound 1 (by omega) t⟩
  | succ d ih =>
    obtain ⟨M,hM⟩ := ih hd
    refine ⟨max n M, ?_⟩
    intro t
    cases t with
    | zero => exact Nat.le_max_left n M
    | succ t => exact Nat.le_trans (hM t) (Nat.le_max_right n M)

/-- Finitely many certified sources have a common bound on all their forward
orbits. This is a finite maximum, not a uniform Collatz height bound. -/
theorem finite_basin_orbits_bounded (P : Nat → Prop) (B : Nat)
    (hP : ∀ n, P n → Basin n) :
    ∃ M : Nat, ∀ n, P n → n ≤ B → ∀ t, orbit n t ≤ M := by
  classical
  induction B with
  | zero =>
    refine ⟨2, ?_⟩
    intro n _ hn t
    exact small_orbit_bound n (by omega) t
  | succ B ih =>
    obtain ⟨M,hM⟩ := ih
    by_cases hnew : P (B+1)
    · obtain ⟨K,hK⟩ := basin_orbit_bounded (hP (B+1) hnew)
      refine ⟨max M K, ?_⟩
      intro n hn hle t
      by_cases hold : n ≤ B
      · exact Nat.le_trans (hM n hn hold t) (Nat.le_max_left M K)
      · have eq : n = B+1 := by omega
        subst n
        exact Nat.le_trans (hK t) (Nat.le_max_right M K)
    · refine ⟨M, ?_⟩
      intro n hn hle t
      have hold : n ≤ B := by
        by_cases hh : n ≤ B
        · exact hh
        · have eq : n = B+1 := by omega
          subst n
          exact False.elim (hnew hn)
      exact hM n hn hold t

/-- Global geometric obstruction: a strict inverse-reachability induction from
finitely many sources with bounded forward orbits cannot cover an unbounded
domain. No affine restriction or bounded word length occurs in this statement. -/
theorem no_inverse_descent_cover (P : Nat → Prop) (B M : Nat)
    (hunbounded : ∀ K, ∃ q, P q ∧ K < q)
    (hbase : ∀ b, P b → b ≤ B → ∀ t, orbit b t ≤ M) :
    ¬ (∀ q, P q → B < q →
      ∃ x t, P x ∧ x < q ∧ orbit x t = q) := by
  intro cover
  have bounded : ∀ q, P q → ∀ t, orbit q t ≤ M := by
    intro q
    induction q using Nat.strong_induction_on with
    | h q ih =>
      intro hq
      by_cases hb : q ≤ B
      · exact hbase q hq hb
      · obtain ⟨x,u,hx,hsmall,heq⟩ := cover q hq (by omega)
        intro t
        rw [← heq, ← orbit_add x u t]
        exact ih x hsmall hx (u+t)
  obtain ⟨q,hq,hlarge⟩ := hunbounded M
  have bad := bounded q hq 0
  change q ≤ M at bad
  omega

/-- An unbounded certified domain has arbitrarily large inputs with no smaller
ancestor inside that same domain. -/
theorem arbitrarily_large_inverse_minimal (P : Nat → Prop)
    (hP : ∀ n, P n → Basin n)
    (hunbounded : ∀ K, ∃ q, P q ∧ K < q) (B : Nat) :
    ∃ q, P q ∧ B < q ∧
      ¬ (∃ x t, P x ∧ x < q ∧ orbit x t = q) := by
  classical
  obtain ⟨M,hM⟩ := finite_basin_orbits_bounded P B hP
  have hno := no_inverse_descent_cover P B M hunbounded hM
  apply Classical.byContradiction
  intro h
  apply hno
  intro q hq hlarge
  apply Classical.byContradiction
  intro hh
  exact h ⟨q,hq,hlarge,hh⟩

/-- Positive certified odd ternary units. -/
def CertifiedUnit (n : Nat) : Prop :=
  0 < n ∧ n % 2 = 1 ∧ n % 3 ≠ 0 ∧ Basin n

theorem basin_four_succ (n : Nat) (hodd : n % 2 = 1) (hbasin : Basin n) :
    Basin (4*n+1) := by
  have h := (basin_odd n hodd).mpr hbasin
  exact (basin_exch (4*n+1) (3*n+1) n rfl rfl).mpr h

/-- A fully explicit unbounded certified family in one unit class. -/
theorem certified_lift (n : Nat) (hmod : n % 6 = 1) (hbasin : Basin n) :
    (64*n+21) % 6 = 1 ∧ Basin (64*n+21) := by
  have h1 := basin_four_succ n (by omega) hbasin
  have h2 := basin_four_succ (4*n+1) (by omega) h1
  have h3 := basin_four_succ (4*(4*n+1)+1) (by omega) h2
  constructor
  · omega
  · have heq : 4*(4*(4*n+1)+1)+1 = 64*n+21 := by omega
    rwa [heq] at h3

theorem certified_units_unbounded : ∀ K, ∃ q, CertifiedUnit q ∧ K < q := by
  have family : ∀ K, ∃ q, q % 6 = 1 ∧ Basin q ∧ K < q := by
    intro K
    induction K with
    | zero => exact ⟨1,by decide,⟨0,rfl⟩,by omega⟩
    | succ K ih =>
      obtain ⟨q,hmod,hbasin,hlarge⟩ := ih
      obtain ⟨hnewmod,hnewbasin⟩ := certified_lift q hmod hbasin
      exact ⟨64*q+21,hnewmod,hnewbasin,by omega⟩
  intro K
  obtain ⟨q,hmod,hbasin,hlarge⟩ := family K
  exact ⟨q,⟨by omega,by omega,by omega,hbasin⟩,hlarge⟩

/-- Unconditional all-rank obstruction to a complete inverse return dictionary,
including arbitrary supplied words and arbitrarily many exceptional bases. -/
theorem certified_units_inverse_minimal (B : Nat) :
    ∃ q, CertifiedUnit q ∧ B < q ∧
      ¬ (∃ x t, CertifiedUnit x ∧ x < q ∧ orbit x t = q) := by
  exact arbitrarily_large_inverse_minimal CertifiedUnit
    (fun _ h => h.2.2.2) certified_units_unbounded B


/-- An expanding actual word ending at a point that agrees with one to ternary
precision K must use more than K odd inputs. This includes all ordinary lifts
of the whole ternary cylinder, not a finite sample of its endpoints. -/
theorem expansion_depth_for_endpoint_lift (n t K r : Nat)
    (hexpand : 2^t < 3^(oddCount n t))
    (hend : orbit n t = 1 + 3^K*r) :
    K < oddCount n t := by
  by_cases hlt : K < oddCount n t
  · exact hlt
  · have hp : oddCount n t ≤ K := by omega
    have hpower : 1 < 3^(oddCount n t) := by
      have := Nat.two_pow_pos t
      omega
    have hdiv : 3^(oddCount n t) ∣ 3^K := by
      refine ⟨3^(K-oddCount n t), ?_⟩
      rw [← Nat.pow_add]
      congr 1
      omega
    have hmod : (1 + 3^K*r) % 3^(oddCount n t) = 1 := by
      rw [Nat.add_mod, Nat.mul_mod, Nat.mod_eq_zero_of_dvd hdiv]
      simp [Nat.mod_eq_of_lt hpower]
    have bad := expanding_endpoint_not_one_mod n t hexpand
    rw [hend] at bad
    exact False.elim (bad hmod)

/-- Thus an arbitrary (possibly infinite) collection of expanding words whose
odd counts are bounded by K misses every endpoint 1+3^K*r. A finite dictionary
is a special case. -/
theorem bounded_expansion_misses_lift (n t K r : Nat)
    (hbound : oddCount n t ≤ K) :
    ¬ (2^t < 3^(oddCount n t) ∧ orbit n t = 1 + 3^K*r) := by
  intro h
  have hdeep := expansion_depth_for_endpoint_lift n t K r h.1 h.2
  omega

end CollatzGlobal
