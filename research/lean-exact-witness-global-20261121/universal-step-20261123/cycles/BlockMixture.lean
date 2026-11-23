/-
All-length exclusion for mixed concatenations of two equal-shape affine
Collatz blocks with a 6-smooth carry difference.  This is a theorem about
the complete affine cycle equation, with arbitrary block and cycle lengths.
It does not assert that every possible Collatz cycle has this block form.
-/
import Std

set_option autoImplicit false
set_option maxHeartbeats 2000000

namespace CollatzBlockMixture

def geometric (P Q : Nat) : Nat → Nat
  | 0 => 0
  | n+1 => P^n + Q*geometric P Q n

def weighted (P Q : Nat) : List Bool → Nat
  | [] => 0
  | b::bs => (if b then P^bs.length else 0) + Q*weighted P Q bs

def carry (P Q c d : Nat) : List Bool → Nat
  | [] => 0
  | b::bs => P^bs.length*(c + if b then d else 0) + Q*carry P Q c d bs

def Path (P Q c d : Nat) : Nat → List Bool → Nat → Prop
  | x, [], y => x=y
  | x, b::bs, y =>
      ∃ z, Q*z=P*x+c+(if b then d else 0) ∧ Path P Q c d z bs y

theorem path_affine (P Q c d : Nat) (bs : List Bool) (x y : Nat)
    (path : Path P Q c d x bs y) :
    Q^bs.length*y=P^bs.length*x+carry P Q c d bs := by
  induction bs generalizing x y with
  | nil =>
    simp only [Path] at path
    simp [path,carry]
  | cons b bs ih =>
    obtain ⟨z,edge,tail⟩ := path
    have rest := ih z y tail
    have edgeScaled := congrArg (P^bs.length*·) edge
    have restScaled := congrArg (Q*·) rest
    simp only [List.length_cons,Nat.pow_succ,carry]
    grind

theorem geometric_alternate (P Q n : Nat) :
    geometric P Q (n+1)=Q^n+P*geometric P Q n := by
  induction n with
  | zero => simp [geometric]
  | succ n ih =>
    simp only [geometric] at ih ⊢
    simp only [Nat.pow_succ]
    grind

theorem geometric_balance (P Q n : Nat) :
    Q^n+P*geometric P Q n=P^n+Q*geometric P Q n := by
  have h := geometric_alternate P Q n
  simp only [geometric] at h
  omega

theorem carry_decomposition (P Q c d : Nat) (bs : List Bool) :
    carry P Q c d bs=c*geometric P Q bs.length+d*weighted P Q bs := by
  induction bs with
  | nil => simp [carry,geometric,weighted]
  | cons b bs ih =>
    cases b <;> simp only [carry,weighted,List.length_cons,geometric] <;> grind

private theorem weighted_le (P Q : Nat) (bs : List Bool) :
    weighted P Q bs ≤ geometric P Q bs.length := by
  induction bs with
  | nil => simp [weighted,geometric]
  | cons b bs ih =>
    have hm := Nat.mul_le_mul_left Q ih
    cases b <;> simp [weighted,List.length_cons,geometric] <;> omega

private theorem weighted_pos (P Q : Nat) (posP : 0<P) (posQ : 0<Q)
    (bs : List Bool) (hasTrue : true ∈ bs) : 0<weighted P Q bs := by
  induction bs with
  | nil => simp at hasTrue
  | cons b bs ih =>
    cases b with
    | false =>
      have ht : true ∈ bs := by simpa using hasTrue
      have hp := Nat.mul_pos posQ (ih ht)
      simpa [weighted] using hp
    | true =>
      have hp := Nat.pow_pos posP (n:=bs.length)
      change 0 < P^bs.length+Q*weighted P Q bs
      omega

private theorem weighted_lt (P Q : Nat) (posP : 0<P) (posQ : 0<Q)
    (bs : List Bool) (hasFalse : false ∈ bs) :
    weighted P Q bs < geometric P Q bs.length := by
  induction bs with
  | nil => simp at hasFalse
  | cons b bs ih =>
    cases b with
    | false =>
      have hw := Nat.mul_le_mul_left Q (weighted_le P Q bs)
      have hp := Nat.pow_pos posP (n:=bs.length)
      change 0+Q*weighted P Q bs < P^bs.length+Q*geometric P Q bs.length
      omega
    | true =>
      have hf : false ∈ bs := by simpa using hasFalse
      have hw := Nat.mul_lt_mul_of_pos_left (ih hf) posQ
      change P^bs.length+Q*weighted P Q bs < P^bs.length+Q*geometric P Q bs.length
      omega

/-- A complete all-length obstruction.  Both block types occur.  No
proper factor of the closing denominator replaces the cycle equation. -/
theorem no_mixed_cycle (P Q c d x : Nat) (bs : List Bool)
    (posP : 0<P) (posQ : 0<Q)
    (hasTrue : true ∈ bs) (hasFalse : false ∈ bs)
    (coprime : Nat.Coprime (geometric P Q bs.length) d) :
    Q^bs.length*x ≠ P^bs.length*x+carry P Q c d bs := by
  intro cycle
  rw [carry_decomposition] at cycle
  have balance := geometric_balance P Q bs.length
  have scaled := congrArg (·*x) balance
  have combined :
      Q*geometric P Q bs.length*x =
      P*geometric P Q bs.length*x+c*geometric P Q bs.length+
        d*weighted P Q bs := by grind
  have fullDiv : geometric P Q bs.length ∣
      P*geometric P Q bs.length*x+c*geometric P Q bs.length+
        d*weighted P Q bs := by
    rw [←combined]
    refine ⟨Q*x,?_⟩
    ac_rfl
  have prefixDiv : geometric P Q bs.length ∣
      P*geometric P Q bs.length*x+c*geometric P Q bs.length := by
    refine ⟨P*x+c,?_⟩
    grind
  have productDiv := (Nat.dvd_add_iff_right prefixDiv).mpr fullDiv
  have weightDiv := coprime.dvd_of_dvd_mul_left productDiv
  have positive := weighted_pos P Q posP posQ bs hasTrue
  have below := weighted_lt P Q posP posQ bs hasFalse
  have impossible := Nat.le_of_dvd positive weightDiv
  omega

private theorem geometric_coprime_right (P Q n : Nat)
    (coprime : Nat.Coprime P Q) (nonzero : 0<n) :
    Nat.Coprime (geometric P Q n) Q := by
  cases n with
  | zero => omega
  | succ n =>
    simp only [geometric,Nat.coprime_iff_gcd_eq_one,
      Nat.gcd_add_mul_left_left]
    exact coprime.pow_left n

private theorem geometric_coprime_left (P Q n : Nat)
    (coprime : Nat.Coprime P Q) (nonzero : 0<n) :
    Nat.Coprime (geometric P Q n) P := by
  cases n with
  | zero => omega
  | succ n =>
    rw [geometric_alternate]
    simp only [Nat.coprime_iff_gcd_eq_one,Nat.gcd_add_mul_left_left]
    exact coprime.symm.pow_left n

theorem geometric_coprime_smooth (A p u v n : Nat)
    (posA : 0<A) (posP : 0<p) (posN : 0<n) :
    Nat.Coprime (geometric (3^p) (2^A) n) (2^u*3^v) := by
  have cop : Nat.Coprime (3^p) (2^A) :=
    ((by decide : Nat.Coprime 3 2).pow_left p).pow_right A
  have twoPower : 2 ∣ 2^A := by
    simpa using Nat.pow_dvd_pow 2 (show 1≤A by omega)
  have threePower : 3 ∣ 3^p := by
    simpa using Nat.pow_dvd_pow 3 (show 1≤p by omega)
  have two := (geometric_coprime_right _ _ _ cop posN).coprime_dvd_right twoPower
  have three := (geometric_coprime_left _ _ _ cop posN).coprime_dvd_right threePower
  exact (two.pow_right u).mul_right (three.pow_right v)

/-- Any two parity blocks of the same length A and odd count p whose
complete carries differ by 2^u*3^v admit no mixed positive integer cycle,
uniformly in A,p,u,v and the number and ordering of the blocks. -/
theorem no_smooth_mixed_collatz_cycle (A p c u v x : Nat) (bs : List Bool)
    (posA : 0<A) (posP : 0<p)
    (hasTrue : true ∈ bs) (hasFalse : false ∈ bs) :
    (2^A)^bs.length*x ≠
      (3^p)^bs.length*x+carry (3^p) (2^A) c (2^u*3^v) bs := by
  have posN : 0<bs.length := by
    cases bs with
    | nil => simp at hasTrue
    | cons b bs => simp
  exact no_mixed_cycle _ _ _ _ _ bs (Nat.pow_pos (by decide))
    (Nat.pow_pos (by decide)) hasTrue hasFalse
    (geometric_coprime_smooth A p u v bs.length posA posP posN)

/-- The same exclusion stated directly for a closed finite path of
integer block-boundary states.  There is no bound on path length. -/
theorem no_smooth_closed_path (A p c u v x : Nat) (bs : List Bool)
    (posA : 0<A) (posP : 0<p)
    (hasTrue : true ∈ bs) (hasFalse : false ∈ bs) :
    ¬Path (3^p) (2^A) c (2^u*3^v) x bs x := by
  intro path
  exact no_smooth_mixed_collatz_cycle A p c u v x bs posA posP hasTrue hasFalse
    (path_affine _ _ _ _ bs x x path)

end CollatzBlockMixture

#print axioms CollatzBlockMixture.geometric_alternate
#print axioms CollatzBlockMixture.path_affine
#print axioms CollatzBlockMixture.geometric_balance
#print axioms CollatzBlockMixture.carry_decomposition
#print axioms CollatzBlockMixture.no_mixed_cycle
#print axioms CollatzBlockMixture.geometric_coprime_smooth
#print axioms CollatzBlockMixture.no_smooth_mixed_collatz_cycle
#print axioms CollatzBlockMixture.no_smooth_closed_path
