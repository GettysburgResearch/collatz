import SmoothCore

namespace Collatz.CorePrefix

open Collatz.SourceDeletion Collatz.MinimumFailure Collatz.SmoothCore

/-- A hit by the reference core supplies an ordinary merger at a strictly
smaller base on every sufficiently deep lift, with no bound on the exponent r. -/
theorem prefix_merger (r v h t : Nat) (hit : run h (3^r*v)=1) :
    run 2 (run h (3^r*(v+2^h*(4*t)))) =
      run h (3^r*(v+2^h*(3*t))) := by
  let z := 3^r*v
  have upper := lift h z (3^r*(4*t))
  have lower := lift h z (3^r*(3*t))
  change run h z=1 at hit
  rw [hit] at upper lower
  rw [show 3^r*(v+2^h*(4*t))=z+2^h*(3^r*(4*t)) by dsimp [z];ring,
      show 3^r*(v+2^h*(3*t))=z+2^h*(3^r*(3*t)) by dsimp [z];ring,
      upper,lower]
  let L := 3^(odds h z)*(3^r*t)
  rw [show 3^(odds h z)*(3^r*(4*t))=4*L by dsimp [L];ring,
      show 3^(odds h z)*(3^r*(3*t))=3*L by dsimp [L];ring]
  simp only [run]; unfold step; split <;> split <;> omega

/-- A hypothetical minimum forbids every lower reference whose hit of 1 leaves
two spare binary digits of agreement with the original, fixed core. -/
theorem no_fast_prefix {w r : Nat} (tower : FirstTower w r) {v h t : Nat}
    (hv : 0<v) (ht : 0<t) (shape : w=v+2^h*(4*t)) :
    run h (3^r*v) ≠ 1 := by
  intro hit
  have p : 0<2^h*t := Nat.mul_pos (Nat.pow_pos (by decide)) ht
  have small : v+2^h*(3*t)<w := by
    rw [shape]
    rw [show 2^h*(3*t)=3*(2^h*t) by ring, show 2^h*(4*t)=4*(2^h*t) by ring]
    omega
  have safe := tower.smaller (v+2^h*(3*t)) (by omega) small r
  have met := prefix_merger r v h t hit
  rw [←shape] at met
  apply tower.bad
  apply (good_run h _).mp
  apply (good_run 2 _).mp
  rw [met]
  exact (good_run h _).mpr safe

#print axioms prefix_merger
#print axioms no_fast_prefix
end Collatz.CorePrefix
