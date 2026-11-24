import FirstPassageMarks

/-! A narrow ordinary source annulus fixes the odd count from a stopped
endpoint and clock. This is the finite arithmetic interface behind the
endpoint-only first-passage fiber estimate; probability and asymptotics
are outside this module. -/
namespace CollatzShell.EndpointFibers

open OffsetDescent PostDescentFibers FirstPassageMarks

private theorem reciprocal_bound (K t : ℕ) (small : t ≤ K) :
    (K+1)^t*(K-t) ≤ K^t*K := by
  induction t with
  | zero => simp
  | succ t ih =>
    have prev := ih (by omega)
    have diff : K-t=K-(t+1)+1 := by omega
    have stepbound : (K+1)*(K-(t+1)) ≤ K*(K-t) := by
      rw [diff]
      have : K-(t+1) ≤ K := Nat.sub_le _ _
      nlinarith
    calc
      (K+1)^(t+1)*(K-(t+1)) = (K+1)^t*((K+1)*(K-(t+1))) := by rw [pow_succ]; ring
      _ ≤ (K+1)^t*(K*(K-t)) := Nat.mul_le_mul_left _ stepbound
      _ = ((K+1)^t*(K-t))*K := by ring
      _ ≤ (K^t*K)*K := Nat.mul_le_mul_right _ prev
      _ = K^(t+1)*K := by rw [pow_succ]

private theorem count_le {Y t n m L U : ℕ} (Ypos : 0<Y)
    (small : t ≤ 3*Y) (separation : 3*Y*U < 3*(3*Y-t)*L)
    (low : L ≤ m) (high : n ≤ U) (floor : ∀ i<t, Y ≤ orbit i n)
    (endpoint : orbit t m = orbit t n) : oddCount t m ≤ oddCount t n := by
  let K := 3*Y
  have Kpos : 0<K := by dsimp [K]; omega
  have lo := Nat.mul_le_mul_left (K^t) (linear_lower t m)
  rw [endpoint] at lo
  have comp := lo.trans (scaled_orbit_upper t Y n floor)
  have est := reciprocal_bound K t small
  have scaled : K^t*((K-t)*(3^(oddCount t m)*m)) ≤
      K^t*(K*(3^(oddCount t n)*n)) := calc
    K^t*((K-t)*(3^(oddCount t m)*m))
        = (K^t*(3^(oddCount t m)*m))*(K-t) := by ring
    _ ≤ ((K+1)^t*(3^(oddCount t n)*n))*(K-t) := Nat.mul_le_mul_right _ comp
    _ = ((K+1)^t*(K-t))*(3^(oddCount t n)*n) := by ring
    _ ≤ (K^t*K)*(3^(oddCount t n)*n) := Nat.mul_le_mul_right _ est
    _ = K^t*(K*(3^(oddCount t n)*n)) := by ring
  have lin := Nat.le_of_mul_le_mul_left scaled (pow_pos Kpos _)
  by_contra fail
  have gap : oddCount t n+1 ≤ oddCount t m := by omega
  have pw : 3^(oddCount t n)*3 ≤ 3^(oddCount t m) := by
    rw [← pow_succ]
    exact Nat.pow_le_pow_right (by omega) gap
  have enough : 3^(oddCount t n)*(3*(K-t)*L) ≤
      3^(oddCount t n)*(K*U) := calc
    3^(oddCount t n)*(3*(K-t)*L) = (K-t)*((3^(oddCount t n)*3)*L) := by ring
    _ ≤ (K-t)*(3^(oddCount t m)*m) := Nat.mul_le_mul_left _ (Nat.mul_le_mul pw low)
    _ ≤ K*(3^(oddCount t n)*n) := lin
    _ ≤ K*(3^(oddCount t n)*U) := Nat.mul_le_mul_left _ (Nat.mul_le_mul_left _ high)
    _ = 3^(oddCount t n)*(K*U) := by ring
  have contra := Nat.le_of_mul_le_mul_left enough (by positivity)
  exact (not_le_of_gt separation) contra

/-- Two first entrances at the same physical clock and endpoint have the
same odd count on the stated narrow source annulus. The strict linear
separation inequality accounts for the entire affine correction. -/
theorem entrance_odd_count_unique {Y t n m L U : ℕ} (Ypos : 0<Y)
    (small : t ≤ 3*Y) (separation : 3*Y*U < 3*(3*Y-t)*L)
    (nlo : L ≤ n) (nhi : n ≤ U) (mlo : L ≤ m) (mhi : m ≤ U)
    (nf : FirstBelow Y t n) (mf : FirstBelow Y t m)
    (endpoint : orbit t n = orbit t m) : oddCount t n = oddCount t m := by
  apply Nat.le_antisymm
  · exact count_le Ypos small separation nlo mhi mf.2 endpoint
  · exact count_le Ypos small separation mlo nhi nf.2 endpoint.symm

/-- An endpoint-only stopped fiber has the same linear cardinal bound as
a fiber in which the odd count was additionally specified. -/
theorem entrance_endpoint_card (S : Finset ℕ) {Y t z L U : ℕ} (Ypos : 0<Y)
    (small : t ≤ 3*Y) (separation : 3*Y*U < 3*(3*Y-t)*L)
    (sources : ∀ n∈S, L ≤ n ∧ n ≤ U ∧ FirstBelow Y t n ∧ orbit t n=z) :
    S.card ≤ t*U/(3*Y)+1 := by
  by_cases ex : S.Nonempty
  · obtain ⟨m,hm⟩ := ex
    have base := sources m hm
    apply entrance_fiber_card S Ypos small (p := oddCount t m) (z := z)
    intro n hn
    have row := sources n hn
    refine ⟨row.2.1,row.2.2.1,row.2.2.2,?_⟩
    exact entrance_odd_count_unique Ypos small separation row.1 row.2.1
      base.1 base.2.1 row.2.2.1 base.2.2.1 (row.2.2.2.trans base.2.2.2.symm)
  · have empty : S=∅ := Finset.not_nonempty_iff_eq_empty.mp ex
    simp [empty]

/-- The useful annular specialization needs only a clock at most half
the reciprocal-error scale and an endpoint ratio less than 3/2. -/
theorem entrance_endpoint_card_narrow (S : Finset ℕ) {Y t z L U : ℕ}
    (Ypos : 0<Y) (clock : 2*t ≤ 3*Y) (annulus : 2*U < 3*L)
    (sources : ∀ n∈S, L ≤ n ∧ n ≤ U ∧ FirstBelow Y t n ∧ orbit t n=z) :
    S.card ≤ t*U/(3*Y)+1 := by
  have small : t ≤ 3*Y := by omega
  have addback : 3*Y-t+t=3*Y := Nat.sub_add_cancel small
  have scaled : (3*Y)*(2*U) < (3*Y)*(3*L) := Nat.mul_lt_mul_of_pos_left annulus (by omega)
  have doubled : 3*Y ≤ 2*(3*Y-t) := by omega
  have upper := Nat.mul_le_mul_right (3*L) doubled
  have separation : 3*Y*U < 3*(3*Y-t)*L := by nlinarith only [scaled, upper]
  exact entrance_endpoint_card S Ypos small separation sources

#print axioms entrance_odd_count_unique
#print axioms entrance_endpoint_card
#print axioms entrance_endpoint_card_narrow

end CollatzShell.EndpointFibers
