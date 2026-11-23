import Collatz.HighGapPump
import Collatz.UnboundedGapReset

/-!
Signed low-block shadows of actual positive Collatz paths.

The low block may be positive or negative.  In particular, -1 is a legal
fixed odd shadow; no termination of a signed Collatz map is assumed.
Every finite signed trace exists, its cleared magnitude has the uniform
4^r bound, and sufficient dyadic separation compiles the same gap word
to an actual positive ordinary path with its exact high block retained.

This is the arithmetic interface used by BINARY_RUN_COMPACTNESS.md.
-/

open CollatzReverseBasin CollatzClosure CollatzWitness CollatzHighGapPump
open CollatzUnboundedGapReset

set_option autoImplicit false
set_option maxHeartbeats 4000000

namespace CollatzSignedShadow

/-- An actual finite accelerated odd trace over the signed integers. -/
inductive SignedTrace : Int → List Nat → Int → Prop where
  | nil (z : Int) (odd : z % 2 = 1) : SignedTrace z [] z
  | cons (z w endpoint : Int) (a : Nat) (tail : List Nat)
      (positive : 0 < a) (odd : z % 2 = 1)
      (edge : 3*z+1 = (2: Int)^a*w)
      (rest : SignedTrace w tail endpoint) :
      SignedTrace z (a::tail) endpoint

theorem source_odd {z endpoint : Int} {word : List Nat}
    (trace : SignedTrace z word endpoint) : z % 2 = 1 := by
  cases trace with
  | nil z odd => exact odd
  | cons z w endpoint a tail positive odd edge rest => exact odd

theorem endpoint_odd {z endpoint : Int} {word : List Nat}
    (trace : SignedTrace z word endpoint) : endpoint % 2 = 1 := by
  induction trace with
  | nil z odd => exact odd
  | cons z w endpoint a tail positive odd edge rest ih => exact ih

theorem positive_gaps {z endpoint : Int} {word : List Nat}
    (trace : SignedTrace z word endpoint) : PositiveGaps word := by
  induction trace with
  | nil z odd => simp [PositiveGaps]
  | cons z w endpoint a tail positive odd edge rest ih =>
    intro b member
    rcases List.mem_cons.mp member with eq | mem
    · simpa [eq] using positive
    · exact ih b mem

theorem affine_identity {z endpoint : Int} {word : List Nat}
    (trace : SignedTrace z word endpoint) :
    (3: Int)^word.length*z + (correction word : Int) =
      (2: Int)^total word*endpoint := by
  induction trace with
  | nil z odd => simp [correction,total]
  | cons z w endpoint a tail positive odd edge rest ih =>
    simp only [List.length_cons,correction,total,Int.natCast_add,
      Int.natCast_mul,Int.natCast_pow,Int.pow_succ,Int.pow_add]
    grind

/-- Powers of two can be removed from every positive natural integer. -/
theorem nat_odd_factor (n : Nat) (positive : 0<n) :
    ∃ a u : Nat, n=2^a*u ∧ u%2=1 := by
  induction n using Nat.strong_induction_on with
  | h n ih =>
    by_cases odd : n%2=1
    · exact ⟨0,n,by simp,odd⟩
    have even : n%2=0 := by omega
    have smaller : n/2<n := by omega
    obtain ⟨a,u,value,unit⟩ := ih (n/2) smaller (by omega)
    refine ⟨a+1,u,?_,unit⟩
    have twice : n=2*(n/2) := by omega
    rw [twice,value,Nat.pow_succ]
    grind

/-- Signed factorization retains the sign and an odd integral quotient. -/
theorem int_odd_factor (z : Int) (nonzero : z≠0) :
    ∃ a : Nat, ∃ u : Int, z=(2: Int)^a*u ∧ u%2=1 := by
  obtain ⟨a,u,value,odd⟩ := nat_odd_factor z.natAbs (by omega)
  have magnitude : (z.natAbs : Int)=(2: Int)^a*(u: Int) := by
    exact_mod_cast value
  by_cases positive : 0≤z
  · refine ⟨a,(u: Int),?_,?_⟩
    · have abs : (z.natAbs : Int)=z := Int.natAbs_of_nonneg positive
      omega
    · omega
  · refine ⟨a,-(u: Int),?_,?_⟩
    · have abs : (z.natAbs : Int) = -z := by omega
      rw [abs] at magnitude
      grind
    · omega

/-- Every odd signed state has a nonempty exact next odd gap. -/
theorem next_signed_gap (z : Int) (odd : z%2=1) :
    ∃ a : Nat, ∃ u : Int,
      0<a ∧ u%2=1 ∧ 3*z+1=(2: Int)^a*u := by
  obtain ⟨a,u,value,unit⟩ := int_odd_factor (3*z+1) (by omega)
  refine ⟨a,u,?_,unit,value⟩
  cases a with
  | zero => simp only [Int.pow_zero,Int.one_mul] at value; omega
  | succ a => omega

/-- A finite signed trace exists for every requested number of odd events.
This includes both fixed shadows 1 and -1. -/
theorem trace_exists (z : Int) (odd : z%2=1) (r : Nat) :
    ∃ word endpoint, word.length=r ∧ SignedTrace z word endpoint := by
  induction r generalizing z with
  | zero => exact ⟨[],z,rfl,SignedTrace.nil z odd⟩
  | succ r ih =>
    obtain ⟨a,u,positive,unit,edge⟩ := next_signed_gap z odd
    obtain ⟨word,endpoint,length,rest⟩ := ih u unit
    exact ⟨a::word,endpoint,by simp [length],
      SignedTrace.cons z u endpoint a word positive odd edge rest⟩

/-- Clearing the accumulated dyadic denominator grows signed magnitude by
at most four per odd event, independently of all valuation gaps. -/
theorem cleared_magnitude {z endpoint : Int} {word : List Nat}
    (trace : SignedTrace z word endpoint) :
    2^total word*endpoint.natAbs ≤ 4^word.length*z.natAbs := by
  induction trace with
  | nil z odd => simp [total]
  | cons z w endpoint a tail positive odd edge rest ih =>
    have one : 2^a*w.natAbs ≤ 4*z.natAbs := by
      have eq := congrArg Int.natAbs edge
      have triangle := Int.natAbs_add_le (3*z) 1
      simp [Int.natAbs_mul,Int.natAbs_pow] at eq triangle
      have nonzero : 0<z.natAbs := by omega
      omega
    have first := Nat.mul_le_mul_left (2^a) ih
    have second := Nat.mul_le_mul_left (4^tail.length) one
    simp only [total,List.length_cons,Nat.pow_add,Nat.pow_succ]
    grind

/-- A small cleared low block guarantees that its entire supplied clock is
strictly below the unused binary separation. -/
theorem clock_below_separation {z endpoint : Int} {word : List Nat} {D : Nat}
    (trace : SignedTrace z word endpoint)
    (small : 4^word.length*z.natAbs < 2^D) : total word<D := by
  have magnitude := cleared_magnitude trace
  have endpointUnit := endpoint_odd trace
  have nonzero : 1≤endpoint.natAbs := by omega
  have denominator := Nat.mul_le_mul_left (2^total word) nonzero
  have powers : 2^total word<2^D := by omega
  by_cases bound : total word<D
  · exact bound
  have opposite : D≤total word := by omega
  have monotone := Nat.pow_le_pow_right (by decide : 0<2) opposite
  omega

/-- The signed endpoint stays strictly inside the remaining binary block;
this is the bound needed for both positive concatenation and negative borrow. -/
theorem endpoint_below_separation {z endpoint : Int} {word : List Nat} {D : Nat}
    (trace : SignedTrace z word endpoint)
    (small : 4^word.length*z.natAbs < 2^D) :
    endpoint.natAbs < 2^(D-total word) := by
  have clock := clock_below_separation trace small
  have bound := Nat.lt_of_le_of_lt (cleared_magnitude trace) small
  have power : 2^D=2^total word*2^(D-total word) := by
    rw [←Nat.pow_add,Nat.add_sub_of_le (by omega : total word≤D)]
  rw [power] at bound
  exact Nat.lt_of_mul_lt_mul_left bound

/-- Every exact natural gap prefix follows the actual ordinary map for
precisely its total number of shortcut clocks. -/
theorem prefix_orbit {n endpoint : Nat} {word : List Nat}
    (path : Prefix n word endpoint) : orbit n (total word)=endpoint := by
  have halvings (a m : Nat) : orbit (2^a*m) a=m := by
    induction a with
    | zero => simp [orbit]
    | succ a ih =>
      have step : shortcut (2^(a+1)*m)=2^a*m := by
        rw [Nat.pow_succ]
        have factor : 2^a*2*m=2*(2^a*m) := by grind
        rw [factor]
        unfold shortcut
        simp
      rw [orbit,step,ih]
  induction word generalizing n with
  | nil => simpa [Prefix,total,correction,orbit] using path.2
  | cons a tail ih =>
    obtain ⟨positive,m,edge,rest⟩ := (prefix_cons_iff n a endpoint tail).mp path
    obtain ⟨b,rfl⟩ := Nat.exists_eq_succ_of_ne_zero (by omega : a≠0)
    have edge' : 3*n+1=2*(2^b*m) := by rw [Nat.pow_succ] at edge; grind
    have step : shortcut n=2^b*m := by unfold shortcut; split <;> omega
    rw [total,orbit_add,orbit,step,halvings]
    exact ih rest

/-- Every exact signed affine lift compiles to a positive ordinary prefix.
The complete natural source is retained, and the endpoint is an integer
because the unused dyadic separation pays the whole supplied shadow clock. -/
theorem compile_signed_lift {z endpoint : Int} {word : List Nat}
    (trace : SignedTrace z word endpoint) (n u D : Nat)
    (positive : 0<n) (source : (n: Int)=(2: Int)^D*(u: Int)+z)
    (clock : total word≤D) :
    ∃ m : Nat, 0<m ∧ Prefix n word m ∧
      (m: Int)=(2: Int)^(D-total word)*(3: Int)^word.length*(u: Int)+endpoint := by
  let m : Int := (2: Int)^(D-total word)*(3: Int)^word.length*(u: Int)+endpoint
  have power : (2: Int)^total word*(2: Int)^(D-total word)=(2: Int)^D := by
    rw [←Int.pow_add,Nat.add_sub_of_le clock]
  have affine := affine_identity trace
  have identity : (2: Int)^total word*m=
      (3: Int)^word.length*(n: Int)+(correction word: Int) := by
    dsimp [m]
    rw [source]
    grind
  have powPositive : 0<(3: Int)^word.length := by
    exact_mod_cast (Nat.pow_pos (by decide : 0<3) (n:=word.length))
  have sourcePositive : 0<(n: Int) := by omega
  have productPositive := Int.mul_pos powPositive sourcePositive
  have mPositive : 0<m := by
    have denominator : 0<(2: Int)^total word := by
      exact_mod_cast (Nat.pow_pos (by decide : 0<2) (n:=total word))
    have leftPositive : 0<(2: Int)^total word*m := by omega
    exact Int.pos_of_mul_pos_right leftPositive denominator
  refine ⟨m.toNat,by omega,⟨positive_gaps trace,?_⟩,?_⟩
  · have cast : (m.toNat: Int)=m := by omega
    rw [←cast] at identity
    exact_mod_cast identity.symm
  · change (m.toNat: Int)=m
    omega

/-- Uniform signed separation, with the actual natural orbit endpoint and
the exact ordinary clock both exposed. -/
theorem separated_shadow {z endpoint : Int} {word : List Nat}
    (trace : SignedTrace z word endpoint) (n u D : Nat)
    (positive : 0<n) (source : (n: Int)=(2: Int)^D*(u: Int)+z)
    (small : 4^word.length*z.natAbs<2^D) :
    total word<D ∧
    (orbit n (total word): Int)=
      (2: Int)^(D-total word)*(3: Int)^word.length*(u: Int)+endpoint := by
  have clock := clock_below_separation trace small
  obtain ⟨m,_,path,value⟩ := compile_signed_lift trace n u D positive source (by omega)
  exact ⟨clock,by rw [prefix_orbit path]; exact value⟩

/-- The complete separated-shadow certificate used in the binary-run proof:
an ordinary clock, a positive actual endpoint, its exact signed block split,
and a nonzero low block strictly smaller than the remaining dyadic block. -/
theorem separated_shadow_certificate {z endpoint : Int} {word : List Nat}
    (trace : SignedTrace z word endpoint) (n u D : Nat)
    (positive : 0<n) (source : (n: Int)=(2: Int)^D*(u: Int)+z)
    (small : 4^word.length*z.natAbs<2^D) :
    total word<D ∧ 0<orbit n (total word) ∧
    (orbit n (total word): Int)=
      (2: Int)^(D-total word)*(3: Int)^word.length*(u: Int)+endpoint ∧
    0<endpoint.natAbs ∧ endpoint.natAbs<2^(D-total word) := by
  have clock := clock_below_separation trace small
  obtain ⟨m,mPositive,path,value⟩ :=
    compile_signed_lift trace n u D positive source (by omega)
  have odd := endpoint_odd trace
  exact ⟨clock,by rw [prefix_orbit path]; exact mPositive,
    by rw [prefix_orbit path]; exact value,
    by omega,endpoint_below_separation trace small⟩

end CollatzSignedShadow
