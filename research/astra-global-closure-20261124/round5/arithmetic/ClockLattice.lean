import Mathlib.GroupTheory.OrderOfElement
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Ring
import Mathlib.Data.ZMod.Basic
import Mathlib.Data.Nat.ModEq
import Mathlib.Data.Finset.Card

/-! Exact relations behind the two-dimensional lattice of local unit equations.
The units can lie in the unit group of a ring modulo a full prime power. -/
namespace Collatz.ClockLattice

/-- The clock relation and the short monomial relation specialize every integral
combination, in any commutative group. -/
theorem local_lattice {G : Type*} [CommGroup G] (x y θ : G)
    (A p r s i j : ℤ) (hclock : x ^ A * y ^ (-p) = 1)
    (hroot : x ^ r * y ^ s = θ) :
    x ^ (i*A+j*r) * y ^ (-i*p+j*s) = θ ^ j := by
  have h : -i*p = (-p)*i := by ring
  rw [h, mul_comm i A, mul_comm j r, mul_comm j s, zpow_add, zpow_add,
    zpow_mul, zpow_mul, zpow_mul, zpow_mul]
  calc
    _ = (x ^ A * y ^ (-p)) ^ i * (x ^ r * y ^ s) ^ j := by
      rw [mul_zpow, mul_zpow]; ac_rfl
    _ = θ ^ j := by rw [hclock, hroot, one_zpow, one_mul]

/-- Transversality of the two original directions survives every independent
change of lattice coordinates. This gives the independent valuation rows. -/
theorem projection_determinant (A p r s i j k l : ℤ) :
    (i*A+j*r)*(-k*p+l*s) - (k*A+l*r)*(-i*p+j*s) =
    (i*l-k*j)*(A*s+p*r) := by ring

/-- A relation between the projected rows has zero coefficients when the
clock is transverse to the monomial and the lattice coordinates are independent. -/
theorem independent_rows (A p r s i j k l m n : ℤ)
    (hdir : A*s+p*r ≠ 0) (hind : i*l-k*j ≠ 0)
    (hx : m*(i*A+j*r)+n*(k*A+l*r) = 0)
    (hy : m*(-i*p+j*s)+n*(-k*p+l*s) = 0) : m = 0 ∧ n = 0 := by
  have hd : (i*A+j*r)*(-k*p+l*s) - (k*A+l*r)*(-i*p+j*s) ≠ 0 := by
    rw [projection_determinant]; exact mul_ne_zero hind hdir
  have hm : m*((i*A+j*r)*(-k*p+l*s) - (k*A+l*r)*(-i*p+j*s)) = 0 := by
    linear_combination (-k*p+l*s)*hx - (k*A+l*r)*hy
  have hn : n*((i*A+j*r)*(-k*p+l*s) - (k*A+l*r)*(-i*p+j*s)) = 0 := by
    linear_combination (i*A+j*r)*hy - (-i*p+j*s)*hx
  exact ⟨(mul_eq_zero.mp hm).resolve_right hd, (mul_eq_zero.mp hn).resolve_right hd⟩

/-- The weighted squared covolume of the lattice equals the sum of its
three squared coordinate minors (the rank-two Gram determinant). -/
theorem gram_area {R : Type*} [CommRing R] (A p r s w : R) :
    (A^2+p^2)*(r^2+s^2+w^2) - (A*r-p*s)^2 =
    (A*s+p*r)^2 + (A*w)^2 + (p*w)^2 := by ring

/-- A divisibility certificate in a polynomial quotient specializes at every
root of the defining polynomial, also over composite residue rings. -/
theorem factor_mod_clock {R : Type*} [CommRing R] (F P H K B : R)
    (hfactor : F = P*H + B*K) (hclock : B = 0) (hcarry : P = 0) : F = 0 := by
  simp [hfactor, hclock, hcarry]

/-- The exact nonnegative-semimodule closure at a physical edge. -/
theorem apery_edge (p a t t' e : ℤ) (he : 1 ≤ e)
    (h : t' - t = p*e-(p+a)) : ∃ k : ℤ, 0 ≤ k ∧ t'+a=t+p*k := by
  refine ⟨e-1, by omega, ?_⟩
  linear_combination h

/-- Reflection of discrepancies forces reflection of the actual gap at a pair
of mirrored edges. The proof retains the literal division exponents. -/
theorem reflected_gap (p A e f x y x' y' H : ℤ) (hp : p ≠ 0)
    (h : y-x=p*e-A) (h' : y'-x'=p*f-A)
    (hs : x+y'=H) (ht : y+x'=H) : e=f := by
  apply mul_left_cancel₀ hp
  linear_combination h' - h + ht - hs

/-- Count the genuinely distinct representatives of `0,a,...,ka` below the
next digit step.  For an Apéry representative `rep i ≤ a*i` is the minimum
property in the residue class of `a*i`. -/
theorem digit_step_cap (S : Finset ℕ) (a p k w : ℕ) (rep : ℕ → ℕ)
    (hcop : Nat.gcd p a = 1) (hk : k < p)
    (hmem : ∀ i ≤ k, rep i ∈ S) (hle : ∀ i ≤ k, rep i ≤ a*i)
    (hmod : ∀ i ≤ k, Nat.ModEq p (rep i) (a*i))
    (hcount : (S.filter (fun n => n < w)).card ≤ k) : w ≤ a*k := by
  by_contra! h
  have bound : (Finset.range (k+1)).card ≤ (S.filter (fun n => n < w)).card := by
    apply Finset.card_le_card_of_injOn rep
    · intro i hi
      have hik : i ≤ k := by simpa [Nat.lt_succ_iff] using hi
      exact Finset.mem_filter.mpr ⟨hmem i hik,
        lt_of_le_of_lt ((hle i hik).trans (Nat.mul_le_mul_left a hik)) h⟩
    · intro i hi j hj hij
      have hik : i ≤ k := by simpa [Nat.lt_succ_iff] using hi
      have hjk : j ≤ k := by simpa [Nat.lt_succ_iff] using hj
      have he : Nat.ModEq p (a*i) (a*j) := (hmod i hik).symm.trans (hij ▸ hmod j hjk)
      exact (Nat.ModEq.cancel_left_of_coprime hcop he).eq_of_lt_of_lt
        (lt_of_le_of_lt hik hk) (lt_of_le_of_lt hjk hk)
  rw [Finset.card_range] at bound
  omega

#print axioms local_lattice
#print axioms projection_determinant
#print axioms independent_rows
#print axioms gram_area
#print axioms factor_mod_clock
#print axioms apery_edge
#print axioms reflected_gap
#print axioms digit_step_cap
end Collatz.ClockLattice
