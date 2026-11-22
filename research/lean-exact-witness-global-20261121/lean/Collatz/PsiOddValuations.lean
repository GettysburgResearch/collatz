/-
Every odd initial even valuation closes its whole psi query under the
original complete-source Interval induction hypothesis. The target changes
by an actual unequal-clock merger, while the entire source word is retained.
-/
import Collatz.LowGapGlobal

open CollatzReverseBasin CollatzClosure CollatzWitness CollatzGapMultiset
open CollatzBoundedGapCofinal CollatzUnboundedGapReset

set_option autoImplicit false
set_option maxHeartbeats 2000000

namespace CollatzPsiOddValuations

private theorem three_pow_phase (e : Nat) :
    3^e%4=if e%2=0 then 1 else 3 := by
  induction e with
  | zero => rfl
  | succ e ih =>
    rw [Nat.pow_succ,Nat.mul_mod,ih]
    by_cases even : e%2=0
    · have odd : (e+1)%2≠0 := by omega
      simp [even,odd]
    · have odd : (e+1)%2=0 := by omega
      simp [even,odd]

/-- The two even endpoints have exactly the same second ordinary image. -/
theorem two_step_diamond (a : Nat) (phase : a%4=2) :
    orbit a 2=orbit (3*a+2) 2 := by
  have ae : a%2=0 := by omega
  have ao : (a/2)%2≠0 := by omega
  have be : (3*a+2)%2=0 := by omega
  have bbe : ((3*a+2)/2)%2=0 := by omega
  simp only [orbit,shortcut,ae,ao,be,bbe,ite_true,ite_false]
  omega

/-- All odd initial valuations have the same successful half-target phase.
The clocks grow with e; neither source nor target is cut off. -/
theorem odd_valuation_target_merge (e q : Nat) (odd : e%2=1) (phase : q%4=1) :
    orbit (2^(e+1)*q-1) (e+3)=orbit (2^e*q-1) (e+2) := by
  have positive : 0<q := by omega
  have powerPositive : 0<3^e*q := Nat.mul_pos (Nat.pow_pos (by decide)) positive
  have ternaryPhase : (3^e*q)%4=3 := by
    rw [Nat.mul_mod,three_pow_phase]
    simp [odd,phase]
  let a := 3^e*q-1
  have aPhase : a%4=2 := by dsimp [a]; omega
  have endpoint : 3^(e+1)*q-1=3*a+2 := by
    have power : 3^(e+1)*q=3*(3^e*q) := by rw [Nat.pow_succ]; grind
    dsimp [a]
    omega
  calc
    orbit (2^(e+1)*q-1) (e+3)
        = orbit (orbit (2^(e+1)*q-1) (e+1)) 2 := by
            rw [←orbit_add]
    _ = orbit (3^(e+1)*q-1) 2 := by rw [odd_run (e+1) q positive]
    _ = orbit (3*a+2) 2 := by rw [endpoint]
    _ = orbit a 2 := (two_step_diamond a aPhase).symm
    _ = orbit (orbit (2^e*q-1) e) 2 := by rw [odd_run e q positive]
    _ = orbit (2^e*q-1) (e+2) := (orbit_add _ e 2).symm

/-- The smaller target is exactly the psi target of the halved source. -/
theorem odd_valuation_target_equivalence (e q : Nat)
    (odd : e%2=1) (phase : q%4=1) :
    Basin (2^(e+1)*q-1) ↔ Basin (2^e*q-1) := by
  have merge := odd_valuation_target_merge e q odd phase
  calc
    Basin (2^(e+1)*q-1) ↔ Basin (orbit (2^(e+1)*q-1) (e+3)) :=
      (orbit_basin _ _).symm
    _ ↔ Basin (orbit (2^e*q-1) (e+2)) := by rw [merge]
    _ ↔ Basin (2^e*q-1) := orbit_basin _ _

private theorem first_gap_one (q a : Nat) (tail : List Nat)
    (cert : Certificate q (a::tail)) (phase : q%4=3) : a=1 := by
  obtain ⟨positive,u,step,_⟩ := (certificate_cons_iff q a tail).mp cert
  by_cases other : a=1
  · exact other
  have high : 2≤a := by omega
  have exponent : a=(a-2)+2 := by omega
  have factor : 2^a=4*2^(a-2) := by
    calc
      2^a=2^((a-2)+2) := congrArg (fun b : Nat => 2^b) exponent
      _=4*2^(a-2) := by rw [Nat.pow_add]; omega
  have multiple : 3*q+1=4*(2^(a-2)*u) := by
    rw [factor] at step
    simpa [Nat.mul_assoc] using step
  omega

/-- Entire psi-query closure for every odd initial even exponent. The phase
q=1 mod4 halves the source and keeps its complete gap word unchanged. The
other phase has first gap one and uses the existing expanding-source rule. -/
theorem psi_odd_valuation_rule (source e : Nat) (gaps : List Nat)
    (cert : PoweredCertificate source e gaps) (oddExponent : e%2=1)
    (ih : CollatzGapComparison.Hyp Interval (grades e gaps)) : Basin (2*source-1) := by
  obtain ⟨q,sourceEq,qcert⟩ := cert
  have qo : q%2=1 := witness_odd (certificate_witness qcert)
  have qp : 0<q := by omega
  have sourcePositive : 0<source := by
    rw [sourceEq]
    exact Nat.mul_pos (Nat.pow_pos (by decide)) qp
  by_cases phase : q%4=1
  · let f := e-1
    have exponent : e=f+1 := by dsimp [f]; omega
    have sourceShape : source=2*(2^f*q) := by
      rw [sourceEq,exponent,Nat.pow_succ]
      grind
    have drop : Less (grades f gaps) (grades e gaps) := by
      rw [exponent]
      exact grades_even_decrease f gaps
    have child : Basin (source-1) :=
      ih (2^f*q) (source-1) f gaps ⟨by omega,by omega⟩ ⟨q,rfl,qcert⟩ drop
    have targetShape : 2*source-1=2^(e+1)*q-1 := by
      rw [sourceEq,Nat.pow_succ]
      grind
    rw [targetShape]
    apply (odd_valuation_target_equivalence e q oddExponent phase).mpr
    simpa [sourceEq] using child
  · have phase' : q%4=3 := by omega
    cases gaps with
    | nil =>
      have one : q=1 := by simpa [Certificate,correction,total] using qcert.2
      omega
    | cons a tail =>
      have first := first_gap_one q a tail qcert phase'
      subst a
      exact CollatzLowIntervalRefinement.first_gap_one_rule source (2*source-1) e tail
        ⟨by omega,by omega⟩ ⟨q,sourceEq,qcert⟩ ih

/-- The formerly remaining length-three valuation is a direct special case. -/
theorem psi_valuation_three_rule (source : Nat) (gaps : List Nat)
    (cert : PoweredCertificate source 3 gaps)
    (ih : CollatzGapComparison.Hyp Interval (grades 3 gaps)) : Basin (2*source-1) :=
  psi_odd_valuation_rule source 3 gaps cert (by decide) ih

end CollatzPsiOddValuations
