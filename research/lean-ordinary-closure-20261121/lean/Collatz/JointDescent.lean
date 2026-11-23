/- Joint ordinary comparison descent. The search must supply a complete cover;
this file proves soundness, and does not assume or claim that a cover was found. -/
import Collatz.Closure
open CollatzReverseBasin CollatzClosure
namespace CollatzJoint

inductive Kind where
  | triple | five
  deriving DecidableEq, Repr

def Kind.factor : Kind → Nat
  | .triple => 3
  | .five => 5

structure Weights where
  triple : Nat
  five : Nat
  deriving Repr

def Weights.get (w : Weights) : Kind → Nat
  | .triple => w.triple
  | .five => w.five

structure Form where
  a : Nat
  b : Nat
  deriving DecidableEq, Repr

def Form.eval (f : Form) (t : Nat) := f.a * t + f.b

def Form.mul (q : Nat) (f : Form) : Form := ⟨q*f.a, q*f.b⟩

theorem eval_mul (q : Nat) (f : Form) (t : Nat) :
    (f.mul q).eval t = q * f.eval t := by
  simp only [Form.mul, Form.eval]
  grind

def Comparison (q : Kind) (u : Nat) : Prop := Basin u ↔ Basin (q.factor * u)

def Lower (w : Weights) (p : Kind) (r : Form) (q : Kind) (u : Form) : Prop :=
  0 < u.b ∧ w.get q * u.a ≤ w.get p * r.a ∧ w.get q * u.b < w.get p * r.b

instance (w : Weights) (p : Kind) (r : Form) (q : Kind) (u : Form) :
    Decidable (Lower w p r q u) := inferInstanceAs (Decidable (_ ∧ _ ∧ _))

theorem lower_rank {w : Weights} {p : Kind} {r : Form} {q : Kind} {u : Form}
    (h : Lower w p r q u) (t : Nat) :
    0 < u.eval t ∧ w.get q * u.eval t < w.get p * r.eval t := by
  obtain ⟨hb, ha, hc⟩ := h
  have hm := Nat.mul_le_mul_right t ha
  simp only [Form.eval]
  constructor
  · omega
  · have e1 : w.get q * (u.a*t+u.b) = (w.get q*u.a)*t+w.get q*u.b := by grind
    have e2 : w.get p * (r.a*t+r.b) = (w.get p*r.a)*t+w.get p*r.b := by grind
    omega

inductive Step where
  | double (forward : Bool) (dest : Form)
  | odd (forward : Bool) (dest : Form)
  | query (forward : Bool) (kind : Kind) (dest : Form)
  deriving Repr

def Step.dest : Step → Form
  | .double _ d | .odd _ d | .query _ _ d => d

def OddLink (s d : Form) : Prop :=
  s.a % 2 = 0 ∧ s.b % 2 = 1 ∧ 3*s.a = 2*d.a ∧ 3*s.b+1 = 2*d.b

instance (s d : Form) : Decidable (OddLink s d) :=
  inferInstanceAs (Decidable (_ ∧ _ ∧ _ ∧ _))

def Step.Valid (w : Weights) (p : Kind) (r s : Form) : Step → Prop
  | .double true d => d = s.mul 2
  | .double false d => s = d.mul 2
  | .odd true d => OddLink s d
  | .odd false d => OddLink d s
  | .query true q d => d = s.mul q.factor ∧ Lower w p r q s
  | .query false q d => s = d.mul q.factor ∧ Lower w p r q d

instance (w : Weights) (p : Kind) (r s : Form) (e : Step) :
    Decidable (e.Valid w p r s) := by
  cases e with
  | double f d => cases f <;> simp only [Step.Valid] <;> infer_instance
  | odd f d => cases f <;> simp only [Step.Valid] <;> infer_instance
  | query f q d => cases f <;> simp only [Step.Valid] <;> infer_instance

private theorem oddLink_sound {s d : Form} (h : OddLink s d) (t : Nat) :
    Basin (s.eval t) ↔ Basin (d.eval t) := by
  obtain ⟨ha,hb,hc,hd⟩ := h
  have par : s.eval t % 2 = 1 := by
    simp [Form.eval, Nat.add_mod, Nat.mul_mod, ha, hb]
  have eq : 3*s.eval t+1 = 2*d.eval t := by
    simp only [Form.eval]
    calc 3*(s.a*t+s.b)+1 = (3*s.a)*t+(3*s.b+1) := by grind
         _ = (2*d.a)*t+2*d.b := by rw [hc,hd]
         _ = 2*(d.a*t+d.b) := by grind
  exact (basin_odd _ par).symm.trans (eq ▸ basin_twice (d.eval t))

def LowerHyp (w : Weights) (p : Kind) (r : Form) (t : Nat) : Prop :=
  ∀ q u, 0 < u → w.get q * u < w.get p * r.eval t → Comparison q u

theorem step_sound {w : Weights} {p : Kind} {r s : Form} {e : Step}
    (h : e.Valid w p r s) (t : Nat) (ih : LowerHyp w p r t) :
    Basin (s.eval t) ↔ Basin (e.dest.eval t) := by
  cases e with
  | double forward d =>
    cases forward with
    | false =>
      change s = d.mul 2 at h
      simp only [Step.dest, h, eval_mul]
      exact basin_twice _
    | true =>
      change d = s.mul 2 at h
      simp only [Step.dest, h, eval_mul]
      exact (basin_twice _).symm
  | odd forward d =>
    cases forward with
    | false => exact (oddLink_sound h t).symm
    | true => exact oddLink_sound h t
  | query forward q d =>
    cases forward with
    | false =>
      obtain ⟨he, hl⟩ := h
      have hr := lower_rank hl t
      have hc := ih q (d.eval t) hr.1 hr.2
      change Basin (s.eval t) ↔ Basin (d.eval t)
      rw [he, eval_mul]
      exact hc.symm
    | true =>
      obtain ⟨he, hl⟩ := h
      have hr := lower_rank hl t
      have hc := ih q (s.eval t) hr.1 hr.2
      change Basin (s.eval t) ↔ Basin (d.eval t)
      rw [he, eval_mul]
      exact hc

def endpoint (s : Form) : List Step → Form
  | [] => s
  | e::es => endpoint e.dest es

def validPath (w : Weights) (p : Kind) (r s : Form) : List Step → Bool
  | [] => true
  | e::es => decide (e.Valid w p r s) && validPath w p r e.dest es

theorem path_sound {w : Weights} {p : Kind} {r s : Form} {es : List Step}
    (h : validPath w p r s es = true) (t : Nat) (ih : LowerHyp w p r t) :
    Basin (s.eval t) ↔ Basin ((endpoint s es).eval t) := by
  induction es generalizing s with
  | nil => exact Iff.rfl
  | cons e es ind =>
    have hv := Bool.and_eq_true_iff.mp h
    exact (step_sound (of_decide_eq_true hv.1) t ih).trans (ind hv.2)

structure Certificate where
  left : List Step
  right : List Step
  deriving Repr

def Certificate.check (w : Weights) (p : Kind) (r : Form) (c : Certificate) : Bool :=
  validPath w p r r c.left && validPath w p r (r.mul p.factor) c.right &&
  decide (endpoint r c.left = endpoint (r.mul p.factor) c.right)

theorem certificate_sound {w : Weights} {p : Kind} {r : Form} {c : Certificate}
    (h : c.check w p r = true) (t : Nat) (ih : LowerHyp w p r t) :
    Comparison p (r.eval t) := by
  have hh := Bool.and_eq_true_iff.mp h
  have hp := Bool.and_eq_true_iff.mp hh.1
  have he := of_decide_eq_true hh.2
  have a := path_sound hp.1 t ih
  have b := path_sound hp.2 t ih
  rw [he] at a
  have eq : (r.mul p.factor).eval t = p.factor * r.eval t := eval_mul _ _ _
  exact a.trans (eq ▸ b.symm)

/-- Total successful certificates, with no UNRESOLVED branch. -/
def Complete (w : Weights) : Prop :=
  ∀ p n, 1 < n → n % 2 = 1 → ∃ r : Form, ∃ t : Nat, ∃ c : Certificate,
    r.eval t = n ∧ c.check w p r = true

private theorem comparison_one (p : Kind) : Comparison p 1 := by
  cases p with
  | triple =>
    constructor
    · intro _; exact ⟨5, rfl⟩
    · intro _; exact ⟨0, rfl⟩
  | five =>
    constructor
    · intro _; exact ⟨4, rfl⟩
    · intro _; exact ⟨0, rfl⟩

/-- Simultaneous strong induction; no clock or odd-count alignment is needed. -/
theorem comparisons_of_complete {w : Weights} (hw3 : 0 < w.triple)
    (hw5 : 0 < w.five) (hc : Complete w) :
    ∀ p n, 0 < n → Comparison p n := by
  have weights_pos (p : Kind) : 0 < w.get p := by
    cases p <;> assumption
  have all : ∀ rank, ∀ p n, w.get p*n = rank → 0<n → Comparison p n := by
    intro rank
    induction rank using Nat.strong_induction_on with
    | h rank ih =>
      intro p n he hn
      by_cases h1 : n = 1
      · simpa [h1] using comparison_one p
      by_cases even : n % 2 = 0
      · let m := n/2
        have hm : 0 < m := by dsimp [m]; omega
        have en : n = 2*m := by dsimp [m]; omega
        have hlt : w.get p*m < rank := by
          have small : m<n := by dsimp [m]; omega
          have hh := Nat.mul_lt_mul_of_pos_left small (weights_pos p)
          omega
        have sub := ih (w.get p*m) hlt p m rfl hm
        unfold Comparison at sub ⊢
        rw [en]
        have ex : p.factor*(2*m) = 2*(p.factor*m) := by grind
        exact (basin_twice m).trans (sub.trans (ex ▸ (basin_twice (p.factor*m)).symm))
      · have odd : n % 2 = 1 := by omega
        obtain ⟨r,t,c,er,ec⟩ := hc p n (by omega) odd
        rw [← er]
        apply certificate_sound ec t
        intro q u hu hsmall
        have hs : w.get q*u < rank := by rw [er] at hsmall; omega
        exact ih (w.get q*u) hs q u rfl hu
  intro p n hn
  exact all _ p n rfl hn

/-- A sufficient global closing theorem. Complete is an explicit open obligation. -/
theorem collatz_of_complete {w : Weights} (hw3 : 0 < w.triple)
    (hw5 : 0 < w.five) (hc : Complete w) : ∀ n, 0 < n → Basin n := by
  have all := comparisons_of_complete hw3 hw5 hc
  apply reverse_generates ⟨basin_twice, basin_odd, ?_⟩ (show Basin 1 from ⟨0,rfl⟩)
  intro n hn hb
  have positive : 0 < n := by omega
  exact (all .triple n positive).mpr hb

/-- A finite table records successful rules only; its validity is distinct from coverage. -/
structure Row where
  kind : Kind
  root : Form
  certificate : Certificate
  deriving Repr

def Row.check (w : Weights) (r : Row) := r.certificate.check w r.kind r.root

theorem table_row_sound {w : Weights} {rows : List Row} {r : Row}
    (h : rows.all (Row.check w) = true) (hr : r ∈ rows) (t : Nat)
    (ih : LowerHyp w r.kind r.root t) : Comparison r.kind (r.root.eval t) := by
  exact certificate_sound (List.all_eq_true.mp h r hr) t ih

end CollatzJoint
