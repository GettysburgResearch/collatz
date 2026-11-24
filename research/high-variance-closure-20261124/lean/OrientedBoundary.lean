import Mathlib.Tactic

namespace OrientedBoundary

structure Colors where
  color : ℕ → Bool
  evenRule (n : ℕ) : color (2*n) = color n
  oddRule (n : ℕ) : color (2*n+1) = color (3*n+2)

def edge (c : Colors) (n : ℕ) : Bool × Bool := (c.color n,c.color (n+1))

theorem childChoice (c : Colors) (n : ℕ) (h : c.color n ≠ c.color (n+1)) :
    (edge c (2*n)=edge c n ∧ c.color (2*n+1)=c.color (2*n+2)) ∨
    (c.color (2*n)=c.color (2*n+1) ∧ edge c (2*n+1)=edge c n) := by
  have h2 : c.color (2*n+2) = c.color (n+1) := by
    rw [show 2*n+2=2*(n+1) by omega, c.evenRule]
  have h1 := c.evenRule n
  unfold edge
  rw [show 2*n+1+1=2*n+2 by omega]
  cases a : c.color n <;> cases b : c.color (n+1) <;> cases e : c.color (2*n+1) <;>
    simp_all

theorem zeroTriple (c : Colors) (l : ℕ) :
    edge c (4*l+2) = edge c (6*l+4) := by
  have a : c.color (4*l+2) = c.color (3*l+2) := by
    rw [show 4*l+2=2*(2*l+1) by omega, c.evenRule, c.oddRule]
  have b : c.color (6*l+4)=c.color (3*l+2) := by
    rw [show 6*l+4=2*(3*l+2) by omega,c.evenRule]
  have d := c.oddRule (2*l+1)
  have e : 2*(2*l+1)+1=4*l+2+1 := by omega
  have f : 3*(2*l+1)+2=6*l+4+1 := by omega
  rw [e,f] at d
  exact Prod.ext (a.trans b.symm) d

theorem inverseThird (c : Colors) (l : ℕ) :
    edge c (3*l+1) = edge c (4*l+1) := by
  have h := c.oddRule (2*l)
  rw [show 2*(2*l)+1=4*l+1 by omega,
      show 3*(2*l)+2=2*(3*l+1) by omega,c.evenRule] at h
  have j : c.color (4*l+1+1) = c.color (3*l+1+1) := by
    rw [show 4*l+1+1=2*(2*l+1) by omega,c.evenRule,c.oddRule]
  exact Prod.ext h.symm j.symm

private theorem run (c : Colors) (k z : ℕ) (hz : 0<z) :
    c.color (2^k*z-1)=c.color (3^k*z-1) := by
  induction k generalizing z with
  | zero => simp
  | succ k ih =>
    have hw : 0 < 2^k*z := by positivity
    rw [show 2^(k+1)*z-1=2*(2^k*z-1)+1 by
          rw [show 2^(k+1)*z=2*(2^k*z) by ring]; omega, c.oddRule,
        show 3*(2^k*z-1)+2=2^k*(3*z)-1 by
          rw [show 2^k*(3*z)=3*(2^k*z) by ring]; omega,
        ih (3*z) (by omega),show 3^k*(3*z)=3^(k+1)*z by ring]

theorem forbiddenGap (c : Colors) (s l : ℕ) :
    let n := 2^(2*s+1)*(4*l+3)-2
    c.color n=c.color (n+1) := by
  dsimp
  let u:=4*l+3
  have hu : 0<u := by dsimp [u];omega
  have h2 : 0<2^(2*s)*u := by positivity
  have h3 : 0<3^(2*s)*u := by positivity
  have h2e : 2^(2*s+1)*u=2*(2^(2*s)*u) := by ring
  change c.color (2^(2*s+1)*u-2)=c.color (2^(2*s+1)*u-2+1)
  rw [show 2^(2*s+1)*u-2=2*(2^(2*s)*u-1) by omega,c.evenRule,
      show 2*(2^(2*s)*u-1)+1=2^(2*s+1)*u-1 by omega,
      run c (2*s) u hu,run c (2*s+1) u hu]
  have hmod : 3^(2*s)*u % 4=3 := by
    have h9 : Nat.ModEq 4 9 1 := by decide
    have hu4 : Nat.ModEq 4 u 3 := by dsimp [u,Nat.ModEq]; omega
    change Nat.ModEq 4 (3^(2*s)*u) 3
    rw [pow_mul]
    simpa using ((h9.pow s).mul hu4)
  let v:=3^(2*s)*u/4
  have he : 3^(2*s)*u=4*v+3 := by dsimp [v]; omega
  rw [show 3^(2*s+1)*u=3*(3^(2*s)*u) by ring,he,
      show 4*v+3-1=2*(2*v+1) by omega,c.evenRule,c.oddRule,
      show 3*(4*v+3)-1=2*(3*(2*v+1)+1) by omega,c.evenRule]
  rw [show 3*(2*v+1)+1=2*(3*v+2) by omega,c.evenRule]

#print axioms childChoice
#print axioms zeroTriple
#print axioms inverseThird
#print axioms forbiddenGap

end OrientedBoundary
