import Std

namespace Collatz.KernelTransfer

def step (n : Nat) : Nat := if n%2=0 then n/2 else (3*n+1)/2
def run (k n : Nat) : Nat := Nat.rec n (fun _ x => step x) k

private theorem append (a b n : Nat) : run (a+b) n=run b (run a n) := by
  induction b with
  | zero => rfl
  | succ b ih => change step (run (a+b) n)=step (run b (run a n)); rw [ih]

private theorem half (v : Nat) : step (2*v)=v := by simp [step]

private theorem halvePow (k v : Nat) : run k (2^k*v)=v := by
  induction k with
  | zero => simp only [Nat.pow_zero, Nat.one_mul]; rfl
  | succ k ih =>
    rw [show k+1=1+k by omega, append]
    change run k (step (2^(1+k)*v))=v
    rw [Nat.pow_add, Nat.pow_one, Nat.mul_assoc, half, ih]

/-- Pick one inverse odd branch after at most five doublings, keeping a ternary-unit low coefficient. -/
theorem inverse_digit (r : Nat) (hr : r%3≠0) :
    ∃ b z : Nat, b≤5 ∧ z%3=1 ∧ z%2=1 ∧ 3*z+1=2^(b+1)*r := by
  have split9 : r%9=1 ∨ r%9=2 ∨ r%9=4 ∨ r%9=5 ∨ r%9=7 ∨ r%9=8 := by omega
  rcases split9 with h|h|h|h|h|h
  · exact ⟨1,(4*r-1)/3, by decide, by omega, by omega, by omega⟩
  · exact ⟨0,(2*r-1)/3, by decide, by omega, by omega, by omega⟩
  · exact ⟨5,(64*r-1)/3, by decide, by omega, by omega, by omega⟩
  · exact ⟨2,(8*r-1)/3, by decide, by omega, by omega, by omega⟩
  · exact ⟨3,(16*r-1)/3, by decide, by omega, by omega, by omega⟩
  · exact ⟨4,(32*r-1)/3, by decide, by omega, by omega, by omega⟩

private theorem oneInverse (b v n : Nat) (ho : v%2=1)
    (eq : 3*v+1=2^(b+1)*n) : run (b+1) v=n := by
  have hstep : step v=2^b*n := by
    rw [show 2^(b+1)*n=2*(2^b*n) by rw [Nat.pow_succ]; ac_rfl] at eq
    simp [step, show v%2≠0 by omega, eq]
  rw [show b+1=1+b by omega,append]
  change run b (step v)=n
  rw [hstep,halvePow]

/-- Uniformly in the unbounded high digits n: every ternary-unit subsequence
is realized by *one* dyadic residue and an ordinary clock at most 6h. -/
theorem ternary_row (h r : Nat) (hr : r<3^h) (hu : r%3≠0) :
    ∃ A p : Nat, A≤6*h ∧ p<2^A ∧ ∀ n, run A (2^A*n+p)=3^h*n+r := by
  induction h generalizing r with
  | zero => simp at hr; omega
  | succ h ih =>
    obtain ⟨b,z,hb,hz3,hz2,he⟩ := inverse_digit r hu
    -- Remove one factor of three from the high coefficient. Normalize the
    -- new low part modulo 3^h before applying the smaller-row assertion.
    let v := z%3^h
    let d := z/3^h
    have powpos : 0<3^h := by exact Nat.pow_pos (by decide)
    have hz : z=3^h*d+v := (Nat.div_add_mod _ _).symm
    by_cases h0 : h=0
    · subst h
      have rz : r<3 := by simpa using hr
      have lo : z<2^(b+1) := by
        have hh := Nat.mul_lt_mul_of_pos_left rz (Nat.pow_pos (a:=2) (n:=b+1) (by decide))
        omega
      refine ⟨b+1,z,by omega,lo,?_⟩
      intro n
      apply oneInverse b
      · rw [Nat.add_mod, Nat.mul_mod, Nat.pow_succ, Nat.mul_mod (2^b) 2 2]
        simp [hz2]
      · change 3*(2^(b+1)*n+z)+1=2^(b+1)*(3*n+r)
        rw [Nat.mul_add, Nat.mul_comm 3 (2^(b+1)*n), Nat.add_assoc, he, Nat.mul_add]
        ac_rfl
    · have dv : 3 ∣ 3^h := by
        cases h with
        | zero => contradiction
        | succ h => rw [Nat.pow_succ]; exact Nat.dvd_mul_left 3 _
      have vpos : v<3^h := Nat.mod_lt _ powpos
      have vu : v%3≠0 := by
        have hm := congrArg (· % 3) hz
        simp [Nat.add_mod, Nat.mul_mod, Nat.mod_eq_zero_of_dvd dv, hz3] at hm
        omega
      obtain ⟨A,p,hA,hp,hh⟩ := ih v vpos vu
      have dz : d<2^(b+1) := by
        have e1 := Nat.mul_lt_mul_of_pos_left hr (Nat.pow_pos (a:=2) (n:=b+1) (by decide))
        rw [Nat.pow_succ 3 h] at e1
        have e2 : z<2^(b+1)*3^h := by
          have ze : (2^(b+1)*3^h)*3=2^(b+1)*(3^h*3) := Nat.mul_assoc _ _ _
          omega
        exact (Nat.div_lt_iff_lt_mul powpos).mpr e2
      refine ⟨A+(b+1),2^A*d+p,by omega,?_,?_⟩
      · rw [Nat.pow_add]
        calc
          2^A*d+p < 2^A*(d+1) := by rw [Nat.mul_add,Nat.mul_one]; omega
          _ ≤ 2^A*2^(b+1) := Nat.mul_le_mul_left _ dz
      · intro n
        have ex : 2^(A+(b+1))*n+(2^A*d+p) = 2^A*(2^(b+1)*n+d)+p := by
          rw [Nat.pow_add,Nat.mul_add]; ac_rfl
        rw [ex, append, hh]
        have xeq : 3^h*(2^(b+1)*n+d)+v = 2^(b+1)*(3^h*n)+z := by
          rw [Nat.mul_add,hz]; ac_rfl
        rw [xeq]
        apply oneInverse b
        · rw [Nat.add_mod, Nat.mul_mod, Nat.pow_succ, Nat.mul_mod (2^b) 2 2]
          simp [hz2]
        · rw [Nat.mul_add, Nat.add_assoc, he, Nat.mul_add]
          rw [Nat.pow_succ 3 h]
          ac_rfl

#print axioms inverse_digit
#print axioms ternary_row
end Collatz.KernelTransfer
