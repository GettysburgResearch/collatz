import Collatz.SignedShadow
import Collatz.LowIntervalRefinement

/-!
Every negative odd shadow has a bounded noncontracting prefix.

No eventual behavior of the negative Collatz map is assumed. If all initial
prefixes contracted, the positive affine correction would spend the finite
initial negative magnitude within 3m odd events. A sufficiently separated
positive source follows the selected prefix physically and strictly grows.
-/

open CollatzReverseBasin CollatzClosure CollatzWitness CollatzHighGapPump
open CollatzUnboundedGapReset CollatzSignedShadow

set_option autoImplicit false
set_option maxHeartbeats 4000000

namespace CollatzNegativeShadow

/-- Every state of a signed trace starting negative remains negative. -/
theorem negative_endpoint {z endpoint : Int} {word : List Nat}
    (trace : SignedTrace z word endpoint) (negative : z<0) : endpoint<0 := by
  induction trace with
  | nil z odd => exact negative
  | cons z w endpoint a tail positive odd edge rest ih =>
    apply ih
    have power : 0<(2: Int)^a := by
      exact_mod_cast (Nat.pow_pos (by decide : 0<2) (n:=a))
    have product : (2: Int)^a*w<0 := by omega
    by_cases result : w<0
    · exact result
    have nonnegative := Int.mul_nonneg (by omega : 0≤(2: Int)^a) (by omega : 0≤w)
    omega

/-- The full signed correction remains below the initial cleared magnitude. -/
theorem negative_correction_bound (m : Nat) (positive : 0<m)
    {word : List Nat} {endpoint : Int}
    (trace : SignedTrace (-(m: Int)) word endpoint) :
    correction word<3^word.length*m := by
  have endpointNegative := negative_endpoint trace (by omega)
  have power : 0<(2: Int)^total word := by
    exact_mod_cast (Nat.pow_pos (by decide : 0<2) (n:=total word))
  have product := Int.mul_neg_of_pos_of_neg power endpointNegative
  have identity := affine_identity trace
  have bound : (correction word: Int)<(3: Int)^word.length*(m: Int) := by
    grind
  exact_mod_cast bound

/-- If every prefix pays at least its linear multiplier, each odd event
contributes at least one third of the final power of three to the correction. -/
theorem correction_prefix_floor (word : List Nat)
    (floor : ∀ front tail : List Nat, word=front++tail →
      3^front.length≤2^total front) :
    word.length*3^word.length≤3*correction word := by
  generalize lengthEq : word.length=n
  induction n generalizing word with
  | zero =>
    have empty : word=[] := List.length_eq_zero_iff.mp lengthEq
    simp [empty,correction]
  | succ n ih =>
    obtain empty | ⟨front,a,shape⟩ := List.eq_nil_or_concat word
    · simp [empty] at lengthEq
    have shape' : word=front++[a] := by simpa [List.concat_eq_append] using shape
    have frontLength : front.length=n := by rw [shape',List.length_append] at lengthEq; simp at lengthEq; omega
    have subfloor : ∀ pre tail : List Nat, front=pre++tail →
        3^pre.length≤2^total pre := by
      intro pre tail eq
      exact floor pre (tail++[a]) (by rw [shape',eq,List.append_assoc])
    have previous := ih front subfloor frontLength
    have last := floor front [a] shape'
    rw [shape',correction_append]
    simp only [List.length_cons,List.length_nil,correction,Nat.pow_zero,
      Nat.mul_zero,Nat.add_zero,Nat.one_mul,Nat.pow_succ]
    rw [frontLength] at last
    have scaled := Nat.mul_le_mul_left 3 previous
    have scaledLast := Nat.mul_le_mul_left 3 last
    grind

/-- Split a signed trace at a literal prefix without replacing its tail. -/
theorem split_signed_trace {z endpoint : Int} (front tail : List Nat)
    (trace : SignedTrace z (front++tail) endpoint) :
    ∃ middle : Int, SignedTrace z front middle ∧ SignedTrace middle tail endpoint := by
  induction front generalizing z with
  | nil => exact ⟨z,SignedTrace.nil z (source_odd trace),trace⟩
  | cons a front ih =>
    cases trace with
    | cons z w endpoint a rest positive odd edge trace =>
      obtain ⟨middle,first,last⟩ := ih trace
      exact ⟨middle,SignedTrace.cons z w middle a front positive odd edge first,last⟩

/-- Every negative shadow has a nonempty noncontracting prefix among its
first 3m odd events. The witness is extracted from the supplied signed trace. -/
theorem noncontracting_prefix (m : Nat) (positive : 0<m)
    {word : List Nat} {endpoint : Int}
    (trace : SignedTrace (-(m: Int)) word endpoint) (length : word.length=3*m) :
    ∃ front tail : List Nat, ∃ middle : Int,
      word=front++tail ∧ front≠[] ∧ front.length≤3*m ∧
      2^total front≤3^front.length ∧ SignedTrace (-(m: Int)) front middle := by
  by_cases existsPrefix : ∃ front tail : List Nat,
      word=front++tail ∧ front≠[] ∧ 2^total front≤3^front.length
  · obtain ⟨front,tail,shape,nonempty,coefficient⟩ := existsPrefix
    have prefixLength : front.length≤3*m := by
      rw [shape,List.length_append] at length
      omega
    have trace' : SignedTrace (-(m: Int)) (front++tail) endpoint := by rwa [←shape]
    obtain ⟨middle,first,_⟩ := split_signed_trace front tail trace'
    exact ⟨front,tail,middle,shape,nonempty,prefixLength,coefficient,first⟩
  · have floor : ∀ front tail : List Nat, word=front++tail →
        3^front.length≤2^total front := by
      intro front tail shape
      by_cases empty : front=[]
      · simp [empty,total]
      by_cases coefficient : 2^total front≤3^front.length
      · exact False.elim (existsPrefix ⟨front,tail,shape,empty,coefficient⟩)
      · omega
    have spent := correction_prefix_floor word floor
    have available := negative_correction_bound m positive trace
    have strict := Nat.mul_lt_mul_of_pos_left available (by decide : 0<3)
    rw [length] at spent strict
    have factor : 3*m*3^(3*m)=3*(3^(3*m)*m) := by ac_rfl
    rw [factor] at spent
    omega

/-- An unconditional finite negative-shadow selector, with no valuation or
negative-orbit termination assumption. -/
theorem bounded_negative_prefix (m : Nat) (positive : 0<m) (odd : m%2=1) :
    ∃ word : List Nat, ∃ endpoint : Int,
      word≠[] ∧ word.length≤3*m ∧ 2^total word≤3^word.length ∧
      SignedTrace (-(m: Int)) word endpoint := by
  obtain ⟨full,endpoint,length,trace⟩ :=
    trace_exists (-(m: Int)) (by omega) (3*m)
  obtain ⟨word,tail,middle,_,nonempty,bound,coefficient,first⟩ :=
    noncontracting_prefix m positive trace length
  exact ⟨word,middle,nonempty,bound,coefficient,first⟩

/-- A nonempty noncontracting odd prefix uses fewer than twice its number
of odd events in ordinary clocks. No shadow magnitude factor is needed. -/
theorem noncontracting_clock_bound (word : List Nat) (nonempty : word≠[])
    (coefficient : 2^total word≤3^word.length) : total word<2*word.length := by
  have lengthPositive : 0<word.length := by
    cases word with
    | nil => exact False.elim (nonempty rfl)
    | cons a tail => simp
  have strict := Nat.pow_lt_pow_left (by decide : 3<4) (by omega : word.length≠0)
  have power : 4^word.length=2^(2*word.length) := by rw [Nat.pow_mul]
  rw [power] at strict
  by_cases result : total word<2*word.length
  · exact result
  have reverse := Nat.pow_le_pow_right (by decide : 0<2)
    (show 2*word.length≤total word by omega)
  omega

/-- A separated negative low block makes the positive source itself larger
than the two states in the ordinary cycle through one. -/
theorem source_above_two (n u D m : Nat) (positive : 0<n) (mPositive : 0<m)
    (source : n+m=2^D*u) (separation : 6*m≤D) : 2<n := by
  have uPositive : 0<u := by
    by_cases zero : u=0
    · simp [zero] at source
      omega
    · omega
  have factor := Nat.mul_le_mul_left (2^D) (show 1≤u by omega)
  have power := Nat.pow_le_pow_right (by decide : 0<2)
    (show m+2≤D by omega)
  have lower : 2^(m+2)=4*2^m := by rw [Nat.pow_add]; omega
  rw [lower] at power
  have grows : m<2^m := Nat.lt_two_pow_self
  omega

/-- Actual positive source expansion forced by every sufficiently separated
negative odd low block. This exposes precisely the original-source ordinary
clock and odd endpoint needed by the complete-certificate rank consumer. -/
theorem physical_negative_return (n u D m : Nat)
    (positive : 0<n) (mPositive : 0<m) (mOdd : m%2=1)
    (source : n+m=2^D*u) (separation : 6*m≤D) :
    2<n ∧ ∃ word : List Nat, ∃ endpoint : Nat,
      word≠[] ∧ word.length≤3*m ∧ 2^total word≤3^word.length ∧
      0<total word ∧ total word<6*m ∧ total word<D ∧
      Prefix n word endpoint ∧ n<endpoint ∧ endpoint%2=1 ∧
      orbit n (total word)=endpoint := by
  obtain ⟨word,shadow,nonempty,length,coefficient,trace⟩ :=
    bounded_negative_prefix m mPositive mOdd
  have clockBound := noncontracting_clock_bound word nonempty coefficient
  have clock : total word<D := by omega
  have naturalSource : (n: Int)=(2: Int)^D*(u: Int)-(m: Int) := by
    have cast : (n: Int)+(m: Int)=(2: Int)^D*(u: Int) := by exact_mod_cast source
    omega
  obtain ⟨endpoint,_,path,value⟩ :=
    compile_signed_lift trace n u D positive naturalSource (by omega)
  have endpointOdd : endpoint%2=1 := by
    have shadowOdd := endpoint_odd trace
    obtain ⟨b,exponent⟩ := Nat.exists_eq_succ_of_ne_zero (by omega : D-total word≠0)
    have evenHigh : (2: Int)^(D-total word)*(3: Int)^word.length*(u: Int)=
        2*((2: Int)^b*(3: Int)^word.length*(u: Int)) := by
      rw [exponent,Int.pow_succ]
      grind
    rw [evenHigh] at value
    omega
  have clockPositive : 0<total word := by
    cases word with
    | nil => exact False.elim (nonempty rfl)
    | cons a tail =>
      have head := (positive_gaps trace) a (by simp)
      simp only [total]
      omega
  exact ⟨source_above_two n u D m positive mPositive source separation,
    word,endpoint,nonempty,length,coefficient,clockPositive,by omega,clock,path,
    CollatzLowIntervalRefinement.prefix_expands n endpoint word path nonempty coefficient,
    endpointOdd,prefix_orbit path⟩

end CollatzNegativeShadow
