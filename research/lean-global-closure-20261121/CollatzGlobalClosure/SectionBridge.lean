import CollatzGlobalClosure.BandOffset
import CollatzGlobalClosure.MarkedCylinders
import CollatzGlobalClosure.MarkedResetWitness
import CollatzGlobalClosure.SectionResetReturns

/-!
Composition with the exact forced section from the frozen PR #173 source.
The independently named ordinary maps are proved equal here. In particular,
the thin family inhabits the same `Marked` predicate used by `bounded_visit`
and by the actual first-positive-return theorem.
-/

namespace CollatzSectionBridge

open CollatzShell CollatzShell.ForwardSection

theorem endpoint_orbit_eq (k n : Nat) :
    CollatzEndpointSteering.orbit k n = CollatzShell.orbit k n := by
  induction k generalizing n with
  | zero => rfl
  | succ k ih => exact ih (CollatzShell.step n)

theorem witness_orbit_eq (k n : Nat) :
    CollatzMarkedResetWitness.orbit k n = CollatzShell.orbit k n := by
  induction k generalizing n with
  | zero => rfl
  | succ k ih => exact ih (CollatzShell.step n)

theorem cylinder_marked_eq (n : Nat) :
    CollatzMarkedCylinders.Marked n ↔ Marked n := Iff.rfl

theorem witness_marked_eq (n : Nat) :
    CollatzMarkedResetWitness.Marked n ↔ Marked n := Iff.rfl

/-- The offset transfer is about the actual ordinary map in the section theorem.
It is a finite ordinary descent; it does not assert a smaller marked return. -/
theorem offset_descent {d k a : Nat} (ha : 0 < a) (kd : k ≤ d)
    (drop : CollatzShell.orbit k a < a) :
    CollatzShell.orbit k (2^d+a) < 2^d+a := by
  rw [← endpoint_orbit_eq] at drop ⊢
  exact CollatzBandOffset.band_descent ha kd drop

/-- A supplied terminal certificate can be used at its actual clock, provided
the high-bit padding lasts that long. -/
theorem offset_certificate_descent {d k a : Nat} (ha : 1 < a) (kd : k ≤ d)
    (hit : CollatzShell.orbit k a = 1) :
    CollatzShell.orbit k (2^d+a) < 2^d+a := by
  rw [← endpoint_orbit_eq] at hit ⊢
  exact CollatzBandOffset.band_descent_of_certificate ha kd hit

/-- The exponentially thin family uses the exact forced section and has no
strict ordinary descent through its entire binary-exponent clock. Its smaller
offset has the same finite survival property. -/
theorem thin_family_in_section (m : Nat) (hm : 0 < m) :
    let n := CollatzBandOffset.thinSeed m
    let a := CollatzBandOffset.thinOffset m
    Marked n ∧ n = 2^n.log2+a ∧ 2^m*a < 2^n.log2 ∧
      ∀ k ≤ n.log2, n ≤ CollatzShell.orbit k n ∧ a ≤ CollatzShell.orbit k a := by
  dsimp only
  refine ⟨CollatzBandOffset.thinSeed_marked m hm, ?_, ?_, ?_⟩
  · rw [CollatzBandOffset.thinSeed_log2]
    exact CollatzBandOffset.thinSeed_split m
  · have h := CollatzBandOffset.thinSeed_width m
    rw [CollatzBandOffset.thinSeed_log2]
    rwa [CollatzBandOffset.thinSeed_log2,
      CollatzBandOffset.thinSeed_split, Nat.add_sub_cancel_left] at h
  · intro k hk
    rw [CollatzBandOffset.thinSeed_log2] at hk
    rw [← endpoint_orbit_eq, ← endpoint_orbit_eq]
    exact ⟨CollatzBandOffset.thinSeed_no_descent m k hk,
      CollatzBandOffset.thinOffset_no_descent m k hk⟩

/-- The binary-exponent clock obstruction survives every finite exception range. -/
theorem cofinal_marked_clock_obstruction (L : Nat) :
    ∃ n, L < n ∧ 1 < n ∧ Marked n ∧
      ∀ k ≤ n.log2, n ≤ CollatzShell.orbit k n := by
  let m := L+1
  let n := CollatzBandOffset.thinSeed m
  obtain ⟨mark, split, _, survives⟩ := thin_family_in_section m (by dsimp [m]; omega)
  have lg := CollatzBandOffset.thinSeed_log2 m
  have pw := Nat.lt_two_pow_self (n := 5*m)
  have low : 2^(5*m) ≤ n := by
    change 2^(5*m) ≤ CollatzBandOffset.thinSeed m
    rw [split, lg]
    omega
  have big : 5*m < n := pw.trans_le low
  have nL : L < n := (show L < 5*m by dsimp [m]; omega).trans big
  have np : 1 < n := (show 1 ≤ 5*m by dsimp [m]; omega).trans_lt big
  exact ⟨n,nL,np,mark,fun k hk => (survives k hk).1⟩

set_option maxRecDepth 100000 in
set_option exponentiation.threshold 2048 in
/-- A concrete independent kernel calculation checks the same marked map. -/
theorem exact_reset_pair :
    let n := CollatzMarkedResetWitness.source
    let m := CollatzMarkedResetWitness.target
    Marked n ∧ Marked m ∧ CollatzShell.orbit 13 n = m ∧ n < m ∧
      n.log2 = 535 ∧ m.log2 = 541 := by
  obtain ⟨_, hn, hm, hit, inc, ln, lm, _⟩ :=
    CollatzMarkedResetWitness.exact_reset_pair
  exact ⟨hn,hm,by rwa [witness_orbit_eq] at hit,inc,ln,lm⟩

#print axioms endpoint_orbit_eq
#print axioms witness_orbit_eq
#print axioms thin_family_in_section
#print axioms cofinal_marked_clock_obstruction
#print axioms exact_reset_pair

end CollatzSectionBridge
