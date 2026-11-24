module

public import TernaryItinerary
import all TernaryItinerary

public section

/-! Fixed-arity positive rows and the minimum odd input on a genuine shortcut
path. The asymptotic use of Evertse is a written theorem. -/
namespace Collatz.LiteralCarry

open Collatz.Itinerary
set_option autoImplicit false

def chooseTerm (selected : Bool) (v : Nat) := if selected then v else 0

/-- In a positive three-summand decomposition of a fourth coordinate the only
zero subsums of the signed row are the empty and complete subsums. -/
theorem no_proper_subsum {u a b c : Nat} (row : u = a + b + c)
    (ha : 0 < a) (hb : 0 < b) (hc : 0 < c) (e i j k : Bool)
    (zero : chooseTerm e u = chooseTerm i a + chooseTerm j b + chooseTerm k c) :
    e = i ∧ i = j ∧ j = k := by
  cases e <;> cases i <;> cases j <;> cases k <;>
    simp_all [chooseTerm] <;> omega

private theorem step_unit {z : Nat} (h : z%3 ≠ 0 ∨ z%2=1) : step z%3 ≠ 0 := by
  by_cases e : z%2=0
  · have eq : 2*step z=z := by simp [step,e]; omega
    omega
  · have eq : 2*step z=3*z+1 := by simp [step,e]; omega
    omega

private theorem run_unit (l z : Nat) (h : z%3 ≠ 0) : run l z % 3 ≠ 0 := by
  induction l generalizing z with
  | zero => simpa [run] using h
  | succ l ih => exact ih (step z) (step_unit (Or.inl h))

/-- The genuine endpoint is a ternary unit as soon as the prefix contains
an odd input. -/
theorem unit_after_odd (l z : Nat) (ho : 0 < (readMarks l z).length) :
    run l z % 3 ≠ 0 := by
  induction l generalizing z with
  | zero => simp [readMarks] at ho
  | succ l ih =>
    by_cases odd : z%2=1
    · exact run_unit l (step z) (step_unit (Or.inr odd))
    · exact ih (step z) (by simpa [readMarks, odd] using ho)

/-- All common content of the original three-coordinate row divides its
fixed positive source once an odd branch has occurred. -/
theorem original_content {g l p n : Nat} (odd : 0 < (readMarks l n).length)
    (hg : g ∣ 2^l*run l n) (hn : g ∣ 3^p*n) : g ∣ n := by
  have unit := unit_after_odd l n odd
  have unit' : (run l n).Coprime 3 := by
    change (run l n).gcd 3 = 1
    rw [Nat.gcd_comm, Nat.gcd_rec]
    have r : run l n%3=1 ∨ run l n%3=2 := by omega
    rcases r with r|r <;> rw [r] <;> decide
  have cop : (2^l*run l n).Coprime (3^p) := Nat.Coprime.pow_right p
    (Nat.Coprime.mul_left (Nat.Coprime.pow_left l (by decide : Nat.Coprime 2 3)) unit')
  exact (Nat.Coprime.coprime_dvd_left hg cop).dvd_of_dvd_mul_left hn

/-- Every common divisor of the left power of two and the displaced coordinate
already divides the unscaled displacement. -/
theorem content_dvd_displacement {g l j t : Nat} (hg : g ∣ 2^l)
    (ht : g ∣ 3^j*t) : g ∣ t := by
  have cop : (2^l).Coprime (3^j) :=
    Nat.Coprime.pow_right j (Nat.Coprime.pow_left l (by decide : Nat.Coprime 2 3))
  exact (Nat.Coprime.coprime_dvd_left hg cop).dvd_of_dvd_mul_left ht

/-- The primitive height pays the full ternary multiplier for every odd divisor
of the displacement, with all its prime multiplicities. -/
theorem primitive_height_gain {g l j t x c d : Nat} (row : 2^l = 3^j*t + x + c)
    (gpos : 0 < g) (tpos : 0 < t) (hg : g ∣ 2^l) (ht : g ∣ 3^j*t)
    (hd : d ∣ t) (hodd : d.Coprime 2) : 3^j*d ≤ 2^l/g := by
  have cop : g.Coprime d := Nat.Coprime.coprime_dvd_left hg
    (Nat.Coprime.pow_left l hodd.symm)
  have large := Nat.le_of_dvd tpos
    (cop.mul_dvd_of_dvd_of_dvd (content_dvd_displacement hg ht) hd)
  apply (Nat.le_div_iff_mul_le gpos).2
  calc
    3^j*d*g = 3^j*(g*d) := by ac_rfl
    _ ≤ 3^j*t := Nat.mul_le_mul_left _ large
    _ ≤ 2^l := by omega

/-- A physical word with fixed length, odd count, carry and target has at most
one displacement from the given initial prefix. -/
theorem displacement_unique {l p h x c r t u : Nat}
    (ht : 2^l*r = 3^h*x+c+3^(p+h)*t)
    (hu : 2^l*r = 3^h*x+c+3^(p+h)*u) : t = u := by
  apply Nat.eq_of_mul_eq_mul_left (Nat.pow_pos (by decide : 0 < 3))
  exact Nat.add_left_cancel (ht.symm.trans hu)

/-- Lower bound on the actual odd inputs among the next `l` shortcut steps. -/
def OddFloor (M l z : Nat) : Prop :=
  ∀ i, i < l → run i z % 2 = 1 → M ≤ run i z

/-- Integer form of the correction-product bound prior to the terminal state. -/
theorem physical_floor_bound (l M z : Nat) (floor : OddFloor M l z) :
    2^l * M^(readMarks l z).length * run l z ≤
      (3*M+1)^(readMarks l z).length * z := by
  induction l generalizing z with
  | zero => simp [readMarks, run]
  | succ l ih =>
    have next : OddFloor M l (step z) := by
      intro i hi ho
      exact floor (i+1) (by omega) (by simpa [run] using ho)
    have tail := ih (step z) next
    let h := (readMarks l (step z)).length
    change 2^l * M^h * run l (step z) ≤ (3*M+1)^h * step z at tail
    by_cases odd : z%2=1
    · have low : M ≤ z := floor 0 (by omega) (by simpa [run] using odd)
      have edge : 2*step z = 3*z+1 := by
        have ne : z%2 ≠ 0 := by omega
        simp [step,ne]; omega
      have factor : M*(3*z+1) ≤ (3*M+1)*z := by
        rw [Nat.mul_add, Nat.add_mul, Nat.mul_one, Nat.one_mul]
        rw [show M*(3*z)=3*M*z by ac_rfl]; omega
      simp only [readMarks, odd, ite_true, List.length_cons, run]
      change 2^(l+1)*M^(h+1)*run l (step z) ≤ (3*M+1)^(h+1)*z
      calc
        2^(l+1)*M^(h+1)*run l (step z) = 2*M*(2^l*M^h*run l (step z)) := by
          simp only [Nat.pow_succ]; ac_rfl
        _ ≤ 2*M*((3*M+1)^h*step z) := Nat.mul_le_mul_left _ tail
        _ = (3*M+1)^h*(M*(3*z+1)) := by rw [← edge]; ac_rfl
        _ ≤ (3*M+1)^h*((3*M+1)*z) := Nat.mul_le_mul_left _ factor
        _ = (3*M+1)^(h+1)*z := by rw [Nat.pow_succ]; ac_rfl
    · have even : z%2=0 := by omega
      have edge : 2*step z = z := by simp [step,even]; omega
      simp only [readMarks, odd, ite_false, run]
      change 2^(l+1)*M^h*run l (step z) ≤ (3*M+1)^h*z
      calc
        2^(l+1)*M^h*run l (step z) = 2*(2^l*M^h*run l (step z)) := by
          rw [Nat.pow_succ]; ac_rfl
        _ ≤ 2*((3*M+1)^h*step z) := Nat.mul_le_mul_left _ tail
        _ = (3*M+1)^h*(2*step z) := by ac_rfl
        _ = (3*M+1)^h*z := congrArg (fun a => (3*M+1)^h*a) edge

/-- The actual binary input sequence, in forward chronological order. -/
def parityWord : Nat → Nat → List Nat
  | 0, _ => []
  | l+1, z => z%2 :: parityWord l (step z)

/-- Agreeing on all the next `l` bits forces a full power of two in the
source difference, even when later physical values leave the initial interval. -/
theorem agreement_dvd (l z d : Nat) (h : parityWord l (z+d)=parityWord l z) :
    2^l ∣ d := by
  induction l generalizing z d with
  | zero => simp
  | succ l ih =>
    have hh := List.cons.inj (show (z+d)%2 :: parityWord l (step (z+d)) =
        z%2 :: parityWord l (step z) from h)
    let e := d/2
    have de : d=2*e := by dsimp [e]; omega
    have he : 2^l ∣ e := by
      by_cases even : z%2=0
      · have even' : (z+d)%2=0 := hh.1.trans even
        have eq : step (z+d)=step z+e := by simp [step,even,even']; omega
        exact ih (step z) e (eq ▸ hh.2)
      · have even' : (z+d)%2 ≠ 0 := by omega
        have eq : step (z+d)=step z+3*e := by simp [step,even,even']; omega
        have full := ih (step z) (3*e) (eq ▸ hh.2)
        exact (Nat.Coprime.pow_left l (by decide : Nat.Coprime 2 3)).dvd_of_dvd_mul_left full
    obtain ⟨q, hq⟩ := he
    exact ⟨q, by rw [de,hq,Nat.pow_succ]; ac_rfl⟩

/-- Distinct physical starting values in the first binary block have distinct
length-`l` future parity words. -/
theorem low_words_injective (l z w : Nat) (hz : z < 2^l) (hw : w < 2^l)
    (eq : parityWord l z = parityWord l w) : z=w := by
  have ordered (a b : Nat) (hb : b < 2^l) (lt : a < b)
      (same : parityWord l a = parityWord l b) : False := by
    have split : a+(b-a)=b := by omega
    have div := agreement_dvd l a (b-a) (by simpa [split] using same.symm)
    have := Nat.le_of_dvd (by omega : 0 < b-a) div
    omega
  by_cases lt : z<w
  · exact (ordered z w hw lt eq).elim
  · by_cases gt : w<z
    · exact (ordered w z hz gt eq.symm).elim
    · omega

#print axioms agreement_dvd
#print axioms low_words_injective
#print axioms no_proper_subsum
#print axioms unit_after_odd
#print axioms original_content
#print axioms content_dvd_displacement
#print axioms primitive_height_gain
#print axioms displacement_unique
#print axioms physical_floor_bound
end Collatz.LiteralCarry
