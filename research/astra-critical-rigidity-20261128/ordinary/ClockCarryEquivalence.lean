import PrefixCarryClosure
import PairedClock
import Mathlib.Data.Nat.Find

/-! Exact finite maxima, in the native shortcut clock. The "clock" side
quantifies ordinary positive odd integer sources; the "carry" side quantifies
finite Boolean words with the ordered offset equation. -/

set_option autoImplicit false
namespace Collatz.ClockCarryEquivalence
open Collatz.PoweredAffine
open Collatz.PrefixCarryClosure

private theorem orbit_shift (n k : Nat) : PairedClock.orbit n (k+1)=PairedClock.orbit (step n) k := by
  induction k with
  | zero => rfl
  | succ k ih => change PairedClock.step (PairedClock.orbit n (k+1))=PairedClock.step (PairedClock.orbit (step n) k); rw [ih]

private theorem orbit_agrees (n k : Nat) : orbit n k=PairedClock.orbit n k := by
  induction k generalizing n with
  | zero => rfl
  | succ k ih => exact (ih (step n)).trans (orbit_shift n k).symm

private theorem grade_depart (n k : Nat) :
    PairedClock.grade n (k+1)=n%2+PairedClock.grade (step n) k := by
  induction k with
  | zero => simp [PairedClock.grade,PairedClock.orbit]
  | succ k ih =>
    change PairedClock.grade n (k+1)+PairedClock.orbit n (k+1)%2=n%2+(PairedClock.grade (step n) k+PairedClock.orbit (step n) k%2)
    rw [ih,orbit_shift]
    omega

private theorem grade_of_realizes (n : Nat) (w : List Bool) (hw : Realizes n w) :
    PairedClock.grade n w.length=ones w := by
  induction w generalizing n with
  | nil => rfl
  | cons b w ih =>
    rw [List.length_cons,grade_depart,ih _ hw.2,hw.1]
    rfl

private theorem orbit_add (n k d : Nat) :
    PairedClock.orbit n (k+d)=PairedClock.orbit (PairedClock.orbit n k) d := by
  induction d with
  | zero => rfl
  | succ d ih => change PairedClock.step (PairedClock.orbit n (k+d))=_; rw [ih]; rfl

private theorem grade_add (n k d : Nat) :
    PairedClock.grade n (k+d)=PairedClock.grade n k+PairedClock.grade (PairedClock.orbit n k) d := by
  induction d with
  | zero => simp [PairedClock.grade]
  | succ d ih =>
    change PairedClock.grade n (k+d)+PairedClock.orbit n (k+d)%2=PairedClock.grade n k+
      (PairedClock.grade (PairedClock.orbit n k) d+PairedClock.orbit (PairedClock.orbit n k) d%2)
    rw [ih,orbit_add]
    omega

private theorem prefix_grade (s : Nat) (odd : s%2=1) :
    PairedClock.grade s 2+PairedClock.grade (3*s) 2=3 := by
  have odd3 : 3*s%2=1 := by omega
  have A := odd_step odd
  have B := odd_step odd3
  change (0+s%2+step s%2)+(0+(3*s)%2+step (3*s)%2)=3
  omega

private def nativeWord (s : Nat) : Nat → List Bool
  | 0 => []
  | k+1 => decide (s%2=1)::nativeWord (step s) k

private theorem native_length (s k : Nat) : (nativeWord s k).length=k := by
  induction k generalizing s with
  | zero => rfl
  | succ k ih => simp [nativeWord,ih]

private theorem native_realizes (s k : Nat) : Realizes s (nativeWord s k) := by
  induction k generalizing s with
  | zero => trivial
  | succ k ih =>
    refine ⟨?_,ih _⟩
    by_cases h : s%2=1
    · simp [h]
    · simp [h]; omega

/-- An ordinary odd source stays value-unmerged through the native date
and uses a bounded total number of odd shortcut letters. -/
def HasClock (G k : Nat) : Prop := ∃ s : Nat, s%2=1 ∧
  PairedClock.grade s k+PairedClock.grade (3*s) k≤G ∧ ∀ i≤k, PairedClock.orbit s i≠PairedClock.orbit (3*s) i

/-- Two words of equal length and positive equal grade obey the ordered
affine correction equation. -/
def HasCarry (P L : Nat) : Prop := ∃ u v : List Bool,
  u.length=L ∧ v.length=L ∧ 1≤ones u ∧ ones u=ones v ∧ ones u≤P ∧
  numerator u+3^ones u=numerator v+2^L

private theorem small_carry {P : Nat} (hp : 1≤P) : HasCarry P 2 := by
  exact ⟨[false,true],[true,false],rfl,rfl,by decide,rfl,hp,by decide⟩

/-- Every static solution has a true positive odd source unmerged through
two more native dates, including the three initial odd departures. -/
theorem carry_to_clock {P L : Nat} (hc : HasCarry P L) : HasClock (2*P+3) (L+2) := by
  obtain ⟨u,v,ul,vl,lo,gr,hi,eq⟩ := hc
  have len : u.length=v.length := ul.trans vl.symm
  rw [←ul] at eq
  obtain ⟨s,_,odd,hu,hv,_,sep⟩ := Collatz.AdjacentWordClosure.ordinary_lifts_arbitrarily_large
    u v len gr eq 0
  have a := grade_of_realizes _ u hu
  have b := grade_of_realizes _ v hv
  rw [orbit_agrees,ul] at a
  rw [orbit_agrees,vl] at b
  have init := prefix_grade s odd
  refine ⟨s,odd,?_,?_⟩
  · rw [Nat.add_comm L 2,grade_add,grade_add]
    omega
  · intro i h
    have orig := sep i (by omega)
    simpa only [orbit_agrees] using orig

/-- Close *every* ordinary unmatched horizon to a static solution of at
least that length and at most sixteen times one plus its original grade. -/
theorem clock_to_carry {G k : Nat} (hc : HasClock G k) :
    ∃ L, k≤L ∧ HasCarry (16*(G+1)) L := by
  obtain ⟨s,odd,budget,sep⟩ := hc
  cases k with
  | zero => exact ⟨2,by decide,small_carry (by omega)⟩
  | succ k =>
    let u := nativeWord (step s) k
    let v := nativeWord (step (3*s)) k
    have ul : u.length=k := native_length _ _
    have vl : v.length=k := native_length _ _
    have hu : Realizes (step s) u := native_realizes _ _
    have hv : Realizes (step (3*s)) v := native_realizes _ _
    have gu := grade_of_realizes _ u hu
    have gv := grade_of_realizes _ v hv
    rw [ul] at gu
    rw [vl] at gv
    have odd3 : (3*s)%2=1 := by omega
    rw [grade_depart,grade_depart,odd,odd3] at budget
    have diff : orbit (step s) u.length≠orbit (step (3*s)) v.length := by
      rw [ul,vl,orbit_agrees,orbit_agrees,←orbit_shift,←orbit_shift]
      exact sep _ (by omega)
    obtain ⟨tu,tv,lengths,lo,gr,hi,eq⟩ := close_positive_source_suffix s G u v odd
      (ul.trans vl.symm) hu hv diff (by omega)
    let U := false::(u++tu)
    let V := true::(v++tv)
    exact ⟨U.length,by simp [U,ul],U,V,rfl,lengths.symm,lo,gr,hi,eq⟩

private def cap (G : Nat) : Nat := (2*(G+1)+1)*G

private theorem clock_bound {G k : Nat} (h : HasClock G k) : k≤cap G := by
  obtain ⟨s,odd,budget,sep⟩ := h
  have witness := PairedClock.unmatched_ternary_power s 1 k odd (by simpa using sep)
  simp only [pow_one] at witness
  exact witness.trans (Nat.mul_le_mul (by omega) budget)

private theorem carry_bound {P L : Nat} (h : HasCarry P L) : L≤cap (2*P+3) :=
  (Nat.le_add_right _ 2).trans (clock_bound (carry_to_clock h))

/-- The actual maximum of ordinary unmatched clocks. -/
noncomputable def clockMax (G : Nat) : Nat := by
  classical exact Nat.findGreatest (HasClock G) (cap G)

/-- The actual maximum static carry length, with the customary value
zero when no calendars exist in the grade range. -/
noncomputable def carryMax (P : Nat) : Nat := by
  classical exact Nat.findGreatest (HasCarry P) (cap (2*P+3))

private theorem clock_max_spec (G : Nat) : HasClock G (clockMax G) := by
  classical
  have zero : HasClock G 0 := by
    refine ⟨1,by decide,by simp [PairedClock.grade],?_⟩
    intro i h
    obtain rfl : i=0 := by omega
    decide
  exact Nat.findGreatest_spec (Nat.zero_le _) zero

private theorem carry_max_spec {P : Nat} (hp : 1≤P) : HasCarry P (carryMax P) := by
  classical
  exact Nat.findGreatest_spec (carry_bound (small_carry hp)) (small_carry hp)

/-- Both finite-maximum inequalities with their original constants. -/
theorem maximum_sandwich (G P : Nat) (hp : 1≤P) :
    carryMax P+2≤clockMax (2*P+3) ∧ clockMax G≤carryMax (16*(G+1)) := by
  classical
  have c := carry_to_clock (carry_max_spec hp)
  obtain ⟨L,le,hL⟩ := clock_to_carry (clock_max_spec G)
  exact ⟨Nat.le_findGreatest (clock_bound c) c,le.trans (Nat.le_findGreatest (carry_bound hL) hL)⟩

/-- A positive integer normalization of the familiar G log(2+G) rate. -/
def logBudget (G : Nat) : Nat := (G+1)*((G+2).log2+1)

private theorem logBudget_rescale (m n : Nat) (bound : m≤16*(n+1)) :
    logBudget m≤102*logBudget n := by
  have up : m+2<2^((n+2).log2+1+5) := by
    have h := Nat.lt_log2_self (n := n+2)
    rw [pow_add]
    norm_num
    omega
  have hlog : (m+2).log2<(n+2).log2+1+5 := (Nat.log2_lt (by omega)).2 up
  have factor := Nat.mul_le_mul (show m+1≤17*(n+1) by omega)
    (show (m+2).log2+1≤6*((n+2).log2+1) by omega)
  calc logBudget m ≤ (17*(n+1))*(6*((n+2).log2+1)) := factor
       _ = _ := by unfold logBudget; ring

/-- The global G log G clock law is exactly the static p log p statement
over the full ordered pair of words, with p the actual common grade. -/
theorem logarithmic_clock_iff_ordered_carry :
    (∃ C : Nat, ∀ G, clockMax G≤C*logBudget G) ↔
    (∃ D : Nat, ∀ u v : List Bool, u.length=v.length → 1≤ones u → ones u=ones v →
      numerator u+3^ones u=numerator v+2^u.length → u.length≤D*logBudget (ones u)) := by
  classical
  constructor
  · rintro ⟨C,hC⟩
    refine ⟨C*102,?_⟩
    intro u v len pos grade eq
    have h : HasCarry (ones u) u.length := ⟨u,v,rfl,len.symm,pos,grade,le_rfl,eq⟩
    have clk := carry_to_clock h
    calc u.length ≤ u.length+2 := by omega
         _ ≤ clockMax (2*ones u+3) := Nat.le_findGreatest (clock_bound clk) clk
         _ ≤ C*logBudget (2*ones u+3) := hC _
         _ ≤ C*(102*logBudget (ones u)) := Nat.mul_le_mul_left _ (logBudget_rescale _ _ (by omega))
         _ = _ := by ring
  · rintro ⟨D,hD⟩
    refine ⟨D*102,?_⟩
    intro G
    obtain ⟨L,lower,u,v,ul,vl,lo,grades,bound,eq⟩ := clock_to_carry (clock_max_spec G)
    rw [←ul] at eq
    calc clockMax G ≤ L := lower
         _ = u.length := ul.symm
         _ ≤ D*logBudget (ones u) := hD u v (ul.trans vl.symm) lo grades eq
         _ ≤ D*(102*logBudget G) := Nat.mul_le_mul_left _ (logBudget_rescale _ _ bound)
         _ = _ := by ring

#print axioms carry_to_clock
#print axioms clock_to_carry
#print axioms maximum_sandwich
#print axioms logarithmic_clock_iff_ordered_carry
end Collatz.ClockCarryEquivalence
