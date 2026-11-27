import Mathlib.Data.Nat.GCD.BigOperators
import Mathlib.Tactic

/-! Finite ordinary affine rows, signed zero-sum pruning, and the projective
divisibility bound for lifts with sparse terminal carries. -/
set_option autoImplicit false

namespace Collatz.SparseTerminal

/-- The actual shortcut branches, with clock, odd count and affine carry. -/
inductive Walk : ℕ → ℕ → ℕ → ℕ → ℕ → Prop
  | nil (x : ℕ) : Walk 0 0 0 x x
  | even {k p c x y : ℕ} : Walk k p c x y → Walk (k+1) p (2*c) (2*x) y
  | odd {k p c u y : ℕ} : Walk k p c (3*u+2) y →
      Walk (k+1) (p+1) (3^p+2*c) (2*u+1) y

/-- Every positive or zero ordinary source has the path used below. -/
theorem exists_walk (k x : ℕ) : ∃ p c y, Walk k p c x y := by
  induction k generalizing x with
  | zero => exact ⟨0, 0, x, .nil x⟩
  | succ k ih =>
    by_cases h : x%2=0
    · have hx : x = 2*(x/2) := by omega
      obtain ⟨p,c,y,w⟩ := ih (x/2)
      exact ⟨p,2*c,y,hx ▸ Walk.even w⟩
    · have hx : x = 2*(x/2)+1 := by omega
      obtain ⟨p,c,y,w⟩ := ih (3*(x/2)+2)
      exact ⟨p+1,3^p+2*c,y,hx ▸ Walk.odd w⟩

/-- Integer numerator for the composed physical branches. -/
theorem affine_row {k p c x y : ℕ} (w : Walk k p c x y) :
    2^k*y=3^p*x+c := by
  induction w with
  | nil => simp
  | even w ih => rw [pow_succ]; nlinarith only [ih]
  | @odd k p c u y w ih => rw [pow_succ, pow_succ]; nlinarith only [ih]

/-- The lift follows the identical branch choices and retains the actual carry. -/
theorem lift_walk {k p c x y : ℕ} (w : Walk k p c x y) (t : ℕ) :
    Walk k p c (x+2^k*t) (y+3^p*t) := by
  induction w generalizing t with
  | nil x => simpa using Walk.nil (x+t)
  | @even k p c x y w ih =>
    convert Walk.even (ih t) using 1
    ring
  | @odd k p c u y w ih =>
    have z := ih (3*t)
    have xeq : (3*u+2)+2^k*(3*t) = 3*(u+2^k*t)+2 := by ring
    rw [xeq] at z
    convert Walk.odd z using 1 <;> ring

/-- The elementary height saving uses the original, positive ordinary source. -/
theorem physical_height {k p c x y : ℕ} (w : Walk k p c x y) (hx : 0<x) :
    2^k*y ≤ 4^p*x := by
  induction w with
  | nil => simp
  | @even k p c x y w ih =>
    have high := ih (by omega)
    rw [pow_succ]; nlinarith only [high]
  | @odd k p c u y w ih =>
    have high := ih (by omega)
    rw [pow_succ, pow_succ]
    nlinarith only [high, Nat.zero_le (4^p*u)]

/-- The full ternary modulus is present even when a different lift was chosen
at every depth and its terminal word was individually chosen. -/
theorem terminal_difference {k p c x y l h d r t : ℕ} (w : Walk k p c x y)
    (tail : Walk l h d (y+3^p*t) r) :
    Walk k p c (x+2^k*t) (y+3^p*t) ∧
      2^l*r = 3^h*y + d + 3^(p+h)*t := by
  refine ⟨lift_walk w t, ?_⟩
  rw [affine_row tail, pow_add]
  ring

/-- Starting one below a prescribed multiple of a power of two gives the
literal run of odd inputs in the constructed two-run completions. -/
theorem odd_run (d u : ℕ) : ∃ c, Walk d d c
    (2^d*(u+1)-1) (3^d*(u+1)-1) := by
  induction d generalizing u with
  | zero => simpa using (show ∃ c, Walk 0 0 c u u from ⟨0, .nil u⟩)
  | succ d ih =>
    obtain ⟨c,w⟩ := ih (3*u+2)
    have hp : 0<2^d*(u+1) := by positivity
    have eq1 : 3*(2^d*(u+1)-1)+2 = 2^d*(3*u+2+1)-1 := by
      rw [show 2^d*(3*u+2+1)=3*(2^d*(u+1)) by ring]
      omega
    rw [← eq1] at w
    have hsrc : 2*(2^d*(u+1)-1)+1=2^(d+1)*(u+1)-1 := by
      rw [show 2^(d+1)*(u+1)=2*(2^d*(u+1)) by ring]
      omega
    have htarget : 3^d*(3*u+2+1)-1=3^(d+1)*(u+1)-1 := by
      congr 1
      ring
    exact ⟨_,hsrc ▸ htarget ▸ Walk.odd w⟩

/-- Every following halving is an actual even step. -/
theorem even_run (j x : ℕ) : Walk j 0 0 (2^j*x) x := by
  induction j with
  | zero => simpa using Walk.nil x
  | succ j ih =>
    convert Walk.even ih using 1
    ring

/-- Carry of a repeated block with denominator clock A and numerator clock Q. -/
def repeatCarry (A Q c : ℤ) : ℕ → ℤ
  | 0 => 0
  | t+1 => Q * repeatCarry A Q c t + A^t*c

theorem repeat_carry_identity (A Q c : ℤ) (t : ℕ) :
    (A-Q)*repeatCarry A Q c t = c*(A^t-Q^t) := by
  induction t with
  | zero => simp [repeatCarry]
  | succ t ih =>
    simp only [repeatCarry,pow_succ]
    linear_combination Q*ih

/-- A finite signed presentation can have all its zero subsums removed
without changing its value, even when the original atom values coincide. -/
theorem prune_signed {ι : Type*} (s : Finset ι) (z : ι → ℤ) :
    ∃ t ⊆ s, ∑ i ∈ t, z i = ∑ i ∈ s, z i ∧
      ∀ a ⊆ t, a.Nonempty → ∑ i ∈ a, z i ≠ 0 := by
  classical
  refine Finset.strongInductionOn s ?_
  intro s ih
  by_cases clean : ∀ a ⊆ s, a.Nonempty → ∑ i ∈ a, z i ≠ 0
  · exact ⟨s, Finset.Subset.rfl, rfl, clean⟩
  · push Not at clean
    obtain ⟨a, ha, hne, hzero⟩ := clean
    obtain ⟨t, ht, he, hc⟩ := ih (s \ a) (Finset.sdiff_ssubset ha hne)
    have total := Finset.sum_sdiff ha (f := z)
    rw [hzero, add_zero] at total
    exact ⟨t, ht.trans Finset.sdiff_subset, he.trans total, hc⟩

/-- Any prime-to-six divisor of a primitive right coordinate divides the
ordinary multiplier. All multiplicities are retained. -/
theorem strip_clock {a b g y u v : ℕ} (ha : a∣y) (hclock : g*y=b*2^u*3^v)
    (h2 : Nat.Coprime a 2) (h3 : Nat.Coprime a 3) : a∣b := by
  have all : a∣b*2^u*3^v := hclock ▸ (ha.trans (dvd_mul_left y g))
  exact (h2.pow_right u).dvd_of_dvd_mul_right
    ((h3.pow_right v).dvd_of_dvd_mul_right all)

/-- The product of the primitive outside parts divides the numerator left
after stripping every explicit clock. -/
theorem outside_product {ι : Type*} (s : Finset ι) (b a : ι → ℕ)
    {out V : ℕ} (h0 : out∣V) (h : ∀ i ∈ s, a i∣b i) :
    out * ∏ i ∈ s, a i ∣ V * ∏ i ∈ s, b i :=
  Nat.mul_dvd_mul h0 (Finset.prod_dvd_prod_of_dvd _ _ h)

/-- Exact divisibility form of the projective local gain. Here g is the
content, V is the primitive zero-th coordinate, b the chosen pivot's
multiplier, R the product of all right multipliers, and P any product of
outside parts as above. -/
theorem pivot_divisibility {g V b R P u v p h : ℕ}
    (hzero : 3^(p+h) ∣ g*V) (hpivot : g∣b*2^u*3^v)
    (hb : b∣R) (hout : P∣V*R) (hcop : Nat.Coprime P 3) :
    3^(p+h)*P ∣ 3^v*(V*R) := by
  have lifted : 3^(p+h) ∣ 2^u * (3^v*(V*b)) := by
    have a := hzero.trans (Nat.mul_dvd_mul_right hpivot V)
    convert a using 1
    ring
  have cp : Nat.Coprime (3^(p+h)) (2^u) :=
    ((show Nat.Coprime 3 2 by decide).pow_left (p+h)).pow_right u
  have p0 := cp.dvd_of_dvd_mul_left lifted
  have h3 : 3^(p+h) ∣ 3^v*(V*R) :=
    p0.trans (Nat.mul_dvd_mul_left (3^v) (Nat.mul_dvd_mul_left V hb))
  exact (hcop.pow_right (p+h)).symm.mul_dvd_of_dvd_of_dvd h3
    (hout.trans (dvd_mul_left (V*R) (3^v)))

#print axioms exists_walk
#print axioms affine_row
#print axioms lift_walk
#print axioms physical_height
#print axioms terminal_difference
#print axioms odd_run
#print axioms even_run
#print axioms repeat_carry_identity
#print axioms prune_signed
#print axioms strip_clock
#print axioms outside_product
#print axioms pivot_divisibility
end Collatz.SparseTerminal
