/-
Unbounded ordinary inverse ladders for the half-budget attack.
The transfer is guarded by an actual smaller-source budget certificate;
no universal cover or global convergence is asserted.
-/
import Collatz.BudgetTransfer

open CollatzReverseBasin CollatzHalfCrossing CollatzBudgetTransfer

namespace CollatzTernaryLadder

/-- Every input in a run of `s` odd-only shortcut steps is odd. -/
theorem ones_block (s v : Nat) (hv : 0<v) :
    (run (2^s*v-1) s).value = 3^s*v-1 ∧
    (run (2^s*v-1) s).odds = s := by
  induction s generalizing v with
  | zero => simp [run, start]
  | succ s ih =>
    have ih' := ih (2*v) (by omega)
    have en : 2^(s+1)*v-1 = 2^s*(2*v)-1 := by rw [Nat.pow_succ]; grind
    rw [en]
    have hp : 0 < 3^s*v := Nat.mul_pos (Nat.pow_pos (by decide)) hv
    have hodd : (3^s*(2*v)-1)%2 ≠ 0 := by
      have e : 3^s*(2*v) = 2*(3^s*v) := by grind
      rw [e]; omega
    change (advance (run (2^s*(2*v)-1) s)).value = 3^(s+1)*v-1 ∧
      (advance (run (2^s*(2*v)-1) s)).odds = s+1
    rw [advance_value, advance_odds, ih'.1, ih'.2]
    simp only [hodd, ↓reduceIte]
    constructor
    · unfold shortcut
      rw [ite_eq_right hodd, Nat.pow_succ]
      have e : 3^s*(2*v)=2*(3^s*v) := by grind
      have e' : 3^s*3*v=3*(3^s*v) := by grind
      rw [e, e']
      omega
    · trivial

/-- A valuation-two step consists of an odd shortcut and a halving. -/
theorem twos_one (u : Nat) :
    (run (4*u+1) 2).value = 3*u+1 ∧
    (run (4*u+1) 2).odds = 1 := by
  have hp : (4*u+1)%2 ≠ 0 := by omega
  have h1 : shortcut (4*u+1)=6*u+2 := by unfold shortcut; rw [ite_eq_right hp]; omega
  have h2 : shortcut (6*u+2)=3*u+1 := by unfold shortcut; rw [ite_eq_left (by omega)]; omega
  simp only [run, start, advance, hp, ↓reduceIte, h1]
  simp only [show (6*u+2)%2=0 by omega, ↓reduceIte, h2]
  trivial

/-- A whole unbounded valuation-two block, with exact clock and odd count. -/
theorem twos_block (r u : Nat) :
    (run (4^r*u+1) (2*r)).value = 3^r*u+1 ∧
    (run (4^r*u+1) (2*r)).odds = r := by
  induction r generalizing u with
  | zero => simp [run, start]
  | succ r ih =>
    have en : 4^(r+1)*u+1 = 4*(4^r*u)+1 := by rw [Nat.pow_succ]; grind
    have hfirst := twos_one (4^r*u)
    have hn : 3*(4^r*u)+1 = 4^r*(3*u)+1 := by grind
    have hrest := ih (3*u)
    have hcomp := run_add_value_odds (4*(4^r*u)+1) 2 (2*r)
    rw [hfirst.1, hn, hrest.1, hrest.2, hfirst.2] at hcomp
    rw [en]
    have ht : 2*(r+1)=2+2*r := by omega
    rw [ht]
    constructor
    · rw [hcomp.1, Nat.pow_succ]; grind
    · omega

/-- The complete ladder is a legal ordinary path, not a symbolic inverse word. -/
theorem ladder_path (r s u v : Nat) (hv : 0<v)
    (hlink : 3^s*v = 4^r*u+2) :
    (run (2^s*v-1) (s+2*r)).value = 3^r*u+1 ∧
    (run (2^s*v-1) (s+2*r)).odds = s+r := by
  have h1 := ones_block s v hv
  have h2 := twos_block r u
  have hcomp := run_add_value_odds (2^s*v-1) s (2*r)
  have hmid : 3^s*v-1=4^r*u+1 := by omega
  rw [h1.1, hmid, h2.1, h2.2, h1.2] at hcomp
  exact hcomp

theorem ones_prefix_odds (s v j : Nat) (hv : 0<v) (hj : j≤s) :
    (run (2^s*v-1) j).odds = j := by
  have en : 2^s*v-1 = 2^j*(2^(s-j)*v)-1 := by
    rw [← Nat.mul_assoc, ← Nat.pow_add, Nat.add_sub_of_le hj]
  rw [en]
  exact (ones_block j (2^(s-j)*v) (Nat.mul_pos (Nat.pow_pos (by decide)) hv)).2

/-- Every partial valuation-two block has the expected rounded odd count. -/
theorem twos_prefix_odds (r u j : Nat) (hj : j≤2*r) :
    (run (4^r*u+1) j).odds = (j+1)/2 := by
  let h := j/2
  have hh : h≤r := by dsimp [h]; omega
  have en : 4^r*u+1 = 4^h*(4^(r-h)*u)+1 := by
    rw [← Nat.mul_assoc, ← Nat.pow_add, Nat.add_sub_of_le hh]
  have hb := twos_block h (4^(r-h)*u)
  rw [← en] at hb
  by_cases he : j%2=0
  · have ej : j=2*h := by dsimp [h]; omega
    rw [ej, hb.2]
    omega
  · have ej : j=2*h+1 := by dsimp [h]; omega
    have hhr : h<r := by omega
    have ef : 4^(r-h)*u = 4*(4^(r-h-1)*u) := by
      have ee : r-h=(r-h-1)+1 := by omega
      rw [ee, Nat.pow_succ]
      grind
    have hp : (3^h*(4^(r-h)*u)+1)%2 ≠ 0 := by
      rw [ef]
      have eq : 3^h*(4*(4^(r-h-1)*u)) = 4*(3^h*(4^(r-h-1)*u)) := by grind
      rw [eq]; omega
    rw [ej]
    change (advance (run (4^r*u+1) (2*h))).odds = (2*h+1+1)/2
    rw [advance_odds, hb.1, hb.2]
    simp only [hp, ↓reduceIte]
    omega

/-- An expanding endpoint bounds every earlier even prefix of the second block. -/
theorem geometric_prefix (s r h : Nat) (hh : h≤r)
    (hfinal : 2^(s+2*r) ≤ 3^(s+r)) :
    2^(s+2*h) ≤ 3^(s+h) := by
  have eD : 2^(s+2*r) = 2^(s+2*h)*4^(r-h) := by
    change 2^(s+2*r) = 2^(s+2*h)*(2^2)^(r-h)
    rw [← Nat.pow_mul, ← Nat.pow_add]
    congr 1
    omega
  have eA : 3^(s+r) = 3^(s+h)*3^(r-h) := by
    rw [← Nat.pow_add]
    congr 1
    omega
  rw [eD, eA] at hfinal
  have hp := Nat.pow_le_pow_left (show 3≤4 by decide) (r-h)
  have hc : 2^(s+2*h)*3^(r-h) ≤ 3^(s+h)*3^(r-h) :=
    Nat.le_trans (Nat.mul_le_mul_left _ hp) hfinal
  exact Nat.le_of_mul_le_mul_right hc (Nat.pow_pos (by decide))

/-- All ladder prefixes have coefficient at least one, not merely one half. -/
theorem ladder_prefix_expands (r s u v j : Nat) (hv : 0<v)
    (hlink : 3^s*v=4^r*u+2)
    (hexpand : 2^(s+2*r) ≤ 3^(s+r)) (hj : j≤s+2*r) :
    (run (2^s*v-1) j).den ≤ (run (2^s*v-1) j).mul := by
  rw [run_den, run_mul]
  by_cases hjs : j≤s
  · rw [ones_prefix_odds s v j hv hjs]
    exact Nat.pow_le_pow_left (by decide) j
  · have hk : j-s≤2*r := by omega
    have hone := ones_block s v hv
    have hmid : 3^s*v-1=4^r*u+1 := by omega
    have hc := (run_add_value_odds (2^s*v-1) s (j-s)).2
    rw [hone.1, hmid, hone.2, twos_prefix_odds r u (j-s) hk] at hc
    have ej : s+(j-s)=j := by omega
    rw [ej] at hc
    rw [hc]
    let h := (j-s)/2
    have hh : h≤r := by dsimp [h]; omega
    have hg := geometric_prefix s r h hh hexpand
    by_cases he : (j-s)%2=0
    · have ej2 : j=s+2*h := by dsimp [h]; omega
      have eo : (j-s+1)/2=h := by dsimp [h]; omega
      rw [eo, ej2]
      exact hg
    · have ej2 : j=s+2*h+1 := by dsimp [h]; omega
      have eo : (j-s+1)/2=h+1 := by dsimp [h]; omega
      rw [eo, ej2, show s+(h+1)=(s+h)+1 by omega, Nat.pow_succ, Nat.pow_succ]
      have hm := Nat.mul_le_mul_right 2 hg
      have hp : 2*3^(s+h)≤3*3^(s+h) := by omega
      omega

/-- Strict endpoint expansion makes this an actual smaller-ancestor rule. -/
theorem ladder_smaller (r s u v : Nat) (hv : 0<v)
    (hlink : 3^s*v=4^r*u+2)
    (hexpand : 2^(s+2*r) < 3^(s+r)) :
    2^s*v-1 < 3^r*u+1 := by
  have hp := ladder_path r s u v hv hlink
  have hid := run_identity (2^s*v-1) (s+2*r)
  rw [hp.1, run_mul, hp.2, run_den] at hid
  apply Classical.byContradiction
  intro hn
  have hg : 3^r*u+1 ≤ 2^s*v-1 := by omega
  have h1 := Nat.mul_lt_mul_of_pos_right hexpand (show 0<3^r*u+1 by omega)
  have h2 := Nat.mul_le_mul_left (3^(s+r)) hg
  omega

/-- The whole unbounded ladder transports a supplied smaller-source budget. -/
theorem budget_ladder (r s u v : Nat) (hv : 0<v)
    (hlink : 3^s*v=4^r*u+2)
    (hexpand : 2^(s+2*r) < 3^(s+r))
    (hx : BudgetAt (2^s*v-1)) : BudgetAt (3^r*u+1) := by
  have hp := ladder_path r s u v hv hlink
  apply budget_inverse_smaller (2^s*v-1) (3^r*u+1) (s+2*r) hp.1
  · intro j hj
    have hh := ladder_prefix_expands r s u v j hv hlink (by omega) (by omega)
    omega
  · rw [run_den, run_mul, hp.2]
    omega
  · exact ladder_smaller r s u v hv hlink hexpand
  · exact hx

private theorem run_zero_value (t : Nat) : (run 0 t).value=0 := by
  induction t with
  | zero => rfl
  | succ t ih =>
    change (advance (run 0 t)).value=0
    rw [advance_value, ih]
    rfl

/-- The algebraic ladder guard itself guarantees a positive ordinary source. -/
theorem ladder_source_pos (r s u v : Nat) (hv : 0<v)
    (hlink : 3^s*v=4^r*u+2) : 0<2^s*v-1 := by
  have hp := (ladder_path r s u v hv hlink).1
  by_cases hx : 2^s*v-1=0
  · rw [hx, run_zero_value] at hp
    omega
  · omega

/-- Every positive ternary depth ends at a ternary unit. -/
theorem ladder_target_unit (r u : Nat) (hr : 0<r) : (3^r*u+1)%3 ≠ 0 := by
  have he : 3^r*u+1 = 3*(3^(r-1)*u)+1 := by
    have er : r=(r-1)+1 := by omega
    rw [er, Nat.pow_succ]
    grind
  rw [he]
  omega

/-- The unit-restricted induction rule keeps the source unit condition explicit.
It is not automatic from the ladder equations. -/
theorem budget_ladder_unit_induction (r s u v : Nat) (hv : 0<v)
    (hlink : 3^s*v=4^r*u+2)
    (hexpand : 2^(s+2*r) < 3^(s+r))
    (hxunit : (2^s*v-1)%3 ≠ 0)
    (smaller : ∀ x : Nat, 0<x → x<3^r*u+1 → x%3≠0 → BudgetAt x) :
    BudgetAt (3^r*u+1) := by
  apply budget_ladder r s u v hv hlink hexpand
  exact smaller _ (ladder_source_pos r s u v hv hlink)
    (ladder_smaller r s u v hv hlink hexpand) hxunit

/-- Spending the first odd step gives an unconditional ternary-unit source.
The stronger expansion margin pays for that step exactly. -/
theorem budget_ladder_unit_entrance (r s u v : Nat) (hs : 0<s) (hv : 0<v)
    (hlink : 3^s*v=4^r*u+2)
    (hexpand : 3*2^(s+2*r) < 2*3^(s+r))
    (smaller : ∀ x : Nat, 0<x → x<3^r*u+1 → x%3≠0 → BudgetAt x) :
    BudgetAt (3^r*u+1) := by
  have hlink' : 3^(s-1)*(3*v)=4^r*u+2 := by
    have es : s=(s-1)+1 := by omega
    rw [es, Nat.pow_succ] at hlink
    have ee : 3^(s-1)*3*v=3^(s-1)*(3*v) := by grind
    rwa [ee] at hlink
  have hpow2 : 2^(s+2*r)=2*2^((s-1)+2*r) := by
    have ee : s+2*r=((s-1)+2*r)+1 := by omega
    rw [ee, Nat.pow_succ]
    omega
  have hpow3 : 3^(s+r)=3*3^((s-1)+r) := by
    have ee : s+r=((s-1)+r)+1 := by omega
    rw [ee, Nat.pow_succ]
    omega
  have hexpand' : 2^((s-1)+2*r)<3^((s-1)+r) := by
    rw [hpow2, hpow3] at hexpand
    omega
  have hp : 0<2^(s-1)*v := Nat.mul_pos (Nat.pow_pos (by decide)) hv
  have hunit : (2^(s-1)*(3*v)-1)%3≠0 := by
    have ee : 2^(s-1)*(3*v)=3*(2^(s-1)*v) := by grind
    rw [ee]
    omega
  exact budget_ladder_unit_induction r (s-1) u (3*v) (by omega)
    hlink' hexpand' hunit smaller

end CollatzTernaryLadder
