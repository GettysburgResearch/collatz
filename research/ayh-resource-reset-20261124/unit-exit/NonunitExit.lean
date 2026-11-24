import Mathlib.Tactic.Ring
import Mathlib.Tactic.Positivity

/-! Physical affine identities and the ordinary rational-shadow comparison.
The two label laws are exactly invariance of an ordinary shortcut label. -/
namespace NonunitExit

variable {α : Type*} (f : ℕ → α)
variable (he : ∀ n, f (2*n) = f n) (ho : ∀ n, f (2*n+1) = f (3*n+2))

include he ho

private theorem plusfour (s : ℕ) : f (4*s+1)=f (3*s+1) := by
  calc
    f (4*s+1) = f (2*(2*s)+1) := by congr 1; omega
    _ = f (3*(2*s)+2) := ho _
    _ = f (2*(3*s+1)) := by congr 1; omega
    _ = f (3*s+1) := he _

private theorem doubleplus (s : ℕ) : f (3*(16*s+1))=f (27*s+2) := by
  calc
    f (3*(16*s+1)) = f (2*(24*s+1)+1) := by congr 1; omega
    _ = f (3*(24*s+1)+2) := ho _
    _ = f (2*(36*s+2)+1) := by congr 1; omega
    _ = f (3*(36*s+2)+2) := ho _
    _ = f (2*(2*(27*s+2))) := by congr 1; omega
    _ = f (27*s+2) := by rw [he,he]

private theorem oddJ (x : ℕ) : f (2*x+1) = f (3*(2*x+1)+1) := by
  rw [ho,show 3*(2*x+1)+1=2*(3*x+2) by omega,he]

/-- The old low and high labels and the intermediate label form an exact chain. -/
theorem physical_chain (s : ℕ) (hs : s%2=1) :
    f (3*s)=f (16*s+1) ∧ f (3*(16*s+1))=f (32*s+1) ∧
    f (3*(32*s+1))=f (3*(3*s)) := by
  have j (n : ℕ) (hn : n%2=1) : f n=f (3*n+1) := by
    convert oddJ f he ho (n/2) using 1 <;> congr 1 <;> omega
  have p (s : ℕ) : f (16*s+1)=f (9*s+1) := by
    calc
      _ = f (4*(4*s)+1) := by congr 1; omega
      _ = f (3*(4*s)+1) := plusfour f he ho _
      _ = f (4*(3*s)+1) := by congr 1; omega
      _ = f (3*(3*s)+1) := plusfour f he ho _
      _ = _ := by congr 1; omega
  refine ⟨?_, ?_, ?_⟩
  · calc
      _ = f (3*(3*s)+1) := j _ (by omega)
      _ = f (9*s+1) := by congr 1; omega
      _ = _ := (p s).symm
  · calc
      _ = f (27*s+2) := doubleplus f he ho _
      _ = f (3*(9*s)+2) := by congr 1; omega
      _ = f (2*(9*s)+1) := (ho (9*s)).symm
      _ = f (9*(2*s)+1) := by congr 1; omega
      _ = f (16*(2*s)+1) := (p (2*s)).symm
      _ = _ := by congr 1; omega
  · calc
      _ = f (3*(16*(2*s)+1)) := by congr 1; omega
      _ = f (27*(2*s)+2) := doubleplus f he ho _
      _ = f (2*(27*s+1)) := by congr 1; omega
      _ = f (27*s+1) := he _
      _ = f (3*(3*(3*s))+1) := by congr 1; omega
      _ = _ := (j _ (by omega)).symm

omit he ho

/-- On binary labels exactly one successor inherits the full directed defect. -/
theorem directed_successor (b : ℕ → Bool)
    (he' : ∀ n, b (2*n)=b n) (ho' : ∀ n, b (2*n+1)=b (3*n+2))
    (s : ℕ) (hs : s%2=1) (d : b (3*s)≠b (3*(3*s))) :
    (b (16*s+1)=b (3*s) ∧ b (3*(16*s+1))=b (3*(3*s)) ∧
      b (32*s+1)=b (3*(32*s+1))) ∨
    (b (32*s+1)=b (3*s) ∧ b (3*(32*s+1))=b (3*(3*s)) ∧
      b (16*s+1)=b (3*(16*s+1))) := by
  obtain ⟨a,m,c⟩ := physical_chain b he' ho' s hs
  by_cases h : b (3*(16*s+1))=b (3*s)
  · exact Or.inr ⟨m.symm.trans h, c, a.symm.trans h.symm⟩
  · have h' : b (3*(16*s+1))=b (3*(3*s)) := by
      cases e₁ : b (3*s) <;> cases e₂ : b (3*(3*s)) <;>
        cases e₃ : b (3*(16*s+1)) <;> simp_all
    exact Or.inl ⟨a.symm, h', m.symm.trans (h'.trans c.symm)⟩

/-- Valid even and odd filters on a numerator with a positive odd denominator. -/
def stepD (d n : ℕ) := if n%2=0 then n/2 else (3*n+d)/2
def iterD (d : ℕ) : ℕ → ℕ → ℕ
  | 0, n => n
  | k+1, n => iterD d k (stepD d n)
def gradeD (d : ℕ) : ℕ → ℕ → ℕ
  | 0, _ => 0
  | k+1, n => gradeD d k (stepD d n) + n%2

private theorem shifted (d b k q : ℕ) :
    stepD d (b+2^(k+1)*q) = stepD d b + 2^k * (3^(b%2)*q) := by
  rw [show b+2^(k+1)*q = b+2*(2^k*q) by rw [pow_succ]; ring]
  have par : (b+2*(2^k*q))%2=b%2 := by omega
  unfold stepD
  rw [par]
  by_cases h : b%2=0
  · simp [h]; omega
  · have hb : b%2=1 := by omega
    simp [hb]
    rw [show 3*(b+2*(2^k*q))+d = (3*b+d)+2*(3*(2^k*q)) by ring]
    rw [show 2^k*(3*q)=3*(2^k*q) by ring]
    omega

/-- A complete affine lift for rational shadows, with arbitrary denominator. -/
theorem shadow_lift (d k b q : ℕ) :
    iterD d k (b+2^k*q) = iterD d k b + 3^(gradeD d k b)*q := by
  induction k generalizing b q with
  | zero => simp [iterD,gradeD]
  | succ k ih =>
    rw [iterD, shifted, ih, iterD,gradeD,pow_add]
    ring

private theorem denom_step (d n : ℕ) (hd : d%2=1) :
    stepD d (d*n)=d*stepD 1 n := by
  have hp : (d*n)%2=n%2 := by simp [Nat.mul_mod,hd]
  unfold stepD
  rw [hp]
  by_cases h : n%2=0
  · simp only [h,ite_true]
    have hn : n=2*(n/2) := by omega
    conv_lhs => rw [hn]
    rw [show d*(2*(n/2))=2*(d*(n/2)) by ring]
    omega
  · simp only [h,ite_false]
    have hn : 3*n+1=2*((3*n+1)/2) := by omega
    rw [show 3*(d*n)+d=d*(3*n+1) by ring]
    conv_lhs => rw [hn]
    rw [show d*(2*((3*n+1)/2))=2*(d*((3*n+1)/2)) by ring]
    omega

theorem denom_iter (d n k : ℕ) (hd : d%2=1) :
    iterD d k (d*n)=d*iterD 1 k n := by
  induction k generalizing n with
  | zero => rfl
  | succ k ih => rw [iterD,denom_step d n hd,ih,iterD]

/-- An exact equality of shadow value and relative grade verifies actual meeting
for every ordinary high part compatible with the itinerary. -/
theorem shadow_certifies (d x b k q : ℕ) (hd : d%2=1)
    (hx : d*x=b+2^k*q)
    (hv : iterD d k b=iterD d k (3*b))
    (hg : gradeD d k b=1+gradeD d k (3*b)) :
    iterD 1 k x=iterD 1 k (3*x) := by
  have h₁ := shadow_lift d k b q
  have h₂ := shadow_lift d k (3*b) (3*q)
  rw [← hx,denom_iter d x k hd] at h₁
  have hx' : d*(3*x)=3*b+2^k*(3*q) := by
    calc
      _ = 3*(d*x) := by ring
      _ = _ := by rw [hx]; ring
  rw [← hx',denom_iter d (3*x) k hd] at h₂
  have eq : d*iterD 1 k x=d*iterD 1 k (3*x) := by
    rw [h₁,h₂,hv,hg,pow_add]
    ring
  exact Nat.eq_of_mul_eq_mul_left (by omega : 0<d) eq

#print axioms physical_chain
#print axioms directed_successor
#print axioms shadow_lift
#print axioms denom_iter
#print axioms shadow_certifies

end NonunitExit
