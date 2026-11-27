import Mathlib.Data.Nat.Basic
import Lean.Elab.Tactic.Omega

/-!
A finite cut rules out every later weighted meeting of a supplied crest.
The odd count includes the original all-odd Mersenne ramp.
-/

namespace Collatz.MersenneCrests

abbrev State := Nat × Nat

def next (z : State) : State :=
  ((if z.1 % 2 = 0 then z.1 / 2 else (3 * z.1 + 1) / 2),
   z.2 + z.1 % 2)

def run (z : State) : Nat → State
  | 0 => z
  | n+1 => next (run z n)

def crest (r : Nat) : State := (3^r - 1, r)

def onCycle (z : State) : Prop := z.1 = 1 ∨ z.1 = 2

instance (z : State) : Decidable (onCycle z) := by unfold onCycle; infer_instance

theorem run_add (z : State) (a b : Nat) :
    run z (a+b) = run (run z a) b := by
  induction b with
  | zero => rfl
  | succ b ih => exact congrArg next ih

private theorem run_succ_left (z : State) (h : Nat) :
    run z (h+1) = run (next z) h := by
  induction h with
  | zero => rfl
  | succ h ih => exact congrArg next ih

private theorem next_ramp (a q : Nat) (ha : 0 < a) :
    next (2*a-1,q) = (3*a-1,q+1) := by
  have odd : (2*a-1)%2 = 1 := by omega
  simp [next, odd] <;> omega

theorem initial_ramp (r q a : Nat) (ha : 0 < a) :
    run (2^r*a-1,q) r = (3^r*a-1,q+r) := by
  induction r generalizing q a with
  | zero => simp [run]
  | succ r ih =>
    rw [run_succ_left, Nat.pow_succ 2 r,
      show 2^r*2*a = 2*(2^r*a) by ac_rfl,
      next_ramp _ _ (Nat.mul_pos (Nat.pow_pos (by decide)) ha),
      show 3*(2^r*a)=2^r*(3*a) by ac_rfl, ih (q+1) (3*a) (by omega),
      show 3^r*(3*a)=3^(r+1)*a by rw [Nat.pow_succ]; ac_rfl]
    congr 1 <;> omega

theorem original_to_crest (r : Nat) :
    run (2^r-1,0) r = crest r := by
  simpa [crest] using initial_ramp r 0 1 (by decide)

private theorem cycle_next {z : State} (hz : onCycle z) : onCycle (next z) := by
  obtain ⟨x,q⟩ := z
  rcases hz with h | h <;> dsimp at h <;> subst x <;> simp [onCycle, next]

private theorem next_inj {z w : State} (hz : onCycle z) (hw : onCycle w)
    (h : next z = next w) : z = w := by
  obtain ⟨x,q⟩ := z
  obtain ⟨y,r⟩ := w
  rcases hz with hx | hx <;> rcases hw with hy | hy <;>
    dsimp at hx hy <;> subst x <;> subst y <;> simp [next] at h ⊢ <;> omega

private theorem runs_on_cycle (z : State) (hz : onCycle z) (h : Nat) :
    onCycle (run z h) := by
  induction h with
  | zero => exact hz
  | succ h ih => exact cycle_next ih

private theorem run_inj {z w : State} (hz : onCycle z) (hw : onCycle w) (h : Nat)
    (eq : run z h = run w h) : z = w := by
  induction h with
  | zero => exact eq
  | succ h ih => exact ih (next_inj (runs_on_cycle z hz h) (runs_on_cycle w hw h) eq)

theorem no_meeting_after_cut {z w : State} {cut : Nat}
    (hz : onCycle (run z cut)) (hw : onCycle (run w cut))
    (hne : run z cut ≠ run w cut) (h : Nat) : run z h ≠ run w h := by
  intro hm
  apply hne
  by_cases hh : h ≤ cut
  · obtain ⟨k, rfl⟩ := Nat.exists_eq_add_of_le hh
    rw [run_add, run_add, hm]
  · have hc : cut ≤ h := by omega
    obtain ⟨k, rfl⟩ := Nat.exists_eq_add_of_le hc
    rw [run_add, run_add] at hm
    exact run_inj hz hw k hm

set_option maxRecDepth 24000 in
set_option maxHeartbeats 4000000 in
private theorem cut19 :
    onCycle (run (crest 19) 200) ∧
    ∀ f : Fin 19, 0 < f.val →
      onCycle (run (crest f.val) 200) ∧
      run (crest 19) 200 ≠ run (crest f.val) 200 := by decide

/-- Prime exponent 19 has no shorter positive matched Mersenne at any
    common post-crest date, even though its trajectory reaches one. -/
theorem prime19_no_shortening {f : Nat} (hf : 0 < f) (hlt : f < 19) (h : Nat) :
    run (crest 19) h ≠ run (crest f) h := by
  obtain ⟨hw,hne⟩ := cut19.2 ⟨f,hlt⟩ hf
  exact no_meeting_after_cut cut19.1 hw hne h

theorem original19_no_shortening {f : Nat} (hf : 0 < f) (hlt : f < 19) (h : Nat) :
    run (2^19-1,0) (19+h) ≠ run (2^f-1,0) (f+h) := by
  rw [run_add, run_add, original_to_crest, original_to_crest]
  exact prime19_no_shortening hf hlt h

set_option maxRecDepth 24000 in
theorem crest19_reaches_one : (run (crest 19) 97).1 = 1 := by decide

end Collatz.MersenneCrests
