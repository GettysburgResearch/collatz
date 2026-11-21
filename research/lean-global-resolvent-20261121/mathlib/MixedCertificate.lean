import Mathlib.Data.Multiset.DershowitzManna
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum

/-!
One well-founded order for ordinary certificate consumption and prefix replacement.
The order and its well-foundedness are Mathlib's Dershowitz--Manna order.
The all-state rule coverage required by `close_of_complete_rules` is an explicit
hypothesis; this file does not assert that Collatz supplies that coverage.
-/

namespace CollatzCertificateOrder

abbrev Bag := Multiset ℕ
abbrev Below := Multiset.IsDershowitzMannaLT (α := ℕ)

theorem below_wellFounded : WellFounded Below :=
  Multiset.wellFounded_isDershowitzMannaLT

theorem replace_prefix (old fresh tail : Bag) (hne : old ≠ 0)
    (h : ∀ y ∈ fresh, ∃ z ∈ old, y < z) :
    Below (fresh + tail) (old + tail) := by
  exact ⟨tail, fresh, old, hne, add_comm _ _, add_comm _ _, h⟩

theorem consume_prefix (old tail : Bag) (hne : old ≠ 0) :
    Below tail (old + tail) := by
  simpa using replace_prefix old 0 tail hne (by simp)

theorem replace_below_member (old fresh tail : Bag) (z : ℕ) (hz : z ∈ old)
    (h : ∀ y ∈ fresh, y < z) : Below (fresh + tail) (old + tail) := by
  apply replace_prefix old fresh tail
  · intro he; simp [he] at hz
  · intro y hy; exact ⟨z, hz, h y hy⟩

/-- Every child in a rule has a smaller complete certificate bag. -/
structure Rule {S : Type*} (measure : S → Bag) (goal : S → Prop) (s : S) where
  children : List S
  decrease : ∀ c ∈ children, Below (measure c) (measure s)
  sound : (∀ c ∈ children, goal c) → goal s

/-- The global coverage premise is deliberately visible, never supplied as an axiom. -/
theorem close_of_complete_rules {S : Type*} (measure : S → Bag) (goal : S → Prop)
    (coverage : ∀ s, Nonempty (Rule measure goal s)) : ∀ s, goal s := by
  have wf : WellFounded (fun a b : S => Below (measure a) (measure b)) :=
    InvImage.wf measure below_wellFounded
  intro s
  induction s using wf.induction with
  | h s ih =>
    obtain ⟨r⟩ := coverage s
    exact r.sound (fun c hc => ih c (r.decrease c hc))

def shortcut (n : ℕ) : ℕ := if n % 2 = 0 then n / 2 else (3 * n + 1) / 2

def orbit : ℕ → ℕ → ℕ
  | 0, n => n
  | k + 1, n => orbit k (shortcut n)

def Basin (n : ℕ) : Prop := ∃ k, orbit k n = 1

theorem orbit_add (a b n : ℕ) : orbit (a + b) n = orbit b (orbit a n) := by
  induction a generalizing n with
  | zero => simp [orbit]
  | succ a ih => simpa [Nat.succ_add, orbit] using ih (shortcut n)

theorem basin_of_orbit {n m k : ℕ} (he : orbit k n = m) (hm : Basin m) : Basin n := by
  obtain ⟨j, hj⟩ := hm
  exact ⟨k + j, by rw [orbit_add, he, hj]⟩

theorem basin_step (n : ℕ) : Basin (shortcut n) ↔ Basin n := by
  constructor
  · rintro ⟨k, hk⟩; exact ⟨k + 1, hk⟩
  · rintro ⟨k, hk⟩
    cases k with
    | zero =>
      have hn : n = 1 := hk
      subst n
      exact ⟨1, by decide⟩
    | succ k => exact ⟨k, hk⟩

theorem basin_orbit (k n : ℕ) : Basin (orbit k n) ↔ Basin n := by
  induction k generalizing n with
  | zero => rfl
  | succ k ih => exact (ih (shortcut n)).trans (basin_step n)

structure Affine where
  a : ℕ
  b : ℕ
  deriving DecidableEq, Repr

def Affine.eval (p : Affine) (t : ℕ) : ℕ := p.a * t + p.b

def StepCheck (p q : Affine) : Prop :=
  p.a % 2 = 0 ∧
    if p.b % 2 = 0 then 2 * q.a = p.a ∧ 2 * q.b = p.b
    else 2 * q.a = 3 * p.a ∧ 2 * q.b = 3 * p.b + 1

instance (p q : Affine) : Decidable (StepCheck p q) := inferInstanceAs
  (Decidable (p.a % 2 = 0 ∧
    if p.b % 2 = 0 then 2 * q.a = p.a ∧ 2 * q.b = p.b
    else 2 * q.a = 3 * p.a ∧ 2 * q.b = 3 * p.b + 1))

theorem stepCheck_sound {p q : Affine} (h : StepCheck p q) (t : ℕ) :
    shortcut (p.eval t) = q.eval t := by
  obtain ⟨ha, hs⟩ := h
  have hp : (p.eval t) % 2 = p.b % 2 := by
    simp [Affine.eval, Nat.add_mod, Nat.mul_mod, ha]
  by_cases hb : p.b % 2 = 0
  · obtain ⟨hqa, hqb⟩ := (ite_eq_left hb ▸ hs)
    have hn : p.eval t = 2 * q.eval t := by
      dsimp [Affine.eval]
      rw [← hqa, ← hqb]
      ring
    simp [shortcut, hn]
  · obtain ⟨hqa, hqb⟩ := (ite_eq_right hb ▸ hs)
    have hn : 3 * p.eval t + 1 = 2 * q.eval t := by
      dsimp [Affine.eval]
      calc
        3 * (p.a * t + p.b) + 1 = (3 * p.a) * t + (3 * p.b + 1) := by ring
        _ = 2 * q.a * t + 2 * q.b := by rw [← hqa, ← hqb]
        _ = 2 * (q.a * t + q.b) := by ring
    simp [shortcut, hp, hb, hn]

/-- The endpoint is excluded from the stored prefix. -/
def TraceCheck : List Affine → Affine → Prop
  | [], _ => True
  | [p], z => StepCheck p z
  | p :: q :: rest, z => StepCheck p q ∧ TraceCheck (q :: rest) z

instance (ps : List Affine) (z : Affine) : Decidable (TraceCheck ps z) := by
  induction ps with
  | nil => exact isTrue trivial
  | cons p ps ih =>
    cases ps with
    | nil => exact inferInstanceAs (Decidable (StepCheck p z))
    | cons q qs => exact inferInstanceAs (Decidable (StepCheck p q ∧ TraceCheck (q :: qs) z))

def start (ps : List Affine) (z : Affine) : Affine := ps.headD z

theorem traceCheck_sound (ps : List Affine) (z : Affine) (h : TraceCheck ps z) (t : ℕ) :
    orbit ps.length ((start ps z).eval t) = z.eval t := by
  induction ps with
  | nil => rfl
  | cons p ps ih =>
    cases ps with
    | nil => simpa [orbit, start] using stepCheck_sound h t
    | cons q qs =>
      have he := stepCheck_sound h.1 t
      simpa [orbit, start, he] using ih h.2

def evalBag (ps : List Affine) (t : ℕ) : Bag := ↑(ps.map (fun p => p.eval t))

def BoundCheck (ps : List Affine) (z : Affine) : Prop :=
  ∀ p ∈ ps, p.a ≤ z.a ∧ p.b < z.b

instance (ps : List Affine) (z : Affine) : Decidable (BoundCheck ps z) :=
  inferInstanceAs (Decidable (∀ p ∈ ps, p.a ≤ z.a ∧ p.b < z.b))

theorem boundCheck_sound {ps : List Affine} {z : Affine} (h : BoundCheck ps z) (t : ℕ) :
    ∀ y ∈ evalBag ps t, y < z.eval t := by
  intro y hy
  simp only [evalBag, Multiset.mem_coe, List.mem_map] at hy
  obtain ⟨p, hp, rfl⟩ := hy
  obtain ⟨ha, hb⟩ := h p hp
  exact Nat.add_lt_add_of_le_of_lt (Nat.mul_le_mul_right t ha) hb

/-- Any supplied common tail may be arbitrarily long and arbitrarily high. -/
theorem affine_replacement_decreases (old fresh : List Affine) (z : Affine)
    (hz : z ∈ old) (h : BoundCheck fresh z) (t : ℕ) (tail : Bag) :
    Below (evalBag fresh t + tail) (evalBag old t + tail) := by
  apply replace_below_member _ _ _ (z.eval t)
  · simp only [evalBag, Multiset.mem_coe, List.mem_map]
    exact ⟨z, hz, rfl⟩
  · exact boundCheck_sound h t


/-! Two infinite paired descent families from PR169. The new check establishes
that every inserted ordinary upper-prefix state lies below the original start,
so these length-increasing splices decrease the same certificate order as
ordinary prefix consumption. No finite-coverage claim is made. -/

def parentIndexA (t : ℕ) : ℕ := 1889568 * t + 1686382
def childIndexA (t : ℕ) : ℕ := 524288 * t + 467911
def aParentUpper : List Affine := [
  ⟨241864704, 215856897⟩,
  ⟨362797056, 323785346⟩,
  ⟨181398528, 161892673⟩,
  ⟨272097792, 242839010⟩,
  ⟨136048896, 121419505⟩,
  ⟨204073344, 182129258⟩,
  ⟨102036672, 91064629⟩,
  ⟨153055008, 136596944⟩,
  ⟨76527504, 68298472⟩,
  ⟨38263752, 34149236⟩,
  ⟨19131876, 17074618⟩]
def aChildUpper : List Affine := [
  ⟨67108864, 59892609⟩,
  ⟨100663296, 89838914⟩,
  ⟨50331648, 44919457⟩,
  ⟨75497472, 67379186⟩,
  ⟨37748736, 33689593⟩,
  ⟨56623104, 50534390⟩,
  ⟨28311552, 25267195⟩,
  ⟨42467328, 37900793⟩,
  ⟨63700992, 56851190⟩,
  ⟨31850496, 28425595⟩,
  ⟨47775744, 42638393⟩,
  ⟨71663616, 63957590⟩,
  ⟨35831808, 31978795⟩,
  ⟨53747712, 47968193⟩,
  ⟨80621568, 71952290⟩,
  ⟨40310784, 35976145⟩,
  ⟨60466176, 53964218⟩,
  ⟨30233088, 26982109⟩,
  ⟨45349632, 40473164⟩,
  ⟨22674816, 20236582⟩,
  ⟨11337408, 10118291⟩,
  ⟨17006112, 15177437⟩,
  ⟨25509168, 22766156⟩,
  ⟨12754584, 11383078⟩,
  ⟨6377292, 5691539⟩]
def aUpperEnd : Affine := ⟨9565938, 8537309⟩
def aChildLower : List Affine := [
  ⟨33554432, 29946305⟩,
  ⟨50331648, 44919458⟩,
  ⟨25165824, 22459729⟩,
  ⟨37748736, 33689594⟩,
  ⟨18874368, 16844797⟩,
  ⟨28311552, 25267196⟩,
  ⟨14155776, 12633598⟩,
  ⟨7077888, 6316799⟩,
  ⟨10616832, 9475199⟩,
  ⟨15925248, 14212799⟩,
  ⟨23887872, 21319199⟩,
  ⟨35831808, 31978799⟩,
  ⟨53747712, 47968199⟩,
  ⟨80621568, 71952299⟩]
def aLowerEnd : Affine := ⟨120932352, 107928449⟩

theorem aParentUpper_path (t : ℕ) :
    orbit 11 (128 * parentIndexA t + 1) = aUpperEnd.eval t := by
  have h := traceCheck_sound aParentUpper aUpperEnd (by decide) t
  have hi : 128 * parentIndexA t + 1 = (start aParentUpper aUpperEnd).eval t := by
    dsimp [start, aParentUpper, parentIndexA, Affine.eval]
    ring
  rw [hi]
  exact h

theorem aChildUpper_path (t : ℕ) :
    orbit 25 (128 * childIndexA t + 1) = aUpperEnd.eval t := by
  have h := traceCheck_sound aChildUpper aUpperEnd (by decide) t
  have hi : 128 * childIndexA t + 1 = (start aChildUpper aUpperEnd).eval t := by
    dsimp [start, aChildUpper, childIndexA, Affine.eval]
    ring
  rw [hi]
  exact h

theorem aChildLower_path (t : ℕ) :
    orbit 14 (64 * childIndexA t + 1) = 64 * parentIndexA t + 1 := by
  have h := traceCheck_sound aChildLower aLowerEnd (by decide) t
  have hi : 64 * childIndexA t + 1 = (start aChildLower aLowerEnd).eval t := by
    dsimp [start, aChildLower, childIndexA, Affine.eval]
    ring
  have he : aLowerEnd.eval t = 64 * parentIndexA t + 1 := by
    dsimp [aLowerEnd, parentIndexA, Affine.eval]
    ring
  rw [hi, ← he]
  exact h

theorem a_source_certificate_decreases (t : ℕ) (tail : Bag) :
    Below (evalBag aChildUpper t + tail) (evalBag aParentUpper t + tail) := by
  apply affine_replacement_decreases _ _ (aParentUpper.headD aUpperEnd) _ _ t tail
  · decide
  · decide

theorem a_paired_closure (t : ℕ)
    (child : Basin (128 * childIndexA t + 1) → Basin (64 * childIndexA t + 1)) :
    Basin (128 * parentIndexA t + 1) → Basin (64 * parentIndexA t + 1) := by
  intro hparent
  have he : Basin (aUpperEnd.eval t) := by
    rw [← aParentUpper_path t]
    exact (basin_orbit _ _).mpr hparent
  have hc : Basin (128 * childIndexA t + 1) := by
    exact basin_of_orbit (aChildUpper_path t) he
  have hl := (basin_orbit 14 (64 * childIndexA t + 1)).mpr (child hc)
  rwa [aChildLower_path t] at hl

def parentIndexB (t : ℕ) : ℕ := 1889568 * t + 1196494
def childIndexB (t : ℕ) : ℕ := 1048576 * t + 663969
def bParentUpper : List Affine := [
  ⟨241864704, 153151233⟩,
  ⟨362797056, 229726850⟩,
  ⟨181398528, 114863425⟩,
  ⟨272097792, 172295138⟩,
  ⟨136048896, 86147569⟩,
  ⟨204073344, 129221354⟩,
  ⟨102036672, 64610677⟩,
  ⟨153055008, 96916016⟩,
  ⟨76527504, 48458008⟩,
  ⟨38263752, 24229004⟩,
  ⟨19131876, 12114502⟩]
def bChildUpper : List Affine := [
  ⟨134217728, 84988033⟩,
  ⟨201326592, 127482050⟩,
  ⟨100663296, 63741025⟩,
  ⟨150994944, 95611538⟩,
  ⟨75497472, 47805769⟩,
  ⟨113246208, 71708654⟩,
  ⟨56623104, 35854327⟩,
  ⟨84934656, 53781491⟩,
  ⟨127401984, 80672237⟩,
  ⟨191102976, 121008356⟩,
  ⟨95551488, 60504178⟩,
  ⟨47775744, 30252089⟩,
  ⟨71663616, 45378134⟩,
  ⟨35831808, 22689067⟩,
  ⟨53747712, 34033601⟩,
  ⟨80621568, 51050402⟩,
  ⟨40310784, 25525201⟩,
  ⟨60466176, 38287802⟩,
  ⟨30233088, 19143901⟩,
  ⟨45349632, 28715852⟩,
  ⟨22674816, 14357926⟩,
  ⟨11337408, 7178963⟩,
  ⟨17006112, 10768445⟩,
  ⟨25509168, 16152668⟩,
  ⟨12754584, 8076334⟩,
  ⟨6377292, 4038167⟩]
def bUpperEnd : Affine := ⟨9565938, 6057251⟩
def bChildLower : List Affine := [
  ⟨67108864, 42494017⟩,
  ⟨100663296, 63741026⟩,
  ⟨50331648, 31870513⟩,
  ⟨75497472, 47805770⟩,
  ⟨37748736, 23902885⟩,
  ⟨56623104, 35854328⟩,
  ⟨28311552, 17927164⟩,
  ⟨14155776, 8963582⟩,
  ⟨7077888, 4481791⟩,
  ⟨10616832, 6722687⟩,
  ⟨15925248, 10084031⟩,
  ⟨23887872, 15126047⟩,
  ⟨35831808, 22689071⟩,
  ⟨53747712, 34033607⟩,
  ⟨80621568, 51050411⟩]
def bLowerEnd : Affine := ⟨120932352, 76575617⟩

theorem bParentUpper_path (t : ℕ) :
    orbit 11 (128 * parentIndexB t + 1) = bUpperEnd.eval t := by
  have h := traceCheck_sound bParentUpper bUpperEnd (by decide) t
  have hi : 128 * parentIndexB t + 1 = (start bParentUpper bUpperEnd).eval t := by
    dsimp [start, bParentUpper, parentIndexB, Affine.eval]
    ring
  rw [hi]
  exact h

theorem bChildUpper_path (t : ℕ) :
    orbit 26 (128 * childIndexB t + 1) = bUpperEnd.eval t := by
  have h := traceCheck_sound bChildUpper bUpperEnd (by decide) t
  have hi : 128 * childIndexB t + 1 = (start bChildUpper bUpperEnd).eval t := by
    dsimp [start, bChildUpper, childIndexB, Affine.eval]
    ring
  rw [hi]
  exact h

theorem bChildLower_path (t : ℕ) :
    orbit 15 (64 * childIndexB t + 1) = 64 * parentIndexB t + 1 := by
  have h := traceCheck_sound bChildLower bLowerEnd (by decide) t
  have hi : 64 * childIndexB t + 1 = (start bChildLower bLowerEnd).eval t := by
    dsimp [start, bChildLower, childIndexB, Affine.eval]
    ring
  have he : bLowerEnd.eval t = 64 * parentIndexB t + 1 := by
    dsimp [bLowerEnd, parentIndexB, Affine.eval]
    ring
  rw [hi, ← he]
  exact h

theorem b_source_certificate_decreases (t : ℕ) (tail : Bag) :
    Below (evalBag bChildUpper t + tail) (evalBag bParentUpper t + tail) := by
  apply affine_replacement_decreases _ _ (bParentUpper.headD bUpperEnd) _ _ t tail
  · decide
  · decide

theorem b_paired_closure (t : ℕ)
    (child : Basin (128 * childIndexB t + 1) → Basin (64 * childIndexB t + 1)) :
    Basin (128 * parentIndexB t + 1) → Basin (64 * parentIndexB t + 1) := by
  intro hparent
  have he : Basin (bUpperEnd.eval t) := by
    rw [← bParentUpper_path t]
    exact (basin_orbit _ _).mpr hparent
  have hc : Basin (128 * childIndexB t + 1) := by
    exact basin_of_orbit (bChildUpper_path t) he
  have hl := (basin_orbit 15 (64 * childIndexB t + 1)).mpr (child hc)
  rwa [bChildLower_path t] at hl

end CollatzCertificateOrder

#print axioms CollatzCertificateOrder.close_of_complete_rules
#print axioms CollatzCertificateOrder.consume_prefix
#print axioms CollatzCertificateOrder.a_source_certificate_decreases
#print axioms CollatzCertificateOrder.b_source_certificate_decreases
#print axioms CollatzCertificateOrder.a_paired_closure
#print axioms CollatzCertificateOrder.b_paired_closure
