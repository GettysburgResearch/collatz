/-
Every sufficiently large target admits a canonical root-11 source whose
entire future ordinary orbit lies below half the target. This is an exact
source-selection theorem. Successful return of an arbitrary target carry to
one of the resulting descent cones is not assumed or proved here.
-/
import Collatz.BoundedFourNormalForm

open CollatzReverseBasin CollatzClosure CollatzWitness CollatzGapMultiset
open CollatzHighGapPump CollatzBoundedFourNormalForm

set_option autoImplicit false
set_option maxHeartbeats 3000000

namespace CollatzRootedSourceFloor

def orbit (n : Nat) : Nat → Nat
  | 0 => n
  | k+1 => orbit (shortcut n) k

theorem orbit_add (n k j : Nat) : orbit n (k+j)=orbit (orbit n k) j := by
  induction k generalizing n with
  | zero => simp [orbit]
  | succ k ih => simpa [orbit,Nat.succ_add] using ih (shortcut n)

theorem orbit_pow_two (e u : Nat) : orbit (2^e*u) e=u := by
  induction e with
  | zero => simp [orbit]
  | succ e ih =>
    have form : 2^(e+1)*u=2*(2^e*u) := by rw [Nat.pow_succ]; ac_rfl
    simpa [orbit,form,shortcut] using ih

private theorem first_gap (n a u : Nat) (positive : 0<a)
    (edge : 3*n+1=2^a*u) : shortcut n=2^(a-1)*u := by
  obtain ⟨b,rfl⟩ := Nat.exists_eq_succ_of_ne_zero (by omega : a≠0)
  have identity : 3*n+1=2*(2^b*u) := by rw [edge,Nat.pow_succ]; ac_rfl
  change shortcut n=2^b*u
  unfold shortcut
  split <;> omega

theorem orbit_gap (n a u : Nat) (positive : 0<a)
    (edge : 3*n+1=2^a*u) : orbit n a=u := by
  obtain ⟨b,eq⟩ := Nat.exists_eq_succ_of_ne_zero (by omega : a≠0)
  have first := first_gap n a u positive edge
  rw [eq] at first ⊢
  simpa [orbit,first] using orbit_pow_two b u

/-- The prefix identity executes at its stated total ordinary clock. -/
theorem prefix_clock (n u : Nat) (word : List Nat) (path : Prefix n word u) :
    orbit n (total word)=u := by
  induction word generalizing n with
  | nil => simpa [total,orbit,correction] using path.2
  | cons a word ih =>
    obtain ⟨positive,q,edge,rest⟩ := (prefix_cons_iff n a u word).mp path
    simp only [total,orbit_add,orbit_gap n a q positive edge]
    exact ih q rest

/-- Every future ordinary state lies below the stated floor. -/
def Safe (n L : Nat) : Prop := ∀ k, orbit n k≤L

theorem safe_value {n L : Nat} (safe : Safe n L) : n≤L := safe 0

theorem safe_step {n L : Nat} (safe : Safe n L) : Safe (shortcut n) L :=
  fun k => safe (k+1)

theorem safe_orbit {n L : Nat} (safe : Safe n L) (k : Nat) :
    Safe (orbit n k) L := by
  intro j
  rw [←orbit_add]
  exact safe (k+j)

theorem safe_prefix {n u L : Nat} {word : List Nat}
    (safe : Safe n L) (path : Prefix n word u) : Safe u L := by
  have result := safe_orbit safe (total word)
  rwa [prefix_clock n u word path] at result

private theorem safe_prepend {n L : Nat} (value : n≤L)
    (next : Safe (shortcut n) L) : Safe n L := by
  intro k
  cases k with
  | zero => exact value
  | succ k => exact next k

theorem safe_power {u L : Nat} (safe : Safe u L) (e : Nat)
    (value : 2^e*u≤L) : Safe (2^e*u) L := by
  induction e with
  | zero => simpa using safe
  | succ e ih =>
    have form : 2^(e+1)*u=2*(2^e*u) := by rw [Nat.pow_succ]; ac_rfl
    have child : 2^e*u≤L := by rw [form] at value; omega
    apply safe_prepend value
    simpa [form,shortcut] using ih child

theorem safe_remove_power {u L : Nat} (e : Nat) (safe : Safe (2^e*u) L) :
    Safe u L := by
  have result := safe_orbit safe e
  rwa [orbit_pow_two] at result

private def seedStates : List Nat := [11,17,26,13,20,10,5,8,4,2,1]

private theorem seed_closed (n : Nat) (member : n∈seedStates) :
    shortcut n∈seedStates := by
  simp only [seedStates,List.mem_cons,List.not_mem_nil,or_false] at member
  rcases member with h|h|h|h|h|h|h|h|h|h|h <;> subst n <;> decide

private theorem seed_bounded (n : Nat) (member : n∈seedStates) : n≤26 := by
  simp only [seedStates,List.mem_cons,List.not_mem_nil,or_false] at member
  omega

theorem eleven_safe : Safe 11 26 := by
  have stable (n k : Nat) (member : n∈seedStates) : orbit n k∈seedStates := by
    induction k generalizing n with
    | zero => exact member
    | succ k ih => exact ih (shortcut n) (seed_closed n member)
  intro k
  exact seed_bounded _ (stable 11 k (by decide))

private theorem safe_gap (n a u L : Nat) (positive : 0<a)
    (edge : 3*n+1=2^a*u) (safe : Safe u L) (peak : 2^(a-1)*u≤L) :
    Safe n L := by
  have first := first_gap n a u positive edge
  have firstSafe : Safe (shortcut n) L := by
    rw [first]
    exact safe_power safe (a-1) peak
  have odd : n%2=1 := by
    obtain ⟨b,eq⟩ := Nat.exists_eq_succ_of_ne_zero (by omega : a≠0)
    have identity : 3*n+1=2*(2^b*u) := by rw [edge,eq,Nat.pow_succ]; ac_rfl
    omega
  have ordinary : 2*shortcut n=3*n+1 := by unfold shortcut; split <;> omega
  apply safe_prepend (by rw [←first] at peak; omega) firstSafe

/-- The first dyadic crossing of a floor doubles a value still below it. -/
theorem power_crossing (u L b : Nat) (safe : Safe u L) (above : L<2^b*u) :
    ∃ e, 1≤e ∧ e≤b ∧ L<2^e*u ∧ 2^e*u≤2*L ∧
      Safe (shortcut (2^e*u)) L := by
  induction b with
  | zero => have value := safe_value safe; simp at above; omega
  | succ b ih =>
    by_cases earlier : L<2^b*u
    · obtain ⟨e,positive,bounded,low,high,future⟩ := ih earlier
      exact ⟨e,positive,by omega,low,high,future⟩
    · have below : 2^b*u≤L := by omega
      have form : 2^(b+1)*u=2*(2^b*u) := by rw [Nat.pow_succ]; ac_rfl
      refine ⟨b+1,by omega,by omega,above,by rw [form]; omega,?_⟩
      simpa [form,shortcut] using safe_power safe b below

/-- A cut inside one literal source gap, with both exact prefix paths kept.
The endpoint is an even ordinary state of the original supplied path. -/
structure FloorCut (q L : Nat) (word : List Nat) where
  front : List Nat
  gap : Nat
  tail : List Nat
  e : Nat
  u : Nat
  split : word=front++gap::tail
  e_positive : 1≤e
  e_lt_gap : e<gap
  gap_bounded : gap≤4
  before : Prefix q (front++[gap-e]) (2^e*u)
  after : Prefix u tail 11
  above : L<2^e*u
  at_most : 2^e*u≤2*L
  future : Safe (shortcut (2^e*u)) L

theorem cut_ordinary_clock (q L : Nat) (word : List Nat) (cut : FloorCut q L word) :
    orbit q (total cut.front+(cut.gap-cut.e))=2^cut.e*cut.u := by
  simpa [total_append,total] using
    prefix_clock q (2^cut.e*cut.u) (cut.front++[cut.gap-cut.e]) cut.before

/-- The cut redistributes the one original gap between an executed prefix
and the retained even run. It neither inserts nor discards an ordinary clock. -/
theorem cut_clock_decomposition (q L : Nat) (word : List Nat)
    (cut : FloorCut q L word) :
    total word=(total cut.front+(cut.gap-cut.e))+cut.e+total cut.tail := by
  have identity := congrArg total cut.split
  rw [total_append] at identity
  simp only [total] at identity
  have paid := cut.e_lt_gap
  omega

theorem cut_future_bound (q L : Nat) (word : List Nat) (cut : FloorCut q L word)
    (k : Nat) : orbit q ((total cut.front+(cut.gap-cut.e))+(k+1))≤L := by
  rw [orbit_add,cut_ordinary_clock q L word cut]
  exact cut.future k

/-- An arbitrary supplied bounded-four prefix is either entirely below the
floor or has an exact final crossing inside a gap of that very prefix. -/
theorem safe_or_cut (q L : Nat) (word : List Nat)
    (path : Prefix q word 11) (bounded : ∀ a∈word, a≤4) (seed : 26≤L) :
    Safe q L ∨ Nonempty (FloorCut q L word) := by
  induction word generalizing q with
  | nil =>
    have endpoint : q=11 := by simpa [correction,total] using path.2
    subst q
    exact Or.inl (fun k => Nat.le_trans (eleven_safe k) seed)
  | cons a word ih =>
    obtain ⟨positive,u,edge,rest⟩ := (prefix_cons_iff q a 11 word).mp path
    have ab := bounded a (by simp)
    have wb : ∀ b∈word, b≤4 := fun b hb => bounded b (by simp [hb])
    rcases ih u rest wb with safe | cut
    · by_cases peak : L<2^(a-1)*u
      · obtain ⟨e,epos,eb,low,high,future⟩ := power_crossing u L (a-1) safe peak
        have elt : e<a := by omega
        have factor : 2^(a-e)*(2^e*u)=2^a*u := by
          rw [←Nat.mul_assoc,←Nat.pow_add]
          rw [show a-e+e=a by omega]
        have first : Prefix q [a-e] (2^e*u) := by
          refine ⟨by intro b hb; have eq := List.mem_singleton.mp hb; omega,?_⟩
          simpa [correction,total,factor] using edge
        exact Or.inr ⟨{
          front:=[], gap:=a, tail:=word, e:=e, u:=u,
          split:=rfl, e_positive:=epos, e_lt_gap:=elt, gap_bounded:=ab,
          before:=first, after:=rest, above:=low, at_most:=high, future:=future }⟩
      · exact Or.inl (safe_gap q a u L positive edge safe (by omega))
    · obtain ⟨cut⟩ := cut
      refine Or.inr ⟨{
        front:=a::cut.front, gap:=cut.gap, tail:=cut.tail, e:=cut.e, u:=cut.u,
        split:=?_, e_positive:=cut.e_positive, e_lt_gap:=cut.e_lt_gap,
        gap_bounded:=cut.gap_bounded, before:=?_, after:=cut.after,
        above:=cut.above, at_most:=cut.at_most, future:=cut.future }⟩
      · simpa [List.cons_append] using congrArg (a::·) cut.split
      · exact (prefix_cons_iff q a (2^cut.e*cut.u)
          (cut.front++[cut.gap-cut.e])).mpr ⟨positive,u,edge,cut.before⟩

/-- A cofinal rooted prefix supplies an exact cut for every floor above the
ordinary peak of the fixed 11 tail. The complete chosen path is retained. -/
theorem rooted_floor_cut (L : Nat) (seed : 26≤L) :
    ∃ q word, L<q ∧ (∀ a∈word, a≤4) ∧ Prefix q word 11 ∧
      Nonempty (FloorCut q L word) := by
  obtain ⟨q,word,large,_,bounded,path⟩ := cofinal_eleven_prefixes L
  rcases safe_or_cut q L word path bounded seed with safe | cut
  · have small := safe_value safe
    omega
  · exact ⟨q,word,large,bounded,path,cut⟩

/-- Global source selection with the canonical literal tail. Beyond 88, the
selected source cannot be a bare power of two times the endpoint 11. -/
theorem canonical_floor_source (L : Nat) (large : 88≤L) :
    ∃ source e u tail, source=2^e*u ∧ 1≤e ∧ e≤3 ∧ tail≠[] ∧
      Prefix u tail 11 ∧ (∀ a∈tail, a≤4) ∧ L<source ∧ source≤2*L ∧
      Safe (shortcut source) L ∧
      PoweredCertificate source e (tail++elevenTail) := by
  obtain ⟨q,word,_,bounded,_,⟨cut⟩⟩ := rooted_floor_cut L (by omega)
  have runSmall : cut.e≤3 := by have h:=cut.e_lt_gap; have h':=cut.gap_bounded; omega
  have tailBound : ∀ a∈cut.tail, a≤4 := by
    intro a ha
    apply bounded a
    rw [cut.split]
    simp [ha]
  have nonempty : cut.tail≠[] := by
    intro empty
    have endpoint : cut.u=11 := by
      simpa [empty,correction,total] using cut.after.2
    have powerBound : 2^cut.e≤8 :=
      Nat.pow_le_pow_right (by decide : 1≤2) runSmall
    have sourceBound : 2^cut.e*cut.u≤88 := by rw [endpoint]; omega
    have above := cut.above
    omega
  exact ⟨2^cut.e*cut.u,cut.e,cut.u,cut.tail,rfl,cut.e_positive,runSmall,
    nonempty,cut.after,tailBound,cut.above,cut.at_most,cut.future,
    ⟨cut.u,rfl,canonical_certificate cut.u cut.tail cut.after⟩⟩

/-- Every target at least 177 has a canonical source inside its comparison
interval, while the source's entire subsequent orbit stays below half of
the original target. No convergence hypothesis about the target is used. -/
theorem source_for_every_target (target : Nat) (large : 177≤target) :
    ∃ source e u tail, source=2^e*u ∧ 1≤e ∧ e≤3 ∧ tail≠[] ∧
      Prefix u tail 11 ∧ (∀ a∈tail, a≤4) ∧
      (target-1)/2<source ∧ source≤target-1 ∧ target≤2*source+1 ∧
      Safe (shortcut source) ((target-1)/2) ∧
      PoweredCertificate source e (tail++elevenTail) := by
  obtain ⟨source,e,u,tail,parent,epos,esmall,nonempty,path,bounded,lower,upper,
    future,cert⟩ := canonical_floor_source ((target-1)/2) (by omega)
  exact ⟨source,e,u,tail,parent,epos,esmall,nonempty,path,bounded,lower,
    by omega,by omega,future,cert⟩

/-- An odd floor above one cannot itself occur in a wholly bounded orbit:
its next ordinary step would exceed that floor. -/
theorem safe_strict {n L : Nat} (safe : Safe n L) (odd : L%2=1) (_large : 1<L) :
    n<L := by
  have value := safe_value safe
  have next := safe_value (safe_step safe)
  by_cases lower : n<L
  · exact lower
  have same : n=L := by omega
  subst n
  have identity : 2*shortcut L=3*L+1 := by unfold shortcut; split <;> omega
  omega

theorem safe_odd_core (source e u L : Nat) (parent : source=2^e*u)
    (positive : 1≤e) (future : Safe (shortcut source) L) : Safe u L := by
  obtain ⟨b,eq⟩ := Nat.exists_eq_succ_of_ne_zero (by omega : e≠0)
  have form : source=2*(2^b*u) := by rw [parent,eq,Nat.pow_succ]; ac_rfl
  have bounded : Safe (2^b*u) L := by simpa [form,shortcut] using future
  exact safe_remove_power b bounded

/-- For a target 3 mod 4, the selected source lies in the genuine residual
strip, not at its already closed near boundary. -/
theorem residual_source_for_target (target : Nat) (large : 177≤target)
    (phase : target%4=3) :
    ∃ source e u tail, source=2^e*u ∧ 1≤e ∧ e≤3 ∧ tail≠[] ∧
      Prefix u tail 11 ∧ (∀ a∈tail, a≤4) ∧
      source+1<target ∧ target≤2*source+1 ∧
      Safe (shortcut source) ((target-1)/2) ∧
      PoweredCertificate source e (tail++elevenTail) := by
  obtain ⟨source,e,u,tail,parent,epos,esmall,nonempty,path,bounded,_,_,upper,
    future,cert⟩ := source_for_every_target target large
  have floorOdd : ((target-1)/2)%2=1 := by omega
  have strict := safe_strict future floorOdd (by omega : 1<(target-1)/2)
  obtain ⟨b,eq⟩ := Nat.exists_eq_succ_of_ne_zero (by omega : e≠0)
  have form : source=2*(2^b*u) := by rw [parent,eq,Nat.pow_succ]; ac_rfl
  have twice : 2*shortcut source=source := by simp [form,shortcut]
  refine ⟨source,e,u,tail,parent,epos,esmall,nonempty,path,bounded,?_,upper,future,cert⟩
  omega

/-- Any interval return to a source confined below an odd floor is an actual
strict decrease below twice that floor plus one. -/
theorem safe_interval_cap (source returned L : Nat) (safe : Safe source L)
    (odd : L%2=1) (large : 1<L) (cap : returned≤2*source+1) :
    returned<2*L+1 := by
  have strict := safe_strict safe odd large
  omega

/-- The wider ordinary-source cap also lies strictly below the original
target: the next source state is confined below the same odd floor. -/
theorem safe_odd_source_cap (u returned L : Nat) (safe : Safe u L)
    (sourceOdd : u%2=1) (floorOdd : L%2=1) (large : 1<L)
    (cap : returned≤3*u+2) : returned<2*L+1 := by
  have next := safe_strict (safe_step safe) floorOdd large
  have identity : 2*shortcut u=3*u+1 := by unfold shortcut; split <;> omega
  omega

/-- The original target floor survives arbitrary literal source-prefix
consumption. Every return through the odd-source cone is a strict descent
below that ORIGINAL target, not merely below a later enlarged carry. -/
theorem original_target_cap_descent (target source e u v returned : Nat)
    (front : List Nat) (parent : source=2^e*u) (epos : 1≤e)
    (large : 177≤target) (phase : target%4=3)
    (future : Safe (shortcut source) ((target-1)/2))
    (path : Prefix u front v) (odd : v%2=1) (cap : returned≤3*v+2) :
    returned<target := by
  have core := safe_odd_core source e u ((target-1)/2) parent epos future
  have endpoint := safe_prefix core path
  have result := safe_odd_source_cap v returned ((target-1)/2) endpoint odd
    (by omega) (by omega) cap
  omega

/-- Padding funded by the gap just consumed is itself an actual state of
the same confined source orbit. Every such interval capture is a strict
descent below the original target. There is no gap-size bound here. -/
theorem consumed_gap_cap_descent (target n a u e returned : Nat)
    (large : 177≤target) (phase : target%4=3)
    (safe : Safe n ((target-1)/2)) (edge : 3*n+1=2^a*u) (paid : e<a)
    (cap : returned≤2*(2^e*u)+1) : returned<target := by
  have factor : 2^(a-e)*(2^e*u)=2^a*u := by
    rw [←Nat.mul_assoc,←Nat.pow_add,show a-e+e=a by omega]
  have path : Prefix n [a-e] (2^e*u) := by
    refine ⟨by intro b hb; have eq := List.mem_singleton.mp hb; omega,?_⟩
    simpa [correction,total,factor] using edge
  have endpoint := safe_prefix safe path
  have result := safe_interval_cap (2^e*u) returned ((target-1)/2) endpoint
    (by omega) (by omega) cap
  omega

theorem orbit_positive (n k : Nat) (positive : 0<n) : 0<orbit n k := by
  induction k generalizing n with
  | zero => exact positive
  | succ k ih =>
    apply ih (shortcut n)
    unfold shortcut
    split <;> omega

/-- A concrete ordinary target prefix returning to the source cone closes
under strong induction on the ORIGINAL target value. No source rank is
required for this terminal descent. -/
theorem target_prefix_cap_closes (target source e u v returned : Nat)
    (sourceFront targetFront : List Nat) (parent : source=2^e*u) (epos : 1≤e)
    (large : 177≤target) (phase : target%4=3)
    (future : Safe (shortcut source) ((target-1)/2))
    (sourcePath : Prefix u sourceFront v) (odd : v%2=1)
    (targetPath : Prefix target targetFront returned) (cap : returned≤3*v+2)
    (prior : ∀ n, 0<n → n<target → Basin n) : Basin target := by
  have lower := original_target_cap_descent target source e u v returned sourceFront
    parent epos large phase future sourcePath odd cap
  have positive := orbit_positive target (total targetFront) (by omega : 0<target)
  rw [prefix_clock target returned targetFront targetPath] at positive
  exact (prefix_basin targetPath).mpr (prior returned positive lower)

end CollatzRootedSourceFloor
