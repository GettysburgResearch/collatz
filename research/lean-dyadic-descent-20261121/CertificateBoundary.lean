import OffsetDescent

/-!
# A complete-certificate rewrite at the second even boundary

The source is `4*(4*p+1)` and its supplied odd certificate begins with gap
four. A predecessor of `p` with gaps at most three replaces that source by
`8*z`. The complete child certificate forces `z` odd, so the child source
is at least four larger than the original source. Every target is preserved
unchanged. The inherited certificate suffix is retained literally.

Independent exact boundary identities also give a transport of every target
at most `32*p+9` into the smaller interval at most `32*p+1` within eight
shortcut steps, when `p=1 mod 8` and `p` is nonterminal. The main complete-
certificate reset needs no such target movement because its source grows.

`GradeLess` and `grades` reproduce the two definitions in PR177 at
`a0a0d76f91b4e3846c1b1f0706cad56cb6098317`. This module uses an inductive
complete-gap certificate with its own checked ordinary-orbit semantics. It
does not import PR177 or assert that its remaining dispatcher is complete.
-/

namespace CollatzShell.CertificateBoundary

open OffsetDescent

set_option maxHeartbeats 2000000

/-- A complete supplied odd-gap word, with terminal value exactly one. -/
inductive Certificate : Nat → List Nat → Prop
  | terminal : Certificate 1 []
  | cons {n a u : Nat} {tail : List Nat} :
      0<a → 3*n+1=2^a*u → Certificate u tail → Certificate n (a::tail)

/-- The highest changed multiplicity decreases. This is the exact comparison
used by the source-pinned PR177 complete-certificate order. -/
def GradeLess (new old : List Nat) : Prop :=
  ∃ a, new.count a < old.count a ∧
    ∀ b, a<b → new.count b=old.count b

def grades (evenRun : Nat) (gaps : List Nat) : List Nat :=
  (if evenRun=0 then [] else [2*evenRun+1]) ++ gaps.map (2*·)

def PoweredCertificate (n e : Nat) (gaps : List Nat) : Prop :=
  ∃ q, n=2^e*q ∧ Certificate q gaps

theorem certificate_odd {n : Nat} {word : List Nat}
    (cert : Certificate n word) : n%2=1 := by
  cases cert with
  | terminal => rfl
  | @cons n a u tail positive edge _ =>
    obtain ⟨b,rfl⟩ := Nat.exists_eq_succ_of_ne_zero (by omega : a≠0)
    rw [pow_succ] at edge
    have parity := congrArg (fun x : Nat => x%2) edge
    simp [Nat.add_mod,Nat.mul_mod] at parity
    omega

theorem certificate_cons_iff (n a : Nat) (tail : List Nat) :
    Certificate n (a::tail) ↔
      0<a ∧ ∃ u, 3*n+1=2^a*u ∧ Certificate u tail := by
  constructor
  · intro cert
    cases cert with
    | cons positive edge child => exact ⟨positive,_,edge,child⟩
  · rintro ⟨positive,u,edge,child⟩
    exact Certificate.cons positive edge child

private theorem basin_of_endpoint {t n u : Nat} (endpoint : orbit t n=u)
    (known : Basin u) : Basin n := by
  obtain ⟨h,hit⟩ := known
  exact ⟨t+h,by rw [orbit_add,endpoint,hit]⟩

/-- The local certificate definition denotes an actual ordinary Collatz hit. -/
theorem certificate_basin {n : Nat} {word : List Nat}
    (cert : Certificate n word) : Basin n := by
  induction cert with
  | terminal => exact ⟨0,rfl⟩
  | @cons n a u tail positive edge child ih =>
    have odd := certificate_odd (Certificate.cons positive edge child)
    obtain ⟨b,rfl⟩ := Nat.exists_eq_succ_of_ne_zero (by omega : a≠0)
    have first : step n=2^b*u := by
      simp only [step,odd,show (1:Nat)≠0 by decide,ite_false]
      rw [edge,pow_succ]
      rw [show 2^b*2*u=2*(2^b*u) by ring]
      omega
    have reaches : orbit (b+1) n=u := by
      simp only [orbit,first]
      exact orbit_pad b u
    exact basin_of_endpoint reaches ih

theorem powered_certificate_basin {n e : Nat} {word : List Nat}
    (cert : PoweredCertificate n e word) : Basin n := by
  obtain ⟨q,shape,cert⟩ := cert
  exact basin_of_endpoint (t:=e) (by rw [shape,orbit_pad]) (certificate_basin cert)

/-- Removing two from the first odd gap preserves the entire supplied suffix.
The exact next odd endpoint also forces the phase used by the eight-step
boundary transport. -/
theorem sibling_certificate (p : Nat) (tail : List Nat)
    (cert : Certificate (4*p+1) (4::tail)) :
    Certificate p (2::tail) ∧ p%8=1 := by
  obtain ⟨_,u,edge,child⟩ := (certificate_cons_iff (4*p+1) 4 tail).mp cert
  have odd := certificate_odd child
  norm_num only [Nat.reducePow] at edge
  have next : 3*p+1=4*u := by omega
  exact ⟨Certificate.cons (by decide) (by simpa using next) child,by omega⟩

/-- The four inverse prefixes are exactly those in PR177's retained-even
reset, here checked directly on complete inductive certificates. -/
theorem doubling_certificate (p : Nat) (tail : List Nat)
    (cert : Certificate p tail) (unit : p%3≠0) (nonterminal : p≠1)
    (not_first_dead : p%9≠7) (not_second_dead : p%27≠19) :
    ∃ z front, 2*p≤z ∧ Certificate z (front++tail) ∧
      (∀ a∈front, a≤3) := by
  have odd := certificate_odd cert
  have positive : 0<p := by omega
  have cells : p%3=2 ∨ p%9=4 ∨ p%27=10 ∨ p%27=1 := by omega
  rcases cells with cell | cell | cell | cell
  · let z := (8*p-1)/3
    have edge : 3*z+1=8*p := by dsimp [z]; omega
    refine ⟨z,[3],?_,?_,?_⟩
    · dsimp [z]; omega
    · exact Certificate.cons (by decide) (by simpa using edge) cert
    · intro a ha
      have eq : a=3 := by simpa using ha
      omega
  · let u := (4*p-1)/3
    let z := (32*p-11)/9
    have edge1 : 3*u+1=4*p := by dsimp [u]; omega
    have edge2 : 3*z+1=8*u := by dsimp [z,u]; omega
    refine ⟨z,[3,2],?_,?_,?_⟩
    · dsimp [z]; omega
    · exact Certificate.cons (by decide) (by simpa using edge2)
        (Certificate.cons (by decide) (by simpa using edge1) cert)
    · intro a ha
      simp only [List.mem_cons,List.not_mem_nil,or_false] at ha
      omega
  · let u := (4*p-1)/3
    let v := (16*p-7)/9
    let z := (128*p-65)/27
    have edge1 : 3*u+1=4*p := by dsimp [u]; omega
    have edge2 : 3*v+1=4*u := by dsimp [v,u]; omega
    have edge3 : 3*z+1=8*v := by dsimp [z,v]; omega
    refine ⟨z,[3,2,2],?_,?_,?_⟩
    · dsimp [z]; omega
    · exact Certificate.cons (by decide) (by simpa using edge3)
        (Certificate.cons (by decide) (by simpa using edge2)
          (Certificate.cons (by decide) (by simpa using edge1) cert))
    · intro a ha
      simp only [List.mem_cons,List.not_mem_nil,or_false] at ha
      omega
  · let u := (4*p-1)/3
    let v := (16*p-7)/9
    let z := (64*p-37)/27
    have large : 28≤p := by omega
    have edge1 : 3*u+1=4*p := by dsimp [u]; omega
    have edge2 : 3*v+1=4*u := by dsimp [v,u]; omega
    have edge3 : 3*z+1=4*v := by dsimp [z,v]; omega
    refine ⟨z,[2,2,2],?_,?_,?_⟩
    · dsimp [z]; omega
    · exact Certificate.cons (by decide) (by simpa using edge3)
        (Certificate.cons (by decide) (by simpa using edge2)
          (Certificate.cons (by decide) (by simpa using edge1) cert))
    · intro a ha
      simp only [List.mem_cons,List.not_mem_nil,or_false] at ha
      omega

/-- The removed grade eight pays for grade seven, an arbitrary finite prefix
of grades at most six, and the sibling's grade four. The entire tail cancels. -/
theorem second_boundary_rank (front tail : List Nat)
    (alphabet : ∀ a∈front, a≤3) :
    GradeLess (grades 3 (front++2::tail)) (grades 2 (4::tail)) := by
  let inserted := (7::front.map (2*·)) ++ [4]
  have below : ∀ a∈inserted, a<8 := by
    intro a ha
    rcases List.mem_append.mp ha with left | right
    · rcases List.mem_cons.mp left with eq | mapped
      · omega
      · obtain ⟨b,hb,eq⟩ := List.mem_map.mp mapped
        have small := alphabet b hb
        omega
    · have eq : a=4 := by simpa using right
      omega
  have none : inserted.count 8=0 := List.count_eq_zero.mpr (by
    intro mem
    have bad := below 8 mem
    omega)
  have raw : GradeLess (inserted++tail.map (2*·)) ([5,8]++tail.map (2*·)) := by
    refine ⟨8,?_,?_⟩
    · simp only [List.count_append]
      rw [none]
      simp
    · intro b hb
      have ni : inserted.count b=0 := List.count_eq_zero.mpr (by
        intro mem
        have bad := below b mem
        omega)
      have no : ([5,8] : List Nat).count b=0 := List.count_eq_zero.mpr (by
        intro mem
        simp only [List.mem_cons,List.not_mem_nil,or_false] at mem
        omega)
      simp only [List.count_append,ni,no]
  simpa [grades,inserted,List.map_append,List.append_assoc] using raw

theorem boundary_three (p : Nat) : orbit 4 (32*p+3)=18*p+2 := by
  have h := affine_lift 4 3 (2*p)
  have count : oddCount 4 3=2 := by decide
  have endpoint : orbit 4 3=2 := by decide
  norm_num only [count,endpoint,Nat.reducePow] at h
  convert h using 1 <;> ring

theorem boundary_five (p : Nat) : orbit 2 (32*p+5)=24*p+4 := by
  have h := affine_lift 2 5 (8*p)
  have count : oddCount 2 5=1 := by decide
  have endpoint : orbit 2 5=4 := by decide
  norm_num only [count,endpoint,Nat.reducePow] at h
  convert h using 1 <;> ring

theorem boundary_nine (p : Nat) : orbit 2 (32*p+9)=24*p+7 := by
  have h := affine_lift 2 9 (8*p)
  have count : oddCount 2 9=1 := by decide
  have endpoint : orbit 2 9=7 := by decide
  norm_num only [count,endpoint,Nat.reducePow] at h
  convert h using 1 <;> ring

theorem boundary_seven (v : Nat) : orbit 8 (256*v+39)=243*v+38 := by
  have h := affine_lift 8 39 v
  have count : oddCount 8 39=5 := by decide
  have endpoint : orbit 8 39=38 := by decide
  norm_num only [count,endpoint,Nat.reducePow] at h
  exact h

/-- Every target in the full old interval reaches the guaranteed child
interval in at most eight actual shortcut steps. Time zero covers targets
which are already in the child interval. -/
theorem full_boundary_transport (p target : Nat)
    (phase : p%8=1) (nonterminal : p≠1)
    (positive : 0<target) (upper : target≤32*p+9) :
    ∃ k, k≤8 ∧ 0<orbit k target ∧ orbit k target≤32*p+1 := by
  have large : 9≤p := by omega
  by_cases inside : target≤32*p+1
  · exact ⟨0,by decide,positive,inside⟩
  by_cases even : target%2=0
  · refine ⟨1,by decide,?_,?_⟩
    all_goals simp only [orbit,step,even,ite_true]; omega
  have odd : target%2=1 := by omega
  have cases : target=32*p+3 ∨ target=32*p+5 ∨
      target=32*p+7 ∨ target=32*p+9 := by omega
  rcases cases with h | h | h | h
  · refine ⟨4,by decide,?_,?_⟩
    all_goals rw [h,boundary_three]; omega
  · refine ⟨2,by decide,?_,?_⟩
    all_goals rw [h,boundary_five]; omega
  · have shape : target=256*(p/8)+39 := by omega
    refine ⟨8,by decide,?_,?_⟩
    all_goals rw [shape,boundary_seven]; omega
  · refine ⟨2,by decide,?_,?_⟩
    all_goals rw [h,boundary_nine]; omega

/-- A constructive complete-certificate rewrite. The child source `8*z`
exceeds the original source `4*(4*p+1)` by at least four. Its entire
supplied suffix `tail` is retained literally. -/
theorem second_even_source_reset (p : Nat) (tail : List Nat)
    (cert : Certificate (4*p+1) (4::tail))
    (unit : p%3≠0) (nonterminal : p≠1)
    (not_first_dead : p%9≠7) (not_second_dead : p%27≠19) :
    ∃ z front, 4*(4*p+1)+4≤8*z ∧
      PoweredCertificate (8*z) 3 (front++2::tail) ∧
      GradeLess (grades 3 (front++2::tail)) (grades 2 (4::tail)) := by
  obtain ⟨sibling,_⟩ := sibling_certificate p tail cert
  obtain ⟨z,front,grows,child,alphabet⟩ := doubling_certificate p (2::tail)
    sibling unit nonterminal not_first_dead not_second_dead
  have odd := certificate_odd child
  exact ⟨z,front,by omega,⟨z,by norm_num,child⟩,
    second_boundary_rank front tail alphabet⟩

/-- The precise lower-rank interval hypothesis used by the local rule. -/
def LowerIntervalHyp (old : List Nat) : Prop :=
  ∀ source target e word, 0<target → target≤2*source+1 →
    PoweredCertificate source e word → GradeLess (grades e word) old → Basin target

/-- The new local dispatcher branch closes the whole original interval under
the common lower-rank induction hypothesis. Universal coverage is not assumed
or concluded. -/
theorem second_boundary_interval_rule (p target : Nat) (tail : List Nat)
    (cert : Certificate (4*p+1) (4::tail))
    (unit : p%3≠0) (nonterminal : p≠1)
    (not_first_dead : p%9≠7) (not_second_dead : p%27≠19)
    (positive : 0<target) (upper : target≤32*p+9)
    (ih : LowerIntervalHyp (grades 2 (4::tail))) : Basin target := by
  obtain ⟨z,front,growth,child,drop⟩ :=
    second_even_source_reset p tail cert unit nonterminal
      not_first_dead not_second_dead
  exact ih (8*z) target 3 (front++2::tail) positive (by omega) child drop

#print axioms certificate_basin
#print axioms powered_certificate_basin
#print axioms doubling_certificate
#print axioms second_boundary_rank
#print axioms full_boundary_transport
#print axioms second_even_source_reset
#print axioms second_boundary_interval_rule

end CollatzShell.CertificateBoundary
