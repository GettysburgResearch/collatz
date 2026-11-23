module

public import WitnessSynthesis

@[expose] public section

/-!
# A source-tail-preserving language for the failed half-erasure carry

The signed-gap transport is an actual ordinary orbit identity for every gap
size. It yields a compositional rule for the unbounded language
`1 :: body ++ [2,1]`, where every letter of `body` is two or three.
The original failed-half target `9*r+2` reaches the final source endpoint
minus one, at exactly the sum of the supplied source gaps. The complete tail
then enters PR177's same lower-grade interval induction. The remaining debt
states are not asserted to have a total successful dispatcher.
-/

namespace CollatzShell.CarryLanguage

open WitnessGlobal WitnessSynthesis

private theorem gap_endpoint_positive {r u a : Nat}
    (gap : 3*r+1=2^a*u) : 0<u := by
  by_contra fail
  have zero : u=0 := by omega
  rw [zero,mul_zero] at gap
  omega

/-- Source-gap arithmetic becomes a physical target word: b halvings followed
by a-b odd steps. The exponent conservation law is exact, not a rank claim. -/
theorem signed_gap_transport (r u a p b : Nat) (hp : 1≤p) (hb : b≤a)
    (hu : 0<u) (gap : 3*r+1=2^a*u) :
    orbit a (3^p*r+3^(p-1)-2^b)=3^(a+p-b-1)*u-1 := by
  have core : 0<3^(p-1)*u := by positivity
  have inner : 0<2^(a-b)*(3^(p-1)*u) := by positivity
  have power_three : 3^p=3^(p-1)*3 := by
    simpa only [show p-1+1=p by omega] using (pow_succ (3:Nat) (p-1))
  have power_two : 2^a=2^b*2^(a-b) := by
    simpa only [show b+(a-b)=a by omega] using (pow_add (2:Nat) b (a-b))
  have coefficient : 3^p*r+3^(p-1)=
      2^b*(2^(a-b)*(3^(p-1)*u)) := by
    calc
      3^p*r+3^(p-1)=3^(p-1)*(3*r+1) := by
        rw [power_three]
        ring
      _ =3^(p-1)*(2^a*u) := by rw [gap]
      _ =2^b*(2^(a-b)*(3^(p-1)*u)) := by
        rw [power_two]
        ring
  have factor : 3^p*r+3^(p-1)-2^b=
      2^b*(2^(a-b)*(3^(p-1)*u)-1) := by
    rw [coefficient]
    have split : 2^(a-b)*(3^(p-1)*u)=
        (2^(a-b)*(3^(p-1)*u)-1)+1 := by omega
    conv_lhs => rw [split,Nat.mul_add,mul_one,Nat.add_sub_cancel]
  calc
    orbit a (3^p*r+3^(p-1)-2^b)=
        orbit (a-b) (orbit b (3^p*r+3^(p-1)-2^b)) := by
      rw [← orbit_add]
      congr 1
      omega
    _ =orbit (a-b) (2^(a-b)*(3^(p-1)*u)-1) := by rw [factor,orbit_pad]
    _ =3^(a-b)*(3^(p-1)*u)-1 := (odd_run (a-b) (3^(p-1)*u) core).1
    _ =3^(a+p-b-1)*u-1 := by
      rw [← mul_assoc,← pow_add,show (a-b)+(p-1)=a+p-b-1 by omega]

/-- The exact first transition out of the failed short-diamond carry. -/
theorem carry_step {r u a : Nat} (gap : 3*r+1=2^a*u) :
    orbit a (9*r+2)=3^(a+1)*u-1 := by
  have result := signed_gap_transport r u a 2 0 (by decide) (by omega)
    (gap_endpoint_positive gap) gap
  have source : 3^2*r+3^(2-1)-2^0=9*r+2 := by norm_num
  simpa only [source,show a+2-0-1=a+1 by omega] using result

/-- Both debt states one and two use the same transition on source gaps two
or three. Their next debt is respectively one or two. -/
theorem small_debt_step {r u a p : Nat} (gap : 3*r+1=2^a*u)
    (state : p=1 ∨ p=2) (gapSize : a=2 ∨ a=3) :
    orbit a (3^p*r-1)=3^(a-1)*u-1 := by
  rcases state with rfl|rfl
  · have result := signed_gap_transport r u a 1 1 (by decide) (by omega)
      (gap_endpoint_positive gap) gap
    have source : 3^1*r+3^(1-1)-2^1=3^1*r-1 := by norm_num
    simpa only [source,show a+1-1-1=a-1 by omega] using result
  · have result := signed_gap_transport r u a 2 2 (by decide) (by omega)
      (gap_endpoint_positive gap) gap
    have source : 3^2*r+3^(2-1)-2^2=3^2*r-1 := by norm_num
    simpa only [source,show a+2-2-1=a-1 by omega] using result

private theorem last_debt_step {r u : Nat} (gap : 3*r+1=2^1*u) :
    orbit 1 (3^1*r-1)=u-1 := by
  have result := signed_gap_transport r u 1 1 1 (by decide) (by decide)
    (gap_endpoint_positive gap) gap
  have source : 3^1*r+3^(1-1)-2^1=3^1*r-1 := by norm_num
  rw [source] at result
  simpa only [Nat.reduceAdd,Nat.reduceSub,Nat.reducePow,one_mul] using result

/-- The two debt states are preserved over an arbitrary supplied word in
{2,3}. No word-length bound is present. -/
theorem debt_word {r u p : Nat} {body : List Nat}
    (trace : GapTrace r u body) (state : p=1 ∨ p=2)
    (alphabet : ∀ a∈body, a=2 ∨ a=3) :
    ∃ q, (q=1 ∨ q=2) ∧ orbit body.sum (3^p*r-1)=3^q*u-1 := by
  induction body generalizing r p with
  | nil =>
    have eq : r=u := trace
    exact ⟨p,state,by simp only [List.sum_nil,orbit,eq]⟩
  | cons a body ih =>
    obtain ⟨_,v,gap,rest⟩ := trace
    have allowed := alphabet a (by simp)
    have next : a-1=1 ∨ a-1=2 := by omega
    obtain ⟨q,qstate,result⟩ := ih rest next (by
      intro b hb
      exact alphabet b (by simp [hb]))
    refine ⟨q,qstate,?_⟩
    rw [List.sum_cons,orbit_add a body.sum,small_debt_step gap state allowed]
    exact result

/-- Complete physical resolution of the target path on the unbounded source
language 1 {2,3}* 2 1. It lands one below the retained source endpoint. -/
theorem carry_language_transport {r u : Nat} {body : List Nat}
    (trace : GapTrace r u (1::(body++[2,1])))
    (alphabet : ∀ a∈body, a=2 ∨ a=3) :
    orbit (body.sum+4) (9*r+2)=u-1 := by
  obtain ⟨_,v,first,rest⟩ := trace
  obtain ⟨m,middle,last⟩ := (trace_append_iff v u body [2,1]).mp rest
  obtain ⟨_,q,second,_,u',third,final⟩ := last
  have endpoint : u'=u := final
  subst u'
  obtain ⟨p,state,through⟩ := debt_word middle (Or.inr rfl : 2=1 ∨ 2=2) alphabet
  have start : orbit 1 (9*r+2)=3^2*v-1 := by
    simpa using carry_step first
  have penultimate : orbit 2 (3^p*m-1)=3^1*q-1 := by
    simpa using small_debt_step second state (Or.inl rfl : 2=2 ∨ 2=3)
  rw [show body.sum+4=1+(body.sum+3) by omega,orbit_add 1 (body.sum+3),start,
    orbit_add body.sum 3,through,orbit_add 2 1,penultimate,last_debt_step third]

private theorem bounded_prefix_grade_drop (front tail : List Nat) (m : Nat)
    (mem : m∈front) (bound : ∀ a∈front, a≤m) :
    GradeDrop (sourceGrades 0 tail) (sourceGrades 0 (front++tail)) := by
  have positive : 0<(front.map (2*·)).count (2*m) := by
    apply List.count_pos_iff.mpr
    exact List.mem_map.mpr ⟨m,mem,rfl⟩
  refine ⟨2*m,?_,?_⟩
  · simp only [sourceGrades,ite_true,List.nil_append,List.map_append,List.count_append]
    omega
  · intro b hb
    have absent : b∉front.map (2*·) := by
      intro bad
      obtain ⟨a,ha,eq⟩ := List.mem_map.mp bad
      have le := bound a ha
      omega
    have zero : (front.map (2*·)).count b=0 := List.count_eq_zero.mpr absent
    simp only [sourceGrades,ite_true,List.nil_append,List.map_append,List.count_append,zero,
      Nat.zero_add]

/-- The literal source tail is strictly lower in the exact highest-changed-
multiplicity order used by PR177 and PR180. -/
theorem language_grade_drop (body tail : List Nat)
    (alphabet : ∀ a∈body, a=2 ∨ a=3) :
    GradeDrop (sourceGrades 0 tail)
      (sourceGrades 0 ((1::(body++[2,1]))++tail)) := by
  by_cases three : 3∈body
  · apply bounded_prefix_grade_drop _ tail 3
    · simp [three]
    · intro a ha
      simp only [List.mem_cons,List.mem_append] at ha
      rcases ha with h|h|h|h|h
      · omega
      · rcases alphabet a h with rfl|rfl <;> omega
      · omega
      · omega
      · contradiction
  · apply bounded_prefix_grade_drop _ tail 2
    · simp
    · intro a ha
      simp only [List.mem_cons,List.mem_append] at ha
      rcases ha with h|h|h|h|h
      · omega
      · rcases alphabet a h with rfl|rfl
        · omega
        · exact False.elim (three h)
      · omega
      · omega
      · contradiction

private theorem orbit_positive (h n : Nat) (positive : 0<n) : 0<orbit h n := by
  induction h generalizing n with
  | zero => exact positive
  | succ h ih =>
    apply ih
    unfold step
    split <;> omega

/-- An actual one-query rule for the unresolved carry. It consumes the
supplied prefix, retains its literal complete tail, and uses exactly the
existing lower-grade interval hypothesis. It does not assume a new source
witness for an already proved target. -/
theorem carry_language_interval_rule {r : Nat} (body tail : List Nat)
    (cert : GapTrace r 1 ((1::(body++[2,1]))++tail))
    (alphabet : ∀ a∈body, a=2 ∨ a=3)
    (ih : IntervalHyp (sourceGrades 0 ((1::(body++[2,1]))++tail))) :
    Basin (9*r+2) := by
  obtain ⟨u,front,rest⟩ :=
    (trace_append_iff r 1 (1::(body++[2,1])) tail).mp cert
  have transport := carry_language_transport front alphabet
  have positive : 0<u-1 := by
    rw [← transport]
    exact orbit_positive _ _ (by omega)
  have supplied : PoweredTrace u 0 tail := ⟨u,by omega,by simp,rest⟩
  have child := ih u (u-1) 0 tail ⟨positive,by omega⟩ supplied
    (language_grade_drop body tail alphabet)
  exact (basin_at_hit (x := 9*r+2) (q := u-1) ⟨body.sum+4,transport⟩).mpr child

#print axioms signed_gap_transport
#print axioms carry_step
#print axioms small_debt_step
#print axioms debt_word
#print axioms carry_language_transport
#print axioms language_grade_drop
#print axioms carry_language_interval_rule

end CollatzShell.CarryLanguage
