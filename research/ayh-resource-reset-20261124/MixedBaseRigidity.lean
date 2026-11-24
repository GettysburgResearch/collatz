import Std.Tactic

/-!
Scalar rigidity of the eleven mixed-base Collatz rules of Yolcu, Aaronson
and Heule (2023). The domain is the usual natural-number chain. A symbol
denotes a strictly increasing unary operator. Weak orientation of five
specified rules already collapses all digit operators.
-/
namespace MixedBaseRigidity

inductive Sym | a | b | c | d | e | f | g deriving DecidableEq, Repr
open Sym

abbrev Ops := Sym → Nat → Nat

def interp (p : Ops) : List Sym → Nat → Nat
  | [], x => x
  | s :: w, x => p s (interp p w x)

def rules : List (List Sym × List Sym) :=
  [([a,d],[d]), ([b,d],[g,d]), ([a,e],[e,a]), ([a,f],[e,b]),
   ([a,g],[f,a]), ([b,e],[f,b]), ([b,f],[g,a]), ([b,g],[g,b]),
   ([c,e],[c,b]), ([c,f],[c,a,a]), ([c,g],[c,a,b])]

def Strict (p : Ops) := ∀ s x y, x < y → p s x < p s y

def Weak (p : Ops) (rev : Bool) :=
  ∀ l r, (l,r) ∈ rules → ∀ x,
    interp p (if rev then r.reverse else r) x ≤
      interp p (if rev then l.reverse else l) x

private theorem extensive {p : Ops} (hs : Strict p) (s : Sym) (x : Nat) :
    x ≤ p s x := by
  induction x with
  | zero => omega
  | succ x ih =>
    have := hs s x (x+1) (by omega)
    omega

private theorem reflect {p : Ops} (hs : Strict p) (s : Sym) {x y : Nat}
    (h : p s x ≤ p s y) : x ≤ y := by
  by_cases hn : x ≤ y
  · exact hn
  · have := hs s y x (by omega)
    omega

private theorem rigid {p : Ops} (hs : Strict p) (s : Sym)
    (cof : ∀ n, ∃ y, n ≤ y ∧ p s y ≤ y) : ∀ n, p s n = n := by
  intro n
  obtain ⟨y, hny, hy⟩ := cof n
  have advance : ∀ k, p s n + k ≤ p s (n+k) := by
    intro k
    induction k with
    | zero => simp
    | succ k ih =>
      have := hs s (n+k) (n+k+1) (by omega)
      change p s n + (k+1) ≤ p s (n+k+1)
      omega
  have he : n + (y-n) = y := by omega
  have ha := advance (y-n)
  rw [he] at ha
  have := extensive hs s n
  omega

def DigitIdentities (p : Ops) :=
  (∀ x, p a x = x) ∧ (∀ x, p b x = x) ∧
  (∀ x, p e x = x) ∧ (∀ x, p f x = x) ∧ (∀ x, p g x = x)

theorem forwardCollapse (p : Ops) (hs : Strict p) (h : Weak p false) :
    DigitIdentities p := by
  have hbd (x) : p g (p d x) ≤ p b (p d x) := h [b,d] [g,d] (by decide) x
  have hcg (x) : p a (p b x) ≤ p g x :=
    reflect hs c (h [c,g] [c,a,b] (by decide) x)
  have ha : ∀ x, p a x = x := rigid hs a (fun n =>
    ⟨p b (p d n), Nat.le_trans (extensive hs d n) (extensive hs b _),
      Nat.le_trans (hcg _) (hbd _)⟩)
  have hgf (x) : p f x ≤ p g x := by
    have h' : p f (p a x) ≤ p a (p g x) := h [a,g] [f,a] (by decide) x
    simpa only [ha] using h'
  have hfe (x) : p e (p b x) ≤ p f x := by
    have h' : p e (p b x) ≤ p a (p f x) := h [a,f] [e,b] (by decide) x
    simpa only [ha] using h'
  have heb (x) : p b x ≤ p e x := reflect hs c (h [c,e] [c,b] (by decide) x)
  have hb : ∀ x, p b x = x := rigid hs b (fun n =>
    ⟨p b (p d n), Nat.le_trans (extensive hs d n) (extensive hs b _),
      Nat.le_trans (heb _) (Nat.le_trans (hfe _) (Nat.le_trans (hgf _) (hbd _)))⟩)
  have hg : ∀ x, p g x = x := rigid hs g (fun n =>
    ⟨p d n, extensive hs d n, by simpa only [hb] using hbd n⟩)
  have hf : ∀ x, p f x = x := fun n =>
    Nat.le_antisymm (by simpa only [hg] using hgf n) (extensive hs f n)
  have he : ∀ x, p e x = x := fun n =>
    Nat.le_antisymm (by simpa only [hb,hf] using hfe n) (extensive hs e n)
  exact ⟨ha,hb,he,hf,hg⟩

theorem reverseCollapse (p : Ops) (hs : Strict p) (h : Weak p true) :
    DigitIdentities p := by
  have hbd (x) : p g x ≤ p b x := reflect hs d (h [b,d] [g,d] (by decide) x)
  have hcg (x) : p b (p a (p c x)) ≤ p g (p c x) := h [c,g] [c,a,b] (by decide) x
  have ha : ∀ x, p a x = x := rigid hs a (fun n =>
    ⟨p c n, extensive hs c n, reflect hs b (Nat.le_trans (hcg n) (hbd _))⟩)
  have hgf (x) : p f x ≤ p g x := by
    have h' : p a (p f x) ≤ p g (p a x) := h [a,g] [f,a] (by decide) x
    simpa only [ha] using h'
  have hfe (x) : p b (p e x) ≤ p f x := by
    have h' : p b (p e x) ≤ p f (p a x) := h [a,f] [e,b] (by decide) x
    simpa only [ha] using h'
  have heb (x) : p b (p c x) ≤ p e (p c x) := h [c,e] [c,b] (by decide) x
  have hb : ∀ x, p b x = x := rigid hs b (fun n =>
    ⟨p c n, extensive hs c n, Nat.le_trans (heb n)
      (reflect hs b (Nat.le_trans (hfe _) (Nat.le_trans (hgf _) (hbd _))))⟩)
  have hg : ∀ x, p g x = x := fun n =>
    Nat.le_antisymm (by simpa only [hb] using hbd n) (extensive hs g n)
  have hf : ∀ x, p f x = x := fun n =>
    Nat.le_antisymm (by simpa only [hg] using hgf n) (extensive hs f n)
  have he : ∀ x, p e x = x := fun n =>
    Nat.le_antisymm (by simpa only [hb,hf] using hfe n) (extensive hs e n)
  exact ⟨ha,hb,he,hf,hg⟩

/-- Applies to every rule in either word orientation. -/
theorem allRulesEqual (p : Ops) (rev : Bool) (hs : Strict p) (h : Weak p rev) :
    ∀ l r, (l,r) ∈ rules → ∀ x,
    interp p (if rev then l.reverse else l) x =
      interp p (if rev then r.reverse else r) x := by
  have hid : DigitIdentities p := by
    cases rev with
    | false => exact forwardCollapse p hs h
    | true => exact reverseCollapse p hs h
  obtain ⟨ha, hb, he, hf, hg⟩ := hid
  intro l r hr x
  simp only [rules,List.mem_cons,List.not_mem_nil,or_false,Prod.mk.injEq] at hr
  rcases hr with h|h|h|h|h|h|h|h|h|h|h <;> obtain ⟨rfl,rfl⟩ := h <;>
    cases rev <;> simp [interp,ha,hb,he,hf,hg]

end MixedBaseRigidity
