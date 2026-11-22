import Collatz.LowIntervalRefinement

set_option autoImplicit false
set_option maxHeartbeats 2000000
set_option maxRecDepth 2000

namespace CollatzSourceEnvelope

open CollatzReverseBasin CollatzClosure CollatzWitness CollatzGapMultiset
open CollatzHighGapPump CollatzLowIntervalRefinement CollatzBoundedGapCofinal

/-- Largest initial even exponent payable after consuming a literal prefix. -/
def boost (e : Nat) : List Nat → Nat
  | [] => e
  | a::word => boost (max e (a-1)) word

theorem boost_ge_initial (e : Nat) (word : List Nat) : e≤boost e word := by
  induction word generalizing e with
  | nil => exact Nat.le_refl _
  | cons a word ih =>
    exact Nat.le_trans (Nat.le_max_left _ _) (ih (max e (a-1)))

theorem boost_ge_gap {a e : Nat} {word : List Nat} (mem : a∈word) :
    a-1≤boost e word := by
  induction word generalizing e with
  | nil => simp at mem
  | cons b word ih =>
    rcases List.mem_cons.mp mem with eq | ht
    · subst a
      exact Nat.le_trans (Nat.le_max_right _ _) (boost_ge_initial _ _)
    · exact ih ht

theorem boosted_step_rank (e a : Nat) (tail : List Nat) (positive : 1≤e) :
    Less (grades (max e (a-1)) tail) (grades e (a::tail)) := by
  by_cases keep : a-1≤e
  · rw [Nat.max_eq_left keep]
    exact prefix_rank e [a] tail (by simp)
  · rw [Nat.max_eq_right (by omega : e≤a-1)]
    exact shortened_gap_rank e a tail positive (by omega)

/-- Maximum powered source among all literal cuts, including the current one. -/
def crest (e q : Nat) : List Nat → Nat
  | [] => 2^e*q
  | a::word => max (2^e*q) (crest (max e (a-1)) ((3*q+1)/2^a) word)

/-- Maximum strictly lower-ranked literal-cut source. The empty-prefix option
halves the initial powered source; every nonempty prefix uses its maximal
payable even run. No intermediate interval membership is required. -/
def envelope (e q : Nat) : List Nat → Nat
  | [] => 2^(e-1)*q
  | a::word => max (2^(e-1)*q)
      (crest (max e (a-1)) ((3*q+1)/2^a) word)

theorem crest_self (e q : Nat) (word : List Nat) : 2^e*q≤crest e q word := by
  cases word with
  | nil => exact Nat.le_refl _
  | cons a word => exact Nat.le_max_left _ _

private theorem successor_value {q a u : Nat} (edge : 3*q+1=2^a*u) :
    (3*q+1)/2^a=u := by
  rw [edge]
  exact Nat.mul_div_cancel_left _ (Nat.pow_pos (by decide))

private theorem empty_prefix (q : Nat) : Prefix q [] q := by
  simp [Prefix,PositiveGaps,correction,total]

/-- The finite maximum is attained by an actual source with the literal
remaining certificate. The accumulated run equals the prefix's boost. -/
theorem crest_witness {e q : Nat} {word : List Nat}
    (positive : 1≤e) (cert : Certificate q word) :
    ∃ front tail u f, word=front++tail ∧ Prefix q front u ∧
      f=boost e front ∧ crest e q word=2^f*u ∧ Certificate u tail ∧
      (grades f tail=grades e word ∨ Less (grades f tail) (grades e word)) := by
  induction word generalizing e q with
  | nil =>
    exact ⟨[],[],q,e,rfl,empty_prefix q,rfl,rfl,cert,Or.inl rfl⟩
  | cons a word ih =>
    obtain ⟨apos,u,edge,uc⟩ := (certificate_cons_iff q a word).mp cert
    have value := successor_value edge
    by_cases left : crest (max e (a-1)) u word≤2^e*q
    · refine ⟨[],a::word,q,e,rfl,empty_prefix q,rfl,?_,cert,Or.inl rfl⟩
      simp only [crest,value,Nat.max_eq_left left]
    · obtain ⟨front,tail,v,f,split,path,run,attained,vc,rank⟩ :=
        ih (e := max e (a-1)) (by have h:=Nat.le_max_left e (a-1); omega) uc
      have drop := boosted_step_rank e a word positive
      have rank' : Less (grades f tail) (grades e (a::word)) := by
        rcases rank with same | below
        · rw [same]; exact drop
        · exact less_trans below drop
      refine ⟨a::front,tail,v,f,by simp [split],?_,run,?_,vc,Or.inr rank'⟩
      · exact (prefix_cons_iff q a v front).mpr ⟨apos,u,edge,path⟩
      · simp only [crest,value,Nat.max_eq_right (by omega : 2^e*q≤crest (max e (a-1)) u word)]
        exact attained

private theorem half_rank (e : Nat) (word : List Nat) (positive : 1≤e) :
    Less (grades (e-1) word) (grades e word) := by
  have result := grades_even_decrease (e-1) word
  simpa only [show e-1+1=e by omega] using result

/-- Every envelope value is an attained, strictly lower complete source rank. -/
theorem envelope_witness {e q : Nat} {word : List Nat}
    (positive : 1≤e) (cert : Certificate q word) :
    ∃ front tail u f, word=front++tail ∧ Prefix q front u ∧
      envelope e q word=2^f*u ∧ Certificate u tail ∧
      Less (grades f tail) (grades e word) := by
  cases word with
  | nil =>
    exact ⟨[],[],q,e-1,rfl,empty_prefix q,rfl,cert,half_rank e [] positive⟩
  | cons a word =>
    obtain ⟨apos,u,edge,uc⟩ := (certificate_cons_iff q a word).mp cert
    have value := successor_value edge
    by_cases left : crest (max e (a-1)) u word≤2^(e-1)*q
    · refine ⟨[],a::word,q,e-1,rfl,empty_prefix q,?_,cert,
        half_rank e (a::word) positive⟩
      simp only [envelope,value,Nat.max_eq_left left]
    · obtain ⟨front,tail,v,f,split,path,_,attained,vc,rank⟩ :=
        crest_witness (e := max e (a-1)) (by have h:=Nat.le_max_left e (a-1); omega) uc
      have drop := boosted_step_rank e a word positive
      have rank' : Less (grades f tail) (grades e (a::word)) := by
        rcases rank with same | below
        · rw [same]; exact drop
        · exact less_trans below drop
      refine ⟨a::front,tail,v,f,by simp [split],?_,?_,vc,rank'⟩
      · exact (prefix_cons_iff q a v front).mpr ⟨apos,u,edge,path⟩
      · simp only [envelope,value,Nat.max_eq_right (by omega :
          2^(e-1)*q≤crest (max e (a-1)) u word)]
        exact attained

theorem envelope_half (e q : Nat) (word : List Nat) :
    2^(e-1)*q≤envelope e q word := by
  cases word with
  | nil => exact Nat.le_refl _
  | cons a word => exact Nat.le_max_left _ _

/-- Every supplied literal cut occurs in the crest with its maximal payable
even exponent. This is independent of the source/target interval at all
earlier cut points. -/
theorem crest_cut_bound {e q u : Nat} {front tail : List Nat}
    (positive : 1≤e) (cert : Certificate q (front++tail))
    (path : Prefix q front u) :
    2^(boost e front)*u≤crest e q (front++tail) := by
  induction front generalizing e q with
  | nil =>
    have eq : q=u := by simpa [Prefix,correction,total] using path.2
    simpa only [boost,List.nil_append,eq] using crest_self e q tail
  | cons a front ih =>
    obtain ⟨apos,v,edge,vc⟩ := (certificate_cons_iff q a (front++tail)).mp cert
    obtain ⟨_,z,edgez,pathz⟩ := (prefix_cons_iff q a u front).mp path
    have same : z=v := Nat.eq_of_mul_eq_mul_left (Nat.pow_pos (by decide))
      (edgez.symm.trans edge)
    subst z
    have small := ih (e := max e (a-1)) (by have h:=Nat.le_max_left e (a-1); omega) vc pathz
    simp only [List.cons_append,crest,boost,successor_value edge]
    exact Nat.le_trans small (Nat.le_max_right _ _)

theorem envelope_cut_bound {e q u : Nat} {front tail : List Nat}
    (positive : 1≤e) (nonempty : front≠[])
    (cert : Certificate q (front++tail)) (path : Prefix q front u) :
    2^(boost e front)*u≤envelope e q (front++tail) := by
  cases front with
  | nil => exact False.elim (nonempty rfl)
  | cons a front =>
    obtain ⟨_,v,edge,vc⟩ := (certificate_cons_iff q a (front++tail)).mp cert
    obtain ⟨_,z,edgez,pathz⟩ := (prefix_cons_iff q a u front).mp path
    have same : z=v := Nat.eq_of_mul_eq_mul_left (Nat.pow_pos (by decide))
      (edgez.symm.trans edge)
    subst z
    have small := crest_cut_bound (e := max e (a-1))
      (by have h:=Nat.le_max_left e (a-1); omega) vc pathz
    simp only [List.cons_append,envelope,boost,successor_value edge]
    exact Nat.le_trans small (Nat.le_max_right _ _)

/-- Exact upper bound on the initial run of every lower-ranked literal
prefix deletion. The common tail is cancelled before comparing grades. -/
theorem literal_cut_run_bound {e f : Nat} {front tail : List Nat}
    (drop : Less (grades f tail) (grades e (front++tail))) : f≤boost e front := by
  by_cases done : f≤boost e front
  · exact done
  have fpos : f≠0 := by omega
  have initial := boost_ge_initial e front
  have small : Less [2*f+1] ((if e=0 then [] else [2*e+1])++front.map (2*·)) := by
    apply (less_append_right_iff _ _ (tail.map (2*·))).mp
    simpa [grades,fpos,List.map_append,List.append_assoc] using drop
  have bound : ∀ b∈((if e=0 then [] else [2*e+1])++front.map (2*·)), b<2*f+1 := by
    intro b hb
    rcases List.mem_append.mp hb with he | hf
    · by_cases zero : e=0
      · simp [zero] at he
      · have val : b=2*e+1 := by simpa [zero] using he
        omega
    · obtain ⟨a,ha,eq⟩ := List.mem_map.mp hf
      have le := boost_ge_gap (e := e) ha
      omega
  obtain ⟨a,less,same⟩ := small
  have member := List.count_pos_iff.mp (by omega :
    0<((if e=0 then [] else [2*e+1])++front.map (2*·)).count a)
  have below := bound a member
  have equal := same (2*f+1) below
  have absent : 2*f+1∉((if e=0 then [] else [2*e+1])++front.map (2*·)) := by
    intro mem
    have no := bound (2*f+1) mem
    omega
  rw [List.count_eq_zero.mpr absent] at equal
  simp at equal

/-- The envelope is the exact supremum over all lower-ranked literal source
cuts with any new initial even exponent, not merely one chosen family. -/
theorem envelope_maximal {e f q u : Nat} {front tail : List Nat}
    (positive : 1≤e) (cert : Certificate q (front++tail))
    (path : Prefix q front u)
    (drop : Less (grades f tail) (grades e (front++tail))) :
    2^f*u≤envelope e q (front++tail) := by
  have bound := literal_cut_run_bound drop
  by_cases empty : front=[]
  · subst front
    have qu : q=u := by simpa [Prefix,correction,total] using path.2
    have below : f<e := by
      have le : f≤e := by simpa [boost] using bound
      by_cases eq : f=e
      · subst f
        exact False.elim (less_irrefl (grades e tail) (by simpa using drop))
      · omega
    have power := Nat.pow_le_pow_right (by decide : 0<2) (by omega : f≤e-1)
    have scaled := Nat.mul_le_mul_right u power
    rw [← qu] at scaled
    rw [← qu]
    exact Nat.le_trans scaled (envelope_half e q tail)
  · have power := Nat.pow_le_pow_right (by decide : 0<2) bound
    have scaled := Nat.mul_le_mul_right u power
    exact Nat.le_trans scaled (envelope_cut_bound positive empty cert path)

/-- Exact interval coverage by the entire class of strictly paid literal cuts.
The right-to-left witness is attained inside the supplied complete word. -/
theorem literal_cut_interval_iff {e q target : Nat} {word : List Nat}
    (positive : 1≤e) (cert : Certificate q word) :
    (∃ front tail u f, word=front++tail ∧ Prefix q front u ∧
      Certificate u tail ∧ Less (grades f tail) (grades e word) ∧
      target≤2*(2^f*u)+1) ↔ target≤2*envelope e q word+1 := by
  constructor
  · rintro ⟨front,tail,u,f,split,path,_,drop,height⟩
    subst word
    have bound := envelope_maximal positive cert path drop
    omega
  · intro height
    obtain ⟨front,tail,u,f,split,path,attained,uc,drop⟩ :=
      envelope_witness positive cert
    exact ⟨front,tail,u,f,split,path,uc,drop,by simpa [attained] using height⟩

theorem boost_le {e bound : Nat} {word : List Nat}
    (initial : e≤bound) (gaps : ∀a∈word, a-1≤bound) : boost e word≤bound := by
  induction word generalizing e with
  | nil => exact initial
  | cons a word ih =>
    apply ih (Nat.max_le.mpr ⟨initial,gaps a (by simp)⟩)
    intro b hb
    exact gaps b (by simp [hb])

/-- On the residual alphabet, the maximizing child keeps that same alphabet
and has initial even exponent at most three. Its suffix may be empty. -/
theorem low_envelope_witness {e q : Nat} {word : List Nat}
    (positive : 1≤e) (small : e≤3) (cert : Certificate q word)
    (bounded : ∀a∈word, a≤4) :
    ∃ front tail u f, word=front++tail ∧ Prefix q front u ∧
      envelope e q word=2^f*u ∧ Certificate u tail ∧ f≤3 ∧
      (∀a∈tail, a≤4) ∧ Less (grades f tail) (grades e word) := by
  obtain ⟨front,tail,u,f,split,path,attained,uc,drop⟩ := envelope_witness positive cert
  have bound : boost e front≤3 := by
    apply boost_le small
    intro a ha
    have h := bounded a (by rw [split]; exact List.mem_append_left tail ha)
    omega
  have paid : f≤boost e front := literal_cut_run_bound (by simpa [split] using drop)
  refine ⟨front,tail,u,f,split,path,attained,uc,by omega,?_,drop⟩
  intro a ha
  exact bounded a (by rw [split]; exact List.mem_append_right front ha)

/-- Any target in the maximal child interval is certified without requiring
it to lie in each intermediate source interval. -/
theorem envelope_interval_rule {e q target : Nat} {word : List Nat}
    (positive : 1≤e) (cert : Certificate q word)
    (targetPositive : 0<target) (height : target≤2*envelope e q word+1)
    (ih : CollatzGapComparison.Hyp Interval (grades e word)) : Basin target := by
  obtain ⟨_,tail,u,f,_,_,attained,uc,drop⟩ := envelope_witness positive cert
  exact ih (envelope e q word) target f tail ⟨targetPositive,height⟩
    ⟨u,attained,uc⟩ drop

/-- Ordinary shortcut iteration, with its physical clock retained. -/
def run (n : Nat) : Nat → Nat
  | 0 => n
  | k+1 => run (shortcut n) k

theorem run_basin (n k : Nat) : Basin (run n k) ↔ Basin n := by
  induction k generalizing n with
  | zero => exact Iff.rfl
  | succ k ih => exact (ih (shortcut n)).trans (basin_step n)

/-- Independent target and partner clocks are allowed. The partner can use
the full paid envelope, which may be strictly larger than half the source. -/
theorem envelope_merger_rule {e q target partner L R : Nat} {word : List Nat}
    (positive : 1≤e) (cert : Certificate q word)
    (partnerPositive : 0<partner) (height : partner≤2*envelope e q word+1)
    (meeting : run partner L=run target R)
    (ih : CollatzGapComparison.Hyp Interval (grades e word)) : Basin target := by
  have known := envelope_interval_rule positive cert partnerPositive height ih
  have endpoint := (run_basin partner L).mpr known
  rw [meeting] at endpoint
  exact (run_basin target R).mp endpoint

theorem envelope_target_entry_rule {e q target R : Nat} {word : List Nat}
    (positive : 1≤e) (cert : Certificate q word)
    (targetPositive : 0<run target R) (height : run target R≤2*envelope e q word+1)
    (ih : CollatzGapComparison.Hyp Interval (grades e word)) : Basin target := by
  exact (run_basin target R).mp
    (envelope_interval_rule positive cert targetPositive height ih)

/-- A finite ordinary target clock reaches the maximal paid source interval.
This is a proposition to be proved for the residual states, not an axiom. -/
def TargetHitsEnvelope (e q : Nat) (word : List Nat) (target : Nat) : Prop :=
  ∃ R, 0<run target R ∧ run target R≤2*envelope e q word+1

/-- A positive interval partner meets the target, with independent clocks. -/
def TargetMergesEnvelope (e q : Nat) (word : List Nat) (target : Nat) : Prop :=
  ∃ partner L R, 0<partner ∧ partner≤2*envelope e q word+1 ∧
    run partner L=run target R

theorem hits_implies_merges {e q target : Nat} {word : List Nat}
    (hit : TargetHitsEnvelope e q word target) :
    TargetMergesEnvelope e q word target := by
  obtain ⟨R,positive,height⟩ := hit
  exact ⟨run target R,0,R,positive,height,rfl⟩

/-- Only targets beyond both the ordinary near interval and the maximal paid
literal-cut interval need an additional merger. No bound on word length,
target clock, partner clock, or source size is imposed. -/
def LowEnvelopeMerger : Prop :=
  ∀ e q word target, Certificate q word → 1≤e → e≤3 →
    (∀a∈word, a≤4) → target%2=1 →
    2^e*q+1<target → target≤2*(2^e*q)+1 →
    2*envelope e q word+1<target → TargetMergesEnvelope e q word target

/-- The forward-entry-only version is a sufficient specialization. -/
def LowEnvelopeEntry : Prop :=
  ∀ e q word target, Certificate q word → 1≤e → e≤3 →
    (∀a∈word, a≤4) → target%2=1 →
    2^e*q+1<target → target≤2*(2^e*q)+1 →
    2*envelope e q word+1<target → TargetHitsEnvelope e q word target

theorem entry_implies_merger (entry : LowEnvelopeEntry) : LowEnvelopeMerger := by
  intro e q word target cert positive small bounded odd near upper outside
  exact hits_implies_merges
    (entry e q word target cert positive small bounded odd near upper outside)

/-- Conditional closure of precisely the published low-interval obligation.
The universal merger selector remains the explicit unproved premise. -/
theorem low_interval_of_envelope_merger (selector : LowEnvelopeMerger) :
    LowIntervalStep := by
  intro source target e word cert positive small bounded odd near upper ih
  obtain ⟨q,eq,qc⟩ := cert
  by_cases height : target≤2*envelope e q word+1
  · exact envelope_interval_rule positive qc (by omega) height ih
  · obtain ⟨partner,L,R,partnerPositive,bound,meeting⟩ :=
      selector e q word target qc positive small bounded odd
        (by simpa [eq] using near) (by simpa [eq] using upper) (by omega)
    exact envelope_merger_rule positive qc partnerPositive bound meeting ih

theorem collatz_of_envelope_merger (selector : LowEnvelopeMerger) :
    ∀n, 0<n → Basin n :=
  collatz_of_low_interval (low_interval_of_envelope_merger selector)

theorem collatz_of_envelope_entry (entry : LowEnvelopeEntry) :
    ∀n, 0<n → Basin n :=
  collatz_of_envelope_merger (entry_implies_merger entry)

theorem example_envelope : envelope 1 13 [3,4]=20 := by decide

theorem example_interval_closes
    (ih : CollatzGapComparison.Hyp Interval (grades 1 [3,4])) : Basin 31 := by
  have cert : Certificate 13 [3,4] := by
    constructor
    · intro a ha
      simp only [List.mem_cons,List.not_mem_nil,or_false] at ha
      rcases ha with h | h <;> subst a <;> decide
    · decide
  exact envelope_interval_rule (by decide) cert (by decide)
    (by rw [example_envelope]; decide) ih

end CollatzSourceEnvelope
