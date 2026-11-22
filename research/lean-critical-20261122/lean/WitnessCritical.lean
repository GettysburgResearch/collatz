import WitnessSynthesis

/-!
A total arithmetic continuation of the literal-source carry program.
The positive 3x-1 map supplies the exact reflected target word. No bounded
carry state or successful termination hypothesis is hidden in the compiler.
-/

namespace CollatzShell.WitnessCritical

open WitnessGlobal WitnessSynthesis

def minusStep (c : Nat) : Nat :=
  if c % 2 = 0 then c / 2 else (3*c-1) / 2

def minusOrbit : Nat → Nat → Nat
  | 0,c => c
  | a+1,c => minusOrbit a (minusStep c)

def minusOdds : Nat → Nat → Nat
  | 0,_ => 0
  | a+1,c => minusOdds a (minusStep c) + if c%2=0 then 0 else 1

theorem minus_step_positive {c : Nat} (hc : 0<c) : 0<minusStep c := by
  unfold minusStep
  split <;> omega

theorem minus_orbit_positive (a : Nat) {c : Nat} (hc : 0<c) :
    0<minusOrbit a c := by
  induction a generalizing c with
  | zero => exact hc
  | succ a ih => exact ih (minus_step_positive hc)

private theorem positive_step {x : Nat} (hx : 0<x) : 0<step x := by
  unfold step
  split <;> omega

private theorem positive_orbit (a : Nat) {x : Nat} (hx : 0<x) :
    0<orbit a x := by
  induction a generalizing x with
  | zero => exact hx
  | succ a ih => exact ih (positive_step hx)

private theorem reflected_even {x c q : Nat} (_hc : 0<c)
    (pair : x+c=2*q) (even : c%2=0) :
    step x + minusStep c=q := by
  have xeven : x%2=0 := by omega
  simp only [step,minusStep,xeven,even,ite_true]
  omega

private theorem reflected_odd {x c q : Nat} (hc : 0<c)
    (pair : x+c=2*q) (odd : c%2≠0) :
    step x + minusStep c=3*q := by
  have xodd : x%2≠0 := by omega
  simp only [step,minusStep,ite_eq_right odd,ite_eq_right xodd]
  omega

/-- Every finite 3x-1 word is the exact reflected ordinary Collatz word on
the opposite side of a sufficiently large binary multiple. -/
theorem reflected_prefix (a : Nat) {x c q : Nat} (hx : 0<x) (hc : 0<c)
    (pair : x+c=2^a*q) :
    orbit a x + minusOrbit a c=3^(minusOdds a c)*q := by
  induction a generalizing x c q with
  | zero => simpa [orbit,minusOrbit,minusOdds] using pair
  | succ a ih =>
    have split : x+c=2*(2^a*q) := by simpa [pow_succ,mul_assoc,mul_comm,mul_left_comm] using pair
    by_cases even : c%2=0
    · have next := reflected_even hc split even
      have inducted := ih (positive_step hx) (minus_step_positive hc) next
      simpa only [orbit,minusOrbit,minusOdds,even,ite_true,Nat.add_zero] using inducted
    · have next := reflected_odd hc split even
      have next' : step x+minusStep c=2^a*(3*q) := by nlinarith [next]
      have inducted := ih (positive_step hx) (minus_step_positive hc) next'
      simpa only [orbit,minusOrbit,minusOdds,ite_eq_right even,pow_succ,mul_assoc] using inducted

def debtNext (a p c : Nat) : Nat := minusOrbit a (c+3^(p-1))

def exponentNext (a p c : Nat) : Nat := p-1+minusOdds a (c+3^(p-1))

/-- A complete arithmetic transition for every positive source gap and every
positive debt. The new exponent may be zero, which is a successful exit. -/
theorem carry_gap_transport {r u a p c x : Nat}
    (hp : 0<p) (hc : 0<c) (hx : 0<x)
    (gap : 3*r+1=2^a*u) (carry : x+c=3^p*r) :
    0<debtNext a p c ∧
    orbit a x+debtNext a p c=3^(exponentNext a p c)*u := by
  have power : 3^p=3^(p-1)*3 := by
    simpa only [show p-1+1=p by omega] using pow_succ (3:Nat) (p-1)
  have pair : x+(c+3^(p-1))=2^a*(3^(p-1)*u) := by
    calc
      x+(c+3^(p-1))=3^(p-1)*(3*r+1) := by rw [power] at carry; nlinarith [carry]
      _ =3^(p-1)*(2^a*u) := by rw [gap]
      _ =2^a*(3^(p-1)*u) := by ring
  have reflected := reflected_prefix a hx (by positivity : 0<c+3^(p-1)) pair
  refine ⟨minus_orbit_positive a (by positivity),?_⟩
  dsimp only [debtNext,exponentNext]
  rw [pow_add]
  nlinarith [reflected]

/-- A zero ternary exponent is a literal smaller-endpoint exit, not a claim
that the exponent decreases at every source edge. -/
theorem zero_exponent_exit {x c r : Nat} (hc : 0<c)
    (carry : x+c=3^0*r) : x<r := by
  norm_num at carry
  omega

/-- The terminal source one retains the exact positive Collatz map under
one ordinary source-cycle padding letter. -/
theorem terminal_padding_transport {p c x : Nat}
    (hp : 0<p) (hc : 0<c) (hx : 0<x) (carry : x+c=3^p) :
    0<debtNext 2 p c ∧ 0<exponentNext 2 p c ∧
    orbit 2 x+debtNext 2 p c=3^(exponentNext 2 p c) := by
  have trans := carry_gap_transport (r:=1) (u:=1) (a:=2) hp hc hx
    (by decide) (by simpa using carry)
  have pos := positive_orbit 2 hx
  have eq : orbit 2 x+debtNext 2 p c=3^(exponentNext 2 p c) := by simpa using trans.2
  refine ⟨trans.1,?_,eq⟩
  by_contra fail
  have zero : exponentNext 2 p c=0 := by omega
  rw [zero] at eq
  norm_num at eq
  omega

/-- Every positive ordinary target has a terminal-source debt representation.
The terminal program therefore cannot be declared harmless merely because
its supplied source is one. -/
theorem every_target_terminal_debt {x : Nat} (hx : 0<x) :
    ∃ p c, 0<p ∧ 0<c ∧ x+c=3^p := by
  have lower : x<3^x := Nat.lt_pow_self (by decide : 1<3)
  exact ⟨x,3^x-x,hx,by omega,by omega⟩

structure DebtResult where
  consumed : List Nat
  exponent : Nat
  debt : Nat

/-- A total finite computation. It stops when the exponent reaches zero, or
when the literal supplied source word is exhausted. Those two outcomes have
different mathematical meanings. -/
def compileDebt : List Nat → Nat → Nat → DebtResult
  | [],p,c => ⟨[],p,c⟩
  | a::word,p,c =>
    if p=0 then ⟨[],p,c⟩ else
    let next := compileDebt word (exponentNext a p c) (debtNext a p c)
    ⟨a::next.consumed,next.exponent,next.debt⟩

/-- The compiler consumes an actual prefix of any supplied word. Every
remaining source letter is literal, and its target endpoint is exact. -/
theorem compiler_complete {r endpoint x p c : Nat} {word : List Nat}
    (trace : GapTrace r endpoint word) (hx : 0<x) (hc : 0<c)
    (carry : x+c=3^p*r) :
    let result := compileDebt word p c
    ∃ middle tail,
      word=result.consumed++tail ∧
      GapTrace r middle result.consumed ∧ GapTrace middle endpoint tail ∧
      0<result.debt ∧
      orbit result.consumed.sum x+result.debt=3^result.exponent*middle ∧
      (result.exponent=0 ∨ tail=[]) := by
  induction word generalizing r x p c with
  | nil =>
    refine ⟨r,[],rfl,?_,trace,hc,?_,Or.inr rfl⟩
    · rfl
    · simpa only [compileDebt,List.sum_nil,orbit] using carry
  | cons a word ih =>
    by_cases zero : p=0
    · simp only [compileDebt,zero,ite_true]
      exact ⟨r,a::word,rfl,rfl,trace,hc,by simpa [zero,orbit] using carry,Or.inl trivial⟩
    · obtain ⟨ha,u,gap,rest⟩ := trace
      obtain ⟨newPositive,newCarry⟩ := carry_gap_transport (by omega : 0<p) hc hx gap carry
      obtain ⟨middle,tail,wordEq,frontTrace,tailTrace,debtPositive,meeting,finished⟩ :=
        ih rest (positive_orbit a hx) newPositive newCarry
      simp only [compileDebt,ite_eq_right zero]
      refine ⟨middle,tail,?_,?_,tailTrace,debtPositive,?_,finished⟩
      · simpa only [List.cons_append] using congrArg (List.cons a) wordEq
      · exact ⟨ha,u,gap,frontTrace⟩
      · simpa only [List.sum_cons,orbit_add] using meeting

/-- At a zero-exponent output the actual target has become smaller than the
retained source endpoint, irrespective of all intermediate debt growth. -/
theorem compiler_zero_exit {r endpoint x p c : Nat} {word : List Nat}
    (trace : GapTrace r endpoint word) (hx : 0<x) (hc : 0<c)
    (carry : x+c=3^p*r) (zero : (compileDebt word p c).exponent=0) :
    ∃ middle tail,
      word=(compileDebt word p c).consumed++tail ∧
      GapTrace middle endpoint tail ∧
      0<orbit (compileDebt word p c).consumed.sum x ∧
      orbit (compileDebt word p c).consumed.sum x<middle := by
  obtain ⟨middle,tail,wordEq,_,rest,positive,eq,_⟩ := compiler_complete trace hx hc carry
  exact ⟨middle,tail,wordEq,rest,positive_orbit _ hx,
    zero_exponent_exit positive (by simpa [zero] using eq)⟩

private theorem nonempty_maximum (front : List Nat) (nonempty : front≠[]) :
    ∃ m, m∈front ∧ ∀ a∈front, a≤m := by
  induction front with
  | nil => exact False.elim (nonempty rfl)
  | cons a front ih =>
    by_cases empty : front=[]
    · subst front
      exact ⟨a,by simp,by intro b hb; simp only [List.mem_singleton] at hb; omega⟩
    · obtain ⟨m,mem,bound⟩ := ih empty
      refine ⟨max a m,?_,?_⟩
      · rcases le_total a m with le|le
        · simpa only [max_eq_right le] using List.mem_cons_of_mem a mem
        · simp only [max_eq_left le,List.mem_cons, true_or]
      · intro b hb
        rcases List.mem_cons.mp hb with rfl|hb
        · exact le_max_left _ _
        · exact le_trans (bound b hb) (le_max_right _ _)

/-- Deleting any nonempty supplied prefix decreases the exact complete-source
grade. There is no fixed alphabet or carry-state bound in this statement. -/
theorem prefix_grade_drop (front tail : List Nat) (nonempty : front≠[]) :
    GradeDrop (sourceGrades 0 tail) (sourceGrades 0 (front++tail)) := by
  obtain ⟨m,mem,bound⟩ := nonempty_maximum front nonempty
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

/-- A successful compiler exit uses the literal retained tail in the old
well-founded source order, regardless of intermediate exponent increases. -/
theorem compiler_interval_rule {r x p c : Nat} {word : List Nat}
    (cert : GapTrace r 1 word) (hx : 0<x) (hc : 0<c)
    (carry : x+c=3^p*r)
    (consumed : (compileDebt word p c).consumed≠[])
    (zero : (compileDebt word p c).exponent=0)
    (ih : IntervalHyp (sourceGrades 0 word)) : Basin x := by
  obtain ⟨middle,tail,wordEq,rest,positive,smaller⟩ :=
    compiler_zero_exit cert hx hc carry zero
  have middlePositive : 0<middle := by omega
  have supplied : PoweredTrace middle 0 tail := ⟨middle,middlePositive,by simp,rest⟩
  have grade : GradeDrop (sourceGrades 0 tail) (sourceGrades 0 word) := by
    rw [wordEq]
    exact prefix_grade_drop _ _ consumed
  have child := ih middle (orbit (compileDebt word p c).consumed.sum x) 0 tail
    ⟨positive,by omega⟩ supplied grade
  exact (basin_at_hit (x:=x) ⟨(compileDebt word p c).consumed.sum,rfl⟩).mpr child

private theorem minus_one (a : Nat) : minusOrbit a 1=1 ∧ minusOdds a 1=a := by
  induction a with
  | zero => decide
  | succ a ih => simpa [minusOrbit,minusOdds,minusStep] using ih

/-- Initialization of the failed-half target in the positive-debt program. -/
theorem carry_initialization {r u a : Nat} (gap : 3*r+1=2^a*u) :
    orbit a (9*r+2)+1=3^(a+1)*u := by
  have pair : (9*r+2)+1=2^a*(3*u) := by nlinarith [gap]
  have trans := reflected_prefix a (by omega : 0<9*r+2) (by decide : 0<1) pair
  simpa only [(minus_one a).1,(minus_one a).2,pow_succ,mul_assoc] using trans

/-- Three exact states suffice for this enlarged successful language. In
particular the new E state accepts arbitrarily many gap twos and a gap four
that returns to D2. Other transitions remain handled by the total compiler,
but are not declared successful by this language. -/
inductive SafeDebtWord : Nat → Nat → List Nat → Prop
  | finish : SafeDebtWord 1 1 [1]
  | d1_two {word} : SafeDebtWord 1 1 word → SafeDebtWord 1 1 (2::word)
  | d1_three {word} : SafeDebtWord 2 1 word → SafeDebtWord 1 1 (3::word)
  | d2_one {word} : SafeDebtWord 1 2 word → SafeDebtWord 2 1 (1::word)
  | d2_two {word} : SafeDebtWord 1 1 word → SafeDebtWord 2 1 (2::word)
  | d2_three {word} : SafeDebtWord 2 1 word → SafeDebtWord 2 1 (3::word)
  | e_two {word} : SafeDebtWord 1 2 word → SafeDebtWord 1 2 (2::word)
  | e_three {word} : SafeDebtWord 1 1 word → SafeDebtWord 1 2 (3::word)
  | e_four {word} : SafeDebtWord 2 1 word → SafeDebtWord 1 2 (4::word)

private theorem compile_zero (tail : List Nat) (c : Nat) :
    compileDebt tail 0 c=⟨[],0,c⟩ := by
  cases tail <;> simp [compileDebt]

/-- Every word in the three-state grammar resolves the debt before touching
an arbitrary supplied suffix. This is induction over all words, with no
finite length or number-of-fours cutoff. -/
theorem safe_language_compile {p c : Nat} {word : List Nat}
    (language : SafeDebtWord p c word) (tail : List Nat) :
    compileDebt (word++tail) p c=⟨word,0,1⟩ := by
  induction language <;>
    simp_all [compileDebt,exponentNext,debtNext,minusOrbit,minusOdds,minusStep,compile_zero]

/-- The enlarged language yields actual convergence queries in the same
complete-source order, retaining the literal original tail. -/
theorem safe_carry_interval_rule {r : Nat} {word tail : List Nat}
    (cert : GapTrace r 1 ((1::word)++tail)) (language : SafeDebtWord 2 1 word)
    (ih : IntervalHyp (sourceGrades 0 ((1::word)++tail))) : Basin (9*r+2) := by
  obtain ⟨_,v,gap,rest⟩ := cert
  have initial := carry_initialization gap
  have initial' : orbit 1 (9*r+2)+1=3^2*v := by simpa using initial
  have positive : 0<orbit 1 (9*r+2) := positive_orbit 1 (by omega)
  obtain ⟨middle,remainder,wordEq,_,tailTrace,debtPositive,meeting,_⟩ :=
    compiler_complete rest positive (by decide : 0<1) initial'
  have compiled : compileDebt (word.append tail) 2 1=⟨word,0,1⟩ :=
    safe_language_compile language tail
  simp only [compiled] at wordEq debtPositive meeting
  have sameTail : tail=remainder := List.append_cancel_left wordEq
  subst remainder
  have middlePositive : 0<middle := by
    have pos := positive_orbit word.sum positive
    norm_num at meeting
    omega
  have endpointPositive := positive_orbit word.sum positive
  have supplied : PoweredTrace middle 0 tail := ⟨middle,middlePositive,by simp,tailTrace⟩
  have child := ih middle (orbit word.sum (orbit 1 (9*r+2))) 0 tail
    ⟨endpointPositive,by norm_num at meeting; omega⟩ supplied
    (prefix_grade_drop (1::word) tail (by simp))
  have first := (basin_at_hit (x:=orbit 1 (9*r+2)) ⟨word.sum,rfl⟩).mpr child
  exact (basin_at_hit (x:=9*r+2) ⟨1,rfl⟩).mpr first

/-- Every exponent has a nondecreasing terminal fixed state representing the
already absorbed positive target one. Any successful rank must first remove
the absorption set; the debt exponent itself is not a strict rank. -/
theorem terminal_one_fixed (p : Nat) (hp : 0<p) :
    debtNext 2 p (3^p-1)=3^p-1 ∧ exponentNext 2 p (3^p-1)=p := by
  let q := 3^(p-1)
  have hq : 0<q := by dsimp [q]; positivity
  have power : 3^p=3*q := by
    dsimp [q]
    simpa only [show p-1+1=p by omega,mul_comm] using pow_succ (3:Nat) (p-1)
  have start : 3^p-1+3^(p-1)=4*q-1 := by rw [power]; dsimp [q] at *; omega
  have odd : (4*q-1)%2≠0 := by omega
  have first : minusStep (4*q-1)=6*q-2 := by simp only [minusStep,ite_eq_right odd]; omega
  have even : (6*q-2)%2=0 := by omega
  have second : minusStep (6*q-2)=3*q-1 := by simp only [minusStep,even,ite_true]; omega
  simp only [debtNext,exponentNext]
  rw [start]
  norm_num only [minusOrbit,minusOdds,first,second,odd,even,ite_true,ite_false]
  rw [power]
  omega

theorem terminal_two_fixed (p : Nat) (hp : 0<p) :
    debtNext 2 p (3^p-2)=3^p-2 ∧ exponentNext 2 p (3^p-2)=p := by
  let q := 3^(p-1)
  have hq : 0<q := by dsimp [q]; positivity
  have power : 3^p=3*q := by
    dsimp [q]
    simpa only [show p-1+1=p by omega,mul_comm] using pow_succ (3:Nat) (p-1)
  have start : 3^p-2+3^(p-1)=4*q-2 := by rw [power]; dsimp [q] at *; omega
  have even : (4*q-2)%2=0 := by omega
  have first : minusStep (4*q-2)=2*q-1 := by simp only [minusStep,even,ite_true]; omega
  have odd : (2*q-1)%2≠0 := by omega
  have second : minusStep (2*q-1)=3*q-2 := by simp only [minusStep,ite_eq_right odd]; omega
  simp only [debtNext,exponentNext]
  rw [start]
  norm_num only [minusOrbit,minusOdds,first,second,odd,even,ite_true,ite_false]
  rw [power]
  omega

#print axioms minus_step_positive
#print axioms minus_orbit_positive
#print axioms reflected_prefix
#print axioms carry_gap_transport
#print axioms zero_exponent_exit
#print axioms terminal_padding_transport
#print axioms every_target_terminal_debt
#print axioms compiler_complete
#print axioms compiler_zero_exit
#print axioms prefix_grade_drop
#print axioms compiler_interval_rule
#print axioms carry_initialization
#print axioms safe_language_compile
#print axioms safe_carry_interval_rule
#print axioms terminal_one_fixed
#print axioms terminal_two_fixed

end CollatzShell.WitnessCritical
