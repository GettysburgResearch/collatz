import PostDescentFibers
import Mathlib.Data.Finset.Max

/-! Exact first-entrance band and multiplicity of a stopped physical fiber. -/
namespace CollatzShell.FirstPassageMarks

open OffsetDescent PostDescentFibers

/-- A first entrance strictly below the indicated height at a specified time. -/
def FirstBelow (Y t n : ℕ) : Prop :=
  orbit t n < Y ∧ ∀ i < t, Y ≤ orbit i n

private theorem input_le_twice_step (y : ℕ) : y ≤ 2*step y := by
  by_cases even : y%2=0
  · simp [step,even]; omega
  · simp [step,even]; omega

/-- An entry from above lands no farther than a halving below the threshold. -/
theorem entrance_band {Y t n : ℕ} (start : Y ≤ n) (first : FirstBelow Y t n) :
    Y ≤ 2*orbit t n ∧ orbit t n < Y := by
  refine ⟨?_, first.1⟩
  cases t with
  | zero => simpa only [orbit] using (show Y ≤ 2*n by omega)
  | succ h =>
    have prev := first.2 h (by omega)
    rw [orbit_add]
    exact prev.trans (input_le_twice_step _)

/-- An integer form of the reciprocal Bernoulli bound. -/
private theorem reciprocal_bound (m t : ℕ) (small : t ≤ m) :
    (m+1)^t*(m-t) ≤ m^t*m := by
  induction t with
  | zero => simp
  | succ t ih =>
    have prev := ih (by omega)
    have diff : m-t=m-(t+1)+1 := by omega
    have stepbound : (m+1)*(m-(t+1)) ≤ m*(m-t) := by
      rw [diff]
      have : m-(t+1) ≤ m := Nat.sub_le _ _
      nlinarith
    calc
      (m+1)^(t+1)*(m-(t+1)) = (m+1)^t*((m+1)*(m-(t+1))) := by rw [pow_succ]; ring
      _ ≤ (m+1)^t*(m*(m-t)) := Nat.mul_le_mul_left _ stepbound
      _ = ((m+1)^t*(m-t))*m := by ring
      _ ≤ (m^t*m)*m := Nat.mul_le_mul_right _ prev
      _ = m^(t+1)*m := by rw [pow_succ]

/-- The width in ordinary-source coordinates of one stopped endpoint and
odd-count fiber. This bound has no exponentials and uses the original scale. -/
theorem entrance_source_width {Y t n m U : ℕ} (Ypos : 0<Y) (small : t ≤ 3*Y)
    (ordered : m ≤ n) (upper : n ≤ U) (first : FirstBelow Y t m)
    (hend : orbit t n = orbit t m) (hcount : oddCount t n = oddCount t m) :
    n-m ≤ t*U/(3*Y) := by
  let K := 3*Y
  have Kpos : 0<K := by dsimp [K]; omega
  have fibers : K^t*n ≤ (K+1)^t*m := same_endpoint_source_bound hend hcount first.2
  have est := reciprocal_bound K t small
  have scaled : K^t*((K-t)*n) ≤ K^t*(K*m) := calc
    K^t*((K-t)*n) = (K^t*n)*(K-t) := by ring
    _ ≤ ((K+1)^t*m)*(K-t) := Nat.mul_le_mul_right _ fibers
    _ = ((K+1)^t*(K-t))*m := by ring
    _ ≤ (K^t*K)*m := Nat.mul_le_mul_right _ est
    _ = K^t*(K*m) := by ring
  have lin := Nat.le_of_mul_le_mul_left scaled (pow_pos Kpos _)
  have addt : K-t+t=K := Nat.sub_add_cancel small
  have addn : n-m+m=n := Nat.sub_add_cancel ordered
  have kmul : (n-m)*K ≤ t*n := by
    nlinarith only [lin, congrArg (fun v : ℕ => v*n) addt,
      congrArg (fun v : ℕ => v*K) addn]
  apply (Nat.le_div_iff_mul_le Kpos).mpr
  exact kmul.trans (Nat.mul_le_mul_left _ upper)

/-- The finite first-passage fiber has one point per source and at most the
floor of the linear width plus one. No distribution on the landing is used. -/
theorem entrance_fiber_card (S : Finset ℕ) {Y t p z U : ℕ} (Ypos : 0<Y)
    (small : t ≤ 3*Y) (sources : ∀ n ∈ S, n ≤ U ∧ FirstBelow Y t n ∧
      orbit t n=z ∧ oddCount t n=p) :
    S.card ≤ t*U/(3*Y)+1 := by
  by_cases ex : S.Nonempty
  · let m := S.min' ex
    have hm : m ∈ S := S.min'_mem ex
    have src := sources m hm
    have sub : S ⊆ Finset.Icc m (m+t*U/(3*Y)) := by
      intro n hn
      have row := sources n hn
      have ord : m ≤ n := S.min'_le n hn
      have width := entrance_source_width Ypos small ord row.1 src.2.1
        (row.2.2.1.trans src.2.2.1.symm) (row.2.2.2.trans src.2.2.2.symm)
      exact Finset.mem_Icc.mpr ⟨ord,by omega⟩
    have size := Finset.card_le_card sub
    rw [Nat.card_Icc, Nat.add_assoc, Nat.add_sub_cancel_left] at size
    exact size
  · have empty : S=∅ := Finset.not_nonempty_iff_eq_empty.mp ex
    simp [empty]

#print axioms entrance_band
#print axioms entrance_source_width
#print axioms entrance_fiber_card

end CollatzShell.FirstPassageMarks
