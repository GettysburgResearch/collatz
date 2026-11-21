module
public import Mathlib.Basic.Real.Basic
public import Mathlib.Algebra.BigOperators.Group.Finset.Basic
public import Mathlib.Algebra.BigOperators.Group.Finset.Piecewise
public import Mathlib.Algebra.Order.BigOperators.Group.Finset
public import Mathlib.Data.Finset.Interval
public import Mathlib.Order.Interval.Finset.Nat
public import Mathlib.Tactic.Linarith
public import Mathlib.Tactic.NormNum
public import Mathlib.Tactic.Ring
public import Mathlib.Tactic.Positivity

@[expose] public section

namespace CollatzHitPotentials

variable {α : Type*}

attribute [local instance] Classical.propDecidable

def orbit (f : α → α) : ℕ → α → α
  | 0, x => x
  | k+1, x => orbit f k (f x)

def Hits (f : α → α) (a x : α) : Prop := ∃ k, orbit f k x = a

def Nonperiodic (f : α → α) (a : α) : Prop := ∀ k, 0 < k → orbit f k a ≠ a

noncomputable def hit (f : α → α) (a x : α) : ℝ := by
  classical
  exact if Hits f a x then 1 else 0
noncomputable def anchor (a x : α) : ℝ := by
  classical
  exact if x = a then 1 else 0
noncomputable def killed (f : α → α) (a : α) (g : α → ℝ) (x : α) : ℝ := by
  classical
  exact if x = a then 0 else g (f x)

lemma orbit_succ (f : α → α) (k : ℕ) (x : α) :
    orbit f (k+1) x = f (orbit f k x) := by
  induction k generalizing x with
  | zero => rfl
  | succ k ih => simpa [orbit] using ih (f x)

lemma orbit_add (f : α → α) (k l : ℕ) (x : α) :
    orbit f (k+l) x = orbit f l (orbit f k x) := by
  induction k generalizing x with
  | zero => simp [orbit]
  | succ k ih => simpa [orbit, Nat.succ_add] using ih (f x)

lemma hits_self (f : α → α) (a : α) : Hits f a a := ⟨0, rfl⟩

lemma hits_iff_eq_or_next (f : α → α) (a x : α) :
    Hits f a x ↔ x = a ∨ Hits f a (f x) := by
  constructor
  · rintro ⟨k, hk⟩
    cases k with
    | zero => exact Or.inl hk
    | succ k => exact Or.inr ⟨k, hk⟩
  · rintro (h | ⟨k, hk⟩)
    · exact ⟨0, h⟩
    · exact ⟨k+1, hk⟩

lemma nonperiodic_not_hit_next {f : α → α} {a : α} (h : Nonperiodic f a) :
    ¬ Hits f a (f a) := by
  rintro ⟨k, hk⟩
  exact h (k+1) (by omega) hk

lemma hit_bounds (f : α → α) (a x : α) : 0 ≤ hit f a x ∧ hit f a x ≤ 1 := by
  classical
  by_cases h : Hits f a x <;> simp [hit, h]

lemma hit_anchor_equation {f : α → α} {a : α} (ha : Nonperiodic f a) (x : α) :
    hit f a x - hit f a (f x) = anchor a x := by
  classical
  by_cases hx : x = a
  · subst x
    simp [hit, anchor, hits_self, nonperiodic_not_hit_next ha]
  · have he : Hits f a x ↔ Hits f a (f x) := by
      rw [hits_iff_eq_or_next]
      simp [hx]
    simp [hit, anchor, hx, he]

/-- Exact finite Green identity for a fixed nonperiodic target. -/
theorem finite_anchor_green {f : α → α} {a : α} (ha : Nonperiodic f a)
    (k : ℕ) (x : α) :
    hit f a x = (∑ j ∈ Finset.range k, anchor a (orbit f j x)) + hit f a (orbit f k x) := by
  induction k with
  | zero => simp [orbit]
  | succ k ih =>
    rw [Finset.sum_range_succ]
    have he := hit_anchor_equation ha (orbit f k x)
    rw [← orbit_succ f k x] at he
    linarith

/-- Killing at the target makes the Green equation valid even for cyclic targets. -/
theorem hit_killed_equation (f : α → α) (a x : α) :
    hit f a x = anchor a x + killed f a (hit f a) x := by
  classical
  by_cases hx : x = a
  · subst x
    simp [hit, anchor, killed, hits_self]
  · have he : Hits f a x ↔ Hits f a (f x) := by
      rw [hits_iff_eq_or_next]
      simp [hx]
    simp [hit, anchor, killed, hx, he]

lemma one_killed_equation (f : α → α) (a x : α) :
    (1:ℝ) = anchor a x + killed f a (fun _ => 1) x := by
  classical
  by_cases hx : x = a <;> simp [anchor, killed, hx]

lemma solution_on_hits {f : α → α} {a : α} {g : α → ℝ}
    (hg : ∀ x, g x = anchor a x + killed f a g x)
    {x : α} (hx : Hits f a x) : g x = 1 := by
  classical
  obtain ⟨k, hk⟩ := hx
  induction k generalizing x with
  | zero =>
    change x = a at hk
    subst x
    simpa [anchor, killed] using hg a
  | succ k ih =>
    by_cases ha : x = a
    · subst x
      simpa [anchor, killed] using hg a
    · have hn := ih hk
      have he := hg x
      simpa [anchor, killed, ha, hn] using he

/-- The actual fixed-source hitting function is the least nonnegative solution. -/
theorem hit_minimal_solution {f : α → α} {a : α} {g : α → ℝ}
    (hg0 : ∀ x, 0 ≤ g x)
    (hg : ∀ x, g x = anchor a x + killed f a g x) :
    ∀ x, hit f a x ≤ g x := by
  classical
  intro x
  by_cases hx : Hits f a x
  · simp [hit, hx, solution_on_hits hg hx]
  · simpa [hit, hx] using hg0 x

noncomputable def defect (f : α → α) (a x : α) : ℝ := 1 - hit f a x

lemma defect_bounds (f : α → α) (a x : α) :
    0 ≤ defect f a x ∧ defect f a x ≤ 1 := by
  have h := hit_bounds f a x
  dsimp [defect]
  constructor <;> linarith [h.1, h.2]

lemma defect_killed_fixed (f : α → α) (a x : α) :
    defect f a x = killed f a (defect f a) x := by
  classical
  by_cases hx : x = a
  · subst x
    simp [defect, killed, hit, hits_self]
  · have he := hit_killed_equation f a x
    simp [anchor, killed, hx] at he ⊢
    simp [defect, he]

lemma hits_next_iff_of_return {f : α → α} {a : α}
    (ha : Hits f a (f a)) (x : α) : Hits f a x ↔ Hits f a (f x) := by
  rw [hits_iff_eq_or_next]
  constructor
  · rintro (rfl | h)
    · exact ha
    · exact h
  · exact Or.inr

/-- At a cyclic target the defect is exactly invariant at every ordinary point,
including the target itself. -/
lemma defect_invariant_of_return {f : α → α} {a : α}
    (ha : Hits f a (f a)) (x : α) : defect f a (f x) = defect f a x := by
  have he := hits_next_iff_of_return ha x
  simp only [defect, hit, he]

/-- Bounded nonnegative uniqueness includes cycles and escaping trajectories:
its exact missing obstruction is the killed fixed function `1-hit`. -/
theorem all_hit_iff_unique_bounded_solution (f : α → α) (a : α) :
    (∀ x, Hits f a x) ↔
    (∀ g : α → ℝ, (∀ x, 0 ≤ g x ∧ g x ≤ 1) →
      (∀ x, g x = anchor a x + killed f a g x) → g = hit f a) := by
  classical
  constructor
  · intro hall g _hg hgfix
    funext x
    have hv := solution_on_hits hgfix (hall x)
    simpa [hit, hall x] using hv
  · intro hu x
    have he := hu (fun _ => 1) (by intro y; norm_num) (one_killed_equation f a)
    have hv : hit f a x = 1 := by rw [← he]
    by_contra hn
    simp [hit, hn] at hv

/-- Pure finite-density arithmetic for two disjoint predecessor populations. -/
theorem variance_lower {c p q : ℝ} (hc : 0 < c)
    (hp : c/5 ≤ p) (hq : c/16 ≤ q) (hpq : p+q ≤ 1) :
    c^2/80 ≤ p*(1-p) := by
  have hp0 : 0 ≤ p := by linarith
  have hq0 : 0 ≤ c/16 := by positivity
  have hh : c/16 ≤ 1-p := by linarith
  have hm := mul_le_mul hp hh hq0 hp0
  nlinarith

/-- If the coboundary energy is `1/X`, no uniform Poincare constant survives. -/
theorem finite_scale_poincare_obstruction {c p q X K : ℝ}
    (hc : 0 < c) (hX : 0 < X)
    (hp : c/5 ≤ p) (hq : c/16 ≤ q) (hpq : p+q ≤ 1)
    (hscale : 80*K < c^2*X) :
    K/X < p*(1-p) := by
  have hv := variance_lower hc hp hq hpq
  have hk : K/X < c^2/80 := by
    apply (div_lt_iff₀ hX).2
    nlinarith
  exact lt_of_lt_of_le hk hv

lemma hits_comparable {f : α → α} {a b x : α}
    (ha : Hits f a x) (hb : Hits f b x) : Hits f b a ∨ Hits f a b := by
  obtain ⟨k, hk⟩ := ha
  obtain ⟨l, hl⟩ := hb
  by_cases hkl : k ≤ l
  · obtain ⟨r, hr⟩ := Nat.exists_eq_add_of_le hkl
    rw [hr, orbit_add, hk] at hl
    exact Or.inl ⟨r, hl⟩
  · obtain ⟨r, hr⟩ := Nat.exists_eq_add_of_le (by omega : l ≤ k)
    rw [hr, orbit_add, hl] at hk
    exact Or.inr ⟨r, hk⟩

lemma invariant_on_hits {f : α → α} {a x : α} {g : α → ℝ}
    (hg : ∀ y, g (f y) = g y) (hx : Hits f a x) : g x = g a := by
  obtain ⟨k, hk⟩ := hx
  induction k generalizing x with
  | zero => simpa [orbit] using congrArg g hk
  | succ k ih =>
    have he := ih hk
    rw [hg x] at he
    exact he

/-- This ordinary trace estimate needs constancy only on the actual predecessor
chains in the finite sample, rather than invariance on a completion. -/
theorem predecessor_trace (f : α → α) (a : α) (g : α → ℝ) (S : Finset α)
    (hg : ∀ x ∈ S, Hits f a x → g x = g a) :
    ((S.filter (fun x => Hits f a x)).card : ℝ) * g a ^ 2 ≤ ∑ x ∈ S, g x ^ 2 := by
  classical
  have hs : (∑ x ∈ S.filter (fun x => Hits f a x), g x ^ 2) =
      ((S.filter (fun x => Hits f a x)).card : ℝ) * g a ^ 2 := by
    calc
      _ = ∑ x ∈ S.filter (fun x => Hits f a x), g a ^ 2 := by
        apply Finset.sum_congr rfl
        intro x hx
        rw [hg x (Finset.mem_filter.mp hx).1 (Finset.mem_filter.mp hx).2]
      _ = _ := by simp
  rw [← hs]
  apply Finset.sum_le_sum_of_subset_of_nonneg (Finset.filter_subset _ _)
  intro x _ _
  exact sq_nonneg (g x)

/-- A density theorem is an explicit hypothesis here: this file does not assume
or silently formalize the analytic PD input. -/
theorem conditional_density_trace (f : α → α) (a : α) (g : α → ℝ)
    (S : Finset α) {c X : ℝ} (hX : 0 < X)
    (hg : ∀ x ∈ S, Hits f a x → g x = g a)
    (hcount : c * X ≤ ((S.filter (fun x => Hits f a x)).card : ℝ)) :
    c * g a ^ 2 ≤ (∑ x ∈ S, g x ^ 2) / X := by
  classical
  apply (le_div_iff₀ hX).2
  calc
    c * g a ^ 2 * X = (c*X) * g a ^ 2 := by ring
    _ ≤ ((S.filter (fun x => Hits f a x)).card : ℝ) * g a ^ 2 :=
      mul_le_mul_of_nonneg_right hcount (sq_nonneg (g a))
    _ ≤ _ := predecessor_trace f a g S hg

/- A finite domain keeps both the outer boundary and the ordinary anchor. -/
noncomputable def stopped (f : α → α) (D : α → Prop) (g : α → ℝ) : ℕ → α → ℝ
  | 0, x => g x
  | k+1, x => if D x then stopped f D g k (f x) else 0

noncomputable def exitDatum (D : α → Prop) (g : α → ℝ) (x : α) : ℝ :=
  if D x then 0 else g x

lemma stopped_add (f : α → α) (D : α → Prop) (g h : α → ℝ) (k : ℕ) (x : α) :
    stopped f D (fun y => g y + h y) k x = stopped f D g k x + stopped f D h k x := by
  induction k generalizing x with
  | zero => rfl
  | succ k ih =>
    by_cases hx : D x <;> simp [stopped, hx, ih]

lemma stopped_succ_right (f : α → α) (D : α → Prop) (g : α → ℝ) (k : ℕ) (x : α) :
    stopped f D g (k+1) x = stopped f D (stopped f D g 1) k x := by
  induction k generalizing x with
  | zero => rfl
  | succ k ih =>
    by_cases hx : D x <;> simp only [stopped, hx, ite_true, ite_false]
    · exact ih (f x)

lemma stopped_balance {f : α → α} {D : α → Prop} {g : α → ℝ}
    (hg : ∀ x, D x → g x = g (f x)) (k : ℕ) (x : α) :
    stopped f D g k x = stopped f D (exitDatum D g) k x + stopped f D g (k+1) x := by
  have he : g = fun y => exitDatum D g y + stopped f D g 1 y := by
    funext y
    by_cases hy : D y
    · simp [exitDatum, stopped, hy, hg y hy]
    · simp [exitDatum, stopped, hy]
  calc
    stopped f D g k x = stopped f D (fun y => exitDatum D g y + stopped f D g 1 y) k x := by
      exact congrArg (fun h => stopped f D h k x) he
    _ = stopped f D (exitDatum D g) k x + stopped f D (stopped f D g 1) k x :=
      stopped_add f D (exitDatum D g) (stopped f D g 1) k x
    _ = _ := by rw [← stopped_succ_right]

/-- The finite boundary-flux identity retains a terminal interior term. In a
finite Collatz box that term contains every internal nontrivial cycle. -/
theorem finite_exit_green {f : α → α} {D : α → Prop} {g : α → ℝ}
    (hg : ∀ x, D x → g x = g (f x)) (k : ℕ) (x : α) :
    g x = (∑ j ∈ Finset.range k, stopped f D (exitDatum D g) j x) + stopped f D g k x := by
  induction k with
  | zero => simp [stopped]
  | succ k ih =>
    rw [Finset.sum_range_succ]
    have he := stopped_balance hg k x
    linarith

/-- Summing the pathwise identity requires no limiting measure and no mixing
assumption about the fixed ordinary source. -/
theorem finite_exit_green_sum {f : α → α} {D : α → Prop} {g : α → ℝ}
    (hg : ∀ x, D x → g x = g (f x)) (k : ℕ) (S : Finset α) :
    (∑ x ∈ S, g x) =
      (∑ x ∈ S, ∑ j ∈ Finset.range k, stopped f D (exitDatum D g) j x) +
      ∑ x ∈ S, stopped f D g k x := by
  rw [← Finset.sum_add_distrib]
  apply Finset.sum_congr rfl
  intro x _
  exact finite_exit_green hg k x

def T (n : ℕ) : ℕ := if n % 2 = 0 then n/2 else (3*n+1)/2

lemma one_returns : Hits T 1 (T 1) := by
  refine ⟨1, ?_⟩
  norm_num [orbit, T]

lemma collatz_defect_invariant (n : ℕ) : defect T 1 (T n) = defect T 1 n :=
  defect_invariant_of_return one_returns n

/-- Conditional finite-scale closure estimate: a single surviving source
forces a definite mean square energy whenever its predecessor population has
the supplied lower density. The population bound is an explicit hypothesis. -/
theorem surviving_source_energy {a : ℕ} (ha : ¬ Hits T 1 a) (S : Finset ℕ)
    {c X : ℝ} (hX : 0 < X)
    (hcount : c*X ≤ ((S.filter (fun n => Hits T a n)).card : ℝ)) :
    c ≤ (∑ n ∈ S, defect T 1 n ^ 2) / X := by
  have ht := conditional_density_trace T a (defect T 1) S hX
    (by
      intro n _ hn
      exact invariant_on_hits collatz_defect_invariant hn) hcount
  simpa [defect, hit, ha] using ht

def Small (n : ℕ) : Prop := n=1 ∨ n=2 ∨ n=4 ∨ n=8

lemma small_step {n : ℕ} (hn : Small n) : Small (T n) := by
  rcases hn with rfl | rfl | rfl | rfl <;> norm_num [T, Small]

lemma small_orbit (k : ℕ) {n : ℕ} (hn : Small n) : Small (orbit T k n) := by
  induction k generalizing n with
  | zero => exact hn
  | succ k ih => exact ih (small_step hn)

lemma after_small {n k : ℕ} (hn : Small (T n)) (hk : 0 < k) :
    Small (orbit T k n) := by
  cases k with
  | zero => omega
  | succ k => exact small_orbit k hn

lemma nonperiodic_five : Nonperiodic T 5 := by
  intro k hk he
  have hs := after_small (n := 5) (by norm_num [T, Small]) hk
  rw [he] at hs
  norm_num [Small] at hs

lemma nonperiodic_sixteen : Nonperiodic T 16 := by
  intro k hk he
  have hs := after_small (n := 16) (by norm_num [T, Small]) hk
  rw [he] at hs
  norm_num [Small] at hs

lemma five_not_sixteen : ¬ Hits T 16 5 := by
  rintro ⟨k, hk⟩
  cases k with
  | zero => norm_num [orbit] at hk
  | succ k =>
    have hs := after_small (n := 5) (by norm_num [T, Small]) (by omega : 0 < k+1)
    rw [hk] at hs
    norm_num [Small] at hs

lemma sixteen_not_five : ¬ Hits T 5 16 := by
  rintro ⟨k, hk⟩
  cases k with
  | zero => norm_num [orbit] at hk
  | succ k =>
    have hs := after_small (n := 16) (by norm_num [T, Small]) (by omega : 0 < k+1)
    rw [hk] at hs
    norm_num [Small] at hs

lemma five_sixteen_disjoint (n : ℕ) : ¬ (Hits T 5 n ∧ Hits T 16 n) := by
  rintro ⟨h5, h16⟩
  rcases hits_comparable h5 h16 with h | h
  · exact five_not_sixteen h
  · exact sixteen_not_five h

/-- This Collatz observable has exactly one ordinary defect. -/
theorem five_exact_anchor (n : ℕ) :
    hit T 5 n - hit T 5 (T n) = if n=5 then 1 else 0 := by
  have he := hit_anchor_equation nonperiodic_five n
  by_cases hn : n=5 <;> simpa [anchor, hn] using he

/-- Its unnormalised squared coboundary energy is exactly one on every
initial interval containing the anchor. -/
theorem five_finite_energy {X : ℕ} (hX : 5 ≤ X) :
    (∑ n ∈ Finset.Icc 1 X, (hit T 5 n - hit T 5 (T n))^2) = 1 := by
  simp_rw [five_exact_anchor]
  have he : ∀ n : ℕ, ((if n=5 then 1 else 0 : ℝ)^2) = if n=5 then 1 else 0 := by
    intro n
    split_ifs <;> norm_num
  simp_rw [he]
  simp [Finset.sum_ite_eq', hX]

#print axioms finite_anchor_green
#print axioms hit_killed_equation
#print axioms hit_minimal_solution
#print axioms all_hit_iff_unique_bounded_solution
#print axioms five_sixteen_disjoint
#print axioms five_exact_anchor
#print axioms five_finite_energy
#print axioms finite_scale_poincare_obstruction
#print axioms predecessor_trace
#print axioms conditional_density_trace
#print axioms collatz_defect_invariant
#print axioms surviving_source_energy
#print axioms finite_exit_green
#print axioms finite_exit_green_sum

end CollatzHitPotentials
