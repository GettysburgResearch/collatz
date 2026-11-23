/-
An all-parameter physical forcing theorem joining the dyadic coset argument
to the signed low-block shadow.  The conclusion concerns an actual positive
ordinary Collatz iterate, with its exact clock and low-block borrow bound.
The conversion from a binary-run cap to a sufficiently separated block is
proved as written combinatorics in BINARY_RUN_COMPACTNESS.md.
-/
import Collatz.DyadicCoset
import Collatz.SignedShadow

open CollatzReverseBasin CollatzClosure CollatzWitness
open CollatzUnboundedGapReset CollatzDyadicCoset CollatzSignedShadow

set_option autoImplicit false
set_option maxHeartbeats 2000000

namespace CollatzBinaryRunForcing

/-- The ordinary clock of any actual positive odd trace is at most twice
its odd-event count plus the starting binary length. This keeps the original
ordinary clock when run visits are transferred to an atomic source measure. -/
theorem ordinary_clock_budget (n ell : Nat) (word : List Nat) (endpoint : Int)
    (trace : SignedTrace (n:Int) word endpoint) (height : n<2^ell) :
    total word<2*word.length+ell := by
  apply clock_below_separation trace
  have bound := Nat.mul_lt_mul_of_pos_left height
    (Nat.pow_pos (by decide : 0<4) (n:=word.length))
  have power : 4^word.length*2^ell=2^(2*word.length+ell) := by
    rw [Nat.pow_add,Nat.pow_mul]
  simpa [power] using bound

/-- A wide signed binary gap forces an alternating high-block pattern on
the actual positive orbit, within fewer than 4^s accelerated odd steps.
All signs, positivity, integer endpoints, and ordinary clocks are retained.
No eventual-convergence hypothesis is used for either signed or positive maps. -/
theorem actual_pattern (n u D s : Nat) (z : Int)
    (positive : 0<n) (highOdd : u%2=1) (lowOdd : z%2=1) (capPositive : 0<s)
    (source : (n:Int)=(2:Int)^D*(u:Int)+z)
    (separation : 4^(4^s-1)*z.natAbs<2^D) :
    ∃ word : List Nat, ∃ low : Int,
      SignedTrace z word low ∧ word.length<4^s ∧ total word<D ∧
      0<orbit n (total word) ∧
      (orbit n (total word):Int)=
        (2:Int)^(D-total word)*(3:Int)^word.length*(u:Int)+low ∧
      0<low.natAbs ∧ low.natAbs<2^(D-total word) ∧
      ((3^word.length*u)%2^(2*s+2)=1+8*alternating s ∨
       (3^word.length*u)%2^(2*s+2)=alternating (s+1)) := by
  obtain ⟨j,jb,pattern⟩ := alternating_residue_forcing u s highOdd capPositive
  obtain ⟨word,low,length,trace⟩ := trace_exists z lowOdd j
  have exponent : j≤4^s-1 := by omega
  have power : 4^j≤4^(4^s-1) := Nat.pow_le_pow_right (by decide) exponent
  have small : 4^word.length*z.natAbs<2^D := by
    rw [length]
    exact Nat.lt_of_le_of_lt (Nat.mul_le_mul_right z.natAbs power) separation
  obtain ⟨clock,endpointPositive,value,nonzero,bound⟩ :=
    separated_shadow_certificate trace n u D positive source small
  exact ⟨word,low,trace,by omega,clock,endpointPositive,value,nonzero,bound,
    by simpa [length] using pattern⟩

/-- A convenient binary-exponent sufficient condition for the same forcing.
The entire low block is bounded before any shadow orbit is constructed. -/
theorem actual_pattern_of_gap (n u D s ell : Nat) (z : Int)
    (positive : 0<n) (highOdd : u%2=1) (lowOdd : z%2=1) (capPositive : 0<s)
    (source : (n:Int)=(2:Int)^D*(u:Int)+z)
    (lowBound : z.natAbs<2^ell) (gap : 2*(4^s-1)+ell≤D) :
    ∃ word : List Nat, ∃ low : Int,
      SignedTrace z word low ∧ word.length<4^s ∧ total word<D ∧
      0<orbit n (total word) ∧
      (orbit n (total word):Int)=
        (2:Int)^(D-total word)*(3:Int)^word.length*(u:Int)+low ∧
      0<low.natAbs ∧ low.natAbs<2^(D-total word) ∧
      ((3^word.length*u)%2^(2*s+2)=1+8*alternating s ∨
       (3^word.length*u)%2^(2*s+2)=alternating (s+1)) := by
  apply actual_pattern n u D s z positive highOdd lowOdd capPositive source
  have strict := Nat.mul_lt_mul_of_pos_left lowBound
    (Nat.pow_pos (by decide : 0<4) (n:=4^s-1))
  have combine : 4^(4^s-1)*2^ell=2^(2*(4^s-1)+ell) := by
    rw [Nat.pow_add,Nat.pow_mul]
  rw [combine] at strict
  exact Nat.lt_of_lt_of_le strict (Nat.pow_le_pow_right (by decide) gap)

end CollatzBinaryRunForcing
