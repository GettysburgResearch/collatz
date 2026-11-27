module

public import PassageBoundary
import all PassageBoundary
import Mathlib.Tactic

public section
namespace Collatz.Itinerary.PassageBoundary

open Finset
set_option autoImplicit false

/-- Ordinary counting errors at the finitely many boundaries of a dyadic
partition force adjacent disagreements before a specified last octave. -/
theorem scheduled_mass {f : ℕ → ℝ} {d : ℝ} (bits : ∀ n, f n=0 ∨ f n=1)
    (double : ∀ n, f (2*n)=f n) (pos : 0<d) (proper : d<1) (k j : ℕ)
    (budget : ∀ n, 2^k≤n → n≤2^(k+1) →
      |partialSum f (2^j*n)-d*((2:ℝ)^j*n)|≤min d (1-d)/4*(2:ℝ)^j) :
    min d (1-d)/2 ≤ ∑ i ∈ range j, variation f (k+i) := by
  let L := 2^k
  let m := min d (1-d)
  have width : 2^(k+1)=L+L := by dsimp only [L]; rw [pow_succ]; omega
  have cell (r : ℕ) (hr : r<L) : |Cell f (L+r) j-d|≤m/2 := by
    let n := L+r
    have e0 := budget n (Nat.le_add_right _ _) (by rw [width]; dsimp only [n]; omega)
    have e1 := budget (n+1) (by dsimp only [n]; change L≤L+r+1; omega)
      (by rw [width]; dsimp only [n]; omega)
    let err (a : ℕ) := partialSum f (2^j*a)-d*((2:ℝ)^j*a)
    have eq : Cell f n j-d=(err (n+1)-err n)/(2:ℝ)^j := by
      unfold Cell err
      push_cast
      field_simp
      ring
    change |Cell f n j-d|≤m/2
    rw [eq,abs_div,abs_of_pos (by positivity : 0<(2:ℝ)^j)]
    apply (div_le_iff₀ (by positivity : 0<(2:ℝ)^j)).mpr
    have le := abs_sub (err (n+1)) (err n)
    change |err n|≤m/4*(2:ℝ)^j at e0
    change |err (n+1)|≤m/4*(2:ℝ)^j at e1
    linarith
  have point (r : ℕ) (hr : r<L) : m/2≤|Cell f (L+r) j-f (L+r)| := by
    have near := cell r hr
    have apart : m≤|d-f (L+r)| := by
      rcases bits (L+r) with a | a
      · rw [a,sub_zero,abs_of_pos pos]; exact min_le_left ..
      · rw [a,abs_of_neg (by linarith : d-1<0)]; dsimp only [m]; linarith [min_le_right d (1-d)]
    have tri := abs_add_le (d-Cell f (L+r) j) (Cell f (L+r) j-f (L+r))
    rw [sub_add_sub_cancel,abs_sub_comm d (Cell f (L+r) j)] at tri
    linarith
  have total := Finset.sum_le_sum (s:=range L) (fun r hr => point r (mem_range.mp hr))
  simp only [sum_const,card_range,nsmul_eq_mul] at total
  apply le_trans _ (multiscale f double k j)
  apply (le_div_iff₀ (by positivity : 0<(2:ℝ)^k)).mpr
  simpa only [L,Nat.cast_pow,Nat.cast_ofNat,mul_comm] using total

#print axioms scheduled_mass
end Collatz.Itinerary.PassageBoundary
