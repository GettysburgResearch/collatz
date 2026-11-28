import CyclicMarginalTransport

/-! Multiscale cyclic transport bounds an individual heavy target cylinder. -/
set_option autoImplicit false
set_option warningAsError true

namespace Collatz.CyclicAtomBound
open Collatz.CyclicTent Collatz.CyclicMarginalTransport
open scoped BigOperators

/-- Width `j+1` in ternary units. -/
def circle (j : ℕ) : ℕ := 2*3^j

@[simp] theorem circle_zero : circle 0=2 := rfl

theorem circle_pos (j : ℕ) : 0<circle j := by unfold circle; positivity

theorem circle_succ (j : ℕ) : circle (j+1)=3*circle j := by simp only [circle,pow_succ]; ring

/-- The higher target law projects to the lower law on every lower-period test. -/
def consistent (m : ℕ) (lower upper : ℕ→ℚ) : Prop :=
  ∀ f : ℕ→ℚ, periodic m f → average (3*m) upper f = average m lower f

private theorem one_level {m : ℕ} (hm : 0<m) (L shift : ℕ) (low high : ℕ→ℚ)
    (hc : consistent m low high) (flow : Flow m) (hr : flow.demands high) :
    average (3*m) high (scaledTent (3*m) L shift) ≤
      average m low (scaledTent m L shift)+4*(m:ℚ)*flow.cost := by
  have hband := flow_band_bound hm L shift flow high hr
  have hlow := hc _ (scaled_period m L shift hm)
  have hdiff : average (3*m) high (band m L shift) =
      average (3*m) high (scaledTent (3*m) L shift)-average (3*m) high (scaledTent m L shift) := by
    simp only [average,band,mul_sub,Finset.sum_sub_distrib]
  linarith

private theorem base_level (L shift : ℕ) (p : ℕ→ℚ) (hn : ∀i<2,0≤p i)
    (hs : (∑ i∈Finset.range 2,p i)=1) :
    average 2 p (scaledTent 2 L shift) ≤ (L:ℚ)^2+1 := by
  calc
    _ ≤ ∑ i∈Finset.range 2, p i*((L:ℚ)^2+1) := by
      apply Finset.sum_le_sum
      intro i hi
      apply mul_le_mul_of_nonneg_left _ (hn i (Finset.mem_range.mp hi))
      exact tent_two_bound L (shift+i)
    _ = _ := by rw [←Finset.sum_mul,hs,one_mul]

/-- Finite hierarchy. Only widths `1,..,J+1` enter its hypotheses. -/
theorem hierarchy_tent_bound (J L shift : ℕ) (A : ℚ) (target : ℕ→ℕ→ℚ)
    (hn : ∀i<2,0≤target 0 i) (hs : (∑ i∈Finset.range 2,target 0 i)=1)
    (hc : ∀j<J,consistent (circle j) (target j) (target (j+1)))
    (hflow : ∀j<J,∃ flow:Flow (circle j),flow.demands (target (j+1)) ∧ flow.cost≤A) :
    average (circle J) (target J) (scaledTent (circle J) L shift) ≤
      (L:ℚ)^2+1+2*((circle J:ℚ)-2)*A := by
  have inductive_bound : ∀ j≤J, average (circle j) (target j) (scaledTent (circle j) L shift) ≤
      (L:ℚ)^2+1+2*((circle j:ℚ)-2)*A := by
    intro j
    induction j with
    | zero =>
      intro _
      simpa only [circle_zero,Nat.cast_ofNat,sub_self,mul_zero,zero_mul,add_zero] using base_level L shift (target 0) hn hs
    | succ j ih =>
      intro hj
      have hj' : j<J := by omega
      obtain ⟨flow,hr,hcost⟩ := hflow j hj'
      have hfirst := one_level (circle_pos j) L shift (target j) (target (j+1)) (hc j hj') flow hr
      have hsecond := ih (by omega)
      have hcost' := mul_le_mul_of_nonneg_left hcost (show 0≤4*(circle j:ℚ) by positivity)
      rw [circle_succ]
      push_cast
      linarith
  exact inductive_bound J (by omega)

/-- Every heavy atom of the actual coherent target has to pay directed cost.
The bound is integral after clearing rational masses. No complex analysis enters. -/
theorem actual_atom_cost (J L d : ℕ) (hd : d<circle J) (A : ℚ) (target : ℕ→ℕ→ℚ)
    (hpos : ∀j≤J,∀i<circle j,0≤target j i) (hs : (∑ i∈Finset.range 2,target 0 i)=1)
    (hc : ∀j<J,consistent (circle j) (target j) (target (j+1)))
    (hflow : ∀j<J,∃ flow:Flow (circle j),flow.demands (target (j+1)) ∧ flow.cost≤A) :
    (circle J:ℚ)*L*target J d ≤ (L:ℚ)^2+1+2*((circle J:ℚ)-2)*A := by
  let m := circle J
  let shift := (m-1)*(d+L)
  have hm : 0<m := circle_pos J
  have hcenter : m∣(shift+d)+L := by
    refine ⟨d+L,?_⟩
    dsimp only [shift]
    calc
      _ = ((m-1)+1)*(d+L) := by ring
      _ = _ := by rw [Nat.sub_add_cancel (by omega : 1≤m)]
  have hpeak := tent_peak m L (shift+d) hm hcenter
  have hmass := hpos J (by omega) d hd
  have hscaled : (m:ℚ)*L*target J d ≤ target J d*scaledTent m L shift d := by
    unfold scaledTent
    calc
      _ = target J d*((m:ℚ)*L) := by ring
      _ ≤ _ := mul_le_mul_of_nonneg_left (mul_le_mul_of_nonneg_left hpeak (Nat.cast_nonneg _)) hmass
  have hsingle : target J d * scaledTent m L shift d ≤ average m (target J) (scaledTent m L shift) := by
    apply Finset.single_le_sum (f:=fun i => target J i*scaledTent m L shift i)
    · intro i hi
      exact mul_nonneg (hpos J (by omega) i (Finset.mem_range.mp hi))
        (mul_nonneg (Nat.cast_nonneg _) (tent_nonneg m L (shift+i) hm))
    · exact Finset.mem_range.mpr hd
  exact hscaled.trans (hsingle.trans (hierarchy_tent_bound J L shift A target (hpos 0 (by omega)) hs hc hflow))

end Collatz.CyclicAtomBound
