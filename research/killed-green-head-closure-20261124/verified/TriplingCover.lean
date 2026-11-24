import Mathlib.Tactic.Ring

/-! Semantic checker for a directed tripling cover. A row (a,b) denotes
every ordinary input a*n+b, n ≥ 0. The abstract relation is instantiated
by the user's directed reachability or implication relation. -/
namespace Collatz.TriplingCover

inductive Op where | h | D | t | i | A
  deriving DecidableEq

structure Rule where
  den : ℕ
  residue : ℕ
  slope : ℕ
  base : ℕ

def rule (r : ℕ) : Op → Rule
  | .h => ⟨2, 0, 1, 0⟩
  | .D => ⟨1, 0, 2, 0⟩
  | .t => ⟨2, 1, 3, 2⟩
  | .i => ⟨3, 2, 2, 1⟩
  | .A => ⟨6, r, 18, 3*r⟩

abbrev Row := ℕ × ℕ

def evaluate (p : Row) (n : ℕ) := p.1*n+p.2

def advance (d : Rule) (p : Row) : Option Row :=
  if p.1%d.den=0 ∧ p.2%d.den=d.residue then
    some (d.slope*(p.1/d.den), d.slope*(p.2/d.den)+d.base)
  else none

def run (r : ℕ) : List Op → Row → Option Row
  | [], p => some p
  | o::os, p => (advance (rule r o) p).bind (run r os)

def triple (p : Row) : Row := (3*p.1, 3*p.2)

inductive Tree where
  | leaf (word : List Op)
  | split2 (left right : Tree)
  | split3 (first second third : Tree)

def child (k j : ℕ) (p : Row) : Row := (k*p.1, p.2 + j*p.1)

def check (r : ℕ) : Tree → Row → Bool
  | .leaf word, p => decide (run r word p = some (triple p))
  | .split2 l h, p => check r l (child 2 0 p) && check r h (child 2 1 p)
  | .split3 a b c, p =>
    check r a (child 3 0 p) && check r b (child 3 1 p) && check r c (child 3 2 p)

def Rules (r : ℕ) (R : ℕ → ℕ → Prop) : Prop :=
  ∀ o n, R ((rule r o).den*n+(rule r o).residue)
           ((rule r o).slope*n+(rule r o).base)

theorem advance_sound {d : Rule} {p q : Row} {R : ℕ → ℕ → Prop}
    (hd : ∀ n, R (d.den*n+d.residue) (d.slope*n+d.base))
    (h : advance d p = some q) (n : ℕ) : R (evaluate p n) (evaluate q n) := by
  unfold advance at h
  split at h
  next guard =>
    obtain ⟨ha, hb⟩ := guard
    have h1 := Nat.mod_add_div p.1 d.den
    have h2 := Nat.mod_add_div p.2 d.den
    rw [ha, Nat.zero_add] at h1
    rw [hb] at h2
    injection h with hq
    subst q
    have hi : evaluate p n = d.den*((p.1/d.den)*n+p.2/d.den)+d.residue := by
      unfold evaluate
      calc
        p.1*n+p.2 = (d.den*(p.1/d.den))*n+(d.residue+d.den*(p.2/d.den)) :=
          congrArg₂ (fun a b => a*n+b) h1.symm h2.symm
        _ = _ := by ring
    rw [hi]
    convert hd ((p.1/d.den)*n+p.2/d.den) using 1
    dsimp [evaluate]
    ring
  next => contradiction

theorem run_sound {r : ℕ} {R : ℕ → ℕ → Prop} (h0 : ∀ x, R x x)
    (ht : ∀ {x y z}, R x y → R y z → R x z) (hr : Rules r R)
    (w : List Op) {p q : Row} (h : run r w p = some q) (n : ℕ) :
    R (evaluate p n) (evaluate q n) := by
  induction w generalizing p with
  | nil =>
    have he : p=q := Option.some.inj h
    subst q
    exact h0 _
  | cons o w ih =>
    cases ha : advance (rule r o) p with
    | none => simp [run, ha] at h
    | some v =>
      simp [run, ha] at h
      exact ht (advance_sound (hr o) ha n) (ih h)

def Covers (R : ℕ → ℕ → Prop) (p : Row) := ∀ n, R (evaluate p n) (3*evaluate p n)

theorem split_sound {R : ℕ → ℕ → Prop} {k : ℕ} (hk : 0<k) {p : Row}
    (h : ∀ j, j<k → Covers R (child k j p)) : Covers R p := by
  intro n
  have hi : evaluate p n = evaluate (child k (n%k) p) (n/k) := by
    unfold child evaluate
    dsimp only
    calc
      p.1*n+p.2 = p.1*(n%k+k*(n/k))+p.2 :=
        congrArg (fun x => p.1*x+p.2) (Nat.mod_add_div n k).symm
      _ = _ := by ring
  rw [hi]
  exact h _ (Nat.mod_lt n hk) _

/-- A successful finite Boolean check yields the relation on every point of
the input progression, for any reflexive transitive relation obeying the rows. -/
theorem check_sound {r : ℕ} {R : ℕ → ℕ → Prop} (h0 : ∀ x, R x x)
    (ht : ∀ {x y z}, R x y → R y z → R x z) (hr : Rules r R)
    (tree : Tree) {p : Row} (h : check r tree p = true) : Covers R p := by
  induction tree generalizing p with
  | leaf w =>
    simp only [check, decide_eq_true_eq] at h
    intro n
    have he : evaluate (triple p) n = 3*evaluate p n := by dsimp [triple, evaluate]; ring
    rw [← he]
    exact run_sound h0 ht hr w h n
  | split2 l u ihl ihu =>
    simp only [check, Bool.and_eq_true] at h
    refine split_sound (R := R) (p := p) (k := 2) (by decide) ?_
    intro j hj
    have hj' : j=0 ∨ j=1 := by omega
    rcases hj' with rfl | rfl
    · exact ihl h.1
    · exact ihu h.2
  | split3 a b c iha ihb ihc =>
    simp only [check, Bool.and_eq_true] at h
    refine split_sound (R := R) (p := p) (k := 3) (by decide) ?_
    intro j hj
    have hj' : j=0 ∨ j=1 ∨ j=2 := by omega
    rcases hj' with rfl | rfl | rfl
    · exact iha h.1.1
    · exact ihb h.1.2
    · exact ihc h.2

#print axioms advance_sound
#print axioms run_sound
#print axioms split_sound
#print axioms check_sound
end Collatz.TriplingCover
