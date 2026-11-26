import InversePowerRows

/-! At an odd factorization `3*n+1 = 2^e*u`, the exponent is exact.
The eight possible excesses `5*e-(n.log2+1) = 0,...,7` suffice for the
universal convergence test. -/

namespace CollatzShell.MarkedCylinders
open ForwardSection

/-- The lower and upper bounds retain all eight integer excesses. -/
def CriticalMark (n : Nat) : Prop :=
  Marked n ∧ ∃ e u : Nat, Odd u ∧ 3*n+1=2^e*u ∧
    n.log2+1≤5*e ∧ 5*e≤n.log2+8

/-- Deleting the two low bits `01` reduces the binary exponent by two and
preserves the defining geometric section inequality. -/
private theorem quarter_section (m : Nat) (mp : 0<m) (mark : InSection (4*m+1)) :
    (4*m+1).log2=m.log2+2 ∧ InSection m := by
  have lo := Nat.log2_self_le mp.ne'
  have hi := Nat.lt_log2_self (n:=m)
  have oct : (4*m+1).log2=m.log2+2 := by
    apply (Nat.log2_eq_iff (by omega)).2
    simp only [pow_succ] at hi ⊢
    omega
  have off : 4*m+1-2^(m.log2+2)=4*(m-2^m.log2)+1 := by
    rw [pow_add]; omega
  refine ⟨oct,?_⟩
  unfold InSection at mark ⊢
  rw [oct,off,pow_add] at mark
  norm_num only [Nat.reducePow] at mark
  nlinarith only [mark, Nat.zero_le (m-2^m.log2),Nat.zero_le m.log2]

/-- Removing a high excess gives an ordinary smaller marked source whose
exact odd cofactor is unchanged. The two source trajectories meet after
one clock from the partner and three from the original source. -/
theorem critical_quarter_descent {n e u : Nat} (large : 3<n) (mark : Marked n)
    (odd : Odd u) (factor : 3*n+1=2^e*u) (deep : n.log2+9≤5*e) :
    ∃ m f : Nat, 0<m ∧ m<n ∧ n=4*m+1 ∧ e=f+2 ∧ n.log2=m.log2+2 ∧
      Marked m ∧ Odd u ∧ 3*m+1=2^f*u ∧ m.log2+1≤5*f ∧
      (5*e-(n.log2+1))=(5*f-(m.log2+1))+8 ∧ orbit 1 m=orbit 3 n := by
  have nd : 2≤n.log2 := (Nat.le_log2 (by omega)).2 (by omega)
  have eg : 3≤e := by omega
  let k := e-3
  let z := 2^k*u
  have ek : e=k+3 := by dsimp [k]; omega
  have full : 3*n+1=8*z := by
    rw [factor,ek,pow_add]; dsimp only [z]; ring
  let m := (n-1)/4
  have form : n=4*m+1 := by dsimp only [m]; omega
  have mp : 0<m := by omega
  have mo : m%2=1 := by omega
  have eq : 3*m+1=2*z := by omega
  obtain ⟨oct,sect⟩ := quarter_section m mp (form ▸ mark.2)
  have dig : n.log2=m.log2+2 := by simpa only [← form] using oct
  have small : 3*m+1=2^(k+1)*u := by dsimp only [z] at eq; rw [eq,pow_succ]; ring
  have mn : step m=z := by simp [step,mo,eq]
  have nn : step n=4*z := by simp [step,mark.1,full]; omega
  have cross : orbit 1 m=orbit 3 n := by
    simp only [orbit,mn,nn,show 4*z=2*(2*z) by omega,step_double]
  refine ⟨m,k+1,mp,by omega,form,by omega,dig,⟨mo,sect⟩,odd,small,by omega,by omega,cross⟩

/-- Every supplied prefix exponent can be augmented to the unique exponent
whose remaining cofactor is odd. -/
private theorem exact_exponent {n g a : Nat} (initial : 3*n+1=2^g*a) :
    ∃ e u : Nat, g≤e ∧ Odd u ∧ 3*n+1=2^e*u := by
  have ap : a≠0 := by intro h; simp [h] at initial
  obtain ⟨k,u,odd,ak⟩ := Nat.exists_eq_two_pow_mul_odd ap
  exact ⟨g+k,u,by omega,odd,by rw [initial,ak,pow_add,Nat.mul_assoc]⟩

/-- Every positive source reaches one iff all marks in the eight-excess
critical section do. The cofactor in `CriticalMark` must be odd. -/
theorem universal_iff_critical_mark : Universal ↔ ∀ n : Nat, CriticalMark n → Basin n := by
  constructor
  · intro all n crit; exact all n (by have := crit.1.1; omega)
  · intro critical
    apply universal_iff_marked_power.mpr
    intro n
    induction n using Nat.strong_induction_on with
    | h n ih =>
      intro marked cert
      obtain ⟨g,a,dig,initial⟩ := cert
      obtain ⟨e,u,ge,odd,factor⟩ := exact_exponent initial
      have low : n.log2+1≤5*e := by omega
      by_cases edge : 5*e≤n.log2+8
      · exact critical n ⟨marked,e,u,odd,factor,low,edge⟩
      have no : n%2=1 := marked.1
      by_cases tiny : n≤3
      · have cases' : n=1 ∨ n=3 := by omega
        rcases cases' with rfl|rfl
        · exact ⟨0,rfl⟩
        · exact ⟨5,rfl⟩
      obtain ⟨m,f,_,lt,_,_,_,mark,_,fac,d,_,meet⟩ :=
        critical_quarter_descent (by omega : 3<n) marked odd factor (by omega)
      have bm := ih m lt mark ⟨f,u,d,fac⟩
      exact (basin_at_hit (show Hits n (orbit 1 m) from ⟨3,meet.symm⟩)).mpr
        ((basin_at_hit (show Hits m (orbit 1 m) from ⟨1,rfl⟩)).mp bm)

#print axioms critical_quarter_descent
#print axioms universal_iff_critical_mark
end CollatzShell.MarkedCylinders
