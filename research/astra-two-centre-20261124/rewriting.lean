import Std

namespace Collatz.PeakCertificate

abbrev Point := Nat × Nat

def period : Nat := 7342984060644141028475928576
def source : Point := (9664, period)

def neighbors (p : Point) : List Point := Id.run do
  let (x, k) := p
  let mut ns := [(2*x-1, 2*k)]
  if x%2 == 1 then ns := ((x+1)/2, k/2) :: ns
  else ns := (3*x/2, 3*k/2) :: ns
  if x%3 == 0 then ns := (2*x/3, 2*k/3) :: ns
  return ns

def check : Nat → Point → Point → Bool
  | 0, _, _ => false
  | d+1, parent, p =>
      if p.2 >= 1024*period then decide (p.1-1 >= 1024*9663)
      else
        decide (p.1 >= 9664 ∧ p.2 >= period ∧ p.2%6 = 0) &&
          (neighbors p).all (fun q => q == parent || check d p q)

set_option maxRecDepth 10000 in
set_option maxHeartbeats 0 in
theorem finite_tree : check 93 source source = true := by decide


inductive Known : Point → Prop
  | mk (p parent : Point) (d : Nat) (checked : check (d+1) parent p = true)
      (back : p ≠ parent → Known parent) : Known p

theorem root_known : Known source := .mk _ _ 92 finite_tree (fun h => False.elim (h rfl))

theorem local_safety {p : Point} (known : Known p) :
    (p.1-1 ≥ 1024*9663 ∧ p.2 ≥ 1024*period) ∨
      (p.1 ≥ 9664 ∧ p.2 ≥ period ∧ p.2%6 = 0 ∧ ∀ q ∈ neighbors p, Known q) := by
  obtain ⟨p, parent, d, h, back⟩ := known
  have current : Known p := .mk p parent d h back
  simp only [check] at h
  split at h
  next hp => exact .inl ⟨of_decide_eq_true h, hp⟩
  next =>
    simp only [Bool.and_eq_true, decide_eq_true_eq, List.all_eq_true] at h
    refine .inr ⟨h.1.1, h.1.2.1, h.1.2.2, ?_⟩
    intro q hq
    by_cases eq : q = parent
    · subst q
      by_cases e : p = parent
      · exact e ▸ current
      · exact back e
    · have child : check d p q = true := by simpa [eq] using h.2 q hq
      cases d with
      | zero => simp [check] at child
      | succ d' => exact .mk q p d' child (fun _ => current)

def value (p : Point) (t : Nat) := p.1 + p.2*t

def Edge (x y : Nat) : Prop :=
  y+1 = 2*x ∨ 2*y = x+1 ∨ 2*y = 3*x ∨ 3*y = 2*x

theorem lift {p : Point} {t y : Nat} (hp : p.1 ≥ 9664) (hd : p.2%6 = 0)
    (edge : Edge (value p t) y) : ∃ q ∈ neighbors p, value q t = y := by
  obtain ⟨x,k⟩ := p
  change k%6 = 0 at hd
  change x ≥ 9664 at hp
  obtain ⟨u, rfl⟩ : ∃ u, k = 6*u := ⟨k/6, by omega⟩
  change Edge (x+(6*u)*t) y at edge
  simp only [Edge, Nat.mul_assoc] at edge
  rcases edge with h | h | h | h
  · refine ⟨(2*x-1,2*(6*u)), ?_, ?_⟩
    · simp [neighbors]; split <;> split <;> simp_all
    · simp only [value, Nat.mul_assoc]; omega
  · have ho : x%2 = 1 := by omega
    refine ⟨((x+1)/2,(6*u)/2), ?_, ?_⟩
    · simp [neighbors, ho]; split <;> simp_all
    · have e : (6*u)/2 = 3*u := by omega
      simp only [value,e,Nat.mul_assoc]; omega
  · have he : x%2 ≠ 1 := by omega
    refine ⟨(3*x/2,3*(6*u)/2), ?_, ?_⟩
    · simp [neighbors, he]; split <;> simp_all
    · have e : 3*(6*u)/2 = 9*u := by omega
      simp only [value,e,Nat.mul_assoc]; omega
  · have hz : x%3 = 0 := by omega
    refine ⟨(2*x/3,2*(6*u)/3), ?_, ?_⟩
    · simp [neighbors, hz]; split <;> simp_all
    · have e : 2*(6*u)/3 = 4*u := by omega
      simp only [value,e,Nat.mul_assoc]; omega

end Collatz.PeakCertificate

#print axioms Collatz.PeakCertificate.finite_tree
#print axioms Collatz.PeakCertificate.local_safety
#print axioms Collatz.PeakCertificate.lift
