module

public import Std

public section

namespace Collatz.PhaseRepulsion

private theorem normalized_three_step (q r a c d : Nat)
    (edge : 2^a*r = 3*q+1) (clock : a+d=3+3*c) :
    8*(2^c)*r ≤ 2^d*(3*q+2^c) := by
  have hk := Nat.two_pow_pos c
  have e : 3+c ≤ d+a := by omega
  have hp := Nat.pow_le_pow_right (by decide : 0<2) e
  rw [Nat.pow_add, Nat.pow_add] at hp
  calc
    _ ≤ (2^d*2^a)*r := Nat.mul_le_mul_right r hp
    _ = 2^d*(3*q+1) := by rw [Nat.mul_assoc,edge]
    _ ≤ _ := Nat.mul_le_mul_left _ (by omega)

private theorem three_iter (q a c : Nat → Nat) (j L : Nat)
    (edges : ∀ i, j ≤ i → i < j+L → 2^(a i)*q (i+1)=3*q i+1)
    (clocks : ∀ i, j ≤ i → i < j+L → a i+c (i+1)=3+3*c i)
    (floorEnd : 2^(c (j+L)) ≤ q (j+L)) :
    2^(c j)*(4*8^L+3^L) ≤ 5*3^L*q j := by
  induction L generalizing j with
  | zero =>
    simp only [Nat.add_zero] at floorEnd
    simp only [Nat.pow_zero, Nat.mul_one, Nat.reduceAdd, Nat.mul_comm (2^(c j)) 5]
    exact Nat.mul_le_mul_left 5 floorEnd
  | succ L ih =>
    have tail := ih (j+1) (fun i lo hi => edges i (by omega) (by omega))
      (fun i lo hi => clocks i (by omega) (by omega)) (by simpa [Nat.add_assoc, Nat.add_comm, Nat.add_left_comm] using floorEnd)
    have hs := normalized_three_step _ _ _ _ _ (edges j (by omega) (by omega))
      (clocks j (by omega) (by omega))
    let K := 2^(c j)
    let D := 2^(c (j+1))
    let U := 8^L
    let V := 3^L
    change D*(4*U+V) ≤ 5*V*q (j+1) at tail
    change 8*K*q (j+1) ≤ D*(3*q j+K) at hs
    have mulD : D*(8*K*(4*U+V)) ≤ D*(5*V*(3*q j+K)) := calc
      _ = (8*K)*(D*(4*U+V)) := by ac_rfl
      _ ≤ (8*K)*(5*V*q (j+1)) := Nat.mul_le_mul_left _ tail
      _ = (5*V)*(8*K*q (j+1)) := by ac_rfl
      _ ≤ (5*V)*(D*(3*q j+K)) := Nat.mul_le_mul_left _ hs
      _ = _ := by ac_rfl
    have bound := Nat.le_of_mul_le_mul_left mulD (Nat.two_pow_pos _)
    rw [Nat.pow_succ, Nat.pow_succ]
    change K*(4*(U*8)+V*3) ≤ 5*(V*3)*q j
    grind

theorem three_run_length (q a c : Nat → Nat) (j L : Nat)
    (edges : ∀ i, j ≤ i → i < j+L → 2^(a i)*q (i+1)=3*q i+1)
    (clocks : ∀ i, j ≤ i → i < j+L → a i+c (i+1)=3+3*c i)
    (floorEnd : 2^(c (j+L)) ≤ q (j+L)) :
    4*8^L ≤ 3^L*(5*q j-1) := by
  have hi := three_iter q a c j L edges clocks floorEnd
  have hf : 1 ≤ 2^(c j) := Nat.two_pow_pos _
  have hl := Nat.mul_le_mul_right (4*8^L+3^L) hf
  rw [Nat.one_mul] at hl
  have h := Nat.le_trans hl hi
  rw [Nat.mul_sub, Nat.mul_one]
  have he : 3^L*(5*q j)=5*3^L*q j := by ac_rfl
  omega

#print axioms three_run_length
end Collatz.PhaseRepulsion
