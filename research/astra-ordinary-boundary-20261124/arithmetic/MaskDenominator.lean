import Std

/-! Complete-carry congruences for discrepancy masks.  Integer representatives
avoid a field assumption on a possibly composite cycle modulus. -/
namespace MaskDenominator

def Cong (d x y : Int) : Prop := d ∣ x - y

private theorem refl (d x : Int) : Cong d x x := by simp [Cong]

private theorem times {d x y v w : Int} (h : Cong d x y) (k : Cong d v w) :
    Cong d (x*v) (y*w) := by
  obtain ⟨a, ha⟩ := h
  obtain ⟨b, hb⟩ := k
  exact ⟨a*v+y*b, by grind⟩

private theorem power {d x y : Int} (h : Cong d x y) (n : Nat) :
    Cong d (x^n) (y^n) := by
  induction n with
  | zero => simp [Cong]
  | succ n ih => simpa [Int.pow_succ] using times ih h

structure Atom where
  index : Nat
  prefixClock : Nat
  level : Nat

def mask (z : Int) (atoms : List Atom) : Int :=
  (atoms.map (fun a => z ^ a.level)).sum

def carry (last : Nat) (atoms : List Atom) : Int :=
  (atoms.map (fun a => (3:Int)^(last-a.index) * 2^a.prefixClock)).sum

/-- No common denominator, prime modulus, or bound on the number of summands
is assumed. The pointwise level equation allows the same integer shift at
every atom and includes negative unshifted levels. -/
theorem mask_carry {d z : Int} {p A K last : Nat} (xs : List Atom)
    (hp : Cong d (z^p) 2) (hA : Cong d (z^A) 3)
    (h : ∀ a ∈ xs, a.index ≤ last ∧ a.level + A*a.index = K+p*a.prefixClock) :
    Cong d ((3:Int)^last * mask z xs) (z^K * carry last xs) := by
  induction xs with
  | nil => simp [mask, carry, Cong]
  | cons a xs ih =>
    obtain ⟨hi, he⟩ := h a (by simp)
    have ht := ih (fun b hb => h b (by simp [hb]))
    have hl : Cong d (z^a.level * (3:Int)^a.index) (z^K * 2^a.prefixClock) := by
      have hleft := times (refl d (z^a.level)) (power hA a.index)
      have hright := times (refl d (z^K)) (power hp a.prefixClock)
      have eq : z^a.level * (z^A)^a.index = z^K * (z^p)^a.prefixClock := by
        rw [← Int.pow_mul, ← Int.pow_mul, ← Int.pow_add, ← Int.pow_add, he]
      obtain ⟨u, hu⟩ := hleft
      obtain ⟨v, hv⟩ := hright
      exact ⟨v-u, by grind⟩
    have hl' := times (refl d ((3:Int)^(last-a.index))) hl
    have powerEq : (3:Int)^last = 3^(last-a.index) * 3^a.index := by
      rw [← Int.pow_add, Nat.sub_add_cancel hi]
    simp only [mask, carry, List.map_cons, List.sum_cons] at ht ⊢
    obtain ⟨u, hu⟩ := hl'
    obtain ⟨v, hv⟩ := ht
    exact ⟨u+v, by grind⟩

/-- Evaluate a certificate that the mask divides X^(p*L)-1. -/
theorem torsion_factor {d z maskValue : Int} {p L : Nat}
    (hp : Cong d (z^p) 2) (hm : d ∣ maskValue)
    (hfactor : maskValue ∣ z^(p*L)-1) : d ∣ (2:Int)^L-1 := by
  obtain ⟨u, hu⟩ := Int.dvd_trans hm hfactor
  obtain ⟨v, hv⟩ := power hp L
  rw [Int.pow_mul] at hu
  exact ⟨u-v, by grind⟩

/-- At an ordinary prefix the exact difference retains the numerical divisor. -/
theorem prefix_difference {x y C U V : Int} (h : U*y = V*x+C) :
    (U-V)*x-C = U*(x-y) := by grind

def blockCarry (u v : Int) : List Int → Int
  | [] => 0
  | c :: cs => v^cs.length * c + u * blockCarry u v cs

def geometric (u v : Int) : Nat → Int
  | 0 => 0
  | n+1 => v^n + u * geometric u v n

theorem geometric_difference (u v : Int) (n : Nat) :
    (u-v)*geometric u v n = u^n-v^n := by
  induction n with
  | zero => simp [geometric]
  | succ n ih =>
    simp only [geometric, Int.pow_succ]
    grind

/-- The carry difference is extracted once for any pattern and multiplicity. -/
theorem block_split (u v c delta : Int) (js : List Int) :
    blockCarry u v (js.map (fun j => c+delta*j))
      = c*geometric u v js.length + delta*blockCarry u v js := by
  induction js with
  | nil => simp [blockCarry, geometric]
  | cons j js ih =>
    simp only [List.map_cons, List.length_cons, List.length_map, blockCarry, geometric, ih]
    grind

#print axioms geometric_difference
#print axioms block_split
#print axioms mask_carry
#print axioms torsion_factor
#print axioms prefix_difference
end MaskDenominator
