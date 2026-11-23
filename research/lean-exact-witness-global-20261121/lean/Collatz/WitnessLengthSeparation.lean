/-
The original residue implication needs output lengths unbounded even on
four-step input witnesses.  This module constructs the inputs and proves an
arbitrary-length forced positive prefix for every possible output witness.
It does not assert the existence of those output witnesses.
-/
import Collatz.HighGapPump
import Collatz.RootedSourceFloor

open CollatzWitness CollatzGapMultiset CollatzHighGapPump

set_option autoImplicit false
set_option maxHeartbeats 3000000

namespace CollatzWitnessLengthSeparation

private def seed : Nat := 222399981598543

/-- An integral presentation of (4^(27h)-1)/81. -/
def parameter : Nat → Nat
  | 0 => 0
  | h+1 => 4^27 * parameter h + seed

def input (h : Nat) : Nat := 256 * parameter (h+1) + 1
def output (h : Nat) : Nat := 128 * parameter (h+1) + 1
def exponent (h : Nat) : Nat := 27*(h+1)
def inputWord (h : Nat) : List Nat := [2,2,2,2*exponent h+2]
def forcedWord (h : Nat) : List Nat :=
  [2,2,2,1] ++ List.replicate (exponent h-1) 2

private theorem parameter_identity (h : Nat) :
    4^(27*h)=81*parameter h+1 := by
  induction h with
  | zero => simp [parameter]
  | succ h ih =>
    have seedIdentity : 81*seed+1=4^27 := by decide
    rw [show 27*(h+1)=27*h+27 by omega,Nat.pow_add,ih,parameter]
    grind

private theorem parameter_positive_odd (h : Nat) :
    0<parameter (h+1) ∧ parameter (h+1)%2=1 := by
  constructor
  · simp only [parameter,seed]; omega
  · change (18014398509481984*parameter h+222399981598543)%2=1
    omega

private theorem factor_unique (a b u v : Nat)
    (uOdd : u%2=1) (vOdd : v%2=1) (eq : 2^a*u=2^b*v) : a=b ∧ u=v := by
  have notLess (a b u v : Nat) (uOdd : u%2=1)
      (eq : 2^a*u=2^b*v) : ¬a<b := by
    intro less
    obtain ⟨d,hd⟩ := Nat.exists_eq_add_of_le (show a+1≤b by omega)
    have shape : b=a+(d+1) := by omega
    rw [shape,Nat.pow_add] at eq
    have cancel : u=2^(d+1)*v := by
      apply Nat.eq_of_mul_eq_mul_left (Nat.pow_pos (by decide) : 0<2^a)
      simpa [Nat.mul_assoc] using eq
    rw [Nat.pow_succ] at cancel
    have even : u=2*(2^d*v) := by grind
    omega
  have same : a=b := by
    have left := notLess a b u v uOdd eq
    have right := notLess b a v u vOdd eq.symm
    omega
  subst b
  exact ⟨rfl,Nat.eq_of_mul_eq_mul_left (Nat.pow_pos (by decide)) eq⟩

/-- Every displayed odd state, including the last one, exceeds one. -/
private inductive Forced : Nat → List Nat → Nat → Prop
  | nil (n : Nat) (large : 1<n) (odd : n%2=1) : Forced n [] n
  | cons (n m endpoint a : Nat) (tail : List Nat)
      (large : 1<n) (positive : 0<a)
      (edge : 3*n+1=2^a*m) (rest : Forced m tail endpoint) :
      Forced n (a::tail) endpoint

private theorem forced_source_odd {n endpoint : Nat} {word : List Nat}
    (path : Forced n word endpoint) : n%2=1 := by
  cases path with
  | nil n large odd => exact odd
  | cons n m endpoint a tail large positive edge rest =>
    obtain ⟨b,rfl⟩ := Nat.exists_eq_succ_of_ne_zero (by omega : a≠0)
    rw [Nat.pow_succ] at edge
    have even : 3*n+1=2*(2^b*m) := by grind
    omega

private theorem forced_prefix {n endpoint : Nat} {word : List Nat}
    (path : Forced n word endpoint) : Prefix n word endpoint := by
  induction path with
  | nil n large odd => simp [Prefix,PositiveGaps,correction,total]
  | cons n m endpoint a tail large positive edge rest ih =>
    exact (prefix_cons_iff n a endpoint tail).mpr ⟨positive,m,edge,ih⟩

private theorem forced_append {n middle endpoint : Nat} {front tail : List Nat}
    (first : Forced n front middle) (last : Forced middle tail endpoint) :
    Forced n (front++tail) endpoint := by
  induction first with
  | nil => exact last
  | cons n m middle a front large positive edge rest ih =>
    exact Forced.cons n m endpoint a (front++tail) large positive edge (ih last)

/-- Determinism consumes this entire supplied prefix from EVERY complete
certificate, including certificates with larger length or terminal padding. -/
private theorem forced_consumes {n endpoint : Nat} {front : List Nat}
    (path : Forced n front endpoint) (word : List Nat)
    (cert : Certificate n word) :
    ∃ tail, word=front++tail ∧ Certificate endpoint tail ∧ tail≠[] := by
  induction path generalizing word with
  | nil n large odd =>
    refine ⟨word,rfl,cert,?_⟩
    intro empty
    have one : n=1 := by simpa [empty,Certificate,correction,total] using cert.2
    omega
  | cons n m endpoint a front large positive edge rest ih =>
    cases word with
    | nil =>
      have one : n=1 := by simpa [Certificate,correction,total] using cert.2
      omega
    | cons b word =>
      obtain ⟨_,v,other,complete⟩ := (certificate_cons_iff n b word).mp cert
      have vOdd := witness_odd (certificate_witness complete)
      have mOdd := forced_source_odd rest
      obtain ⟨sameGap,sameEnd⟩ := factor_unique a b m v mOdd vOdd (by omega)
      subst b
      subst v
      obtain ⟨tail,shape,completeTail,nonempty⟩ := ih word complete
      exact ⟨tail,by simp [shape],completeTail,nonempty⟩

private theorem geometric_forced (j k : Nat) :
    Forced (3^j*4^(k+1)+1) (List.replicate k 2) (4*3^(j+k)+1) := by
  induction k generalizing j with
  | zero =>
    simpa [Nat.mul_comm] using Forced.nil (4*3^j+1)
      (by have := Nat.pow_pos (by decide : 0<3) (n:=j); omega) (by omega)
  | succ k ih =>
    have first : 1<3^j*4^(k+1+1)+1 := by
      have := Nat.mul_pos (Nat.pow_pos (by decide : 0<3) (n:=j))
        (Nat.pow_pos (by decide : 0<4) (n:=k+1+1))
      omega
    have edge : 3*(3^j*4^(k+1+1)+1)+1=2^2*(3^(j+1)*4^(k+1)+1) := by
      simp only [Nat.pow_succ]
      grind
    have last := ih (j+1)
    have endpoint : (j+1)+k=j+(k+1) := by omega
    rw [endpoint] at last
    simpa [List.replicate_succ] using
      Forced.cons _ _ _ 2 _ first (by decide) edge last

private theorem target_forced (h : Nat) :
    Forced (output h) (forcedWord h) (4*3^(exponent h-1)+1) := by
  let K := parameter (h+1)
  let m := exponent h
  have kp : 0<K := (parameter_positive_odd h).1
  have mPositive : 0<m := by simp [m,exponent]
  have identity : 4^m=81*K+1 := parameter_identity (h+1)
  have last := geometric_forced 0 (m-1)
  have mEq : m-1+1=m := by omega
  simp only [Nat.pow_zero,Nat.one_mul,Nat.zero_add,mEq] at last
  have coreOdd : (4^m+1)%2=1 := by
    obtain ⟨k,eq⟩ := Nat.exists_eq_succ_of_ne_zero (by omega : m≠0)
    rw [eq,Nat.pow_succ]
    omega
  have coreLarge : 1<4^m+1 := by have := Nat.pow_pos (by decide : 0<4) (n:=m); omega
  have front : Forced (128*K+1) [2,2,2,1] (4^m+1) := by
    apply Forced.cons _ (96*K+1) _ 2 _ (by omega) (by decide) (by omega)
    apply Forced.cons _ (72*K+1) _ 2 _ (by omega) (by decide) (by omega)
    apply Forced.cons _ (54*K+1) _ 2 _ (by omega) (by decide) (by omega)
    apply Forced.cons _ (4^m+1) _ 1 _ (by omega) (by decide) (by omega)
    exact Forced.nil _ coreLarge coreOdd
  exact forced_append front last

/-- Every member has an actual four-gap input certificate and exactly the
requested residue 257. Its final exponent is unrestricted. -/
theorem four_step_input (h : Nat) :
    (inputWord h).length=4 ∧ Certificate (input h) (inputWord h) ∧
    input h%512=257 ∧ (input h+1)/2=output h := by
  have kp := parameter_positive_odd h
  have identity := parameter_identity (h+1)
  have power : 2^(2*exponent h+8)=256*4^exponent h := by
    rw [Nat.pow_add,Nat.pow_mul]
    change 4^exponent h*256=256*4^exponent h
    omega
  have cert : Certificate (input h) (inputWord h) := by
    constructor
    · simp [inputWord,PositiveGaps]
    · simp only [inputWord,List.length_cons,List.length_nil,
        correction,total,Nat.pow_zero,Nat.mul_zero,Nat.add_zero]
      have exponents : 2+(2+(2+(2*exponent h+2)))=2*exponent h+8 := by omega
      rw [exponents,power]
      change 81*(256*parameter (h+1)+1)+175=256*4^exponent h
      unfold exponent
      omega
  exact ⟨rfl,cert,by unfold input; omega,by unfold input output; omega⟩

/-- Both clocks are physical clocks of the original integers. The input
has reached one after 2m+8 clocks; at clock 2m+7 the output is 3^m+1.
The displayed odd prefix is unconditional, independently of output success. -/
theorem exact_clocks (h : Nat) :
    Prefix (output h) (forcedWord h) (4*3^(exponent h-1)+1) ∧
    CollatzRootedSourceFloor.orbit (input h) (2*exponent h+8)=1 ∧
    CollatzRootedSourceFloor.orbit (output h) (2*exponent h+7)=3^exponent h+1 ∧
    3^exponent h+1<output h := by
  have path := forced_prefix (target_forced h)
  have complete := (four_step_input h).2.1
  have sourcePath : Prefix (input h) (inputWord h) 1 := by
    simpa [Prefix,Certificate] using complete
  have sourceClock := CollatzRootedSourceFloor.prefix_clock _ _ _ sourcePath
  have sourceTotal : total (inputWord h)=2*exponent h+8 := by
    simp only [inputWord,total]
    omega
  rw [sourceTotal] at sourceClock
  have repeatTotal (k : Nat) : total (List.replicate k 2)=2*k := by
    induction k with
    | zero => rfl
    | succ k ih => simp [List.replicate_succ,total,ih]; omega
  have mPositive : 0<exponent h := by unfold exponent; omega
  have targetTotal : total (forcedWord h)=2*exponent h+5 := by
    simp only [forcedWord,total_append,total,repeatTotal]
    omega
  have targetClock := CollatzRootedSourceFloor.prefix_clock _ _ _ path
  rw [targetTotal] at targetClock
  have lastEdge : 3*(4*3^(exponent h-1)+1)+1=2^2*(3^exponent h+1) := by
    have power : 3^exponent h=3^(exponent h-1)*3 := by
      rw [←Nat.pow_succ,show (exponent h-1).succ=exponent h by omega]
    rw [power]
    grind
  have last := CollatzRootedSourceFloor.orbit_gap _ 2 _ (by decide) lastEdge
  refine ⟨path,sourceClock,?_,?_⟩
  · rw [show 2*exponent h+7=(2*exponent h+5)+2 by omega,
      CollatzRootedSourceFloor.orbit_add,targetClock]
    exact last
  · have powers := Nat.pow_lt_pow_left (by decide : 3<4)
      (by omega : exponent h≠0)
    have identity := parameter_identity (h+1)
    have positive := (parameter_positive_odd h).1
    change 3^exponent h+1<128*parameter (h+1)+1
    change 4^exponent h=81*parameter (h+1)+1 at identity
    omega

/-- An arbitrary complete output witness contains the full displayed actual
prefix and a nonempty complete tail at its endpoint. -/
theorem output_prefix_and_tail (h : Nat) (word : List Nat)
    (cert : Certificate (output h) word) :
    Prefix (output h) (forcedWord h) (4*3^(exponent h-1)+1) ∧
    ∃ tail, word=forcedWord h++tail ∧
      Certificate (4*3^(exponent h-1)+1) tail ∧ tail≠[] := by
  exact ⟨forced_prefix (target_forced h),forced_consumes (target_forced h) word cert⟩

/-- Four odd steps on the input force at least 27(h+1)+4 odd steps in
every possible complete output witness. Output existence is not assumed. -/
theorem output_length_lower_bound (h : Nat) (word : List Nat)
    (cert : Certificate (output h) word) : exponent h+4≤word.length := by
  obtain ⟨_,tail,shape,_,nonempty⟩ := output_prefix_and_tail h word cert
  have tailPositive : 0<tail.length := by
    cases tail with
    | nil => exact False.elim (nonempty rfl)
    | cons => simp
  have mPositive : 0<exponent h := by unfold exponent; omega
  rw [shape,List.length_append]
  simp only [forcedWord,List.length_append,List.length_cons,List.length_nil,
    List.length_replicate]
  omega

/-- The bound applies verbatim to the increasing-tuple formulation in the
question, preserving its given length r and every exponent. -/
theorem tuple_length_lower_bound (h r : Nat) (A : Nat → Nat)
    (zero : A 0=0) (increasing : Increasing r A)
    (identity : 3^r*output h+offset A r=2^(A r)) : exponent h+4≤r := by
  obtain ⟨word,positive,length,scheduleEq⟩ := schedule_exists r A zero increasing
  have correctionEq : correction word=offset A r := by
    rw [←offset_schedule,length]
    exact offset_congr (fun i hi => scheduleEq i (by omega))
  have totalEq : total word=A r := by
    rw [←schedule_end,length]
    exact scheduleEq r (by omega)
  have complete : Certificate (output h) word := by
    refine ⟨positive,?_⟩
    simpa [length,correctionEq,totalEq] using identity
  have bound := output_length_lower_bound h word complete
  omega

/-- For every proposed bound, a four-step input has no output certificate
of length at most that bound. This rules out a total bounded-length
transformer without assuming that any output certificate exists. -/
theorem no_input_length_bound (bound : Nat) :
    ∃ x word, word.length=4 ∧ Certificate x word ∧ x%512=257 ∧
      ∀ r A, A 0=0 → Increasing r A →
        3^r*((x+1)/2)+offset A r=2^(A r) → bound<r := by
  obtain ⟨length,complete,residue,half⟩ := four_step_input bound
  refine ⟨input bound,inputWord bound,length,complete,residue,?_⟩
  intro r A zero increasing identity
  rw [half] at identity
  have lower := tuple_length_lower_bound bound r A zero increasing identity
  unfold exponent at lower
  omega

end CollatzWitnessLengthSeparation
