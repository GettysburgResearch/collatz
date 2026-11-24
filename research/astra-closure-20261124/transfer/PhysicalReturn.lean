import Std

namespace Collatz.PhysicalReturn

def step (n : Nat) : Nat := if n % 2 = 0 then n / 2 else (3*n+1)/2
def run : Nat → Nat → Nat
  | 0, n => n
  | k+1, n => run k (step n)
def oddCount : Nat → Nat → Nat
  | 0, _ => 0
  | k+1, n => oddCount k (step n) + (n % 2)

private theorem run_add (a b n : Nat) : run (a+b) n = run b (run a n) := by
  induction a generalizing n with
  | zero => simp [run]
  | succ a ih => rw [Nat.succ_add]; exact ih (step n)

private theorem one_lift (x n : Nat) :
    step (2*x+n) = 3^(n%2)*x+step n := by
  have hi : n%2=0 ∨ n%2=1 := by omega
  rcases hi with h|h <;> simp [step, h, Nat.add_mod] <;> omega

/-- Arbitrary high lifts have the exact same low-word affine law. The base n
may exceed 2^k, as it does on the actual child arm 81m+r. -/
theorem affine_lift (k n q : Nat) :
    run k (2^k*q+n) = 3^(oddCount k n)*q+run k n := by
  induction k generalizing n q with
  | zero => simp [run, oddCount]
  | succ k ih =>
    have eq : 2^(k+1)*q = 2*(2^k*q) := by rw [Nat.pow_succ]; ac_rfl
    have coeff : 3^(n%2)*(2^k*q) = 2^k*(3^(n%2)*q) := by ac_rfl
    rw [run, eq, one_lift, coeff, ih, oddCount, Nat.pow_add, run, Nat.mul_assoc]

/-- Two different affine slopes can collide on at most one ordinary lift.
This includes time pairs whose two source clocks differ. -/
theorem unique_affine_collision (a b c d q v : Nat) (h : a ≠ b)
    (hq : a*q+c = b*q+d) (hv : a*v+c = b*v+d) : q=v := by
  apply Classical.byContradiction
  intro hne
  rcases Nat.lt_or_gt_of_ne hne with hlt|hgt
  · obtain ⟨t, ht⟩ := Nat.exists_eq_add_of_lt hlt
    rw [ht, Nat.add_assoc] at hv
    simp only [Nat.mul_add] at hv ⊢
    have eq : a*(t+1)=b*(t+1) := by simp only [Nat.mul_add, Nat.mul_one] at *; omega
    exact h (Nat.eq_of_mul_eq_mul_right (by omega) eq)
  · obtain ⟨t, ht⟩ := Nat.exists_eq_add_of_lt hgt
    rw [ht, Nat.add_assoc] at hq
    simp only [Nat.mul_add] at hq ⊢
    have eq : a*(t+1)=b*(t+1) := by simp only [Nat.mul_add, Nat.mul_one] at *; omega
    exact h (Nat.eq_of_mul_eq_mul_right (by omega) eq)

def Escapes (n : Nat) : Prop := ∀ B : Nat, ∃ t, B < run t n

/-- A bounded suffix makes the entire physical orbit bounded, including the
finite prefix before that suffix. -/
theorem escaping_suffix (n k : Nat) (h : Escapes n) : Escapes (run k n) := by
  induction k with
  | zero => exact h
  | succ k ih =>
    rw [run_add]
    change Escapes (step (run k n))
    intro B
    obtain ⟨j, hj⟩ := ih (max B (run k n))
    cases j with
    | zero =>
      change max B (run k n) < run k n at hj
      omega
    | succ j => exact ⟨j, Nat.lt_of_le_of_lt (Nat.le_max_left ..) hj⟩

/-- Every bounded positive root at most K has an all-future bound in a
common finite cap. This gives existence, with no rate for that cap. -/
theorem finite_bounded_root_cap (K : Nat) :
    ∃ C : Nat, ∀ v ≤ K, ¬Escapes v → ∀ t, run t v ≤ C := by
  classical
  induction K with
  | zero =>
    exact ⟨0, by
      intro v hv _ t
      have : v=0 := by omega
      subst v
      induction t with
      | zero => exact Nat.le_refl 0
      | succ t ih => simpa [run, step] using ih⟩
  | succ K ih =>
    obtain ⟨C, hC⟩ := ih
    by_cases hs : Escapes (K+1)
    · refine ⟨C, ?_⟩
      intro v hv hb t
      have he : v ≠ K+1 := fun e => hb (e ▸ hs)
      have : v≤K := by omega
      exact hC v this hb t
    · simp only [Escapes, Classical.not_forall, not_exists, Nat.not_lt] at hs
      obtain ⟨B, hB⟩ := hs
      refine ⟨max B C, ?_⟩
      intro v hv hb t
      by_cases he : v=K+1
      · subst v; exact Nat.le_trans (hB t) (Nat.le_max_left ..)
      · exact Nat.le_trans (hC v (by omega) hb t) (Nat.le_max_right ..)

private theorem column_union (roots : List Nat) (a : Nat) (choices : List Nat) :
    roots.countP (fun w => decide (w ∈ a::choices)) ≤
      roots.count a + roots.countP (fun w => decide (w ∈ choices)) := by
  induction roots with
  | nil => simp
  | cons z zs ih =>
    by_cases ha : z=a <;> by_cases hb : z ∈ choices <;>
      simp [List.countP_cons, List.mem_cons, ha, hb] at * <;> omega

private theorem row_pairs (roots choices : List Nat) (B : Nat)
    (atoms : ∀ w, roots.count w ≤ B) :
    roots.countP (fun w => decide (w ∈ choices)) ≤ choices.length*B := by
  induction choices with
  | nil => simp
  | cons a cs ih =>
    have hu := column_union roots a cs
    have ha := atoms a
    rw [List.length_cons, Nat.succ_mul]
    omega

/-- Product sampling with replacement, retaining the two actual marginal
multisets. A degree bound and a marginal multiplicity bound hold after any
source selection for which their hypotheses have been proved. -/
theorem product_relation_count (left right : List Nat) (choices : Nat → List Nat)
    (D B : Nat) (degree : ∀ v, (choices v).length ≤ D)
    (atoms : ∀ w, right.count w ≤ B) :
    (left.map (fun v => right.countP (fun w => decide (w ∈ choices v)))).sum ≤
      left.length*(D*B) := by
  induction left with
  | nil => simp
  | cons v vs ih =>
    have hr := Nat.le_trans (row_pairs right (choices v) B atoms)
      (Nat.mul_le_mul_right B (degree v))
    rw [List.map_cons, List.sum_cons, List.length_cons, Nat.succ_mul]
    omega

#print axioms product_relation_count
#print axioms affine_lift
#print axioms unique_affine_collision
#print axioms escaping_suffix
#print axioms finite_bounded_root_cap
end Collatz.PhysicalReturn
