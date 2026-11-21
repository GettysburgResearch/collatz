import CollatzGlobal.AdaptiveDescent

/-!
A total finite normalizer whose residual closing statement is equivalent to
the full ordinary Collatz conjecture. The equivalence uses the imported,
kernel-checked PR174 reverse criterion. The residual closing statement is
an explicit unproved hypothesis, never an axiom.
-/

open CollatzReverseBasin CollatzClosure

namespace CollatzGlobal

theorem shortcut_positive {n : Nat} (hn : 0 < n) : 0 < shortcut n := by
  unfold shortcut
  split <;> omega

theorem orbit_positive {n : Nat} (hn : 0 < n) (t : Nat) : 0 < orbit n t := by
  induction t generalizing n with
  | zero => exact hn
  | succ t ih => exact ih (shortcut_positive hn)

theorem shortcut_unit {n : Nat} (hn : n % 3 ≠ 0) : (shortcut n) % 3 ≠ 0 := by
  unfold shortcut
  split <;> omega

theorem orbit_unit {n : Nat} (hn : n % 3 ≠ 0) (t : Nat) :
    (orbit n t) % 3 ≠ 0 := by
  induction t generalizing n with
  | zero => exact hn
  | succ t ih => exact ih (shortcut_unit hn)

/-- Return of the actual ordinary pair `(3m-1,m)` to the same relation.
No equality of odd counts is required for this pointwise finite algorithm. -/
def PsiReturn (m t : Nat) : Prop :=
  orbit (3*m-1) t = 3*orbit m t-1

instance (m t : Nat) : Decidable (PsiReturn m t) :=
  inferInstanceAs (Decidable (orbit (3*m-1) t = 3*orbit m t-1))

theorem psi_return_zero (m : Nat) : PsiReturn m 0 := rfl

theorem psi_return_append {m s t : Nat} (hs : PsiReturn m s)
    (ht : PsiReturn (orbit m s) t) : PsiReturn m (s+t) := by
  unfold PsiReturn at hs ht ⊢
  rw [orbit_add, orbit_add, hs]
  exact ht

def lastPsiReturn (m : Nat) : Nat → Nat
  | 0 => 0
  | d+1 => if PsiReturn m (d+1) then d+1 else lastPsiReturn m d

theorem lastPsiReturn_le (m d : Nat) : lastPsiReturn m d ≤ d := by
  induction d with
  | zero => exact Nat.le_refl 0
  | succ d ih => unfold lastPsiReturn; split <;> omega

theorem lastPsiReturn_returns (m d : Nat) : PsiReturn m (lastPsiReturn m d) := by
  induction d with
  | zero => exact psi_return_zero m
  | succ d ih =>
    unfold lastPsiReturn
    split
    · assumption
    · exact ih

theorem lastPsiReturn_maximal (m d t : Nat) (ht : t ≤ d)
    (hr : PsiReturn m t) : t ≤ lastPsiReturn m d := by
  induction d with
  | zero => exact ht
  | succ d ih =>
    unfold lastPsiReturn
    split
    · exact ht
    · by_cases hle : t ≤ d
      · exact ih hle
      · have e : t = d+1 := by omega
        subst t
        contradiction

def FinitePsiResidual (m d : Nat) : Prop :=
  ∀ t : Nat, 0 < t → t ≤ d → ¬ PsiReturn m t

def psiResidual (m d : Nat) : Nat := orbit m (lastPsiReturn m d)
def psiResidualClock (m d : Nat) : Nat := d-lastPsiReturn m d

theorem psi_residual_positive {m : Nat} (hm : 0 < m) (d : Nat) :
    0 < psiResidual m d := orbit_positive hm _

theorem psi_residual_hits {m d : Nat} (h : orbit (3*m-1) d = 1) :
    orbit (3*psiResidual m d-1) (psiResidualClock m d) = 1 := by
  unfold psiResidual psiResidualClock
  have hr := lastPsiReturn_returns m d
  unfold PsiReturn at hr
  rw [← hr, ← orbit_add]
  have e : lastPsiReturn m d + (d-lastPsiReturn m d)=d := by
    have := lastPsiReturn_le m d
    omega
  rwa [e]

theorem psi_residual_is_finite (m d : Nat) :
    FinitePsiResidual (psiResidual m d) (psiResidualClock m d) := by
  intro t ht hle hr
  have all := psi_return_append (lastPsiReturn_returns m d) hr
  have bound : lastPsiReturn m d+t ≤ d := by
    have := lastPsiReturn_le m d
    unfold psiResidualClock at hle
    omega
  have max := lastPsiReturn_maximal m d (lastPsiReturn m d+t) bound all
  omega

theorem psi_residual_basin (m d : Nat) : Basin m ↔ Basin (psiResidual m d) :=
  (orbit_basin m (lastPsiReturn m d)).symm

/-- Exact ordinary target certificate transport out of the finite residual. -/
theorem compile_psi_residual_clock {m d a : Nat}
    (h : orbit (psiResidual m d) a = 1) :
    orbit m (lastPsiReturn m d+a) = 1 := by
  rw [orbit_add]
  exact h

/-- A source hit cannot itself be a return: `1=3r-1` has no positive
ordinary integer solution. In particular the residual source clock is positive. -/
theorem lastPsiReturn_before_hit {m d : Nat} (hm : 0 < m)
    (hit : orbit (3*m-1) d = 1) : lastPsiReturn m d < d := by
  have le := lastPsiReturn_le m d
  by_cases hlt : lastPsiReturn m d < d
  · exact hlt
  · have eq : lastPsiReturn m d = d := by omega
    have hr := lastPsiReturn_returns m d
    rw [eq] at hr
    unfold PsiReturn at hr
    rw [hit] at hr
    have hp := orbit_positive hm d
    omega

/-- The one residual closing obligation for this executable normalizer. -/
def ResidualPsiClosure : Prop :=
  ∀ m d : Nat, 0 < m → m % 3 ≠ 0 → orbit (3*m-1) d = 1 →
    FinitePsiResidual m d → Basin m

/-- Exact global equivalence. The nontrivial global reverse-binary criterion
is imported from the separately attributed PR146/PR174 core development.
No instance of `ResidualPsiClosure` is asserted or assumed as an axiom. -/
theorem collatz_iff_finite_psi_residual :
    (∀ n : Nat, 0 < n → Basin n) ↔ ResidualPsiClosure := by
  constructor
  · intro all m d hm _ _ _
    exact all m hm
  · intro residual
    apply collatz_of_open_lemma
    intro k _ upper
    obtain ⟨d, hd⟩ := upper
    have hit := (hits_iff_orbit (3*(27*k+1)-1) d).mp hd
    have small := residual (psiResidual (27*k+1) d)
      (psiResidualClock (27*k+1) d)
      (psi_residual_positive (by omega) d)
      (orbit_unit (by omega) (lastPsiReturn (27*k+1) d))
      (psi_residual_hits hit)
      (psi_residual_is_finite (27*k+1) d)
    exact (psi_residual_basin (27*k+1) d).mpr small

/-- A residual still present in the first source-certificate layer. -/
theorem psi_first_layer_residual :
    orbit (3*11-1) 5 = 1 ∧ FinitePsiResidual 11 5 := by
  constructor
  · decide
  · intro t ht hle
    have e : t=1 ∨ t=2 ∨ t=3 ∨ t=4 ∨ t=5 := by omega
    rcases e with e | e | e | e | e <;> subst t <;> decide

/-- In the entire power-of-two source layer, the equivalent power of three
is strictly smaller than the unknown target. No exponent bound is used. -/
theorem jacobsthal_three_power_smaller (i m : Nat)
    (h : 3*m = 2*4^(i+1)+1) : 3^i < m := by
  have hp : 3^i ≤ 4^i := Nat.pow_le_pow_left (by omega) i
  have hpos : 0 < 4^i := Nat.pow_pos (by omega)
  rw [Nat.pow_succ] at h
  omega

/-- The whole source-rank-zero layer is discharged under an ordinary
least-counterexample floor, by the credited PR174 Jacobsthal equivalence.
This floor is an explicit hypothesis; source-clock minimality does not imply it. -/
theorem jacobsthal_closed_under_ordinary_floor (i m : Nat)
    (h : 3*m = 2*4^(i+1)+1)
    (floor : ∀ a : Nat, a < m → 0 < a → Basin a) : Basin m := by
  apply (basin_jacobsthal i m h).mpr
  exact floor (3^i) (jacobsthal_three_power_smaller i m h) (Nat.pow_pos (by omega))

end CollatzGlobal
