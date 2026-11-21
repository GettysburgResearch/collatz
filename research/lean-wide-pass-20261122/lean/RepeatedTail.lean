import MarkedDensityPotential

/-!
The full ordinary-clock reference measure retains periodic sources as well.
This module checks its actual-map height input: after any repeated odd
state, every subsequent value is already represented before that repeat.
The infinite weighted tail estimate is stated separately in the proof note.
-/

namespace CollatzShell.WideRepeatedTail

open ForwardSection InverseDensityPotential

theorem odd_orbit_positive_odd (n : Nat) (positive : 0 < n)
    (odd : n % 2 = 1) (j : Nat) :
    0 < oddOrbit n j ∧ oddOrbit n j % 2 = 1 := by
  cases j with
  | zero => exact ⟨positive, odd⟩
  | succ j =>
    exact ⟨(odd_step_unit (oddOrbit n j)).1,
      (odd_step_unit (oddOrbit n j)).2.1⟩

theorem odd_step_le_double (n : Nat) (positive : 0 < n)
    (odd : n % 2 = 1) : oddStep n ≤ 2*n := by
  have exponent := odd_step_exponent_pos odd
  have power : 2 ≤ 2 ^ twos (3*n+1) := by
    exact (show 2 = 2^1 by rfl) ▸
      Nat.pow_le_pow_right (by decide : 0 < 2) exponent
  have split := odd_step_split n
  have bound := Nat.mul_le_mul_right (oddStep n) power
  nlinarith

theorem odd_orbit_height (n : Nat) (positive : 0 < n)
    (odd : n % 2 = 1) (j : Nat) : oddOrbit n j ≤ 2^j*n := by
  induction j with
  | zero => simp [oddOrbit]
  | succ j ih =>
    obtain ⟨pos, ho⟩ := odd_orbit_positive_odd n positive odd j
    have next := odd_step_le_double (oddOrbit n j) pos ho
    change oddStep (oddOrbit n j) ≤ _
    calc
      oddStep (oddOrbit n j) ≤ 2 * oddOrbit n j := next
      _ ≤ 2 * (2^j*n) := Nat.mul_le_mul_left 2 ih
      _ = 2^(j+1)*n := by ring

/-- No future state is discarded: it equals an explicitly bounded earlier
state. The repeated value need not belong to the trivial cycle. -/
theorem repeated_odd_prefix (n p q : Nat) (before : p < q)
    (hrep : oddOrbit n p = oddOrbit n q) :
    ∀ j : Nat, ∃ i : Nat, i < q ∧ oddOrbit n j = oddOrbit n i := by
  intro j
  induction j using Nat.strong_induction_on with
  | h j ih =>
    by_cases short : j < q
    · exact ⟨j, short, rfl⟩
    · have lower : p+(j-q) < j := by omega
      obtain ⟨i, hi, value⟩ := ih (p+(j-q)) lower
      refine ⟨i, hi, ?_⟩
      calc
        oddOrbit n j = oddOrbit (oddOrbit n q) (j-q) := by
          rw [← odd_orbit_add]
          congr 1
          omega
        _ = oddOrbit (oddOrbit n p) (j-q) := by rw [← hrep]
        _ = oddOrbit n (p+(j-q)) := (odd_orbit_add n p (j-q)).symm
        _ = oddOrbit n i := value

/-- This bound holds for the entire actual orbit once a repetition has
occurred; no periodic source is killed or assigned a fresh endpoint weight. -/
theorem repeated_odd_height (n p q : Nat) (positive : 0 < n)
    (odd : n % 2 = 1) (before : p < q)
    (hrep : oddOrbit n p = oddOrbit n q) (j : Nat) :
    oddOrbit n j ≤ 2^q*n := by
  obtain ⟨i, hi, eq⟩ := repeated_odd_prefix n p q before hrep j
  rw [eq]
  exact (odd_orbit_height n positive odd i).trans
    (Nat.mul_le_mul_right n
      (Nat.pow_le_pow_right (by decide : 0 < 2) (Nat.le_of_lt hi)))

#print axioms odd_orbit_positive_odd
#print axioms odd_step_le_double
#print axioms odd_orbit_height
#print axioms repeated_odd_prefix
#print axioms repeated_odd_height

end CollatzShell.WideRepeatedTail
