/-
A least bad target and a minimum supplied source grade produce one canonical
counterquery carrying BOTH the original unrestricted interval hypothesis and
the original-target source floor. No source witness is reset after selection.
-/
import Collatz.RootedSourceFloor
import Collatz.SourceOrbitProgress

open CollatzReverseBasin CollatzClosure CollatzWitness CollatzGapMultiset
open CollatzHighGapPump CollatzBoundedGapCofinal CollatzBoundedFourNormalForm
open CollatzRootedSourceFloor

set_option autoImplicit false
set_option maxHeartbeats 3000000

namespace CollatzJointMinimalCounterexample

def Prior (target : Nat) : Prop := ∀ n, 0<n → n<target → Basin n

/-- Minimum is taken among every supplied complete source certificate whose
interval captures this fixed target, without restricting the future query. -/
def SourceMinimal (target _source e : Nat) (gaps : List Nat) : Prop :=
  ∀ childSource childE childGaps,
    PoweredCertificate childSource childE childGaps → Interval childSource target →
    ¬Less (grades childE childGaps) (grades e gaps)

theorem least_bad_target (failure : ∃ n, 0<n ∧ ¬Basin n) :
    ∃ target, 0<target ∧ ¬Basin target ∧ Prior target := by
  classical
  have descend (n : Nat) : 0<n → ¬Basin n →
      ∃ target, 0<target ∧ ¬Basin target ∧ Prior target := by
    induction n using Nat.strong_induction_on with
    | h n ih =>
      intro positive bad
      by_cases lower : ∃ m, 0<m ∧ m<n ∧ ¬Basin m
      · obtain ⟨m,mp,ml,mb⟩ := lower
        exact ih m ml mp mb
      · refine ⟨n,positive,bad,?_⟩
        intro m mp ml
        apply Classical.byContradiction
        intro mb
        exact lower ⟨m,mp,ml,mb⟩
  obtain ⟨n,positive,bad⟩ := failure
  exact descend n positive bad

private def Admits (target : Nat) (word : List Nat) : Prop :=
  ∃ source e gaps, word=grades e gaps ∧
    PoweredCertificate source e gaps ∧ Interval source target

private theorem minimal_word (target : Nat) (word : List Nat) (present : Admits target word) :
    ∃ minimal, Admits target minimal ∧
      ∀ new, Less new minimal → ¬Admits target new := by
  classical
  have descend : ∀ word, Admits target word →
      ∃ minimal, Admits target minimal ∧ ∀ new, Less new minimal → ¬Admits target new := by
    intro word
    induction word using CollatzGapMultiset.induction_on with
    | step old ih =>
      intro occurs
      by_cases lower : ∃ new, Less new old ∧ Admits target new
      · obtain ⟨new,drop,member⟩ := lower
        exact ih new drop member
      · refine ⟨old,occurs,?_⟩
        intro new drop member
        exact lower ⟨new,drop,member⟩
  exact descend word present

/-- Well-founded source selection is applied once, to an actual existing
complete certificate. The result is minimal for the original grade order. -/
theorem minimum_capturing_source (target source e : Nat) (gaps : List Nat)
    (cert : PoweredCertificate source e gaps) (active : Interval source target) :
    ∃ selected selectedE selectedGaps,
      PoweredCertificate selected selectedE selectedGaps ∧ Interval selected target ∧
      SourceMinimal target selected selectedE selectedGaps := by
  obtain ⟨word,⟨selected,selectedE,selectedGaps,value,supplied,captures⟩,minimum⟩ :=
    minimal_word target (grades e gaps) ⟨source,e,gaps,rfl,cert,active⟩
  refine ⟨selected,selectedE,selectedGaps,supplied,captures,?_⟩
  intro child childE childGaps childCert childActive drop
  exact minimum (grades childE childGaps) (by simpa [value] using drop)
    ⟨child,childE,childGaps,rfl,childCert,childActive⟩

/-- The resulting hypothesis is the ORIGINAL full Hyp Interval. If a smaller
grade query had a bad target y, target minimality would give target<=y, so
its same source would also capture the original least bad target. -/
theorem original_interval_hyp (target source e : Nat) (gaps : List Nat)
    (positive : 0<target) (prior : Prior target)
    (minimum : SourceMinimal target source e gaps) :
    CollatzGapComparison.Hyp Interval (grades e gaps) := by
  classical
  intro child childTarget childE childGaps active cert drop
  apply Classical.byContradiction
  intro bad
  have least : target≤childTarget := by
    apply Classical.byContradiction
    intro smaller
    exact bad (prior childTarget active.1 (by omega))
  exact minimum child childE childGaps cert
    ⟨positive,by have upper:=active.2; omega⟩ drop

private theorem perm_sum {xs ys : List Nat} (perm : xs.Perm ys) : xs.sum=ys.sum := by
  induction perm with
  | nil => rfl
  | cons a _ ih => simp [ih]
  | swap a b tail => simp only [List.sum_cons]; omega
  | trans _ _ first second => exact first.trans second

private theorem grade_clock_bound (e : Nat) (gaps : List Nat) :
    e+total gaps≤(grades e gaps).sum := by
  have mapped : (gaps.map (2*·)).sum=2*total gaps := by
    induction gaps with
    | nil => simp [total]
    | cons a gaps ih => simp [total,ih,Nat.mul_add]
  by_cases zero : e=0
  · simp [grades,zero,mapped]
    omega
  · simp [grades,zero,mapped]
    omega

/-- At one fixed source grade, the represented source values are bounded.
This permits a maximum-source tie break without a new rank assumption. -/
theorem source_grade_bound (source e : Nat) (gaps : List Nat)
    (cert : PoweredCertificate source e gaps) : source≤2^(grades e gaps).sum := by
  obtain ⟨q,parent,qcert⟩ := cert
  have scaled : q≤3^gaps.length*q :=
    Nat.le_mul_of_pos_left q (Nat.pow_pos (by decide))
  have identity := qcert.2
  have oddBound : q≤2^total gaps := by omega
  have powerBound := Nat.mul_le_mul_left (2^e) oddBound
  have sourceBound : source≤2^(e+total gaps) := by
    simpa [parent,Nat.pow_add] using powerBound
  exact Nat.le_trans sourceBound (Nat.pow_le_pow_right (by decide : 0<2)
    (grade_clock_bound e gaps))

private theorem bounded_maximum (P : Nat → Prop) (N : Nat)
    (present : ∃ n, P n) (bounded : ∀ n, P n → n≤N) :
    ∃ largest, P largest ∧ ∀ n, P n → n≤largest := by
  classical
  have descend : ∀ N, (∃ n, P n) → (∀ n, P n → n≤N) →
      ∃ largest, P largest ∧ ∀ n, P n → n≤largest := by
    intro N
    induction N with
    | zero =>
      intro present bounded
      obtain ⟨n,hn⟩ := present
      exact ⟨n,hn,by intro m hm; have h:=bounded m hm; omega⟩
    | succ N ih =>
      intro present bounded
      by_cases top : P (N+1)
      · exact ⟨N+1,top,bounded⟩
      · apply ih present
        intro n hn
        have below := bounded n hn
        by_cases equal : n=N+1
        · exact False.elim (top (by simpa [equal] using hn))
        · omega
  exact descend N present bounded

def SourceMaximal (target source e : Nat) (gaps : List Nat) : Prop :=
  ∀ childSource childE childGaps,
    PoweredCertificate childSource childE childGaps → Interval childSource target →
    (grades childE childGaps).Perm (grades e gaps) → childSource≤source

/-- Choose the largest represented source at the already selected grade.
The grade multiset remains exactly the same, up to permutation. -/
theorem maximum_source_at_grade (target source e : Nat) (gaps : List Nat)
    (cert : PoweredCertificate source e gaps) (active : Interval source target) :
    ∃ selected selectedE selectedGaps,
      PoweredCertificate selected selectedE selectedGaps ∧ Interval selected target ∧
      (grades selectedE selectedGaps).Perm (grades e gaps) ∧
      SourceMaximal target selected selectedE selectedGaps := by
  let P : Nat → Prop := fun child => ∃ f word,
    PoweredCertificate child f word ∧ Interval child target ∧
      (grades f word).Perm (grades e gaps)
  have present : ∃ n, P n := ⟨source,e,gaps,cert,active,List.Perm.refl _⟩
  have bounded : ∀ n, P n → n≤2^(grades e gaps).sum := by
    intro n hn
    obtain ⟨f,word,supplied,_,perm⟩ := hn
    have bound := source_grade_bound n f word supplied
    rwa [perm_sum perm] at bound
  obtain ⟨selected,⟨selectedE,selectedGaps,supplied,captures,perm⟩,maximal⟩ :=
    bounded_maximum P (2^(grades e gaps).sum) present bounded
  refine ⟨selected,selectedE,selectedGaps,supplied,captures,perm,?_⟩
  intro child f word supplied captures same
  exact maximal child ⟨f,word,supplied,captures,same.trans perm⟩

/-- The two selections are compatible: minimum grade first, then maximum
source value among precisely that grade. -/
theorem minimum_maximum_source (target source e : Nat) (gaps : List Nat)
    (cert : PoweredCertificate source e gaps) (active : Interval source target) :
    ∃ selected selectedE selectedGaps,
      PoweredCertificate selected selectedE selectedGaps ∧ Interval selected target ∧
      SourceMinimal target selected selectedE selectedGaps ∧
      SourceMaximal target selected selectedE selectedGaps := by
  obtain ⟨first,firstE,firstGaps,firstCert,firstActive,minimum⟩ :=
    minimum_capturing_source target source e gaps cert active
  obtain ⟨selected,selectedE,selectedGaps,supplied,captures,perm,maximum⟩ :=
    maximum_source_at_grade target first firstE firstGaps firstCert firstActive
  refine ⟨selected,selectedE,selectedGaps,supplied,captures,?_,maximum⟩
  intro child f word childCert childActive drop
  exact minimum child f word childCert childActive
    ((less_perm (List.Perm.refl _) perm).mp drop)

def SameGradeHyp (source e : Nat) (gaps : List Nat) : Prop :=
  ∀ child childTarget f word, Interval child childTarget →
    PoweredCertificate child f word → (grades f word).Perm (grades e gaps) →
    source<child → Basin childTarget

/-- The source-value tie break also supplies a full arbitrary-target
hypothesis for strictly larger sources at the same grade. -/
theorem original_same_grade_hyp (target source e : Nat) (gaps : List Nat)
    (positive : 0<target) (prior : Prior target)
    (maximum : SourceMaximal target source e gaps) : SameGradeHyp source e gaps := by
  classical
  intro child childTarget f word active cert perm grows
  apply Classical.byContradiction
  intro bad
  have least : target≤childTarget := by
    apply Classical.byContradiction
    intro smaller
    exact bad (prior childTarget active.1 (by omega))
  have bounded := maximum child f word cert
    ⟨positive,by have upper:=active.2; omega⟩ perm
  omega

private theorem orbit_agrees (n k : Nat) :
    CollatzUnboundedGapReset.orbit n k=CollatzRootedSourceFloor.orbit n k := by
  induction k generalizing n with
  | zero => rfl
  | succ k ih => exact ih (shortcut n)

/-- Any bad query with the original interval hypothesis already has the
future source floor. This uses successive steps of its SAME supplied witness. -/
theorem bad_query_floor (target source e : Nat) (gaps : List Nat)
    (large : 177≤target) (cert : PoweredCertificate source e gaps)
    (bad : ¬Basin target)
    (ih : CollatzGapComparison.Hyp Interval (grades e gaps)) :
    Safe (shortcut source) ((target-1)/2) := by
  classical
  intro clock
  apply Classical.byContradiction
  intro outside
  have high : 2<CollatzUnboundedGapReset.orbit source (clock+1) := by
    rw [orbit_agrees]
    change 2<CollatzRootedSourceFloor.orbit (shortcut source) clock
    omega
  obtain ⟨f,tail,endpoint,decrease⟩ :=
    CollatzSourceOrbitProgress.advance_certificate source (clock+1) e gaps cert high
  have drop : Less (grades f tail) (grades e gaps) := by
    rcases decrease with zero | strict
    · omega
    · exact strict
  have active : Interval (CollatzUnboundedGapReset.orbit source (clock+1)) target := by
    constructor
    · omega
    · rw [orbit_agrees]
      change target≤2*CollatzRootedSourceFloor.orbit (shortcut source) clock+1
      omega
  exact bad (ih _ target f tail active endpoint drop)

theorem least_bad_shape (target : Nat) (positive : 0<target)
    (bad : ¬Basin target) (prior : Prior target) :
    1105<target ∧ target%4=3 := by
  have large : 1105<target := by
    by_cases high : 1105<target
    · exact high
    · exact False.elim (bad (terminal_core_range target positive (by omega)))
  have odd : target%2=1 := by
    by_cases even : target%2=0
    · have child := prior (target/2) (by omega) (by omega)
      have value : target=2*(target/2) := by omega
      exact False.elim (bad (by rw [value]; exact (basin_twice (target/2)).mpr child))
    · omega
  have phase : target%4=3 := by
    have cases : target%4=1 ∨ target%4=3 := by omega
    rcases cases with one | three
    · let child := (3*target+1)/4
      have edge : 3*target+1=4*child := by dsimp [child]; omega
      have path : Prefix target [2] child := by
        refine ⟨by simp [PositiveGaps],?_⟩
        simpa [correction,total] using edge
      have childPositive : 0<child := by omega
      have smaller : child<target := by omega
      exact False.elim (bad ((prefix_basin path).mpr (prior child childPositive smaller)))
    · exact three
  exact ⟨large,phase⟩

/-- All already proved interval rules apply to the jointly selected source
with no change of witness. A bad query therefore has precisely the low shape. -/
theorem bad_query_low_shape (target source e : Nat) (gaps : List Nat)
    (large : 1105<target) (cert : PoweredCertificate source e gaps)
    (active : Interval source target) (bad : ¬Basin target)
    (ih : CollatzGapComparison.Hyp Interval (grades e gaps)) :
    1≤e ∧ e≤3 ∧ (∀ a∈gaps, a≤4) ∧ source+1<target := by
  have nonterminal : source≠1 := by have upper:=active.2; omega
  have bounded : ∀ a∈gaps, a≤4 := by
    intro a member
    by_cases small : a≤4
    · exact small
    · obtain ⟨front,tail,form⟩ := List.mem_iff_append.mp member
      subst gaps
      exact False.elim (bad (high_gap_powered_interval_rule source target e a front tail
        active.1 cert (by omega) ih))
  have esmall : e≤3 := by
    by_cases small : e≤3
    · exact small
    · exact False.elim (bad (large_even_interval_rule source target e gaps
        active.1 cert (by omega) ih))
  have epos : 1≤e := by
    by_cases zero : e=0
    · obtain ⟨q,parent,qcert⟩ := cert
      have same : source=q := by simpa [zero] using parent
      have odd : source%2=1 := by
        rw [same]
        exact witness_odd (certificate_witness qcert)
      have step : 2*shortcut source=3*source+1 := by unfold shortcut; split <;> omega
      have grown : Interval (shortcut source) target := ⟨active.1,by have h:=active.2; omega⟩
      exact False.elim (bad (CollatzGapComparison.ordinary_source
        (show PoweredCertificate source e gaps from ⟨q,parent,qcert⟩)
        nonterminal grown ih))
    · omega
  have far : source+1<target := by
    by_cases lower : source+1<target
    · exact lower
    · obtain ⟨q,parent,qcert⟩ := cert
      obtain ⟨f,eq⟩ := Nat.exists_eq_succ_of_ne_zero (by omega : e≠0)
      have form : source=2*(2^f*q) := by rw [parent,eq,Nat.pow_succ]; ac_rfl
      have step : 2*shortcut source=source := by simp [form,shortcut]
      have smaller : Interval (shortcut source) target := ⟨active.1,by omega⟩
      exact False.elim (bad (CollatzGapComparison.ordinary_source
        (show PoweredCertificate source e gaps from ⟨q,parent,qcert⟩)
        nonterminal smaller ih))
  exact ⟨epos,esmall,bounded,far⟩

/-- The original bad supplied word itself has the canonical fixed-tail form.
Neither its represented source nor its grade is replaced during normalization. -/
theorem bad_query_canonical (target source e : Nat) (gaps : List Nat)
    (large : 1105<target) (cert : PoweredCertificate source e gaps)
    (active : Interval source target) (bad : ¬Basin target)
    (ih : CollatzGapComparison.Hyp Interval (grades e gaps)) :
    ∃ q front, source=2^e*q ∧ Prefix q front 11 ∧ front≠[] ∧
      gaps=front++elevenTail ∧ 1≤e ∧ e≤3 ∧ (∀ a∈front, a≤4) ∧
      source+1<target := by
  obtain ⟨epos,esmall,bounded,far⟩ :=
    bad_query_low_shape target source e gaps large cert active bad ih
  obtain ⟨q,parent,qcert⟩ := cert
  rcases certificate_normal_form q gaps qcert bounded with
    ⟨c,k,value,_⟩ | ⟨front,k,path,form⟩
  · exact False.elim (bad (terminal_core_interval_rule source target e c
      (by simpa [value] using parent) esmall active))
  · cases k with
    | succ k =>
      subst gaps
      exact False.elim (bad (terminal_padding_interval_rule source target e q k front
        parent path active ih))
    | zero =>
      simp only [List.replicate_zero,List.append_nil] at form
      have nonempty : front≠[] := by
        intro empty
        have eleven : q=11 := by simpa [empty,correction,total] using path.2
        have powerBound : 2^e≤8 := Nat.pow_le_pow_right (by decide : 1≤2) esmall
        have sourceBound : source≤88 := by rw [parent,eleven]; omega
        have targetBound := active.2
        omega
      refine ⟨q,front,parent,path,nonempty,form,epos,esmall,?_,far⟩
      intro a member
      apply bounded a
      rw [form]
      simp [member]

/-- Every nonempty literal source prefix of a bad interval query has a
strictly contracting leading coefficient. This is an all-prefix restriction. -/
theorem bad_query_prefix_contracts (target source e : Nat) (gaps front tail : List Nat)
    (cert : PoweredCertificate source e gaps) (active : Interval source target)
    (bad : ¬Basin target) (ih : CollatzGapComparison.Hyp Interval (grades e gaps))
    (form : gaps=front++tail) (nonempty : front≠[]) :
    3^front.length<2^total front := by
  by_cases smaller : 3^front.length<2^total front
  · exact smaller
  · subst gaps
    exact False.elim (bad (CollatzLowIntervalRefinement.coefficient_interval_rule
      source target e front tail active cert nonempty (by omega) ih))

/-- One source certificate carries every resource simultaneously. The target
is least bad; the source has minimum grade and maximum value at that grade.
The canonical word is the selected supplied word itself. -/
structure JointBadQuery where
  target : Nat
  source : Nat
  e : Nat
  q : Nat
  front : List Nat
  target_large : 1105<target
  target_phase : target%4=3
  bad : ¬Basin target
  prior : Prior target
  parent : source=2^e*q
  path : Prefix q front 11
  nonempty : front≠[]
  even_positive : 1≤e
  even_bounded : e≤3
  gaps_bounded : ∀ a∈front, a≤4
  lower : source+1<target
  upper : target≤2*source+1
  certificate : PoweredCertificate source e (front++elevenTail)
  source_minimum : SourceMinimal target source e (front++elevenTail)
  source_maximum : SourceMaximal target source e (front++elevenTail)
  interval_hyp : CollatzGapComparison.Hyp Interval (grades e (front++elevenTail))
  same_grade_hyp : SameGradeHyp source e (front++elevenTail)
  future : Safe (shortcut source) ((target-1)/2)
  contracting : ∀ piece tail, front++elevenTail=piece++tail → piece≠[] →
    3^piece.length<2^total piece

/-- Global reduction to a canonical counterquery with BOTH induction
resources, the future source floor, and the source-value tie break. -/
theorem joint_counterexample (failure : ∃ n, 0<n ∧ ¬Basin n) :
    Nonempty JointBadQuery := by
  obtain ⟨target,positive,bad,prior⟩ := least_bad_target failure
  obtain ⟨large,phase⟩ := least_bad_shape target positive bad prior
  obtain ⟨initial,initialE,_,tail,_,_,_,_,_,_,_,_,upper,_,initialCert⟩ :=
    source_for_every_target target (by omega)
  obtain ⟨source,e,gaps,cert,active,minimum,maximum⟩ :=
    minimum_maximum_source target initial initialE (tail++elevenTail)
      initialCert ⟨positive,upper⟩
  have ih := original_interval_hyp target source e gaps positive prior minimum
  have sameGrade := original_same_grade_hyp target source e gaps positive prior maximum
  have floor := bad_query_floor target source e gaps (by omega) cert bad ih
  obtain ⟨q,front,parent,path,nonempty,form,epos,esmall,bounded,far⟩ :=
    bad_query_canonical target source e gaps large cert active bad ih
  subst gaps
  refine ⟨{
    target:=target, source:=source, e:=e, q:=q, front:=front,
    target_large:=large, target_phase:=phase, bad:=bad, prior:=prior,
    parent:=parent, path:=path, nonempty:=nonempty,
    even_positive:=epos, even_bounded:=esmall, gaps_bounded:=bounded,
    lower:=far, upper:=active.2, certificate:=cert,
    source_minimum:=minimum, source_maximum:=maximum,
    interval_hyp:=ih, same_grade_hyp:=sameGrade, future:=floor, contracting:=?_ }⟩
  intro piece tail form nonempty
  exact bad_query_prefix_contracts target source e (front++elevenTail) piece tail
    cert active bad ih form nonempty

/-- The full problem may now be closed only on this strengthened canonical
domain. All hypotheses are obtained jointly from a counterexample, rather
than independently supplied witnesses. This proposition remains unproved. -/
def FloorIntervalStep : Prop :=
  ∀ target source e q front, 1105<target → target%4=3 → Prior target →
    source=2^e*q → Prefix q front 11 → front≠[] →
    1≤e → e≤3 → (∀ a∈front, a≤4) → source+1<target → target≤2*source+1 →
    PoweredCertificate source e (front++elevenTail) →
    CollatzGapComparison.Hyp Interval (grades e (front++elevenTail)) →
    SameGradeHyp source e (front++elevenTail) →
    Safe (shortcut source) ((target-1)/2) →
    (∀ piece tail, front++elevenTail=piece++tail → piece≠[] →
      3^piece.length<2^total piece) → Basin target

/-- A floor-restricted return proof suffices for full Collatz. The only
remaining premise is the explicitly named FloorIntervalStep. -/
theorem collatz_of_floor_interval (cover : FloorIntervalStep) :
    ∀ n, 0<n → Basin n := by
  classical
  intro n positive
  apply Classical.byContradiction
  intro bad
  obtain ⟨query⟩ := joint_counterexample ⟨n,positive,bad⟩
  exact query.bad (cover query.target query.source query.e query.q query.front
    query.target_large query.target_phase query.prior query.parent query.path query.nonempty
    query.even_positive query.even_bounded query.gaps_bounded query.lower query.upper
    query.certificate query.interval_hyp query.same_grade_hyp query.future query.contracting)

/-- The reduction is exact: a universal Collatz proof immediately supplies
the restricted step, and the preceding theorem proves the converse. -/
theorem collatz_iff_floor_interval :
    (∀ n, 0<n → Basin n) ↔ FloorIntervalStep := by
  constructor
  · intro all target source e q front large _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    exact all target (by omega)
  · exact collatz_of_floor_interval

/-- The user's exact residue-512 certificate implication has the same new
frontier, using the already proved unrestricted-witness equivalence. -/
theorem original_residue_iff_floor_interval :
    CollatzWitness.ResidueImplication ↔ FloorIntervalStep :=
  CollatzWitness.original_iff_collatz.trans collatz_iff_floor_interval

end CollatzJointMinimalCounterexample
