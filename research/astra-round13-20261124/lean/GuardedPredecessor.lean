import AffinePairReturn

namespace CollatzShell.AffinePairReturn

/-- Reversing one final halving and an actual odd run lands at the specified
    source. Only the equality and positivity are required to execute the word. -/
theorem guarded_predecessor (s r z : Nat) (hz : 0<z)
    (guard : 3^s*z=2*r+1) :
    orbit (s+1) (2^s*z-1)=r := by
  rw [orbit_add,(odd_run s z hz).1,guard]
  change step (2*r+1-1)=r
  simp [step_double]

theorem predecessor_smaller (s r z : Nat) (hz : 0<z) (hs : 2≤s)
    (guard : 3^s*z=2*r+1) :
    0<2^s*z-1 ∧ 2^s*z-1<r := by
  have ratio (a : Nat) : 2*2^(a+2)<3^(a+2) := by
    induction a with
    | zero => decide
    | succ a ih =>
      rw [show a+1+2=(a+2)+1 by omega,pow_succ 2 (a+2),pow_succ 3 (a+2)]
      omega
  have h := ratio (s-2)
  rw [Nat.sub_add_cancel hs] at h
  have h' := Nat.mul_lt_mul_of_pos_right h hz
  have lo : 2≤2^s := by
    obtain ⟨a,eq⟩ := Nat.exists_eq_add_of_le hs
    rw [eq,pow_add]
    have h2 : 0<2^a := by positivity
    omega
  have lx := Nat.mul_le_mul_right z lo
  rw [Nat.mul_assoc] at h'
  omega

/-- The odd h=0 guard in PR193 / LS3 of PR194. -/
theorem ls3_predecessor (t : Nat) :
    orbit 5 (64*t+47)=162*t+121 ∧ 0<64*t+47 ∧ 64*t+47<162*t+121 ∧
    81*(64*t+47)+65=32*(162*t+121) := by
  have g : 3^4*(4*t+3)=2*(162*t+121)+1 := by ring
  have h := guarded_predecessor 4 (162*t+121) (4*t+3) (by omega) g
  have e : 2^4*(4*t+3)-1=64*t+47 := by omega
  rw [e] at h
  exact ⟨h,by omega,by omega,by omega⟩

#print axioms guarded_predecessor
#print axioms predecessor_smaller
#print axioms ls3_predecessor

end CollatzShell.AffinePairReturn
