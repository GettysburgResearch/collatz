import SectionDynamics
import CollatzGlobalClosure.BandCollision

/-!
Strict ranks compose along actual marked returns only while every intermediate
ordinary state remains in their stated domain.  This file retains that floor;
large endpoints alone would not justify a finite-exception rank argument.
-/

namespace CollatzSectionFeatures

open CollatzShell CollatzShell.ForwardSection

theorem depth_one_of_mod_four {n : Nat} (mod : n % 4 = 1) :
    twos (n+1) = 1 := by
  have nz : n+1 ≠ 0 := by omega
  have lower : 1 ≤ twos (n+1) :=
    (Nat.prime_two.pow_dvd_iff_le_factorization nz).mp (by norm_num; omega)
  have upper : ¬ 2 ≤ twos (n+1) := by
    intro too
    have := (Nat.prime_two.pow_dvd_iff_le_factorization nz).mpr too
    norm_num at this
    omega
  omega

/-- A strict first-return rank drops across every positive ordinary segment
between marks, provided the whole segment stays above the exception cutoff. -/
theorem rank_drop_at_marked_endpoint {A : Type*} [Preorder A]
    (rank : Nat → A) (B : Nat)
    (dec : ∀ n, B < n → 1 < n → Marked n → rank (next n) < rank n)
    (n t : Nat) (marked : Marked n) (tp : 0 < t)
    (floor : ∀ j ≤ t, B < orbit j n ∧ 1 < orbit j n)
    (endpoint : Marked (orbit t n)) : rank (orbit t n) < rank n := by
  induction t using Nat.strong_induction_on generalizing n with
  | h t ih =>
    have initial := floor 0 (by omega)
    change B < n ∧ 1 < n at initial
    have np : 0 < n := by omega
    let r := returnTime n
    have rp : 0 < r := by dsimp [r,returnTime]; omega
    have rt : r ≤ t := returnTime_min np tp endpoint
    have first : rank (next n) < rank n := dec n initial.1 initial.2 marked
    by_cases eq : r = t
    · have hit : next n = orbit t n := by
        change orbit r n = orbit t n
        rw [eq]
      simpa only [hit] using first
    · have dpos : 0 < t-r := by omega
      have dlt : t-r < t := by omega
      have hit : orbit (t-r) (next n) = orbit t n := by
        change orbit (t-r) (orbit r n) = orbit t n
        rw [← orbit_add, Nat.add_sub_of_le rt]
      have floor' : ∀ j ≤ t-r, B < orbit j (next n) ∧ 1 < orbit j (next n) := by
        intro j hj
        have base := floor (r+j) (by omega)
        rw [orbit_add] at base
        exact base
      have endpoint' : Marked (orbit (t-r) (next n)) := by rwa [hit]
      have rest := ih (t-r) dlt (next n) (next_marked n np) dpos floor' endpoint'
      rw [hit] at rest
      exact rest.trans first

theorem orbit_halving_floor (k n : Nat) : n ≤ 2^k * orbit k n := by
  induction k generalizing n with
  | zero => simp [orbit]
  | succ k ih =>
    have one : n ≤ 2 * step n := by
      unfold step
      split <;> omega
    calc n ≤ 2 * step n := one
         _ ≤ 2 * (2^k * orbit k (step n)) := Nat.mul_le_mul_left 2 (ih (step n))
         _ = 2^(k+1) * orbit (k+1) n := by simp only [orbit,pow_succ]; ring

/-- No function of binary exponent and trailing-one depth is a strict
first-return rank beyond a finite cutoff. No monotonicity, computability,
linearity, or well-foundedness assumption on the function is needed. -/
theorem no_eventual_feature_rank {A : Type*} [Preorder A]
    (F : Nat × Nat → A) :
    ¬ ∃ B, ∀ n, B < n → 1 < n → Marked n →
      F ((next n).log2,twos (next n+1)) < F (n.log2,twos (n+1)) := by
  rintro ⟨B,dec⟩
  obtain ⟨n,m,t,_,_,_,mn,mm,lg,n4,m4,tp,hit,_,guard⟩ :=
    CollatzBandCollision.cofinal_equal_features (B+1)
  let rank : Nat → A := fun x => F (x.log2,twos (x+1))
  have floor : ∀ j ≤ t, B < orbit j n ∧ 1 < orbit j n := by
    intro j jt
    have upper : n ≤ 2^t * orbit j n :=
      (orbit_halving_floor j n).trans
        (Nat.mul_le_mul_right _ (Nat.pow_le_pow_right (by decide) jt))
    have product : 2^t * (B+2) ≤ 2^t * orbit j n := by
      calc _ = (B+1+1)*2^t := by ring
           _ ≤ n := guard
           _ ≤ _ := upper
    have bound := Nat.le_of_mul_le_mul_left product (by positivity : 0 < 2^t)
    omega
  have endpoint : Marked (orbit t n) := by rwa [hit]
  have drop := rank_drop_at_marked_endpoint rank B dec n t mn tp floor endpoint
  have same : rank m = rank n := by
    dsimp [rank]
    rw [depth_one_of_mod_four n4,depth_one_of_mod_four m4,lg]
  rw [hit,same] at drop
  exact (lt_irrefl (rank n)) drop

#print axioms depth_one_of_mod_four
#print axioms rank_drop_at_marked_endpoint
#print axioms orbit_halving_floor
#print axioms no_eventual_feature_rank

end CollatzSectionFeatures
