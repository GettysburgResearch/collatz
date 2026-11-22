import WitnessCritical

/-!
Exact all-parameter split of the initial-exponent-two, head-three query.
The successful phase uses the current query's smaller-target induction;
the other phase retains an explicit ordinary reverse-even obligation.
No universal capture or Collatz convergence is assumed or asserted.
-/

namespace CollatzShell.MixedCoverAttack

open WitnessGlobal WitnessSynthesis

set_option maxHeartbeats 2000000
set_option maxRecDepth 10000

private theorem grade_drop_common {new old : List Nat}
    (drop : GradeDrop new old) (common : List Nat) :
    GradeDrop (common++new) (common++old) := by
  obtain ⟨a,lower,above⟩ := drop
  refine ⟨a,?_,?_⟩
  · simp only [List.count_append]
    omega
  · intro b hb
    simp only [List.count_append,above b hb]

/-- An arbitrary nonempty interior supplied block may be removed while
retaining the initial exponent, the leading three, and the literal tail. -/
theorem interior_grade_drop (e : Nat) (front tail : List Nat)
    (nonempty : front≠[]) :
    GradeDrop (sourceGrades e (3::tail))
      (sourceGrades e (3::(front++tail))) := by
  have drop := grade_drop_common (WitnessCritical.prefix_grade_drop front tail nonempty)
    ((if e=0 then [] else [2*e+1])++[6])
  simpa only [sourceGrades,ite_true,List.nil_append,List.map_cons,
    List.map_append,List.append_assoc,List.singleton_append] using drop

/-- Delete a growing interior block whose endpoint admits the same leading
gap. The replacement source is larger, its complete grade is smaller,
and every old interval target is covered without changing that target. -/
theorem interior_splice_interval_rule {q u v replacement e target : Nat}
    {front tail : List Nat} (gap : 3*q+1=8*u)
    (splice : 3*replacement+1=8*v) (growth : u<v)
    (nonempty : front≠[]) (_bridge : GapTrace u v front) (rest : GapTrace v 1 tail)
    (active : Interval (2^e*q) target)
    (ih : IntervalHyp (sourceGrades e (3::(front++tail)))) : Basin target := by
  have larger : q<replacement := by omega
  have rp : 0<replacement := by omega
  have cover : Interval (2^e*replacement) target := by
    have scaled := Nat.mul_le_mul_left (2^e) (Nat.le_of_lt larger)
    exact ⟨active.1,by have h:=active.2; omega⟩
  have cert : PoweredTrace (2^e*replacement) e (3::tail) :=
    ⟨replacement,rp,rfl,by exact ⟨by decide,v,by simpa using splice,rest⟩⟩
  exact ih (2^e*replacement) target e (3::tail) cover cert
    (interior_grade_drop e front tail nonempty)

/-- The complete source prefix [3,1] can always be replaced by [3].
The new odd source is 4u+1, and every active interval target is discharged. -/
theorem head_three_one_interval_rule {q e target : Nat} {tail : List Nat}
    (cert : GapTrace q 1 (3::1::tail))
    (active : Interval (2^e*q) target)
    (ih : IntervalHyp (sourceGrades e (3::1::tail))) : Basin target := by
  obtain ⟨_,u,gap,_,v,edge,rest⟩ := cert
  norm_num at gap edge
  exact interior_splice_interval_rule (front:=[1]) gap
    (replacement:=4*u+1) (by omega) (by omega) (by simp)
    (by exact ⟨by decide,v,by simpa using edge,rfl⟩) rest active ih

/-- The complete source prefix [3,2,1] can always be replaced by [3].
This excises the growing interior [2,1], although the whole prefix shrinks. -/
theorem head_three_two_one_interval_rule {q e target : Nat} {tail : List Nat}
    (cert : GapTrace q 1 (3::2::1::tail))
    (active : Interval (2^e*q) target)
    (ih : IntervalHyp (sourceGrades e (3::2::1::tail))) : Basin target := by
  obtain ⟨_,u,gap,_,v,first,_,z,last,rest⟩ := cert
  norm_num at gap first last
  have congruence : z%3=2 := by omega
  let replacement := (8*z-1)/3
  have splice : 3*replacement+1=8*z := by dsimp [replacement]; omega
  exact interior_splice_interval_rule (front:=[2,1]) gap splice
    (by omega) (by simp)
    (by exact ⟨by decide,v,by simpa using first,by decide,z,by simpa using last,rfl⟩)
    rest active ih

/-- Replace a supplied [3,4,1] prefix at initial exponent two by [3,3]
at exponent three. The deleted gap-four grade pays for the larger initial
run and extra gap three, and the actual replacement source is larger. -/
theorem head_three_four_one_interval_rule {q target : Nat} {tail : List Nat}
    (cert : GapTrace q 1 (3::4::1::tail))
    (active : Interval (4*q) target)
    (ih : IntervalHyp (sourceGrades 2 (3::4::1::tail))) : Basin target := by
  obtain ⟨_,u,first,_,v,second,_,z,third,rest⟩ := cert
  norm_num at first second third
  have phase : z%27=2 := by omega
  let j := z/27
  have zForm : z=27*j+2 := by dsimp [j]; omega
  let a := 72*j+5
  let replacement := 192*j+13
  have firstNew : 3*replacement+1=8*a := by dsimp [replacement,a]; omega
  have secondNew : 3*a+1=8*z := by dsimp [a]; omega
  have qp : q=256*j+13 := by omega
  have larger : 4*q<8*replacement := by dsimp [replacement]; omega
  have newCert : PoweredTrace (8*replacement) 3 (3::3::tail) := by
    refine ⟨replacement,by dsimp [replacement]; omega,by simp,?_⟩
    exact ⟨by decide,a,by simpa using firstNew,by decide,z,by simpa using secondNew,rest⟩
  have cover : Interval (8*replacement) target :=
    ⟨active.1,by have h:=active.2; omega⟩
  have drop : GradeDrop (sourceGrades 3 (3::3::tail))
      (sourceGrades 2 (3::4::1::tail)) := by
    refine ⟨8,?_,?_⟩
    · simp [sourceGrades]
    · intro b above
      have h2 : 2≠b := by omega
      have h5 : 5≠b := by omega
      have h6 : 6≠b := by omega
      have h7 : 7≠b := by omega
      have h8 : 8≠b := by omega
      simp [sourceGrades,h2,h5,h6,h7,h8]
  exact ih (8*replacement) target 3 (3::3::tail) cover newCert drop

private theorem trace_source_bound {q : Nat} {word : List Nat}
    (cert : GapTrace q 1 word) : q≤2^word.sum := by
  induction word generalizing q with
  | nil => change q=1 at cert; simp [cert]
  | cons a word induction =>
    obtain ⟨_,u,edge,rest⟩ := cert
    have smaller := Nat.mul_le_mul_left (2^a) (induction rest)
    have bound : q≤2^a*2^word.sum := by omega
    simpa only [List.sum_cons,pow_add] using bound

private theorem grades_sum_bound (e : Nat) (word : List Nat) :
    e+word.sum≤(sourceGrades e word).sum := by
  have mapped : (word.map (2*·)).sum=2*word.sum := by
    induction word with
    | nil => simp
    | cons a word induction => simp only [List.map_cons,List.sum_cons,induction]; omega
  by_cases zero : e=0
  · simp only [sourceGrades,zero,ite_true,List.nil_append,mapped]
    omega
  · simp only [sourceGrades,zero,ite_false,List.sum_append,List.sum_singleton,mapped]
    omega

/-- Every actual complete source has a finite ceiling depending only on
the sum of its grades. Equal grade multisets therefore share this ceiling. -/
theorem powered_source_ceiling {source e : Nat} {word : List Nat}
    (cert : PoweredTrace source e word) : source≤2^(sourceGrades e word).sum := by
  obtain ⟨q,_,rfl,trace⟩ := cert
  have first := Nat.mul_le_mul_left (2^e) (trace_source_bound trace)
  have second := Nat.pow_le_pow_right (by decide : 1≤2) (grades_sum_bound e word)
  exact le_trans (by simpa only [←pow_add] using first) second

/-- A larger source with the same complete grade multiset decreases a
natural-number defect. This is not induction on unbounded source growth. -/
theorem same_grade_source_defect_drop {source replacement e : Nat}
    {word old : List Nat} (cert : PoweredTrace replacement e word)
    (same : (sourceGrades e word).Perm old) (larger : source<replacement) :
    2^old.sum-replacement<2^old.sum-source := by
  have bound := powered_source_ceiling cert
  have equal := same.sum_eq
  rw [equal] at bound
  omega

/-- For each fixed grade multiset, bounded reverse source order is well
founded by the finite-ceiling defect. -/
theorem fixed_grade_source_tie_wellFounded (old : List Nat) :
    WellFounded (fun (replacement source : Nat) =>
      replacement≤2^old.sum ∧ source<replacement) := by
  have wf := InvImage.wf (fun source : Nat => 2^old.sum-source) Nat.lt_wfRel.wf
  apply wf.mono
  intro replacement source relation
  change 2^old.sum-replacement<2^old.sum-source
  omega

/-- The second induction coordinate permits a larger supplied source with
the same multiset. The preceding ceiling theorem gives its finite defect. -/
def LargerSameGradeHyp (source : Nat) (old : List Nat) : Prop :=
  ∀ replacement target e word, Interval replacement target →
    PoweredTrace replacement e word → (sourceGrades e word).Perm old →
    source<replacement → Basin target

/-- The source prefix [3,4,2] can be permuted to [2,3,4] at the same even
exponent. The new odd source is exactly q+4, the literal tail survives,
and the finite-defect source coordinate strictly decreases. -/
theorem head_three_four_two_interval_rule {q e target : Nat} {tail : List Nat}
    (cert : GapTrace q 1 (3::4::2::tail))
    (active : Interval (2^e*q) target)
    (ih : LargerSameGradeHyp (2^e*q) (sourceGrades e (3::4::2::tail))) :
    Basin target := by
  obtain ⟨_,u,first,_,v,second,_,z,third,rest⟩ := cert
  norm_num at first second third
  have phase : z%27=1 := by omega
  let j := z/27
  have zForm : z=27*j+1 := by dsimp [j]; omega
  have qForm : q=512*j+13 := by omega
  let a := 144*j+5
  let b := 384*j+13
  have firstNew : 3*(q+4)+1=4*b := by dsimp [b]; omega
  have secondNew : 3*b+1=8*a := by dsimp [b,a]; omega
  have thirdNew : 3*a+1=16*z := by dsimp [a]; omega
  have newCert : PoweredTrace (2^e*(q+4)) e (2::3::4::tail) := by
    refine ⟨q+4,by omega,rfl,?_⟩
    exact ⟨by decide,b,by simpa using firstNew,by decide,a,
      by simpa using secondNew,by decide,z,by simpa using thirdNew,rest⟩
  have same : (sourceGrades e (2::3::4::tail)).Perm
      (sourceGrades e (3::4::2::tail)) := by
    apply List.Perm.append_left
    simp only [List.map_cons]
    exact (List.Perm.swap _ _ _).trans (List.Perm.cons _ (List.Perm.swap _ _ _))
  have larger : 2^e*q<2^e*(q+4) :=
    Nat.mul_lt_mul_of_pos_left (by omega) (by positivity)
  have cover : Interval (2^e*(q+4)) target :=
    ⟨active.1,by have h:=active.2; omega⟩
  exact ih (2^e*(q+4)) target e (2::3::4::tail) cover newCert same larger

private theorem trace_positive_odd {u : Nat} {word : List Nat}
    (trace : GapTrace u 1 word) : 0<u ∧ u%2=1 := by
  cases word with
  | nil => change u=1 at trace; omega
  | cons a word =>
    obtain ⟨positive,v,edge,_⟩ := trace
    obtain ⟨b,rfl⟩ := Nat.exists_eq_succ_of_ne_zero (by omega : a≠0)
    have expansion : 2^(b+1)*v=2*(2^b*v) := by ring
    rw [expansion] at edge
    omega

private theorem trace_forced_one {u : Nat} {word : List Nat}
    (trace : GapTrace u 1 word) (phase : u%4=3) :
    ∃ tail, word=1::tail := by
  cases word with
  | nil => change u=1 at trace; omega
  | cons a tail =>
    obtain ⟨positive,v,edge,_⟩ := trace
    have one : a=1 := by
      by_contra no
      have two : 2≤a := by omega
      have expansion : 2^a=4*2^(a-2) := by
        conv_lhs => rw [show a=(a-2)+2 by omega,pow_add]
        ring
      rw [expansion] at edge
      have scaled : 3*u+1=4*(2^(a-2)*v) := by nlinarith [edge]
      omega
    exact ⟨tail,by rw [one]⟩

private theorem trace_forced_two_one {u : Nat} {word : List Nat}
    (trace : GapTrace u 1 word) (phase : u%16=9) :
    ∃ tail, word=2::1::tail := by
  cases word with
  | nil => change u=1 at trace; omega
  | cons a tail =>
    obtain ⟨positive,v,edge,rest⟩ := trace
    have oddV := (trace_positive_odd rest).2
    have two : a=2 := by
      by_cases one : a=1
      · norm_num [one] at edge
        omega
      · by_contra no
        have three : 3≤a := by omega
        have expansion : 2^a=8*2^(a-3) := by
          conv_lhs => rw [show a=(a-3)+3 by omega,pow_add]
          ring
        rw [expansion] at edge
        have scaled : 3*u+1=8*(2^(a-3)*v) := by nlinarith [edge]
        omega
    norm_num [two] at edge
    obtain ⟨suffix,eq⟩ := trace_forced_one rest (by omega)
    exact ⟨suffix,by rw [two,eq]⟩

private theorem trace_forced_two {u : Nat} {word : List Nat}
    (trace : GapTrace u 1 word) (phase : u%8=1) (nonterminal : u≠1) :
    ∃ tail, word=2::tail := by
  cases word with
  | nil => exact False.elim (nonterminal trace)
  | cons a tail =>
    obtain ⟨positive,v,edge,rest⟩ := trace
    have oddV := (trace_positive_odd rest).2
    have two : a=2 := by
      by_cases one : a=1
      · norm_num [one] at edge
        omega
      · by_contra no
        have three : 3≤a := by omega
        have expansion : 2^a=8*2^(a-3) := by
          conv_lhs => rw [show a=(a-3)+3 by omega,pow_add]
          ring
        rw [expansion] at edge
        have scaled : 3*u+1=8*(2^(a-3)*v) := by nlinarith [edge]
        omega
    exact ⟨tail,by rw [two]⟩

private theorem t_two_low_word {j : Nat} {word : List Nat}
    (trace : GapTrace (48*j+5) 1 word)
    (low : ∀ a∈word, a≤4) :
    ∃ tail, word=4::tail ∧ j%2=0 ∧ GapTrace (9*j+1) 1 tail := by
  cases word with
  | nil => change 48*j+5=1 at trace; omega
  | cons a tail =>
    obtain ⟨positive,v,edge,rest⟩ := trace
    have small := low a (by simp)
    have oddV := (trace_positive_odd rest).2
    have four : a=4 := by
      interval_cases a <;> norm_num at edge <;> omega
    norm_num [four] at edge
    have endpoint : v=9*j+1 := by omega
    exact ⟨tail,by rw [four],by omega,by simpa [endpoint] using rest⟩

/-- Binary valuation one forces a deletable [3,1] source prefix. This
discharges the whole interval, independently of the half-erasure phase. -/
theorem head_three_valuation_one_rule {q u e target w : Nat} {word : List Nat}
    (gap : 3*q+1=8*u) (rest : GapTrace u 1 word)
    (factor : 9*u-1=2*w) (oddW : w%2=1)
    (active : Interval (2^e*q) target)
    (ih : IntervalHyp (sourceGrades e (3::word))) : Basin target := by
  obtain ⟨tail,eq⟩ := trace_forced_one rest (by omega)
  rw [eq] at rest ih
  exact head_three_one_interval_rule
    (by exact ⟨by decide,u,by simpa using gap,rest⟩) active ih

/-- Every binary valuation at least four forces a deletable [3,2,1]
source prefix. There is no carry-size or supplied-tail length bound. -/
theorem head_three_valuation_large_rule {q u e target t w : Nat} {word : List Nat}
    (gap : 3*q+1=8*u) (rest : GapTrace u 1 word)
    (factor : 9*u-1=2^t*w) (large : 4≤t)
    (active : Interval (2^e*q) target)
    (ih : IntervalHyp (sourceGrades e (3::word))) : Basin target := by
  have expansion : 2^t=16*2^(t-4) := by
    conv_lhs => rw [show t=(t-4)+4 by omega,pow_add]
    ring
  have scaled : 9*u-1=16*(2^(t-4)*w) := by rw [factor,expansion]; ring
  have phase : u%16=9 := by omega
  obtain ⟨tail,eq⟩ := trace_forced_two_one rest phase
  rw [eq] at rest ih
  exact head_three_two_one_interval_rule
    (by exact ⟨by decide,u,by simpa using gap,rest⟩) active ih

/-- This is the same-source inner hypothesis of PR176, expressed in the
existing PR180 physical trace interface. It leaves the supplied source and
its complete certificate unchanged. -/
def SmallerTargetHyp (source target : Nat) : Prop :=
  ∀ child, Interval source child → child < target → Basin child

/-- At each outer source grade, the larger-source and smaller-target
permissions are simultaneously justified by two ordinary natural-number
inductions. A complete dispatcher remains an explicit input. -/
theorem close_fixed_grade_with_source_and_target (old : List Nat)
    (outer : IntervalHyp old)
    (dispatch : ∀ source target e word, (sourceGrades e word).Perm old →
      PoweredTrace source e word → Interval source target → IntervalHyp old →
      LargerSameGradeHyp source old → SmallerTargetHyp source target → Basin target) :
    ∀ source target e word, (sourceGrades e word).Perm old →
      PoweredTrace source e word → Interval source target → Basin target := by
  intro source
  induction source using (fixed_grade_source_tie_wellFounded old).induction with
  | h source sourceIH =>
    intro target
    induction target using Nat.strong_induction_on with
    | h target targetIH =>
      intro e word same cert active
      apply dispatch source target e word same cert active outer
      · intro replacement child newE newWord childActive childCert childSame larger
        have bound := powered_source_ceiling childCert
        rw [childSame.sum_eq] at bound
        exact sourceIH replacement ⟨bound,larger⟩ child newE newWord childSame childCert childActive
      · intro child childActive smaller
        exact targetIH child smaller e word same cert childActive

private theorem two_step_diamond {a : Nat} (phase : a % 4 = 2) :
    orbit 2 a = orbit 2 (3*a+2) := by
  have e : a % 2 = 0 := by omega
  have o : (a/2) % 2 ≠ 0 := by omega
  have f : (3*a+2) % 2 = 0 := by omega
  have g : ((3*a+2)/2) % 2 = 0 := by omega
  simp only [orbit,step,e,o,f,g,ite_true,ite_false]
  omega

/-- Four actual shortcut clocks expose a doubled psi query at the negative
nine carry. This uses the supplied source gap three, not its later tail. -/
theorem head_three_prefix_four {q u : Nat} (gap : 3*q+1=8*u) :
    orbit 4 (8*q-1)=36*u-5 := by
  have qp : 0<q := by omega
  have run := (odd_run 3 q qp).1
  have run' : orbit 3 (8*q-1)=27*q-1 := by simpa using run
  rw [show (4:Nat)=3+1 by rfl,orbit_add,run']
  change step (27*q-1)=36*u-5
  unfold step
  split <;> omega

/-- The proposed partner lies below the ORIGINAL head-three target at
every ordinary source size. No comparison with a later carry is used. -/
theorem head_three_partner_smaller {q u : Nat} (gap : 3*q+1=8*u) :
    0<18*u-3 ∧ 18*u-3<8*q-1 := by omega

private theorem head_three_forms {q u t w : Nat}
    (gap : 3*q+1=8*u) (factor : 9*u-1=2^t*w) :
    36*u-5=2^(t+2)*w-1 ∧ 18*u-3=2^(t+1)*w-1 := by
  have up : 0<u := by omega
  have base : 9*u=2^t*w+1 := by omega
  have p2 : 2^(t+2)*w=4*(2^t*w) := by ring
  have p1 : 2^(t+1)*w=2*(2^t*w) := by ring
  rw [p2,p1]
  omega

/-- All odd-run lengths are allowed. The complete physical merger has a
five-clock lag independent of t, and its partner is genuinely smaller. -/
theorem head_three_unbounded_merger {q u t w : Nat}
    (gap : 3*q+1=8*u) (factor : 9*u-1=2^t*w) (wp : 0<w)
    (phase : (3^t*w)%4=1) :
    orbit (t+8) (8*q-1)=orbit (t+3) (18*u-3) := by
  obtain ⟨leftForm,rightForm⟩ := head_three_forms gap factor
  have ap : 0<3^(t+1)*w := Nat.mul_pos (by positivity) wp
  have aPhase : (3^(t+1)*w)%4=3 := by
    rw [show 3^(t+1)*w=3*(3^t*w) by ring,Nat.mul_mod,phase]
  let a := 3^(t+1)*w-1
  have ae : a%4=2 := by dsimp [a]; omega
  have next : 3^(t+2)*w-1=3*a+2 := by
    have eq : 3^(t+2)*w=3*(3^(t+1)*w) := by ring
    dsimp [a]
    omega
  calc
    orbit (t+8) (8*q-1)
        =orbit ((t+2)+2) (orbit 4 (8*q-1)) := by rw [←orbit_add]; congr 1; omega
    _ =orbit ((t+2)+2) (2^(t+2)*w-1) := by rw [head_three_prefix_four gap,leftForm]
    _ =orbit 2 (3^(t+2)*w-1) := by rw [orbit_add,(odd_run (t+2) w wp).1]
    _ =orbit 2 (3*a+2) := by rw [next]
    _ =orbit 2 a := (two_step_diamond ae).symm
    _ =orbit ((t+1)+2) (2^(t+1)*w-1) := by rw [orbit_add,(odd_run (t+1) w wp).1]
    _ =orbit (t+3) (18*u-3) := by rw [rightForm]

/-- The favorable phase closes under the same-source target induction.
It therefore covers arbitrary supplied complete tails without constructing
or charging any new certificate for the smaller ordinary partner. -/
theorem head_three_same_source_rule {source q u t w : Nat}
    (gap : 3*q+1=8*u) (factor : 9*u-1=2^t*w) (wp : 0<w)
    (phase : (3^t*w)%4=1) (active : Interval source (8*q-1))
    (inner : SmallerTargetHyp source (8*q-1)) : Basin (8*q-1) := by
  obtain ⟨positive,smaller⟩ := head_three_partner_smaller gap
  have partner := inner (18*u-3) ⟨positive,by have h:=active.2; omega⟩ smaller
  have meeting := head_three_unbounded_merger gap factor wp phase
  have endpoint := (basin_at_hit (show Hits (18*u-3) (orbit (t+3) (18*u-3)) from
    ⟨t+3,rfl⟩)).mp partner
  rw [←meeting] at endpoint
  exact (basin_at_hit (show Hits (8*q-1) (orbit (t+8) (8*q-1)) from
    ⟨t+8,rfl⟩)).mpr endpoint

/-- In the complementary phase the actual two arms reduce to the ordinary
pair (6c+1,c). Its convergence/merger is retained as an obligation. -/
theorem head_three_residual_pair {q u t w c : Nat}
    (gap : 3*q+1=8*u) (factor : 9*u-1=2^t*w) (wp : 0<w)
    (residual : 3^(t+1)*w=4*c+1) :
    orbit (t+7) (8*q-1)=6*c+1 ∧
    orbit (t+3) (18*u-3)=c := by
  obtain ⟨leftForm,rightForm⟩ := head_three_forms gap factor
  constructor
  · calc
      orbit (t+7) (8*q-1)
          =orbit ((t+2)+1) (orbit 4 (8*q-1)) := by rw [←orbit_add]; congr 1; omega
      _ =orbit ((t+2)+1) (2^(t+2)*w-1) := by rw [head_three_prefix_four gap,leftForm]
      _ =step (3^(t+2)*w-1) := by rw [orbit_add,(odd_run (t+2) w wp).1]; rfl
      _ =step (2*(6*c+1)) := by
        congr 1
        have eq : 3^(t+2)*w=3*(3^(t+1)*w) := by ring
        rw [eq,residual]
        omega
      _ =6*c+1 := step_double _
  · calc
      orbit (t+3) (18*u-3)
          =orbit ((t+1)+2) (2^(t+1)*w-1) := by rw [rightForm]
      _ =orbit 2 (3^(t+1)*w-1) := by rw [orbit_add,(odd_run (t+1) w wp).1]
      _ =orbit 2 (4*c) := by simp only [residual,Nat.add_sub_cancel]
      _ =c := by simpa using orbit_pad 2 c

/-- The reverse-even pair exactly preserves both basin questions; it is
not an implication obtained by discarding the larger arm. -/
theorem head_three_residual_equivalence {q u t w c : Nat}
    (gap : 3*q+1=8*u) (factor : 9*u-1=2^t*w) (wp : 0<w)
    (residual : 3^(t+1)*w=4*c+1) :
    (Basin (8*q-1) ↔ Basin (6*c+1)) ∧
    (Basin (18*u-3) ↔ Basin c) := by
  obtain ⟨left,right⟩ := head_three_residual_pair gap factor wp residual
  exact ⟨basin_at_hit ⟨t+7,left⟩,basin_at_hit ⟨t+3,right⟩⟩

/-- The source edge fixes the ternary cofactor class at every binary
valuation, retaining the ordinary source rather than a completion. -/
theorem head_three_cofactor_class {q u t w : Nat}
    (gap : 3*q+1=8*u) (factor : 9*u-1=2^t*w) :
    (2^t*w)%27=17 ∧ w%3≠0 := by
  have up : 0<u := by omega
  have congruence : (2^t*w)%27=17 := by omega
  refine ⟨congruence,?_⟩
  intro zero
  have divisible : (2^t*w)%3=0 := by rw [Nat.mul_mod,zero]; simp
  omega

/-- The residual lies in the smaller ternary class 2 mod9. The displayed
cofactor is a ternary unit, so its exact ternary valuation is t+1. -/
theorem head_three_residual_ternary {q u t w c : Nat}
    (gap : 3*q+1=8*u) (factor : 9*u-1=2^t*w) (positiveT : 1≤t)
    (residual : 3^(t+1)*w=4*c+1) :
    c%9=2 ∧ (2^t*w)%27=17 ∧ w%3≠0 := by
  have expansion : 3^(t+1)=9*3^(t-1) := by
    rw [show t+1=(t-1)+2 by omega,pow_add]
    ring
  have scaled : 4*c+1=9*(3^(t-1)*w) := by rw [←residual,expansion]; ring
  exact ⟨by omega,head_three_cofactor_class gap factor⟩

/-- The cofactor is classified modulo108 by the binary valuation modulo18.
The table combines the actual source's class modulo27 with the failed
half-erasure phase modulo4. -/
def residualCofactor (r : Nat) : Nat :=
  match r with
  | 0 => 71 | 1 => 49 | 2 => 11 | 3 => 73 | 4 => 23 | 5 => 25
  | 6 => 107 | 7 => 13 | 8 => 47 | 9 => 37 | 10 => 59 | 11 => 97
  | 12 => 35 | 13 => 85 | 14 => 83 | 15 => 1 | 16 => 95 | _ => 61

private theorem binary_mod_period (t : Nat) : 2^(t+18)%27=2^t%27 := by
  rw [pow_add,Nat.mul_mod]
  norm_num

private theorem ternary_mod_period (t : Nat) : 3^(t+18)%4=3^t%4 := by
  rw [pow_add,Nat.mul_mod]
  norm_num

private theorem powers_mod_eighteen (t : Nat) :
    2^t%27=2^(t%18)%27 ∧ 3^t%4=3^(t%18)%4 := by
  induction t using Nat.strong_induction_on with
  | h t ih =>
    by_cases small : t<18
    · simp [Nat.mod_eq_of_lt small]
    · have positive : 0<t := by omega
      obtain ⟨a,b⟩ := ih (t-18) (by omega)
      have shift : t=t-18+18 := by omega
      have residue : (t-18)%18=t%18 := by omega
      constructor
      · calc
          2^t%27=2^(t-18)%27 := by conv_lhs => rw [shift]; exact binary_mod_period _
          _ =2^(t%18)%27 := by rw [a,residue]
      · calc
          3^t%4=3^(t-18)%4 := by conv_lhs => rw [shift]; exact ternary_mod_period _
          _ =3^(t%18)%4 := by rw [b,residue]

set_option maxRecDepth 10000 in
private theorem residual_table_finite :
    ∀ (r : Fin 18) (w : Fin 108),
      ((2^r.val*w.val)%27=17 ∧ (3^r.val*w.val)%4=3) ↔
        w.val=residualCofactor r.val := by decide

private theorem residual_table (r w : Nat) (small : r<18) :
    ((2^r*w)%27=17 ∧ (3^r*w)%4=3) ↔ w%108=residualCofactor r := by
  have a : (w%108)%27=w%27 := Nat.mod_mod_of_dvd w (by decide : 27∣108)
  have b : (w%108)%4=w%4 := Nat.mod_mod_of_dvd w (by decide : 4∣108)
  have f := residual_table_finite ⟨r,small⟩ ⟨w%108,Nat.mod_lt _ (by decide)⟩
  change ((2^r*(w%108))%27=17 ∧ (3^r*(w%108))%4=3) ↔
    w%108=residualCofactor r at f
  have left : (2^r*(w%108))%27=(2^r*w)%27 := by
    calc
      (2^r*(w%108))%27=((2^r%27)*((w%108)%27))%27 := Nat.mul_mod _ _ _
      _ =((2^r%27)*(w%27))%27 := by rw [a]
      _ =(2^r*w)%27 := (Nat.mul_mod _ _ _).symm
  have right : (3^r*(w%108))%4=(3^r*w)%4 := by
    calc
      (3^r*(w%108))%4=((3^r%4)*((w%108)%4))%4 := Nat.mul_mod _ _ _
      _ =((3^r%4)*(w%4))%4 := by rw [b]
      _ =(3^r*w)%4 := (Nat.mul_mod _ _ _).symm
  simpa only [left,right] using f

/-- An exact finite residue test at every unbounded binary valuation. -/
theorem residual_cofactor_classification (t w : Nat) :
    ((2^t*w)%27=17 ∧ (3^t*w)%4=3) ↔
      w%108=residualCofactor (t%18) := by
  obtain ⟨a,b⟩ := powers_mod_eighteen t
  have left : (2^t*w)%27=(2^(t%18)*w)%27 := by
    calc
      (2^t*w)%27=((2^t%27)*(w%27))%27 := Nat.mul_mod _ _ _
      _ =((2^(t%18)%27)*(w%27))%27 := by rw [a]
      _ =(2^(t%18)*w)%27 := (Nat.mul_mod _ _ _).symm
  have right : (3^t*w)%4=(3^(t%18)*w)%4 := by
    calc
      (3^t*w)%4=((3^t%4)*(w%4))%4 := Nat.mul_mod _ _ _
      _ =((3^(t%18)%4)*(w%4))%4 := by rw [b]
      _ =(3^(t%18)*w)%4 := (Nat.mul_mod _ _ _).symm
  rw [left,right]
  exact residual_table _ _ (Nat.mod_lt _ (by decide))

/-- Every failed head-three half-erasure belongs to one of eighteen
explicit unbounded cofactor families. No bound on the source or t is used. -/
theorem head_three_residual_parameterization {q u t w : Nat}
    (gap : 3*q+1=8*u) (factor : 9*u-1=2^t*w)
    (failed : (3^t*w)%4=3) :
    ∃ j, w=108*j+residualCofactor (t%18) := by
  have cls := (residual_cofactor_classification t w).mp
    ⟨(head_three_cofactor_class gap factor).1,failed⟩
  exact ⟨w/108,by omega⟩

private theorem odd_core (n : Nat) (positive : 0<n) :
    ∃ t w, 0<w ∧ w%2=1 ∧ n=2^t*w := by
  induction n using Nat.strong_induction_on with
  | h n ih =>
    by_cases odd : n%2=1
    · exact ⟨0,n,positive,odd,by simp⟩
    · obtain ⟨t,w,wp,wo,eq⟩ := ih (n/2) (by omega) (by omega)
      refine ⟨t+1,w,wp,wo,?_⟩
      have form : 2^(t+1)*w=2*(2^t*w) := by ring
      rw [form,←eq]
      omega

/-- The two arithmetic phases exhaust every actual odd head-three source.
The failed branch retains a positive ordinary residual and exact cofactor
class; successful termination of that residual is not assumed. -/
theorem head_three_exhaustive_split {q u : Nat}
    (gap : 3*q+1=8*u) (oddU : u%2=1) :
    ∃ t w, 1≤t ∧ 0<w ∧ w%2=1 ∧ 9*u-1=2^t*w ∧
      ((orbit (t+8) (8*q-1)=orbit (t+3) (18*u-3)) ∨
       ∃ c j, 0<c ∧ c%9=2 ∧ 3^(t+1)*w=4*c+1 ∧
         w=108*j+residualCofactor (t%18) ∧
         orbit (t+7) (8*q-1)=6*c+1 ∧ orbit (t+3) (18*u-3)=c) := by
  obtain ⟨t,w,wp,wo,factor⟩ := odd_core (9*u-1) (by omega)
  have tp : 1≤t := by
    by_contra no
    have zero : t=0 := by omega
    simp only [zero,pow_zero,one_mul] at factor
    omega
  refine ⟨t,w,tp,wp,wo,factor,?_⟩
  have ternaryOdd : (3^t*w)%2=1 := by
    rw [Nat.mul_mod,Nat.pow_mod,wo]
    norm_num
  by_cases phase : (3^t*w)%4=1
  · exact Or.inl (head_three_unbounded_merger gap factor wp phase)
  · have failed : (3^t*w)%4=3 := by omega
    have p : 0<3^(t+1)*w := Nat.mul_pos (by positivity) wp
    have residue : (3^(t+1)*w)%4=1 := by
      rw [show 3^(t+1)*w=3*(3^t*w) by ring,Nat.mul_mod,failed]
    let c := (3^(t+1)*w-1)/4
    have ceq : 3^(t+1)*w=4*c+1 := by dsimp [c]; omega
    have cphase := (head_three_residual_ternary gap factor tp ceq).1
    obtain ⟨j,param⟩ := head_three_residual_parameterization gap factor failed
    exact Or.inr ⟨c,j,by omega,cphase,ceq,param,
      head_three_residual_pair gap factor wp ceq⟩

/-- This sufficient remaining implication is an explicit hypothesis. It
only concerns the eighteen unbounded residual parameter families. -/
def ResidualReturn : Prop :=
  ∀ t w c, 1≤t → 0<w → (∃ j, w=108*j+residualCofactor (t%18)) →
    3^(t+1)*w=4*c+1 → Basin c → Basin (6*c+1)

/-- The displayed residual return implication would close the ENTIRE
head-three psi branch in the mixed induction, with arbitrary source tails.
It is not asserted that ResidualReturn itself holds. -/
theorem head_three_of_residual_return (returnRule : ResidualReturn)
    {source q u : Nat} (gap : 3*q+1=8*u) (oddU : u%2=1)
    (active : Interval source (8*q-1))
    (inner : SmallerTargetHyp source (8*q-1)) : Basin (8*q-1) := by
  obtain ⟨positive,smaller⟩ := head_three_partner_smaller gap
  have partner := inner (18*u-3) ⟨positive,by have h:=active.2; omega⟩ smaller
  obtain ⟨t,w,tp,wp,_,_,cases⟩ := head_three_exhaustive_split gap oddU
  rcases cases with meeting | ⟨c,j,_,_,residual,param,left,right⟩
  · have endpoint := (basin_at_hit (show Hits (18*u-3) (orbit (t+3) (18*u-3)) from
      ⟨t+3,rfl⟩)).mp partner
    rw [←meeting] at endpoint
    exact (basin_at_hit (show Hits (8*q-1) (orbit (t+8) (8*q-1)) from
      ⟨t+8,rfl⟩)).mpr endpoint
  · have small := (basin_at_hit ⟨t+3,right⟩).mp partner
    have large := returnRule t w c tp wp ⟨j,param⟩ residual small
    exact (basin_at_hit ⟨t+7,left⟩).mpr large

/-- With the supplied complete word retained, mixed source-grade and
same-source target induction leaves only TWO affine residual families.
Every other binary valuation is discharged, uniformly over every tail. -/
theorem head_three_two_family_frontier {q u : Nat} {word : List Nat}
    (gap : 3*q+1=8*u) (rest : GapTrace u 1 word)
    (inner : SmallerTargetHyp (4*q) (8*q-1))
    (outer : IntervalHyp (sourceGrades 2 (3::word))) :
    Basin (8*q-1) ∨
      (∃ j, q=128*j+13 ∧ u=48*j+5 ∧ Basin (729*j+74) ∧
        (Basin (8*q-1) ↔ Basin (6*(729*j+74)+1))) ∨
      (∃ j, q=256*j+173 ∧ u=96*j+65 ∧ Basin (2187*j+1478) ∧
        (Basin (8*q-1) ↔ Basin (6*(2187*j+1478)+1))) := by
  have active : Interval (4*q) (8*q-1) := ⟨by omega,by omega⟩
  have poweredActive : Interval (2^2*q) (8*q-1) := by simpa using active
  obtain ⟨t,w,tp,wp,wo,factor,cases⟩ :=
    head_three_exhaustive_split gap (trace_positive_odd rest).2
  by_cases one : t=1
  · left
    apply head_three_valuation_one_rule gap rest (w:=w) _ wo poweredActive outer
    simpa [one] using factor
  by_cases large : 4≤t
  · exact Or.inl (head_three_valuation_large_rule gap rest factor large poweredActive outer)
  obtain ⟨positive,smaller⟩ := head_three_partner_smaller gap
  have partner := inner (18*u-3) ⟨positive,by omega⟩ smaller
  rcases cases with meeting | ⟨c,j,_,_,residual,param,left,right⟩
  · left
    have endpoint := (basin_at_hit (show Hits (18*u-3) (orbit (t+3) (18*u-3)) from
      ⟨t+3,rfl⟩)).mp partner
    rw [←meeting] at endpoint
    exact (basin_at_hit (show Hits (8*q-1) (orbit (t+8) (8*q-1)) from
      ⟨t+8,rfl⟩)).mpr endpoint
  · have small := (basin_at_hit ⟨t+3,right⟩).mp partner
    have equiv := basin_at_hit (show Hits (8*q-1) (6*c+1) from ⟨t+7,left⟩)
    have cases : t=2 ∨ t=3 := by omega
    rcases cases with two | three
    · norm_num [two,residualCofactor] at param factor residual
      have ceq : c=729*j+74 := by omega
      right; left
      exact ⟨j,by omega,by omega,by simpa [ceq] using small,by simpa [ceq] using equiv⟩
    · norm_num [three,residualCofactor] at param factor residual
      have ceq : c=2187*j+1478 := by omega
      right; right
      exact ⟨j,by omega,by omega,by simpa [ceq] using small,by simpa [ceq] using equiv⟩

/-- The last unhandled even-j residue in the valuation-two family has
an actual thirteen-clock descent below its ORIGINAL target. -/
theorem head_three_two_residue_descent (h : Nat) :
    orbit 13 (8192*h+4199)=6561*h+3364 ∧
      0<6561*h+3364 ∧ 6561*h+3364<8192*h+4199 := by
  have first := (head_three_residual_pair (q:=1024*h+525) (u:=384*h+197)
    (t:=2) (w:=864*h+443) (c:=5832*h+2990)
    (by omega) (by norm_num; omega) (by omega) (by norm_num; omega)).1
  have left : orbit 9 (8192*h+4199)=34992*h+17941 := by
    change orbit 9 (8*(1024*h+525)-1)=6*(5832*h+2990)+1 at first
    rw [show 8*(1024*h+525)-1=8192*h+4199 by omega,
      show 6*(5832*h+2990)+1=34992*h+17941 by omega] at first
    exact first
  have last : orbit 4 (34992*h+17941)=6561*h+3364 :=
    one_gap_orbit (by decide) (by norm_num; omega)
  refine ⟨?_,by omega,by omega⟩
  calc
    orbit 13 (8192*h+4199)=orbit 4 (orbit 9 (8192*h+4199)) := by
      rw [←orbit_add]
    _ =6561*h+3364 := by rw [left,last]

/-- The ENTIRE valuation-two residual family with a supplied low-alphabet
word closes. Its even source parameters split into the two successful
source surgeries and one exact ordinary descent; the terminal parameter
is checked by its complete physical orbit. -/
theorem head_three_two_low_family_rule {j : Nat} {word : List Nat}
    (trace : GapTrace (48*j+5) 1 word) (low : ∀ a∈word, a≤4)
    (inner : SmallerTargetHyp (4*(128*j+13)) (8*(128*j+13)-1))
    (outer : IntervalHyp (sourceGrades 2 (3::word)))
    (tie : LargerSameGradeHyp (4*(128*j+13)) (sourceGrades 2 (3::word))) :
    Basin (8*(128*j+13)-1) := by
  by_cases zero : j=0
  · subst j
    exact ⟨56,by decide⟩
  obtain ⟨tail,wordEq,even,rest⟩ := t_two_low_word trace low
  rw [wordEq] at outer tie
  have full : GapTrace (128*j+13) 1 (3::4::tail) := by
    exact ⟨by decide,48*j+5,by norm_num; omega,
      by decide,9*j+1,by norm_num; omega,rest⟩
  have active : Interval (4*(128*j+13)) (8*(128*j+13)-1) := ⟨by omega,by omega⟩
  by_cases first : j%4=2
  · obtain ⟨suffix,eq⟩ := trace_forced_one rest (by omega)
    rw [eq] at full outer
    exact head_three_four_one_interval_rule full active outer
  by_cases second : j%8=0
  · obtain ⟨suffix,eq⟩ := trace_forced_two rest (by omega) (by omega)
    rw [eq] at full tie
    apply head_three_four_two_interval_rule (e:=2) full
    · simpa using active
    · simpa using tie
  · have phase : j%8=4 := by omega
    let h := j/8
    have jForm : j=8*h+4 := by dsimp [h]; omega
    have targetForm : 8*(128*j+13)-1=8192*h+4199 := by omega
    obtain ⟨clock,positive,smaller⟩ := head_three_two_residue_descent h
    have child : Basin (6561*h+3364) :=
      inner (6561*h+3364) ⟨positive,by have bound:=active.2; omega⟩ (by omega)
    apply (basin_at_hit (show Hits (8*(128*j+13)-1) (6561*h+3364) from ?_)).mpr child
    exact ⟨13,by rw [targetForm]; exact clock⟩

/-- The valuation-three residual retains the literal source prefix
[3,2,2] and the actual complete certificate at its displayed endpoint. -/
theorem head_three_three_forced_prefix {j : Nat} {word : List Nat}
    (trace : GapTrace (96*j+65) 1 word) :
    ∃ tail, word=2::2::tail ∧ GapTrace (54*j+37) 1 tail := by
  obtain ⟨middle,first⟩ := trace_forced_two trace (by omega) (by omega)
  rw [first] at trace
  obtain ⟨_,v,edge,rest⟩ := trace
  norm_num at edge
  have vForm : v=72*j+49 := by omega
  obtain ⟨tail,second⟩ := trace_forced_two rest (by omega) (by omega)
  rw [second] at rest
  obtain ⟨_,z,last,finish⟩ := rest
  norm_num at last
  have zForm : z=54*j+37 := by omega
  exact ⟨tail,by rw [first,second],by simpa [zForm] using finish⟩

/-- Exhaustive final low-alphabet head-three split. The valuation-one,
valuation-two, and every valuation-at-least-four branch are discharged.
Only one affine valuation-three family remains, with all original-source
constraints, its literal [3,2,2] prefix, and the residual basin obligation. -/
theorem head_three_low_final_frontier {q u : Nat} {word : List Nat}
    (gap : 3*q+1=8*u) (rest : GapTrace u 1 word)
    (low : ∀ a∈word, a≤4)
    (inner : SmallerTargetHyp (4*q) (8*q-1))
    (outer : IntervalHyp (sourceGrades 2 (3::word)))
    (tie : LargerSameGradeHyp (4*q) (sourceGrades 2 (3::word))) :
    Basin (8*q-1) ∨ ∃ j tail,
      q=256*j+173 ∧ u=96*j+65 ∧ word=2::2::tail ∧
      GapTrace (54*j+37) 1 tail ∧ Basin (2187*j+1478) ∧
      (Basin (8*q-1) ↔ Basin (6*(2187*j+1478)+1)) := by
  rcases head_three_two_family_frontier gap rest inner outer with
    paid | two | three
  · exact Or.inl paid
  · obtain ⟨j,qForm,uForm,_,_⟩ := two
    subst q
    subst u
    exact Or.inl (head_three_two_low_family_rule rest low inner outer tie)
  · obtain ⟨j,qForm,uForm,small,equivalence⟩ := three
    have trace : GapTrace (96*j+65) 1 word := by simpa [uForm] using rest
    obtain ⟨tail,wordEq,finish⟩ := head_three_three_forced_prefix trace
    exact Or.inr ⟨j,tail,qForm,uForm,wordEq,finish,small,equivalence⟩

end CollatzShell.MixedCoverAttack

#print axioms CollatzShell.MixedCoverAttack.head_three_prefix_four
#print axioms CollatzShell.MixedCoverAttack.head_three_partner_smaller
#print axioms CollatzShell.MixedCoverAttack.head_three_unbounded_merger
#print axioms CollatzShell.MixedCoverAttack.head_three_same_source_rule
#print axioms CollatzShell.MixedCoverAttack.head_three_residual_pair
#print axioms CollatzShell.MixedCoverAttack.head_three_residual_equivalence
#print axioms CollatzShell.MixedCoverAttack.head_three_cofactor_class
#print axioms CollatzShell.MixedCoverAttack.head_three_residual_ternary
#print axioms CollatzShell.MixedCoverAttack.residual_cofactor_classification
#print axioms CollatzShell.MixedCoverAttack.head_three_residual_parameterization
#print axioms CollatzShell.MixedCoverAttack.head_three_exhaustive_split
#print axioms CollatzShell.MixedCoverAttack.head_three_of_residual_return
#print axioms CollatzShell.MixedCoverAttack.interior_grade_drop
#print axioms CollatzShell.MixedCoverAttack.interior_splice_interval_rule
#print axioms CollatzShell.MixedCoverAttack.head_three_one_interval_rule
#print axioms CollatzShell.MixedCoverAttack.head_three_two_one_interval_rule
#print axioms CollatzShell.MixedCoverAttack.head_three_valuation_one_rule
#print axioms CollatzShell.MixedCoverAttack.head_three_valuation_large_rule
#print axioms CollatzShell.MixedCoverAttack.head_three_two_family_frontier

#print axioms CollatzShell.MixedCoverAttack.head_three_four_one_interval_rule
#print axioms CollatzShell.MixedCoverAttack.powered_source_ceiling
#print axioms CollatzShell.MixedCoverAttack.same_grade_source_defect_drop
#print axioms CollatzShell.MixedCoverAttack.fixed_grade_source_tie_wellFounded
#print axioms CollatzShell.MixedCoverAttack.head_three_four_two_interval_rule
#print axioms CollatzShell.MixedCoverAttack.close_fixed_grade_with_source_and_target
#print axioms CollatzShell.MixedCoverAttack.head_three_two_residue_descent
#print axioms CollatzShell.MixedCoverAttack.head_three_two_low_family_rule
#print axioms CollatzShell.MixedCoverAttack.head_three_three_forced_prefix
#print axioms CollatzShell.MixedCoverAttack.head_three_low_final_frontier
