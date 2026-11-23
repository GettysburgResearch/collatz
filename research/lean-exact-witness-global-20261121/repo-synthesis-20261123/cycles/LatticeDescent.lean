/-
Integer lattice descent for arbitrary successive long repetitions of one
contracting affine Collatz word, separated by arbitrary certified defects.
Core/Std only.  No universal word decomposition or Collatz axiom is assumed.
-/
import Std

set_option autoImplicit false
set_option maxHeartbeats 2000000

namespace CollatzLatticeDescent

/-- The exact integer affine edge after normalization by the common lattice. -/
def PaidEdge (x y : Int) : Prop :=
  ∃ a b : Nat, ∃ e : Int, a + e.natAbs < b ∧ (b:Int)*y = a*x+e

private theorem edge_size (a b : Nat) (e x y : Int)
    (edge : (b:Int)*y = a*x+e) :
    b*y.natAbs ≤ a*x.natAbs+e.natAbs := by
  have h := Int.natAbs_add_le ((a:Int)*x) e
  rw [←edge] at h
  simpa only [Int.natAbs_mul, Int.natAbs_natCast] using h

theorem paid_zero (y : Int) (edge : PaidEdge 0 y) : y=0 := by
  obtain ⟨a,b,e,budget,eq⟩ := edge
  have bound := edge_size a b e 0 y eq
  have zero : y.natAbs=0 := by
    apply Classical.byContradiction
    intro bad
    have one : 1≤y.natAbs := by omega
    have lower := Nat.mul_le_mul_left b one
    simp only [Nat.mul_one, Int.natAbs_zero, Nat.mul_zero,
      Nat.zero_add] at lower bound
    omega
  exact Int.natAbs_eq_zero.mp zero

theorem paid_strict (x y : Int) (nonzero : x≠0)
    (edge : PaidEdge x y) : y.natAbs < x.natAbs := by
  obtain ⟨a,b,e,budget,eq⟩ := edge
  have bound := edge_size a b e x y eq
  have positive : 0<x.natAbs := Int.natAbs_pos.mpr nonzero
  have below := Nat.mul_lt_mul_of_pos_right budget positive
  have error := Nat.mul_le_mul_left e.natAbs (show 1≤x.natAbs by omega)
  rw [Nat.add_mul] at below
  simp only [Nat.mul_one] at error
  apply Classical.byContradiction
  intro bad
  have order : x.natAbs ≤ y.natAbs := by omega
  have lower := Nat.mul_le_mul_left b order
  omega

theorem paid_weak (x y : Int) (edge : PaidEdge x y) :
    y.natAbs ≤ x.natAbs := by
  by_cases zero : x=0
  · subst x
    have zy := paid_zero y edge
    simp [zy]
  · exact Nat.le_of_lt (paid_strict x y zero edge)

/-- An all-time paid trace reaches zero by its initial integer magnitude.
This is a finite explicit clock bound, not only a well-founded existence. -/
theorem paid_clock (h : Nat → Int)
    (edges : ∀ j, PaidEdge (h j) (h (j+1))) :
    ∀ j, (h j).natAbs ≤ (h 0).natAbs-j := by
  intro j
  induction j with
  | zero => simp
  | succ j ih =>
      by_cases hz : h j=0
      · have next := paid_zero (h (j+1)) (by simpa [hz] using edges j)
        simp [next]
      · have drop := paid_strict (h j) (h (j+1)) hz (edges j)
        omega

theorem paid_hit (h : Nat → Int)
    (edges : ∀ j, PaidEdge (h j) (h (j+1))) :
    h (h 0).natAbs = 0 := by
  have bound := paid_clock h edges (h 0).natAbs
  exact Int.natAbs_eq_zero.mp (by omega)

theorem paid_tail_zero (h : Nat → Int)
    (edges : ∀ j, PaidEdge (h j) (h (j+1)))
    (j : Nat) (late : (h 0).natAbs ≤ j) : h j=0 := by
  have bound := paid_clock h edges j
  exact Int.natAbs_eq_zero.mp (by omega)

/-- Literal repetition of an affine block, with every intermediate integer
retained.  Instantiating it with a Collatz word uses that word's actual
ordinary intermediate endpoints, not its rational completion. -/
def Repeat (P Q C : Int) : Nat → Int → Int → Prop
  | 0, x, y => x=y
  | k+1, x, y => ∃ v, Q*v=P*x+C ∧ Repeat P Q C k v y

theorem block_displacement (P Q C x y : Int)
    (edge : Q*y=P*x+C) :
    Q*((Q-P)*y-C)=P*((Q-P)*x-C) := by
  have h := congrArg ((Q-P)*·) edge
  grind

theorem repeat_displacement (P Q C : Int) (k : Nat) (x y : Int)
    (path : Repeat P Q C k x y) :
    Q^k*((Q-P)*y-C)=P^k*((Q-P)*x-C) := by
  induction k generalizing x y with
  | zero =>
      have eq : x=y := path
      subst y
      simp
  | succ k ih =>
      obtain ⟨v,edge,tail⟩ := path
      have first := block_displacement P Q C x v edge
      have rest := ih v y tail
      have f := congrArg (P^k*·) first
      have r := congrArg (Q*·) rest
      simp only [Int.pow_succ]
      grind

theorem repeat_lattice (P Q : Nat) (C : Int) (k : Nat) (x y : Int)
    (coprime : Nat.Coprime Q P)
    (path : Repeat P Q C k x y) :
    ((Q^k:Nat):Int) ∣ ((Q:Int)-P)*x-C := by
  have eq := repeat_displacement P Q C k x y path
  have product : ((Q^k:Nat):Int) ∣ ((P^k:Nat):Int)*(((Q:Int)-P)*x-C) := by
    refine ⟨((Q:Int)-P)*y-C, ?_⟩
    simpa using eq.symm
  have natProduct : Q^k ∣ P^k*((((Q:Int)-P)*x-C).natAbs) := by
    simpa [Int.natAbs_mul] using Int.ofNat_dvd_left.mp product
  have cop := (coprime.pow_left k).pow_right k
  exact Int.ofNat_dvd_left.mpr (cop.dvd_of_dvd_mul_left natProduct)

theorem macro_displacement (P Q C R S B : Int) (k : Nat) (x v y : Int)
    (run : Repeat P Q C k x v) (defect : S*y=R*v+B) :
    S*Q^k*((Q-P)*y-C) =
      R*P^k*((Q-P)*x-C)+Q^k*((Q-P)*B-(S-R)*C) := by
  have repeated := repeat_displacement P Q C k x v run
  have one := congrArg ((Q-P)*·) defect
  have r := congrArg (R*·) repeated
  have s := congrArg (Q^k*·) one
  grind

/-- Once the source and target displacement are written in the common
ordinary lattice, the exact macro identity is a PaidEdge. -/
theorem macro_paid (P Q R S D : Nat) (E h h' : Int) (k : Nat)
    (budget : R*P^k*D+E.natAbs*Q^k < S*Q^k*D)
    (correctTarget : (S:Int)*Q^k*(D*h') =
      (R:Int)*P^k*(D*h)+Q^k*E) : PaidEdge h h' := by
  refine ⟨R*P^k*D,S*Q^k*D,(Q:Int)^k*E,?_,?_⟩
  · simpa [Int.natAbs_mul,Int.natAbs_pow,Nat.mul_comm] using budget
  · simpa [Int.mul_assoc] using correctTarget

theorem power_ratio_mono (P Q K k : Nat) (ordered : P≤Q) (long : K≤k) :
    P^k*Q^K ≤ P^K*Q^k := by
  obtain ⟨j,rfl⟩ := Nat.exists_eq_add_of_le long
  have bound := Nat.mul_le_mul_left (P^K*Q^K) (Nat.pow_le_pow_left ordered j)
  simpa [Nat.pow_add,Nat.mul_assoc,Nat.mul_comm,Nat.mul_left_comm] using bound

/-- One finite cutoff certificate pays every larger independent exponent. -/
theorem cutoff_budget (P Q R S E K k : Nat)
    (positive : 0<Q) (ordered : P≤Q) (long : K≤k)
    (cutoff : R*P^K+E < S*Q^K) :
    R*P^k*Q^K+E*Q^k < S*Q^k*Q^K := by
  have ratio := Nat.mul_le_mul_left R (power_ratio_mono P Q K k ordered long)
  have scaled := Nat.mul_lt_mul_of_pos_right cutoff
    (Nat.pow_pos positive (n:=k))
  have term : R*P^k*Q^K ≤ R*P^K*Q^k := by
    simpa [Nat.mul_assoc] using ratio
  have bound := Nat.lt_of_le_of_lt (Nat.add_le_add_right term (E*Q^k))
    (show R*P^K*Q^k+E*Q^k < S*Q^K*Q^k by
      simpa [Nat.add_mul,Nat.mul_assoc] using scaled)
  simpa [Nat.mul_assoc,Nat.mul_comm,Nat.mul_left_comm] using bound

theorem run_lattice (P Q K k : Nat) (C x v : Int)
    (coprime : Nat.Coprime Q P) (long : K≤k)
    (run : Repeat P Q C k x v) :
    ((Q^K:Nat):Int) ∣ ((Q:Int)-P)*x-C := by
  have small : ((Q^K:Nat):Int) ∣ ((Q^k:Nat):Int) :=
    Int.ofNat_dvd.mpr (Nat.pow_dvd_pow Q long)
  exact Int.dvd_trans small (repeat_lattice P Q C k x v coprime run)

theorem uniform_macro_paid (P Q R S K k : Nat) (C B x v y h h' : Int)
    (positive : 0<Q) (ordered : P≤Q) (long : K≤k)
    (run : Repeat P Q C k x v) (defect : (S:Int)*y=R*v+B)
    (source : ((Q:Int)-P)*x-C = ((Q^K:Nat):Int)*h)
    (target : ((Q:Int)-P)*y-C = ((Q^K:Nat):Int)*h')
    (cutoff : R*P^K+(((Q:Int)-P)*B-((S:Int)-R)*C).natAbs < S*Q^K) :
    PaidEdge h h' := by
  have transport := macro_displacement P Q C R S B k x v y run defect
  rw [source,target] at transport
  exact macro_paid P Q R S (Q^K) _ h h' k
    (cutoff_budget P Q R S _ K k positive ordered long cutoff) (by
      simpa using transport)

/-- Complete all-time ordinary affine consumer.  Defect types and run
lengths may change at every step, without any finite-alphabet assumption.
All intermediate repeated-block endpoints are actual integers. -/
theorem arbitrary_defect_hit (P Q K : Nat) (C : Int)
    (x v B : Nat → Int) (R S k : Nat → Nat)
    (positive : 0<Q) (ordered : P≤Q) (coprime : Nat.Coprime Q P)
    (long : ∀ j, K≤k j)
    (run : ∀ j, Repeat P Q C (k j) (x j) (v j))
    (defect : ∀ j, (S j:Int)*x (j+1)=R j*v j+B j)
    (cutoff : ∀ j, R j*P^K+
      (((Q:Int)-P)*B j-((S j:Int)-R j)*C).natAbs < S j*Q^K) :
    let H := ((((Q:Int)-P)*x 0-C)/((Q^K:Nat):Int)).natAbs
    ∀ j, H≤j → ((Q:Int)-P)*x j=C := by
  let h : Nat → Int := fun j => (((Q:Int)-P)*x j-C)/((Q^K:Nat):Int)
  have normalized : ∀ j, ((Q:Int)-P)*x j-C=((Q^K:Nat):Int)*h j := by
    intro j
    exact (Int.mul_ediv_cancel_of_dvd
      (run_lattice P Q K (k j) C (x j) (v j) coprime (long j) (run j))).symm
  have edges : ∀ j, PaidEdge (h j) (h (j+1)) := by
    intro j
    exact uniform_macro_paid P Q (R j) (S j) K (k j) C (B j)
      (x j) (v j) (x (j+1)) (h j) (h (j+1)) positive ordered (long j)
      (run j) (defect j) (normalized j) (normalized (j+1)) (cutoff j)
  change ∀ j, (h 0).natAbs≤j → ((Q:Int)-P)*x j=C
  intro j late
  have zero := paid_tail_zero h edges j late
  have eq := normalized j
  rw [zero,Int.mul_zero] at eq
  omega

def wordMultiplier : List Bool → Nat
  | [] => 1
  | b::bs => (if b then 3 else 1)*wordMultiplier bs

def wordCarry : List Bool → Nat
  | [] => 0
  | b::bs => wordMultiplier bs*(if b then 1 else 0)+2*wordCarry bs

/-- A literal positive shortcut trace, retaining every branch and endpoint. -/
def WordTrace : List Bool → Int → Int → Prop
  | [], x, y => 0<x ∧ x=y
  | b::bs, x, y => 0<x ∧ x%2=(if b then 1 else 0) ∧
      ∃ v, 2*v=(if b then 3*x+1 else x) ∧ WordTrace bs v y

theorem word_affine (w : List Bool) (x y : Int) (trace : WordTrace w x y) :
    ((2^w.length:Nat):Int)*y=(wordMultiplier w:Int)*x+wordCarry w := by
  induction w generalizing x y with
  | nil =>
      have eq : x=y := trace.2
      simp [eq,wordMultiplier,wordCarry]
  | cons b bs ih =>
      obtain ⟨_,_,v,edge,tail⟩ := trace
      have rest := ih v y tail
      have scaled := congrArg (fun z : Int => 2*z) rest
      have first := congrArg (fun z : Int => (wordMultiplier bs:Int)*z) edge
      cases b <;>
        simp only [wordMultiplier,wordCarry,List.length_cons,Nat.pow_succ,
          Bool.false_eq_true,ite_false,ite_true,Int.natCast_mul,Int.natCast_add,
          Nat.mul_one,Nat.mul_zero,Nat.zero_add] at * <;> grind

theorem word_coprime (w : List Bool) : Nat.Coprime (2^w.length) (wordMultiplier w) := by
  have odd : Nat.Coprime 2 (wordMultiplier w) := by
    induction w with
    | nil => simp [wordMultiplier]
    | cons b bs ih =>
      cases b with
      | false => simpa [wordMultiplier] using ih
      | true => exact (by decide : Nat.Coprime 2 3).mul_right ih
  exact odd.pow_left w.length

def WordRepeat (w : List Bool) : Nat → Int → Int → Prop
  | 0, x, y => x=y
  | k+1, x, y => ∃ v, WordTrace w x v ∧ WordRepeat w k v y

theorem word_repeat_affine (w : List Bool) (k : Nat) (x y : Int)
    (run : WordRepeat w k x y) :
    Repeat (wordMultiplier w) (2^w.length) (wordCarry w) k x y := by
  induction k generalizing x y with
  | zero => exact run
  | succ k ih =>
      obtain ⟨v,head,tail⟩ := run
      exact ⟨v,word_affine w x v head,ih v y tail⟩

/-- End-to-end consumer for literal positive ordinary words.  Every defect
word and repetition exponent may vary independently at every boundary.
The finite arithmetic cutoff is a displayed hypothesis, not an axiom. -/
theorem ordinary_word_language_hit (u : List Bool) (K : Nat)
    (t : Nat → List Bool) (x v : Nat → Int) (k : Nat → Nat)
    (contracting : wordMultiplier u < 2^u.length)
    (long : ∀ j, K≤k j)
    (runs : ∀ j, WordRepeat u (k j) (x j) (v j))
    (defects : ∀ j, WordTrace (t j) (v j) (x (j+1)))
    (cutoff : ∀ j, wordMultiplier (t j)*(wordMultiplier u)^K+
      ((((2^u.length:Nat):Int)-(wordMultiplier u:Int))*wordCarry (t j)-
        (((2^(t j).length:Nat):Int)-(wordMultiplier (t j):Int))*
          wordCarry u).natAbs < 2^(t j).length*(2^u.length)^K) :
    ∀ j, (((((2^u.length:Nat):Int)-(wordMultiplier u:Int))*x 0-
      wordCarry u)/(((2^u.length)^K:Nat):Int)).natAbs≤j →
      (((2^u.length:Nat):Int)-(wordMultiplier u:Int))*x j=wordCarry u := by
  apply arbitrary_defect_hit (wordMultiplier u) (2^u.length) K (wordCarry u)
    x v (fun j => wordCarry (t j)) (fun j => wordMultiplier (t j))
    (fun j => 2^(t j).length) k
  · exact Nat.pow_pos (by decide) (n:=u.length)
  · exact Nat.le_of_lt contracting
  · exact word_coprime u
  · exact long
  · intro j
    exact word_repeat_affine u (k j) (x j) (v j) (runs j)
  · intro j
    exact word_affine (t j) (v j) (x (j+1)) (defects j)
  · intro j
    exact cutoff j

#print axioms paid_zero
#print axioms paid_strict
#print axioms paid_weak
#print axioms paid_clock
#print axioms paid_hit
#print axioms paid_tail_zero
#print axioms block_displacement
#print axioms repeat_displacement
#print axioms repeat_lattice
#print axioms macro_displacement
#print axioms macro_paid
#print axioms power_ratio_mono
#print axioms cutoff_budget
#print axioms run_lattice
#print axioms uniform_macro_paid
#print axioms arbitrary_defect_hit
#print axioms word_affine
#print axioms word_coprime
#print axioms word_repeat_affine
#print axioms ordinary_word_language_hit

end CollatzLatticeDescent
