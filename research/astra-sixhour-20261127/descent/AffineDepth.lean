import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination

namespace Collatz.AffineDepth

/-- An actual chronological word of forward and inverse ordinary edges from
N−1. The final two integer decorations are the affine coefficients after
clearing the common denominator 6^h. -/
inductive Walk (N : ℤ) : ℕ → ℤ → ℤ → ℤ → Prop where
  | start : Walk N 0 (N-1) 1 1
  | fwdEven {h : ℕ} {x y A c : ℤ} (earlier : Walk N h x A c) (step : 2*y=x) :
      Walk N (h+1) y (3*A) (3*c)
  | fwdOdd {h : ℕ} {x y A c : ℤ} (earlier : Walk N h x A c) (step : 2*y=3*x+1) :
      Walk N (h+1) y (9*A) (9*c-3*6^h)
  | backEven {h : ℕ} {x y A c : ℤ} (earlier : Walk N h x A c) (step : y=2*x) :
      Walk N (h+1) y (12*A) (12*c)
  | backOdd {h : ℕ} {x y A c : ℤ} (earlier : Walk N h x A c) (step : 3*y+1=2*x) :
      Walk N (h+1) y (4*A) (4*c+2*6^h)

/-- Denominator spacing and an intercept budget uniform over all physical
words of a given length, including source-selected words. -/
theorem geometry {N x A c : ℤ} {h : ℕ} (w : Walk N h x A c) :
    0<A ∧ 6^h*x=A*N-c ∧ -(12:Int)^h≤c ∧ c≤12^h := by
  induction w with
  | start => simp
  | @fwdEven h x y A c _ step ih =>
    obtain ⟨pa,id,lo,hi⟩ := ih
    have pos := pow_pos (by decide : (0:ℤ)<12) h
    rw [show (6:ℤ)^(h+1)=6^h*6 from pow_succ _ _,pow_succ]
    refine ⟨by omega,?_,by omega,by omega⟩
    linear_combination 3*id + 3*(6:ℤ)^h*step
  | @fwdOdd h x y A c _ step ih =>
    obtain ⟨pa,id,lo,hi⟩ := ih
    have pos := pow_pos (by decide : (0:ℤ)<6) h
    have smaller := pow_le_pow_left₀ (by decide : (0:ℤ)≤6) (by decide : (6:ℤ)≤12) h
    rw [show (6:ℤ)^(h+1)=6^h*6 from pow_succ _ _,pow_succ]
    refine ⟨by omega,?_,by omega,by omega⟩
    linear_combination 9*id + 3*(6:ℤ)^h*step
  | @backEven h x y A c _ step ih =>
    obtain ⟨pa,id,lo,hi⟩ := ih
    rw [show (6:ℤ)^(h+1)=6^h*6 from pow_succ _ _,pow_succ]
    refine ⟨by omega,?_,by omega,by omega⟩
    linear_combination 12*id + 6*(6:ℤ)^h*step
  | @backOdd h x y A c _ step ih =>
    obtain ⟨pa,id,lo,hi⟩ := ih
    have pos := pow_pos (by decide : (0:ℤ)<6) h
    have smaller := pow_le_pow_left₀ (by decide : (0:ℤ)≤6) (by decide : (6:ℤ)≤12) h
    rw [show (6:ℤ)^(h+1)=6^h*6 from pow_succ _ _,pow_succ]
    refine ⟨by omega,?_,by omega,by omega⟩
    linear_combination 4*id + 2*(6:ℤ)^h*step

/-- At the stated ordinary size a numerically smaller endpoint physically
forces the claimed cap on its leading affine coefficient. -/
theorem smaller_forces_slope {N x A c : ℤ} {h : ℕ} (w : Walk N h x A c)
    (room : 1000*12^h<N) (cut : 81*x≤128*N-271) : 81*A≤128*6^h := by
  obtain ⟨_,id,_,hi⟩ := geometry w
  have big := pow_pos (by decide : (0:ℤ)<12) h
  have den := pow_pos (by decide : (0:ℤ)<6) h
  have paid := mul_le_mul_of_nonneg_left cut den.le
  by_contra wrong
  have gap := mul_le_mul_of_nonneg_right (by omega : (1:ℤ)≤81*A-128*6^h) (by omega : 0≤N)
  nlinarith only [id,paid,gap,room,hi,den,big]

/-- No accidental numerical equality with the original triple can occur at
small word length: both affine coefficients are forced to match exactly. -/
theorem numerical_triple_rigid {N x A c : ℤ} {h : ℕ} (w : Walk N h x A c)
    (room : 1000*12^h<N) (triple : 81*x=384*N-813) :
    81*A=384*6^h ∧ 81*c=813*6^h := by
  obtain ⟨_,id,lo,hi⟩ := geometry w
  have big := pow_pos (by decide : (0:ℤ)<12) h
  have den := pow_pos (by decide : (0:ℤ)<6) h
  have ds := pow_le_pow_left₀ (by decide : (0:ℤ)≤6) (by decide : (6:ℤ)≤12) h
  have exact_id : (81*A-384*6^h)*N=81*c-813*6^h := by
    linear_combination (6:ℤ)^h*triple - 81*id
  have gap : 81*A=384*6^h := by
    by_contra wrong
    rcases lt_or_gt_of_ne wrong with lh|rh
    · have g := mul_le_mul_of_nonneg_right (by omega : (81*A-384*6^h:ℤ)≤-1) (by omega : 0≤N)
      rw [exact_id] at g
      omega
    · have g := mul_le_mul_of_nonneg_right (by omega : (1:ℤ)≤81*A-384*6^h) (by omega : 0≤N)
      rw [exact_id] at g
      omega
  rw [gap,sub_self,zero_mul] at exact_id
  exact ⟨gap,by omega⟩

#print axioms geometry
#print axioms smaller_forces_slope
#print axioms numerical_triple_rigid

end Collatz.AffineDepth
