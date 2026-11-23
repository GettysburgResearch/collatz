/-
Uniform denominator clearing for every reverse power of three.

The construction uses integer numerator identities only. Actual ordinary
legality is obtained from the existing positive-gap Prefix theorem. The
resulting additive comparisons remain explicit obligations; their universal
convergence is not assumed.
-/
import Collatz.GapComparison

open CollatzReverseBasin CollatzClosure CollatzWitness CollatzGapMultiset
open CollatzHighGapPump

set_option autoImplicit false
set_option maxHeartbeats 4000000

namespace CollatzMergerDenominatorClear

private theorem even_factor (N : Nat) (positive : 0 < N) (even : N % 2 = 0) :
    ∃ a p, 0 < a ∧ p % 2 = 1 ∧ N = 2^a*p := by
  obtain ⟨a,identity⟩ := CollatzDirected.oddCore_factor N positive
  have odd := (CollatzDirected.oddCore_spec N positive).2.1
  have apos : 0 < a := by
    by_cases zero : a = 0
    · simp only [zero,Nat.pow_zero,Nat.one_mul] at identity
      omega
    · omega
  exact ⟨a,CollatzDirected.oddCore N,apos,odd,identity⟩

/-- Clear every remaining ternary denominator of a positive odd numerator.
The invariant p + C(word) = 2^total(word)*z records the exact rational
trajectory while all objects in the proof remain natural integers. -/
theorem positive_numerator_clear (j p : Nat) (odd : p % 2 = 1) :
    ∃ word z, PositiveGaps word ∧ word.length = j ∧ 0 < z ∧
      p + correction word = 2^total word*z := by
  induction j generalizing p with
  | zero =>
    refine ⟨[],p,?_,rfl,by omega,?_⟩
    · simp [PositiveGaps]
    · simp [correction,total]
  | succ j ih =>
    have powodd : 3^j % 2 = 1 := by simp [Nat.pow_mod]
    have ppos : 0 < p := by omega
    have positive : 0 < p+3^j := Nat.lt_of_lt_of_le ppos (Nat.le_add_right p (3^j))
    have even : (p+3^j) % 2 = 0 := by rw [Nat.add_mod,odd,powodd]
    obtain ⟨a,q,apos,qodd,step⟩ := even_factor (p+3^j) positive even
    obtain ⟨word,z,legal,len,zpos,identity⟩ := ih q qodd
    refine ⟨a::word,z,?_,by simp [len],zpos,?_⟩
    · intro b hb
      rcases List.mem_cons.mp hb with eq | mem
      · omega
      · exact legal b mem
    · simp only [correction,total,len,Nat.pow_add]
      calc
        p + (3^j + 2^a*correction word) =
            2^a*(q+correction word) := by grind
        _ = 2^a*(2^total word*z) := by rw [identity]
        _ = _ := by grind

/-- For EVERY positive k there is a finite legal gap template clearing
-1/3^k to a nonnegative integer. The k=1 endpoint is exactly zero.
No convergence claim about the terminal integer is needed. -/
theorem denominator_clear (k : Nat) (positive : 0 < k) :
    ∃ word z, PositiveGaps word ∧ word.length = k ∧
      correction word = 1 + 2^total word*z := by
  obtain ⟨j,rfl⟩ := Nat.exists_eq_succ_of_ne_zero (by omega : k ≠ 0)
  cases j with
  | zero => exact ⟨[1],0,by simp [PositiveGaps],rfl,by decide⟩
  | succ j =>
    have powodd : 3^(j+1) % 2 = 1 := by simp [Nat.pow_mod]
    have lower : 3 ≤ 3^(j+1) := by
      have h := Nat.pow_le_pow_right (by decide : 0<3) (by omega : 1≤j+1)
      exact h
    have positive : 0 < 3^(j+1)-1 := by omega
    have even : (3^(j+1)-1) % 2 = 0 := by omega
    obtain ⟨a,p,apos,podd,step⟩ := even_factor (3^(j+1)-1) positive even
    obtain ⟨word,z,legal,len,_,identity⟩ := positive_numerator_clear (j+1) p podd
    refine ⟨a::word,z,?_,by simp [len],?_⟩
    · intro b hb
      rcases List.mem_cons.mp hb with eq | mem
      · omega
      · exact legal b mem
    · have step' : 3^(j+1) = 1+2^a*p := by omega
      simp only [correction,total,len]
      rw [Nat.pow_add 2 a (total word)]
      rw [step']
      calc
        1+2^a*p+2^a*correction word = 1+2^a*(p+correction word) := by grind
        _ = 1+2^a*(2^total word*z) := by rw [identity]
        _ = _ := by grind

private theorem even_factor_bounded (K N : Nat) (positive : 0 < N)
    (even : N % 2 = 0) (bound : N ≤ 2*3^K) :
    ∃ a p, 0 < a ∧ a ≤ 2*K+1 ∧ p % 2 = 1 ∧ p ≤ 3^K ∧
      N = 2^a*p := by
  obtain ⟨a,p,apos,podd,identity⟩ := even_factor N positive even
  have ppos : 1 ≤ p := by omega
  have lower : 2 ≤ 2^a := Nat.pow_le_pow_right (by decide : 0<2) apos
  have pbound : p ≤ 3^K := by
    have hp := Nat.mul_le_mul_right p lower
    omega
  have apow : 2^a ≤ N := by
    have hp := Nat.mul_le_mul_left (2^a) ppos
    simpa [identity] using hp
  have power3 : 3^K ≤ 4^K := Nat.pow_le_pow_left (by decide) K
  have power2 : 2^(2*K+1)=2*4^K := by
    rw [Nat.pow_add,Nat.pow_mul]
    grind
  have abound : a ≤ 2*K+1 := by
    apply (Nat.pow_le_pow_iff_right (by decide : 1<2)).mp
    rw [power2]
    omega
  exact ⟨a,p,apos,abound,podd,pbound,identity⟩

/-- A uniform numerator invariant bounds each gap and the whole clearing
clock. This is a proved all-index bound, not an empirical stopping estimate. -/
theorem positive_numerator_clear_bounded (K j p : Nat)
    (remaining : j ≤ K) (odd : p % 2 = 1) (bounded : p ≤ 3^K) :
    ∃ word z, PositiveGaps word ∧ word.length = j ∧
      (∀ a ∈ word, a ≤ 2*K+1) ∧ total word ≤ j*(2*K+1) ∧
      0 < z ∧ p+correction word=2^total word*z := by
  induction j generalizing p with
  | zero =>
    refine ⟨[],p,by simp [PositiveGaps],rfl,by simp,by simp [total],by omega,?_⟩
    simp [correction,total]
  | succ j ih =>
    have ppos : 0 < p := by omega
    have positive : 0 < p+3^j := Nat.lt_of_lt_of_le ppos (Nat.le_add_right p (3^j))
    have powodd : 3^j % 2 = 1 := by simp [Nat.pow_mod]
    have even : (p+3^j) % 2 = 0 := by rw [Nat.add_mod,odd,powodd]
    have powle : 3^j ≤ 3^K := Nat.pow_le_pow_right (by decide) (by omega)
    have upper : p+3^j ≤ 2*3^K := by omega
    obtain ⟨a,q,apos,amax,qodd,qmax,step⟩ := even_factor_bounded K (p+3^j) positive even upper
    obtain ⟨word,z,legal,len,gapmax,clockmax,zpos,identity⟩ := ih q (by omega) qodd qmax
    refine ⟨a::word,z,?_,by simp [len],?_,?_,zpos,?_⟩
    · intro b hb
      rcases List.mem_cons.mp hb with eq | mem
      · omega
      · exact legal b mem
    · intro b hb
      rcases List.mem_cons.mp hb with eq | mem
      · omega
      · exact gapmax b mem
    · change a+total word ≤ (j+1)*(2*K+1)
      calc
        a+total word ≤ (2*K+1)+j*(2*K+1) := Nat.add_le_add amax clockmax
        _ = _ := by grind
    · simp only [correction,total,len,Nat.pow_add]
      calc
        p+(3^j+2^a*correction word)=2^a*(q+correction word) := by grind
        _ = 2^a*(2^total word*z) := by rw [identity]
        _ = _ := by grind

/-- Every denominator-clearing template can be constructed within a
quadratic clock budget, with each gap at most 2k-1. -/
theorem denominator_clear_bounded (k : Nat) (positive : 0 < k) :
    ∃ word z, PositiveGaps word ∧ word.length=k ∧
      (∀ a ∈ word, a ≤ 2*k-1) ∧ total word ≤ k*(2*k-1) ∧
      correction word=1+2^total word*z := by
  obtain ⟨K,rfl⟩ := Nat.exists_eq_succ_of_ne_zero (by omega : k ≠ 0)
  cases K with
  | zero =>
    refine ⟨[1],0,by simp [PositiveGaps],rfl,?_,by decide,by decide⟩
    intro a ha
    have eq : a=1 := by simpa using ha
    omega
  | succ K =>
    have powodd : 3^(K+1) % 2 = 1 := by simp [Nat.pow_mod]
    have lower : 3 ≤ 3^(K+1) := Nat.pow_le_pow_right (by decide : 0<3) (by omega : 1≤K+1)
    have positive : 0 < 3^(K+1)-1 := by omega
    have even : (3^(K+1)-1) % 2 = 0 := by omega
    have upper : 3^(K+1)-1 ≤ 2*3^(K+1) := by omega
    obtain ⟨a,p,apos,amax,podd,pmax,step⟩ :=
      even_factor_bounded (K+1) (3^(K+1)-1) positive even upper
    obtain ⟨word,z,legal,len,gapmax,clockmax,_,identity⟩ :=
      positive_numerator_clear_bounded (K+1) (K+1) p (by omega) podd pmax
    have grade : 2*(K+1+1)-1=2*(K+1)+1 := by omega
    refine ⟨a::word,z,?_,by simp [len],?_,?_,?_⟩
    · intro b hb
      rcases List.mem_cons.mp hb with eq | mem
      · omega
      · exact legal b mem
    · intro b hb
      rcases List.mem_cons.mp hb with eq | mem
      · omega
      · have h := gapmax b mem
        omega
    · rw [grade]
      change a+total word ≤ (K+1+1)*(2*(K+1)+1)
      calc
        a+total word ≤ (2*(K+1)+1)+(K+1)*(2*(K+1)+1) :=
          Nat.add_le_add amax clockmax
        _ = _ := by grind
    · have step' : 3^(K+1)=1+2^a*p := by omega
      simp only [correction,total,len]
      rw [Nat.pow_add 2 a (total word),step']
      calc
        1+2^a*p+2^a*correction word=1+2^a*(p+correction word) := by grind
        _ = 1+2^a*(2^total word*z) := by rw [identity]
        _ = _ := by grind

theorem positive_total (word : List Nat) (legal : PositiveGaps word)
    (nonempty : word ≠ []) : 0 < total word := by
  cases word with
  | nil => exact False.elim (nonempty rfl)
  | cons a tail =>
    have h := legal a (by simp)
    simp only [total]
    omega

theorem length_le_total (word : List Nat) (legal : PositiveGaps word) :
    word.length ≤ total word := by
  induction word with
  | nil => simp [total]
  | cons a tail ih =>
    have apos := legal a (by simp)
    have rest : PositiveGaps tail := fun b hb => legal b (by simp [hb])
    have lower := ih rest
    simp only [List.length_cons,total]
    omega

theorem correction_height_bound (word : List Nat) (legal : PositiveGaps word) :
    2^word.length*(correction word+2^total word) ≤
      3^word.length*2^total word := by
  induction word with
  | nil => simp [correction,total]
  | cons a tail ih =>
    have apos := legal a (by simp)
    have rest : PositiveGaps tail := fun b hb => legal b (by simp [hb])
    have h := ih rest
    have two : 2 ≤ 2^a := Nat.pow_le_pow_right (by decide : 0<2) apos
    have lower : 2^tail.length ≤ 2^total tail :=
      Nat.pow_le_pow_right (by decide) (length_le_total tail rest)
    have small := Nat.mul_le_mul two lower
    have error := Nat.mul_le_mul_left (3^tail.length) small
    have main := Nat.mul_le_mul_left (2*2^a) h
    simp only [List.length_cons,correction,total,Nat.pow_succ,Nat.pow_add]
    grind

/-- The integer reached when the denominator clears is explicitly small.
This bound supplies no assumption about that integer's eventual orbit. -/
theorem clearing_endpoint_bound (word : List Nat) (z : Nat)
    (legal : PositiveGaps word) (clears : correction word=1+2^total word*z) :
    2^word.length*(z+1) < 3^word.length := by
  have bound := correction_height_bound word legal
  rw [clears] at bound
  have positive : 0<2^word.length := Nat.pow_pos (by decide)
  have strict : 2^total word*(2^word.length*(z+1)) <
      2^total word*3^word.length := by grind
  exact Nat.lt_of_mul_lt_mul_left strict

/-- The total source exponent need only fit the uniformly constructed word.
The entire certified suffix remains literally unchanged, now preceded by
the exact remaining even run. -/
theorem complete_witness_additive_rewrite
    (k n a z : Nat) (word tail : List Nat)
    (legal : PositiveGaps word) (length : word.length = k+1)
    (clears : correction word = 1+2^total word*z)
    (fits : total word ≤ a) (cert : Certificate (3^k*n) (a::tail)) :
    ∃ q, Certificate q tail ∧
      PoweredCertificate (2^(a-total word)*q) (a-total word) tail ∧
      Less (grades (a-total word) tail) (grades 0 (a::tail)) ∧
      Prefix n word (2^(a-total word)*q+z) ∧
      (Basin n ↔ Basin (2^(a-total word)*q+z)) := by
  obtain ⟨_,q,first,tailCert⟩ := (certificate_cons_iff (3^k*n) a tail).mp cert
  have nonempty : word ≠ [] := by intro empty; simp [empty] at length
  have clockpos := positive_total word legal nonempty
  have powSplit : 2^a = 2^total word*2^(a-total word) := by
    rw [←Nat.pow_add]
    congr 1
    omega
  have first' : 3^(k+1)*n+1=2^a*q := by
    rw [Nat.pow_succ]
    grind
  have path : Prefix n word (2^(a-total word)*q+z) := by
    refine ⟨legal,?_⟩
    rw [length,clears]
    rw [powSplit] at first'
    grind
  let inserted := if a-total word=0 then [] else [2*(a-total word)+1]
  have smaller : ∀ b ∈ inserted, b < 2*a := by
    intro b hb
    by_cases zero : a-total word=0
    · simp [inserted,zero] at hb
    · have val : b=2*(a-total word)+1 := by simpa [inserted,zero] using hb
      omega
  have rank := replace_one_with_tail (2*a) inserted (tail.map (2*·)) smaller
  have rank' : Less (grades (a-total word) tail) (grades 0 (a::tail)) := by
    simpa [grades,inserted] using rank
  exact ⟨q,tailCert,⟨q,rfl,tailCert⟩,rank',path,prefix_basin path⟩

/-- A clearing template exists for each reverse power; there is no finite
menu of preselected powers and no extra congruence guard. The fitting and
additive-child coverage conditions are retained exactly. -/
theorem uniform_reverse_power_template (k : Nat) :
    ∃ word z, PositiveGaps word ∧ word.length = k+1 ∧
      (∀ a ∈ word, a ≤ 2*k+1) ∧ total word ≤ (k+1)*(2*k+1) ∧
      2^(k+1)*(z+1)<3^(k+1) ∧
      correction word = 1+2^total word*z ∧
      ∀ n a tail, total word ≤ a → Certificate (3^k*n) (a::tail) →
        ∃ q, Certificate q tail ∧
          PoweredCertificate (2^(a-total word)*q) (a-total word) tail ∧
          Less (grades (a-total word) tail) (grades 0 (a::tail)) ∧
          (Basin n ↔ Basin (2^(a-total word)*q+z)) := by
  obtain ⟨word,z,legal,len,gapmax,clockmax,clear⟩ :=
    denominator_clear_bounded (k+1) (by omega)
  have bound := clearing_endpoint_bound word z legal clear
  have grade : 2*(k+1)-1=2*k+1 := by omega
  rw [grade] at gapmax clockmax
  rw [len] at bound
  refine ⟨word,z,legal,len,gapmax,clockmax,bound,clear,?_⟩
  intro n a tail fits cert
  obtain ⟨q,tailCert,child,drop,_,merge⟩ :=
    complete_witness_additive_rewrite k n a z word tail legal len clear fits cert
  exact ⟨q,tailCert,child,drop,merge⟩

theorem reverse_nine_template :
    PositiveGaps [3,2,1] ∧ ([3,2,1] : List Nat).length=3 ∧
      correction [3,2,1] = 1+2^total [3,2,1]*1 := by
  simp [PositiveGaps,correction,total]

/-- The quadratic sufficient budget is below the usual ternary-order scale.
The statement is purely numerical and does not assume a valuation theorem. -/
theorem quadratic_clock_below_order_scale (k : Nat) :
    (k+1)*(2*k+1) ≤ 2*3^k := by
  induction k with
  | zero => decide
  | succ k ih =>
    by_cases zero : k=0
    · subst k
      decide
    · have positive : 1 ≤ k := by omega
      have square : k ≤ k*k := Nat.le_mul_self k
      have left : (k+1+1)*(2*(k+1)+1)=2*(k*k)+7*k+6 := by grind
      have right : 3*((k+1)*(2*k+1))=6*(k*k)+9*k+3 := by grind
      have polynomial : (k+1+1)*(2*(k+1)+1) ≤ 3*((k+1)*(2*k+1)) := by
        rw [left,right]
        omega
      have scaled := Nat.mul_le_mul_left 3 ih
      calc
        (k+1+1)*(2*(k+1)+1) ≤ 3*((k+1)*(2*k+1)) := polynomial
        _ ≤ 3*(2*3^k) := scaled
        _ = 2*3^(k+1) := by rw [Nat.pow_succ]; grind

/-- Clearing need not land at one, even though every template is finite. -/
theorem nonunit_clearing_endpoint :
    PositiveGaps [3,1,3,1,1,1,2] ∧
      correction [3,1,3,1,1,1,2] = 1+2^12*3 := by
  simp [PositiveGaps,correction]

/-- The low prefix produced by the asymmetric psi reset has a second exact
handoff. Its five target odd steps merge at the inherited odd source plus six.
The additive child is an explicit remaining comparison, not a solved case. -/
theorem reverse_nine_low_handoff (n : Nat) (tail : List Nat)
    (cert : Certificate (9*n) ([1,1,3]++tail)) :
    ∃ q, Certificate q tail ∧
      Less (grades 0 tail) (grades 0 ([1,1,3]++tail)) ∧
      Prefix n [1,1,1,1,1] (q+6) ∧ (Basin n ↔ Basin (q+6)) := by
  obtain ⟨q,path,tailCert⟩ := CollatzLowGapLoops.split_certificate (9*n) [1,1,3] tail cert
  have source : 243*n+19=32*q := by
    have h := path.2
    simp only [List.length_cons,List.length_nil,correction,total] at h
    grind
  have targetPath : Prefix n [1,1,1,1,1] (q+6) := by
    refine ⟨by simp [PositiveGaps],?_⟩
    simp only [List.length_cons,List.length_nil,correction,total]
    grind
  have first := odd_to_odd_replacement 1 [] (1::3::tail) (by simp)
  have second := odd_to_odd_replacement 1 [] (3::tail) (by simp)
  have third := odd_to_odd_replacement 3 [] tail (by simp)
  have drop : Less (grades 0 tail) (grades 0 ([1,1,3]++tail)) := by
    simpa using less_trans third (less_trans second first)
  exact ⟨q,tailCert,drop,targetPath,prefix_basin targetPath⟩

end CollatzMergerDenominatorClear
