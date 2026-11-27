import OrdinaryGapWord
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Algebra.Order.BigOperators.GroupWithZero.Finset
import Mathlib.Data.Finset.Max
import Mathlib.Data.Nat.Find
import Mathlib.Tactic.NormNum

/-! A finite simple-path estimate. All inequalities use ordinary natural
integers and exact powers. No analytic packing or fixed floor is assumed. -/
set_option autoImplicit false
set_option warningAsError true

namespace OldHeadBudget
open scoped BigOperators

private theorem single_factor (u : ℕ) :
    (3*(u+3)+1)^6*(u+1) ≤ (3*(u+3))^6*(u+3) := by
  have ident :
      (3*(u+3)+1)^6*(u+1) +
      (1701*u^5+27405*u^4+176715*u^3+570087*u^2+920087*u+594323) =
      (3*(u+3))^6*(u+3) := by ring
  omega

private theorem rank_factor (a v : ℕ) (h : 2*v+3 ≤ a) :
    (3*a+1)^6*(2*v+1) ≤ (3*a)^6*(2*v+3) := by
  obtain ⟨d,hd⟩ := Nat.exists_eq_add_of_le h
  have old := single_factor (2*v+d)
  have mono : (3*a)^6*d ≤ (3*a+1)^6*d :=
    Nat.mul_le_mul_right d (Nat.pow_le_pow_left (by omega) _)
  rw [← show 2*v+d+3=a by omega] at mono ⊢
  nlinarith only [old,mono]

/-- The local correction product on *any* set of distinct odd heights at
least three is bounded by its cardinality, without an upper height cutoff. -/
theorem sixth_product (s : Finset ℕ) (odd : ∀ a∈s, a%2=1)
    (floor : ∀ a∈s, 3≤a) :
    (∏ a ∈ s, (3*a+1)^6) ≤ (2*s.card+1)*(∏ a ∈ s, (3*a)^6) := by
  induction s using Finset.induction_on_max with
  | empty => simp
  | insert a s largest ih =>
    have h0 : a ∉ s := fun ha => (Nat.lt_irrefl a) (largest a ha)
    have odda := odd a (Finset.mem_insert_self a s)
    have floora := floor a (Finset.mem_insert_self a s)
    have odds : ∀ b∈s, b%2=1 := fun b hb => odd b (Finset.mem_insert_of_mem hb)
    have floors : ∀ b∈s, 3≤b := fun b hb => floor b (Finset.mem_insert_of_mem hb)
    have inject : s.card ≤ (Finset.range ((a-3)/2)).card := by
      apply Finset.card_le_card_of_injOn (fun b : ℕ => (b-3)/2)
      · intro b hb
        have b1 := odds b hb
        have b2 := floors b hb
        have b3 := largest b hb
        simp only [Finset.mem_coe,Finset.mem_range] at *
        omega
      · intro b hb c hc eq
        have b1 := odds b hb
        have b2 := floors b hb
        have c1 := odds c hc
        have c2 := floors c hc
        dsimp at eq
        omega
    rw [Finset.card_range] at inject
    have single := rank_factor a s.card (by omega)
    have tail := ih odds floors
    rw [Finset.prod_insert h0,Finset.prod_insert h0,Finset.card_insert_of_notMem h0]
    calc
      _ ≤ (3*a+1)^6*((2*s.card+1)*∏ i ∈ s, (3*i)^6) :=
        Nat.mul_le_mul_left _ tail
      _ = ((3*a+1)^6*(2*s.card+1))*(∏ i ∈ s,(3*i)^6) := by ring
      _ ≤ ((3*a)^6*(2*s.card+3))*(∏ i ∈ s,(3*i)^6) :=
        Nat.mul_le_mul_right _ single
      _ = _ := by ring

structure Orbit where
  x : ℕ → ℕ
  e : ℕ → ℕ
  odd : ∀ i, x i % 2 = 1
  edge : ∀ i, 2^(e i)*x (i+1)=3*x i+1

def clock (o : Orbit) (n : ℕ) : ℕ := ∑ i ∈ Finset.range n, o.e i

theorem Orbit.pos (o : Orbit) (i : ℕ) : 0<o.x i := by have := o.odd i; omega

private theorem exact_product (o : Orbit) (n : ℕ) :
    (2^(clock o n)*o.x n)^6*(∏ i ∈ Finset.range n, (3*o.x i)^6) =
    (3^n*o.x 0)^6*(∏ i ∈ Finset.range n, (3*o.x i+1)^6) := by
  induction n with
  | zero => simp [clock]
  | succ n ih =>
    have eq := o.edge n
    rw [clock,Finset.sum_range_succ,pow_add,Finset.prod_range_succ,
      Finset.prod_range_succ]
    rw [← show clock o n = ∑ i ∈ Finset.range n, o.e i from rfl]
    calc
      _ = ((2^(clock o n)*o.x n)^6*∏ i ∈ Finset.range n, (3*o.x i)^6) *
          (3*(2^(o.e n)*o.x (n+1)))^6 := by ring
      _ = _ := by rw [ih,eq,pow_succ 3 n]; ring

/-- The complete sixth-power affine bound on a finite ordinary odd segment
with distinct departed states; the terminal may coincide with a departure. -/
theorem simple_budget (o : Orbit) (n : ℕ)
    (simple : Set.InjOn o.x (Finset.range n : Finset ℕ))
    (floor : ∀ i<n, 3≤o.x i) :
    (2^(clock o n)*o.x n)^6 ≤ (3^n*o.x 0)^6*(2*n+1) := by
  let s := (Finset.range n).image o.x
  have hs : s.card=n := (Finset.card_image_iff.mpr simple).trans (Finset.card_range n)
  have ho : ∀ a∈s, a%2=1 := by
    intro a ha
    obtain ⟨i,_,rfl⟩ := Finset.mem_image.mp ha
    exact o.odd i
  have hf : ∀ a∈s, 3≤a := by
    intro a ha
    obtain ⟨i,hi,rfl⟩ := Finset.mem_image.mp ha
    exact floor i (Finset.mem_range.mp hi)
  have prod := sixth_product s ho hf
  rw [hs] at prod
  dsimp [s] at prod
  rw [Finset.prod_image simple,Finset.prod_image simple] at prod
  have hp : 0<∏ i ∈ Finset.range n, (3*o.x i)^6 :=
    Finset.prod_pos (fun i _ => by have := o.pos i; positivity)
  apply Nat.le_of_mul_le_mul_right (c := ∏ i ∈ Finset.range n,(3*o.x i)^6) _ hp
  rw [exact_product,mul_assoc]
  exact Nat.mul_le_mul_left _ prod

#print axioms sixth_product
#print axioms simple_budget
end OldHeadBudget
