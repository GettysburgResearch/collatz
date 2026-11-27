import Std

/-! Exact ordinary arithmetic for the visible-prefix and repayment arguments. -/
namespace Repayment

/-- A shortcut orbit, including an empty segment. -/
def iter (f : Nat → Nat) : Nat → Nat → Nat
  | 0, x => x
  | n+1, x => f (iter f n x)

private theorem iter_add (f : Nat → Nat) (i j x : Nat) :
    iter f (i+j) x = iter f j (iter f i x) := by
  induction j with
  | zero => rfl
  | succ j ih => exact congrArg f ih

/-- Every witness from any allowed source paying a long clock is on the
complete forward orbit of a member of the *same* fixed-clock image. -/
theorem late_visitor_factor (f : Nat → Nat) (Allowed : Nat → Prop)
    (q cutoff : Nat)
    (visit : ∃ z t, Allowed z ∧ cutoff ≤ t ∧ iter f t z=q) :
    ∃ w, (∃ z, Allowed z ∧ iter f cutoff z=w) ∧ ∃ d, iter f d w=q := by
  obtain ⟨z,t,hz,ht,hit⟩ := visit
  obtain ⟨d,rfl⟩ := Nat.exists_eq_add_of_le ht
  exact ⟨iter f cutoff z, ⟨z,hz,rfl⟩, d, (iter_add f cutoff d z) ▸ hit⟩

/-- An accelerated path records each physical halving exponent. -/
inductive OddPath : List Nat → Nat → Nat → Prop where
  | nil (x : Nat) : OddPath [] x x
  | cons {e x y z : Nat} {rest : List Nat}
      (exponent : 0 < e) (oddIn : x%2=1) (oddOut : y%2=1)
      (edge : 3*x+1=2^e*y) (later : OddPath rest y z) :
      OddPath (e::rest) x z

/-- The all-ones inverse gives a sharp lower bound for every physical inverse
word of the same odd length, with the full additive correction. -/
theorem inverse_length_bound {w : List Nat} {x y : Nat} (path : OddPath w x y) :
    2^w.length*(y+1) ≤ 3^w.length*(x+1) := by
  induction path with
  | nil x => simp
  | @cons e x y z rest pos _ _ edge _ ih =>
    have two : 2 ≤ 2^e := by
      obtain ⟨k,rfl⟩ := Nat.exists_eq_succ_of_ne_zero (by omega : e≠0)
      rw [Nat.pow_succ]
      have := Nat.two_pow_pos k
      omega
    have first := Nat.mul_le_mul_right y two
    have small : 2*(y+1) ≤ 3*(x+1) := by omega
    simp only [List.length_cons, Nat.pow_succ]
    calc
      2^rest.length*2*(z+1) = 2*(2^rest.length*(z+1)) := by ac_rfl
      _ ≤ 2*(3^rest.length*(y+1)) := Nat.mul_le_mul_left _ ih
      _ = 3^rest.length*(2*(y+1)) := by ac_rfl
      _ ≤ 3^rest.length*(3*(x+1)) := Nat.mul_le_mul_left _ small
      _ = 3^rest.length*3*(x+1) := by ac_rfl

private theorem forward_linear_floor {w : List Nat} {x y : Nat} (path : OddPath w x y) :
    3^w.length*x ≤ 2^w.sum*y := by
  induction path with
  | nil x => simp
  | @cons e x y z rest _ _ _ edge _ ih =>
    have small : 3*x ≤ 2^e*y := by omega
    simp only [List.length_cons,List.sum_cons,Nat.pow_succ,Nat.pow_add]
    calc
      3^rest.length*3*x = 3^rest.length*(3*x) := Nat.mul_assoc _ _ _
      _ ≤ 3^rest.length*(2^e*y) := Nat.mul_le_mul_left _ small
      _ = 2^e*(3^rest.length*y) := by ac_rfl
      _ ≤ 2^e*(2^rest.sum*z) := Nat.mul_le_mul_left _ ih
      _ = 2^e*2^rest.sum*z := by ac_rfl

/-- A variable forward word on the original arm transports the allowed
source ratio with its exact homogeneous factor, regardless of the carry. -/
theorem merger_source_scale {w : List Nat} {q y z P Q : Nat} (path : OddPath w q y)
    (budget : Q*z ≤ P*q) :
    3^w.length*(Q*z) ≤ P*(2^w.sum*y) := by
  calc
    3^w.length*(Q*z) ≤ 3^w.length*(P*q) := Nat.mul_le_mul_left _ budget
    _ = P*(3^w.length*q) := by ac_rfl
    _ ≤ P*(2^w.sum*y) := Nat.mul_le_mul_left _ (forward_linear_floor path)

/-- Equality at the all-ones word gives its exact physical repayment digits
and imposes an absolute bound on their number for any proposed smaller start. -/
theorem ones_floor {b x y floor : Nat} (path : OddPath (List.replicate b 1) x y)
    (below : x < floor) :
    2^b*(y+1)=3^b*(x+1) ∧ 2^b ∣ x+1 ∧ 2^b ≤ floor := by
  have equation : ∀ {n u v : Nat}, OddPath (List.replicate n 1) u v →
      2^n*(v+1)=3^n*(u+1) := by
    intro n
    induction n with
    | zero => intro u v h; cases h; simp
    | succ n ih =>
      intro u v h
      rw [List.replicate_succ] at h
      cases h with
      | @cons _ _ y _ _ _ _ _ edge later =>
        have he : 2*(y+1) = 3*(u+1) := by simp at edge; omega
        have ht := ih later
        calc
          2^(n+1)*(v+1) = 2*(2^n*(v+1)) := by rw [Nat.pow_succ]; ac_rfl
          _ = 2*(3^n*(y+1)) := by rw [ht]
          _ = 3^n*(2*(y+1)) := by ac_rfl
          _ = 3^(n+1)*(u+1) := by rw [he,Nat.pow_succ,Nat.mul_assoc]
  have he := equation path
  have cp := (((by decide : Nat.Coprime 2 3).pow_left b).pow_right b)
  have hd : 2^b ∣ x+1 := cp.dvd_of_dvd_mul_left ⟨y+1,he.symm⟩
  exact ⟨he,hd,Nat.le_trans (Nat.le_of_dvd (by omega) hd) (by omega)⟩

/-- With at least b bits of scale already paid, b further inverse odd steps
cannot recover the old minimum, even after arbitrary choices of those gaps. -/
theorem no_same_precision_repayment {w : List Nat} {x z m b : Nat}
    (path : OddPath w m z) (length : w.length=b+1)
    (large : 52 ≤ x) (paid : 2^(b+1)*(x-13) ≤ z) : x ≤ m := by
  have hb := inverse_length_bound path
  rw [length] at hb
  have pw : 3^b ≤ 4^b := Nat.pow_le_pow_left (by decide) b
  have identity : 2^(b+1)*2^(b+1) = 4^(b+1) := by
    rw [← Nat.mul_pow]
  have low : 4*(x-13) ≥ 3*x := by omega
  have comp : 3^(b+1)*x ≤ 4^(b+1)*(x-13) := by
    simp only [Nat.pow_succ,Nat.mul_assoc]
    exact Nat.le_trans (Nat.mul_le_mul_right _ pw) (Nat.mul_le_mul_left _ low)
  have lower : 4^(b+1)*(x-13) < 2^(b+1)*(z+1) := by
    rw [← identity,Nat.mul_assoc]
    exact Nat.mul_lt_mul_of_pos_left (by omega) (Nat.two_pow_pos _)
  have hlt := Nat.lt_of_le_of_lt comp (Nat.lt_of_lt_of_le lower hb)
  exact Nat.le_of_lt_succ (Nat.lt_of_mul_lt_mul_left hlt)

#print axioms late_visitor_factor
#print axioms inverse_length_bound
#print axioms merger_source_scale
#print axioms ones_floor
#print axioms no_same_precision_repayment
end Repayment
