import CriticalSection

/-! Transport a physical merger of compressed odd endpoints into a strictly
smaller source of the same exact critical excess. -/

namespace CollatzShell.MarkedCylinders
open ForwardSection

private theorem scaled_section {n m D b : Nat}
    (dig : n.log2 = D + b) (lo : 2^D ≤ m) (scaled : 2^b*m ≤ n)
    (sect : InSection n) : m.log2 = D ∧ InSection m := by
  have high := Nat.lt_log2_self (n:=n)
  rw [dig] at high
  have scale : 0 < 2^b := pow_pos (by decide) _
  have hi : m < 2^(D+1) := by
    apply Nat.lt_of_mul_lt_mul_left (a:=2^b)
    calc 2^b*m ≤ n := scaled
         _ < 2^(D+b+1) := high
         _ = 2^b*2^(D+1) := by rw [← pow_add]; congr 1; omega
  have oct := (Nat.log2_eq_iff (by have : 0 < 2^D := pow_pos (by decide) _; omega)).mpr
    (show 2^D ≤ m ∧ m < 2^(D+1) from ⟨lo,hi⟩)
  refine ⟨oct,?_⟩
  unfold InSection at sect ⊢
  rw [oct]
  rw [dig,show (2:Nat)^(D+b)=2^b*2^D by rw [← pow_add,Nat.add_comm]] at sect
  have rem : 2^b*(m-2^D) ≤ n-2^b*2^D := by
    rw [Nat.mul_sub]; omega
  have bound : 2^b * ((D+1)*(m-2^D)) ≤ 2^b*(70*2^D) := by
    calc 2^b*((D+1)*(m-2^D)) = (D+1)*(2^b*(m-2^D)) := by ring
         _ ≤ (D+b+1)*(n-2^b*2^D) := Nat.mul_le_mul (by omega) rem
         _ ≤ 70*(2^b*2^D) := sect
         _ = 2^b*(70*2^D) := by ring
  exact Nat.le_of_mul_le_mul_left bound scale

private theorem hit_factored {x e y : Nat} (xo : x%2=1) (ep : 0<e)
    (eq : 3*x+1=2^e*y) : Hits x y := by
  obtain ⟨k,rfl⟩ := Nat.exists_eq_succ_of_ne_zero ep.ne'
  have st : step x=2^k*y := by
    rw [show (2:Nat)^(k+1)*y = 2*(2^k*y) by ring] at eq
    simp [step,xo,eq]
  exact ⟨k+1,by simp only [orbit,st,orbit_pad]⟩

/-- A compressed odd cofactor can be lifted to a strictly smaller critical
source with exactly the original surplus. The two endpoint clocks may differ.
The lower-octave test is necessary at the bottom boundary of the mark. -/
theorem critical_compression {n m D k f u v z : Nat}
    (kn : 0<k) (fp : 0<f) (mark : Marked n)
    (oct : n.log2 = D+10*k)
    (low : n.log2+1 ≤ 5*(f+2*k)) (high : 5*(f+2*k) ≤ n.log2+8)
    (en : 3*n+1=2^(f+2*k)*u) (mv : 3*m+1=2^f*v) (vo : Odd v)
    (less : 2^(8*k)*v ≤ u) (edge : 2^D ≤ m)
    (un : Hits u z) (vn : Hits v z) :
    m.log2 = D ∧ 2^(10*k)*m < n ∧ CriticalMark m ∧
    5*(f+2*k)-(n.log2+1) = 5*f-(m.log2+1) ∧ Hits n z ∧ Hits m z := by
  have scale : 1 < (2:Nat)^(10*k) := one_lt_pow₀ (by decide) (by omega)
  have fac : 2^(10*k)*(3*m+1) ≤ 3*n+1 := by
    calc 2^(10*k)*(3*m+1) = 2^(f+2*k)*(2^(8*k)*v) := by
           rw [mv]
           calc 2^(10*k)*(2^f*v) = 2^(10*k+f)*v := by rw [pow_add]; ring
                _ = 2^((f+2*k)+8*k)*v := by congr 2; omega
                _ = 2^(f+2*k)*(2^(8*k)*v) := by rw [pow_add]; ring
         _ ≤ 2^(f+2*k)*u := Nat.mul_le_mul_left _ less
         _ = 3*n+1 := en.symm
  have small : 2^(10*k)*m<n := by
    rw [Nat.mul_add,Nat.mul_one,show 2^(10*k)*(3*m)=3*(2^(10*k)*m) by ring] at fac
    omega
  obtain ⟨mo,sec⟩ := scaled_section oct edge small.le mark.2
  have odd : m%2=1 := by
    obtain ⟨j,rfl⟩ := Nat.exists_eq_succ_of_ne_zero fp.ne'
    rw [pow_succ] at mv
    have even : 2^j*2*v=2*(2^j*v) := by ring
    rw [even] at mv; omega
  exact ⟨mo,small,⟨⟨odd,sec⟩,f,v,vo,mv,by omega,by omega⟩,by omega,
    (hit_factored mark.1 (by omega) en).trans un,(hit_factored odd fp mv).trans vn⟩

#print axioms critical_compression
end CollatzShell.MarkedCylinders
