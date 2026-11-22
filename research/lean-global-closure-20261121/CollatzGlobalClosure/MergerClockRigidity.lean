import CollatzGlobalClosure.EndpointSteering
import Init.Data.Nat.Coprime

/-!
# Large-source rigidity for arbitrary ordinary multiplicative mergers

Every source is an ordinary natural number and both clocks are actual
shortcut Collatz clocks.  No convergence premise or prescribed parity word
is used.  Once `n + 2^H > 3^H`, a merger between `n` and `m*n` within clock
`H` forces exact equality of their normalized affine slopes.
-/

set_option autoImplicit false

namespace CollatzMergerClockRigidity

open CollatzEndpointSteering

def correction : Nat → Nat → Nat
  | 0, _ => 0
  | h+1, n => 3^(odds h (step n))*(n%2) + 2*correction h (step n)

theorem odds_le_clock (h n : Nat) : odds h n ≤ h := by
  induction h generalizing n with
  | zero => simp [odds]
  | succ h ih =>
    have := ih (step n)
    simp only [odds]
    omega

private theorem step_numerator (n : Nat) :
    2*step n = 3^(n%2)*n+n%2 := by
  by_cases even : n%2=0
  · simp [step,even]
    omega
  · have odd : n%2=1 := by omega
    simp [step,odd]
    omega

theorem actual_affine_identity (h n : Nat) :
    2^h*orbit h n=3^(odds h n)*n+correction h n := by
  induction h generalizing n with
  | zero => simp [orbit,odds,correction]
  | succ h ih =>
    have old := ih (step n)
    have one := step_numerator n
    simp only [orbit,odds,correction,Nat.pow_add,Nat.pow_one]
    grind

/-- The all-odd numerator is an upper bound for every actual correction.
The added power of two avoids truncated-subtraction conventions. -/
theorem correction_bound (h n : Nat) :
    correction h n+2^h≤3^h := by
  induction h generalizing n with
  | zero => simp [correction]
  | succ h ih =>
    have old := ih (step n)
    have count := odds_le_clock h (step n)
    have powers : 3^(odds h (step n))≤3^h :=
      Nat.pow_le_pow_of_le (by decide) count
    have bit : n%2≤1 := by omega
    have extra := Nat.mul_le_mul_left (3^(odds h (step n))) bit
    simp only [Nat.mul_one] at extra
    simp only [correction,Nat.pow_succ]
    omega

/-- Padding a shorter affine equation to a common clock preserves the same
universal correction budget.  This is equation padding, not orbit padding. -/
theorem padded_correction_bound (h H n : Nat) (clock : h≤H) :
    2^(H-h)*correction h n+2^H≤3^H := by
  have old := Nat.mul_le_mul_left (2^(H-h)) (correction_bound h n)
  have two : 2^(H-h)*2^h=2^H := by
    rw [← Nat.pow_add,Nat.sub_add_cancel clock]
  have scale : 2^(H-h)≤3^(H-h) :=
    Nat.pow_le_pow_left (by decide : 2≤3) (H-h)
  have total := Nat.mul_le_mul_right (3^h) scale
  have three : 3^(H-h)*3^h=3^H := by
    rw [← Nat.pow_add,Nat.sub_add_cancel clock]
  rw [Nat.mul_add,two] at old
  rw [three] at total
  exact Nat.le_trans old total

theorem padded_affine_identity (h H n : Nat) (clock : h≤H) :
    2^H*orbit h n=
      (2^(H-h)*3^(odds h n))*n+2^(H-h)*correction h n := by
  have old := congrArg (fun z => 2^(H-h)*z) (actual_affine_identity h n)
  have two : 2^(H-h)*2^h=2^H := by
    rw [← Nat.pow_add,Nat.sub_add_cancel clock]
  simpa only [Nat.mul_add,← Nat.mul_assoc,two] using old

private theorem small_offsets_force_equal_slopes
    (A B c d n P Q : Nat)
    (identity : A*n+c=B*n+d)
    (leftBudget : c+P≤Q) (rightBudget : d+P≤Q)
    (large : Q<n+P) : A=B := by
  by_cases ab : A<B
  · have gap : A+1≤B := by omega
    have product := Nat.mul_le_mul_right n gap
    rw [Nat.add_mul,Nat.one_mul] at product
    omega
  · by_cases ba : B<A
    · have gap : B+1≤A := by omega
      have product := Nat.mul_le_mul_right n gap
      rw [Nat.add_mul,Nat.one_mul] at product
      omega
    · omega

/-- Every merger with unequal clocks below a shared bound has equal affine
slopes once the source exceeds the exact universal correction budget.
The multiplier is arbitrary, and the actual words can vary with the source. -/
theorem large_source_merger_slopes
    (h t H n m : Nat) (leftClock : h≤H) (rightClock : t≤H)
    (large : 3^H<n+2^H) (meet : orbit h n=orbit t (m*n)) :
    2^(H-h)*3^(odds h n)=m*2^(H-t)*3^(odds t (m*n)) := by
  have left := padded_affine_identity h H n leftClock
  have right := padded_affine_identity t H (m*n) rightClock
  have equation :
      (2^(H-h)*3^(odds h n))*n+2^(H-h)*correction h n=
      (m*2^(H-t)*3^(odds t (m*n)))*n+
        2^(H-t)*correction t (m*n) := by
    calc
      _ = 2^H*orbit h n := left.symm
      _ = 2^H*orbit t (m*n) := by rw [meet]
      _ = _ := by rw [right]; ac_rfl
  exact small_offsets_force_equal_slopes _ _ _ _ _ _ _ equation
    (padded_correction_bound h H n leftClock)
    (padded_correction_bound t H (m*n) rightClock) large

/-- A source with genuinely different slopes pays a pointwise clock cost.
This does not just bound the number or density of such sources. -/
theorem nonresonant_merger_clock_bound
    (h t H n m : Nat) (leftClock : h≤H) (rightClock : t≤H)
    (different : 2^(H-h)*3^(odds h n) ≠
      m*2^(H-t)*3^(odds t (m*n)))
    (meet : orbit h n=orbit t (m*n)) : n+2^H≤3^H := by
  by_cases large : 3^H<n+2^H
  · exact False.elim (different
      (large_source_merger_slopes h t H n m leftClock rightClock large meet))
  · omega

def HasTwoThreeRatio (m : Nat) : Prop :=
  ∃ a b u v, 2^u*3^a=m*2^v*3^b

/-- Every multiplier outside the rational group generated by two and three
obeys the bound, for every source and every pair of ordinary clocks. -/
theorem nonsmooth_multiplier_clock_bound
    (h t H n m : Nat) (leftClock : h≤H) (rightClock : t≤H)
    (nonsmooth : ¬HasTwoThreeRatio m)
    (meet : orbit h n=orbit t (m*n)) : n+2^H≤3^H := by
  apply nonresonant_merger_clock_bound h t H n m leftClock rightClock _ meet
  intro equation
  apply nonsmooth
  exact ⟨odds h n,odds t (m*n),H-h,H-t,equation⟩

theorem padded_slope_bound (h H n : Nat) (clock : h≤H) :
    2^(H-h)*3^(odds h n)≤3^H := by
  have two : 2^(H-h)≤3^(H-h) :=
    Nat.pow_le_pow_left (by decide : 2≤3) (H-h)
  have three : 3^(odds h n)≤3^h :=
    Nat.pow_le_pow_of_le (by decide) (odds_le_clock h n)
  have product := Nat.mul_le_mul two three
  rw [← Nat.pow_add,Nat.sub_add_cancel clock] at product
  exact product

theorem affine_offset_bound (h H n B M : Nat)
    (clock : h≤H) (offset : B≤M) :
    (2^(H-h)*3^(odds h n))*B+2^(H-h)*correction h n+2^H
      ≤3^H*(M+1) := by
  have slope := padded_slope_bound h H n clock
  have product := Nat.mul_le_mul slope offset
  have remainder := padded_correction_bound h H n clock
  rw [Nat.mul_add,Nat.mul_one]
  omega

/-- Arbitrary affine source families, with independent actual clocks.
The universal budget depends on both intercepts and the common clock;
the leading coefficients and the words may be arbitrary. -/
theorem large_affine_pair_merger_slopes
    (h t H n A B C D : Nat)
    (leftClock : h≤H) (rightClock : t≤H)
    (large : 3^H*(max B D+1)<n+2^H)
    (meet : orbit h (A*n+B)=orbit t (C*n+D)) :
    (2^(H-h)*3^(odds h (A*n+B)))*A=
      (2^(H-t)*3^(odds t (C*n+D)))*C := by
  have left := padded_affine_identity h H (A*n+B) leftClock
  have right := padded_affine_identity t H (C*n+D) rightClock
  have equation :
      ((2^(H-h)*3^(odds h (A*n+B)))*A)*n+
        ((2^(H-h)*3^(odds h (A*n+B)))*B+
          2^(H-h)*correction h (A*n+B))=
      ((2^(H-t)*3^(odds t (C*n+D)))*C)*n+
        ((2^(H-t)*3^(odds t (C*n+D)))*D+
          2^(H-t)*correction t (C*n+D)) := by
    calc
      _ = 2^H*orbit h (A*n+B) := by rw [left]; grind
      _ = 2^H*orbit t (C*n+D) := by rw [meet]
      _ = _ := by rw [right]; grind
  exact small_offsets_force_equal_slopes _ _ _ _ _ _ _ equation
    (affine_offset_bound h H (A*n+B) B (max B D) leftClock (Nat.le_max_left _ _))
    (affine_offset_bound t H (C*n+D) D (max B D) rightClock (Nat.le_max_right _ _))
    large

theorem nonresonant_affine_pair_clock_bound
    (h t H n A B C D : Nat)
    (leftClock : h≤H) (rightClock : t≤H)
    (different : (2^(H-h)*3^(odds h (A*n+B)))*A ≠
      (2^(H-t)*3^(odds t (C*n+D)))*C)
    (meet : orbit h (A*n+B)=orbit t (C*n+D)) :
    n+2^H≤3^H*(max B D+1) := by
  by_cases large : 3^H*(max B D+1)<n+2^H
  · exact False.elim (different
      (large_affine_pair_merger_slopes h t H n A B C D leftClock rightClock large meet))
  · omega

def TwoThreeResonant (A C : Nat) : Prop :=
  ∃ a b u v, (2^u*3^a)*A=(2^v*3^b)*C

/-- A purely arithmetic test on the two fixed leading coefficients gives
the same all-source lower bound without specifying either parity word. -/
theorem nonsmooth_affine_pair_clock_bound
    (h t H n A B C D : Nat)
    (leftClock : h≤H) (rightClock : t≤H)
    (nonsmooth : ¬TwoThreeResonant A C)
    (meet : orbit h (A*n+B)=orbit t (C*n+D)) :
    n+2^H≤3^H*(max B D+1) := by
  apply nonresonant_affine_pair_clock_bound h t H n A B C D leftClock rightClock _ meet
  intro equation
  apply nonsmooth
  exact ⟨odds h (A*n+B),odds t (C*n+D),H-h,H-t,equation⟩

/-- Parameter lifting preserves each actual finite word, including arbitrary
nonnegative affine intercepts and a clock shorter than the common period. -/
theorem affine_parameter_lift
    (h H n A B z : Nat) (clock : h≤H) :
    orbit h (A*(n+2^H*z)+B)=
      ((2^(H-h)*3^(odds h (A*n+B)))*A)*z+orbit h (A*n+B) := by
  have power : 2^h*2^(H-h)=2^H := by
    rw [← Nat.pow_add,Nat.add_sub_of_le clock]
  have form : A*(n+2^H*z)+B=2^h*(2^(H-h)*A*z)+(A*n+B) := by
    rw [← power]
    grind
  rw [form,orbit_shift]
  ac_rfl

/-- An entire binary parameter ray is a genuine common-future family
exactly when one merger and its actual affine slope equality hold. -/
theorem affine_merger_ray_iff
    (h t H n A B C D : Nat)
    (leftClock : h≤H) (rightClock : t≤H) :
    (∀ z, orbit h (A*(n+2^H*z)+B)=orbit t (C*(n+2^H*z)+D)) ↔
      orbit h (A*n+B)=orbit t (C*n+D) ∧
      (2^(H-h)*3^(odds h (A*n+B)))*A=
        (2^(H-t)*3^(odds t (C*n+D)))*C := by
  constructor
  · intro all
    have base := all 0
    simp only [Nat.mul_zero,Nat.add_zero] at base
    have next := all 1
    rw [affine_parameter_lift h H n A B 1 leftClock,
      affine_parameter_lift t H n C D 1 rightClock] at next
    simp only [Nat.mul_one] at next
    exact ⟨base,by omega⟩
  · rintro ⟨base,slope⟩ z
    rw [affine_parameter_lift h H n A B z leftClock,
      affine_parameter_lift t H n C D z rightClock,slope,base]

/-- One sufficiently large observed ordinary merger automatically certifies
an infinite actual arithmetic family at the same independent clocks.
The input threshold rules out an accidental isolated affine crossing. -/
theorem large_merger_propagates
    (h t H n A B C D : Nat)
    (leftClock : h≤H) (rightClock : t≤H)
    (large : 3^H*(max B D+1)<n+2^H)
    (meet : orbit h (A*n+B)=orbit t (C*n+D)) :
    ∀ z, orbit h (A*(n+2^H*z)+B)=orbit t (C*(n+2^H*z)+D) := by
  apply (affine_merger_ray_iff h t H n A B C D leftClock rightClock).mpr
  exact ⟨meet,large_affine_pair_merger_slopes h t H n A B C D
    leftClock rightClock large meet⟩

/-- The same large-source certificate covers the complete nonnegative
parameter residue class, including its members below the observed point. -/
theorem large_merger_covers_residue_class
    (h t H n A B C D : Nat)
    (leftClock : h≤H) (rightClock : t≤H)
    (large : 3^H*(max B D+1)<n+2^H)
    (meet : orbit h (A*n+B)=orbit t (C*n+D)) :
    ∀ z, orbit h (A*(n%2^H+2^H*z)+B)=
      orbit t (C*(n%2^H+2^H*z)+D) := by
  let r := n%2^H
  let q := n/2^H
  have decomposition : n=r+2^H*q := (Nat.mod_add_div n (2^H)).symm
  have base := meet
  rw [decomposition,
    affine_parameter_lift h H r A B q leftClock,
    affine_parameter_lift t H r C D q rightClock] at base
  have next := large_merger_propagates h t H n A B C D
    leftClock rightClock large meet 1
  simp only [Nat.mul_one] at next
  have nextForm : n+2^H=r+2^H*(q+1) := by rw [decomposition]; grind
  rw [nextForm,
    affine_parameter_lift h H r A B (q+1) leftClock,
    affine_parameter_lift t H r C D (q+1) rightClock] at next
  simp only [Nat.mul_add,Nat.mul_one] at next
  have slope : (2^(H-h)*3^(odds h (A*r+B)))*A=
      (2^(H-t)*3^(odds t (C*r+D)))*C := by omega
  rw [slope] at base
  apply (affine_merger_ray_iff h t H r A B C D leftClock rightClock).mpr
  exact ⟨by omega,slope⟩

theorem multiplier_not_resonant_of_coprime_divisor
    (m d : Nat) (nontrivial : 1<d) (factor : d∣m)
    (two : Nat.Coprime d 2) (three : Nat.Coprime d 3) :
    ¬HasTwoThreeRatio m := by
  rintro ⟨a,b,u,v,equation⟩
  have coprime : Nat.Coprime d (2^u*3^a) :=
    (two.pow_right u).mul_right (three.pow_right a)
  have divides : d∣2^u*3^a := by
    obtain ⟨k,factor⟩ := factor
    refine ⟨k*2^v*3^b,?_⟩
    rw [equation,factor]
    ac_rfl
  have := coprime.eq_one_of_dvd divides
  omega

theorem coprime_factor_multiplier_clock_bound
    (h t H n m d : Nat) (leftClock : h≤H) (rightClock : t≤H)
    (nontrivial : 1<d) (factor : d∣m)
    (two : Nat.Coprime d 2) (three : Nat.Coprime d 3)
    (meet : orbit h n=orbit t (m*n)) : n+2^H≤3^H :=
  nonsmooth_multiplier_clock_bound h t H n m leftClock rightClock
    (multiplier_not_resonant_of_coprime_divisor m d nontrivial factor two three) meet

/-- In particular every proposed universal multiplication-by-five merger
must allow clocks increasing at least logarithmically with the source. -/
theorem five_merger_clock_bound
    (h t H n : Nat) (leftClock : h≤H) (rightClock : t≤H)
    (meet : orbit h n=orbit t (5*n)) : n+2^H≤3^H := by
  exact coprime_factor_multiplier_clock_bound h t H n 5 5 leftClock rightClock
    (by decide) (Nat.dvd_refl _) (by decide) (by decide) meet

theorem affine_not_resonant_of_coprime_divisor
    (A C d : Nat) (nontrivial : 1<d) (factor : d∣C)
    (leftCoefficient : Nat.Coprime d A)
    (two : Nat.Coprime d 2) (three : Nat.Coprime d 3) :
    ¬TwoThreeResonant A C := by
  rintro ⟨a,b,u,v,equation⟩
  have coprime : Nat.Coprime d ((2^u*3^a)*A) :=
    ((two.pow_right u).mul_right (three.pow_right a)).mul_right leftCoefficient
  have divides : d∣(2^u*3^a)*A := by
    obtain ⟨k,factor⟩ := factor
    refine ⟨(2^v*3^b)*k,?_⟩
    rw [equation,factor]
    ac_rfl
  have := coprime.eq_one_of_dvd divides
  omega

theorem coprime_factor_affine_pair_clock_bound
    (h t H n A B C D d : Nat)
    (leftClock : h≤H) (rightClock : t≤H)
    (nontrivial : 1<d) (factor : d∣C)
    (leftCoefficient : Nat.Coprime d A)
    (two : Nat.Coprime d 2) (three : Nat.Coprime d 3)
    (meet : orbit h (A*n+B)=orbit t (C*n+D)) :
    n+2^H≤3^H*(max B D+1) :=
  nonsmooth_affine_pair_clock_bound h t H n A B C D leftClock rightClock
    (affine_not_resonant_of_coprime_divisor A C d nontrivial factor leftCoefficient
      two three) meet

end CollatzMergerClockRigidity

#print axioms CollatzMergerClockRigidity.odds_le_clock
#print axioms CollatzMergerClockRigidity.actual_affine_identity
#print axioms CollatzMergerClockRigidity.correction_bound
#print axioms CollatzMergerClockRigidity.padded_correction_bound
#print axioms CollatzMergerClockRigidity.padded_affine_identity
#print axioms CollatzMergerClockRigidity.large_source_merger_slopes
#print axioms CollatzMergerClockRigidity.nonresonant_merger_clock_bound
#print axioms CollatzMergerClockRigidity.nonsmooth_multiplier_clock_bound
#print axioms CollatzMergerClockRigidity.padded_slope_bound
#print axioms CollatzMergerClockRigidity.affine_offset_bound
#print axioms CollatzMergerClockRigidity.large_affine_pair_merger_slopes
#print axioms CollatzMergerClockRigidity.nonresonant_affine_pair_clock_bound
#print axioms CollatzMergerClockRigidity.nonsmooth_affine_pair_clock_bound
#print axioms CollatzMergerClockRigidity.affine_parameter_lift
#print axioms CollatzMergerClockRigidity.affine_merger_ray_iff
#print axioms CollatzMergerClockRigidity.large_merger_propagates
#print axioms CollatzMergerClockRigidity.large_merger_covers_residue_class
#print axioms CollatzMergerClockRigidity.multiplier_not_resonant_of_coprime_divisor
#print axioms CollatzMergerClockRigidity.coprime_factor_multiplier_clock_bound
#print axioms CollatzMergerClockRigidity.five_merger_clock_bound
#print axioms CollatzMergerClockRigidity.affine_not_resonant_of_coprime_divisor
#print axioms CollatzMergerClockRigidity.coprime_factor_affine_pair_clock_bound
