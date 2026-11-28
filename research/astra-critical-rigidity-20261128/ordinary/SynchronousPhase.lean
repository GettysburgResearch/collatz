import AffineOrbit

/-! The genuine synchronous quotient of the positive shortcut map and its
finite-date cycle-entry decomposition. The density and Brownian inputs
in the accompanying manuscript are separate written results. -/

namespace Collatz.SynchronousPhase
open Collatz.PoweredAffine

abbrev Source := {n : ℕ // 0 < n}

def move (x : Source) : Source := ⟨step x.1, step_positive x.2⟩

def twice (x : Source) : Source := ⟨2 * x.1, by have := x.2; omega⟩

def walk (x : Source) (t : ℕ) : Source := ⟨orbit x.1 t, orbit_positive x.2 t⟩

private theorem walk_add (x : Source) (t u : ℕ) : walk x (t + u) = walk (walk x t) u := by
  induction t generalizing x with
  | zero => simp [walk, orbit]
  | succ t ih =>
    rw [Nat.succ_add]
    exact ih (move x)

private theorem persists {x y : Source} {t u : ℕ} (ht : walk x t = walk y t)
    (hu : t ≤ u) : walk x u = walk y u := by
  obtain ⟨d, rfl⟩ := Nat.exists_eq_add_of_le hu
  rw [walk_add, walk_add, ht]

def Meets (x y : Source) : Prop := ∃ t, walk x t = walk y t

def relation : Setoid Source where
  r := Meets
  iseqv := {
    refl := fun _ => ⟨0, rfl⟩
    symm := fun ⟨t, h⟩ => ⟨t, h.symm⟩
    trans := by
      rintro x y z ⟨t, ht⟩ ⟨u, hu⟩
      exact ⟨max t u, (persists ht (Nat.le_max_left _ _)).trans
        (persists hu (Nat.le_max_right _ _))⟩ }

def Phase := Quotient relation

def phase (x : Source) : Phase := Quotient.mk relation x

theorem phase_eq_iff (x y : Source) : phase x = phase y ↔ Meets x y :=
  ⟨Quotient.exact, fun h => Quotient.sound (s := relation) h⟩

private theorem move_twice (x : Source) : move (twice x) = x := by
  apply Subtype.ext
  change (if (2 * x.1) % 2 = 0 then 2 * x.1 / 2 else _) = x.1
  simp

private theorem move_meets {x y : Source} : Meets (move x) (move y) ↔ Meets x y := by
  constructor
  · rintro ⟨t, ht⟩
    exact ⟨t + 1, ht⟩
  · rintro ⟨t, ht⟩
    exact ⟨t, (show walk x (t + 1) = walk y (t + 1) from persists ht (Nat.le_succ t))⟩

private theorem twice_meets {x y : Source} (h : Meets x y) : Meets (twice x) (twice y) :=
  move_meets.mp (by simpa only [move_twice] using h)

/-- Both directions are actual positive integer operations. -/
def shift : Equiv.Perm Phase where
  toFun := Quotient.map move fun _ _ h => move_meets.mpr h
  invFun := Quotient.map twice fun _ _ h => twice_meets h
  left_inv := by
    intro q
    refine Quotient.inductionOn q fun x => ?_
    apply Quotient.sound
    exact ⟨1, show move (twice (move x)) = move x from move_twice _⟩
  right_inv := by
    intro q
    refine Quotient.inductionOn q fun x => ?_
    change phase (move (twice x)) = phase x
    rw [move_twice]

theorem shift_phase (x : Source) : shift (phase x) = phase (move x) := rfl

theorem inverse_shift_phase (x : Source) : shift.symm (phase x) = phase (twice x) := rfl

/-- The class of the odd input is exactly the class of its unshortened odd output. -/
theorem odd_triple_phase (x : Source) (hx : x.1 % 2 = 1) :
    phase ⟨3 * x.1 + 1, by omega⟩ = phase x := by
  apply (phase_eq_iff _ _).mpr
  refine ⟨1, Subtype.ext ?_⟩
  change step (3 * x.1 + 1) = step x.1
  have he : (3 * x.1 + 1) % 2 = 0 := by omega
  simp [step, he, hx]

/-- A periodic phase is an actual repeat on a positive tail. -/
theorem phase_return_iff (x : Source) (p : ℕ) :
    phase (walk x p) = phase x ↔ ∃ t, walk x (t + p) = walk x t := by
  rw [phase_eq_iff]
  constructor <;> rintro ⟨t, ht⟩ <;> refine ⟨t, ?_⟩
  · rwa [Nat.add_comm, walk_add]
  · rwa [Nat.add_comm t p, walk_add] at ht

/-- A whole finite family of equal phases has one genuine common date. -/
theorem family_meeting_iff {ι : Type*} [Fintype ι] (sources : ι → Source) (y : Source) :
    (∀ i, phase (sources i) = phase y) ↔ ∃ t, ∀ i, walk (sources i) t = walk y t := by
  constructor
  · intro h
    classical
    choose t ht using fun i => (phase_eq_iff (sources i) y).mp (h i)
    exact ⟨Finset.univ.sup t, fun i => persists (ht i) (Finset.le_sup (Finset.mem_univ i))⟩
  · rintro ⟨t, ht⟩ i
    exact (phase_eq_iff _ _).mpr ⟨t, ht i⟩

def Periodic (p : ℕ) (x : Source) : Prop := walk x p = x

private theorem periodic_future {p : ℕ} {x : Source} (hx : Periodic p x) (t : ℕ) :
    Periodic p (walk x t) := by
  unfold Periodic at hx ⊢
  rw [← walk_add, Nat.add_comm, walk_add, hx]

private theorem repeat_laps {x : Source} {p : ℕ} (h : Periodic p x) (k : ℕ) :
    walk x (p * k) = x := by
  induction k with
  | zero => rfl
  | succ k ih => rw [Nat.mul_succ, walk_add, ih]; exact h

/-- Once two same-phase arms both have the supplied positive period, their
actual values at that date agree. No counting or balancing assumption enters. -/
theorem equal_on_periodic_locus {x y : Source} {H p : ℕ} (hp : 0 < p)
    (hx : Periodic p (walk x H)) (hy : Periodic p (walk y H)) :
    walk x H = walk y H ↔ phase x = phase y := by
  constructor
  · intro h
    exact (phase_eq_iff _ _).mpr ⟨H, h⟩
  · intro eq
    obtain ⟨t, ht⟩ := (phase_eq_iff _ _).mp eq
    have hbig : t ≤ H + p * (t + 1) := by
      have := Nat.le_mul_of_pos_left (t + 1) hp
      omega
    have same := persists ht hbig
    rwa [walk_add, walk_add, repeat_laps hx, repeat_laps hy] at same

def FirstIn (target : Source → Prop) (x : Source) (t : ℕ) : Prop :=
  target (walk x t) ∧ ∀ u < t, ¬target (walk x u)

/-- A genuine equality before both entries forces their exact entry dates to agree. -/
theorem same_future_entry {target : Source → Prop} {x y : Source} {t u H : ℕ}
    (hx : FirstIn target x t) (hy : FirstIn target y u)
    (hxt : H ≤ t) (hyu : H ≤ u) (same : walk x H = walk y H) : t = u := by
  apply Nat.le_antisymm
  · by_contra! h
    exact (hx.2 u h) ((persists same hyu).symm ▸ hy.1)
  · by_contra! h
    exact (hy.2 t h) ((persists same hxt) ▸ hx.1)

private theorem periodic_after_entry {x : Source} {t H p : ℕ}
    (hx : FirstIn (Periodic p) x t) (ht : t ≤ H) : Periodic p (walk x H) := by
  obtain ⟨d, rfl⟩ := Nat.exists_eq_add_of_le ht
  rw [walk_add]
  exact periodic_future hx.1 d

/-- Exact finite-date partition into already periodic equal phases and
an unentered state with a common, strictly later first-entry clock. -/
theorem collision_at_clock_iff {x y : Source} {t u H p : ℕ} (hp : 0 < p)
    (hx : FirstIn (Periodic p) x t) (hy : FirstIn (Periodic p) y u) :
    walk x H = walk y H ↔
      (t ≤ H ∧ u ≤ H ∧ phase x = phase y) ∨
      (H < t ∧ t = u ∧ walk x H = walk y H) := by
  constructor
  · intro same
    by_cases ht : t ≤ H
    · have hu : u ≤ H := by
        by_contra! late
        exact (hy.2 H late) (same ▸ periodic_after_entry hx ht)
      exact Or.inl ⟨ht, hu, (phase_eq_iff _ _).mpr ⟨H, same⟩⟩
    · have hu : H ≤ u := by
        by_contra! early
        exact (hx.2 H (by omega)) (same.symm ▸ periodic_after_entry hy (by omega))
      exact Or.inr ⟨by omega, same_future_entry hx hy (by omega) hu same, same⟩
  · rintro (⟨ht, hu, h⟩ | ⟨_, _, h⟩)
    · exact (equal_on_periodic_locus hp (periodic_after_entry hx ht)
        (periodic_after_entry hy hu)).mpr h
    · exact h

end Collatz.SynchronousPhase
