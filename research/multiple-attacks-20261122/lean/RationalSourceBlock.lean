module

public import RationalShadow

@[expose] public section

/-!
# Arbitrary repeated source blocks supply rational shadows

The source block can have any finite positive-gap word. The full affine
constant is retained. The resulting displacement is passed to the physical
target-shadow theorem; no claim of universal rational periodicity is used.
-/

namespace CollatzRationalShadow

open CollatzShell CollatzShell.WitnessGlobal

def gapOffset : List Nat → Nat
  | [] => 0
  | a :: rest => 3^rest.length+2^a*gapOffset rest

def repeatWord (word : List Nat) : Nat → List Nat
  | 0 => []
  | e+1 => word ++ repeatWord word e

def AffineRepeat (a b C : Nat) : Nat → Nat → Nat → Prop
  | 0, r, u => r=u
  | e+1, r, u => ∃ v, a*r+C=b*v ∧ AffineRepeat a b C e v u

theorem gap_trace_affine (word : List Nat) (r u : Nat)
    (trace : GapTrace r u word) :
    2^word.sum*u=3^word.length*r+gapOffset word := by
  induction word generalizing r with
  | nil => simpa [GapTrace,gapOffset] using trace.symm
  | cons a rest ih =>
      obtain ⟨_,v,edge,tail⟩ := trace
      have endeq := ih v tail
      have left := congrArg (fun x : Nat => 2^a*x) endeq
      have right := congrArg (fun x : Nat => 3^rest.length*x) edge
      simp only [List.sum_cons,List.length_cons,gapOffset,pow_add,pow_succ]
      ring_nf at left right ⊢
      omega

theorem gap_repeat_affine (word : List Nat) (e r u : Nat)
    (trace : GapTrace r u (repeatWord word e)) :
    AffineRepeat (3^word.length) (2^word.sum) (gapOffset word) e r u := by
  induction e generalizing r with
  | zero => simpa [repeatWord,GapTrace,AffineRepeat] using trace
  | succ e ih =>
      obtain ⟨v,first,rest⟩ :=
        (trace_append_iff r u word (repeatWord word e)).mp trace
      exact ⟨v,(gap_trace_affine word r v first).symm,ih v rest⟩

theorem affine_repeat_identity (a b C D e r u : Nat)
    (denominator : D+a=b) (trace : AffineRepeat a b C e r u) :
    b^e*(D*u)+a^e*C=a^e*(D*r)+b^e*C := by
  induction e generalizing r with
  | zero =>
      have eq : r=u := trace
      simpa using congrArg (fun x => D*x+C) eq.symm
  | succ e ih =>
      obtain ⟨v,edge,rest⟩ := trace
      have tail := ih v rest
      have first : b*(D*v)+a*C=a*(D*r)+b*C := by
        have deq := congrArg (fun x : Nat => D*x) edge
        rw [← denominator] at deq ⊢
        ring_nf at deq ⊢
        omega
      have left := congrArg (fun x : Nat => b*x) tail
      have right := congrArg (fun x : Nat => a^e*x) first
      simp only [pow_succ]
      ring_nf at left right ⊢
      omega

theorem affine_repeat_positive_displacement (L s C D e r u : Nat)
    (denominator : D+3^s=2^L)
    (trace : AffineRepeat (3^s) (2^L) C e r u) (large : C<D*r) :
    ∃ t, 0<t ∧ D*r=2^(L*e)*t+C := by
  have eq := affine_repeat_identity (3^s) (2^L) C D e r u denominator trace
  have dr : D*r=(D*r-C)+C := by omega
  have rearranged : (3^s)^e*(D*r-C)+(2^L)^e*C=(2^L)^e*(D*u) := by
    have dr' := congrArg (fun x : Nat => (3^s)^e*x) dr
    ring_nf at eq dr' ⊢
    omega
  have divides : (2^L)^e ∣ (3^s)^e*(D*r-C)+(2^L)^e*C :=
    ⟨D*u,rearranged⟩
  have prod : (2^L)^e ∣ (3^s)^e*(D*r-C) :=
    (Nat.dvd_add_iff_left (dvd_mul_right ((2^L)^e) C)).mpr divides
  have cop : Nat.Coprime ((2^L)^e) ((3^s)^e) :=
    ((((by decide : Nat.Coprime 2 3).pow_left L).pow_left e).pow_right s).pow_right e
  obtain ⟨t,ht⟩ := cop.dvd_of_dvd_mul_left prod
  have tp : 0<t := by
    by_contra hn
    have tz : t=0 := by omega
    simp only [tz,Nat.mul_zero] at ht
    omega
  refine ⟨t,tp,?_⟩
  rw [pow_mul]
  omega

/-- A sufficiently long repeated block leaves only its exact integer
fixed point or a strictly positive dyadic displacement. -/
theorem affine_repeat_fixed_or_displacement (L s C D e r u : Nat)
    (denominator : D+3^s=2^L)
    (trace : AffineRepeat (3^s) (2^L) C e r u)
    (long : C<2^(L*e)) :
    D*r=C ∨ ∃ t, 0<t ∧ D*r=2^(L*e)*t+C := by
  by_cases eqfixed : D*r=C
  · exact Or.inl eqfixed
  · apply Or.inr
    apply affine_repeat_positive_displacement L s C D e r u denominator trace
    by_contra hsmall
    have le : D*r≤C := by omega
    have deltaPos : 0<C-D*r := by omega
    have split : C=(C-D*r)+D*r := by omega
    have eq := affine_repeat_identity (3^s) (2^L) C D e r u denominator trace
    have rearranged : (3^s)^e*(C-D*r)+(2^L)^e*(D*u)=(2^L)^e*C := by
      have split' := congrArg (fun x : Nat => (3^s)^e*x) split
      ring_nf at eq split' ⊢
      omega
    have divides : (2^L)^e ∣ (3^s)^e*(C-D*r)+(2^L)^e*(D*u) :=
      ⟨C,rearranged⟩
    have prod : (2^L)^e ∣ (3^s)^e*(C-D*r) :=
      (Nat.dvd_add_iff_left (dvd_mul_right ((2^L)^e) (D*u))).mpr divides
    have cop : Nat.Coprime ((2^L)^e) ((3^s)^e) :=
      ((((by decide : Nat.Coprime 2 3).pow_left L).pow_left e).pow_right s).pow_right e
    have dividesDelta := cop.dvd_of_dvd_mul_left prod
    have lower := Nat.le_of_dvd deltaPos dividesDelta
    rw [← pow_mul] at lower
    omega

/-- The source block is arbitrary, and its actual integer trace is kept.
Its only exceptional source is the exact rational fixed point if that
fixed point happens to be an integer. -/
theorem repeated_word_fixed_or_displacement (word : List Nat) (D e r u : Nat)
    (denominator : D+3^word.length=2^word.sum)
    (trace : GapTrace r u (repeatWord word e))
    (long : gapOffset word<2^(word.sum*e)) :
    D*r=gapOffset word ∨
      ∃ t, 0<t ∧ D*r=2^(word.sum*e)*t+gapOffset word := by
  exact affine_repeat_fixed_or_displacement word.sum word.length (gapOffset word)
    D e r u denominator (gap_repeat_affine word e r u trace) long

/-- Once a contracting prefix pays the unit displacement, it pays every
larger physical source displacement as well. -/
theorem paid_displacement_mono (left right offset endpoint t : Nat)
    (contracts : left≤right) (positive : 0<t)
    (unit : left+endpoint<right+offset) :
    left*t+endpoint<right*t+offset := by
  have split : t=(t-1)+1 := by omega
  have remainder := Nat.mul_le_mul_right (t-1) contracts
  calc
    left*t+endpoint=left*(t-1)+(left+endpoint) := by
      conv_lhs => rw [split]
      ring
    _ < left*(t-1)+(right+offset) := Nat.add_lt_add_left unit _
    _ ≤ right*(t-1)+(right+offset) := Nat.add_le_add_right remainder _
    _ =right*t+offset := by
      conv_rhs => rw [split]
      ring

/-- Complete compiler from an arbitrary repeated source word and a
unit-displacement target certificate. The exact integer source fixed
point is retained as the only explicit exception. -/
theorem repeated_word_shadow_dispatch
    (word : List Nat) (D e r u A B j : Nat)
    (denominator : D+3^word.length=2^word.sum)
    (odd : D%2=1)
    (trace : GapTrace r u (repeatWord word e))
    (long : gapOffset word<2^(word.sum*e))
    (horizon : j≤word.sum*e)
    (contracts : 3^(numeratorOdds j D (A*gapOffset word+D*B))≤2^j)
    (unit :
      3^(numeratorOdds j D (A*gapOffset word+D*B))*(2^(word.sum*e-j)*A)+
        numeratorOrbit j D (A*gapOffset word+D*B) <
      2^j*(2^(word.sum*e-j)*A)+(A*gapOffset word+D*B)) :
    D*r=gapOffset word ∨ orbit j (A*r+B)<A*r+B := by
  rcases repeated_word_fixed_or_displacement word D e r u denominator trace long with
      fixed | ⟨t,positive,pin⟩
  · exact Or.inl fixed
  · apply Or.inr
    apply affine_source_shadow_descent j D r A B (gapOffset word) (word.sum*e) t
      odd pin horizon
    have paid := paid_displacement_mono
      (3^(numeratorOdds j D (A*gapOffset word+D*B))*(2^(word.sum*e-j)*A))
      (2^j*(2^(word.sum*e-j)*A)) (A*gapOffset word+D*B)
      (numeratorOrbit j D (A*gapOffset word+D*B)) t
      (Nat.mul_le_mul_right _ contracts) positive unit
    simpa only [mul_assoc] using paid

/-- A separately certified fixed-point target closes the only exceptional
source branch of the complete compiler. -/
theorem repeated_word_shadow_descent
    (word : List Nat) (D e r u A B j : Nat)
    (denominator : D+3^word.length=2^word.sum)
    (odd : D%2=1)
    (trace : GapTrace r u (repeatWord word e))
    (long : gapOffset word<2^(word.sum*e))
    (horizon : j≤word.sum*e)
    (contracts : 3^(numeratorOdds j D (A*gapOffset word+D*B))≤2^j)
    (unit :
      3^(numeratorOdds j D (A*gapOffset word+D*B))*(2^(word.sum*e-j)*A)+
        numeratorOrbit j D (A*gapOffset word+D*B) <
      2^j*(2^(word.sum*e-j)*A)+(A*gapOffset word+D*B))
    (fixed : D*r=gapOffset word → orbit j (A*r+B)<A*r+B) :
    orbit j (A*r+B)<A*r+B := by
  exact (repeated_word_shadow_dispatch word D e r u A B j denominator odd trace
    long horizon contracts unit).elim fixed id

end CollatzRationalShadow

#print axioms CollatzRationalShadow.gap_trace_affine
#print axioms CollatzRationalShadow.gap_repeat_affine
#print axioms CollatzRationalShadow.affine_repeat_identity
#print axioms CollatzRationalShadow.affine_repeat_positive_displacement
#print axioms CollatzRationalShadow.affine_repeat_fixed_or_displacement
#print axioms CollatzRationalShadow.repeated_word_fixed_or_displacement
#print axioms CollatzRationalShadow.paid_displacement_mono
#print axioms CollatzRationalShadow.repeated_word_shadow_dispatch
#print axioms CollatzRationalShadow.repeated_word_shadow_descent
