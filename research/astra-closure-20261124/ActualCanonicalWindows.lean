import ActualCarry
import CanonicalWindows

/-! Substitute the actual discounted scalar on the positive odd Collatz orbit
into the finite canonical-window packing theorem. -/
namespace Collatz.CanonicalWindows
open Collatz.CarryTowerRoundTen.ActualScalar
open Collatz.StrictCarry.Actual
open Finset

noncomputable local instance (m : ℕ) : DecidableEq (Fin m → ℕ) := Classical.decEq _

theorem ordinary_canonical_window_count (q₀ N m : ℕ) (hq : 0 < q₀)
    (ho : Odd q₀) (hm : m ≤ N)
    (distinct : ∀ i ≤ N, ∀ j ≤ N, orbit q₀ i = orbit q₀ j → i = j)
    (height : ∀ i ≤ N, orbit q₀ i < 3^m) :
    N-m+1 ≤
      (((range (N-m+1)).image
        (fun i (k : Fin m) => canonical (orbit q₀ (i+k.val)))).card) +
      (((range (N+1)).filter (fun i => 0 < carry (orbit q₀ i))).card) * (m+1) := by
  exact canonical_window_count (orbit q₀) (fun i => gap (orbit q₀ i))
    (fun i => canonical (orbit q₀ i)) (fun i => carry (orbit q₀ i)) N m hm
    (fun i => complete_step (orbit q₀ i))
    (fun i => actual_edge (orbit q₀ i) (orbit_pos q₀ i hq) (orbit_odd q₀ i ho))
    distinct height

#print axioms ordinary_canonical_window_count
end Collatz.CanonicalWindows
