/-
Unbounded source-gap multiset descent. Lean core only.

An exponent may be replaced by any finite number of strictly smaller exponents.
There is no common numerical energy base and no bound on the inserted length.
The global closing theorem still requires a complete family of sound rewrites.
-/
import Collatz.Witness
import Collatz.SourceWitness

namespace CollatzGapMultiset

/-- Compare finite exponent multisets at their highest changed exponent.
This is the strict multiset extension of the usual order on natural numbers. -/
def Less (new old : List Nat) : Prop :=
  ∃ a, new.count a < old.count a ∧
    ∀ b, a < b → new.count b = old.count b

private def Profile : Nat → Type
  | 0 => Unit
  | h+1 => Nat × Profile h

private def ProfileLess : (h : Nat) → Profile h → Profile h → Prop
  | 0 => fun _ _ => False
  | h+1 => Prod.Lex Nat.lt (ProfileLess h)

private theorem profile_wf (h : Nat) : WellFounded (ProfileLess h) := by
  induction h with
  | zero => exact ⟨fun x => Acc.intro x (by intro y bad; exact False.elim bad)⟩
  | succ h ih =>
    exact ⟨fun (a,b) => Prod.lexAccessible (Nat.lt_wfRel.wf.apply a) ih.apply b⟩

private def profile : (h : Nat) → List Nat → Profile h
  | 0, _ => ()
  | h+1, xs => (xs.count h, profile h xs)

private def Bounded (h : Nat) (xs : List Nat) : Prop := ∀ a ∈ xs, a < h

private theorem pivot_bounded {h : Nat} {new old : List Nat}
    (bound : Bounded h old) {a : Nat} (drop : new.count a < old.count a) : a < h :=
  bound a (List.count_pos_iff.mp (by omega))

private theorem less_bounded {h : Nat} {new old : List Nat}
    (bound : Bounded h old) (lt : Less new old) : Bounded h new := by
  obtain ⟨a,drop,same⟩ := lt
  have ah := pivot_bounded bound drop
  intro b hb
  by_cases hn : b < h
  · exact hn
  have eq := same b (by omega)
  have oldmem : b ∈ old := List.count_pos_iff.mp (by
    have pos := List.count_pos_iff.mpr hb
    omega)
  have := bound b oldmem
  omega

private theorem profile_less {h a : Nat} {new old : List Nat}
    (ha : a < h) (drop : new.count a < old.count a)
    (same : ∀ b, a < b → new.count b = old.count b) :
    ProfileLess h (profile h new) (profile h old) := by
  induction h with
  | zero => omega
  | succ h ih =>
    change Prod.Lex Nat.lt (ProfileLess h)
      (new.count h, profile h new) (old.count h, profile h old)
    by_cases eq : a = h
    · subst a
      exact Prod.Lex.left _ _ drop
    · have ah : a < h := by omega
      rw [same h ah]
      exact Prod.Lex.right _ (ih ah)

private theorem bounded_accessible (h : Nat) (xs : List Nat)
    (bound : Bounded h xs) : Acc Less xs := by
  have acc := (InvImage.wf (profile h) (profile_wf h)).apply xs
  induction acc with
  | intro old _ ih =>
    apply Acc.intro old
    intro new lt
    obtain ⟨a,drop,same⟩ := lt
    exact ih new (profile_less (pivot_bounded bound drop) drop same)
      (less_bounded bound ⟨a,drop,same⟩)

private def capacity : List Nat → Nat
  | [] => 0
  | a::xs => a + capacity xs + 1

private theorem capacity_bounds (xs : List Nat) : Bounded (capacity xs) xs := by
  induction xs with
  | nil => intro a ha; simp at ha
  | cons a xs ih =>
    intro b hb
    rcases List.mem_cons.mp hb with eq | mem
    · subst b; simp only [capacity]; omega
    · have := ih b mem
      simp only [capacity]
      omega

/-- The order is well founded for lists of arbitrary length and arbitrarily large
natural exponents. A parent's finite exponent bound is used only in this proof;
it is not a parameter or a restriction on the order. -/
theorem less_wellFounded : WellFounded Less :=
  ⟨fun xs => bounded_accessible (capacity xs) xs (capacity_bounds xs)⟩

theorem less_irrefl (xs : List Nat) : ¬ Less xs xs := by
  rintro ⟨a,drop,_⟩
  omega

theorem less_trans {xs ys zs : List Nat} (xy : Less xs ys) (yz : Less ys zs) :
    Less xs zs := by
  obtain ⟨a,da,sa⟩ := xy
  obtain ⟨b,db,sb⟩ := yz
  by_cases ab : a < b
  · refine ⟨b,?_,?_⟩
    · rw [sa b ab]; exact db
    · intro c hc; exact (sa c (by omega)).trans (sb c hc)
  · by_cases ba : b < a
    · refine ⟨a,?_,?_⟩
      · rw [← sb a ba]; exact da
      · intro c hc; exact (sa c hc).trans (sb c (by omega))
    · have eq : a = b := by omega
      subst b
      exact ⟨a,Nat.lt_trans da db,fun c hc => (sa c hc).trans (sb c hc)⟩

theorem less_perm {new old new' old' : List Nat}
    (hn : new.Perm new') (ho : old.Perm old') : Less new old ↔ Less new' old' := by
  simp only [Less,hn.count_eq,ho.count_eq]

/-- Any identical multiset may be cancelled, independently of its size. -/
theorem less_append_right_iff (new old tail : List Nat) :
    Less (new ++ tail) (old ++ tail) ↔ Less new old := by
  simp only [Less,List.count_append,Nat.add_lt_add_iff_right,Nat.add_right_cancel_iff]

theorem less_append_left_iff (front new old : List Nat) :
    Less (front ++ new) (front ++ old) ↔ Less new old := by
  simp only [Less,List.count_append,Nat.add_lt_add_iff_left,Nat.add_left_cancel_iff]

/-- A single exponent dominates an arbitrary finite list of smaller exponents. -/
theorem replace_one (a : Nat) (inserted : List Nat)
    (below : ∀ b ∈ inserted, b < a) : Less inserted [a] := by
  have none : inserted.count a = 0 := List.count_eq_zero.mpr (by
    intro ha; have := below a ha; omega)
  refine ⟨a,?_,?_⟩
  · simp [none]
  · intro b hb
    have ni : b ∉ inserted := by intro hi; have := below b hi; omega
    have na : b ≠ a := by omega
    rw [List.count_eq_zero.mpr ni,List.count_eq_zero.mpr (by simpa using na)]

/-- Exact arbitrary prefix insertion with the complete inherited suffix retained. -/
theorem replace_one_with_tail (a : Nat) (inserted tail : List Nat)
    (below : ∀ b ∈ inserted, b < a) : Less (inserted ++ tail) (a::tail) := by
  simpa using (less_append_right_iff inserted [a] tail).mpr (replace_one a inserted below)

private def maximum : List Nat → Nat
  | [] => 0
  | a::xs => max a (maximum xs)

private theorem le_maximum {a : Nat} {xs : List Nat} (mem : a ∈ xs) :
    a ≤ maximum xs := by
  induction xs with
  | nil => simp at mem
  | cons b xs ih =>
    rcases List.mem_cons.mp mem with eq | mem
    · subst a; exact Nat.le_max_left _ _
    · exact Nat.le_trans (ih mem) (Nat.le_max_right _ _)

private theorem maximum_mem {xs : List Nat} (nonempty : xs ≠ []) : maximum xs ∈ xs := by
  induction xs with
  | nil => contradiction
  | cons a xs ih =>
    by_cases nil : xs = []
    · subst xs; simp [maximum]
    · have mem := ih nil
      by_cases le : a ≤ maximum xs
      · simp only [maximum,Nat.max_eq_right le]; exact List.mem_cons_of_mem a mem
      · simp only [maximum,Nat.max_eq_left (by omega : maximum xs ≤ a)]
        exact List.mem_cons_self

/-- Several removed exponents may jointly dominate arbitrarily many insertions.
Different inserted exponents may use different removed dominators. -/
theorem replace_many (removed inserted : List Nat) (nonempty : removed ≠ [])
    (dominated : ∀ b ∈ inserted, ∃ a ∈ removed, b < a) : Less inserted removed := by
  let a := maximum removed
  have amem : a ∈ removed := maximum_mem nonempty
  have below : ∀ b ∈ inserted, b < a := by
    intro b hb
    obtain ⟨c,hc,bc⟩ := dominated b hb
    exact Nat.lt_of_lt_of_le bc (le_maximum hc)
  have none : inserted.count a = 0 := List.count_eq_zero.mpr (by
    intro ha; have := below a ha; omega)
  refine ⟨a,?_,?_⟩
  · have pos := List.count_pos_iff.mpr amem
    omega
  · intro b hb
    have ni : b ∉ inserted := by intro hi; have := below b hi; omega
    have nr : b ∉ removed := by intro hr; have := le_maximum hr; change b ≤ a at this; omega
    rw [List.count_eq_zero.mpr ni,List.count_eq_zero.mpr nr]

/-- Permutations and an arbitrary common remainder do not change the comparison. -/
theorem cancelled_replacement {new old common inserted removed : List Nat}
    (hn : new.Perm (common ++ inserted)) (ho : old.Perm (common ++ removed))
    (nonempty : removed ≠ [])
    (dominated : ∀ b ∈ inserted, ∃ a ∈ removed, b < a) : Less new old := by
  apply (less_perm hn ho).mpr
  exact (less_append_left_iff common inserted removed).mpr
    (replace_many removed inserted nonempty dominated)

/-- Induction consumes a whole supplied exponent word. Its length may increase
without any fixed bound in a recursive call. -/
theorem induction_on {P : List Nat → Prop} (word : List Nat)
    (step : ∀ old, (∀ new, Less new old → P new) → P old) : P word :=
  less_wellFounded.induction word step

/-! ## Initial even runs and whole source certificates -/

open CollatzReverseBasin CollatzClosure CollatzWitness CollatzDirected
open CollatzSourceWitness

/-- Initial halving runs carry an odd grade; accelerated odd gaps carry even
grades. This lets an even source run pay for arbitrarily many odd gaps of at
most the same numerical size. -/
def grades (evenRun : Nat) (gaps : List Nat) : List Nat :=
  (if evenRun = 0 then [] else [2*evenRun+1]) ++ gaps.map (2*·)

theorem odd_to_odd_replacement (a : Nat) (inserted tail : List Nat)
    (below : ∀ b ∈ inserted, b < a) :
    Less (grades 0 (inserted ++ tail)) (grades 0 (a::tail)) := by
  have mapped : ∀ b ∈ inserted.map (2*·), b < 2*a := by
    intro b hb
    obtain ⟨c,hc,eq⟩ := List.mem_map.mp hb
    have := below c hc
    omega
  have lt := replace_one_with_tail (2*a) (inserted.map (2*·))
    (tail.map (2*·)) mapped
  simpa [grades,List.map_append] using lt

/-- The high-gap substitution grammar has no depth restriction: an arbitrarily
long word over 1,2,3,4 followed by its adjusted last gap is below the one old gap.
The complete remaining source witness cancels. Only the rank is proved here;
the arithmetic source and target splice identities are separate obligations. -/
theorem unbounded_high_gap_replacement (a last : Nat) (front tail : List Nat)
    (high : 5 ≤ a) (alphabet : ∀ b ∈ front, b ≤ 4) (lastBound : last ≤ 4) :
    Less (grades 0 ((front ++ [last+(a-5)]) ++ tail)) (grades 0 (a::tail)) := by
  apply odd_to_odd_replacement
  intro b hb
  rcases List.mem_append.mp hb with before | final
  · have := alphabet b before
    omega
  · have eq : b = last+(a-5) := by simpa using final
    omega

theorem even_to_odd_replacement (e : Nat) (inserted tail : List Nat)
    (positive : 0 < e) (bounded : ∀ a ∈ inserted, a ≤ e) :
    Less (grades 0 (inserted ++ tail)) (grades e tail) := by
  have below : ∀ b ∈ inserted.map (2*·), b < 2*e+1 := by
    intro b hb
    obtain ⟨a,ha,eq⟩ := List.mem_map.mp hb
    have := bounded a ha
    omega
  have lt := replace_one_with_tail (2*e+1) (inserted.map (2*·))
    (tail.map (2*·)) below
  simpa [grades,show e ≠ 0 by omega,List.map_append] using lt

/-- The source may be even. The supplied complete odd certificate is retained,
with its initial even run represented separately. -/
def PoweredCertificate (n e : Nat) (gaps : List Nat) : Prop :=
  ∃ odd, n = 2^e*odd ∧ Certificate odd gaps

theorem powered_certificate_basin {n e : Nat} {gaps : List Nat}
    (h : PoweredCertificate n e gaps) : Basin n := by
  obtain ⟨odd,eq,cert⟩ := h
  rw [eq]
  exact (basin_pow_two e odd).mpr (witness_basin (certificate_witness cert))

theorem basin_powered_certificate {n : Nat} (h : Basin n) :
    ∃ e gaps, PoweredCertificate n e gaps := by
  obtain ⟨e,odd,eq,witness⟩ := basin_powered h
  obtain ⟨gaps,cert⟩ := witness_certificate witness
  exact ⟨e,gaps,odd,eq,cert⟩

/-- Peel the actual first exponent from the supplied identity, preserving the
specified tail rather than choosing a fresh convergence certificate. -/
theorem certificate_cons_iff (n a : Nat) (tail : List Nat) :
    Certificate n (a::tail) ↔
      0 < a ∧ ∃ m, 3*n+1 = 2^a*m ∧ Certificate m tail := by
  constructor
  · intro cert
    obtain ⟨positive,identity⟩ := cert
    have ha : 0 < a := positive a (by simp)
    have ht : PositiveGaps tail := fun b hb => positive b (by simp [hb])
    have eq : 3^tail.length*(3*n+1) + 2^a*correction tail =
        2^a*2^total tail := by
      simp only [List.length_cons,correction,total,Nat.pow_succ,Nat.pow_add] at identity
      grind
    have divides : 2^a ∣ 3^tail.length*(3*n+1) := by
      have sum : 2^a ∣ 3^tail.length*(3*n+1) + 2^a*correction tail :=
        ⟨2^total tail,eq⟩
      have rest : 2^a ∣ 2^a*correction tail := ⟨correction tail,rfl⟩
      exact (Nat.dvd_add_iff_left rest).mpr sum
    have coprime : Nat.Coprime (2^a) (3^tail.length) :=
      Nat.gcd_pow_right_of_gcd_eq_one (Nat.gcd_pow_left_of_gcd_eq_one
        (by decide : Nat.gcd 2 3 = 1))
    obtain ⟨m,step⟩ := coprime.dvd_of_dvd_mul_left divides
    have step' : 3*n+1 = 2^a*m := step
    have tailEq : 3^tail.length*m + correction tail = 2^total tail := by
      rw [step'] at eq
      have factored : 2^a*(3^tail.length*m + correction tail) = 2^a*2^total tail := by
        grind
      exact Nat.eq_of_mul_eq_mul_left (Nat.pow_pos (by decide)) factored
    exact ⟨ha,m,step',ht,tailEq⟩
  · rintro ⟨ha,m,step,positive,identity⟩
    refine ⟨?_,?_⟩
    · intro b hb
      rcases List.mem_cons.mp hb with eq | mem
      · simpa [eq] using ha
      · exact positive b mem
    · simp only [List.length_cons,correction,total,Nat.pow_succ,Nat.pow_add]
      calc
        3^tail.length*3*n + (3^tail.length + 2^a*correction tail) =
            3^tail.length*(3*n+1) + 2^a*correction tail := by grind
        _ = 2^a*(3^tail.length*m + correction tail) := by rw [step]; grind
        _ = _ := by rw [identity]

theorem grades_even_decrease (e : Nat) (tail : List Nat) :
    Less (grades e tail) (grades (e+1) tail) := by
  let inserted := if e = 0 then [] else [2*e+1]
  have below : ∀ b ∈ inserted, b < 2*(e+1)+1 := by
    intro b hb
    by_cases eq : e = 0
    · simp [inserted,eq] at hb
    · have val : b = 2*e+1 := by simpa [inserted,eq] using hb
      omega
  have lt := replace_one_with_tail (2*(e+1)+1) inserted (tail.map (2*·)) below
  simpa [grades,inserted] using lt

theorem grades_odd_decrease (e : Nat) (tail : List Nat) :
    Less (grades e tail) (grades 0 ((e+1)::tail)) := by
  let inserted := if e = 0 then [] else [2*e+1]
  have below : ∀ b ∈ inserted, b < 2*(e+1) := by
    intro b hb
    by_cases eq : e = 0
    · simp [inserted,eq] at hb
    · have val : b = 2*e+1 := by simpa [inserted,eq] using hb
      omega
  have lt := replace_one_with_tail (2*(e+1)) inserted (tail.map (2*·)) below
  simpa [grades,inserted] using lt

/-- Every ordinary shortcut step before reaching one strictly decreases the same
graded multiset used by arbitrary-length even-to-odd reset substitutions. -/
theorem ordinary_step {n e : Nat} {gaps : List Nat}
    (cert : PoweredCertificate n e gaps) (nonterminal : n ≠ 1) :
    ∃ e' gaps', PoweredCertificate (shortcut n) e' gaps' ∧
      Less (grades e' gaps') (grades e gaps) := by
  obtain ⟨odd,eq,tailCert⟩ := cert
  cases e with
  | succ e =>
    have form : n = 2*(2^e*odd) := by rw [eq,Nat.pow_succ]; grind
    have step : shortcut n = 2^e*odd := by rw [form]; simp [shortcut]
    exact ⟨e,gaps,⟨odd,step,tailCert⟩,grades_even_decrease e gaps⟩
  | zero =>
    have val : n = odd := by simpa using eq
    subst odd
    cases gaps with
    | nil =>
      have one : n = 1 := by simpa [CollatzWitness.Certificate,correction,total] using tailCert.2
      exact False.elim (nonterminal one)
    | cons a tail =>
      obtain ⟨ha,m,step,child⟩ := (certificate_cons_iff n a tail).mp tailCert
      obtain ⟨b,rfl⟩ := Nat.exists_eq_succ_of_ne_zero (by omega : a ≠ 0)
      have equation : 3*n+1 = 2*(2^b*m) := by rw [step,Nat.pow_succ]; grind
      have result : shortcut n = 2^b*m := by unfold shortcut; split <;> omega
      exact ⟨b,tail,⟨m,result,child⟩,grades_odd_decrease b tail⟩

/-- Queries consume an entire supplied source certificate under one common
well-founded order. Neither the child value nor its witness length is bounded. -/
def Hyp (active : Active) (old : List Nat) : Prop :=
  ∀ kind n e gaps, 0 < n → active kind (oddCore n) →
    Less (grades e gaps) old → PoweredCertificate (known kind n) e gaps →
    Basin (wanted kind n)

def Complete (active : Active) : Prop :=
  ∀ kind n e gaps, 0 < n → active kind (oddCore n) →
    PoweredCertificate (known kind n) e gaps → Hyp active (grades e gaps) →
    Basin (wanted kind n)

/-- A complete sound dispatcher terminates by multiset induction on the actual
source witness, even when a child has arbitrarily many more gaps. -/
theorem close {active : Active} (complete : Complete active) :
    ∀ kind n, 0 < n → active kind (oddCore n) → Claim kind n := by
  have all : ∀ word kind n e gaps, grades e gaps = word →
      0 < n → active kind (oddCore n) →
      PoweredCertificate (known kind n) e gaps → Basin (wanted kind n) := by
    intro word
    induction word using induction_on with
    | step word ih =>
      intro kind n e gaps eq hn ha cert
      apply complete kind n e gaps hn ha cert
      intro q u ee gg hu hau decrease nextCert
      exact ih (grades ee gg) (by simpa [eq] using decrease)
        q u ee gg rfl hu hau nextCert
  intro kind n hn ha
  apply (claim_iff kind n).mpr
  intro source
  obtain ⟨e,gaps,cert⟩ := basin_powered_certificate source
  exact all (grades e gaps) kind n e gaps rfl hn ha cert

/-- A transformed source certificate and two ordinary target prefixes meeting at
one endpoint give a sound recursive rule. Source transformation legality remains
an explicit proof obligation, independently of the multiset decrease. -/
theorem one_query {active : Active} {kind q : Kind} {n u e : Nat}
    {gaps old : List Nat} {join : Nat} {targetOld targetNew : List Nat}
    (sourceNew : PoweredCertificate (known q u) e gaps)
    (decrease : Less (grades e gaps) old)
    (targetParent : Trace (wanted kind n) join targetOld)
    (targetChild : Trace (wanted q u) join targetNew)
    (positive : 0 < u) (activated : active q (oddCore u))
    (ih : Hyp active old) : Basin (wanted kind n) := by
  have child := ih q u e gaps positive activated decrease sourceNew
  exact (trace_basin targetParent).mpr ((trace_basin targetChild).mp child)

/-- This global theorem requires a complete dispatcher on every activated query,
including all odd multiples of nine. No such coverage is asserted here. -/
theorem collatz_of_complete {active : Active} (complete : Complete active)
    (coverage : ∀ n, n % 18 = 9 → active (.reverse 3) n) :
    ∀ n, 0 < n → Basin n := by
  apply deep_reverse_generates ⟨basin_twice,basin_odd,?_⟩
    (show Basin 1 from ⟨0,rfl⟩)
  intro n hn hb
  have ho : n % 2 = 1 := by omega
  have ha := coverage n hn
  rw [← oddCore_of_odd n ho] at ha
  exact close complete (.reverse 3) n (by omega) ha hb

end CollatzGapMultiset
