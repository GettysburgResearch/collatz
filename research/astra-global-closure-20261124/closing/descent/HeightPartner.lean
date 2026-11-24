import Std
import CycleShadows

/-! A positive ordinary predecessor on every ternary height above 1. -/
set_option maxRecDepth 8192
namespace HeightPartner
open CycleShadows

private theorem two (v : Nat) : run T 2 (1+4*v)=1+3*v := by
  have h₁ : T (1+4*v)=2+6*v := by unfold T; split <;> omega
  have h₂ : T (2+6*v)=1+3*v := by unfold T; split <;> omega
  change T (T (1+4*v))=_
  rw [h₁,h₂]

theorem tours (h v : Nat) : run T (2*h) (1+4^h*v) = 1+3^h*v := by
  induction h generalizing v with
  | zero => simp [run]
  | succ h ih =>
    rw [Nat.mul_succ, Nat.add_comm (2*h) 2, run_add]
    rw [Nat.pow_succ, show 4^h*4*v=4*(4^h*v) by ac_rfl,two]
    rw [show 3*(4^h*v)=4^h*(3*v) by ac_rfl,ih,Nat.pow_succ]
    ac_rfl

/-- When the short-witness margin holds, the two prescribed segments
reach the source itself; all assumptions are finite integer tests. -/
theorem height_partner (h d v z : Nat) (hd : 0<d)
    (guard : 3^d*z=2+4^h*v) (margin : 2^d*4^h ≤ 3^d*3^h) :
    ∃ m, 0<m ∧ m%2=1 ∧ m<1+3^h*v ∧ run T (d+2*h) m = 1+3^h*v := by
  have hz : 0<z := by
    by_cases zz : z=0
    · rw [zz,Nat.mul_zero] at guard
      omega
    · omega
  have sz : 2≤2^d := Nat.pow_le_pow_right (by decide : 0<2) (by omega : 1≤d)
  have prod := Nat.le_mul_of_pos_right (2^d) hz
  let m := 2^d*z-1
  have hm : m+1=2^d*z := by dsimp [m]; omega
  have hodd : m%2=1 := by
    cases d with
    | zero => omega
    | succ d =>
      rw [Nat.pow_succ,Nat.mul_right_comm] at hm
      omega
  have lift₁ := lift d m 1 z (by decide) hm
  obtain ⟨h1, w1⟩ := one_rail d
  rw [h1,w1,guard] at lift₁
  have hfirst : run T d m=1+4^h*v := by omega
  have tw : 2^d < 3^d := Nat.pow_lt_pow_left (by decide) (by omega)
  have cost := Nat.mul_le_mul_right v margin
  rw [Nat.mul_assoc,Nat.mul_assoc] at cost
  have lhs : 3^d*(m+1)=2*(2^d)+2^d*(4^h*v) := by
    rw [hm, Nat.mul_left_comm, guard, Nat.mul_add, Nat.mul_comm (2^d) 2]
  have lt : 3^d*(m+1)<3^d*(2+3^h*v) := by
    rw [lhs,Nat.mul_add,Nat.mul_comm (3^d) 2]
    omega
  have small := Nat.lt_of_mul_lt_mul_left lt
  refine ⟨m, by omega, hodd, by omega, ?_⟩
  rw [run_add,hfirst,tours]

private theorem closed12 (x : Nat) (hx : x=1 ∨ x=2) :
    ∀ k, run T k x=1 ∨ run T k x=2 := by
  intro k
  induction k generalizing x with
  | zero => exact hx
  | succ k ih =>
    apply ih
    rcases hx with rfl | rfl <;> decide

private def avoids : Nat → Nat → Bool
  | 0,x => x != 55
  | k+1,x => (x != 55) && avoids k (T x)

private theorem avoids_spec (K x : Nat) (h : avoids K x=true) (k : Nat) (hk : k≤K) :
    run T k x≠55 := by
  induction k generalizing K x with
  | zero =>
    cases K with
    | zero => simpa [avoids, run] using h
    | succ K =>
      simp [avoids] at h
      exact h.1
  | succ k ih =>
    cases K with
    | zero => omega
    | succ K =>
      simp [avoids] at h
      exact ih K (T x) h.2 (by omega)

set_option maxRecDepth 8192 in
private theorem first55 : ∀ x : Fin 55, 0<x.val →
    avoids 72 x.val=true ∧ (run T 72 x.val=1 ∨ run T 72 x.val=2) := by decide

/-- Even all ordinary predecessor words cannot find a smaller source at 55
itself. Both the certified member arm and a later smaller endpoint are explicit. -/
theorem no_predecessor_55 (m k : Nat) (hm : 0<m) (hlt : m<55) : run T k m≠55 := by
  obtain ⟨f,g⟩ := first55 ⟨m,hlt⟩ hm
  by_cases h : k≤72
  · exact avoids_spec 72 m f k h
  · rw [show k=72+(k-72) by omega,run_add]
    have hg := closed12 (run T 72 m) g (k-72)
    omega

theorem witness_55 : run T 71 (3*55-1)=1 ∧ run T 5 55=47 := by decide

#print axioms no_predecessor_55
#print axioms witness_55
#print axioms height_partner
end HeightPartner
