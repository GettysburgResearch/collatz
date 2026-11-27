module

public import PassageGatePrefix
import all PassageGatePrefix
import all PassageGatePacking
import all HourTower
import Mathlib.Tactic

public section
namespace Collatz.Itinerary.PassageGate

open HourTower Finset
set_option autoImplicit false

/-- A hit of a prescribed positive integer before the physical packet
clock sharply bounds that packet's native odd count. -/
theorem early_hit_count {x m D h t : ℕ} (size : 2^h≤D*x)
    (early : t≤h) (hit : run t x=m) :
    count h x ≤ Nat.log 2 (D*m)+Nat.log 3 (D*m) := by
  obtain ⟨carry,eqn,_⟩ := HourTower.carry t x
  rw [hit] at eqn
  have gr : 3^(count t x)*x≤2^t*m := by omega
  have both : 2^(h-t)*3^(count t x)≤D*m := by
    apply Nat.le_of_mul_le_mul_left (c:=2^t) _ (Nat.two_pow_pos _)
    calc
      2^t*(2^(h-t)*3^(count t x))=2^h*3^(count t x) := by
        rw [←mul_assoc,←pow_add,Nat.add_sub_of_le early]
      _ ≤ D*x*3^(count t x) := Nat.mul_le_mul_right _ size
      _ = D*(3^(count t x)*x) := by ac_rfl
      _ ≤ D*(2^t*m) := Nat.mul_le_mul_left D gr
      _ = 2^t*(D*m) := by ac_rfl
  have high := Nat.le_log_of_pow_le (by decide : 1<2)
    ((Nat.le_mul_of_pos_right _ (Nat.pow_pos (by decide : 0<3))).trans both)
  have low := Nat.le_log_of_pow_le (by decide : 1<3)
    ((Nat.le_mul_of_pos_left _ (Nat.two_pow_pos _)).trans both)
  have split := append_count t (h-t) x
  rw [Nat.add_sub_of_le early] at split
  have cap := count_le (h-t) (run t x)
  omega

def visits (x m : ℕ) : Prop := ∃ t, run t x=m

theorem late_ancestor {x m D h : ℕ} (size : 2^h≤D*x)
    (grade : Nat.log 2 (D*m)+Nat.log 3 (D*m)<count h x) (hit : visits x m) :
    visits (run h x) m := by
  obtain ⟨t,eqn⟩ := hit
  have after : h<t := by
    by_contra! before
    exact (Nat.not_lt_of_ge (early_hit_count size before eqn)) grade
  refine ⟨t-h,?_⟩
  rwa [←run_add,Nat.add_sub_of_le after.le]

/-- Every sufficiently large family of high-odd-count ancestors of a
fixed target in a dyadic packet contains a large common exact-clock
fiber ending at a genuine ancestor of that target. -/
theorem synchronized_ancestor {S : Finset ℕ} {m h D U B : ℕ}
    (screen : ∀ x∈S, 0<x ∧ x≤2^h ∧ 2^h≤D*x ∧
      Nat.log 2 (D*m)+Nat.log 3 (D*m)<count h x ∧ count h x≤U ∧ visits x m)
    (many : 3^U*B<S.card) :
    ∃ y, 0<y ∧ y≤3^U ∧ visits y m ∧ B<(S.filter (fun x => run h x=y)).card := by
  classical
  let dst := Icc 1 (3^U)
  have maps : (S:Set ℕ).MapsTo (run h) dst := by
    intro x hx
    obtain ⟨xp,size,_,_,cap,_⟩ := screen x hx
    have top : run h x≤3^(count h x) := by
      simpa using HourTower.upper (t:=1) (by simpa using size)
    exact mem_Icc.mpr ⟨positive_run _ _ xp,top.trans (Nat.pow_le_pow_right (by decide) cap)⟩
  by_contra! fail
  have every (y : ℕ) (hy : y∈dst) : (S.filter (fun x => run h x=y)).card≤B := by
    by_cases none : (S.filter (fun x => run h x=y))=∅
    · simp [none]
    · obtain ⟨x,hx⟩ := Finset.nonempty_iff_ne_empty.mpr none
      obtain ⟨old,eqn⟩ := mem_filter.mp hx
      obtain ⟨_,_,lower,grade,_,ancestor⟩ := screen x old
      have vy := late_ancestor lower grade ancestor
      rw [eqn] at vy
      obtain ⟨yp,yt⟩ := mem_Icc.mp hy
      exact fail y yp yt vy
  have sum := sum_le_sum every
  have total := card_eq_sum_card_fiberwise maps
  dsimp only [dst] at total
  simp [dst] at sum
  omega

#print axioms early_hit_count
#print axioms late_ancestor
#print axioms synchronized_ancestor
end Collatz.Itinerary.PassageGate
