/-
Arbitrary asynchronous paired-word resets of complete source certificates.

The source and target have independent ordinary clocks and unequal odd counts.
All source/target words, parent exponents, and inherited tails are unbounded.
This compiler proves every local reset satisfying its exact identities; it
does not assert coverage of every parent, and does not prove Collatz.

Foundation: PR177 at 00a611094043afeb256d6532b477c0709e8ed270.
-/
import Collatz.UnboundedGapReset

open CollatzReverseBasin CollatzClosure CollatzWitness CollatzGapMultiset
open CollatzUnboundedGapReset

set_option autoImplicit false
set_option maxHeartbeats 4000000

namespace CollatzAsynchronousReset

/-- A reset may synchronize to any initial odd run of the parent target.
The equality involving corrections is written without truncated subtraction.
The whole supplied odd source word is bounded by the removed even exponent. -/
structure Compatible (e j : Nat) (source target : List Nat) : Prop where
  even_positive : 0 < e
  parent_run : j ≤ e+1
  source_positive : PositiveGaps source
  target_positive : PositiveGaps target
  source_bound : ∀ a ∈ source, a ≤ e
  count : target.length = source.length+j
  clock : total target+e = total source+j
  correction : correction target+2^total target =
    2*3^j*correction source+3^(source.length+j)

/-- Every ordinary division in the asynchronous target word follows from the
same affine source identity and the exact two-word correction identity. -/
theorem target_identity {e j m q : Nat} {source target : List Nat}
    (pair : Compatible e j source target) (hm : 0<m)
    (identity : 3^source.length*m+correction source=2^total source*q) :
    3^target.length*(2*m-1)+correction target=
      2^total target*(3^j*2^(e+1-j)*q-1) := by
  have balance : total target+(e+1-j)=total source+1 := by
    have h := pair.clock
    have hj := pair.parent_run
    omega
  have powers : 2^total target*2^(e+1-j)=2*2^total source := by
    rw [←Nat.pow_add,balance,Nat.pow_succ]
    omega
  have restore : 3^(source.length+j)*(2*m-1)+3^(source.length+j)=
      2*3^j*(3^source.length*m) := by
    have restored : (2*m-1)+1=2*m := by omega
    calc
      3^(source.length+j)*(2*m-1)+3^(source.length+j) =
          3^(source.length+j)*((2*m-1)+1) := by grind
      _ = 3^(source.length+j)*(2*m) := by rw [restored]
      _ = _ := by rw [Nat.pow_add]; grind
  have full : 3^target.length*(2*m-1)+correction target+2^total target=
      2^total target*(3^j*2^(e+1-j)*q) := by
    calc
      3^target.length*(2*m-1)+correction target+2^total target =
          3^(source.length+j)*(2*m-1)+
            (2*3^j*correction source+3^(source.length+j)) := by
              rw [pair.count]; have hc := pair.correction; omega
      _ = 2*3^j*(3^source.length*m+correction source) := by grind
      _ = 2*3^j*(2^total source*q) := by rw [identity]
      _ = 2^total target*(3^j*2^(e+1-j)*q) := by grind
  have posPow : 0<2^total target := Nat.pow_pos (by decide)
  have endpoint : 0<3^j*2^(e+1-j)*q := by
    by_cases yes : 0<3^j*2^(e+1-j)*q
    · exact yes
    · have zero : 3^j*2^(e+1-j)*q=0 := by omega
      rw [zero,Nat.mul_zero] at full
      omega
  have final : 2^total target*(3^j*2^(e+1-j)*q-1)+2^total target=
      2^total target*(3^j*2^(e+1-j)*q) := by
    have eq : (3^j*2^(e+1-j)*q-1)+1=3^j*2^(e+1-j)*q := by omega
    calc
      _ = 2^total target*((3^j*2^(e+1-j)*q-1)+1) := by grind
      _ = _ := by rw [eq]
  omega

/-- The parent target has exactly the required initial ordinary odd run.
This uses the supplied positive ordinary odd endpoint, not a 2-adic lift. -/
theorem parent_target_component {e j q : Nat} (hj : j≤e+1) (hq : 0<q) :
    Basin (2*(2^e*q)-1) ↔ Basin (3^j*2^(e+1-j)*q-1) := by
  have scale : 2*(2^e*q)=2^j*(2^(e+1-j)*q) := by
    have exponent : j+(e+1-j)=e+1 := by omega
    calc
      _ = 2^(e+1)*q := by rw [Nat.pow_succ]; grind
      _ = (2^j*2^(e+1-j))*q := by rw [←Nat.pow_add,exponent]
      _ = _ := by grind
  have positive : 0<2^(e+1-j)*q := Nat.mul_pos (Nat.pow_pos (by decide)) hq
  have run := odd_run j (2^(e+1-j)*q) positive
  have hb := orbit_basin (2^j*(2^(e+1-j)*q)-1) j
  rw [run] at hb
  rw [scale]
  have endpoint : 3^j*(2^(e+1-j)*q)=3^j*2^(e+1-j)*q := by grind
  rw [endpoint] at hb
  exact hb.symm

/-- Compile any compatible finite source/target words into a complete
certificate splice with a strict decrease in PR177's common multiset order.
The child integer and both clocks may be larger without any fixed bound. -/
theorem whole_witness_reset {e j m q : Nat} {source target tail : List Nat}
    (pair : Compatible e j source target) (hm : 0<m)
    (identity : 3^source.length*m+correction source=2^total source*q)
    (cert : Certificate q tail) :
    PoweredCertificate m 0 (source++tail) ∧
      Less (grades 0 (source++tail)) (grades e tail) ∧
      (Basin (2*m-1) ↔ Basin (2*(2^e*q)-1)) := by
  have sourcePath := word_path_of_identity pair.source_positive identity
  have targetPath := word_path_of_identity pair.target_positive
    (target_identity pair hm identity)
  have hq : 0<q := by
    have odd := witness_odd (certificate_witness cert)
    omega
  refine ⟨⟨m,by simp,word_path_prepend_certificate sourcePath cert⟩,
    even_to_odd_replacement e source tail pair.even_positive pair.source_bound,?_⟩
  exact (word_path_basin targetPath).trans
    (parent_target_component pair.parent_run hq).symm

/-- An explicit whole-progression instance of the broad compiler. This is
one local rule; its single ternary cell is not a universal cover. -/
def exampleSource (e : Nat) : List Nat := [1,2,7,e]
def exampleTarget : List Nat := [6,1,1,2,1]

theorem example_compatible (e : Nat) (he : 7≤e) :
    Compatible e 1 (exampleSource e) exampleTarget := by
  constructor
  · omega
  · omega
  · intro a ha
    simp [exampleSource] at ha
    omega
  · intro a ha
    simp [exampleTarget] at ha
    omega
  · intro a ha
    simp [exampleSource] at ha
    omega
  · rfl
  · simp [exampleSource,exampleTarget,total]
    omega
  · simp [exampleSource,exampleTarget,correction,total]

theorem example_whole_witness {e m q : Nat} {tail : List Nat} (he : 7≤e)
    (hm : 0<m) (guard : 81*m+1093=1024*(2^e*q)) (cert : Certificate q tail) :
    PoweredCertificate m 0 (exampleSource e++tail) ∧
      Less (grades 0 (exampleSource e++tail)) (grades e tail) ∧
      (Basin (2*m-1) ↔ Basin (2*(2^e*q)-1)) := by
  apply whole_witness_reset (example_compatible e he) hm ?_ cert
  simp [exampleSource,correction,total,Nat.pow_add]
  grind

/-- A complete witness over exponents one, two, and three can represent only
one. This is an all-word statement, independent of any search bound. -/
theorem bounded_three_certificate {m : Nat} {word : List Nat}
    (cert : Certificate m word) (bound : ∀ a ∈ word, a≤3) : m=1 := by
  induction word generalizing m with
  | nil => simpa [Certificate,correction,total] using cert.2
  | cons a word ih =>
    obtain ⟨ha,u,first,tail⟩ := (certificate_cons_iff m a word).mp cert
    have last : u=1 := ih tail (by intro b hb; exact bound b (by simp [hb]))
    have small := bound a (by simp)
    have cases : a=1 ∨ a=2 ∨ a=3 := by omega
    rcases cases with eq | eq | eq <;> subst a <;> rw [last] at first <;>
      simp at first <;> omega

theorem one_two_word_endpoint {n endpoint : Nat} {word : List Nat}
    (path : WordPath n endpoint word) (initial : n=1 ∨ n=2) :
    endpoint=1 ∨ endpoint=2 := by
  induction word generalizing n with
  | nil => change n=endpoint at path; omega
  | cons a word ih =>
    obtain ⟨ha,u,first,rest⟩ := path
    obtain ⟨b,rfl⟩ := Nat.exists_eq_succ_of_ne_zero (by omega : a≠0)
    have even : 3*n+1=2*(2^b*u) := by rw [Nat.pow_succ] at first; grind
    have nOne : n=1 := by omega
    have powpos : 0<2^b := Nat.pow_pos (by decide)
    have ule : u≤2^b*u := by
      have h := Nat.mul_le_mul_right u (show 1≤2^b by omega)
      simpa using h
    have small : u=1 ∨ u=2 := by
      rw [nOne] at even
      by_cases zero : u=0
      · rw [zero,Nat.mul_zero] at even; omega
      · omega
    exact ih rest small

/-- This broad first-odd-run grammar still has a real missing base case:
the parent source eight admits no such reset, at any pair of word lengths.
The target fifteen converges; this theorem only limits the stated grammar. -/
theorem no_first_run_reset_for_eight {m j : Nat} {source target : List Nat}
    (pair : Compatible 3 j source target) (hm : 0<m)
    (identity : 3^source.length*m+correction source=2^total source) : False := by
  have cert : Certificate m source := ⟨pair.source_positive,identity⟩
  have one : m=1 := bounded_three_certificate cert pair.source_bound
  have sourceEq : 3^source.length*m+correction source=2^total source*1 := by
    simpa using identity
  have targetEq := target_identity pair hm sourceEq
  have path := word_path_of_identity pair.target_positive targetEq
  have initial : 2*m-1=1 ∨ 2*m-1=2 := by rw [one]; exact Or.inl rfl
  have endpoint := one_two_word_endpoint path initial
  have bound := pair.parent_run
  have cases : j=0 ∨ j=1 ∨ j=2 ∨ j=3 ∨ j=4 := by omega
  rcases cases with eq | eq | eq | eq | eq <;> subst j <;> simp at endpoint

/-! ## Arbitrary parent-target phases -/

/-- Extract the exact affine equation from a literal ordinary word path. -/
theorem word_path_identity {n endpoint : Nat} {word : List Nat}
    (path : WordPath n endpoint word) :
    3^word.length*n+correction word=2^total word*endpoint := by
  induction word generalizing n with
  | nil => change n=endpoint at path; simpa [correction,total] using path
  | cons a word ih =>
    obtain ⟨_,u,first,rest⟩ := path
    have tail := ih rest
    simp only [List.length_cons,correction,total,Nat.pow_succ,Nat.pow_add]
    calc
      3^word.length*3*n+(3^word.length+2^a*correction word) =
          3^word.length*(3*n+1)+2^a*correction word := by grind
      _ = 2^a*(3^word.length*u+correction word) := by rw [first]; grind
      _ = _ := by rw [tail]; grind

/-- Three-word compatibility allows an arbitrary actual parent-target phase.
The phase may cross its initial odd run, many even runs, and any finite number
of subsequent odd states. Source and both target clocks remain independent. -/
structure ThreeWordCompatible (e : Nat) (source childTarget parentTarget : List Nat) : Prop where
  even_positive : 0<e
  source_positive : PositiveGaps source
  target_positive : PositiveGaps childTarget
  source_bound : ∀ a ∈ source, a≤e
  count : childTarget.length=source.length+parentTarget.length
  clock : total childTarget+e=total source+total parentTarget
  correction :
    2^total parentTarget*correction childTarget+
      2^total childTarget*3^parentTarget.length =
    2^total parentTarget*(3^childTarget.length+
      2*3^parentTarget.length*correction source)+
      2^total childTarget*correction parentTarget

theorem three_word_target_identity {e m q endpoint : Nat}
    {source childTarget parentTarget : List Nat}
    (pair : ThreeWordCompatible e source childTarget parentTarget)
    (hm : 0<m) (hq : 0<q)
    (identity : 3^source.length*m+correction source=2^total source*q)
    (parentIdentity : 3^parentTarget.length*(2*(2^e*q)-1)+correction parentTarget=
      2^total parentTarget*endpoint) :
    3^childTarget.length*(2*m-1)+correction childTarget=
      2^total childTarget*endpoint := by
  have balance : 2^total parentTarget*2^total source=
      2^total childTarget*2^e := by
    rw [←Nat.pow_add,←Nat.pow_add]
    congr 1
    have eq := pair.clock
    omega
  have childRestore : 3^childTarget.length*(2*m-1)+3^childTarget.length=
      2*3^parentTarget.length*(3^source.length*m) := by
    have restored : (2*m-1)+1=2*m := by omega
    calc
      _ = 3^childTarget.length*((2*m-1)+1) := by grind
      _ = 3^childTarget.length*(2*m) := by rw [restored]
      _ = _ := by rw [pair.count,Nat.pow_add]; grind
  have Spositive : 0<2^e*q := Nat.mul_pos (Nat.pow_pos (by decide)) hq
  have parentRestore : 3^parentTarget.length*(2*(2^e*q)-1)+3^parentTarget.length=
      2*3^parentTarget.length*(2^e*q) := by
    have restored : (2*(2^e*q)-1)+1=2*(2^e*q) := by omega
    calc
      _ = 3^parentTarget.length*((2*(2^e*q)-1)+1) := by grind
      _ = 3^parentTarget.length*(2*(2^e*q)) := by rw [restored]
      _ = _ := by grind
  have parentLinear : 2*3^parentTarget.length*(2^e*q)+correction parentTarget=
      2^total parentTarget*endpoint+3^parentTarget.length := by omega
  have full :
      2^total parentTarget*(3^childTarget.length*(2*m-1)+correction childTarget)+
        2^total childTarget*3^parentTarget.length =
      2^total parentTarget*(2^total childTarget*endpoint)+
        2^total childTarget*3^parentTarget.length := by
    calc
      _ = 2^total parentTarget*(3^childTarget.length*(2*m-1))+
          (2^total parentTarget*correction childTarget+
            2^total childTarget*3^parentTarget.length) := by grind
      _ = 2^total parentTarget*(3^childTarget.length*(2*m-1))+
          (2^total parentTarget*(3^childTarget.length+
            2*3^parentTarget.length*correction source)+
            2^total childTarget*correction parentTarget) := by rw [pair.correction]
      _ = 2^total parentTarget*(2*3^parentTarget.length*
          (3^source.length*m+correction source))+
            2^total childTarget*correction parentTarget := by grind
      _ = 2^total parentTarget*(2*3^parentTarget.length*(2^total source*q))+
            2^total childTarget*correction parentTarget := by rw [identity]
      _ = 2^total childTarget*(2*3^parentTarget.length*(2^e*q)+
          correction parentTarget) := by grind
      _ = 2^total childTarget*(2^total parentTarget*endpoint+
          3^parentTarget.length) := by rw [parentLinear]
      _ = _ := by grind
  have scaled :
      2^total parentTarget*(3^childTarget.length*(2*m-1)+correction childTarget)=
      2^total parentTarget*(2^total childTarget*endpoint) := by omega
  exact Nat.eq_of_mul_eq_mul_left (Nat.pow_pos (by decide)) scaled

/-- Full complete-certificate compiler beyond the initial parent odd phase.
The parent-target path is an actual ordinary path supplied to this theorem;
the two affine word identities force every child source and target division. -/
theorem three_word_whole_witness {e m q endpoint : Nat}
    {source childTarget parentTarget tail : List Nat}
    (pair : ThreeWordCompatible e source childTarget parentTarget) (hm : 0<m)
    (identity : 3^source.length*m+correction source=2^total source*q)
    (parentPath : WordPath (2*(2^e*q)-1) endpoint parentTarget)
    (cert : Certificate q tail) :
    PoweredCertificate m 0 (source++tail) ∧
      Less (grades 0 (source++tail)) (grades e tail) ∧
      (Basin (2*m-1) ↔ Basin (2*(2^e*q)-1)) := by
  have hq : 0<q := by
    have odd := witness_odd (certificate_witness cert)
    omega
  have sourcePath := word_path_of_identity pair.source_positive identity
  have targetIdentity := three_word_target_identity pair hm hq identity
    (word_path_identity parentPath)
  have targetPath := word_path_of_identity pair.target_positive targetIdentity
  refine ⟨⟨m,by simp,word_path_prepend_certificate sourcePath cert⟩,
    even_to_odd_replacement e source tail pair.even_positive pair.source_bound,?_⟩
  exact (word_path_basin targetPath).trans (word_path_basin parentPath).symm

/-- A fully checked instance crossing the end of the parent's initial odd
run: two odd events take five parent clocks and four child clocks. -/
theorem beyond_first_run_compatible : ThreeWordCompatible 1 [] [2,2] [1,4] := by
  constructor
  · decide
  · intro a ha; simp at ha
  · intro a ha; simp at ha; omega
  · intro a ha; simp at ha
  · decide
  · decide
  · decide

/-- For every supplied complete certificate of q=8t+1, delete the initial
even run of source2q and retain the entire q-certificate. The target merger
passes beyond the initial parent odd run, so it is outside `Compatible`. -/
theorem beyond_first_run_whole_witness (t : Nat) (tail : List Nat)
    (cert : Certificate (8*t+1) tail) :
    PoweredCertificate (8*t+1) 0 tail ∧
      Less (grades 0 tail) (grades 1 tail) ∧
      (Basin (16*t+1) ↔ Basin (32*t+3)) := by
  have parent : WordPath (2*(2^1*(8*t+1))-1) (9*t+1) [1,4] := by
    apply word_path_of_identity
    · intro a ha; simp at ha; omega
    · simp [correction,total]
      omega
  have h := three_word_whole_witness beyond_first_run_compatible (by omega)
    (show 3^[].length*(8*t+1)+correction []=2^total []*(8*t+1) by simp [correction,total])
    parent cert
  have childEq : 2*(8*t+1)-1=16*t+1 := by omega
  have parentEq : 2*(2^1*(8*t+1))-1=32*t+3 := by omega
  simpa only [List.nil_append,childEq,parentEq] using h

#print axioms target_identity
#print axioms parent_target_component
#print axioms whole_witness_reset
#print axioms example_compatible
#print axioms example_whole_witness
#print axioms bounded_three_certificate
#print axioms no_first_run_reset_for_eight
#print axioms word_path_identity
#print axioms three_word_target_identity
#print axioms three_word_whole_witness
#print axioms beyond_first_run_compatible
#print axioms beyond_first_run_whole_witness

end CollatzAsynchronousReset
