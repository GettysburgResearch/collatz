import Mathlib.Data.Finset.Card
import Mathlib.Data.Finset.Prod
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

namespace Collatz.FactorObstruction

def box (R B : ℕ) : Finset (ℕ × ℕ × ℕ) :=
  (Finset.range (R+1)).product ((Finset.range (R+1)).product (Finset.range (B+1)))

def weight (p h t : ℕ) (v : ℕ × ℕ × ℕ) : ℕ :=
  v.1*p+v.2.1*h+v.2.2*t

/-- A collision gives the signed relation by subtracting its two triples. -/
theorem relation_pair (p h t R B : ℕ) (rate : h ≤ 2*p)
    (room : 3*p*R+t*B+1 < (R+1)*(R+1)*(B+1)) :
    ∃ x ∈ box R B, ∃ y ∈ box R B, x ≠ y ∧ weight p h t x = weight p h t y := by
  apply Finset.exists_ne_map_eq_of_card_lt_of_maps_to (t := Finset.range (3*p*R+t*B+1))
  · simpa [box, Nat.mul_assoc] using room
  · intro x hx
    change x ∈ box R B at hx
    change x ∈ (Finset.range (R+1)).product ((Finset.range (R+1)).product (Finset.range (B+1))) at hx
    obtain ⟨h₁,hrest⟩ := Finset.mem_product.mp hx
    obtain ⟨h₂,h₃⟩ := Finset.mem_product.mp hrest
    simp only [Finset.mem_range] at h₁ h₂ h₃
    apply Finset.mem_range.mpr
    have u := Nat.mul_le_mul_right p (show x.1 ≤ R by omega)
    have v := Nat.mul_le_mul (show x.2.1 ≤ R by omega) rate
    have w := Nat.mul_le_mul_right t (show x.2.2 ≤ B by omega)
    dsimp [weight]
    nlinarith only [u,v,w]

theorem enough_room (p R t B : ℕ) (small : 4*t ≤ R^2) (space : 6*p ≤ B*R)
    (rpos : 0 < R) :
    3*p*R+t*B+1 < (R+1)*(R+1)*(B+1) := by
  have := Nat.mul_le_mul_right B small
  have := Nat.mul_le_mul_right R space
  nlinarith

/-- Even over a nonfield a collision gives a common zero of the two
monomials after substituting X=u^t. -/
theorem equal_monomials {A : Type*} [CommSemiring A] (u : A) (p h t : ℕ)
    (two : u^p = 2) (three : u^h = 3) (x y : ℕ × ℕ × ℕ)
    (eq : weight p h t x = weight p h t y) :
    2^x.1 * 3^x.2.1 * (u^t)^x.2.2 = 2^y.1 * 3^y.2.1 * (u^t)^y.2.2 := by
  have rep (v : ℕ × ℕ × ℕ) : u^(weight p h t v) =
      2^v.1 * 3^v.2.1 * (u^t)^v.2.2 := by
    simp only [weight, pow_add, Nat.mul_comm v.1 p, Nat.mul_comm v.2.1 h,
      Nat.mul_comm v.2.2 t, pow_mul, two, three]
  rw [← rep, eq, rep]

/-- With j=0 the reduced rational slope t/p=a/b gives the positive-root binomial. -/
theorem rational_binomial {A : Type*} [CommSemiring A] (u : A) (p t a b : ℕ)
    (two : u^p = 2) (slope : t*b = p*a) : (u^t)^b = 2^a := by
  rw [← pow_mul, slope, pow_mul, two]

/-- Distinct ordinary smooth numbers are certified by their 2-adic valuation. -/
theorem smooth_inj (a b c d : ℕ) (eq : 2^a*3^b = 2^c*3^d) : a=c ∧ b=d := by
  have odd (j : ℕ) : (3:ℕ)^j%2=1 := by rw [Nat.pow_mod]; simp
  induction a generalizing c with
  | zero =>
    cases c with
    | zero =>
      simp only [pow_zero, one_mul] at eq
      exact ⟨rfl, Nat.pow_right_injective (by decide : 1 < 3) eq⟩
    | succ c =>
      have : 3^b=2*(2^c*3^d) := by simpa [pow_succ, Nat.mul_assoc, Nat.mul_left_comm] using eq
      have := odd b
      omega
  | succ a ih =>
    cases c with
    | zero =>
      have : 2*(2^a*3^b)=3^d := by simpa [pow_succ, Nat.mul_assoc, Nat.mul_left_comm] using eq
      have := odd d
      omega
    | succ c =>
      have e : 2*(2^a*3^b)=2*(2^c*3^d) := by
        simpa [pow_succ, Nat.mul_assoc, Nat.mul_left_comm] using eq
      obtain ⟨h,k⟩ := ih c (by omega)
      exact ⟨by omega,k⟩

/-- At most v residues for a two-dimensional box of smooth products. -/
theorem cyclic_collision (v p h r : ℕ) (hv : 0<v) (room : v < (r+1)*(r+1)) :
    ∃ x ∈ (Finset.range (r+1)).product (Finset.range (r+1)),
    ∃ y ∈ (Finset.range (r+1)).product (Finset.range (r+1)),
      x ≠ y ∧ (p*x.1+h*x.2)%v = (p*y.1+h*y.2)%v := by
  apply Finset.exists_ne_map_eq_of_card_lt_of_maps_to (t := Finset.range v)
  · simpa using room
  · intro x _
    exact Finset.mem_range.mpr (Nat.mod_lt _ hv)

/-- A shared order-v encoding of 2 and 3 bounds the whole modulus. -/
theorem small_cyclic_modulus (g v p h r : ℕ) (hv : 0<v) (room : v < (r+1)*(r+1))
    (encode : ℕ → ℕ)
    (repr : ∀ i j, (2^i*3^j)%g = encode ((p*i+h*j)%v)) : g ≤ 6^r := by
  by_contra no
  have gt : 6^r < g := by omega
  obtain ⟨x,hx,y,hy,ne,eq⟩ := cyclic_collision v p h r hv room
  have small (z : ℕ × ℕ) (hz : z ∈ (Finset.range (r+1)).product (Finset.range (r+1))) :
      2^z.1*3^z.2 < g := by
    obtain ⟨a,b⟩ := Finset.mem_product.mp hz
    simp only [Finset.mem_range] at a b
    have e : 2^z.1*3^z.2 ≤ (2:ℕ)^r*3^r := Nat.mul_le_mul
      (Nat.pow_le_pow_right (by decide) (by omega))
      (Nat.pow_le_pow_right (by decide) (by omega))
    rw [← mul_pow] at e
    exact lt_of_le_of_lt e gt
  have e := (repr x.1 x.2).trans ((congrArg encode eq).trans (repr y.1 y.2).symm)
  rw [Nat.mod_eq_of_lt (small x hx), Nat.mod_eq_of_lt (small y hy)] at e
  obtain ⟨a,b⟩ := smooth_inj _ _ _ _ e
  exact ne (Prod.ext a b)

/-- Exact group encoding from the three power relations. -/
theorem cyclic_rep {A : Type*} [CommSemiring A] (u : A) (v p h i j : ℕ)
    (one : u^v=1) (two : u^p=2) (three : u^h=3) :
    (2:A)^i*3^j = u^((p*i+h*j)%v) := by
  rw [← two, ← three, ← pow_mul, ← pow_mul, ← pow_add]
  let n := p*i+h*j
  change u^n=u^(n%v)
  calc
    u^n = u^(n%v+v*(n/v)) := by rw [Nat.mod_add_div]
    _ = u^(n%v) := by rw [pow_add,pow_mul,one,one_pow,mul_one]

/-- Extracts a modulus divisor from the evaluated Sylvester Bezout representation. -/
theorem bezout_divisor (g H P a b resultant : ℤ) (first : g ∣ H)
    (second : g ∣ P) (certificate : a*H+b*P=resultant) : g ∣ resultant := by
  obtain ⟨i, hi⟩ := first
  obtain ⟨j, hj⟩ := second
  refine ⟨a*i+b*j, ?_⟩
  rw [← certificate, hi, hj]; ring

#print axioms relation_pair
#print axioms enough_room
#print axioms equal_monomials
#print axioms rational_binomial
#print axioms smooth_inj
#print axioms cyclic_collision
#print axioms small_cyclic_modulus
#print axioms cyclic_rep
#print axioms bezout_divisor
end Collatz.FactorObstruction
