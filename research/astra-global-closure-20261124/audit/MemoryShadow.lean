import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Data.Rat.Cast.Order

namespace Collatz.BoundedMemoryShadow

/-- A history is ordered from oldest to newest. False is L, true is P. -/
def Hist : Nat → Type
  | 0 => Unit
  | n + 1 => Bool × Hist n

def snoc : {n : Nat} → Hist n → Bool → Hist (n+1)
  | 0, _, t => (t, ())
  | _+1, (s,u), t => (s, snoc u t)

def shift : {n : Nat} → Hist n → Bool → Hist n
  | 0, _, _ => ()
  | _+1, (_,u), t => snoc u t

private theorem splitLast {n : Nat} (h : Hist (n+1)) :
    ∃ (u : Hist n) (t : Bool), h = snoc u t := by
  induction n with
  | zero =>
    rcases h with ⟨t, u⟩
    exact ⟨(),t,by cases u; rfl⟩
  | succ n ih =>
    rcases h with ⟨a,v⟩
    obtain ⟨w,t,hw⟩ := ih v
    exact ⟨(a,w),t,by rw [hw]; rfl⟩

def allowed (t : Bool) (c : ℤ) : Prop :=
  c = 5 ∨ c = 7 ∨ (t = true ∧ (c = 11 ∨ c = 19))

def oldCarry (t : Bool) : ℚ := if t then 5 else 7

def clockDen (t : Bool) : ℚ := if t then 32 else 8

/-- The complete coefficient identity for a uniform affine shadow rule. -/
def Legal {n : Nat} (a : ℚ) (b : Hist n → ℚ) : Prop :=
  ∀ (s : Hist n) (t : Bool), ∃ c : ℤ, allowed t c ∧
    9*b s + (c : ℚ) = a*oldCarry t + clockDen t*b (shift s t)

private theorem siblings {n : Nat} {a : ℚ} {b : Hist (n+1) → ℚ}
    (h : Legal a b) (u : Hist n) :
    ∃ e : ℤ, -1 ≤ e ∧ e ≤ 1 ∧
      9*(b (false,u)-b (true,u))=2*(e : ℚ) := by
  obtain ⟨c,hc,h₁⟩ := h (false,u) false
  obtain ⟨d,hd,h₂⟩ := h (true,u) false
  simp [allowed] at hc hd
  change 9 * b (false,u) + (c : ℚ) = a * 7 + 8 * b (snoc u false) at h₁
  change 9 * b (true,u) + (d : ℚ) = a * 7 + 8 * b (snoc u false) at h₂
  rcases hc with rfl | rfl <;> rcases hd with rfl | rfl
  · exact ⟨0,by decide,by decide,by push_cast at *; linarith⟩
  · exact ⟨1,by decide,by decide,by push_cast at *; linarith⟩
  · exact ⟨-1,by decide,by decide,by push_cast at *; linarith⟩
  · exact ⟨0,by decide,by decide,by push_cast at *; linarith⟩

/-- Once a history has at least two letters, the oldest letter has no effect. -/
theorem dropOldest {n : Nat} {a : ℚ} {b : Hist (n+2) → ℚ}
    (h : Legal a b) (s : Bool) (v : Hist (n+1)) : b (s,v) = b (false,v) := by
  cases s with
  | false => rfl
  | true =>
    obtain ⟨u,t,rfl⟩ := splitLast v
    obtain ⟨e,he₁,he₂,he⟩ := siblings h (snoc u false)
    obtain ⟨f,hf₁,hf₂,hf⟩ := siblings h (snoc u true)
    obtain ⟨c,_,hc⟩ := h (false,(false,u)) false
    obtain ⟨d,_,hd⟩ := h (false,(true,u)) false
    obtain ⟨i,_,hi⟩ := h (false,(false,u)) true
    obtain ⟨j,_,hj⟩ := h (false,(true,u)) true
    simp [oldCarry,clockDen,shift,snoc] at hc hd hi hj
    have hzq : (16 : ℚ)*(e : ℚ)-64*(f : ℚ)=9*((c : ℚ)-d-i+j) := by
      linarith
    have hz : 16*e-64*f=9*(c-d-i+j) := by exact_mod_cast hzq
    have hfacts : e = 0 ∧ f = 0 := by omega
    rw [hfacts.1] at he
    rw [hfacts.2] at hf
    cases t <;> push_cast at * <;> linarith

/-- All bounded memories reduce to dependence on the most recent letter. -/
theorem memoryOne {n : Nat} {a : ℚ} {b : Hist (n+1) → ℚ}
    (h : Legal a b) (v w : Hist n) (t : Bool) :
    b (snoc v t) = b (snoc w t) := by
  induction n with
  | zero => cases v; cases w; rfl
  | succ n ih =>
    let b' : Hist (n+1) → ℚ := fun u => b (false,u)
    have h' : Legal a b' := by
      intro u t
      obtain ⟨c,hc,he⟩ := h (false,u) t
      rcases u with ⟨s,v⟩
      refine ⟨c,hc,?_⟩
      change 9*b (false,(s,v)) + (c:ℚ) =
        a*oldCarry t + clockDen t*b (s,snoc v t) at he
      change 9*b (false,(s,v)) + (c:ℚ) =
        a*oldCarry t + clockDen t*b (false,snoc v t)
      rw [dropOldest h s (snoc v t)] at he
      exact he
    rcases v with ⟨s,v⟩
    rcases w with ⟨r,w⟩
    change b (s,snoc v t)=b (r,snoc w t)
    rw [dropOldest h s,dropOldest h r]
    exact ih h' v w

/-- Six possible triples (scaled slope and intercepts), under strict contraction. -/
def Classified (a l p : ℚ) : Prop :=
  (83*a=60 ∧ 83*l=5 ∧ 83*p=5) ∨
  (83*a=61 ∧ 83*l=12 ∧ 83*p=12) ∨
  (83*a=63 ∧ 83*l=26 ∧ 83*p=26) ∨
  (83*a=67 ∧ 83*l=54 ∧ 83*p=54) ∨
  (747*a=572 ∧ 747*l=269 ∧ 747*p=103) ∨
  (747*a=724 ∧ 747*l= -161 ∧ 747*p=5)

private theorem allowedL {c : ℤ} (h : allowed false c) : c=5 ∨ c=7 := by
  simpa [allowed] using h

private theorem allowedP {c : ℤ} (h : allowed true c) : c=5 ∨ c=7 ∨ c=11 ∨ c=19 := by
  simpa [allowed] using h

set_option maxHeartbeats 1000000 in
theorem classifyOne {a : ℚ} (ha : 0<a) (hb : a<1) {b : Hist 1 → ℚ}
    (h : Legal a b) : Classified a (b (false,())) (b (true,())) := by
  obtain ⟨ll,c₁,h₁⟩ := h (false,()) false
  obtain ⟨lp,c₂,h₂⟩ := h (false,()) true
  obtain ⟨pl,c₃,h₃⟩ := h (true,()) false
  obtain ⟨pp,c₄,h₄⟩ := h (true,()) true
  simp [oldCarry,clockDen,shift,snoc] at h₁ h₂ h₃ h₄
  unfold Classified
  rcases allowedL c₁ with rfl|rfl <;> rcases allowedP c₂ with rfl|rfl|rfl|rfl <;>
    rcases allowedL c₃ with rfl|rfl <;> rcases allowedP c₄ with rfl|rfl|rfl|rfl <;>
    norm_num at h₁ h₂ h₃ h₄ <;>
    first | exfalso; linarith | left; exact ⟨by linarith,by linarith,by linarith⟩ |
      right; left; exact ⟨by linarith,by linarith,by linarith⟩ |
      right; right; left; exact ⟨by linarith,by linarith,by linarith⟩ |
      right; right; right; left; exact ⟨by linarith,by linarith,by linarith⟩ |
      right; right; right; right; left; exact ⟨by linarith,by linarith,by linarith⟩ |
      right; right; right; right; right; exact ⟨by linarith,by linarith,by linarith⟩

/-- The finite table applies without a bound on the size of the original history. -/
theorem classifyAll {n : Nat} {a : ℚ} (ha : 0<a) (hb : a<1)
    {b : Hist (n+1) → ℚ} (h : Legal a b) (u : Hist n) :
    Classified a (b (snoc u false)) (b (snoc u true)) := by
  let f : Hist 1 → ℚ := fun s => b (snoc u s.1)
  have hf : Legal a f := by
    rintro ⟨s,z⟩ t
    obtain ⟨c,hc,he⟩ := h (snoc u s) t
    have htarget : b (shift (snoc u s) t) = b (snoc u t) := by
      generalize snoc u s = v
      rcases v with ⟨r,v⟩
      exact memoryOne h v u t
    rw [htarget] at he
    exact ⟨c,hc,he⟩
  exact classifyOne ha hb hf

private theorem scaleEquation (d u v q y : ℤ) (a b : ℚ)
    (hu : (d:ℚ)*a=u) (hv : (d:ℚ)*b=v) (hy : a*q+b=y) :
    u*q+v=d*y := by
  have hq : (u:ℚ)*(q:ℚ) + (v:ℚ) = (d:ℚ)*(y:ℚ) := by
    rw [← hu, ← hv, ← hy, mul_add, mul_assoc]
  exact_mod_cast hq

private theorem tableObstruction {a l p : ℚ} (h : Classified a l p)
    (q y : ℤ) (t : Bool) (hy : a*q+(if t then p else l)=y) : 83 ∣ q+7 := by
  rcases h with ⟨ha,hl,hp⟩ | ⟨ha,hl,hp⟩ | ⟨ha,hl,hp⟩ | ⟨ha,hl,hp⟩ |
    ⟨ha,hl,hp⟩ | ⟨ha,hl,hp⟩ <;> cases t <;> simp at hy <;>
    first
    | have hz := scaleEquation 83 60 5 q y a l ha hl hy; omega
    | have hz := scaleEquation 83 60 5 q y a p ha hp hy; omega
    | have hz := scaleEquation 83 61 12 q y a l ha hl hy; omega
    | have hz := scaleEquation 83 61 12 q y a p ha hp hy; omega
    | have hz := scaleEquation 83 63 26 q y a l ha hl hy; omega
    | have hz := scaleEquation 83 63 26 q y a p ha hp hy; omega
    | have hz := scaleEquation 83 67 54 q y a l ha hl hy; omega
    | have hz := scaleEquation 83 67 54 q y a p ha hp hy; omega
    | have hz := scaleEquation 747 572 269 q y a l ha hl hy; omega
    | have hz := scaleEquation 747 572 103 q y a p ha hp hy; omega
    | have hz := scaleEquation 747 724 (-161) q y a l ha hl hy; omega
    | have hz := scaleEquation 747 724 5 q y a p ha hp hy; omega

/-- An integral shadow with any finite past memory forces the PR191 residue. -/
theorem integralShadowResidue {n : Nat} {a : ℚ} (ha : 0<a) (hb : a<1)
    {b : Hist (n+1) → ℚ} (h : Legal a b) (s : Hist (n+1)) (q y : ℤ)
    (hy : a*q+b s=y) : 83 ∣ q+7 := by
  obtain ⟨u,t,rfl⟩ := splitLast s
  apply tableObstruction (classifyAll ha hb h u) q y t
  cases t <;> exact hy

#print axioms dropOldest
#print axioms memoryOne
#print axioms classifyOne
#print axioms classifyAll
#print axioms integralShadowResidue
end Collatz.BoundedMemoryShadow
