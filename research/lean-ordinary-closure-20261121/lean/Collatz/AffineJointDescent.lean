/- Simultaneous ordinary comparisons with a subtractive affine target.
   A checked row proves an implication from strictly smaller active queries.
   A global conclusion additionally requires a total successful cover. -/
import Collatz.Closure
open CollatzReverseBasin CollatzClosure

namespace CollatzAffineJoint

inductive Kind where
  | triple | five | psi
  deriving DecidableEq, Repr

def Kind.target : Kind → Nat → Nat
  | .triple, n => 3*n
  | .five, n => 5*n
  | .psi, n => 2*n-1

structure Weights where
  triple : Nat
  five : Nat
  psi : Nat
  deriving Repr

def Weights.get (w : Weights) : Kind → Nat
  | .triple => w.triple
  | .five => w.five
  | .psi => w.psi

structure Form where
  a : Nat
  b : Nat
  deriving DecidableEq, Repr

def Form.eval (f : Form) (t : Nat) : Nat := f.a*t+f.b

def Form.mul (q : Nat) (f : Form) : Form := ⟨q*f.a,q*f.b⟩

def Form.target (p : Kind) (f : Form) : Form :=
  match p with
  | .triple => f.mul 3
  | .five => f.mul 5
  | .psi => ⟨2*f.a,2*f.b-1⟩

theorem eval_mul (q : Nat) (f : Form) (t : Nat) :
    (f.mul q).eval t=q*f.eval t := by
  simp only [Form.mul, Form.eval]
  grind

/-- Positivity of the constant term is essential for the affine subtraction.
It ensures that truncated natural subtraction never clips a source lift. -/
theorem eval_target (p : Kind) (f : Form) (t : Nat) (hb : 0<f.b) :
    (f.target p).eval t=p.target (f.eval t) := by
  cases p with
  | triple => exact eval_mul 3 f t
  | five => exact eval_mul 5 f t
  | psi =>
      change (2*f.a)*t+(2*f.b-1)=2*(f.a*t+f.b)-1
      have he : 2*(f.a*t+f.b)=(2*f.a)*t+2*f.b := by grind
      omega

def Comparison (p : Kind) (n : Nat) : Prop :=
  Basin n ↔ Basin (p.target n)

def Lower (w : Weights) (p : Kind) (r : Form) (q : Kind) (u : Form) : Prop :=
  0<u.b ∧ w.get q*u.a≤w.get p*r.a ∧ w.get q*u.b<w.get p*r.b

instance (w : Weights) (p : Kind) (r : Form) (q : Kind) (u : Form) :
    Decidable (Lower w p r q u) := inferInstanceAs (Decidable (_ ∧ _ ∧ _))

theorem lower_rank {w : Weights} {p : Kind} {r : Form} {q : Kind} {u : Form}
    (h : Lower w p r q u) (t : Nat) :
    0<u.eval t ∧ w.get q*u.eval t<w.get p*r.eval t := by
  obtain ⟨hb,ha,hc⟩ := h
  have hm := Nat.mul_le_mul_right t ha
  simp only [Form.eval]
  constructor
  · omega
  · have e1 : w.get q*(u.a*t+u.b)=(w.get q*u.a)*t+w.get q*u.b := by grind
    have e2 : w.get p*(r.a*t+r.b)=(w.get p*r.a)*t+w.get p*r.b := by grind
    omega

inductive Step where
  | double (forward : Bool) (dest : Form)
  | odd (forward : Bool) (dest : Form)
  | query (forward : Bool) (kind : Kind) (dest : Form)
  deriving Repr

def Step.dest : Step → Form
  | .double _ d | .odd _ d | .query _ _ d => d

def OddLink (s d : Form) : Prop :=
  s.a%2=0 ∧ s.b%2=1 ∧ 3*s.a=2*d.a ∧ 3*s.b+1=2*d.b

instance (s d : Form) : Decidable (OddLink s d) :=
  inferInstanceAs (Decidable (_ ∧ _ ∧ _ ∧ _))

/-- Queries may use only an explicitly active comparison kind. -/
def Step.Valid (w : Weights) (kinds : List Kind) (p : Kind) (r s : Form) : Step → Prop
  | .double true d => d=s.mul 2
  | .double false d => s=d.mul 2
  | .odd true d => OddLink s d
  | .odd false d => OddLink d s
  | .query true q d => q∈kinds ∧ d=s.target q ∧ Lower w p r q s
  | .query false q d => q∈kinds ∧ s=d.target q ∧ Lower w p r q d

instance (w : Weights) (kinds : List Kind) (p : Kind) (r s : Form) (e : Step) :
    Decidable (e.Valid w kinds p r s) := by
  cases e with
  | double f d => cases f <;> simp only [Step.Valid] <;> infer_instance
  | odd f d => cases f <;> simp only [Step.Valid] <;> infer_instance
  | query f q d => cases f <;> simp only [Step.Valid] <;> infer_instance

private theorem oddLink_sound {s d : Form} (h : OddLink s d) (t : Nat) :
    Basin (s.eval t) ↔ Basin (d.eval t) := by
  obtain ⟨ha,hb,hc,hd⟩ := h
  have par : s.eval t%2=1 := by
    simp [Form.eval,Nat.add_mod,Nat.mul_mod,ha,hb]
  have eq : 3*s.eval t+1=2*d.eval t := by
    simp only [Form.eval]
    calc 3*(s.a*t+s.b)+1=(3*s.a)*t+(3*s.b+1) := by grind
         _=(2*d.a)*t+2*d.b := by rw [hc,hd]
         _=2*(d.a*t+d.b) := by grind
  exact (basin_odd _ par).symm.trans (eq ▸ basin_twice (d.eval t))

def LowerHyp (w : Weights) (kinds : List Kind) (p : Kind) (r : Form) (t : Nat) : Prop :=
  ∀ q, q∈kinds → ∀ u, 0<u → w.get q*u<w.get p*r.eval t → Comparison q u

theorem step_sound {w : Weights} {kinds : List Kind} {p : Kind} {r s : Form} {e : Step}
    (h : e.Valid w kinds p r s) (t : Nat) (ih : LowerHyp w kinds p r t) :
    Basin (s.eval t) ↔ Basin (e.dest.eval t) := by
  cases e with
  | double forward d =>
    cases forward with
    | false =>
      change s=d.mul 2 at h
      simp only [Step.dest,h,eval_mul]
      exact basin_twice _
    | true =>
      change d=s.mul 2 at h
      simp only [Step.dest,h,eval_mul]
      exact (basin_twice _).symm
  | odd forward d =>
    cases forward with
    | false => exact (oddLink_sound h t).symm
    | true => exact oddLink_sound h t
  | query forward q d =>
    cases forward with
    | false =>
      obtain ⟨hq,he,hl⟩ := h
      have hr := lower_rank hl t
      have hc := ih q hq (d.eval t) hr.1 hr.2
      change Basin (s.eval t) ↔ Basin (d.eval t)
      rw [he,eval_target q d t hl.1]
      exact hc.symm
    | true =>
      obtain ⟨hq,he,hl⟩ := h
      have hr := lower_rank hl t
      have hc := ih q hq (s.eval t) hr.1 hr.2
      change Basin (s.eval t) ↔ Basin (d.eval t)
      rw [he,eval_target q s t hl.1]
      exact hc

def endpoint (s : Form) : List Step → Form
  | [] => s
  | e::es => endpoint e.dest es

def validPath (w : Weights) (kinds : List Kind) (p : Kind) (r s : Form) : List Step → Bool
  | [] => true
  | e::es => decide (e.Valid w kinds p r s) && validPath w kinds p r e.dest es

theorem path_sound {w : Weights} {kinds : List Kind} {p : Kind} {r s : Form} {es : List Step}
    (h : validPath w kinds p r s es=true) (t : Nat) (ih : LowerHyp w kinds p r t) :
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

def Certificate.check (w : Weights) (kinds : List Kind) (p : Kind) (r : Form)
    (c : Certificate) : Bool :=
  decide (0<r.b) &&
  (validPath w kinds p r r c.left &&
   (validPath w kinds p r (r.target p) c.right &&
    decide (endpoint r c.left=endpoint (r.target p) c.right)))

theorem certificate_sound {w : Weights} {kinds : List Kind} {p : Kind} {r : Form}
    {c : Certificate} (h : c.check w kinds p r=true) (t : Nat)
    (ih : LowerHyp w kinds p r t) : Comparison p (r.eval t) := by
  have h0 := Bool.and_eq_true_iff.mp h
  have h1 := Bool.and_eq_true_iff.mp h0.2
  have h2 := Bool.and_eq_true_iff.mp h1.2
  have hb : 0<r.b := of_decide_eq_true h0.1
  have he := of_decide_eq_true h2.2
  have a := path_sound h1.1 t ih
  have b := path_sound h2.1 t ih
  rw [he] at a
  have eq : (r.target p).eval t=p.target (r.eval t) := eval_target p r t hb
  exact a.trans (eq ▸ b.symm)

/-- Coverage of EVERY positive source above one, including even psi sources.
The active list can be `[triple, psi]` without any five certificates. -/
def Complete (w : Weights) (kinds : List Kind) : Prop :=
  ∀ p, p∈kinds → ∀ n, 1<n → ∃ r : Form, ∃ t : Nat, ∃ c : Certificate,
    r.eval t=n ∧ c.check w kinds p r=true

private theorem comparison_one (p : Kind) : Comparison p 1 := by
  cases p with
  | triple =>
    constructor
    · intro _; exact ⟨5,rfl⟩
    · intro _; exact ⟨0,rfl⟩
  | five =>
    constructor
    · intro _; exact ⟨4,rfl⟩
    · intro _; exact ⟨0,rfl⟩
  | psi => exact Iff.rfl

/-- The strict query guard alone establishes well-founded induction. No parity
normalization, implicit unresolved branch, or positive-drift premise occurs. -/
theorem comparisons_of_complete {w : Weights} {kinds : List Kind}
    (hc : Complete w kinds) :
    ∀ p, p∈kinds → ∀ n, 0<n → Comparison p n := by
  have all : ∀ rank, ∀ p, p∈kinds → ∀ n,
      w.get p*n=rank → 0<n → Comparison p n := by
    intro rank
    induction rank using Nat.strong_induction_on with
    | h rank ih =>
      intro p hp n he hn
      by_cases h1 : n=1
      · simpa [h1] using comparison_one p
      obtain ⟨r,t,c,er,ec⟩ := hc p hp n (by omega)
      rw [← er]
      apply certificate_sound ec t
      intro q hq u hu hsmall
      have hs : w.get q*u<rank := by rw [er] at hsmall; omega
      exact ih (w.get q*u) hs q hq u rfl hu
  intro p hp n hn
  exact all _ p hp n rfl hn

/-- A complete active triple family implies Collatz. This theorem does not
assert existence of such a complete family. -/
theorem collatz_of_complete_triple {w : Weights} {kinds : List Kind}
    (h3 : Kind.triple∈kinds) (hc : Complete w kinds) : ∀ n, 0<n → Basin n := by
  have all := comparisons_of_complete hc
  apply reverse_generates ⟨basin_twice,basin_odd,?_⟩ (show Basin 1 from ⟨0,rfl⟩)
  intro n hn hb
  have positive : 0<n := by omega
  exact (all .triple h3 n positive).mpr hb

/-- A complete active psi family also implies Collatz through the already
proved ordinary psi criterion. -/
theorem collatz_of_complete_psi {w : Weights} {kinds : List Kind}
    (hp : Kind.psi∈kinds) (hc : Complete w kinds) : ∀ n, 0<n → Basin n := by
  apply collatz_iff_psi_forward.mpr
  intro n hn hb
  exact (comparisons_of_complete hc .psi hp n hn).mp hb

structure Row where
  kind : Kind
  root : Form
  certificate : Certificate
  deriving Repr

def Row.check (w : Weights) (kinds : List Kind) (r : Row) : Bool :=
  decide (r.kind∈kinds) && r.certificate.check w kinds r.kind r.root

theorem table_row_sound {w : Weights} {kinds : List Kind} {rows : List Row} {r : Row}
    (h : rows.all (Row.check w kinds)=true) (hr : r∈rows) (t : Nat)
    (ih : LowerHyp w kinds r.kind r.root t) : Comparison r.kind (r.root.eval t) := by
  have hh := Bool.and_eq_true_iff.mp (List.all_eq_true.mp h r hr)
  exact certificate_sound hh.2 t ih

/-- The even-psi rewrite is an actual ordinary identity. Its psi query is at
the larger input `3*m`; this lemma does not certify a decrease for linear rank. -/
theorem psi_even_of_triple_and_larger_psi (m : Nat) (hm : 0<m)
    (h3 : Comparison .triple m) (hp : Comparison .psi (3*m)) :
    Comparison .psi (2*m) := by
  have he := basin_psi (2*m) (by omega)
  have eq : 3*(2*m)=2*(3*m) := by omega
  rw [eq] at he
  exact (basin_twice m).trans (h3.trans (hp.trans he.symm))

/-- At an odd source, the triple comparison is exactly the psi comparison at
its next shortcut value. The latter value may be even; it must not be
normalized away in a full-source psi cover. -/
theorem odd_triple_iff_psi_successor (n : Nat) (hn : n%2=1) :
    Comparison .triple n ↔ Comparison .psi ((3*n+1)/2) := by
  let a := (3*n+1)/2
  have ha : 2*a=3*n+1 := by dsimp [a]; omega
  have hb : Basin n ↔ Basin a :=
    (basin_odd n hn).symm.trans (ha.symm ▸ basin_twice a)
  have he : 2*a-1=3*n := by omega
  change (Basin n ↔ Basin (3*n)) ↔ (Basin a ↔ Basin (2*a-1))
  rw [he]
  constructor
  · intro h; exact hb.symm.trans h
  · intro h; exact hb.trans h

/-- If a psi rank on a number with odd part `u` and two-adic exponent `k` is
`4^k*u`, the rewrite from `2*m` to `3*m` has strict ratio three quarters.
This algebraic decrease is not asserted to handle the separate triple query. -/
theorem valuation_rank_even_step (k u : Nat) (hu : 0<u) :
    3*(4^k*u)<4^(k+1)*u := by
  have hp : 0<4^k := Nat.pow_pos (by decide)
  have hv : 0<4^k*u := Nat.mul_pos hp hu
  have he : 4^(k+1)*u=4*(4^k*u) := by
    simp [Nat.pow_succ,Nat.mul_comm,Nat.mul_left_comm]
  omega

/-- Ordinary exchange on both arms transports the psi comparison exactly.
This is an equivalence, not an assertion that either side has been proved. -/
theorem psi_exchange (t : Nat) :
    Comparison .psi (4*t+1) ↔ Comparison .psi (3*t+1) := by
  have h1 := basin_exch (4*t+1) (3*t+1) t rfl rfl
  have h2 := basin_exch (8*t+1) (6*t+1) (2*t) (by omega) (by omega)
  have e1 : 2*(4*t+1)-1=8*t+1 := by omega
  have e2 : 2*(3*t+1)-1=6*t+1 := by omega
  simp only [Comparison,Kind.target,e1,e2]
  constructor
  · intro h; exact h1.symm.trans (h.trans h2)
  · intro h; exact h1.trans (h.trans h2.symm)

/-- The even-source and odd-source rules can be exact inverses on this family. -/
theorem reciprocal_even_psi_family (t : Nat) :
    Comparison .psi (6*t+4) ↔ Comparison .psi (8*t+5) := by
  have h := (psi_exchange (2*t+1)).symm
  have e1 : 3*(2*t+1)+1=6*t+4 := by omega
  have e2 : 4*(2*t+1)+1=8*t+5 := by omega
  simpa only [e1,e2] using h

/-- No single natural rank certifies both selected directions of this exact
reciprocal family. Other possible paths are not excluded. -/
theorem no_rank_for_both_reciprocal_arcs (rank : Nat → Nat) (t : Nat) :
    ¬ (rank (8*t+5)<rank (6*t+4) ∧ rank (6*t+4)<rank (8*t+5)) := by
  omega

#print axioms collatz_of_complete_triple
#print axioms collatz_of_complete_psi
#print axioms psi_even_of_triple_and_larger_psi
#print axioms odd_triple_iff_psi_successor
#print axioms valuation_rank_even_step
#print axioms reciprocal_even_psi_family
#print axioms no_rank_for_both_reciprocal_arcs

end CollatzAffineJoint
