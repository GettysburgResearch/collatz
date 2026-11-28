import Lean.Elab.Tactic.Omega
import Init.Data.List.Nat.Range
import Init.Data.Nat.Lemmas

namespace CollatzResearch.ProtectedDescent

/-- Forward iteration, with time counted in edges. -/
def run (step : Nat → Nat) : Nat → Nat → Nat
  | 0, x => x
  | t + 1, x => run step t (step x)

theorem run_add (step : Nat → Nat) (i j x : Nat) :
    run step (i + j) x = run step j (run step i x) := by
  induction i generalizing x with
  | zero => simp [run]
  | succ i ih => simpa [Nat.succ_add, run] using ih (step x)

theorem run_pos (step : Nat → Nat) (h : ∀ x, 0 < x → 0 < step x)
    (t x : Nat) (hx : 0 < x) : 0 < run step t x := by
  induction t generalizing x with
  | zero => exact hx
  | succ t ih => exact ih (step x) (h x hx)

/-- Keep the ordinary step exactly at certified starts. -/
def modified (ordinary down : Nat → Nat) (good : Nat → Bool) (x : Nat) : Nat :=
  if good x then ordinary x else down x

/-- A true descending witness from the current height protects its original
first edge all the way until the path has fallen below the initial target. -/
theorem protectedSuffix (ordinary down : Nat → Nat) (good : Nat → Bool)
    (budget : Nat → Nat)
    (mono : ∀ a b, a ≤ b → budget a ≤ budget b)
    (cert : ∀ x, 1 < x →
      (good x = true ↔ ∃ t, 0 < t ∧ t ≤ budget x ∧ run ordinary t x < x))
    (root : Nat) (hroot : 1 < root) (t cur : Nat)
    (hc : root ≤ cur) (ht : t ≤ budget root) (falls : run ordinary t cur < root) :
    ∃ j, j ≤ t ∧ run (modified ordinary down good) j cur < root := by
  induction t generalizing cur with
  | zero => exact ⟨0, Nat.le_refl _, falls⟩
  | succ t ih =>
    have keep : good cur = true := (cert cur (by omega)).2
      ⟨t+1, by omega, Nat.le_trans ht (mono root cur hc), Nat.lt_of_lt_of_le falls hc⟩
    have edge : modified ordinary down good cur = ordinary cur := by simp [modified, keep]
    by_cases next : ordinary cur < root
    · exact ⟨1, by omega, by simpa [run, edge] using next⟩
    · obtain ⟨j,hj,hy⟩ := ih (ordinary cur) (by omega) (by omega) falls
      exact ⟨j+1, by omega, by simpa [run, edge] using hy⟩

/-- A decidable true-descent modification with nondecreasing lookahead takes
every positive start to one. The statement concerns this modified step. -/
theorem modified_reaches_one (ordinary down : Nat → Nat) (good : Nat → Bool)
    (budget : Nat → Nat)
    (mono : ∀ a b, a ≤ b → budget a ≤ budget b)
    (cert : ∀ x, 1 < x →
      (good x = true ↔ ∃ t, 0 < t ∧ t ≤ budget x ∧ run ordinary t x < x))
    (ordinary_pos : ∀ x, 0 < x → 0 < ordinary x)
    (down_pos : ∀ x, 0 < x → 0 < down x)
    (down_lt : ∀ x, 1 < x → down x < x)
    (x : Nat) (hx : 0 < x) :
    ∃ t, run (modified ordinary down good) t x = 1 := by
  have positive : ∀ z, 0 < z → 0 < modified ordinary down good z := by
    intro z hz
    cases hg : good z <;> simp [modified, hg, ordinary_pos z hz, down_pos z hz]
  induction x using Nat.strongRecOn with
  | ind x ih =>
    by_cases h1 : x = 1
    · exact ⟨0, h1⟩
    have h2 : 1 < x := by omega
    have descend : ∃ j, run (modified ordinary down good) j x < x := by
      cases hg : good x with
      | false => exact ⟨1, by simpa [run, modified, hg] using down_lt x h2⟩
      | true =>
        obtain ⟨t,_,ht,falls⟩ := (cert x h2).1 hg
        obtain ⟨j,_,hj⟩ := protectedSuffix ordinary down good budget mono cert x h2
          t x (Nat.le_refl _) ht falls
        exact ⟨j,hj⟩
    obtain ⟨j,hj⟩ := descend
    obtain ⟨l,hl⟩ := ih _ hj (run_pos _ positive j x hx)
    exact ⟨j+l, by rw [run_add]; exact hl⟩

/-- The ordinary shortcut Collatz map and the allowed down branch. -/
def ordinaryStep (x : Nat) : Nat :=
  if x % 2 = 0 then x / 2 else (3*x+1) / 2

def downStep (x : Nat) : Nat := (x+1) / 2

/-- Keep the ordinary step at one. Else search all times up to floor(log₂ x). -/
def keepStep (x : Nat) : Bool :=
  if x ≤ 1 then true else
    (List.range (x.log2 + 1)).any (fun t => decide (0 < t ∧ run ordinaryStep t x < x))

theorem keepStep_spec (x : Nat) (hx : 1 < x) :
    keepStep x = true ↔
      ∃ t, 0 < t ∧ t ≤ x.log2 ∧ run ordinaryStep t x < x := by
  simp only [keepStep, ite_eq_right (Nat.not_le_of_gt hx), List.any_eq_true,
    List.mem_range, decide_eq_true_eq]
  constructor
  · rintro ⟨t, ht, hp, hf⟩
    exact ⟨t, hp, by omega, hf⟩
  · rintro ⟨t, hp, ht, hf⟩
    exact ⟨t, by omega, hp, hf⟩

/-- Every positive input reaches one under this explicit modified Collatz map. -/
theorem explicit_reaches_one (x : Nat) (hx : 0 < x) :
    ∃ t, run (modified ordinaryStep downStep keepStep) t x = 1 := by
  apply modified_reaches_one ordinaryStep downStep keepStep Nat.log2 _ keepStep_spec _ _ _ x hx
  · intro a b hab
    by_cases ha : a = 0
    · simp [ha, Nat.log2_zero]
    · have hb : b ≠ 0 := by omega
      exact (Nat.le_log2 hb).2 (Nat.le_trans (Nat.log2_self_le ha) hab)
  · intro y hy
    unfold ordinaryStep
    split <;> omega
  · intro y hy
    unfold downStep
    omega
  · intro y hy
    unfold downStep
    omega

end CollatzResearch.ProtectedDescent
