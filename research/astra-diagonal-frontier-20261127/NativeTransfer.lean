import NativeGate
import Mathlib.Tactic.FieldSimp

/-!
Exact ordinary-source cylinder transport for NativeGate.  The cylinder law
does not assert any independence after conditioning on an infinite survivor.
-/
set_option autoImplicit false
set_option warningAsError true

namespace Collatz.NativeGate

theorem orbit_succ_first (x k : ℕ) : orbit x (k+1) = orbit (step x) k := by
  induction k with
  | zero => rfl
  | succ k ih =>
    change step (orbit x (k+1)) = step (orbit (step x) k)
    rw [ih]

theorem odds_succ_first (x k : ℕ) : odds x (k+1) = x % 2 + odds (step x) k := by
  induction k with
  | zero => simp [odds, orbit]
  | succ k ih =>
    change odds x (k+1) + orbit x (k+1) % 2 =
      x % 2 + (odds (step x) k + orbit (step x) k % 2)
    rw [ih, orbit_succ_first]
    omega

theorem step_lift (x t : ℕ) :
    step (x + 2*t) = step x + 3^(x%2)*t := by
  have hp : x % 2 = 0 ∨ x % 2 = 1 := by omega
  rcases hp with hp | hp
  · have hq : (x + 2*t) % 2 = 0 := by omega
    simp only [step, hp, hq, ite_true, pow_zero, one_mul]
    omega
  · have hq : (x + 2*t) % 2 = 1 := by omega
    simp only [step, hp, hq, show ¬ (1 : ℕ) = 0 by decide, ite_false, pow_one]
    omega

/-- The two lifts have exactly the same k-bit itinerary.  The endpoint
separation retains its actual multiplier, including every odd step. -/
theorem cylinder_lift (x k t : ℕ) :
    odds (x + 2^k*t) k = odds x k ∧
    orbit (x + 2^k*t) k = orbit x k + 3^(odds x k)*t := by
  induction k generalizing x t with
  | zero => simp [odds, orbit]
  | succ k ih =>
    have heq : x + 2^(k+1)*t = x + 2*(2^k*t) := by ring
    have hp : (x + 2^(k+1)*t) % 2 = x % 2 := by rw [heq]; omega
    have hs : step (x + 2^(k+1)*t) = step x + 2^k*(3^(x%2)*t) := by
      rw [heq, step_lift]
      ring
    have h := ih (step x) (3^(x%2)*t)
    constructor
    · rw [odds_succ_first, hp, hs, h.1, odds_succ_first]
    · rw [orbit_succ_first, hs, h.2, orbit_succ_first, odds_succ_first, pow_add]
      ring

theorem gate_lift (x k t : ℕ) : Gate k (x + 2^k*t) ↔ Gate k x := by
  have heq (j : ℕ) (hj : j ≤ k) : odds (x + 2^k*t) j = odds x j := by
    obtain ⟨r, rfl⟩ := Nat.exists_eq_add_of_le hj
    have h := (cylinder_lift x j (2^r*t)).1
    simpa only [pow_add, Nat.mul_assoc] using h
  constructor <;> intro h j hj
  · simpa only [heq j hj] using h j hj
  · simpa only [heq j hj] using h j hj

theorem gate_succ (x k : ℕ) :
    Gate (k+1) x ↔ Gate k x ∧ 4*(k+1) ≤ 7*odds x (k+1) := by
  constructor
  · intro h
    exact ⟨fun j hj => h j (by omega), h (k+1) (by omega)⟩
  · rintro ⟨h, hn⟩ j hj
    by_cases he : j = k+1
    · simpa only [he] using hn
    · exact h j (by omega)

theorem candidate_bounds {x k : ℕ} (h : x ∈ candidates k) :
    0 < x ∧ x ≤ 2^k ∧ Gate k x := by
  simpa only [candidates, Finset.mem_filter, Finset.mem_range, Nat.lt_add_one_iff,
    and_assoc, and_left_comm] using h

/-- Complete two-child description at the next native clock. -/
theorem candidate_children (k : ℕ) :
    candidates (k+1) =
      ((candidates k) ∪ (candidates k).image (fun x => x + 2^k)).filter
        (fun x => Gate (k+1) x) := by
  ext x
  simp only [Finset.mem_filter, Finset.mem_union, Finset.mem_image]
  constructor
  · intro h
    obtain ⟨hx, hbound, hg⟩ := candidate_bounds h
    have hk := (gate_succ x k).mp hg |>.1
    refine ⟨?_, hg⟩
    by_cases hsmall : x ≤ 2^k
    · left
      simp only [candidates, Finset.mem_filter, Finset.mem_range]
      exact ⟨by omega, hx, hk⟩
    · right
      have hy : 0 < x-2^k ∧ x-2^k ≤ 2^k := by
        have hp : 2^(k+1) = 2^k*2 := by ring
        omega
      have heq : x-2^k + 2^k*1 = x := by omega
      refine ⟨x-2^k, ?_, by omega⟩
      simp only [candidates, Finset.mem_filter, Finset.mem_range]
      refine ⟨by omega, hy.1, ?_⟩
      exact (gate_lift (x-2^k) k 1).mp (by simpa only [heq] using hk)
  · rintro ⟨hparent, hg⟩
    simp only [candidates, Finset.mem_filter, Finset.mem_range]
    have hp : 2^(k+1) = 2^k*2 := by ring
    rcases hparent with h | ⟨y, hy, rfl⟩
    · obtain ⟨hx, hb, _⟩ := candidate_bounds h
      exact ⟨by omega, hx, hg⟩
    · obtain ⟨hypos, hybound, _⟩ := candidate_bounds hy
      exact ⟨by omega, by omega, hg⟩

theorem children_disjoint (k : ℕ) :
    Disjoint (candidates k) ((candidates k).image (fun x => x + 2^k)) := by
  apply Finset.disjoint_left.mpr
  intro x hx hy
  obtain ⟨y, hy0, he⟩ := Finset.mem_image.mp hy
  have hx' := candidate_bounds hx
  have hy' := candidate_bounds hy0
  omega

theorem sum_children (k : ℕ) (f : ℕ → ℚ) :
    (∑ x ∈ candidates (k+1), f x) =
      ∑ x ∈ candidates k,
        ((if Gate (k+1) x then f x else 0) +
         (if Gate (k+1) (x+2^k) then f (x+2^k) else 0)) := by
  rw [candidate_children, Finset.sum_filter, Finset.sum_union (children_disjoint k),
    Finset.sum_image]
  · rw [Finset.sum_add_distrib]
  · intro x _ y _ h
    exact Nat.add_right_cancel h

def debt (k x : ℕ) : ℚ := 7*(odds x k : ℚ)-4*(k : ℚ)
def reserveWeight (k x : ℕ) : ℚ := 2*debt k x+8
def reserve (k : ℕ) : ℚ := (∑ x ∈ candidates k, reserveWeight k x)/(2:ℚ)^k
def arrivalBudget (k : ℕ) : ℚ := (candidates k).card/(2:ℚ)^k
def deaths (k : ℕ) : ℚ :=
  ∑ x ∈ candidates k, if Gate (k+1) x then 0 else (x:ℚ)⁻¹
def births (k : ℕ) : ℚ :=
  ∑ x ∈ candidates k, if Gate (k+1) (x+2^k) then ((x+2^k:ℕ):ℚ)⁻¹ else 0

theorem mass_identity (k : ℕ) : mass (k+1)+deaths k = mass k+births k := by
  unfold mass deaths births
  rw [sum_children, ← Finset.sum_add_distrib, ← Finset.sum_add_distrib]
  apply Finset.sum_congr rfl
  intro x _
  split_ifs <;> ring

theorem births_le_budget (k : ℕ) : births k ≤ arrivalBudget k := by
  unfold births arrivalBudget
  calc
    _ ≤ ∑ _x ∈ candidates k, ((2:ℚ)^k)⁻¹ := by
      apply Finset.sum_le_sum
      intro x hx
      split_ifs
      · apply (inv_le_inv₀ (by positivity) (by
          have := (candidate_bounds hx).1
          positivity)).2
        norm_cast
        omega
      · positivity
    _ = _ := by simp [div_eq_mul_inv]

theorem debt_nonnegative_iff (k x : ℕ) : 0 ≤ debt k x ↔ 4*k ≤ 7*odds x k := by
  unfold debt
  constructor
  · intro h
    have h' : (4:ℚ)*k ≤ 7*(odds x k : ℚ) := by linarith
    exact_mod_cast h'
  · intro h
    have h' : (4:ℚ)*k ≤ 7*(odds x k : ℚ) := by exact_mod_cast h
    linarith

theorem next_gate_iff {k x : ℕ} (h : Gate k x) :
    Gate (k+1) x ↔ 0 ≤ debt (k+1) x := by
  rw [gate_succ, debt_nonnegative_iff]
  simp only [h, true_and]

theorem debt_next (k x : ℕ) :
    debt (k+1) x = debt k x + 7*(orbit x k % 2 : ℕ)-4 := by
  unfold debt
  simp only [odds, Nat.cast_add, Nat.cast_one]
  ring

theorem sibling_parity (k x : ℕ) :
    orbit x k % 2 + orbit (x+2^k) k % 2 = 1 := by
  have h := (cylinder_lift x k 1).2
  simp only [Nat.mul_one] at h
  rw [h, Nat.add_mod]
  have hp : 3^(odds x k) % 2 = 1 := by
    rw [Nat.pow_mod]
    norm_num
  rw [hp]
  omega

/-- The exact reserve inequality after grouping the actual two children. -/
theorem reserve_children {k x : ℕ} (hx : x ∈ candidates k) :
    2 + (if Gate (k+1) x then reserveWeight (k+1) x else 0) +
      (if Gate (k+1) (x+2^k) then reserveWeight (k+1) (x+2^k) else 0)
      ≤ 2*reserveWeight k x := by
  have hg := (candidate_bounds hx).2.2
  have hd : 0 ≤ debt k x := (debt_nonnegative_iff k x).mpr (hg k (by omega))
  have hg' : Gate k (x+2^k) := by
    simpa only [Nat.mul_one] using (gate_lift x k 1).mpr hg
  have hd' : debt k (x+2^k) = debt k x := by
    unfold debt
    have h := (cylinder_lift x k 1).1
    simpa only [Nat.mul_one] using congrArg (fun q : ℕ => 7*(q:ℚ)-4*(k:ℚ)) h
  have hp := sibling_parity k x
  have p0 : orbit x k % 2 = 0 ∨ orbit x k % 2 = 1 := by omega
  unfold reserveWeight
  simp only [next_gate_iff hg, next_gate_iff hg', debt_next, hd']
  rcases p0 with hp0 | hp0
  · have hp1 : orbit (x+2^k) k % 2 = 1 := by omega
    simp only [hp0, hp1, Nat.cast_zero, Nat.cast_one, mul_zero, mul_one, add_zero]
    split_ifs <;> linarith
  · have hp1 : orbit (x+2^k) k % 2 = 0 := by omega
    simp only [hp0, hp1, Nat.cast_zero, Nat.cast_one, mul_zero, mul_one, add_zero]
    split_ifs <;> linarith

theorem reserve_decreases (k : ℕ) : arrivalBudget k+reserve (k+1) ≤ reserve k := by
  have hs : (2:ℚ)*(candidates k).card +
      (∑ x ∈ candidates (k+1), reserveWeight (k+1) x) ≤
      2*(∑ x ∈ candidates k, reserveWeight k x) := by
    rw [sum_children, Finset.mul_sum]
    have h := Finset.sum_le_sum (s := candidates k)
      (fun x hx => reserve_children (k := k) hx)
    simpa only [Finset.sum_add_distrib, Finset.sum_const, nsmul_eq_mul, mul_comm,
      add_assoc] using h
  unfold arrivalBudget reserve
  rw [pow_succ]
  have hp : (0:ℚ) < 2^k := by positivity
  apply (mul_le_mul_iff_left₀ (by positivity : (0:ℚ) < 2^k*2)).mp
  calc
    _ = 2*(candidates k).card +
        (∑ x ∈ candidates (k+1), reserveWeight (k+1) x) := by field_simp
    _ ≤ _ := hs
    _ = _ := by field_simp

theorem mass_nonnegative (k : ℕ) : 0 ≤ mass k := by
  unfold mass
  exact Finset.sum_nonneg (fun x _ => by positivity)

theorem deaths_nonnegative (k : ℕ) : 0 ≤ deaths k := by
  unfold deaths
  apply Finset.sum_nonneg
  intro x _
  split_ifs <;> positivity

theorem reserve_nonnegative (k : ℕ) : 0 ≤ reserve k := by
  unfold reserve
  apply div_nonneg _ (by positivity)
  apply Finset.sum_nonneg
  intro x hx
  have hg := (candidate_bounds hx).2.2
  have hd := (debt_nonnegative_iff k x).mpr (hg k (by omega))
  unfold reserveWeight
  linarith

/-- Same physical sources, plus only their actual new siblings. -/
theorem envelope_step (k : ℕ) :
    mass (k+1)+reserve (k+1)+deaths k ≤ mass k+reserve k := by
  have hmass := mass_identity k
  have hbirth := births_le_budget k
  have hreserve := reserve_decreases k
  linarith

theorem initial_envelope : mass 0+reserve 0 = 9 := by
  have hc : candidates 0 = {1} := by decide
  simp only [mass, reserve, hc, Finset.sum_singleton]
  norm_num [odds, reserveWeight, debt]

/-- The entire finite loss budget for the native actual-source process. -/
theorem envelope_budget (N : ℕ) :
    mass N+reserve N+(∑ k ∈ Finset.range N, deaths k) ≤ 9 := by
  induction N with
  | zero => simpa using initial_envelope.le
  | succ N ih =>
    rw [Finset.sum_range_succ]
    have h := envelope_step N
    linarith

theorem total_loss_budget (N : ℕ) : (∑ k ∈ Finset.range N, deaths k) ≤ 9 := by
  have h := envelope_budget N
  have hm := mass_nonnegative N
  have hr := reserve_nonnegative N
  linarith

theorem tail_loss_budget (K N : ℕ) :
    (∑ k ∈ Finset.range N, deaths (K+k)) ≤ 9 := by
  have h := total_loss_budget (K+N)
  rw [Finset.sum_range_add] at h
  have hp : 0 ≤ ∑ k ∈ Finset.range K, deaths k :=
    Finset.sum_nonneg (fun k _ => deaths_nonnegative k)
  linarith

theorem native_cutoff (k : ℕ) : k ≤ 2^k := by
  induction k with
  | zero => simp
  | succ k ih =>
    rw [pow_succ]
    have hp : 0 < 2^k := by positivity
    omega

/-- A concrete sufficient analytic target.  Its divergence hypothesis is
OPEN; the finite budget and all references to the map are proved here.
The target is stated for arbitrary nonnegative native-clock hazards so
zero hazards can encode unused clocks. -/
theorem loss_hazard_implies_collatz (hazard : ℕ → ℚ)
    (hnonnegative : ∀ k, 0 ≤ hazard k)
    (hactual : ∀ k, hazard k * mass k ≤ deaths k)
    (hdiverges : ∀ K : ℕ, ∀ B : ℚ, ∃ N : ℕ,
      B < ∑ k ∈ Finset.range N, hazard (K+k)) : Universal := by
  apply extinction_implies_collatz
  intro L hL
  by_contra hnone
  have hmass (n : ℕ) : (L:ℚ)⁻¹ ≤ mass (L+n) := by
    by_contra hsmall
    apply hnone
    refine ⟨L+n, (by have h := native_cutoff (L+n); omega), ?_⟩
    linarith
  exact loss_budget_excludes_atom
    (fun n => mass (L+n)) (fun n => deaths (L+n)) (fun n => hazard (L+n))
    (L:ℚ)⁻¹ 9 (by positivity) hmass
    (fun n => hnonnegative (L+n)) (fun n => hactual (L+n))
    (fun N => tail_loss_budget L N) (hdiverges L)


#print axioms cylinder_lift
#print axioms gate_lift
#print axioms candidate_children
#print axioms mass_identity
#print axioms reserve_decreases
#print axioms envelope_budget
#print axioms total_loss_budget
#print axioms loss_hazard_implies_collatz

end Collatz.NativeGate
