import Mathlib.Tactic

namespace FourTritDelay

def step (x : ℕ) : ℕ := if x % 2 = 0 then x / 2 else (3*x+1)/2

def walk : ℕ → ℕ → ℕ
  | 0, x => x
  | n+1, x => walk n (step x)

private theorem evenStep (n : ℕ) : step (2*n) = n := by
  simp [step]

private theorem oddStep (n : ℕ) : step (2*n+1) = 3*n+2 := by
  simp only [step]
  split <;> omega

private theorem powTwoWalk (h z : ℕ) : walk h (2^h*z) = z := by
  induction h with
  | zero => simp [walk]
  | succ h ih =>
    rw [show 2^(h+1)*z=2*(2^h*z) by ring, walk, evenStep, ih]

theorem oddRun (h z : ℕ) (hz : 0 < z) :
    walk h (2^h*z-1) = 3^h*z-1 := by
  induction h generalizing z with
  | zero => simp [walk]
  | succ h ih =>
    have ha : 0 < 2^h*z := by positivity
    have hb : 0 < 3*z := by omega
    rw [show 2^(h+1)*z-1=2*(2^h*z-1)+1 by rw [show 2^(h+1)*z=2*(2^h*z) by ring]; omega,
        walk, oddStep]
    rw [show 3*(2^h*z-1)+2=2^h*(3*z)-1 by
      rw [show 2^h*(3*z)=3*(2^h*z) by ring]; omega, ih (3*z) hb]
    congr 1
    ring

private theorem walkAdd (a b x : ℕ) :
    walk (a+b) x = walk b (walk a x) := by
  induction a generalizing x with
  | zero => simp [walk]
  | succ a ih => simpa only [Nat.succ_add, walk] using ih (step x)

theorem exactArms (h m z : ℕ) (hz : 0 < z)
    (eqn : 81*m+65=2^(h+4)*z) :
    walk (h+4) m = z ∧ walk (h+4) (81*m+64) = 3^(h+4)*z-1 := by
  have e : 81*m+65=16*(2^h*z) := by
    calc 81*m+65=2^(h+4)*z := eqn
         _=16*(2^h*z) := by ring
  have pos : 0 < m/16+1 := by omega
  have rep : m=2^4*(m/16+1)-1 := by norm_num; omega
  have first : walk 4 m = 2^h*z := by
    conv_lhs => rw [rep]
    rw [oddRun 4 (m/16+1) pos]
    norm_num
    omega
  constructor
  · rw [Nat.add_comm h 4, walkAdd, first, powTwoWalk]
  · rw [show 81*m+64=2^(h+4)*z-1 by omega, oddRun (h+4) z hz]

#print axioms oddRun
#print axioms exactArms

end FourTritDelay
