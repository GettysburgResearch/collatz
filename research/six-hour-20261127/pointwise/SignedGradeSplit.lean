import SevenPhaseOddMap

/-! A dyadically complementary signed word forces a small actual future odd state. -/
namespace SignedGradeSplit
open MultiBlockCompensation ReflectedCycleMinimum SevenPhaseMinimum SevenPhaseOddMap

private theorem count_prefix (x D L : ℕ) (order : D ≤ L) : count x D ≤ count x L := by
  induction D generalizing x L with
  | zero => simp [count]
  | succ D ih =>
    cases L with
    | zero => omega
    | succ L => exact Nat.add_le_add_left (ih (reflected x) L (by omega)) (bit x)

private theorem positive_iter (x D : ℕ) (pos : 0 < x) : 0 < shortcut^[D] x := by
  induction D generalizing x with
  | zero => exact pos
  | succ D ih =>
    rw [Function.iterate_succ_apply]
    apply ih
    unfold shortcut
    split <;> omega

private theorem even_suffix (x : ℕ) (pos : 0 < x) :
    ∃ e v, shortcut^[e] x = v ∧ ordinaryCount x e = 0 ∧ v % 2 = 1 ∧ v ≤ x := by
  induction x using Nat.strong_induction_on with
  | h x ih =>
    by_cases even : x % 2 = 0
    · have next : shortcut x = x / 2 := by simp [shortcut,even]
      obtain ⟨e,v,last,cnt,odd,bound⟩ := ih (x/2) (by omega) (by omega)
      refine ⟨e+1,v,?_,?_,odd,by omega⟩
      · simpa only [Function.iterate_succ_apply,next] using last
      · simp [ordinaryCount,bit,even,next,cnt]
    · exact ⟨0,x,rfl,rfl,by omega,le_rfl⟩

private theorem count_join (x d e : ℕ) :
    ordinaryCount x (d+e) = ordinaryCount x d + ordinaryCount (shortcut^[d] x) e := by
  induction d generalizing x with
  | zero => simp [ordinaryCount]
  | succ d ih =>
    rw [Nat.succ_add,ordinaryCount,ordinaryCount,Function.iterate_succ_apply,ih]
    omega

/-- Split at the funded binary clock. The physical expression is exact, and its odd
count cannot exceed the odd count through the supplied full signed horizon. -/
theorem split_physical {c m A D L : ℕ} (hm : 0 < m) (sum : c+m = 2^D*A)
    (funded : D ≤ L) :
    ordinaryCount c D = count m D ∧ count m D ≤ count m L ∧
    shortcut^[D] c + reflected^[D] m = 3^(count m D)*A := by
  obtain ⟨same,ends⟩ := dual_transport D c m A hm sum
  exact ⟨same,count_prefix m D L funded,ends⟩

/-- The ordinary accelerated trajectory visits a positive odd state below the
full signed count bound, even if the binary split occurs during even halving. -/
theorem small_odd_future {c m A D L b : ℕ} (hc : c % 2 = 1) (hm : 0 < m)
    (sum : c+m = 2^D*A) (funded : D ≤ L) (grade : count m L = b) :
    ∃ j ≤ b, 0 < accelerated^[j] c ∧ accelerated^[j] c % 2 = 1 ∧
      accelerated^[j] c ≤ 3^b*A := by
  obtain ⟨same,budget,ends⟩ := split_physical hm sum funded
  rw [grade] at budget
  have height : shortcut^[D] c ≤ 3^b*A := calc
    shortcut^[D] c ≤ 3^(count m D)*A := by omega
    _ ≤ 3^b*A := Nat.mul_le_mul_right A (Nat.pow_le_pow_right (by decide) budget)
  obtain ⟨e,v,last,zero,odd,small⟩ := even_suffix _ (positive_iter c D (by omega))
  have arrival : shortcut^[D+e] c = v := by
    rw [Nat.add_comm,Function.iterate_add_apply,last]
  have cnt : ordinaryCount c (D+e) ≤ b := by rw [count_join,zero,same]; omega
  have hit : Ancestor b v c := ⟨by omega,hc,D+e,arrival,cnt⟩
  obtain ⟨_,_,j,limit,endpt⟩ := (ancestor_iff odd).mp hit
  exact ⟨j,limit,by omega,by rwa [endpt],by rw [endpt]; exact small.trans height⟩

/-- An actual matching pair of reflected clocks gives a bound at the same
positive source, for arbitrary marked period and arbitrary lap count. -/
theorem matched_grade_future {c m A D P B laps : ℕ} (hc : c % 2 = 1) (hm : 0 < m)
    (sum : c+m = 2^D*A) (grade : count m (D+P*laps) = B*laps) :
    ∃ j ≤ B*laps, 0 < accelerated^[j] c ∧ accelerated^[j] c % 2 = 1 ∧
      accelerated^[j] c ≤ 3^(B*laps)*A :=
  small_odd_future hc hm sum (by omega) grade

end SignedGradeSplit
#print axioms SignedGradeSplit.count_prefix
#print axioms SignedGradeSplit.positive_iter
#print axioms SignedGradeSplit.even_suffix
#print axioms SignedGradeSplit.count_join
#print axioms SignedGradeSplit.split_physical
#print axioms SignedGradeSplit.small_odd_future
#print axioms SignedGradeSplit.matched_grade_future
