import PermanentSafeOrdinary

/-! The exact first-exit date after a genuine positive Syracuse path reaches one.
The reverse-record equivalence keeps both endpoints and every intermediate clock. -/

namespace SignedDeathClock

open PermanentSafeOrdinary

def Pass (m j : Nat) : Prop := 4 * clock m j ≤ 7 * j

def FirstExit (m t : Nat) : Prop := (∀ j < t, Pass m j) ∧ ¬ Pass m t

def ReverseRecord (m h : Nat) : Prop :=
  ∀ k ≤ h, (7 * k : Int) - 4 * ((clock m h : Int) - clock m (h - k)) ≤
    (7 * h : Int) - 4 * clock m h

theorem clock_after_hit (m h k : Nat) (hh : state m h = 1) :
    clock m (h + k) = clock m h + 2 * k := by
  rw [clock_add, hh, clock_one]

theorem pass_after_hit (m h j : Nat) (hh : state m h = 1) (hdate : h ≤ j) :
    Pass m j ↔ j + 4 * clock m h ≤ 8 * h := by
  obtain ⟨k, rfl⟩ := Nat.exists_eq_add_of_le hdate
  rw [Pass, clock_after_hit m h k hh]
  omega

theorem record_iff_pass (m h : Nat) :
    ReverseRecord m h ↔ ∀ j ≤ h, Pass m j := by
  constructor
  · intro hrec j hj
    have hr := hrec (h - j) (Nat.sub_le _ _)
    have he : h - (h - j) = j := by omega
    rw [he] at hr
    unfold Pass
    omega
  · intro hall k hk
    have ht := hall (h - k) (Nat.sub_le _ _)
    unfold Pass at ht
    omega

theorem first_exit_after_hit (m h : Nat) (hh : state m h = 1)
    (hp : ∀ j ≤ h, Pass m j) :
    FirstExit m (4 * (2 * h - clock m h) + 1) := by
  have he := hp h (by omega)
  unfold Pass at he
  have hs : clock m h ≤ 2 * h := by omega
  constructor
  · intro j hj
    by_cases hle : j ≤ h
    · exact hp j hle
    · exact (pass_after_hit m h j hh (by omega)).mpr (by omega)
  · rw [pass_after_hit m h _ hh (by omega)]
    omega

theorem death_grade_range (m h : Nat) (hp : Pass m h)
    (hn : m % 2 = 1) :
    2 * h - clock m h ≤ h ∧ h ≤ 4 * (2 * h - clock m h) := by
  have hclock : ∀ j, j ≤ clock m j := by
    intro j
    induction j with
    | zero => simp [clock]
    | succ j ih =>
      have ho := state_odd m hn j
      have hstep := exact_step (state m j)
      have hnodd := oddMap_odd (state m j)
      have hv : valuation (state m j) ≠ 0 := by
        intro hz
        rw [hz, pow_zero, one_mul] at hstep
        omega
      change j+1 ≤ clock m j + valuation (state m j)
      omega
  have hh := hclock h
  unfold Pass at hp
  omega

end SignedDeathClock

#print axioms SignedDeathClock.clock_after_hit
#print axioms SignedDeathClock.pass_after_hit
#print axioms SignedDeathClock.record_iff_pass
#print axioms SignedDeathClock.first_exit_after_hit
#print axioms SignedDeathClock.death_grade_range
