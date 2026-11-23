module

public import FixedBlockDenominator

@[expose] public section

/-!
# Physical arithmetic for independently repeated cycle blocks

The signed pin block P=[1,1,4,1,1,1,2] and Q=[2] may have independent
positive repetition counts m,n. These declarations prove the complete
integer equation and exclude the entire cone n>=m. The remaining n<m
case is excluded in the accompanying written Matveev/continued-fraction
argument; no logarithmic lower-bound hypothesis is installed here.
-/

namespace CollatzIndependentPins

open CollatzFixedBlock

theorem full_pin_divisibility (m x y : Nat)
    (pin : 2048^m*(y+41)=2187^m*(x+41)) : 2048^m ∣ x+41 := by
  have divprod : 2048^m ∣ 2187^m*(x+41) := by
    rw [← pin]
    exact dvd_mul_right _ _
  have cop : Nat.Coprime (2048^m) (2187^m) :=
    ((by decide : Nat.Coprime 2048 2187).pow_left m).pow_right m
  exact cop.dvd_of_dvd_mul_left divprod

theorem independent_cross_identity (m n x y : Nat)
    (pin : 2048^m*(y+41)=2187^m*(x+41))
    (twos : 4^n*x+3^n=3^n*y+4^n) :
    2048^m*4^n*x+42*2048^m*3^n =
      2187^m*3^n*x+2048^m*4^n+41*2187^m*3^n := by
  have hp := congrArg (fun z : Nat => 3^n*z) pin
  have hq := congrArg (fun z : Nat => 2048^m*z) twos
  nlinarith only [hp,hq]

private theorem diagonal_ratio (m : Nat) (hm : 0<m) :
    8192*6561^m≤6561*8192^m := by
  have rem := Nat.pow_le_pow_left (by decide : 6561≤8192) (m-1)
  calc
    8192*6561^m=(8192*6561)*6561^(m-1) := by
      conv_lhs => rw [show m=1+(m-1) by omega,pow_add]
      ring
    _ ≤(8192*6561)*8192^(m-1) := Nat.mul_le_mul_left _ rem
    _ =6561*8192^m := by
      conv_rhs => rw [show m=1+(m-1) by omega,pow_add]
      ring

theorem independent_ratio_bound (m n : Nat) (hm : 0<m) (hmn : m≤n) :
    8192*(2187^m*3^n)≤6561*(2048^m*4^n) := by
  have hd := diagonal_ratio m hm
  have hr := Nat.pow_le_pow_left (by decide : 3≤4) (n-m)
  have b : 2187^m*3^n=6561^m*3^(n-m) := by
    rw [show n=m+(n-m) by omega,pow_add]
    rw [← Nat.mul_assoc,← mul_pow]
    norm_num
  have a : 2048^m*4^n=8192^m*4^(n-m) := by
    rw [show n=m+(n-m) by omega,pow_add]
    rw [← Nat.mul_assoc,← mul_pow]
    norm_num
  rw [a,b]
  calc
    8192*(6561^m*3^(n-m))=(8192*6561^m)*3^(n-m) := by ring
    _ ≤(6561*8192^m)*3^(n-m) := Nat.mul_le_mul_right _ hd
    _ ≤(6561*8192^m)*4^(n-m) := Nat.mul_le_mul_left _ hr
    _ =6561*(8192^m*4^(n-m)) := by ring

theorem no_independent_cycle_of_twos_ge_pins (m n x y : Nat)
    (hm : 0<m) (hmn : m≤n)
    (pin : 2048^m*(y+41)=2187^m*(x+41))
    (twos : 4^n*x+3^n=3^n*y+4^n) : False := by
  have eqn := independent_cross_identity m n x y pin twos
  have ratio := independent_ratio_bound m n hm hmn
  have large := pin_source_large m x y hm pin
  have ap : 0<2048^m*4^n := by positivity
  have coeff : 2187^m*3^n≤2048^m*4^n := by
    nlinarith only [ratio,ap]
  have deq := Nat.sub_add_cancel coeff
  have dx := congrArg (fun z : Nat => z*x) deq
  have d170 := congrArg (fun z : Nat => z*170) deq
  have lower := Nat.mul_le_mul_left (2048^m*4^n-2187^m*3^n)
    (show 170≤x by omega)
  have nonneg : 0≤2048^m*3^n := Nat.zero_le _
  have cap : 169*(2048^m*4^n)≤211*(2187^m*3^n) := by
    nlinarith only [eqn,dx,d170,lower,nonneg]
  nlinarith only [cap,ratio,ap]

theorem independent_integer_quotient (m n x y : Nat) (hn : 0<n)
    (pin : 2048^m*(y+41)=2187^m*(x+41))
    (twos : 4^n*x+3^n=3^n*y+4^n) :
    ∃ t : Nat, 0<t ∧ x+41=2048^m*t ∧
      3^(7*m+n)<2^(11*m+2*n) ∧
      (2^(11*m+2*n)-3^(7*m+n))*t=42*(4^n-3^n) := by
  obtain ⟨t,ht⟩ := full_pin_divisibility m x y pin
  have tp : 0<t := by
    by_contra h
    have tz : t=0 := by omega
    simp only [tz,Nat.mul_zero] at ht
    omega
  have ap : 0<2048^m := by positivity
  have hy : y+41=2187^m*t := by
    apply Nat.eq_of_mul_eq_mul_left ap
    calc
      2048^m*(y+41)=2187^m*(x+41) := pin
      _ =2048^m*(2187^m*t) := by rw [ht]; ring
  have hx := congrArg (fun z : Nat => 4^n*z) ht
  have hy' := congrArg (fun z : Nat => 3^n*z) hy
  have eqn : (2048^m*4^n)*t+42*3^n=(2187^m*3^n)*t+42*4^n := by
    nlinarith only [twos,hx,hy']
  have cd : 3^n<4^n := Nat.pow_lt_pow_left (by decide : 3<4) (by omega : n≠0)
  have slope : 2187^m*3^n<2048^m*4^n := by
    by_contra h
    have hle : 2048^m*4^n≤2187^m*3^n := by omega
    have hmul := Nat.mul_le_mul_right t hle
    nlinarith only [eqn,cd,hmul]
  have e : (2048^m*4^n-2187^m*3^n)*t=42*(4^n-3^n) := by
    have h1 := Nat.sub_add_cancel (Nat.le_of_lt slope)
    have h2 := Nat.sub_add_cancel (Nat.le_of_lt cd)
    nlinarith only [eqn,h1,h2]
  have pow2 : 2048^m*4^n=2^(11*m+2*n) := by
    rw [pow_add,pow_mul,pow_mul]
    norm_num
  have pow3 : 2187^m*3^n=3^(7*m+n) := by
    rw [pow_add,pow_mul]
    norm_num
  exact ⟨t,tp,ht,by simpa only [pow2,pow3] using slope,
    by simpa only [pow2,pow3] using e⟩

/-- The full ordinary gap-path bridge for independent exponents. -/
theorem independent_gap_cycle_necessary (m n x y : Nat) (hm : 0<m) (hn : 0<n)
    (pin : BlockPath pinWord m x y) (twos : BlockPath [2] n y x) :
    n<m ∧ ∃ t : Nat, 0<t ∧ x+41=2048^m*t ∧
      3^(7*m+n)<2^(11*m+2*n) ∧
      (2^(11*m+2*n)-3^(7*m+n))*t=42*(4^n-3^n) := by
  have hp := repeated_pin_identity m x y pin
  have hq := repeated_twos_identity n y x twos
  constructor
  · by_contra h
    exact no_independent_cycle_of_twos_ge_pins m n x y hm (by omega) hp hq
  · exact independent_integer_quotient m n x y hn hp hq

#print axioms full_pin_divisibility
#print axioms independent_cross_identity
#print axioms independent_ratio_bound
#print axioms no_independent_cycle_of_twos_ge_pins
#print axioms independent_integer_quotient
#print axioms independent_gap_cycle_necessary

end CollatzIndependentPins
