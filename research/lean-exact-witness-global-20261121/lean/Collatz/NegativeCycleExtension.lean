/-
Exact all-word arithmetic for the negative rational cycle controls.
The joint-density and continuous-barrier arguments are written mathematics.
These declarations retain the entire numerator and denominator; they do not
assert that a negative rational cycle is a positive integer counterexample.
-/
import Collatz.LowGapLoops

open CollatzWitness CollatzHighGapPump CollatzLowGapLoops

set_option autoImplicit false
set_option maxHeartbeats 2000000

namespace CollatzNegativeCycleExtension

def extension (front : List Nat) (ones last : Nat) : List Nat :=
  front ++ repeatHead 1 ones [last]

/-- The literal appended word, with no length or exponent cutoff. -/
theorem extension_data (front : List Nat) (ones last : Nat) :
    (extension front ones last).length = front.length+ones+1 ∧
    total (extension front ones last) = total front+ones+last ∧
    correction (extension front ones last)+2^(total front+ones+1) =
      3^(ones+1)*(correction front+2^total front) := by
  have tail := ones_correction ones last
  have multiplied := congrArg (2^total front*·) tail
  have len : (repeatHead 1 ones [last]).length = ones+1 := by
    simp [repeatHead_length]
  have clock : total (repeatHead 1 ones [last]) = ones+last := by
    simp [repeatHead_total,total]
  refine ⟨?_,?_,?_⟩
  · simp [extension,List.length_append,len,Nat.add_assoc]
  · simp [extension,total_append,clock,Nat.add_assoc]
  · rw [extension,correction_append,len]
    rw [show total front+ones+1=total front+(ones+1) by omega,Nat.pow_add]
    grind

/-- Clearing the full negative-cycle denominator preserves the complete
initial binary guard, including oddness of the supplied endpoint. -/
theorem extension_binary_guard (front : List Nat) (ones last n endpoint D : Nat)
    (path : Prefix n front endpoint) (odd : endpoint%2=1) (lastPositive : 0<last)
    (denominator : 2^total (extension front ones last)+D =
      3^(extension front ones last).length) :
    2^(total front+1) ∣ correction (extension front ones last)+D*n := by
  obtain ⟨len,clock,numerator⟩ := extension_data front ones last
  rw [len,clock] at denominator
  have edge := path.2
  have cleared :
      correction (extension front ones last)+D*n+
          2^(total front+ones+1)+2^(total front+ones+last)*n =
        2^total front*3^(ones+1)*(endpoint+1) := by
    have denMul := congrArg (·*n) denominator
    have edgeMul := congrArg (3^(ones+1)*·) edge
    rw [show front.length+ones+1=front.length+(ones+1) by omega,
      Nat.pow_add] at denMul
    grind
  have first : 2^(total front+1) ∣ 2^(total front+ones+1) :=
    Nat.pow_dvd_pow 2 (by omega)
  have second : 2^(total front+1) ∣ 2^(total front+ones+last)*n :=
    Nat.dvd_mul_right_of_dvd (Nat.pow_dvd_pow 2 (by omega)) n
  have paid : 2^(total front+1) ∣ 2^total front*3^(ones+1)*(endpoint+1) := by
    refine ⟨3^(ones+1)*((endpoint+1)/2),?_⟩
    have even : 2*((endpoint+1)/2)=endpoint+1 := by omega
    rw [Nat.pow_succ]
    grind
  rw [←cleared] at paid
  exact (Nat.dvd_add_iff_left first).mpr ((Nat.dvd_add_iff_left second).mpr paid)

/-- The same entire word has the prescribed ternary phase. Clearing the
unit denominator gives `2^last*C = 2*D` modulo every retained power of three;
the rational phase `-C/D` is therefore `-2^(1-last)` in that completion. -/
theorem extension_ternary_guard (front : List Nat) (ones last D precision : Nat)
    (deep : precision≤ones+1)
    (denominator : 2^total (extension front ones last)+D =
      3^(extension front ones last).length) :
    (2^last*correction (extension front ones last))%3^precision =
      (2*D)%3^precision := by
  obtain ⟨len,clock,numerator⟩ := extension_data front ones last
  rw [len,clock] at denominator
  have numMul := congrArg (2^last*·) numerator
  have denMul := congrArg (2*·) denominator
  have common : 2^last*2^(total front+ones+1) =
      2*2^(total front+ones+last) := by
    rw [←Nat.pow_add,Nat.mul_comm 2 (2^(total front+ones+last)),←Nat.pow_succ]
    congr 1
    omega
  have combined :
      2^last*correction (extension front ones last)+2*3^(front.length+ones+1) =
        2*D+3^(ones+1)*(2^last*(correction front+2^total front)) := by
    grind
  have first : 3^(front.length+ones+1)%3^precision=0 :=
    Nat.mod_eq_zero_of_dvd (Nat.pow_dvd_pow 3 (by omega))
  have second : 3^(ones+1)%3^precision=0 :=
    Nat.mod_eq_zero_of_dvd (Nat.pow_dvd_pow 3 deep)
  have reduced := congrArg (fun n : Nat => n%3^precision) combined
  simpa [Nat.add_mod,Nat.mul_mod,first,second] using reduced

end CollatzNegativeCycleExtension
