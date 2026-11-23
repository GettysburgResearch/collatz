module

public import OffsetDescent
public import LongDiamondErasure

@[expose] public section

/-!
# Physical partners after an expanding prefix

An ordinary binary prefix can expand the source. A later endpoint diamond can
still give a smaller partner for the original source, provided its dyadic
saving exceeds that expansion. The prefix, odd run, and both merging paths are
actual orbits; there is no use of unrestricted semigroup multiplication.

The selector for a suitable endpoint diamond remains an explicit hypothesis.
-/

namespace CollatzShell.ResidualPrefixErasure

open OffsetDescent

/-- Exact affine expansion followed by a dyadic saving. The carry condition
handles the complete nonnegative source progression, including its first term. -/
theorem prefix_source_bound (h r b z x : Nat)
    (scale : 2^r*(x+1) = 3^(oddCount h b)*z + orbit h b + 1)
    (slope : 3^(oddCount h b) ≤ 2^(h+r))
    (carry : orbit h b+1 < 2^r*(b+1)) :
    x < 2^h*z+b := by
  have leading := Nat.mul_le_mul_right z slope
  have total : 3^(oddCount h b)*z + (orbit h b+1) <
      2^(h+r)*z + 2^r*(b+1) := Nat.add_lt_add_of_le_of_lt leading carry
  have factor : 2^(h+r)*z + 2^r*(b+1) = 2^r*(2^h*z+b+1) := by
    rw [pow_add]
    ring
  rw [factor] at total
  have scaled : 2^r*(x+1) < 2^r*(2^h*z+b+1) := by
    rw [scale]
    simpa only [Nat.add_assoc] using total
  have smaller := (Nat.mul_lt_mul_left (by positivity : 0<2^r)).mp scaled
  omega

/-- A strict slope advantage alone gives a concrete finite cutoff. -/
theorem prefix_source_bound_eventually (h r b z x : Nat)
    (scale : 2^r*(x+1) = 3^(oddCount h b)*z + orbit h b + 1)
    (slope : 3^(oddCount h b) < 2^(h+r))
    (large : orbit h b+2 ≤ z) :
    x < 2^h*z+b := by
  have gap : 3^(oddCount h b)+1 ≤ 2^(h+r) := by omega
  have leading := Nat.mul_le_mul_right z gap
  have total : 3^(oddCount h b)*z + orbit h b + 1 < 2^(h+r)*z := by
    nlinarith only [leading, large]
  have factor : 2^(h+r)*z = 2^r*(2^h*z) := by
    rw [pow_add]
    ring
  rw [factor] at total
  have scaled : 2^r*(x+1) < 2^r*(2^h*z) := by
    simpa only [scale] using total
  have smaller := (Nat.mul_lt_mul_left (by positivity : 0<2^r)).mp scaled
  omega

/-- Generic physical bridge: a finite prefix, an arbitrarily long odd run,
and a synchronous endpoint diamond combine into a smaller ordinary source. -/
theorem prefix_diamond_partner (h b z k r H u : Nat)
    (hr : 0<r) (hrk : r<k) (hu : 0<u)
    (endpoint : orbit h (2^h*z+b) = 2^k*u-1)
    (diamond : orbit H (3^(k-r)*u-1) =
      orbit H (3^r*(3^(k-r)*u)-1))
    (slope : 3^(oddCount h b) ≤ 2^(h+r))
    (carry : orbit h b+1 < 2^r*(b+1)) :
    let n := 2^h*z+b
    let x := 2^(k-r)*u-1
    0<x ∧ x<n ∧ orbit (k-r+H) x=orbit (h+k+H) n := by
  dsimp only
  obtain ⟨xp,scale,_,merge⟩ := rising_erase_prefix k r H u hr hrk hu diamond
  have adjusted : 2^r*(2^(k-r)*u-1+1) =
      3^(oddCount h b)*z+orbit h b+1 := by
    rw [← orbit_shift, endpoint]
    exact scale
  refine ⟨xp, prefix_source_bound h r b z _ adjusted slope carry, ?_⟩
  rw [show h+k+H=h+(k+H) by omega, orbit_add h (k+H), endpoint]
  exact merge

/-- Version requiring only a strict leading-coefficient advantage, beyond an
explicit finite initial segment. -/
theorem prefix_diamond_partner_eventually (h b z k r H u : Nat)
    (hr : 0<r) (hrk : r<k) (hu : 0<u)
    (endpoint : orbit h (2^h*z+b) = 2^k*u-1)
    (diamond : orbit H (3^(k-r)*u-1) =
      orbit H (3^r*(3^(k-r)*u)-1))
    (slope : 3^(oddCount h b) < 2^(h+r))
    (large : orbit h b+2 ≤ z) :
    let n := 2^h*z+b
    let x := 2^(k-r)*u-1
    0<x ∧ x<n ∧ orbit (k-r+H) x=orbit (h+k+H) n := by
  dsimp only
  obtain ⟨xp,scale,_,merge⟩ := rising_erase_prefix k r H u hr hrk hu diamond
  have adjusted : 2^r*(2^(k-r)*u-1+1) =
      3^(oddCount h b)*z+orbit h b+1 := by
    rw [← orbit_shift, endpoint]
    exact scale
  refine ⟨xp, prefix_source_bound_eventually h r b z _ adjusted slope large, ?_⟩
  rw [show h+k+H=h+(k+H) by omega, orbit_add h (k+H), endpoint]
  exact merge

/-- The seven-step prefix containing the difficult class `27 mod 128`. -/
theorem prefix27 (z : Nat) : orbit 7 (128*z+27)=729*z+161 := by
  have eq := orbit_shift 7 27 z
  have count : oddCount 7 27=6 := by decide
  have base : orbit 7 27=161 := by decide
  simpa only [count,base,Nat.reducePow] using eq

/-- Every member of the `27 mod 128` cylinder grows through the fixed prefix. -/
theorem prefix27_initial_growth (z i : Nat) (hi : i≤7) :
    128*z+27≤orbit i (128*z+27) := by
  have he (x : Nat) (h : x%2=0) : step x=x/2 := by simp [step,h]
  have ho (x : Nat) (h : x%2≠0) : step x=(3*x+1)/2 := by simp [step,h]
  have e0 : step (128*z+27)=192*z+41 := by rw [ho _ (by omega)]; omega
  have e1 : step (192*z+41)=288*z+62 := by rw [ho _ (by omega)]; omega
  have e2 : step (288*z+62)=144*z+31 := by rw [he _ (by omega)]; omega
  have e3 : step (144*z+31)=216*z+47 := by rw [ho _ (by omega)]; omega
  have e4 : step (216*z+47)=324*z+71 := by rw [ho _ (by omega)]; omega
  have e5 : step (324*z+71)=486*z+107 := by rw [ho _ (by omega)]; omega
  have e6 : step (486*z+107)=729*z+161 := by rw [ho _ (by omega)]; omega
  interval_cases i <;> simp only [orbit,e0,e1,e2,e3,e4,e5,e6] <;> omega

/-- The variable odd run extends the no-descent horizon of the original source. -/
theorem prefix27_no_descent_through_run (k u z i : Nat) (hu : 0<u)
    (endpoint : 729*z+162=2^k*u) (hi : i≤7+k) :
    128*z+27≤orbit i (128*z+27) := by
  by_cases early : i≤7
  · exact prefix27_initial_growth z i early
  · have endeq : orbit 7 (128*z+27)=2^k*u-1 := by
      rw [prefix27]
      omega
    have growth := (odd_run k u hu).2 (i-7) (by omega)
    have base := prefix27_initial_growth z 7 le_rfl
    rw [endeq] at base
    rw [show i=7+(i-7) by omega,orbit_add 7 (i-7),endeq]
    exact base.trans growth

/-- A non-dyadic partner slope: every legal eighth-source diamond after this
prefix gives `1024*x = 729*n + 29`, hence a strictly smaller ordinary source.
The source clock is unbounded with `k`. -/
theorem prefix27_eighth_partner (k u z : Nat) (hk : 4≤k) (hu : 0<u)
    (endpoint : 729*z+162 = 2^k*u)
    (phase : (3^(k-3)*u)%256=147) :
    let n := 128*z+27
    let x := 2^(k-3)*u-1
    0<x ∧ x<n ∧ 1024*x=729*n+29 ∧
      orbit (k+5) x=orbit (k+15) n := by
  dsimp only
  have endeq : orbit 7 (128*z+27)=2^k*u-1 := by
    rw [prefix27]
    omega
  obtain ⟨xp,scale,_,merge⟩ := rising_eighth_source_partner k u hk hu phase
  have exact_scale : 1024*(2^(k-3)*u-1)=729*(128*z+27)+29 := by
    omega
  refine ⟨xp,by omega,exact_scale,?_⟩
  rw [show k+15=7+(k+8) by omega,orbit_add 7 (k+8),endeq]
  exact merge

#print axioms prefix_source_bound
#print axioms prefix_source_bound_eventually
#print axioms prefix_diamond_partner
#print axioms prefix_diamond_partner_eventually
#print axioms prefix27
#print axioms prefix27_initial_growth
#print axioms prefix27_no_descent_through_run
#print axioms prefix27_eighth_partner

end CollatzShell.ResidualPrefixErasure
