module

public import AffineCarry
public import WitnessSynthesis

@[expose] public section

/-!
# Compositional arbitrary-debt carry and exact literal-tail capture

The imported GapTrace, sourceGrades, GradeDrop and IntervalHyp are the exact
PR180/PR185 interfaces. The carry computation below is total while its
ternary exponent is positive; exponent zero is a successful interval state.
Its arithmetic soundness does not assert that every run reaches capture.
-/

namespace CollatzShell.CarryCapture

open AffineCarry WitnessGlobal WitnessSynthesis

/-- A finite run of the arbitrary-debt arithmetic transducer. An empty input
leaves both coordinates unchanged. A nonempty input needs p>0 because p=0
has already reached the unpadded interval capture state. -/
def CarryRun (p d : Nat) : List Nat → Nat → Nat → Prop
  | [], q, e => q=p ∧ e=d
  | a::word, q, e => 0<p ∧
      CarryRun (p-1+minusOdds a (3^(p-1)+d))
        (minusOrbit a (3^(p-1)+d)) word q e

/-- Soundness at every finite length, retaining the complete debt and the
actual total ordinary clock of the supplied source prefix. -/
theorem carry_run_sound {r u n p d q e : Nat} {word : List Nat}
    (source : GapTrace r u word) (run : CarryRun p d word q e)
    (target : n+d=3^p*r) :
    orbit word.sum n+e=3^q*u := by
  induction word generalizing r n p d with
  | nil =>
    obtain ⟨rfl,rfl⟩ := run
    have eq : r=u := source
    simpa only [List.sum_nil,orbit,← eq] using target
  | cons a word ih =>
    obtain ⟨_,v,gap,rest⟩ := source
    obtain ⟨positive,run⟩ := run
    have next := gap_transport positive gap target
    simpa only [List.sum_cons,orbit_add] using ih rest run next

/-- A removed source prefix pays for an initial even padding of lower grade.
The arbitrary literal odd tail cancels exactly in the highest-changed-count
order. No newly selected convergence certificate is used. -/
theorem prefix_pays_padding (front tail : List Nat) (m e : Nat)
    (member : m∈front) (bound : ∀ a∈front, a≤m) (lower : e<m) :
    GradeDrop (sourceGrades e tail) (sourceGrades 0 (front++tail)) := by
  have positive : 0<(front.map (2*·)).count (2*m) := by
    apply List.count_pos_iff.mpr
    exact List.mem_map.mpr ⟨m,member,rfl⟩
  have neq : 2*e+1≠2*m := by omega
  refine ⟨2*m,?_,?_⟩
  · by_cases zero : e=0
    · simp only [sourceGrades,zero,ite_true,List.nil_append,List.map_append,
        List.count_append]
      omega
    · simp [sourceGrades,zero,neq,List.map_append,List.count_append]
      omega
  · intro b hb
    have absent : b∉front.map (2*·) := by
      intro bad
      obtain ⟨a,ha,eq⟩ := List.mem_map.mp bad
      have le := bound a ha
      omega
    have zeroCount : (front.map (2*·)).count b=0 := List.count_eq_zero.mpr absent
    have neqB : 2*e+1≠b := by omega
    by_cases zero : e=0
    · simp [sourceGrades,zero,List.map_append,List.count_append,zeroCount]
    · simp [sourceGrades,zero,List.map_append,List.count_append,zeroCount,neqB]

/-- The whole finite transducer plugs directly into the existing common
source-certificate induction. The coefficient budget is the displayed
capture guard; it is not inferred from arithmetic soundness alone. -/
theorem arbitrary_debt_interval_rule {r n p d q f : Nat} (front tail : List Nat)
    (source : GapTrace r 1 (front++tail)) (positive : 0<n)
    (run : CarryRun p d front q f) (target : n+d=3^p*r)
    (m e : Nat) (member : m∈front) (bound : ∀ a∈front, a≤m)
    (lower : e<m) (budget : 3^q≤2^(e+1))
    (ih : IntervalHyp (sourceGrades 0 (front++tail))) : Basin n := by
  obtain ⟨u,frontTrace,suffix⟩ := (trace_append_iff r 1 front tail).mp source
  have physical := carry_run_sound frontTrace run target
  have zpos := ordinary_orbit_positive front.sum n positive
  have active := padded_capture zpos physical budget
  have upos : 0<u := by
    by_contra bad
    have zero : u=0 := by omega
    rw [zero,mul_zero] at physical
    omega
  have cert : PoweredTrace (2^e*u) e tail := ⟨u,upos,rfl,suffix⟩
  have child := ih (2^e*u) (orbit front.sum n) e tail active cert
    (prefix_pays_padding front tail m e member bound lower)
  exact (basin_at_hit ⟨front.sum,rfl⟩).mpr child

private theorem gap_pos {r u a : Nat} (gap : 3*r+1=2^a*u) : 0<u := by
  by_contra bad
  have zero : u=0 := by omega
  rw [zero,mul_zero] at gap
  omega

private theorem small_debt_transition {r u a p : Nat}
    (gap : 3*r+1=2^a*u) (state : p=1 ∨ p=2) (allowed : a=2 ∨ a=3) :
    orbit a (3^p*r-1)+1=3^(a-1)*u := by
  have rpos : 0<r := by
    rcases allowed with rfl|rfl <;> norm_num at gap <;> omega
  have product : 0<3^p*r := by positivity
  have next := gap_transport (show 0<p by omega) gap
    (show (3^p*r-1)+1=3^p*r by omega)
  rcases state with rfl|rfl <;> rcases allowed with rfl|rfl
  all_goals norm_num [minusOrbit,minusOdds,minusStep] at next ⊢
  all_goals exact next

theorem small_debt_word {r u p : Nat} {body : List Nat}
    (positive : 0<r) (source : GapTrace r u body) (state : p=1 ∨ p=2)
    (alphabet : ∀ a∈body, a=2 ∨ a=3) :
    ∃ q, (q=1 ∨ q=2) ∧ orbit body.sum (3^p*r-1)+1=3^q*u := by
  induction body generalizing r p with
  | nil =>
    have eq : r=u := source
    have upos : 0<u := by omega
    refine ⟨p,state,?_⟩
    simp only [List.sum_nil,orbit,eq]
    have hp : 0<3^p*u := by positivity
    omega
  | cons a body ih =>
    obtain ⟨_,v,gap,rest⟩ := source
    have allowed := alphabet a (by simp)
    have next := small_debt_transition gap state allowed
    have ns : a-1=1 ∨ a-1=2 := by omega
    obtain ⟨q,qs,endpt⟩ := ih (gap_pos gap) rest ns
      (fun b hb => alphabet b (by simp [hb]))
    refine ⟨q,qs,?_⟩
    have one : orbit a (3^p*r-1)=3^(a-1)*v-1 := by omega
    rw [List.sum_cons,orbit_add,one]
    exact endpt

/-- The whole language 1 {2,3}* 2 reaches a debt-one endpoint. It need not
consume the additional final gap one required by the earlier unpadded rule. -/
theorem shorter_language_transport {r u : Nat} {body : List Nat}
    (source : GapTrace r u (1::(body++[2])))
    (alphabet : ∀ a∈body, a=2 ∨ a=3) :
    orbit (body.sum+3) (9*r+2)+1=3*u := by
  obtain ⟨_,v,first,rest⟩ := source
  obtain ⟨m,middle,_,u',last,finish⟩ :=
    (trace_append_iff v u body [2]).mp rest
  have endpoint : u'=u := finish
  subst u'
  have start : step (9*r+2)=9*v-1 := by
    norm_num at first
    unfold step
    split <;> omega
  obtain ⟨p,state,through⟩ := small_debt_word (gap_pos first) middle
    (Or.inr rfl : 2=1 ∨ 2=2) alphabet
  have throughEq : orbit body.sum (9*v-1)=3^p*m-1 := by
    norm_num at through
    omega
  have endpt := small_debt_transition last state (Or.inl rfl : 2=2 ∨ 2=3)
  have firstClock : orbit 1 (9*r+2)=9*v-1 := by simpa only [orbit] using start
  rw [show body.sum+3=1+(body.sum+2) by omega,orbit_add 1 (body.sum+2)]
  rw [firstClock,orbit_add body.sum 2,throughEq]
  simpa only [Nat.reduceSub,Nat.reducePow] using endpt

theorem shorter_language_grade (body tail : List Nat)
    (alphabet : ∀ a∈body, a=2 ∨ a=3) :
    GradeDrop (sourceGrades 1 tail)
      (sourceGrades 0 ((1::(body++[2]))++tail)) := by
  by_cases three : 3∈body
  · apply prefix_pays_padding _ tail 3 1
    · simp [three]
    · intro a ha
      simp only [List.mem_cons,List.mem_append,List.not_mem_nil,or_false] at ha
      rcases ha with h|h|h
      · omega
      · rcases alphabet a h with rfl|rfl <;> omega
      · omega
    · omega
  · apply prefix_pays_padding _ tail 2 1
    · simp
    · intro a ha
      simp only [List.mem_cons,List.mem_append,List.not_mem_nil,or_false] at ha
      rcases ha with h|h|h
      · omega
      · rcases alphabet a h with rfl|rfl
        · omega
        · exact False.elim (three h)
      · omega
    · omega

/-- A valid common-source-grade rule for the entire unbounded shorter
language. The child uses the original literal tail and one paid-for halving. -/
theorem shorter_language_interval_rule {r : Nat} (body tail : List Nat)
    (source : GapTrace r 1 ((1::(body++[2]))++tail))
    (alphabet : ∀ a∈body, a=2 ∨ a=3)
    (ih : IntervalHyp (sourceGrades 0 ((1::(body++[2]))++tail))) :
    Basin (9*r+2) := by
  obtain ⟨u,front,rest⟩ :=
    (trace_append_iff r 1 (1::(body++[2])) tail).mp source
  have physical := shorter_language_transport front alphabet
  have positive := ordinary_orbit_positive (body.sum+3) (9*r+2) (by omega)
  have upos : 0<u := by omega
  have active : Interval (2*u) (orbit (body.sum+3) (9*r+2)) := ⟨positive,by omega⟩
  have cert : PoweredTrace (2*u) 1 tail := ⟨u,upos,by norm_num,rest⟩
  have child := ih (2*u) (orbit (body.sum+3) (9*r+2)) 1 tail active cert
    (shorter_language_grade body tail alphabet)
  exact (basin_at_hit ⟨body.sum+3,rfl⟩).mpr child

end CollatzShell.CarryCapture
