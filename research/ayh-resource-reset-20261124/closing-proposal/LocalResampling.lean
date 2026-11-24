import Std

/-! Finite orbit graph and source arithmetic for the written local-resampling argument. -/
namespace LocalResampling

def iterate {α : Type} (T : α → α) : Nat → α → α
  | 0, x => x
  | n+1, x => iterate T n (T x)

def Meet {α : Type} (T : α → α) (H : Nat) (x y : α) : Prop :=
  ∃ i j : Nat, i ≤ H ∧ j ≤ H ∧ iterate T i x = iterate T j y

/-- Paths stay among the candidate sites, indexed by V. -/
inductive Linked {α V : Type} (T : α → α) (H : Nat) (site : V → α) : V → V → Prop
  | refl (v : V) : Linked T H site v v
  | tail {a b c : V} : Linked T H site a b →
      Meet T H (site b) (site c) → Linked T H site a c

theorem iterate_color {α : Type} (T : α → α) (f : α → Bool)
    (hf : ∀ x, f (T x) = f x) (n : Nat) (x : α) :
    f (iterate T n x) = f x := by
  induction n generalizing x with
  | zero => rfl
  | succ n ih => exact (ih (T x)).trans (hf x)

theorem meet_color {α : Type} (T : α → α) (f : α → Bool)
    (hf : ∀ x, f (T x) = f x) {H : Nat} {x y : α} (h : Meet T H x y) :
    f x = f y := by
  obtain ⟨i,j,_,_,he⟩ := h
  exact (iterate_color T f hf i x).symm.trans
    ((congrArg f he).trans (iterate_color T f hf j y))

theorem linked_color {α V : Type} (T : α → α) (f : α → Bool)
    (hf : ∀ x, f (T x) = f x) {H : Nat} {site : V → α} {x y : V}
    (h : Linked T H site x y) : f (site x) = f (site y) := by
  induction h with
  | refl => rfl
  | tail _ edge ih => exact ih.trans (meet_color T f hf edge)

/-- Every candidate's finite graph component omits at least k distinct sites
if each of the two invariant colors has k distinct representatives. -/
theorem k_outside_every_component {α V : Type} (T : α → α) (f : α → Bool)
    (hf : ∀ x, f (T x) = f x) (site : V → α) (H k : Nat)
    (lo hi : Fin k → V) (hlo : ∀ {i j}, lo i = lo j → i = j)
    (hhi : ∀ {i j}, hi i = hi j → i = j)
    (flo : ∀ i, f (site (lo i)) = false) (fhi : ∀ i, f (site (hi i)) = true)
    (v : V) : ∃ outside : Fin k → V,
      (∀ {i j}, outside i = outside j → i = j) ∧
      ∀ i, ¬Linked T H site v (outside i) := by
  cases hv : f (site v) with
  | false =>
    refine ⟨hi, @hhi, ?_⟩
    intro i link
    have eq := linked_color T f hf link
    rw [hv, fhi] at eq
    contradiction
  | true =>
    refine ⟨lo, @hlo, ?_⟩
    intro i link
    have eq := linked_color T f hf link
    rw [hv, flo] at eq
    contradiction

/-- Common ternary residue and fixed public query give the physical stride. -/
theorem query_stride (e u a c i j : Nat) (h : i ≤ j) :
    3^e*(a+3^u*j)+c =
    (3^e*(a+3^u*i)+c)+3^(e+u)*(j-i) := by
  rw [Nat.pow_add, Nat.mul_add, Nat.mul_add]
  have hs : j = i + (j-i) := by omega
  have hterm : 3^e*(3^u*j) = 3^e*(3^u*i)+(3^e*3^u)*(j-i) := by
    calc
      3^e*(3^u*j) = 3^e*(3^u*(i+(j-i))) := congrArg (fun t => 3^e*(3^u*t)) hs
      _ = _ := by simp only [Nat.mul_add, Nat.mul_assoc]
  omega

#print axioms iterate_color
#print axioms meet_color
#print axioms linked_color
#print axioms k_outside_every_component
#print axioms query_stride
end LocalResampling
