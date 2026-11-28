import FiniteExtinction
import AsynchronousGuard

/-! A near-hit extinction clock. The elementary exact inequality
2^19 < 3^12 bounds the number of odd departures before an actual hit at 1.
No bound on when that hit occurs is supplied here. -/
set_option autoImplicit false
set_option warningAsError true

namespace HitClock
open CoreBranching PeakRigidity BinaryPrefixCriterion BinaryCylinder BirthReserve
open FiniteExtinction

def exitClock (h : ℕ) : ℕ := h+2*(h/38+1)

theorem exitClock_mono {h H : ℕ} (le : h≤H) : exitClock h≤exitClock H := by
  have hd : h/38≤H/38 := Nat.div_le_div_right le
  unfold exitClock
  omega

/-- A real positive source that reaches one cannot have an arbitrary grade. -/
theorem hit_grade (x h : ℕ) (positive : 0<x) (hit : run h x=1) :
    19*grade h x≤12*h := by
  have affine := AsynchronousGuard.affine h x
  rw [hit,mul_one] at affine
  have mult : 3^(grade h x)≤3^(grade h x)*x :=
    Nat.le_mul_of_pos_right _ positive
  have leading : 3^(grade h x)≤2^h := by omega
  have low : (2:ℕ)^(19*grade h x)≤3^(12*grade h x) := by
    rw [pow_mul,pow_mul]
    exact Nat.pow_le_pow_left (by decide : (2:ℕ)^19≤3^12) _
  have high : (3:ℕ)^(12*grade h x)≤2^(12*h) := by
    rw [Nat.mul_comm 12 (grade h x),Nat.mul_comm 12 h,pow_mul,pow_mul]
    exact Nat.pow_le_pow_left leading 12
  exact (Nat.pow_le_pow_iff_right (by decide : 1<(2:ℕ))).mp (low.trans high)

/-- The gate has failed by h + 2 floor(h/38) + 2 after a supplied hit h. -/
theorem gate_fails (x h : ℕ) (positive : 0<x) (hit : run h x=1) :
    ¬Gate (exitClock h) x := by
  intro gate
  have last := gate (exitClock h) (Finset.mem_range.mpr (by omega))
  unfold exitClock at last
  rw [grade_add,hit,grade_one_even] at last
  have bound := hit_grade x h positive hit
  omega

/-- A sharper version of the original finite verification transfer.
Only a finite supplied hit budget is assumed; the later population is global. -/
theorem finite_transfer (M H N : ℕ)
    (verified : ∀ x : ℕ, 0<x → x<2^M → ∃ h, h≤H ∧ run h x=1)
    (depth : M≤N) (late : exitClock H≤N) :
    mass N+reserve N≤reserve M := by
  have eq : mass N=tail M N := by
    rw [mass_active]
    unfold tail activeSum
    apply Finset.sum_congr rfl
    intro x _
    by_cases hg : Gate N x
    · simp only [hg,ite_true]
      by_cases hx : x=0
      · simp [hx,tailWeight]
      · have high : 2^M≤x := by
          by_contra hlow
          obtain ⟨h,hh,hit⟩ := verified x (Nat.pos_of_ne_zero hx) (by omega)
          exact gate_fails x h (Nat.pos_of_ne_zero hx) hit
            (gate_mono hg ((exitClock_mono hh).trans late))
        simp [tailWeight,high]
    · simp [hg]
  rw [eq]
  have h := tail_with_reserve M (N-M)
  simpa [Nat.add_sub_of_le depth] using h

theorem finite_transfer_eighth (k H N : ℕ)
    (verified : ∀ x : ℕ, 0<x → x<2^(8*k) → ∃ h, h≤H ∧ run h x=1)
    (depth : 8*k≤N) (late : exitClock H≤N) :
    mass N+reserve N≤(24*(k:ℚ)+5)*(6561/8192:ℚ)^k :=
  (finite_transfer (8*k) H N verified depth late).trans (reserve_eighth k)

#print axioms hit_grade
#print axioms gate_fails
#print axioms finite_transfer
#print axioms finite_transfer_eighth
end HitClock
