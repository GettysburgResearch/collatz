import EarlierOffsets

/-! Fixed gate lists after genuine same-clock physical coalescence, together
with a positive canonical control for two incomparable prescribed targets. -/
set_option autoImplicit false
set_option warningAsError true
namespace JointVisits
open CoreBranching

def Visits (x a : ℕ) : Prop := ∃ i, run i x=a

theorem visits_trans {x a b : ℕ} (ha : Visits x a) (hb : Visits a b) : Visits x b := by
  obtain ⟨i,hi⟩ := ha
  obtain ⟨j,hj⟩ := hb
  exact ⟨i+j,by rw [run_add,hi,hj]⟩

/-- Two gates visited by the same ordinary input are comparable in forward time. -/
theorem visits_comparable {x a b : ℕ} (ha : Visits x a) (hb : Visits x b) :
    Visits a b ∨ Visits b a := by
  obtain ⟨i,hi⟩ := ha
  obtain ⟨j,hj⟩ := hb
  by_cases h : i≤j
  · exact Or.inl ⟨j-i,by rw [←hi,←run_add,Nat.add_sub_of_le h,hj]⟩
  · have h' : j≤i := by omega
    exact Or.inr ⟨i-j,by rw [←hj,←run_add,Nat.add_sub_of_le h',hi]⟩

private theorem lower_one (x : ℕ) : x≤2*step x := by
  unfold step
  split <;> omega

/-- No ordinary shortcut reduces its source by more than a factor two. -/
theorem lower_run (h x : ℕ) : x≤2^h*run h x := by
  induction h generalizing x with
  | zero => simp [run]
  | succ h ih =>
    rw [pow_succ,run,show 2^h*2*run h (step x)=2*(2^h*run h (step x)) by ring]
    exact (lower_one x).trans (Nat.mul_le_mul_left 2 (ih _))

private theorem no_low_prefix {i h x a : ℕ} (ih : i<h) (high : 2^h*a<x) :
    run i x≠a := by
  intro eq
  have lo := lower_run i x
  rw [eq] at lo
  have pp : 2^i≤(2:ℕ)^h := Nat.pow_le_pow_right (by decide) (by omega)
  have ss := Nat.mul_le_mul_right a pp
  omega

/-- At every absolute clock, the two arms agree on whether they visit any
specified gate below the premerger floor. The horizon after merging is unlimited. -/
theorem simultaneous_gate_clock {x y h a : ℕ} (hit : run h x=run h y)
    (hx : 2^h*a<x) (hy : 2^h*a<y) (j : ℕ) : run j x=a ↔ run j y=a := by
  by_cases short : j<h
  · exact iff_of_false (no_low_prefix short hx) (no_low_prefix short hy)
  · have le : h≤j := by omega
    rw [show j=h+(j-h) from (Nat.add_sub_of_le le).symm,run_add,run_add,hit]

/-- Replacing the tripled source by the ordinary source preserves the entire
joint visit event on every successful finite prefix. -/
theorem joint_same_source {x h a b : ℕ} (hit : run h x=run h (3*x)) (high : 2^h*b<x) :
    (Visits x a ∧ Visits (3*x) b) ↔ (Visits x a ∧ Visits x b) := by
  have one (j : ℕ) := simultaneous_gate_clock hit high (by omega : 2^h*b<3*x) j
  exact and_congr_right' (exists_congr fun j => (one j).symm)

/-- Every tripling pair visiting two incomparable gates misses the specified
same-clock test. The finite inequality below can be summed over any source set. -/
theorem incomparable_miss {x h a b : ℕ} (high : 2^h*b<x)
    (incomp : ¬ (Visits a b ∨ Visits b a)) (lo : Visits x a) (hi : Visits (3*x) b) :
    run h x≠run h (3*x) := by
  intro hit
  have both := (joint_same_source hit high).mp ⟨lo,hi⟩
  exact incomp (visits_comparable both.1 both.2)

noncomputable local instance (x a : ℕ) : Decidable (Visits x a) := Classical.propDecidable _

/-- Finite deterministic version, simultaneous for arbitrary prescribed gates. -/
theorem incomparable_count (S : Finset ℕ) (a b h : ℕ) (high : ∀ x ∈ S, 2^h*b<x)
    (incomp : ¬ (Visits a b ∨ Visits b a)) :
    (S.filter (fun x => Visits x a ∧ Visits (3*x) b)).card ≤
      (S.filter (fun x => run h x≠run h (3*x))).card := by
  apply Finset.card_le_card
  intro x hx
  obtain ⟨mem,lo,hi⟩ := Finset.mem_filter.mp hx
  exact Finset.mem_filter.mpr ⟨mem,incomparable_miss (high x mem) incomp lo hi⟩

private theorem one_cycle (j : ℕ) : ∀ y : ℕ, y=1 ∨ y=2 → run j y=1 ∨ run j y=2 := by
  induction j with
  | zero => intro y h; exact h
  | succ j ih =>
    intro y cases
    rcases cases with rfl|rfl
    · exact ih 2 (Or.inr rfl)
    · exact ih 1 (Or.inl rfl)

private theorem no_gate_after_one (x h a : ℕ) (endpt : run h x=1) (large : 2<a)
    (pref : ∀ i : Fin h, run i.val x≠a) : ¬ Visits x a := by
  rintro ⟨i,eq⟩
  by_cases short : i<h
  · exact pref ⟨i,short⟩ eq
  · have le : h≤i := by omega
    rw [show i=h+(i-h) from (Nat.add_sub_of_le le).symm,run_add,endpt] at eq
    have cyc := one_cycle (i-h) 1 (Or.inl rfl)
    omega

/-- Both corrected targets are genuine ternary units in the convergent
component. Their respective forward trajectories never visit each other. -/
theorem canonical_113_control :
    113%48=17 ∧ step (3*113)=509 ∧ 113%3≠0 ∧ 509%3≠0 ∧
    run 10 113=1 ∧ run 33 509=1 ∧ ¬ (Visits 113 509 ∨ Visits 509 113) := by
  refine ⟨by decide,by decide,by decide,by decide,by decide +kernel,by decide +kernel,?_⟩
  exact not_or_intro (no_gate_after_one 113 10 509 (by decide +kernel) (by decide) (by decide +kernel))
    (no_gate_after_one 509 33 113 (by decide +kernel) (by decide) (by decide +kernel))

#print axioms visits_comparable
#print axioms lower_run
#print axioms simultaneous_gate_clock
#print axioms joint_same_source
#print axioms incomparable_miss
#print axioms incomparable_count
#print axioms canonical_113_control
end JointVisits
