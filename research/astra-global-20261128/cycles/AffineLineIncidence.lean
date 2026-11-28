import MixedParity
import Mathlib.Data.Nat.ModEq
import Mathlib.Data.Finset.Card

/-! Finite native line coordinates and the all-moduli intersection bound. -/
set_option autoImplicit false
set_option warningAsError true
namespace Collatz.AffineLineIncidence
open CoreBranching Collatz.CofactorDescent Collatz.MixedParity

/-- The first physical coordinate is an odd-slope affine function of the fresh tail
    for an odd source multiplier. The identity itself holds at any multiplier. -/
theorem native_affine_tail (t A a r u : ℕ) :
    run t (source A a (r + 2^t*u)) =
      run t (source A a r) + (A * 3^(odds t (source A a r))) * u := by
  have hx : source A a (r + 2^t*u) = source A a r + 2^t*(A*u) := by
    unfold source
    ring
  rw [hx, (native_lift t (source A a r) (A*u)).1]
  ring

/-- Native pairs stay on the same integer line at every tail displacement. -/
theorem native_line_elimination (t A a B b r u : ℕ) :
    let p := A * 3^(odds t (source A a r))
    let q := B * 3^(odds t (source B b r))
    p * run t (source B b (r+2^t*u)) + q * run t (source A a r) =
      q * run t (source A a (r+2^t*u)) + p * run t (source B b r) := by
  dsimp
  rw [native_affine_tail, native_affine_tail]
  ring

/-- Translation of both graphs and their common component of slope disappear
    in the comparison between two abscissas of intersection. -/
theorem intersection_spacing (q a s b d x y : ℕ) (hq : 0 < q)
    (hx : (a+s)*x+b ≡ a*x+d [MOD q])
    (hy : (a+s)*y+b ≡ a*y+d [MOD q]) :
    x ≡ y [MOD q / q.gcd s] := by
  have hx' : s*x+b ≡ d [MOD q] := by
    apply Nat.ModEq.add_left_cancel' (a*x)
    simpa only [Nat.add_mul, Nat.add_assoc] using hx
  have hy' : s*y+b ≡ d [MOD q] := by
    apply Nat.ModEq.add_left_cancel' (a*y)
    simpa only [Nat.add_mul, Nat.add_assoc] using hy
  exact Nat.ModEq.cancel_left_div_gcd hq (Nat.ModEq.add_right_cancel' b (hx'.trans hy'.symm))

/-- Every pair of graphs has at most the gcd of the modulus and slope difference
    many intersections among a complete system of representatives. -/
theorem intersection_card (q a s b d : ℕ) (hq : 0 < q) :
    ((Finset.range q).filter
      (fun x => (a+s)*x+b ≡ a*x+d [MOD q])).card ≤ q.gcd s := by
  let g := q.gcd s
  let h := q/g
  have hg : 0 < g := Nat.gcd_pos_of_pos_left s hq
  have hh : 0 < h := Nat.div_pos (Nat.gcd_le_left s hq) hg
  have hq' : h*g=q := Nat.div_mul_cancel (Nat.gcd_dvd_left q s)
  change _ ≤ g
  rw [← Finset.card_range g]
  apply Finset.card_le_card_of_injOn (fun x => x/h)
  · intro x hx
    have hlt := Finset.mem_range.mp (Finset.mem_filter.mp hx).1
    apply Finset.mem_range.mpr
    exact (Nat.div_lt_iff_lt_mul hh).2 (by rw [Nat.mul_comm g h, hq']; exact hlt)
  · intro x hx y hy hsame
    have hx' := (Finset.mem_filter.mp hx).2
    have hy' := (Finset.mem_filter.mp hy).2
    have heq : x%h=y%h := intersection_spacing q a s b d x y hq hx' hy'
    have ex := Nat.mod_add_div x h
    have ey := Nat.mod_add_div y h
    change x/h=y/h at hsame
    rw [heq,hsame] at ex
    exact ex.symm.trans ey

end Collatz.AffineLineIncidence
