import Collatz.BoundedGapCofinal

set_option autoImplicit false
set_option maxHeartbeats 3000000

namespace CollatzSourceRecords

open CollatzReverseBasin CollatzClosure CollatzWitness
open CollatzGapMultiset CollatzBoundedGapCofinal

/-- A complete source at this grade dominates every strictly lower grade
and is largest in its own multiset class. The strict clause excludes a
different lower-grade certificate for the same numerical source. -/
structure Record (source e : Nat) (word : List Nat) : Prop where
  certificate : PoweredCertificate source e word
  lower : ∀ child f tail, PoweredCertificate child f tail →
    Less (grades f tail) (grades e word) → child<source
  same : ∀ child f tail, PoweredCertificate child f tail →
    (grades f tail).Perm (grades e word) → child≤source

private theorem grades_sum_bound (e : Nat) (word : List Nat) :
    e+total word≤(grades e word).sum := by
  have mapped : (word.map (2*·)).sum=2*total word := by
    induction word with
    | nil => rfl
    | cons a word ih => simp only [List.map_cons,List.sum_cons,total,ih]; omega
  by_cases zero : e=0
  · simp only [grades,zero,ite_true,List.nil_append,mapped]
    omega
  · simp only [grades,zero,ite_false,List.sum_append,List.sum_cons,List.sum_nil,mapped]
    omega

private theorem powered_source_ceiling {source e : Nat} {word : List Nat}
    (cert : PoweredCertificate source e word) : source≤2^(grades e word).sum := by
  obtain ⟨q,rfl,positive,identity⟩ := cert
  have qle := Nat.le_mul_of_pos_left q (Nat.pow_pos (by decide : 0<3) : 0<3^word.length)
  have qbound : q≤2^total word := by omega
  have first := Nat.mul_le_mul_left (2^e) qbound
  have second := Nat.pow_le_pow_right (by decide : 0<(2:Nat)) (grades_sum_bound e word)
  exact Nat.le_trans (by simpa only [←Nat.pow_add] using first) second

private theorem perm_sum {left right : List Nat} (same : left.Perm right) :
    left.sum=right.sum := by
  induction same with
  | nil => rfl
  | cons _ _ ih => simp only [List.sum_cons,ih]
  | swap a b rest => simp only [List.sum_cons]; omega
  | trans _ _ ih₁ ih₂ => exact ih₁.trans ih₂

private def AtGrade (source : Nat) (G : List Nat) : Prop :=
  ∃ e word, PoweredCertificate source e word ∧ (grades e word).Perm G

private theorem at_grade_ceiling {source : Nat} {G : List Nat}
    (cert : AtGrade source G) : source≤2^G.sum := by
  obtain ⟨e,word,cert,same⟩ := cert
  have bound := powered_source_ceiling cert
  rw [perm_sum same] at bound
  exact bound

private theorem bounded_maximum (B : Nat) (P : Nat → Prop) :
    (∃ n, P n) → (∀ n, P n → n≤B) → ∃ m, P m ∧ ∀ n, P n → n≤m := by
  classical
  induction B with
  | zero =>
    intro nonempty bound
    obtain ⟨n,hn⟩ := nonempty
    have zero := bound n hn
    refine ⟨n,hn,?_⟩
    intro k hk
    have := bound k hk
    omega
  | succ B ih =>
    intro nonempty bound
    by_cases top : P (B+1)
    · exact ⟨B+1,top,bound⟩
    · apply ih nonempty
      intro n hn
      have upper := bound n hn
      by_cases eq : n=B+1
      · subst n
        exact False.elim (top hn)
      · omega

private theorem minimal_grade (P : List Nat → Prop) (nonempty : ∃ G, P G) :
    ∃ G, P G ∧ ∀ H, Less H G → ¬P H := by
  classical
  have descend : ∀ G, P G → ∃ H, P H ∧ ∀ K, Less K H → ¬P K := by
    intro G
    induction G using less_wellFounded.induction with
    | h G ih =>
      intro existsHere
      by_cases lower : ∃ H, Less H G ∧ P H
      · obtain ⟨H,drop,existsLower⟩ := lower
        exact ih H drop existsLower
      · exact ⟨G,existsHere,by
          intro H drop existsLower
          exact lower ⟨H,drop,existsLower⟩⟩
  obtain ⟨G,hG⟩ := nonempty
  exact descend G hG

private theorem powers_cofinal (N : Nat) : N<2^N := by
  induction N with
  | zero => decide
  | succ N ih => rw [Nat.pow_succ]; omega

/-- There are arbitrarily large complete grade-record sources. This uses
minimality in the well-founded grade relation, not a claim that the list
representation is linearly ordered. The maximum is only within one fixed
multiset class and is bounded by its explicit source ceiling. -/
theorem cofinal_records (N : Nat) : ∃ source e word, N<source ∧ Record source e word := by
  classical
  let P := fun G : List Nat => ∃ source, N<source ∧ AtGrade source G
  have one : Certificate 1 [] := by simp [Certificate,PositiveGaps,correction,total]
  have initial : P (grades N []) := by
    refine ⟨2^N,powers_cofinal N,N,[],?_,List.Perm.refl _⟩
    exact ⟨1,by simp,one⟩
  obtain ⟨G,hG,minimal⟩ := minimal_grade P ⟨grades N [],initial⟩
  obtain ⟨first,large,firstCert⟩ := hG
  obtain ⟨source,cert,maximal⟩ := bounded_maximum (2^G.sum) (fun s => AtGrade s G)
    ⟨first,firstCert⟩ (fun _ c => at_grade_ceiling c)
  have sourceLarge : N<source := Nat.lt_of_lt_of_le large (maximal first firstCert)
  obtain ⟨e,word,certificate,same⟩ := cert
  refine ⟨source,e,word,sourceLarge,certificate,?_,?_⟩
  · intro child f tail childCert drop
    have dropG : Less (grades f tail) G :=
      (less_perm (List.Perm.refl _) same).mp drop
    have notLarge : ¬N<child := by
      intro big
      exact minimal (grades f tail) dropG
        ⟨child,big,f,tail,childCert,List.Perm.refl _⟩
    omega
  · intro child f tail childCert perm
    exact maximal child ⟨f,tail,childCert,perm.trans same⟩

private theorem record_even {source e : Nat} {word : List Nat}
    (record : Record source e word) (large : 1<source) : source%2=0 := by
  by_cases even : source%2=0
  · exact even
  · obtain ⟨f,tail,cert,drop⟩ := ordinary_step record.certificate (by omega)
    have bound := record.lower _ f tail cert drop
    unfold shortcut at bound
    split at bound <;> omega

/-- The cofinal records really lie in the original low domain. The old
high-gap/cofinal replacement rules exclude every initial run >=4 and every
odd gap >=5, independently of any target-convergence premise. -/
theorem record_low_domain {source e : Nat} {word : List Nat}
    (record : Record source e word) (large : 1<source) :
    1≤e ∧ e≤3 ∧ (∀ a∈word, a≤4) ∧ source%2=0 := by
  have even := record_even record large
  have positiveE : 1≤e := by
    by_cases zero : e=0
    · obtain ⟨q,value,cert⟩ := record.certificate
      have odd := witness_odd (certificate_witness cert)
      simp only [zero,Nat.pow_zero,Nat.one_mul] at value
      omega
    · omega
  have lowE : e≤3 := by
    by_cases high : 4≤e
    · obtain ⟨p,new,greater,cert,drop⟩ :=
        large_even_replacement source e source word record.certificate high
      have bound := record.lower p 0 new ⟨p,by simp,cert⟩ drop
      omega
    · omega
  refine ⟨positiveE,lowE,?_,even⟩
  intro a member
  by_cases low : a≤4
  · exact low
  · obtain ⟨front,tail,wordEq⟩ := List.mem_iff_append.mp member
    obtain ⟨q,_,cert⟩ := record.certificate
    rw [wordEq] at cert
    obtain ⟨p,new,greater,child,_,drop⟩ :=
      high_gap_replacement q a source front tail cert (by omega)
    have remove : Less (grades 0 word) (grades e word) := by
      simpa using even_to_odd_replacement e [] word positiveE (by simp)
    have smaller : Less (grades 0 (new++tail)) (grades e word) := by
      apply less_trans _ remove
      simpa only [wordEq] using drop
    have bound := record.lower p 0 (new++tail) ⟨p,by simp,child⟩ smaller
    omega

/-- The only two unchanged-target source moves in the existing order:
strict grade decrease, or a larger complete source at the same grade.
Replacing the source by itself at the same grade is deliberately absent:
it decreases neither the source defect nor the target. -/
def SourceOnlyStep (source : Nat) (old : List Nat) : Prop :=
  ∃ child f tail, PoweredCertificate child f tail ∧ Interval child (2*source-1) ∧
    (Less (grades f tail) old ∨ ((grades f tail).Perm old ∧ source<child))

/-- Every record source S>2 obstructs EVERY unchanged-target source
handoff for its psi target 2S-1, not merely a prescribed prefix language.
The borderline child S-1 is excluded by its actual odd step: that step
has still lower grade and value greater than S. -/
theorem record_no_source_only_psi {source e : Nat} {word : List Nat}
    (record : Record source e word) (large : 2<source) :
    ¬SourceOnlyStep source (grades e word) := by
  intro move
  obtain ⟨child,f,tail,cert,active,step⟩ := move
  rcases step with drop | ⟨same,grows⟩
  · have bound := record.lower child f tail cert drop
    have edge : child+1=source := by obtain ⟨_,cap⟩ := active; omega
    have even := record_even record (by omega)
    have odd : child%2=1 := by omega
    obtain ⟨f',tail',cert',drop'⟩ := ordinary_step cert (by omega)
    have bound' := record.lower (shortcut child) f' tail' cert' (less_trans drop' drop)
    unfold shortcut at bound'
    split at bound' <;> omega
  · have bound := record.same child f tail cert same
    omega

/-- The obstruction is cofinal inside the actual remaining low alphabet
and low initial-even-run domain. It asserts no positive or negative result
about the target's convergence: a valid proof must change that target or
use another independently justified action. -/
theorem cofinal_source_only_obstruction (N : Nat) :
    ∃ source e word, N<source ∧ 2<source ∧ Record source e word ∧
      1≤e ∧ e≤3 ∧ (∀ a∈word, a≤4) ∧
      (2*source-1)%2=1 ∧ source+1<2*source-1 ∧
      Interval source (2*source-1) ∧ ¬SourceOnlyStep source (grades e word) := by
  obtain ⟨source,e,word,big,record⟩ := cofinal_records (N+2)
  obtain ⟨positiveE,lowE,lowWord,even⟩ := record_low_domain record (by omega)
  exact ⟨source,e,word,by omega,by omega,record,positiveE,lowE,lowWord,
    by omega,by omega,⟨by omega,by omega⟩,record_no_source_only_psi record (by omega)⟩

end CollatzSourceRecords
