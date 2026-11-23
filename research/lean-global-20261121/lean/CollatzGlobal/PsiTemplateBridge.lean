import CollatzGlobal.PsiNormalization
import CollatzGlobal.UnboundedLadder

/-!
Fixed-clock conjugation of binary reverse witness transformations into the
psi goal type. The supplied old transformation is an explicit hypothesis;
no unformalized negative-reference template is declared as an axiom here.
-/

open CollatzReverseBasin CollatzClosure

namespace CollatzGlobal

theorem binary_upper_psi_prefix (M : Nat) :
    orbit (128*M+1) 7 = 3*(27*M+1)-1 := by
  have h := (four_ladder (2*M) 3).1
  change orbit (64*(2*M)+1) 6 = 27*(2*M)+1 at h
  have ein : 64*(2*M)+1=128*M+1 := by omega
  have eout : 27*(2*M)+1=54*M+1 := by omega
  rw [ein, eout] at h
  have hs : shortcut (54*M+1)=81*M+2 := by
    unfold shortcut
    split <;> omega
  change orbit (128*M+1) (6+1)=3*(27*M+1)-1
  rw [orbit_add, h]
  simp only [orbit, hs]
  omega

theorem binary_lower_psi_prefix (M : Nat) :
    orbit (64*M+1) 6 = 27*M+1 := by
  exact (four_ladder M 3).1

/-- Exact conjugation of an arbitrary supplied source-clock transformation.
The fixed seven-step overhead cancels, so the source-clock increment remains a. -/
theorem conjugate_binary_source_clock (M M' a : Nat)
    (sourceRule : ∀ d : Nat, orbit (128*M+1) d=1 →
      orbit (128*M'+1) (d+a)=1)
    {d : Nat} (h : orbit (3*(27*M+1)-1) d=1) :
    orbit (3*(27*M'+1)-1) (d+a)=1 := by
  have old : orbit (128*M+1) (7+d)=1 := by
    rw [orbit_add, binary_upper_psi_prefix]
    exact h
  have new := sourceRule (7+d) old
  have e : (7+d)+a=7+(d+a) := by omega
  rw [e, orbit_add, binary_upper_psi_prefix] at new
  exact new

/-- Target certificates pass through the actual six-step ordinary prefixes.
This connects the same psi target relation on both sides of the transformation. -/
theorem conjugate_binary_target (M M' : Nat)
    (targetRule : Basin (64*M'+1) → Basin (64*M+1)) :
    Basin (27*M'+1) → Basin (27*M+1) := by
  intro h
  have old : Basin (64*M'+1) := by
    apply (orbit_basin (64*M'+1) 6).mp
    rw [binary_lower_psi_prefix]
    exact h
  have new := targetRule old
  have out := (orbit_basin (64*M+1) 6).mpr new
  rwa [binary_lower_psi_prefix] at out

end CollatzGlobal
