import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith

/-! Exact section arithmetic for the restricted positive Collatz graph,
including closure of its entire binary kernel under ternary sections. -/
namespace Collatz.Unconventional.MixedMahler

variable {R : Type*} [Zero R]

def sectionAt (m r : ℕ) (w : ℕ → R) : ℕ → R := fun n => w (m*n+r)

def InKernel (q : ℕ) (a b f : ℕ → R) : Prop :=
  f = (fun _ => 0) ∨ ∃ w k c, (w = a ∨ w = b) ∧ c < q^k ∧ f = sectionAt (q^k) c w

/-- Coefficient identities obtained at residues 0, 2, 4 modulo 6 and
1, 5, 9 modulo 12 in the mixed incidence identity. -/
structure TernaryRules (a b : ℕ → R) : Prop where
  a0 : ∀ n, a (3*n) = a (2*n)
  a1 : ∀ n, a (3*n+1) = 0
  a2 : ∀ n, a (3*n+2) = b (2*n+1)
  b0 : ∀ n, b (3*n) = b (4*n)
  b1 : ∀ n, b (3*n+1) = 0
  b2 : ∀ n, b (3*n+2) = a (4*n+3)

def outgoing (a b : ℕ → R) (u : ℕ) : R :=
  if u%2=0 then a (u/2) else if u%4=1 then b (u/4) else 0

def incoming (a b : ℕ → R) (u : ℕ) : R :=
  if u%3=0 then a (u/3) else if u%3=1 then b (u/3) else 0

/-- Coefficient balance of the actual monomial incidence equation implies the
six ternary rules, independently of any choice of edge weights. -/
theorem rules_of_balance {a b : ℕ → R}
    (H : ∀ u, outgoing a b u = incoming a b u) : TernaryRules a b := by
  constructor <;> intro n
  · have h := H (6*n)
    grind [outgoing, incoming]
  · have h := H (6*n+2)
    grind [outgoing, incoming]
  · have h := H (6*n+4)
    grind [outgoing, incoming]
  · have h := H (12*n+1)
    grind [outgoing, incoming]
  · have h := H (12*n+5)
    grind [outgoing, incoming]
  · have h := H (12*n+9)
    grind [outgoing, incoming]

theorem missing_edges {a b : ℕ → R}
    (H : ∀ u, outgoing a b u = incoming a b u) (n : ℕ) :
    a (4*n+1)=0 ∧ b (4*n+2)=0 := by
  constructor
  · have h := H (12*n+3)
    grind [outgoing, incoming]
  · have h := H (12*n+7)
    grind [outgoing, incoming]

theorem first_sections {a b w : ℕ → R} (H : TernaryRules a b)
    (hw : w = a ∨ w = b) {j : ℕ} (hj : j < 3) :
    InKernel 2 a b (sectionAt 3 j w) := by
  have casesj : j=0 ∨ j=1 ∨ j=2 := by omega
  rcases hw with hwa | hwb <;> subst w <;> rcases casesj with rfl | rfl | rfl
  · right; refine ⟨a,1,0,Or.inl rfl,by decide,?_⟩
    funext n; simpa [sectionAt] using H.a0 n
  · left; funext n; exact H.a1 n
  · right; refine ⟨b,1,1,Or.inr rfl,by decide,?_⟩
    funext n; simpa [sectionAt] using H.a2 n
  · right; refine ⟨b,2,0,Or.inr rfl,by decide,?_⟩
    funext n; simpa [sectionAt] using H.b0 n
  · left; funext n; exact H.b1 n
  · right; refine ⟨a,2,3,Or.inl rfl,by decide,?_⟩
    funext n; exact H.b2 n

/-- Every ternary section of every binary section is again a single binary
section of one original coefficient sequence, or the zero sequence. -/
theorem ternary_closure {a b f : ℕ → R} (H : TernaryRules a b)
    (hf : InKernel 2 a b f) {j : ℕ} (hj : j < 3) :
    InKernel 2 a b (sectionAt 3 j f) := by
  rcases hf with rfl | ⟨w,k,c,hw,hc,rfl⟩
  · exact Or.inl rfl
  let m := 2^k
  let d := (m*j+c)/3
  let e := (m*j+c)%3
  have he : e<3 := Nat.mod_lt _ (by decide)
  have hd : d<m := by
    have : m*j ≤ m*2 := Nat.mul_le_mul_left _ (by omega)
    change c<m at hc
    dsimp [d]
    omega
  have hde : 3*d+e=m*j+c := by dsimp [d,e]; omega
  have hcomp : sectionAt 3 j (sectionAt m c w) = sectionAt m d (sectionAt 3 e w) := by
    funext n
    unfold sectionAt
    congr 1
    calc
      m*(3*n+j)+c = 3*(m*n)+(m*j+c) := by ring
      _ = 3*(m*n+d)+e := by rw [← hde]; ring
  change InKernel 2 a b (sectionAt 3 j (sectionAt m c w))
  rw [hcomp]
  rcases first_sections H hw he with hzero | ⟨v,t,r,hv,hr,hvsec⟩
  · rw [hzero]; exact Or.inl rfl
  rw [hvsec]
  right
  refine ⟨v,t+k,2^t*d+r,hv,?_,?_⟩
  · rw [pow_add]
    change 2^t*d+r < 2^t*m
    have hmul := Nat.mul_le_mul_left (2^t) (show d+1≤m by omega)
    rw [Nat.mul_add, Nat.mul_one] at hmul
    omega
  · funext n
    unfold sectionAt
    rw [pow_add]
    change v (2^t*(m*n+d)+r) = v (2^t*m*n+(2^t*d+r))
    congr 1
    ring

/-- Iterating the preceding closure transfers arbitrary depth at base three. -/
theorem ternary_iterates {a b f : ℕ → R} (H : TernaryRules a b)
    (hf : InKernel 2 a b f) (k r : ℕ) (hr : r < 3^k) :
    InKernel 2 a b (sectionAt (3^k) r f) := by
  induction k generalizing f r with
  | zero =>
    have : r=0 := by simpa using hr
    subst r
    have hi : sectionAt (3^0) 0 f = f := by funext n; simp [sectionAt]
    rw [hi]; exact hf
  | succ k ih =>
    let e := r%3
    let d := r/3
    have he : e<3 := Nat.mod_lt _ (by decide)
    have hd : d<3^k := by dsimp [d]; rw [pow_succ] at hr; omega
    have hde : 3*d+e=r := by dsimp [d,e]; omega
    have hcomp : sectionAt (3^(k+1)) r f = sectionAt (3^k) d (sectionAt 3 e f) := by
      funext n; unfold sectionAt; congr 1
      rw [pow_succ, ← hde]; ring
    rw [hcomp]
    exact ih (ternary_closure H hf he) d hd

#print axioms rules_of_balance
#print axioms missing_edges
#print axioms first_sections
#print axioms ternary_closure
#print axioms ternary_iterates

end Collatz.Unconventional.MixedMahler
