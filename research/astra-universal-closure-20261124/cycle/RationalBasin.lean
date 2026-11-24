import Std

/-! The shortcut map on the rational lattice with denominator 13, in numerator
coordinates. All statements below concern this fixed lattice. -/
namespace CollatzRationalBasin

set_option maxRecDepth 100000
set_option maxHeartbeats 3000000

def step (n : Nat) : Nat :=
  if n % 2 = 0 then n / 2 else (3*n + 13) / 2

def run : Nat → Nat → Nat
  | 0, n => n
  | k+1, n => step (run k n)

def reachesCycle (n : Nat) := ∃ k, run k n = 283

def otherCycles : List Nat :=
  [1,2,4,8,13,26,131,179,203,211,227,251,259,262,275,287,311,323,
   331,341,347,358,383,395,419,422,437,439,454,473,491,502,503,518,
   524,527,574,581,599,601,635,662,665,682,716,743,761,797,844,878,
   905,908,959,1004,1048,1087,1121,1148,1202,1231,1364,1393,1445,
   1637,1688,1853,2096,2174,2462,2786]

theorem run_add (a b n : Nat) : run (a+b) n = run b (run a n) := by
  induction b with
  | zero => rfl
  | succ b ih => exact congrArg step ih

theorem closed : ∀ n ∈ otherCycles, step n ∈ otherCycles := by
  have check : otherCycles.all (fun n => otherCycles.contains (step n)) = true := by decide
  intro n hn
  exact List.contains_iff_mem.mp (List.all_eq_true.mp check n hn)

theorem stays (k n : Nat) (hn : n ∈ otherCycles) : run k n ∈ otherCycles := by
  induction k with
  | zero => exact hn
  | succ k ih => exact closed _ ih

theorem lowerCutoff (n : Nat) (positive : 0 < n)
    (small : n < 283 ∨ (n < 579 ∧ 3 ∣ n)) : ¬ reachesCycle n := by
  have check : (List.range 579).all (fun m =>
      if 0 < m ∧ (m < 283 ∨ 3 ∣ m) then otherCycles.contains (run 70 m) else true) = true := by
    decide
  have hb : n < 579 := by omega
  have included := List.all_eq_true.mp check n (List.mem_range.mpr hb)
  have hcond : 0 < n ∧ (n < 283 ∨ 3 ∣ n) := by omega
  rw [ite_eq_left hcond] at included
  rintro ⟨k, hk⟩
  have hstays := stays k (run 70 n) (List.contains_iff_mem.mp included)
  rw [← run_add, Nat.add_comm 70 k, run_add, hk] at hstays
  exact (by decide : run 70 283 ∉ otherCycles) hstays

theorem cycleAndLift : run 8 283 = 283 ∧ run 9 579 = 283 := by decide

theorem leastBasinNumerator : reachesCycle 283 ∧
    ∀ n, 0 < n → n < 283 → ¬ reachesCycle n := by
  exact ⟨⟨0, rfl⟩, fun n hn hlt => lowerCutoff n hn (Or.inl hlt)⟩

theorem leastMultipleNumerator : reachesCycle 579 ∧ 3 ∣ 579 ∧
    ∀ n, 0 < n → n < 579 → 3 ∣ n → ¬ reachesCycle n := by
  exact ⟨⟨9, cycleAndLift.2⟩, by decide, fun n hn hlt hm => lowerCutoff n hn (Or.inr ⟨hlt, hm⟩)⟩

theorem firstTriplingDisagreement :
    ¬ reachesCycle 193 ∧ reachesCycle (3*193) ∧
    ∀ n, 0 < n → n < 193 → (¬ reachesCycle n ∧ ¬ reachesCycle (3*n)) := by
  refine ⟨lowerCutoff 193 (by decide) (by decide), ⟨9, cycleAndLift.2⟩, ?_⟩
  intro n hn hlt
  exact ⟨lowerCutoff n hn (Or.inl (by omega)),
    lowerCutoff (3*n) (by omega) (Or.inr ⟨by omega, Nat.dvd_mul_right 3 n⟩)⟩

theorem reaches_step (n : Nat) : reachesCycle n ↔ reachesCycle (step n) := by
  constructor
  · rintro ⟨k, hk⟩
    cases k with
    | zero =>
      change n = 283 at hk
      subst n
      exact ⟨7, by decide⟩
    | succ k =>
      refine ⟨k, ?_⟩
      change run k (run 1 n) = 283
      rw [← run_add, Nat.add_comm]
      exact hk
  · rintro ⟨k, hk⟩
    exact ⟨1+k, (run_add 1 k n).trans hk⟩

inductive LatticePath : Nat → Nat → Prop where
  | refl (n) : LatticePath n n
  | forward {x y} : LatticePath x y → LatticePath x (step y)
  | backward {x y} : LatticePath x (step y) → LatticePath x y

theorem path_preserves_basin {x y : Nat} (path : LatticePath x y) :
    reachesCycle x ↔ reachesCycle y := by
  induction path with
  | refl => exact Iff.rfl
  | forward path ih => exact ih.trans (reaches_step _)
  | backward path ih => exact ih.trans (reaches_step _).symm

theorem noLowerPath (n : Nat) (positive : 0 < n)
    (small : n < 283 ∨ (n < 579 ∧ 3 ∣ n)) : ¬ LatticePath 283 n := by
  intro path
  exact lowerCutoff n positive small ((path_preserves_basin path).mp ⟨0, rfl⟩)

#print axioms run_add
#print axioms closed
#print axioms stays
#print axioms reaches_step
#print axioms path_preserves_basin
#print axioms noLowerPath
#print axioms lowerCutoff
#print axioms cycleAndLift
#print axioms leastBasinNumerator
#print axioms leastMultipleNumerator
#print axioms firstTriplingDisagreement
end CollatzRationalBasin
