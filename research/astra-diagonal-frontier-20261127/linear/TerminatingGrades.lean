import NativeTightness

/-!
Exact synchronized classes in the component of 1.  The two witnesses of
arrival at 1 may be any visits, including visits after extra complete laps.
A cross sum expresses equality of the signed defects t - 2*q over naturals.
-/

set_option autoImplicit false
set_option warningAsError true

namespace Collatz.NativeGate

private theorem one_phase_grade (n : ℕ) :
    2 * odds 1 n + 1 = n + orbit 1 n := by
  by_cases he : n % 2 = 0
  · obtain ⟨k, rfl⟩ : ∃ k : ℕ, n = 2 * k := ⟨n / 2, by omega⟩
    rw [(one_even_clock k).1, (one_even_clock k).2]
  · obtain ⟨k, rfl⟩ : ∃ k : ℕ, n = 2 * k + 1 := ⟨n / 2, by omega⟩
    change 2 * (odds 1 (2*k) + orbit 1 (2*k) % 2) + 1 =
      2*k + 1 + step (orbit 1 (2*k))
    rw [(one_even_clock k).1, (one_even_clock k).2]
    change 2 * (k + 1) + 1 = 2*k + 1 + 2
    omega

private theorem grade_after_visit {x n : ℕ} (h : orbit x n = 1) (u : ℕ) :
    2 * odds x (n + u) + 1 = 2 * odds x n + u + orbit x (n + u) := by
  rw [odds_add, orbit_add, h]
  have hphase := one_phase_grade u
  omega

/-- A common labelled state forces equal defects at the supplied visits. -/
theorem visit_grade_of_synchronized {x z nx nz t : ℕ}
    (hx : orbit x nx = 1) (hz : orbit z nz = 1)
    (hm : orbit x t = orbit z t) (hq : odds x t = odds z t) :
    nx + 2 * odds z nz = nz + 2 * odds x nx := by
  have hmx : orbit x (t + (nx + nz)) = orbit z (t + (nx + nz)) := by
    rw [orbit_add x t, orbit_add z t, hm]
  have hqx : odds x (t + (nx + nz)) = odds z (t + (nx + nz)) := by
    rw [odds_add x t, odds_add z t, hm, hq]
  have hleft := grade_after_visit hx (t + nz)
  have hright := grade_after_visit hz (t + nx)
  rw [show nx + (t + nz) = t + (nx + nz) by omega] at hleft
  rw [show nz + (t + nx) = t + (nx + nz) by omega] at hright
  omega

/-- Equality of the two visit defects supplies a common date and a common
odd count. Padding uses full actual laps of the positive cycle at 1. -/
theorem synchronized_of_visit_grade {x z nx nz : ℕ}
    (hx : orbit x nx = 1) (hz : orbit z nz = 1)
    (hd : nx + 2 * odds z nz = nz + 2 * odds x nx) :
    ∃ t, orbit x t = orbit z t ∧ odds x t = odds z t := by
  refine ⟨nx + 2 * odds z nz, ?_, ?_⟩
  · calc
      orbit x (nx + 2 * odds z nz) = 1 := by
        rw [orbit_add, hx, (one_even_clock _).1]
      _ = orbit z (nx + 2 * odds z nz) := by
        rw [hd, orbit_add, hz, (one_even_clock _).1]
  · calc
      odds x (nx + 2 * odds z nz) = odds x nx + odds z nz := by
        rw [odds_add, hx, (one_even_clock _).2]
      _ = odds z (nx + 2 * odds z nz) := by
        rw [hd, odds_add, hz, (one_even_clock _).2]
        omega

end Collatz.NativeGate
