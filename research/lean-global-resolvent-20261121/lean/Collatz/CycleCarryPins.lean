import Collatz.CycleCarryRealization

set_option autoImplicit false
set_option maxHeartbeats 2000000
set_option maxRecDepth 2000

namespace CollatzCycleCarryPins

open CollatzTerminalCarry CollatzCycleCarry CollatzCycleCarryRealization

theorem minus_seven_cycle : SignedPath (-7) 3 2 (-7) := by
  apply SignedPath.odd (by decide)
  change SignedPath (-10) 2 1 (-7)
  apply SignedPath.even (by decide)
  change SignedPath (-5) 1 1 (-7)
  apply SignedPath.odd (by decide)
  change SignedPath (-7) 0 0 (-7)
  exact SignedPath.done _

theorem minus_seven_cycles (q : Nat) : SignedPath (-7) (3*q) (2*q) (-7) := by
  induction q with
  | zero => exact SignedPath.done _
  | succ q ih =>
    have result := signed_path_append minus_seven_cycle ih
    simpa only [show 3+3*q=3*(q+1) by omega,
      show 2+2*q=2*(q+1) by omega] using result

theorem minus_eighty_one_to_seven : SignedPath (-81) 13 6 (-7) := by
  apply SignedPath.odd (by decide)
  change SignedPath (-121) 12 5 (-7)
  apply SignedPath.odd (by decide)
  change SignedPath (-181) 11 4 (-7)
  apply SignedPath.odd (by decide)
  change SignedPath (-271) 10 3 (-7)
  apply SignedPath.odd (by decide)
  change SignedPath (-406) 9 2 (-7)
  apply SignedPath.even (by decide)
  change SignedPath (-203) 8 2 (-7)
  apply SignedPath.odd (by decide)
  change SignedPath (-304) 7 1 (-7)
  apply SignedPath.even (by decide)
  change SignedPath (-152) 6 1 (-7)
  apply SignedPath.even (by decide)
  change SignedPath (-76) 5 1 (-7)
  apply SignedPath.even (by decide)
  change SignedPath (-38) 4 1 (-7)
  apply SignedPath.even (by decide)
  change SignedPath (-19) 3 1 (-7)
  apply SignedPath.odd (by decide)
  change SignedPath (-28) 2 0 (-7)
  apply SignedPath.even (by decide)
  change SignedPath (-14) 1 0 (-7)
  apply SignedPath.even (by decide)
  change SignedPath (-7) 0 0 (-7)
  exact SignedPath.done _

private theorem general_last_two {K : Int} (E : Nat)
    (nonzero : K*(2:Int)^E≠5) :
    Program 1 (K*(2:Int)^(E+2)-21) 2 (K*(2:Int)^E-5) := by
  have power : (2:Int)^(E+2)=4*(2:Int)^E := by
    have value := Int.pow_add (2:Int) E 2
    simp only [show (2:Int)^2=4 by decide] at value
    omega
  have high : K*(2:Int)^(E+2)=4*(K*(2:Int)^E) := by rw [power]; grind
  apply Program.odd (by rw [high]; omega)
  have half : (K*(2:Int)^(E+2)-21+(3:Int)^0)/2=
      2*(K*(2:Int)^E)-10 := by rw [high]; simp; omega
  rw [half]
  apply Program.even (by omega) (by omega)
  have half2 : (2*(K*(2:Int)^E)-10)/2=K*(2:Int)^E-5 := by omega
  rw [half2]
  exact Program.done _

/-- A whole affine coefficient language shares the same exact signed-cycle
compiler, provided its high bit survives to the last carried odd step. -/
theorem general_pin_program {K : Int} (q E : Nat)
    (primitive : K%3≠0) (nonzero : K*(2:Int)^E≠5) :
    Program (2*q+7)
      (K*(2:Int)^(3*q+15+E)-81*(3:Int)^(2*q+7))
      (3*q+15) (K*(2:Int)^E-5) := by
  have path := signed_path_append minus_eighty_one_to_seven (minus_seven_cycles q)
  have tail : Program 1 ((3:Int)^1*(-7)+(2:Int)^(E+2)*K) 2
      (K*(2:Int)^E-5) := by
    have eq : (3:Int)^1*(-7)+(2:Int)^(E+2)*K=K*(2:Int)^(E+2)-21 := by grind
    rw [eq]
    exact general_last_two E nonzero
  have result := lift_pin_program path (by decide : 0<1) primitive (E := E+2) tail
  rw [show 6+2*q+1=2*q+7 by omega,
    show (13+3*q)+(E+2)=3*q+15+E by omega,
    show (13+3*q)+2=3*q+15 by omega] at result
  have eq : (3:Int)^(2*q+7)*(-81)+(2:Int)^(3*q+15+E)*K=
      K*(2:Int)^(3*q+15+E)-81*(3:Int)^(2*q+7) := by grind
  rw [eq] at result
  exact result

def tailCoefficient (v : List Nat) : Int := carry v+81*(3:Int)^(v.length+1)

theorem tail_coefficient_primitive (v : List Nat) : tailCoefficient v%3≠0 := by
  have unit := carry_unit v
  unfold tailCoefficient
  omega

/-- An arbitrary supplied suffix is retained exactly; only the repeated
signed-cycle prefix is summarized by its affine center. -/
theorem repeated_prefix_carry (k : Nat) (v : List Nat) :
    carry (repeatedPin k++v)=
      tailCoefficient v*(2:Int)^(11*k)-81*(3:Int)^(7*k+v.length+1) := by
  have corrNat := repeated_correction k
  have corr := congrArg (fun n : Nat => (n:Int)) corrNat
  simp only [Int.natCast_add,Int.natCast_mul,Int.natCast_pow] at corr
  unfold tailCoefficient carry
  rw [List.length_append,repeated_length,total_append,repeated_total,
    correction_append,repeated_total]
  simp only [Int.natCast_add,Int.natCast_mul,Int.natCast_pow]
  have pw2 : (2:Int)^(11*k+total v+1)=
      (2:Int)^(11*k)*(2:Int)^(total v+1) := by
    simpa only [show 11*k+(total v+1)=11*k+total v+1 by omega] using
      (Int.pow_add (2:Int) (11*k) (total v+1))
  have pw3 : (3:Int)^(7*k+v.length+1)=
      (3:Int)^(7*k)*(3:Int)^(v.length+1) := by
    simpa only [show 7*k+(v.length+1)=7*k+v.length+1 by omega] using
      (Int.pow_add (3:Int) (7*k) (v.length+1))
  have p3 : (3:Int)^(v.length+1)=3*(3:Int)^v.length := by
    rw [Int.pow_succ]
    omega
  rw [pw2,pw3,p3]
  grind

/-- The precise whole-prefix pin guard. The denominator and binary horizon
are independent constraints; the theorem does not drop either one. -/
theorem repeated_prefix_program {k q E : Nat} {v : List Nat}
    (denominator : 7*k+v.length+1=2*q+7)
    (horizon : 11*k=3*q+15+E)
    (nonzero : tailCoefficient v*(2:Int)^E≠5) :
    Program ((repeatedPin k++v).length+1) (carry (repeatedPin k++v))
      (3*q+15) (tailCoefficient v*(2:Int)^E-5) := by
  rw [List.length_append,repeated_length,denominator,repeated_prefix_carry,
    denominator,horizon]
  exact general_pin_program q E (tail_coefficient_primitive v) nonzero

/-- Under the full pin horizon, any -1 carry debt beyond two belongs to the
literal retained suffix. Repeating this cycle cannot create it by itself. -/
theorem minus_one_debt_localizes_to_suffix {k q E : Nat} {v : List Nat}
    (horizon : 11*k=3*q+15+E)
    (minusOne : tailCoefficient v*(2:Int)^E-5=(-1:Int)) :
    total (repeatedPin k++v)≤(3*q+15)+total v+2 := by
  have bound := minus_five_pin_exact minusOne
  rw [total_append,repeated_total,horizon]
  rcases bound with h | h | h <;> omega

end CollatzCycleCarryPins
