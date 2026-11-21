import ReturnFourier

/-!
Actual-state links for the temporal marked-frequency argument.

The upper marked-phase estimate below is the proof of PR173's private
`RisingReturns.marked_height`, reproduced with attribution so the new argument
can call a public interface without modifying the pinned source.
Source revision: fa0c9e2a2851e6324391e39c17afcb5913185aec.
Source SHA256: e179465e1b66359f9fa492f73bcba18221a0d4d4767e06f26a025e057c0a0b5a.
-/

namespace CollatzShell.ForwardSection.MarkPhase

open Real

private theorem marked_height {x : Nat} (m : Marked x) :
    height x-x.log2 ≤ 140/((x.log2:ℝ)+1) := by
  let P := 2^x.log2
  have xp : 0<x := by have := m.1; omega
  have xr : (0:ℝ)<x := by exact_mod_cast xp
  have pp : (0:ℝ)<P := by dsimp [P]; positivity
  have pl : P≤x := Nat.log2_self_le xp.ne'
  have bound := m.2
  change (x.log2+1)*(x-P)≤70*P at bound
  have br : ((x.log2:ℝ)+1)*((x:ℝ)-P)≤70*P := by
    simpa only [Nat.cast_add,Nat.cast_one,Nat.cast_mul,Nat.cast_ofNat,Nat.cast_sub pl] using
      (show (((x.log2+1)*(x-P):Nat):ℝ)≤((70*P:Nat):ℝ) by exact_mod_cast bound)
  let v := (x:ℝ)/P
  have vp : 0<v := div_pos xr pp
  have width : v-1≤70/((x.log2:ℝ)+1) := by
    apply (le_div_iff₀ (by positivity)).mpr
    rw [show (v-1)*((x.log2:ℝ)+1)=(((x.log2:ℝ)+1)*(x-P))/P by dsimp [v]; field_simp]
    exact (div_le_iff₀ pp).mpr br
  have id : logb 2 v=height x-(x.log2:ℝ) := by
    dsimp only [v,height,P]
    rw [logb_div xr.ne' pp.ne',Nat.cast_pow,Nat.cast_ofNat,logb_pow,logb_two,mul_one]
  rw [← id]
  apply (div_le_iff₀ (log_pos (by norm_num))).mpr
  calc log v ≤ v-1 := log_le_sub_one_of_pos vp
       _ ≤ _ := width
       _ = (140/((x.log2:ℝ)+1))*(1/2) := by ring
       _ ≤ _ := mul_le_mul_of_nonneg_left log_two_bounds.1 (by positivity)

/-- The narrowing marked section has an actual nonnegative phase tending to
zero with ordinary height. This is a deterministic integer-state estimate. -/
theorem marked_phase_small {x : Nat} (m : Marked x) :
    0 ≤ height x-(x.log2:ℝ) ∧
    height x-(x.log2:ℝ) ≤ 140/((x.log2:ℝ)+1) := by
  constructor
  · exact sub_nonneg.mpr (Real.log2_le_logb x)
  · exact marked_height m

/-- An injective natural-valued sequence eventually leaves every fixed
finite initial interval; monotonicity is unnecessary. -/
theorem injective_eventually_large {f : Nat → Nat} (hf : Function.Injective f) (B : Nat) :
    ∃ J : Nat, ∀ j : Nat, J ≤ j → B ≤ f j := by
  have h : Filter.Tendsto f Filter.atTop Filter.atTop := by
    simpa only [Nat.cofinite_eq_atTop] using hf.tendsto_cofinite
  exact Filter.tendsto_atTop_atTop.mp h B

/-- Along an injective integer sequence, the phase of every sufficiently
late marked term lies in any prescribed positive interval at zero. -/
theorem marked_phase_eventually_small {f : Nat → Nat} (hf : Function.Injective f)
    {δ : ℝ} (hδ : 0<δ) :
    ∃ J : Nat, ∀ j : Nat, J≤j → Marked (f j) →
      0≤height (f j)-((f j).log2:ℝ) ∧
      height (f j)-((f j).log2:ℝ) ≤ δ := by
  obtain ⟨B,hB⟩ := exists_nat_gt (140/δ)
  obtain ⟨J,hJ⟩ := injective_eventually_large hf (2^B)
  refine ⟨J, ?_⟩
  intro j hj marked
  have positive : 0<f j := by have := marked.1; omega
  have logbound : B≤(f j).log2 := (Nat.le_log2 positive.ne').mpr (hJ j hj)
  have logbound' : (B:ℝ)≤((f j).log2:ℝ)+1 := by exact_mod_cast (by omega : B≤(f j).log2+1)
  have numerator : (140:ℝ)≤δ*(((f j).log2:ℝ)+1) := by
    have lower := (div_lt_iff₀ hδ).mp hB
    have upper := mul_le_mul_of_nonneg_right logbound' hδ.le
    linarith
  obtain ⟨lo,hi⟩ := marked_phase_small marked
  exact ⟨lo,hi.trans ((div_le_iff₀ (by positivity)).mpr numerator)⟩

end CollatzShell.ForwardSection.MarkPhase
