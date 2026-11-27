import Mathlib.Data.Nat.ModEq
import Mathlib.Tactic.Ring

/-! Finite arithmetic kernels for sparse corrections of odd Syracuse paths.
The correction can be positive, nonunit, bounded, congruent to one at a supplied
odd modulus and at the inherited dyadic precision. A legal ordinary suffix then
consumes one dyadic bit per physical step. The asymptotic construction is in
SPARSE_SHADOW.md. -/

namespace CollatzRound14.Adelic

/-- Divide an ordinary value with a prescribed dyadic quotient class. -/
theorem liftQuotient {v g s b : ℕ} (hg : 0 < g)
    (h : v ≡ g * b [MOD g * s]) :
    ∃ y, g * y = v ∧ y ≡ b [MOD s] := by
  have hd : v ≡ 0 [MOD g] := (h.of_dvd (dvd_mul_right _ _)).trans
    (Nat.modEq_zero_iff_dvd.mpr (dvd_mul_right _ _))
  obtain ⟨y, hy⟩ := Nat.modEq_zero_iff_dvd.mp hd
  exact ⟨y, hy.symm, Nat.ModEq.mul_left_cancel' hg.ne' (hy ▸ h)⟩

/-- Produce a bounded positive correction for a reset and preserve the
inherited agreement with carry one. Here g is the incoming divisor, s is
the desired quotient precision, and o is an odd simultaneous modulus. -/
theorem boundedSteering {x b g s o r : ℕ} (hg : 0 < g) (hs : 0 < s)
    (ho : 0 < o) (hwidth : 1 < g * s * o) (hco : (g * s).Coprime o)
    (hr : r ∣ g * s) (hpre : 3 * x + 1 ≡ g * b [MOD r]) :
    ∃ d y : ℕ, 1 < d ∧ d < 2 * (g * s * o) ∧
      d ≡ 1 [MOD o] ∧ d ≡ 1 [MOD r] ∧
      g * y = 3 * x + d ∧ y ≡ b [MOD s] := by
  let p := g * s
  have hp : 0 < p := Nat.mul_pos hg hs
  have hlarge : 3 * x ≤ p * (3 * x) + g * b := by
    have : 1 * (3 * x) ≤ p * (3 * x) :=
      Nat.mul_le_mul_right _ (Nat.succ_le_of_lt hp)
    omega
  let u := (p * (3 * x) + g * b) - 3 * x
  have hu : 3 * x + u = p * (3 * x) + g * b := by
    dsimp [u]
    omega
  let z := Nat.chineseRemainder hco u 1
  have hz : (z : ℕ) < p * o :=
    Nat.chineseRemainder_lt_mul hco _ _ hp.ne' ho.ne'
  let d := (z : ℕ) + p * o
  have hdp : d ≡ u [MOD p] := by simpa [d] using z.property.1
  have hdo : d ≡ 1 [MOD o] := by simpa [d] using z.property.2
  have hnew : 3 * x + d ≡ g * b [MOD p] := by
    refine (hdp.add_left _).trans ?_
    rw [hu]
    exact Nat.ModEq.modulus_mul_add
  have hdr : d ≡ 1 [MOD r] :=
    Nat.ModEq.add_left_cancel' _ ((hnew.of_dvd hr).trans hpre.symm)
  obtain ⟨y, hy, hyb⟩ := liftQuotient hg hnew
  refine ⟨d, y, ?_, ?_, hdo, hdr, hy, hyb⟩ <;> dsimp [d, p] at * <;> omega

/-- Positive-gap, unit-carry odd word on ordinary natural numbers. -/
inductive OddWord : List ℕ → ℕ → ℕ → Prop
  | nil (x : ℕ) (h : x % 2 = 1) : OddWord [] x x
  | cons {e x y z : ℕ} {es : List ℕ} (he : 0 < e) (hx : x % 2 = 1)
      (hedge : 2 ^ e * y = 3 * x + 1) (ht : OddWord es y z) :
      OddWord (e :: es) x z

theorem OddWord.oddSource {w : List ℕ} {x z : ℕ} (h : OddWord w x z) :
    x % 2 = 1 := by cases h <;> assumption

private theorem oddOfClose {a b r : ℕ} (hr : 0 < r) (hb : b % 2 = 1)
    (h : a ≡ b [MOD 2 ^ r]) : a % 2 = 1 := by
  obtain ⟨j, rfl⟩ := Nat.exists_eq_succ_of_ne_zero hr.ne'
  have htwo : a % 2 = b % 2 := h.of_dvd (show 2 ∣ 2 ^ j.succ by simp [pow_succ])
  exact htwo.trans hb

/-- Transfer the entire exact word to any ordinary source in its dyadic
cylinder, retaining r dyadic bits at the endpoint. -/
theorem OddWord.transport {w : List ℕ} {x z : ℕ} (hw : OddWord w x z)
    {r : ℕ} (hr : 0 < r) {a : ℕ} (ha : a ≡ x [MOD 2 ^ (w.sum + r)]) :
    ∃ b, OddWord w a b ∧ b ≡ z [MOD 2 ^ r] := by
  induction hw generalizing a with
  | nil x hx =>
    simp only [List.sum_nil, Nat.zero_add] at ha
    exact ⟨a, .nil a (oddOfClose hr hx ha), ha⟩
  | @cons e x y z es he hx hedge ht ih =>
    have hx' : a % 2 = 1 := oddOfClose (by omega : 0 < (e :: es).sum + r) hx ha
    have hfirst := (ha.mul_left 3).add_right 1
    rw [List.sum_cons, Nat.add_assoc, pow_add, ← hedge] at hfirst
    obtain ⟨y', hy', hclose⟩ := liftQuotient (pow_pos (by decide : 0 < 2) e) hfirst
    obtain ⟨z', hz', hlast⟩ := ih hclose
    exact ⟨z', .cons he hx' hy' hz', hlast⟩

#print axioms liftQuotient
#print axioms boundedSteering
#print axioms OddWord.oddSource
#print axioms OddWord.transport
end CollatzRound14.Adelic
