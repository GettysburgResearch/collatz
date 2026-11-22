import CertificateBoundary

/-!
# A sharp obstruction to lower-rank resets which retain one literal suffix

For `u=729*j+7` and `q=3888*j+37`, the source `S=4*q` has first odd gap
four into `u`. Every complete child certificate with the identical supplied
suffix and strictly smaller grade multiset has source at most
`13824*j+130`. This maximum is attained. Equivalently, every such child
satisfies `9*S'+14≤8*S`.

The inserted prefix has no length bound. The proof combines the exact rank
support with ordinary inverse-edge integrality. An explicit power family
supplies unbounded fully certified instances. This is an obstruction only
to unchanged-target, unchanged-suffix source-growing resets; it does not
obstruct deeper suffix edits, unbounded target transport, or asymmetric mergers.

The final theorem also excludes every uniform bounded horizon for direct
forward transport into any lower-rank child interval, while retaining the
same suffix. The sources and targets vary with that proposed horizon. The
explicit unbounded witnesses have a large gap in the preserved suffix;
they are not an unbounded family already in the gap-at-most-four normal form.
-/

namespace CollatzShell.LiteratureCertificate

open CertificateBoundary

set_option maxHeartbeats 3000000
set_option maxRecDepth 10000
set_option exponentiation.threshold 1000

/-- An exact finite positive-gap prefix with a specified ordinary endpoint. -/
inductive OddPrefix : Nat → List Nat → Nat → Prop
  | nil (n : Nat) : OddPrefix n [] n
  | cons {n a v u : Nat} {tail : List Nat} :
      0<a → 3*n+1=2^a*v → OddPrefix v tail u → OddPrefix n (a::tail) u

private theorem prefix_nil_iff (n u : Nat) : OddPrefix n [] u ↔ n=u := by
  constructor
  · intro h; cases h; rfl
  · intro h; subst n; exact OddPrefix.nil u

private theorem prefix_cons_iff (n a u : Nat) (tail : List Nat) :
    OddPrefix n (a::tail) u ↔
      0<a ∧ ∃ v, 3*n+1=2^a*v ∧ OddPrefix v tail u := by
  constructor
  · intro h
    cases h with
    | cons positive edge rest => exact ⟨positive,_,edge,rest⟩
  · rintro ⟨positive,v,edge,rest⟩
    exact OddPrefix.cons positive edge rest

/-- A fixed complete word has only one ordinary source. -/
theorem certificate_unique {n m : Nat} {word : List Nat}
    (left : Certificate n word) (right : Certificate m word) : n=m := by
  induction word generalizing n m with
  | nil => cases left; cases right; rfl
  | cons a tail ih =>
    obtain ⟨_,u,edgeU,certU⟩ := (certificate_cons_iff n a tail).mp left
    obtain ⟨_,v,edgeV,certV⟩ := (certificate_cons_iff m a tail).mp right
    have same := ih certU certV
    rw [same] at edgeU
    omega

private theorem split_certificate (n : Nat) (front tail : List Nat)
    (cert : Certificate n (front++tail)) :
    ∃ u, OddPrefix n front u ∧ Certificate u tail := by
  induction front generalizing n with
  | nil => exact ⟨n,OddPrefix.nil n,cert⟩
  | cons a front ih =>
    obtain ⟨positive,v,edge,child⟩ :=
      (certificate_cons_iff n a (front++tail)).mp cert
    obtain ⟨u,path,rest⟩ := ih v child
    exact ⟨u,OddPrefix.cons positive edge path,rest⟩

/-- Literal suffix preservation determines the endpoint of the new prefix;
one cannot silently choose a different source for the inherited word. -/
theorem prefix_of_shared_suffix {n u : Nat} {front tail : List Nat}
    (child : Certificate n (front++tail)) (source : Certificate u tail) :
    OddPrefix n front u := by
  obtain ⟨v,path,rest⟩ := split_certificate n front tail child
  have same := certificate_unique rest source
  simpa [same] using path

private theorem grade_less_append (new old tail : List Nat) :
    GradeLess (new++tail) (old++tail) ↔ GradeLess new old := by
  simp only [GradeLess,List.count_append,Nat.add_lt_add_iff_right,
    Nat.add_right_cancel_iff]

/-- Cancelling a literal suffix leaves the two-grade front `{5,8}`. -/
theorem rank_cancel_suffix (e : Nat) (front tail : List Nat) :
    GradeLess (grades e (front++tail)) (grades 2 (4::tail)) ↔
      GradeLess (grades e front) [5,8] := by
  have child : grades e (front++tail)=grades e front++tail.map (2*·) := by
    simp [grades,List.map_append,List.append_assoc]
  have parent : grades 2 (4::tail)=[5,8]++tail.map (2*·) := by simp [grades]
  rw [child,parent]
  exact grade_less_append _ _ _

private theorem doubled_count (word : List Nat) (a : Nat) :
    (word.map (2*·)).count (2*a)=word.count a := by
  induction word with
  | nil => rfl
  | cons b word ih =>
    by_cases same : b=a
    · subst b; simp [ih]
    · have different : 2*b≠2*a := by omega
      simp [same,different,ih]

private theorem grades_even_count (e a : Nat) (word : List Nat) :
    (grades e word).count (2*a)=word.count a := by
  by_cases zero : e=0
  · simp [grades,zero,doubled_count]
  · have different : 2*e+1≠2*a := by omega
    simp [grades,zero,different,doubled_count]

private theorem mapped_grade_mem (e a : Nat) (word : List Nat)
    (mem : a∈word) : 2*a∈grades e word := by
  apply List.mem_append_right
  exact List.mem_map.mpr ⟨a,mem,rfl⟩

private theorem initial_grade_mem (e : Nat) (word : List Nat) (positive : 0<e) :
    2*e+1∈grades e word := by
  simp [grades,show e≠0 by omega]

/-- The entire rank ideal has two forms, with no word-length restriction.
Either grade eight is removed, or it is retained while grade five is removed. -/
theorem lower_rank_alphabet (e : Nat) (front : List Nat)
    (drop : GradeLess (grades e front) [5,8]) :
    (e≤3 ∧ ∀ a∈front, a≤3) ∨
      (e≤1 ∧ (∀ a∈front, a≤2 ∨ a=4) ∧ front.count 4≤1) := by
  obtain ⟨pivot,lower,same⟩ := drop
  have oldPositive : 0<([5,8] : List Nat).count pivot := by omega
  have oldMem := List.count_pos_iff.mp oldPositive
  have cases : pivot=5 ∨ pivot=8 := by simpa using oldMem
  rcases cases with rfl | rfl
  · have noFive : (grades e front).count 5=0 := by norm_num at lower; omega
    have support : ∀ b∈grades e front, b<5 ∨ b=8 := by
      intro b hb
      have countPositive := List.count_pos_iff.mpr hb
      by_cases small : b<5
      · exact Or.inl small
      by_cases equal : b=8
      · exact Or.inr equal
      have neFive : b≠5 := by intro eq; rw [eq,noFive] at countPositive; omega
      have eq := same b (by omega)
      have oldZero : ([5,8] : List Nat).count b=0 :=
        List.count_eq_zero.mpr (by simp [neFive,equal])
      rw [oldZero] at eq
      omega
    have eBound : e≤1 := by
      by_cases zero : e=0
      · omega
      have bound := support (2*e+1) (initial_grade_mem e front (by omega))
      omega
    have alphabet : ∀ a∈front, a≤2 ∨ a=4 := by
      intro a ha
      have bound := support (2*a) (mapped_grade_mem e a front ha)
      omega
    have eighth := same 8 (by decide)
    have count : front.count 4=1 := by
      rw [show 8=2*4 by rfl,grades_even_count] at eighth
      simpa using eighth
    exact Or.inr ⟨eBound,alphabet,by omega⟩
  · have noEight : (grades e front).count 8=0 := by norm_num at lower; omega
    have support : ∀ b∈grades e front, b<8 := by
      intro b hb
      have countPositive := List.count_pos_iff.mpr hb
      by_cases small : b<8
      · exact small
      have neEight : b≠8 := by intro eq; rw [eq,noEight] at countPositive; omega
      have eq := same b (by omega)
      have oldZero : ([5,8] : List Nat).count b=0 :=
        List.count_eq_zero.mpr (by simp; omega)
      rw [oldZero] at eq
      omega
    have eBound : e≤3 := by
      by_cases zero : e=0
      · omega
      have bound := support (2*e+1) (initial_grade_mem e front (by omega))
      omega
    have alphabet : ∀ a∈front, a≤3 := by
      intro a ha
      have bound := support (2*a) (mapped_grade_mem e a front ha)
      omega
    exact Or.inl ⟨eBound,alphabet⟩

/-- The lower-three inverse tree has exactly two possible nodes. The second
is divisible by three, so no further positive odd inverse edge exists. -/
theorem lower_three_prefix (j n : Nat) (word : List Nat)
    (path : OddPrefix n word (729*j+7)) (alphabet : ∀ a∈word, a≤3) :
    n=729*j+7 ∨ n=972*j+9 := by
  induction word generalizing n with
  | nil => exact Or.inl ((prefix_nil_iff n _).mp path)
  | cons a word ih =>
    obtain ⟨positive,v,edge,rest⟩ := (prefix_cons_iff n a _ word).mp path
    have aBound := alphabet a (by simp)
    have restBound : ∀ b∈word, b≤3 := fun b hb => alphabet b (by simp [hb])
    have endpoint := ih v rest restBound
    have cases : a=1 ∨ a=2 ∨ a=3 := by omega
    rcases cases with rfl | rfl | rfl <;>
      norm_num only [Nat.reducePow] at edge <;> rcases endpoint with h | h <;> omega

/-- All nodes reached when at most one gap four is permitted and every other
gap is at most two. This is an invariant, not a bounded-depth search. -/
def OneFourTree (j n : Nat) : Prop :=
  n=729*j+7 ∨ n=972*j+9 ∨ n=3888*j+37 ∨ n=5184*j+49 ∨
    n=6912*j+65 ∨ n=4608*j+43 ∨ n=6144*j+57

private theorem low_edge_closed (j n a v : Nat) (positive : 0<a) (small : a≤2)
    (edge : 3*n+1=2^a*v) (endpoint : OneFourTree j v) : OneFourTree j n := by
  have cases : a=1 ∨ a=2 := by omega
  rcases cases with rfl | rfl <;> norm_num only [Nat.reducePow] at edge <;>
    rcases endpoint with h | h | h | h | h | h | h <;>
    unfold OneFourTree <;> omega

theorem one_four_prefix (j n : Nat) (word : List Nat)
    (path : OddPrefix n word (729*j+7))
    (alphabet : ∀ a∈word, a≤2 ∨ a=4) (budget : word.count 4≤1) :
    OneFourTree j n := by
  induction word generalizing n with
  | nil =>
    have eq := (prefix_nil_iff n _).mp path
    exact Or.inl eq
  | cons a word ih =>
    obtain ⟨positive,v,edge,rest⟩ := (prefix_cons_iff n a _ word).mp path
    have aBound := alphabet a (by simp)
    have restBound : ∀ b∈word, b≤2 ∨ b=4 := fun b hb => alphabet b (by simp [hb])
    have restBudget : word.count 4≤1 := by
      by_cases eq : a=4
      · subst a; simp at budget; omega
      · simpa [eq] using budget
    rcases aBound with small | rfl
    · exact low_edge_closed j n a v positive small edge (ih v rest restBound restBudget)
    · have zero : word.count 4=0 := by simpa using budget
      have small : ∀ b∈word, b≤3 := by
        intro b hb
        rcases restBound b hb with le | eq
        · omega
        · have countPositive : 0<word.count 4 :=
            List.count_pos_iff.mpr (by simpa [eq] using hb)
          omega
      have endpoint := lower_three_prefix j v word rest small
      norm_num only [Nat.reducePow] at edge
      rcases endpoint with h | h <;> unfold OneFourTree <;> omega

/-- A sharp ordinary source ceiling for every lower-ranked child retaining
the entire supplied suffix. The child prefix length is unrestricted. -/
theorem same_tail_source_bound (j source e : Nat) (front tail : List Nat)
    (rootCert : Certificate (729*j+7) tail)
    (childCert : PoweredCertificate source e (front++tail))
    (drop : GradeLess (grades e (front++tail)) (grades 2 (4::tail))) :
    source≤13824*j+130 := by
  obtain ⟨n,shape,cert⟩ := childCert
  have path := prefix_of_shared_suffix cert rootCert
  have frontDrop := (rank_cancel_suffix e front tail).mp drop
  rcases lower_rank_alphabet e front frontDrop with low | retained
  · obtain ⟨eBound,alphabet⟩ := low
    have endpoint := lower_three_prefix j n front path alphabet
    have nBound : n≤972*j+9 := by omega
    have power : 2^e≤8 := by
      simpa using Nat.pow_le_pow_right (by decide : 0<2) eBound
    have bound := Nat.mul_le_mul power nBound
    rw [shape]
    omega
  · obtain ⟨eBound,alphabet,budget⟩ := retained
    have endpoint := one_four_prefix j n front path alphabet budget
    have nBound : n≤6912*j+65 := by unfold OneFourTree at endpoint; omega
    have power : 2^e≤2 := by
      simpa using Nat.pow_le_pow_right (by decide : 0<2) eBound
    have bound := Nat.mul_le_mul power nBound
    rw [shape]
    omega

/-- The source ceiling is attained by the concrete prefix `[2,2,4]` and
one initial halving. Thus the proportional loss is not a loose estimate. -/
theorem same_tail_bound_attained (j : Nat) (tail : List Nat)
    (rootCert : Certificate (729*j+7) tail) :
    PoweredCertificate (13824*j+130) 1 ([2,2,4]++tail) ∧
      GradeLess (grades 1 ([2,2,4]++tail)) (grades 2 (4::tail)) := by
  have qCert : Certificate (3888*j+37) (4::tail) :=
    Certificate.cons (by decide) (by norm_num; omega) rootCert
  have first : Certificate (5184*j+49) (2::4::tail) :=
    Certificate.cons (by decide) (by norm_num; omega) qCert
  have second : Certificate (6912*j+65) (2::2::4::tail) :=
    Certificate.cons (by decide) (by norm_num; omega) first
  refine ⟨⟨6912*j+65,by norm_num; omega,second⟩,?_⟩
  apply (rank_cancel_suffix 1 [2,2,4] tail).mpr
  change GradeLess [3,4,4,8] [5,8]
  apply (grade_less_append [3,4,4] [5] [8]).mpr
  refine ⟨5,by decide,?_⟩
  intro b hb
  have left : b∉([3,4,4] : List Nat) := by
    simp only [List.mem_cons,List.not_mem_nil,or_false]
    omega
  have right : b∉([5] : List Nat) := by simp; omega
  rw [List.count_eq_zero.mpr left,List.count_eq_zero.mpr right]

/-- Every same-suffix lower-rank child loses at least one ninth of the original
source, with the exact positive correction retained. -/
theorem proportional_source_loss (j source e : Nat) (front tail : List Nat)
    (rootCert : Certificate (729*j+7) tail)
    (childCert : PoweredCertificate source e (front++tail))
    (drop : GradeLess (grades e (front++tail)) (grades 2 (4::tail))) :
    9*source+14≤8*(4*(3888*j+37)) := by
  have bound := same_tail_source_bound j source e front tail rootCert childCert drop
  omega

theorem no_same_tail_source_growth (j source e : Nat) (front tail : List Nat)
    (rootCert : Certificate (729*j+7) tail)
    (childCert : PoweredCertificate source e (front++tail))
    (drop : GradeLess (grades e (front++tail)) (grades 2 (4::tail))) :
    source<4*(3888*j+37) := by
  have loss := proportional_source_loss j source e front tail rootCert childCert drop
  omega

def familyExponent (m : Nat) : Nat := 729*m+385

def familyIndex (m : Nat) : Nat := 4^(familyExponent m)/2187

private theorem family_power_mod (m : Nat) : 4^(familyExponent m)%2187=22 := by
  have period : (4:Nat)^729%2187=1 := by decide
  have offset : (4:Nat)^385%2187=22 := by decide
  have repeated : (4:Nat)^(729*m)%2187=1 := by
    rw [pow_mul,Nat.pow_mod,period]
    simp
  dsimp [familyExponent]
  rw [pow_add,Nat.mul_mod,repeated,offset]

/-- An explicit complete tail for an unbounded family in the obstructed
ordinary congruence class. No universal Collatz hypothesis is used. -/
theorem certified_family_root (m : Nat) :
    Certificate (729*familyIndex m+7) [2*familyExponent m] := by
  have residue := family_power_mod m
  have division := Nat.mod_add_div (4^(familyExponent m)) 2187
  have edge : 3*(729*familyIndex m+7)+1=4^(familyExponent m) := by
    dsimp [familyIndex]
    omega
  have power : (2:Nat)^(2*familyExponent m)=4^(familyExponent m) := by
    rw [pow_mul]
    rfl
  exact Certificate.cons (u:=1) (by dsimp [familyExponent]; omega)
    (by simpa only [Nat.mul_one,power] using edge) Certificate.terminal

theorem family_index_unbounded (m : Nat) : m<familyIndex m := by
  have small : m+1≤(4:Nat)^m := by
    have h := Nat.lt_two_pow_self (n:=m)
    have base := Nat.pow_le_pow_left (by decide : (2:Nat)≤4) m
    omega
  have pad : 4096*(4:Nat)^m≤4^(familyExponent m) := by
    calc
      4096*4^m=4^(m+6) := by rw [pow_add]; norm_num; ring
      _ ≤4^(familyExponent m) :=
        Nat.pow_le_pow_right (by decide : 0<4) (by dsimp [familyExponent]; omega)
  have enough : 2187*(m+1)≤4^(familyExponent m) := by omega
  dsimp [familyIndex]
  omega

/-- There are arbitrarily large fully certified parent sources on which every
lower-rank child retaining the same entire suffix has the sharp source loss.
This quantifies over all finite inserted prefixes and all initial even runs. -/
theorem unbounded_certified_obstruction (N : Nat) :
    ∃ j tail, N<4*(3888*j+37) ∧ Certificate (3888*j+37) (4::tail) ∧
      (∀ source e front, PoweredCertificate source e (front++tail) →
        GradeLess (grades e (front++tail)) (grades 2 (4::tail)) →
        9*source+14≤8*(4*(3888*j+37))) ∧
      PoweredCertificate (13824*j+130) 1 ([2,2,4]++tail) ∧
      GradeLess (grades 1 ([2,2,4]++tail)) (grades 2 (4::tail)) := by
  let j := familyIndex N
  let tail := [2*familyExponent N]
  have rootCert : Certificate (729*j+7) tail := certified_family_root N
  have parent : Certificate (3888*j+37) (4::tail) :=
    Certificate.cons (by decide) (by norm_num; omega) rootCert
  have large : N<j := family_index_unbounded N
  obtain ⟨attained,drop⟩ := same_tail_bound_attained j tail rootCert
  refine ⟨j,tail,by omega,parent,?_,attained,drop⟩
  intro source e front cert lower
  exact proportional_source_loss j source e front tail rootCert cert lower

/-- No fixed forward lookahead repairs the same-tail prefix-only strategy.
For every proposed horizon there is a fully certified parent and a wanted
target inside its interval, whose first `K` states lie above the interval of
every lower-ranked same-tail child. Sources and targets vary with `K`.

This concerns direct forward transport, not asymmetric common-future mergers.
The constructed preserved suffix contains a large gap. -/
theorem no_uniform_forward_lookahead (K : Nat) :
    ∃ j tail n, 2^K<j ∧ Certificate (729*j+7) tail ∧
      PoweredCertificate (4*(3888*j+37)) 2 (4::tail) ∧
      0<n ∧ n≤2*(4*(3888*j+37))+1 ∧
      (∀ source e front, PoweredCertificate source e (front++tail) →
        GradeLess (grades e (front++tail)) (grades 2 (4::tail)) →
        ∀ t≤K, 2*source+1<orbit t n) := by
  let D := 2^K
  let j := familyIndex D
  let tail := [2*familyExponent D]
  let S := 4*(3888*j+37)
  let M := 13824*j+130
  let Q := (2*S+2)/D
  let n := D*Q-1
  have Dp : 0<D := by dsimp [D]; positivity
  have large : D<j := family_index_unbounded D
  have rootCert : Certificate (729*j+7) tail := certified_family_root D
  have parent : Certificate (3888*j+37) (4::tail) :=
    Certificate.cons (by decide) (by norm_num; omega) rootCert
  have division : (2*S+2)%D+D*Q=2*S+2 := by
    simpa only [Q] using Nat.mod_add_div (2*S+2) D
  have remainder : (2*S+2)%D<D := Nat.mod_lt _ Dp
  have lowProduct : 2*M+2<D*Q := by dsimp [S,M] at *; omega
  have Qp : 0<Q := by
    apply Nat.pos_of_ne_zero
    intro zero
    rw [zero,mul_zero] at lowProduct
    omega
  have low : 2*M+1<n := by dsimp [n]; omega
  have upper : n≤2*S+1 := by dsimp [n]; omega
  have rising : ∀ t≤K, n≤orbit t n := by
    simpa only [n,D] using (odd_run K Q Qp).2
  refine ⟨j,tail,n,large,rootCert,⟨3888*j+37,by norm_num,parent⟩,
    by omega,upper,?_⟩
  intro source e front cert drop t tK
  have sourceBound := same_tail_source_bound j source e front tail rootCert cert drop
  have high := rising t tK
  change source≤M at sourceBound
  omega

end CollatzShell.LiteratureCertificate
