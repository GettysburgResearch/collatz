import Std

/-!
Finite arithmetic used in the head sampling argument. The interval discrepancy,
predecessor-density theorem, and probabilistic limits are written inputs.
-/
namespace HeadSampling

def step (n : Nat) : Nat :=
  if n % 2 = 0 then n / 2 else (3 * n + 1) / 2

def orbit (n : Nat) : Nat → Nat
  | 0 => n
  | j + 1 => orbit (step n) j

def hits (a n : Nat) : Prop := ∃ j, orbit n j = a

theorem hits_step_away {a n : Nat} (h : n ≠ a) :
    hits a n ↔ hits a (step n) := by
  constructor
  · rintro ⟨j, hj⟩
    cases j with
    | zero => exact False.elim (h hj)
    | succ j => exact ⟨j, hj⟩
  · rintro ⟨j, hj⟩
    exact ⟨j+1, hj⟩

theorem source_le_twice_step (n : Nat) : n ≤ 2 * step n := by
  unfold step
  split <;> omega

/-- A hit strictly below the whole comparing prefix can be transported past
    the prefix, even for a nonperiodic specified target. -/
theorem hits_after_above_floor (a n j : Nat) (h : 2^j * a < n) :
    hits a n ↔ hits a (orbit n j) := by
  induction j generalizing n with
  | zero => rfl
  | succ j ih =>
    rw [Nat.pow_succ] at h
    have hx := source_le_twice_step n
    have gain : 0 < 2^j := Nat.two_pow_pos j
    have base : a ≤ 2^j * a := by
      simpa using Nat.mul_le_mul_right a (show 1 ≤ 2^j by omega)
    rw [Nat.mul_right_comm] at h
    have h' : 2^j * a < step n := by omega
    exact (hits_step_away (by omega)).trans (ih (step n) h')

theorem hits_at_common_future {a m n h k : Nat}
    (hm : 2^h * a < m) (hn : 2^k * a < n)
    (eqn : orbit m h = orbit n k) : hits a m ↔ hits a n := by
  rw [hits_after_above_floor a m h hm, hits_after_above_floor a n k hn, eqn]

/-- Earlier prefixes of a finer ordinary head are determined by integer division. -/
theorem coarsen_head (base x r s h : Nat) (hr : r < base^s) (hs : s ≤ h) :
    (base^s * x + r) / base^h = x / base^(h-s) := by
  have hp : 0 < base^s := by omega
  have hx : (base^s * x + r) / base^s = x := by
    rw [Nat.add_comm, Nat.add_mul_div_left _ _ hp, Nat.div_eq_of_lt hr, Nat.zero_add]
  calc
    _ = ((base^s*x+r)/base^s)/base^(h-s) := by rw [Nat.div_div_eq_div_mul, ← Nat.pow_add, Nat.add_sub_of_le hs]
    _ = _ := by rw [hx]

/-- If the colors of the two endpoints differ, at least one genuinely adjacent
    row edge on that very ray differs. -/
theorem change_on_block {β : Type} (f : Nat → β) (s n : Nat)
    (h : f s ≠ f (s+n)) :
    ∃ j, s ≤ j ∧ j < s+n ∧ f j ≠ f (j+1) := by
  induction n with
  | zero => simp at h
  | succ n ih =>
    by_cases e : f s = f (s+n)
    · refine ⟨s+n, by omega, by omega, ?_⟩
      intro e'
      exact h (e.trans e')
    · obtain ⟨j, lo, hi, ne⟩ := ih e
      exact ⟨j, lo, by omega, ne⟩

/-- A probability minorization on each ordinary cell transfers to every
    union of prior cells, including those selected by the past colors. We use
    integer counts and clear a common denominator. -/
theorem mix_cells {α : Type} (cells : List α)
    (hitsIn total : α → Nat) (num den : Nat)
    (h : ∀ x ∈ cells, num * total x ≤ den * hitsIn x) :
    num * (cells.map total).sum ≤ den * (cells.map hitsIn).sum := by
  induction cells with
  | nil => simp
  | cons x xs ih =>
    have hx := h x (by simp)
    have hxs := ih (fun y hy => h y (by simp [hy]))
    simp only [List.map_cons, List.sum_cons, Nat.mul_add]
    omega

/-- Iterating the cleared-denominator conditional minorization gives a count
    for a prescribed target at each of a finite sequence of selected levels. -/
theorem word_mass (good size : Nat → Nat) (num den : Nat)
    (h : ∀ j, num * good j * size (j+1) ≤ den * good (j+1) * size j)
    (pos : ∀ j, 0 < size j) (n : Nat) :
    num^n * good 0 * size n ≤ den^n * good n * size 0 := by
  induction n with
  | zero => simp
  | succ n ih =>
    have L := Nat.mul_le_mul_right (num * size (n+1)) ih
    have R := Nat.mul_le_mul_right (den^n * size 0) (h n)
    have bridge : den^n * good n * size 0 * (num * size (n+1))
        = num * good n * size (n+1) * (den^n * size 0) := by ac_rfl
    rw [bridge] at L
    have H := Nat.le_trans L R
    have z1 : num^n * good 0 * size n * (num * size (n+1))
        = (num^(n+1) * good 0 * size (n+1)) * size n := by rw [Nat.pow_succ]; ac_rfl
    have z2 : den * good (n+1) * size n * (den^n * size 0)
        = (den^(n+1) * good (n+1) * size 0) * size n := by rw [Nat.pow_succ]; ac_rfl
    rw [z1,z2] at H
    exact Nat.le_of_mul_le_mul_right H (pos n)

theorem orbit_add (x i j : Nat) : orbit x (i+j) = orbit (orbit x i) j := by
  induction i generalizing x with
  | zero => simp [orbit]
  | succ i ih => simpa [Nat.succ_add, orbit] using ih (step x)

/-- Two targets visited by a single ordinary start must be in temporal order. -/
theorem visits_comparable {x a b : Nat} (ha : hits a x) (hb : hits b x) :
    hits a b ∨ hits b a := by
  obtain ⟨i, hi⟩ := ha
  obtain ⟨j, hj⟩ := hb
  by_cases h : i ≤ j
  · right
    refine ⟨j-i, ?_⟩
    rw [← hi, ← orbit_add, Nat.add_sub_of_le h, hj]
  · left
    refine ⟨i-j, ?_⟩
    rw [← hj, ← orbit_add, Nat.add_sub_of_le (by omega : j ≤ i), hi]

private def commonTail : List Nat := [11,17,26,13,20,10,5,8,4,2,1]
private def trace7 : List Nat := 7 :: commonTail
private def trace19 : List Nat := [19,29,44,22] ++ commonTail

private theorem confined (S : List Nat) (h : S.all (fun x => S.contains (step x)) = true)
    {x : Nat} (hx : x ∈ S) (j : Nat) : orbit x j ∈ S := by
  induction j generalizing x with
  | zero => exact hx
  | succ j ih => apply ih; simpa using (List.all_eq_true.mp h x hx)

/-- An unconditional, same-component pair of incompatible positive-density
    targets for the written sampling theorem. -/
theorem incompatible_seven_nineteen {x : Nat} (hs : hits 7 x) : ¬ hits 19 x := by
  intro ht
  rcases visits_comparable hs ht with ⟨j, e⟩ | ⟨j, e⟩
  · have hm := confined trace19 (by decide) (x := 19) (by decide) j
    rw [e] at hm
    exact (by decide : 7 ∉ trace19) hm
  · have hm := confined trace7 (by decide) (x := 7) (by decide) j
    rw [e] at hm
    exact (by decide : 19 ∉ trace7) hm

theorem seven_nineteen_merge : orbit 7 1 = 11 ∧ orbit 19 4 = 11 := by decide

private theorem trit_zero_preimage {n : Nat} (h : step n % 3 = 0) :
    n = 2 * step n := by
  unfold step at *
  split <;> split at h <;> omega

theorem ternary_zero_trace {a n : Nat} (ha : a % 3 = 0) (j : Nat)
    (h : orbit n j = a) : n = 2^j * a := by
  induction j generalizing n with
  | zero => simpa [orbit] using h
  | succ j ih =>
    have hs := ih (n := step n) h
    have hz : step n % 3 = 0 := by rw [hs, Nat.mul_mod, ha]; simp
    calc
      n = 2 * step n := trit_zero_preimage hz
      _ = 2^(j+1) * a := by rw [hs, Nat.pow_succ]; ac_rfl

private theorem sum_cap {α : Type} (items : List α) (w : α → Nat) (cap : Nat)
    (hw : ∀ x ∈ items, w x ≤ cap) :
    (items.map w).sum ≤ items.length * cap := by
  induction items with
  | nil => simp
  | cons x xs ih =>
    have a := hw x (by simp)
    have b := ih (fun y hy => hw y (by simp [hy]))
    simp only [List.map_cons, List.sum_cons, List.length_cons, Nat.succ_mul]
    omega

private theorem retained_mass {α : Type} (items : List α) (mass : α → Nat) (cut : Nat) :
    (items.map mass).sum ≤
      (items.map (fun x => if cut ≤ mass x then mass x else 0)).sum + items.length*cut := by
  induction items with
  | nil => simp
  | cons x xs ih =>
    simp only [List.map_cons, List.sum_cons, List.length_cons, Nat.succ_mul]
    split <;> omega

/-- If the large-mass fibers together force dimension above the sum of the
    per-fiber caps including one representative per fiber, a single frozen
    record meets both the cardinality threshold and the dimension threshold. -/
theorem thick_fiber_rank {α : Type} (items : List α) (mass rank : α → Nat)
    (cut target minMass : Nat)
    (total : minMass + items.length*cut ≤ (items.map mass).sum)
    (force : minMass ≤ (items.map (fun x => if cut ≤ mass x then mass x else 0)).sum →
      items.length*target <
        (items.map (fun x => if cut ≤ mass x then rank x + 1 else 0)).sum) :
    ∃ x ∈ items, cut ≤ mass x ∧ target ≤ rank x := by
  have kept := retained_mass items mass cut
  have bound := force (by omega)
  apply Classical.byContradiction
  intro ex
  apply (Nat.not_lt_of_ge
    (sum_cap items (fun x => if cut ≤ mass x then rank x+1 else 0) target ?_)) bound
  intro x hx
  split
  next h =>
    have : ¬ target ≤ rank x := fun t => ex ⟨x,hx,h,t⟩
    omega
  next => omega

#print axioms thick_fiber_rank
#print axioms ternary_zero_trace
#print axioms incompatible_seven_nineteen
#print axioms seven_nineteen_merge
#print axioms hits_at_common_future
#print axioms coarsen_head
#print axioms change_on_block
#print axioms mix_cells
#print axioms word_mass

end HeadSampling
