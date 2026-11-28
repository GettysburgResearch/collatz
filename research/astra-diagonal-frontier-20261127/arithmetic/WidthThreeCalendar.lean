import WidthThree

namespace Collatz.WidthThree

/-! The deterministic calendar argument after the ordinary rank embedding.
The embedding, rank transitivity and analytic height contradiction remain
written in WIDTH_THREE.md. No hypothesis asserting cycle exclusion is used. -/

inductive ClockPhase where
  | one
  | firstTwo
  | secondTwo
  deriving DecidableEq

def Controlled (q : ClockPhase) (v : ℤ) : Prop :=
  match q with
  | .one => -3 ≤ v ∧ v ≤ 3
  | .firstTwo => -4 ≤ v ∧ v ≤ 4
  | .secondTwo => -3 ≤ v ∧ v ≤ 3

def ClockStep (q r : ClockPhase) (v d w : ℤ) : Prop :=
  -6 ≤ d ∧ d ≤ 6 ∧
  match q with
  | .one => r = .firstTwo ∧ 2*w = 3*v+d ∧ 4 ∣ w
  | .firstTwo => (r = .one ∨ r = .secondTwo) ∧ d = 0 ∧ 4*w = 3*v
  | .secondTwo => r = .one ∧ 4*w = 3*v+d

theorem controlledZero (q : ClockPhase) : Controlled q 0 := by
  cases q <;> norm_num [Controlled]

theorem controlledStep {q r : ClockPhase} {v d w : ℤ}
    (hv : Controlled q v) (hs : ClockStep q r v d w) : Controlled r w := by
  rcases hs with ⟨hlo, hhi, hs⟩
  cases q with
  | one =>
      obtain ⟨hr, heq, hm⟩ := hs
      subst r
      obtain ⟨j, hj⟩ := hm
      simp only [Controlled] at hv ⊢
      omega
  | firstTwo =>
      obtain ⟨hr, _, heq⟩ := hs
      rcases hr with hr | hr <;> subst r <;>
        simp only [Controlled] at hv ⊢ <;> omega
  | secondTwo =>
      obtain ⟨hr, heq⟩ := hs
      subst r
      simp only [Controlled] at hv ⊢
      omega

theorem controlledFromZero (q : Nat → ClockPhase) (h d : Nat → ℤ)
    (hs : ∀ n, ClockStep (q n) (q (n+1)) (h n) (d n) (h (n+1)))
    (hz : h 0 = 0) : ∀ n, Controlled (q n) (h n) := by
  intro n
  induction n with
  | zero => rw [hz]; exact controlledZero (q 0)
  | succ n ih => exact controlledStep ih (hs n)

theorem forcedSecondZero {v : ℤ} (hv : Controlled .secondTwo v)
    (hm : 4 ∣ v) : v = 0 := by
  obtain ⟨j, hj⟩ := hm
  simp only [Controlled] at hv
  omega

theorem nonzeroStepSign {q r : ClockPhase} {v d w : ℤ}
    (hs : ClockStep q r v d w) (hv : v ≠ 0) (hw : w ≠ 0) :
    (0 < v ↔ 0 < w) := by
  rcases hs with ⟨hlo, hhi, hs⟩
  cases q with
  | one =>
      obtain ⟨_, heq, hm⟩ := hs
      obtain ⟨j, hj⟩ := hm
      omega
  | firstTwo =>
      obtain ⟨_, _, heq⟩ := hs
      omega
  | secondTwo =>
      obtain ⟨_, heq⟩ := hs
      omega

theorem nonzeroAllSign (q : Nat → ClockPhase) (h d : Nat → ℤ)
    (hs : ∀ n, ClockStep (q n) (q (n+1)) (h n) (d n) (h (n+1)))
    (hn : ∀ n, h n ≠ 0) : ∀ n, (0 < h n ↔ 0 < h 0) := by
  intro n
  induction n with
  | zero => rfl
  | succ n ih =>
      exact (nonzeroStepSign (hs n) (hn n) (hn (n+1))).symm.trans ih

end Collatz.WidthThree
