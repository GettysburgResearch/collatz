import Std

namespace ClockCollision

/-- Physical steps of a deterministic map, including the starting time. -/
def run {α : Type} (f : α → α) : Nat → α → α
  | 0, x => x
  | h + 1, x => f (run f h x)

theorem run_add {α : Type} (f : α → α) (a b : Nat) (x : α) :
    run f (a + b) x = run f b (run f a x) := by
  induction b with
  | zero => rfl
  | succ b ih => simp [run, ih]

/-- An early intersection with the partner's whole forward trace persists at the floor. -/
theorem trace_through_floor {α : Type} (f : α → α) (x y : α) (h : Nat) :
    (∃ i j, i ≤ h ∧ run f i x = run f j y) ↔ ∃ k, run f h x = run f k y := by
  constructor
  · rintro ⟨i, j, hi, hit⟩
    refine ⟨j + (h - i), ?_⟩
    have hx : run f h x = run f (h - i) (run f i x) := by
      rw [← run_add]
      congr 1
      omega
    rw [hx, hit, ← run_add]
  · rintro ⟨k, hit⟩
    exact ⟨h, k, Nat.le_refl _, hit⟩

/-- On an injective reference ray every witness has the same signed difference. -/
theorem unique_offset {α : Type} (f : α → α) {x y : α}
    (inj : ∀ a b, run f a y = run f b y → a = b)
    {i j k l : Nat} (u : run f i x = run f j y) (v : run f k x = run f l y) :
    (i : Int) - j = (k : Int) - l := by
  have same : run f (j + k) y = run f (l + i) y := by
    calc
      run f (j + k) y = run f k (run f j y) := run_add f _ _ _
      _ = run f k (run f i x) := by rw [u]
      _ = run f (i + k) x := (run_add f _ _ _).symm
      _ = run f (k + i) x := by rw [Nat.add_comm i k]
      _ = run f i (run f k x) := run_add f _ _ _
      _ = run f i (run f l y) := by rw [v]
      _ = run f (l + i) y := (run_add f _ _ _).symm
  have eq := inj _ _ same
  omega

/-- A common physical clock distinguishes every block assigned a different root. -/
theorem disjoint_routed_blocks {α : Type} (f : α → α) (h : Nat)
    {P Q : α → Prop} {y z : α} (distinct : y ≠ z)
    (left : ∀ x, P x → run f h x = y) (right : ∀ x, Q x → run f h x = z) :
    ∀ x, P x → Q x → False := by
  intro x hx gx
  exact distinct ((left x hx).symm.trans (right x gx))

def shortcut (n : Nat) : Nat :=
  if n % 2 = 0 then n / 2 else (3*n+1) / 2

/-- The complete two-branch predecessor equation used in the energy sum. -/
theorem predecessor (n y : Nat) :
    shortcut n = y ↔ n = 2*y ∨ (y % 3 = 2 ∧ 3*n+1 = 2*y) := by
  unfold shortcut
  split <;> omega

/-- Exact one-step pushforward of the histogram of any finite multiset of sources. -/
theorem pushforward_bucket (sources : List Nat) (y : Nat) :
    (sources.map shortcut).count y =
    sources.count (2*y) + (if y % 3 = 2 then sources.count ((2*y-1)/3) else 0) := by
  induction sources with
  | nil => simp
  | cons n xs ih =>
    simp only [List.map_cons, List.count_cons, beq_iff_eq, ih, predecessor]
    repeat' split
    all_goals omega

/-- Only the ordinary cycle 1,2 has period dividing two on positive inputs. -/
theorem only_two_cycle (n : Nat) (pos : n > 0) :
    shortcut (shortcut n) = n ↔ n = 1 ∨ n = 2 := by
  rw [predecessor]
  unfold shortcut
  split <;> omega

/-- At a two-parent junction the new ordered equal-endpoint pairs are the cross pairs. -/
theorem branch_energy (a b : Nat) :
    (a + b) * (a + b) = a * a + b * b + 2 * (a * b) := by
  simp [Nat.add_mul, Nat.mul_add, Nat.mul_comm b a, Nat.two_mul]
  omega

/-- Finite-time first-collision flux, before taking any probabilistic limit. -/
theorem accumulate_flux (energy flux : Nat → Nat)
    (step : ∀ t, energy (t+1) = energy t + 2 * flux t) (h : Nat) :
    energy h = energy 0 + 2 * ((List.range h).map flux).sum := by
  induction h with
  | zero => simp
  | succ n ih =>
    rw [step, ih]
    simp [List.range_succ, Nat.mul_add, Nat.add_assoc]

#print axioms trace_through_floor
#print axioms unique_offset
#print axioms disjoint_routed_blocks
#print axioms predecessor
#print axioms pushforward_bucket
#print axioms only_two_cycle
#print axioms branch_energy
#print axioms accumulate_flux

end ClockCollision
