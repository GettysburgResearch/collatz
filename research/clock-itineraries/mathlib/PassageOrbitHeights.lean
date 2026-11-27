module
public import PassageOrbitDenominator
import all PassageOrbitDenominator
import all TernaryItinerary
public section

namespace Collatz.Itinerary.PassageOrbit

/-- Constant term in the numerator of the affine shortcut word. -/
def carry (a : ℕ) : ℕ → ℕ
  | 0 => 0
  | t+1 => if run t a%2=0 then carry a t else 3*carry a t + 2^t

theorem affine_identity (a t : ℕ) :
    2^t*run t a=3^(oddCount a t)*a+carry a t := by
  induction t with
  | zero => simp [run,oddCount,carry]
  | succ t ih =>
    rw [state_succ, Nat.pow_succ, oddCount, pow_add,carry]
    by_cases e : run t a%2=0
    · have h : 2*step (run t a)=run t a := by simp [step,e]; omega
      simp [e]
      rw [Nat.mul_assoc,h]
      exact ih
    · have o : run t a%2=1 := by omega
      have h : 2*step (run t a)=3*run t a+1 := by simp [step,e]; omega
      simp [o]
      rw [Nat.mul_assoc,h]
      nlinarith only [ih]

theorem denominator_carry (a t : ℕ) : denominator a t=
    determinant a t/(determinant a t).gcd (carry a t) := by
  rw [carry_gcd (affine_identity a t)]; rfl

private theorem no_fixed {a : ℕ} (p : 0<a) : step a≠a := by
  unfold step; split <;> omega

private theorem nearby_nonreturn {a : ℕ} (p : 0<a) (t : ℕ) :
    ∃ x, t≤x ∧ x≤t+1 ∧ run x a≠a := by
  by_cases h : run t a=a
  · exact ⟨t+1,by omega,by omega,by rw [state_succ,h]; exact no_fixed p⟩
  · exact ⟨t,by omega,by omega,h⟩

/-- The relative determinant cannot be small at two times separated by
one or two native steps. This uses only the five possible short multipliers. -/
theorem separated_near_times (a t h : ℕ) (lo : 0<h) (hi : h≤2)
    (near : 16*determinant a t < 2^t) :
    2^(t+h)≤16*determinant a (t+h) := by
  have inc := oddCount_increment a t h
  let v := oddCount a (t+h)-oddCount a t
  have hv : v≤h := by dsimp [v]; omega
  have eq : oddCount a (t+h)=oddCount a t+v := by dsimp [v]; omega
  let x : ℕ := 2^t
  let y : ℕ := 3^(oddCount a t)
  change 16*Nat.dist x y < x at near
  unfold determinant
  rw [eq,pow_add,pow_add]
  change x*2^h≤16*Nat.dist (x*2^h) (y*3^v)
  unfold Nat.dist at *
  interval_cases h <;> interval_cases v <;> norm_num at * <;> omega

/-- One of each four consecutive shortcut prefixes is both a nonreturn
and has a large relative determinant, for every positive starting integer. -/
theorem good_in_four {a : ℕ} (p : 0<a) (t : ℕ) :
    ∃ x, t≤x ∧ x≤t+3 ∧ run x a≠a ∧ 2^x≤16*determinant a x := by
  obtain ⟨u,tu,ut,nu⟩ := nearby_nonreturn p t
  obtain ⟨v,uv,vu,nv⟩ := nearby_nonreturn p (u+1)
  by_cases h : 2^u≤16*determinant a u
  · exact ⟨u,tu,by omega,nu,h⟩
  · have hv := separated_near_times a u (v-u) (by omega) (by omega) (by omega)
    rw [show u+(v-u)=v by omega] at hv
    exact ⟨v,by omega,by omega,nv,hv⟩

theorem growth (a t : ℕ) : 2^t*(run t a+1)≤3^t*(a+1) := by
  induction t with
  | zero => simp [run]
  | succ t ih =>
    have edge : 2*(step (run t a)+1)≤3*(run t a+1) := by unfold step; split <;> omega
    rw [state_succ,pow_succ,pow_succ]
    calc
      _ = 2^t*(2*(step (run t a)+1)) := by ring
      _ ≤ 2^t*(3*(run t a+1)) := Nat.mul_le_mul_left _ edge
      _ = 3*(2^t*(run t a+1)) := by ring
      _ ≤ 3*(3^t*(a+1)) := Nat.mul_le_mul_left _ ih
      _ = _ := by ring

private theorem ratio_power {r t : ℕ} (rt : 3*r≤t) : 2^r*3^t≤4^t := by
  obtain ⟨z,rfl⟩ := Nat.exists_eq_add_of_le rt
  have h : (2*3^3)^r≤(4^3)^r := Nat.pow_le_pow_left (by decide) _
  rw [mul_pow,←pow_mul,←pow_mul] at h
  rw [pow_add,pow_add,←Nat.mul_assoc]
  exact Nat.mul_le_mul h (Nat.pow_le_pow_left (by decide) _)

theorem gcd_height {a t : ℕ} (nr : run t a≠a) :
    2^t*(determinant a t).gcd (Nat.dist (run t a) a)≤3^t*(a+1) := by
  have dp : 0<Nat.dist (run t a) a := by unfold Nat.dist; omega
  have gl := (Nat.le_of_dvd dp (Nat.gcd_dvd_right (determinant a t) _)).trans (diff_le_max ..)
  have b := Nat.mul_le_mul_left (2^t) gl
  rcases le_total (run t a) a with h|h
  · rw [max_eq_right h] at b
    exact b.trans (Nat.mul_le_mul (Nat.pow_le_pow_left (by decide) t) (by omega))
  · rw [max_eq_left h] at b
    exact b.trans ((Nat.mul_le_mul_left _ (Nat.le_succ _)).trans (growth a t))

theorem large_denominator {a t r K : ℕ} (rt : 3*r≤t)
    (nr : run t a≠a) (far : 2^t≤K*determinant a t) :
    2^r≤K*(a+1)*denominator a t := by
  let g := (determinant a t).gcd (Nat.dist (run t a) a)
  have cap : 2^t*g≤3^t*(a+1) := gcd_height nr
  have recov : g*denominator a t=determinant a t := Nat.mul_div_cancel' (Nat.gcd_dvd_left ..)
  apply Nat.le_of_mul_le_mul_right (c:=3^t) _ (Nat.pow_pos (by decide))
  calc
    2^r*3^t ≤ 4^t := ratio_power rt
    _ = 2^t*2^t := by rw [←mul_pow]; norm_num
    _ ≤ 2^t*(K*determinant a t) := Nat.mul_le_mul_left _ far
    _ = (K*denominator a t)*(2^t*g) := by rw [←recov]; ring
    _ ≤ (K*denominator a t)*(3^t*(a+1)) := Nat.mul_le_mul_left _ cap
    _ = _ := by ring

theorem large_in_four {a r t : ℕ} (p : 0<a) (rt : 3*r≤t) :
    ∃ x, t≤x ∧ x≤t+3 ∧ 2^r≤16*(a+1)*denominator a x := by
  obtain ⟨x,tx,xt,nr,far⟩ := good_in_four p t
  exact ⟨x,tx,xt,large_denominator (by omega) nr far⟩

end Collatz.Itinerary.PassageOrbit
