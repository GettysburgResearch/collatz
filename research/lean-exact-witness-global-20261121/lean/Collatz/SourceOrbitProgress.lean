/-
Actual source growth at an arbitrary ordinary clock consumes the supplied
complete certificate in its original grade.  The child certificate is obtained
only by iterating ordinary_step; no new witness for an inferred target is used.
-/
import Collatz.BoundedGapCofinal
import Collatz.NegativeShadow

open CollatzReverseBasin CollatzClosure CollatzWitness CollatzGapMultiset
open CollatzBoundedGapCofinal CollatzUnboundedGapReset

set_option autoImplicit false
set_option maxHeartbeats 2000000

namespace CollatzSourceOrbitProgress

theorem cycle_stays_small (n k : Nat) (small : n=1 ∨ n=2) :
    orbit n k=1 ∨ orbit n k=2 := by
  induction k generalizing n with
  | zero => exact small
  | succ k ih =>
    rw [orbit]
    apply ih
    rcases small with one | two
    · subst n
      exact Or.inr (by decide)
    · subst n
      exact Or.inl (by decide)

/-- Every supplied ordinary prefix with endpoint outside the terminal cycle
has a complete endpoint certificate obtained by successive literal source
steps. A positive clock strictly lowers the original complete-source grade. -/
theorem advance_certificate (source clock e : Nat) (gaps : List Nat)
    (cert : PoweredCertificate source e gaps) (outside : 2<orbit source clock) :
    ∃ f tail, PoweredCertificate (orbit source clock) f tail ∧
      (clock=0 ∨ Less (grades f tail) (grades e gaps)) := by
  induction clock generalizing source e gaps with
  | zero => exact ⟨e,gaps,cert,Or.inl rfl⟩
  | succ clock ih =>
    have nonterminal : source≠1 := by
      intro one
      have small := cycle_stays_small source (clock+1) (Or.inl one)
      omega
    obtain ⟨f,tail,child,drop⟩ := ordinary_step cert nonterminal
    by_cases zero : clock=0
    · subst clock
      exact ⟨f,tail,by simpa [orbit] using child,Or.inr drop⟩
    obtain ⟨g,rest,endpoint,decrease⟩ := ih (shortcut source) f tail child
      (by simpa [orbit] using outside)
    refine ⟨g,rest,by simpa [orbit] using endpoint,Or.inr ?_⟩
    rcases decrease with absent | decrease
    · exact False.elim (zero absent)
    · exact less_trans decrease drop

/-- Growth of the odd core at any positive actual clock captures the whole
original interval. Every source step consumes the GIVEN complete certificate;
the initial even grade is then reattached unchanged to both sides. -/
theorem odd_growth_interval_rule (source target e q clock : Nat) (gaps : List Nat)
    (parent : source=2^e*q) (cert : Certificate q gaps)
    (clockPositive : 0<clock) (endpointOdd : orbit q clock%2=1)
    (growth : q<orbit q clock) (active : Interval source target)
    (ih : CollatzGapComparison.Hyp Interval (grades e gaps)) : Basin target := by
  have odd := witness_odd (certificate_witness cert)
  have outside : 2<orbit q clock := by omega
  obtain ⟨f,tail,endpoint,drop⟩ := advance_certificate q clock 0 gaps
    (show PoweredCertificate q 0 gaps from ⟨q,by simp,cert⟩) outside
  have strict : Less (grades f tail) (grades 0 gaps) := by
    rcases drop with zero | strict
    · omega
    · exact strict
  obtain ⟨w,value,wcert⟩ := endpoint
  cases f with
  | zero =>
    have same : orbit q clock=w := by simpa using value
    have endpointCert : Certificate (orbit q clock) tail := by simpa [←same] using wcert
    have bare : Less (tail.map (2*·)) (gaps.map (2*·)) := by
      simpa [grades] using strict
    have lifted := (less_append_left_iff (if e=0 then [] else [2*e+1])
      (tail.map (2*·)) (gaps.map (2*·))).mpr bare
    have ranked : Less (grades e tail) (grades e gaps) := by
      simpa [grades] using lifted
    have height : source<2^e*orbit q clock := by
      rw [parent]
      exact Nat.mul_lt_mul_of_pos_left growth (Nat.pow_pos (by decide))
    exact ih (2^e*orbit q clock) target e tail
      ⟨active.1,by have upper := active.2; omega⟩
      ⟨orbit q clock,rfl,endpointCert⟩ ranked
  | succ f =>
    have even : orbit q clock=2*(2^f*w) := by
      rw [value,Nat.pow_succ]
      ac_rfl
    omega

/-- Every sufficiently separated negative low block gives a successful
strict-grade rule for the WHOLE original interval. The negative shadow
selector is unconditional; the only recursive premise is the original
complete-source interval induction hypothesis. -/
theorem negative_block_interval_rule (source target e q u D m : Nat)
    (gaps : List Nat) (parent : source=2^e*q) (cert : Certificate q gaps)
    (mPositive : 0<m) (mOdd : m%2=1) (sourceBlock : q+m=2^D*u)
    (separation : 6*m≤D) (active : Interval source target)
    (ih : CollatzGapComparison.Hyp Interval (grades e gaps)) : Basin target := by
  have odd := witness_odd (certificate_witness cert)
  obtain ⟨_,word,endpoint,_,_,_,clockPositive,_,_,_,growth,endpointOdd,path⟩ :=
    CollatzNegativeShadow.physical_negative_return q u D m (by omega)
      mPositive mOdd sourceBlock separation
  apply odd_growth_interval_rule source target e q (total word) gaps parent cert
    clockPositive
  · simpa [path] using endpointOdd
  · simpa [path] using growth
  · exact active
  · exact ih

end CollatzSourceOrbitProgress
