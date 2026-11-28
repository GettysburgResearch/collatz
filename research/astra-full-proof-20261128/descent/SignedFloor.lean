import Std.Tactic

/-! A positive and negative integer on a common binary cylinder.
    All inequalities are integral and no convergence assumption is used. -/

set_option autoImplicit false
set_option warningAsError true

namespace Collatz.Sprint.SignedFloor

def P (x : Nat) : Nat := if x%2=0 then x/2 else (3*x+1)/2

def M (a : Nat) : Nat := if a%2=0 then a/2 else (3*a-1)/2

theorem pos_eq (x : Nat) : 2*P x=3^(x%2)*x+x%2 := by
  have e : x%2=0 ∨ x%2=1 := by omega
  rcases e with e|e <;> simp [P,e] <;> omega

theorem neg_eq (a : Nat) (ha : 0<a) : 2*M a+a%2=3^(a%2)*a := by
  have e : a%2=0 ∨ a%2=1 := by omega
  rcases e with e|e <;> simp [M,e] <;> omega

theorem neg_pos (a : Nat) (ha : 0<a) : 0<M a := by
  have e : a%2=0 ∨ a%2=1 := by omega
  rcases e with e|e <;> simp [M,e] <;> omega

theorem ratio_step (x a : Nat) (ha : 0<a) (same : x%2=a%2) : x*M a≤a*P x := by
  have hx := pos_eq x
  rw [same] at hx
  have hn := neg_eq a ha
  have raised : 2*(x*M a) ≤ 2*(a*P x) := by
    calc
      _ = x*(2*M a) := by ac_rfl
      _ ≤ x*(3^(a%2)*a) := Nat.mul_le_mul_left _ (by omega)
      _ = a*(3^(a%2)*x) := by ac_rfl
      _ ≤ a*(2*P x) := Nat.mul_le_mul_left _ (by omega)
      _ = _ := by ac_rfl
  omega

def fwd : Nat → Nat → Nat
  | 0, x => x
  | k+1, x => fwd k (P x)

def negFwd : Nat → Nat → Nat
  | 0, a => a
  | k+1, a => negFwd k (M a)

theorem negFwd_pos (k a : Nat) (ha : 0<a) : 0<negFwd k a := by
  induction k generalizing a with
  | zero => exact ha
  | succ k ih => exact ih (M a) (neg_pos a ha)

theorem ratio_path (k x a : Nat) (ha : 0<a) (source : 2^k ∣ x+a) :
    x*negFwd k a≤a*fwd k x := by
  induction k generalizing x a with
  | zero => simp [fwd, negFwd, Nat.mul_comm]
  | succ k ih =>
    obtain ⟨d,hd⟩ := source
    have evenSum : x+a=2*((2^k)*d) := by
      rw [hd, Nat.pow_succ]
      ac_rfl
    have same : x%2 = a%2 := by omega
    have hx := pos_eq x
    rw [same] at hx
    have hm := neg_eq a ha
    have combine : 2*(P x+M a)=3^(a%2)*(x+a) := by
      rw [Nat.mul_add, Nat.mul_add]
      omega
    have next : 2^k ∣ P x+M a := by
      refine ⟨3^(a%2)*d,?_⟩
      rw [evenSum] at combine
      have scaled : 2*(P x+M a)=2*(2^k*(3^(a%2)*d)) := by
        rw [combine]
        ac_rfl
      omega
    have tail := ih (P x) (M a) (neg_pos a ha) next
    have first := ratio_step x a ha same
    have total : M a*(x*negFwd k (M a))≤M a*(a*fwd k (P x)) := by
      calc
        _ = (x*M a)*negFwd k (M a) := by ac_rfl
        _ ≤ (a*P x)*negFwd k (M a) := Nat.mul_le_mul_right _ first
        _ = a*(P x*negFwd k (M a)) := by ac_rfl
        _ ≤ a*(M a*fwd k (P x)) := Nat.mul_le_mul_left a tail
        _ = _ := by ac_rfl
    exact Nat.le_of_mul_le_mul_left total (neg_pos a ha)

theorem negative_shadow_floor (k x a : Nat) (ha : 0<a)
    (source : 2^k ∣ x+a) : x≤a*fwd k x := by
  have pos := negFwd_pos k a ha
  have first := Nat.mul_le_mul_left x (show 1≤negFwd k a by omega)
  simpa using Nat.le_trans first (ratio_path k x a ha source)

#print axioms ratio_path
#print axioms negative_shadow_floor

end Collatz.Sprint.SignedFloor
