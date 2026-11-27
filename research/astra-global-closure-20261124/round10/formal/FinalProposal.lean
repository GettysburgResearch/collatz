import SmoothCore
import TowerClock

/-! Ordinary minimum-source consequences of the round-ten path theorems.
The final universal consumer retains PR192's OPEN FrontierMerger premise. -/

namespace Collatz.RoundTen

open Collatz.SourceDeletion Collatz.MinimumFailure Collatz.SmoothCore
open Collatz.TowerClock

theorem run_positive (t : Nat) {n : Nat} (hn : 0 < n) : 0 < run t n := by
  induction t generalizing n with
  | zero => exact hn
  | succ t ih =>
    apply ih
    unfold step
    split <;> omega

/-- The full two-run budget excludes an actual first bad tower. Positivity
comes from the same ordinary orbit, not from a rational inverse control. -/
theorem no_two_run_tower {w r m e a b : Nat}
    (start : 3^r*w+1=2^m*a) (exitRow : 3^m*a=2^e*b+1)
    (budget : 2*3^(m+r) ≤ 2^(m+e)) : ¬ FirstTower w r := by
  intro tower
  obtain ⟨path, smaller⟩ := two_run_drop tower.positive start exitRow budget
  have positive : 0 < b := by
    rw [← path]
    exact run_positive _ (Nat.mul_pos (Nat.pow_pos (by decide)) tower.positive)
  have good : Good b := by
    simpa using tower.smaller b positive smaller 0
  exact tower.bad ((good_run (m+e) _).mp (by simpa [path] using good))

/-- An entire family with a return beyond its initial clock obstruction is
excluded. The elementary CRT construction of infinitely many parameters is
written separately; this theorem applies to every supplied ordinary tuple. -/
theorem no_delayed_family_tower {H w a b : Nat}
    (start : 3^(2*H)*w+1=2^(H+1)*a)
    (exitRow : 3^(H+1)*a=2^(5*H+2)*b+1) : ¬ FirstTower w (2*H) := by
  apply no_two_run_tower start exitRow
  have bound : 27^H ≤ 64^H := Nat.pow_le_pow_left (by decide) _
  rw [show H+1+2*H=3*H+1 by omega,
    show H+1+(5*H+2)=6*H+3 by omega, pow_succ, pow_add, pow_mul, pow_mul]
  change 2*(27^H*3) ≤ 64^H*8
  omega

/-- Prefixes through r clocks on the actual first bad tower have maximal odd
count among words of the same length and affine constant. This is a necessary
condition, not a sufficient condition for a bad orbit. -/
theorem first_tower_prefix_maximal {w r f : Nat} (tower : FirstTower w r)
    (clock : f ≤ r) {v : List Bool} (len : v.length=f)
    (same : carry v=carry (trace f (3^r*w))) :
    weight v ≤ weight (trace f (3^r*w)) := by
  by_contra no
  let a := weight (trace f (3^r*w))
  let d := weight v-a
  have more : a < weight v := by dsimp [a]; omega
  have cap : weight v ≤ f := len ▸ weight_le v
  have eq : weight v=a+d := by dsimp [d]; omega
  have split : r=d+(r-d) := by dsimp [d]; omega
  have source : 3^r*w=3^d*(3^(r-d)*w) := by
    calc
      _ = 3^(d+(r-d))*w := congrArg (fun z : Nat => 3^z*w) split
      _ = _ := by rw [pow_add]; ring
  have path := lower_power_meeting len same eq source
  have good : Good (3^(r-d)*w) := tower.earlier (r-d) (by dsimp [d]; omega)
  have endpoint : Good (run f (3^r*w)) := by
    rw [← path.2]
    exact (good_run f _).mpr good
  exact tower.bad ((good_run f _).mp endpoint)

/-- OPEN INPUT. This is the existing PR192 universal consumer, reproduced
at the end of the checked assembly to make the remaining premise visible.
The finite-clock results above do not establish FrontierMerger. -/
theorem final_proposal (open_merger : FrontierMerger) :
    ∀ n : Nat, 0 < n → Good n :=
  universal_iff_frontier_merger.mpr open_merger

#print axioms run_positive
#print axioms no_two_run_tower
#print axioms no_delayed_family_tower
#print axioms first_tower_prefix_maximal
#print axioms final_proposal

end Collatz.RoundTen
