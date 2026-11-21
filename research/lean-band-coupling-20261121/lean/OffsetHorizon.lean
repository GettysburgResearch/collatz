module

public import OffsetDescent

@[expose] public section

/-! A polynomially thin subfamily of the forced band can survive its whole binary horizon. -/

namespace CollatzShell.OffsetDescent

/-- A thin-band family whose low bits force a long increasing odd run. -/
def horizonSeed (m : Nat) : Nat := 2^(4*m)+2^(3*m)-1

theorem horizonSeed_form (m : Nat) :
    horizonSeed m = 2^(3*m)*(2^m+1)-1 := by
  unfold horizonSeed
  congr 1
  rw [Nat.mul_add,mul_one,← pow_add]
  rw [show 3*m+m=4*m by omega]

private theorem max_halving (t n : Nat) : n≤2^t*orbit t n := by
  induction t generalizing n with
  | zero => simp [orbit]
  | succ t ih =>
    have a : n≤2*step n := by unfold step; split <;> omega
    have b := Nat.mul_le_mul_left 2 (ih (step n))
    simpa only [orbit,pow_succ,Nat.mul_assoc,Nat.mul_comm,Nat.mul_left_comm] using a.trans b

private theorem power_gap {m : Nat} (hm : 2≤m) : 2*16^m<27^m := by
  induction m, hm using Nat.le_induction with
  | base => norm_num
  | succ m hm ih =>
    rw [pow_succ,pow_succ]
    have pos : 0<27^m := by positivity
    nlinarith

theorem horizonSeed_log2 {m : Nat} (hm : 0<m) : (horizonSeed m).log2=4*m := by
  have a : 0<2^(3*m) := by positivity
  have b : 2^(3*m)≤2^(4*m) := Nat.pow_le_pow_right (by decide) (by omega)
  have lo : 2^(4*m)≤horizonSeed m := by unfold horizonSeed; omega
  have hi : horizonSeed m<2^(4*m+1) := by unfold horizonSeed; rw [pow_succ]; omega
  have pos : 0<horizonSeed m := by
    have powerPositive : 0<2^(4*m) := by positivity
    exact powerPositive.trans_le lo
  have l := (Nat.le_log2 pos.ne').mpr lo
  have u := (Nat.log2_lt pos.ne').mpr hi
  omega

private theorem width_bound (m : Nat) : 4*m+1≤70*2^m := by
  have h : m<2^m := Nat.lt_two_pow_self
  omega

theorem horizonSeed_marked {m : Nat} (hm : 0<m) :
    ForwardSection.Marked (horizonSeed m) := by
  have small : 0<2^(3*m) := by positivity
  have big : 0<2^(4*m) := by positivity
  have evenA : 2^(4*m)%2=0 := by
    have exp : 4*m=(4*m-1)+1 := by omega
    rw [exp,pow_succ]; omega
  have evenB : 2^(3*m)%2=0 := by
    have exp : 3*m=(3*m-1)+1 := by omega
    rw [exp,pow_succ]; omega
  refine ⟨?_,?_⟩
  · unfold horizonSeed
    omega
  · unfold ForwardSection.InSection
    rw [horizonSeed_log2 hm]
    have width := Nat.mul_le_mul_right (2^(3*m)) (width_bound m)
    have eq : 70*2^m*2^(3*m)=70*2^(4*m) := by
      rw [Nat.mul_assoc,← pow_add]
      congr 2
      omega
    rw [eq] at width
    unfold horizonSeed
    have off : 2^(4*m)+2^(3*m)-1-2^(4*m)=2^(3*m)-1 := by omega
    rw [off]
    exact (Nat.mul_le_mul_left _ (Nat.sub_le _ _)).trans width

/-- Every clock up to the binary horizon fails to descend for this family,
despite the offset being only about the three-quarter power of the seed. -/
theorem horizonSeed_no_descent {m t : Nat} (hm : 2≤m) (ht : t≤4*m) :
    horizonSeed m≤orbit t (horizonSeed m) := by
  have form := horizonSeed_form m
  obtain ⟨atRun,upRun⟩ := odd_run (3*m) (2^m+1) (by positivity)
  rw [← form] at atRun upRun
  by_cases early : t≤3*m
  · exact upRun t early
  · have decomp : t=3*m+(t-3*m) := by omega
    have remain : t-3*m≤m := by omega
    have slow := max_halving (t-3*m) (orbit (3*m) (horizonSeed m))
    rw [← orbit_add,← decomp,atRun] at slow
    have factor : 2^(t-3*m)≤2^m := Nat.pow_le_pow_right (by decide) remain
    have slow' := slow.trans (Nat.mul_le_mul_right (orbit t (horizonSeed m)) factor)
    have gap := power_gap hm
    have power3 : 3^(3*m)=27^m := by rw [pow_mul]; norm_num
    have power2 : 2^(4*m)=16^m := by rw [pow_mul]; norm_num
    have hsmall : 2^(3*m)≤2^(4*m) := Nat.pow_le_pow_right (by decide) (by omega)
    have pos : 0<2^m := by positivity
    rw [power3] at slow'
    have powerPositive : 0<2^(4*m) := by positivity
    have seedBound : horizonSeed m<2*16^m := by unfold horizonSeed; rw [← power2]; omega
    have base : 27^m*2^m≤27^m*(2^m+1)-1 := by
      have h : 0<27^m := by positivity
      rw [Nat.mul_add,mul_one]
      omega
    have mulLower := base.trans slow'
    have endpoint : 27^m≤orbit t (horizonSeed m) := by
      exact Nat.le_of_mul_le_mul_right
        (show 27^m*2^m≤orbit t (horizonSeed m)*2^m by
          simpa only [Nat.mul_comm] using mulLower) pos
    exact (seedBound.trans gap).le.trans endpoint

/-- The native-horizon descent selector is false even on the forced section. -/
theorem not_all_marked_descend_within_log2 :
    ¬ (∀ n, ForwardSection.Marked n → 1<n →
      ∃ t≤n.log2, orbit t n<n) := by
  intro claim
  have marked := horizonSeed_marked (m:=2) (by decide)
  have large : 1<horizonSeed 2 := by decide
  obtain ⟨t,time,descent⟩ := claim (horizonSeed 2) marked large
  rw [horizonSeed_log2 (by decide : 0<2)] at time
  exact Nat.not_lt_of_ge (horizonSeed_no_descent (by decide : 2≤2) time) descent

end CollatzShell.OffsetDescent

#print axioms CollatzShell.OffsetDescent.horizonSeed_marked
#print axioms CollatzShell.OffsetDescent.horizonSeed_no_descent
#print axioms CollatzShell.OffsetDescent.not_all_marked_descend_within_log2
