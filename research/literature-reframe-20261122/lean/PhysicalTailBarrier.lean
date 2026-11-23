import MarkedDyadicTransport

/-!
An ordinary, positive obstruction to a bounded continuation of rising-prefix
erasure. All statements keep the continuation budget explicit. No statement
excludes mergers at larger clocks or asserts a Collatz counterexample.
-/

namespace CollatzShell.PhysicalTailBarrier

open ForwardSection

/-- The +1 coordinate makes every finite ordinary history a power-of-three
term plus a uniformly bounded nonnegative correction. -/
theorem shifted_affine (n t : Nat) : ∃ p D,
    p≤t ∧ (0<t → n%2=0 → p<t) ∧ D<3^t ∧
    2^t*(orbit t n+1)=3^p*(n+1)+D := by
  induction t generalizing n with
  | zero => exact ⟨0,0,by omega,by omega,by decide,by simp [orbit]⟩
  | succ t ih =>
    obtain ⟨p,D,pt,_,Db,eq⟩ := ih (step n)
    have powpos : 0<3^t := by positivity
    have next : 2^(t+1)*(orbit (t+1) n+1)=
        3^p*(2*(step n+1))+2*D := by
      change 2^(t+1)*(orbit t (step n)+1)=_
      rw [pow_succ]
      nlinarith [eq]
    by_cases even : n%2=0
    · have st : 2*(step n+1)=n+2 := by simp [step,even]; omega
      have pp : 3^p≤3^t := Nat.pow_le_pow_right (by decide) pt
      refine ⟨p,3^p+2*D,by omega,by omega,?_,?_⟩
      · rw [pow_succ]; omega
      · rw [next,st]; ring
    · have odd : n%2=1 := by omega
      have st : 2*(step n+1)=3*(n+1) := by simp [step,odd]; omega
      refine ⟨p+1,2*D,by omega,by omega,?_,?_⟩
      · rw [pow_succ]; omega
      · rw [next,st,pow_succ]; ring

private theorem unique_two_three {a b c d : Nat}
    (eq : 2^a*3^b=2^c*3^d) : a=c ∧ b=d := by
  have twos := congrArg (fun n : Nat => n.factorization 2) eq
  have threes := congrArg (fun n : Nat => n.factorization 3) eq
  norm_num [Nat.factorization_mul, Nat.factorization_pow,
    Nat.prime_two.factorization, Nat.prime_three.factorization] at twos threes
  exact ⟨twos,threes⟩

private theorem maximal_tail (A t : Nat) (divides : 2^(t+1) ∣ A+1) :
    2^(t+1)*(orbit (t+1) (A-1)+1)=3^t*(A+1) := by
  obtain ⟨v,eq⟩ := divides
  have vp : 0<v := by
    by_contra h
    have vz : v=0 := by omega
    rw [vz,Nat.mul_zero] at eq
    omega
  have hp : 0<2^t*v := by positivity
  have form : A-1=2*(2^t*v-1) := by
    rw [pow_succ] at eq
    have reorder : 2^t*2*v=2*(2^t*v) := by ring
    rw [reorder] at eq
    omega
  change 2^(t+1)*(orbit t (step (A-1))+1)=_
  rw [form,step_double,(odd_run t v vp).1]
  have pp : 0<3^t*v := by positivity
  rw [Nat.sub_add_cancel (by omega : 1≤3^t*v),eq]
  ring

/-- The actual tail from A-1 has as many odd steps as possible after its
first even step, for every clock within the supplied binary precision. -/
theorem maximal_tail_affine (A H a : Nat) (positive : 0<A)
    (phase : 2^H ∣ A+1) (ah : a≤H) :
    ∃ D, D<3^a ∧ 2^a*(orbit a (A-1)+1)=3^(a-1)*A+D := by
  cases a with
  | zero =>
    refine ⟨0,by decide,?_⟩
    simp [orbit]
    omega
  | succ t =>
    have div := (Nat.pow_dvd_pow 2 ah).trans phase
    have eq := maximal_tail A t div
    refine ⟨3^t,?_,?_⟩
    · rw [pow_succ]
      have pp : 0<3^t := by positivity
      omega
    · simpa [Nat.mul_add] using eq

private theorem weighted_correction {H s t D : Nat}
    (sh : s≤H) (th : t≤H) (db : D<3^t) : 2^s*D<6^H := by
  calc
    2^s*D<2^s*3^t := Nat.mul_lt_mul_of_pos_left db (by positivity)
    _≤2^H*3^H := Nat.mul_le_mul
      (Nat.pow_le_pow_right (by decide) sh) (Nat.pow_le_pow_right (by decide) th)
    _=6^H := by rw [← mul_pow]; norm_num

private theorem radix_coefficients {B L R c d : Nat}
    (cb : c<B) (db : d<B) (eq : B*L+c=B*R+d) : L=R := by
  have bp : 0<B := by omega
  have div := congrArg (fun n : Nat => n/B) eq
  simpa only [Nat.mul_add_div bp, Nat.div_eq_of_lt cb, Nat.div_eq_of_lt db,
    Nat.add_zero] using div

/-- All positive ternary rescalings are excluded simultaneously, with
different continuation clocks allowed on the two sides. -/
theorem bounded_tail_separation {H A B r a b : Nat}
    (phase : 2^H ∣ A+1) (scale : A=3^r*B) (rp : 0<r)
    (odd : B%2=1) (large : 6^H<B) (ah : a≤H) (bh : b≤H) :
    orbit a (A-1)≠orbit b (B-1) := by
  have bp : 0<B := by omega
  have ap : 0<A := by rw [scale]; positivity
  obtain ⟨Da,Dab,aeq⟩ := maximal_tail_affine A H a ap phase ah
  obtain ⟨p,Db,pb,even,DbB,beq⟩ := shifted_affine (B-1) b
  have first : (B-1)%2=0 := by omega
  have count : p≤b-1 := by
    by_cases z : b=0
    · omega
    · have := even (by omega) first; omega
  have cancel : B-1+1=B := by omega
  rw [cancel] at beq
  intro meet
  have cross : B*(2^b*3^(a-1+r))+2^b*Da = B*(2^a*3^p)+2^a*Db := by
    have term : 3^(a-1)*A=3^(a-1+r)*B := by rw [scale,pow_add]; ring
    rw [term] at aeq
    have multA := congrArg (fun z : Nat => 2^b*z) aeq
    have multB := congrArg (fun z : Nat => 2^a*z) beq
    rw [meet] at multA
    nlinarith [multA,multB]
  have smallA : 2^b*Da<B := (weighted_correction bh ah Dab).trans large
  have smallB : 2^a*Db<B := (weighted_correction ah bh DbB).trans large
  have coeff := radix_coefficients smallA smallB cross
  obtain ⟨clocks,odds⟩ := unique_two_three coeff
  omega

/-- Source form for erasing any positive number of bits from a complete
rising run. This excludes only bounded post-run continuations. -/
theorem bounded_erasure_no_meeting {H k u r a b : Nat}
    (phase : 2^H ∣ 3^k*u+1) (odd : u%2=1) (large : 6^H<u)
    (rp : 0<r) (rk : r≤k) (ah : a≤H) (bh : b≤H) :
    orbit (k+a) (2^k*u-1)≠orbit (k-r+b) (2^(k-r)*u-1) := by
  have up : 0<u := by omega
  rw [orbit_add,orbit_add,(odd_run k u up).1,(odd_run (k-r) u up).1]
  apply bounded_tail_separation phase (r:=r) ?_ rp ?_ ?_ ah bh
  · rw [← Nat.mul_assoc,← pow_add]
    congr 2
    omega
  · simp [Nat.mul_mod,Nat.pow_mod,odd]
  · have pp : 1≤3^(k-r) := Nat.one_le_pow _ _ (by decide)
    have := Nat.mul_le_mul_right u pp
    omega

#print axioms shifted_affine
#print axioms maximal_tail_affine
#print axioms bounded_tail_separation
#print axioms bounded_erasure_no_meeting

end CollatzShell.PhysicalTailBarrier
