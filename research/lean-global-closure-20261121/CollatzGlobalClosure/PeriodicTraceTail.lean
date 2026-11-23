/-!
A dependency-free Lean 4 finite kernel for positive-period pressure traces.

The population consists of rational nonnegative weights and nonnegative
positive-representative offsets. The supplied total-mass identity remains an
explicit argument. No Collatz convergence or moment estimate is assumed.

The written note explains the monotone passage to an infinite ordinary tail
and the source-qualified substitution of PR144's exact rational populations.
-/

set_option maxRecDepth 2048

namespace CollatzGlobalClosure.PeriodicTraceTailCore

theorem div_le_div (a b c d : Rat) (hb : 0 < b) (hd : 0 < d)
    (h : a*d ≤ c*b) : a/b ≤ c/d := by
  have hbne := Rat.ne_of_gt hb
  have hdne := Rat.ne_of_gt hd
  apply Rat.le_of_mul_le_mul_right (c := b*d) ?_ (Rat.mul_pos hb hd)
  have hl : a / b * (b * d) = a * d := by
    rw [← Rat.mul_assoc, Rat.div_mul_cancel hbne]
  have hr : c / d * (b * d) = c * b := by
    rw [Rat.mul_comm b d, ← Rat.mul_assoc, Rat.div_mul_cancel hdne]
  rw [hl, hr]
  exact h

theorem reciprocal_square_telescope (k : Rat) (hk : 0 ≤ k) :
    1 / (k + 1)^2 ≤ 2 / (k + 1) - 2 / (k + 2) := by
  have h1 : 0 < k+1 := by grind
  have h2 : 0 < k+2 := by grind
  have h1ne := Rat.ne_of_gt h1
  have h2ne := Rat.ne_of_gt h2
  have heq : 2/(k+1)-2/(k+2) = 2/((k+1)*(k+2)) := by grind
  rw [heq]
  apply div_le_div _ _ _ _ (Rat.pow_pos h1) (Rat.mul_pos h1 h2)
  have hp : 0 ≤ k*(k+1) := Rat.mul_nonneg hk (Rat.le_of_lt h1)
  grind

theorem shifted_reciprocal_square_le (m o k : Rat) (hm : 0 < m)
    (ho : 0 ≤ o) (hk : 0 ≤ k) :
    1 / (o + 2*m*(k+1))^2 ≤
      (1/(2*m^2)) * (1/(k+1)-1/(k+2)) := by
  have hk1 : 0 < k+1 := by grind
  have hk2 : 0 < k+2 := by grind
  have hmne := Rat.ne_of_gt hm
  have hk1ne := Rat.ne_of_gt hk1
  have hk2ne := Rat.ne_of_gt hk2
  have hb : 0 < 2*m*(k+1) :=
    Rat.mul_pos (Rat.mul_pos (by decide) hm) hk1
  have hob : 0 < o+2*m*(k+1) := by grind
  have ho2 : 0 ≤ o^2 := Rat.pow_nonneg ho
  have hop : 0 ≤ o*(2*m*(k+1)) := Rat.mul_nonneg ho (Rat.le_of_lt hb)
  have hs : (2*m*(k+1))^2 ≤ (o+2*m*(k+1))^2 := by grind
  have hfirst : 1/(o+2*m*(k+1))^2 ≤ 1/(2*m*(k+1))^2 := by
    apply div_le_div _ _ _ _ (Rat.pow_pos hob) (Rat.pow_pos hb)
    simpa using hs
  have hden : 0 < 4*m^2 := Rat.mul_pos (by decide) (Rat.pow_pos hm)
  have hcoef : 0 ≤ 1/(4*m^2) := by
    simpa [Rat.div_def] using Rat.le_of_lt (Rat.inv_pos.mpr hden)
  have hsecond := Rat.mul_le_mul_of_nonneg_left
    (reciprocal_square_telescope k hk) hcoef
  have heq : 1/(2*m*(k+1))^2 = (1/(4*m^2))*(1/(k+1)^2) := by grind
  have heq2 : (1/(4*m^2))*(2/(k+1)-2/(k+2)) =
      (1/(2*m^2))*(1/(k+1)-1/(k+2)) := by grind
  rw [heq] at hfirst
  rw [heq2] at hsecond
  exact Rat.le_trans hfirst hsecond

def reciprocalTail (m o : Rat) : Nat → Rat
  | 0 => 0
  | K+1 => reciprocalTail m o K + 1/(o+2*m*((K : Rat)+1))^2

theorem reciprocalTail_le_telescope (m o : Rat) (hm : 0 < m)
    (ho : 0 ≤ o) (K : Nat) :
    reciprocalTail m o K ≤ (1/(2*m^2))*(1-1/((K : Rat)+1)) := by
  induction K with
  | zero => simp only [reciprocalTail]; grind
  | succ K ih =>
    have hterm := shifted_reciprocal_square_le m o (K : Rat) hm ho
      (Rat.natCast_nonneg)
    simp only [reciprocalTail, Rat.natCast_add]
    grind

theorem reciprocalTail_le (m o : Rat) (hm : 0 < m)
    (ho : 0 ≤ o) (K : Nat) : reciprocalTail m o K ≤ 1/(2*m^2) := by
  have h := reciprocalTail_le_telescope m o hm ho K
  have hden : 0 < 2*m^2 := Rat.mul_pos (by decide) (Rat.pow_pos hm)
  have hcoef : 0 ≤ 1/(2*m^2) := by
    simpa [Rat.div_def] using Rat.le_of_lt (Rat.inv_pos.mpr hden)
  have hk : 0 < (K : Rat)+1 := by have := Rat.natCast_nonneg (a := K); grind
  have hi : 0 ≤ 1/((K : Rat)+1) := by
    simpa [Rat.div_def] using Rat.le_of_lt (Rat.inv_pos.mpr hk)
  have hp := Rat.mul_nonneg hcoef hi
  grind

def weightedTail (m : Rat) (K : Nat) : List (Rat × Rat) → Rat
  | [] => 0
  | (z,o)::ps => z*reciprocalTail m o K + weightedTail m K ps

def mass : List (Rat × Rat) → Rat
  | [] => 0
  | (z,_)::ps => z + mass ps

theorem weightedTail_le (m : Rat) (hm : 0 < m) (K : Nat)
    (ps : List (Rat × Rat)) (h : ∀ p ∈ ps, 0 ≤ p.1 ∧ 0 ≤ p.2) :
    weightedTail m K ps ≤ mass ps / (2*m^2) := by
  induction ps with
  | nil => simp only [weightedTail, mass]; grind
  | cons p ps ih =>
    rcases p with ⟨z,o⟩
    have hz : 0 ≤ z := (h (z,o) (by simp)).1
    have ho : 0 ≤ o := (h (z,o) (by simp)).2
    have hrest : ∀ p ∈ ps, 0 ≤ p.1 ∧ 0 ≤ p.2 := by
      intro p hp
      exact h p (by simp [hp])
    have hih := ih hrest
    have ht := Rat.mul_le_mul_of_nonneg_left (reciprocalTail_le m o hm ho K) hz
    simp only [weightedTail, mass]
    grind

theorem collatz_period_tail_scale (q : Nat) :
    (27/5 : Rat)^q / (2*((3 : Rat)^q)^2) = (1/2 : Rat)*(3/5 : Rat)^q := by
  induction q with
  | zero => grind
  | succ q ih =>
    have hp : 0 < (3 : Rat)^q := Rat.pow_pos (by decide)
    have hn := Rat.ne_of_gt hp
    simp only [Rat.pow_succ] at *
    grind

theorem collatz_fourth_tail_bound (q K : Nat) (ps : List (Rat × Rat))
    (h : ∀ p ∈ ps, 0 ≤ p.1 ∧ 0 ≤ p.2)
    (hmass : mass ps = (27/5 : Rat)^q) :
    weightedTail ((3 : Rat)^q) K ps ≤ (1/2 : Rat)*(3/5 : Rat)^q := by
  have hp : 0 < (3 : Rat)^q := Rat.pow_pos (by decide)
  have htail := weightedTail_le ((3 : Rat)^q) hp K ps h
  rw [hmass, collatz_period_tail_scale] at htail
  exact htail

def highHead (m : Rat) : List (Rat × Rat) → Rat
  | [] => 0
  | (z,o)::ps => (if m ≤ o then z/o^2 else 0) + highHead m ps

theorem highHead_le (m : Rat) (hm : 0 < m) (ps : List (Rat × Rat))
    (h : ∀ p ∈ ps, 0 ≤ p.1 ∧ 0 ≤ p.2) : highHead m ps ≤ mass ps / m^2 := by
  induction ps with
  | nil => simp only [highHead, mass]; grind
  | cons p ps ih =>
    rcases p with ⟨z,o⟩
    have hz : 0 ≤ z := (h (z,o) (by simp)).1
    have ho : 0 ≤ o := (h (z,o) (by simp)).2
    have hrest : ∀ p ∈ ps, 0 ≤ p.1 ∧ 0 ≤ p.2 := by
      intro p hp
      exact h p (by simp [hp])
    have hih := ih hrest
    have hterm : (if m ≤ o then z/o^2 else 0) ≤ z/m^2 := by
      split
      next hmo =>
        have hop : 0 < o := by grind
        have hminus : 0 ≤ o-m := by grind
        have hplus : 0 ≤ o+m := by grind
        have hprod := Rat.mul_nonneg hminus hplus
        have hsq : m^2 ≤ o^2 := by grind
        have hmul := Rat.mul_le_mul_of_nonneg_left hsq hz
        exact div_le_div _ _ _ _ (Rat.pow_pos hop) (Rat.pow_pos hm) hmul
      next _ =>
        have hinv : 0 ≤ (m^2)⁻¹ := Rat.le_of_lt (Rat.inv_pos.mpr (Rat.pow_pos hm))
        simpa [Rat.div_def] using Rat.mul_nonneg hz hinv
    simp only [highHead, mass]
    grind

theorem highHead_add_tail_le (m : Rat) (hm : 0 < m) (K : Nat)
    (ps : List (Rat × Rat)) (h : ∀ p ∈ ps, 0 ≤ p.1 ∧ 0 ≤ p.2) :
    highHead m ps + weightedTail m K ps ≤ 3*(mass ps/(2*m^2)) := by
  have hhead := highHead_le m hm ps h
  have htail := weightedTail_le m hm K ps h
  have hn := Rat.ne_of_gt hm
  have heq : mass ps / m^2 = 2*(mass ps/(2*m^2)) := by grind
  rw [heq] at hhead
  grind

theorem collatz_half_period_tail_bound (q K : Nat) (ps : List (Rat × Rat))
    (h : ∀ p ∈ ps, 0 ≤ p.1 ∧ 0 ≤ p.2)
    (hmass : mass ps = (27/5 : Rat)^q) :
    highHead ((3 : Rat)^q) ps + weightedTail ((3 : Rat)^q) K ps ≤
      (3/2 : Rat)*(3/5 : Rat)^q := by
  have hp : 0 < (3 : Rat)^q := Rat.pow_pos (by decide)
  have hb := highHead_add_tail_le ((3 : Rat)^q) hp K ps h
  rw [hmass, collatz_period_tail_scale] at hb
  grind

#print axioms reciprocal_square_telescope
#print axioms weightedTail_le
#print axioms collatz_period_tail_scale
#print axioms collatz_fourth_tail_bound
#print axioms collatz_half_period_tail_bound

end CollatzGlobalClosure.PeriodicTraceTailCore
