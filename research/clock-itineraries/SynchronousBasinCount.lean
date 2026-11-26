module

public import SynchronousBasin
public import WindowCapture
import all WindowCapture
import all MinimumDescent
import all TernaryItinerary

public section
namespace Collatz.Itinerary.SynchronousBasinCount

open WindowCapture FreeTripleClock SynchronousBasin
set_option autoImplicit false

/-- Finite-bank formulation of the published Krasikov–Lagarias lower bound
for each fixed positive target prime to three. This is a hypothesis below. -/
def PredecessorBound : Prop :=
  ∀ b, b%3≠0 → ∃ A, ∀ X, A≤X → ∃ xs : List Nat,
    xs.Nodup ∧ X^21≤xs.length^25 ∧
    ∀ n∈xs, 0<n ∧ n≤X ∧ ∃ h, run h n=b

@[expose] def limit (X : Nat) := 268435456*X/9

/-- Inspect only triples that already coincide after 28 ordinary steps.
The deadline starts at their common endpoint. -/
@[expose] def misses (X O g : Nat) : List Nat :=
  (List.range (limit X+1)).filter (fun x =>
    let b := run 28 x
    decide (0<x) && (run 28 (3*x)==b) && (run 28 (9*x)==b) && !(hitBy O b g))

private theorem enough {F : Nat → Nat} (enc : Encoding 2 28 9 268435456 F)
    {X O g b : Nat} (ub : b%3≠0) (different : ¬(ReachesOne b ↔ ReachesOne g))
    {xs : List Nat} (nd : xs.Nodup)
    (bank : ∀ n∈xs, 0<n ∧ n≤X ∧ ∃ h, run h n=b) :
    xs.length≤(misses X O g).length := by
  have clean := map_distinct (f:=F) nd (fun n hn m hm eq =>
    enc.injective (bank n hn).1 (bank m hm).1 eq)
  have sub : xs.map F ⊆ misses X O g := by
    intro x mem
    obtain ⟨n,inside,rfl⟩ := List.mem_map.mp mem
    obtain ⟨pn,small,h,hit⟩ := bank n inside
    have bound := Nat.le_trans (enc.size n pn) (Nat.mul_le_mul_left 268435456 small)
    have pos := enc.positive n pn
    have common := enc.common n pn
    let u := run 28 (F n)
    have zero : u=BasinUnitEncoding.code n := by simpa [u] using common 0 (by decide)
    have three : run 28 (3*F n)=u := (common 1 (by decide)).trans zero.symm
    have nine : run 28 (9*F n)=u := (common 2 (by decide)).trans zero.symm
    obtain ⟨j,_,path⟩ := enc.downstream pn ub hit
    have actual : run j u=b := by
      simpa only [u,Nat.pow_zero,Nat.one_mul,run_add] using path 0 (by decide)
    have failed : hitBy O u g=false := by
      cases test : hitBy O u g with
      | false => rfl
      | true =>
        obtain ⟨k,_,land⟩ := (hitBy_iff O u g).mp test
        have first := MinimumDescent.good_run j u
        have last := MinimumDescent.good_run k u
        rw [actual] at first
        rw [land] at last
        exact False.elim (different (first.trans last.symm))
    apply List.mem_filter.mpr
    refine ⟨List.mem_range.mpr (by unfold limit; omega),?_⟩
    change (decide (0<F n) && (run 28 (3*F n)==u) &&
      (run 28 (9*F n)==u) && !(hitBy O u g))=true
    simp [pos,three,nine,failed]
  simpa only [List.length_map] using clean.length_le_of_subset sub

private theorem positive (h n : Nat) (pos : 0<n) : 0<run h n := by
  induction h generalizing n with
  | zero => exact pos
  | succ h ih =>
    apply ih; unfold step; split <;> omega

/-- With the published predecessor bound as input, cofinally many fully
finite gate tests, allowing an X^(21/25) quota of misses, are equivalent
to universal Collatz. The deadline and the gate may differ by stage. -/
theorem universal_iff_sparse_triples (lower : PredecessorBound) :
    Universal ↔ ∀ N, ∃ X O g, N≤X ∧ (misses X O g).length^25<X^21 := by
  constructor
  · intro all N
    let X := N+1
    let raw := (List.range (limit X+1)).filter (fun x => decide (0<x))
    let ys := raw.map (run 28)
    have pos : ∀ y∈ys, 0<y := by
      intro y mem
      obtain ⟨x,member,rfl⟩ := List.mem_map.mp mem
      exact positive _ _ (of_decide_eq_true (List.mem_filter.mp member).2)
    obtain ⟨O,allHit⟩ := all_hit all ys pos
    have none : misses X O 1=[] := by
      apply List.eq_nil_iff_forall_not_mem.mpr
      intro x member
      obtain ⟨within,cond⟩ := List.mem_filter.mp member
      simp only [Bool.and_eq_true,Bool.not_eq_true',decide_eq_true_eq] at cond
      have mx : x∈raw := List.mem_filter.mpr ⟨within,decide_eq_true cond.1.1.1⟩
      have reached := (hitBy_iff O (run 28 x) 1).mpr
        (allHit _ (List.mem_map.mpr ⟨x,mx,rfl⟩))
      rw [reached] at cond
      simp at cond
    refine ⟨X,O,1,by dsimp [X]; omega,?_⟩
    rw [none]
    exact Nat.pow_pos (by dsimp [X]; omega)
  · intro pass
    apply Classical.byContradiction
    intro failure
    obtain ⟨q,c,_,col,bad⟩ := odd_bad_unit failure
    have uq : q%3≠0 := by cases c <;> simp_all [digit]
    obtain ⟨A,goodBanks⟩ := lower 1 (by decide)
    obtain ⟨B,badBanks⟩ := lower q uq
    obtain ⟨X,O,g,big,small⟩ := pass (A+B)
    obtain ⟨F,enc⟩ := triple_encoding
    have oppose (b : Nat) (ub : b%3≠0) (diff : ¬(ReachesOne b ↔ ReachesOne g))
        (bank : ∃ xs : List Nat, xs.Nodup ∧ X^21≤xs.length^25 ∧
          ∀ n∈xs, 0<n ∧ n≤X ∧ ∃ h, run h n=b) : False := by
      obtain ⟨xs,nd,count,paths⟩ := bank
      have le := Nat.pow_le_pow_left (enough (O:=O) enc ub diff nd paths) 25
      exact Nat.not_lt_of_ge (Nat.le_trans count le) small
    by_cases gg : ReachesOne g
    · exact oppose q uq (fun eq => bad (eq.mpr gg)) (badBanks X (by omega))
    · exact oppose 1 (by decide) (fun eq => gg (eq.mp ⟨0,rfl⟩)) (goodBanks X (by omega))

#print axioms universal_iff_sparse_triples
end Collatz.Itinerary.SynchronousBasinCount
