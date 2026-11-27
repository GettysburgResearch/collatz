import ProtectedCone
import MirrorEnergy

namespace RampShadow.Postpeak.Stopped

/-- A decomposition at the last upper-word clock. The input z starts
    the stopped suffix of h=H+weight w odd departures. Earlier visitor
    steps and their odd cost are unrestricted. -/
structure Frame (w : Word) (H ell : ℕ) (v z : ℤ) where
  β : Word
  clock : ℕ
  odds : ℕ
  origin : ℤ
  goal : ℤ
  length_eq : β.length = w.length
  total_clock : clock + w.length = H + weight w + ell
  total_odds : odds + weight β = H + weight w
  signed : Walk clock odds origin goal
  physical : Walk clock odds z (goal + 3^odds*v)
  translated : z = origin + 2^clock*v
  offset_eq : 3^weight β * goal + intercept β = offset w

theorem frame_exists {w H ell v z Y} (upper : PeakWord w H v Y)
    (enough : w.length ≤ H+weight w+ell)
    (stopped : Walk (H+weight w+ell) (H+weight w) z Y) :
    Nonempty (Frame w H ell v z) := by
  let a := H+weight w+ell-w.length
  have ac : a+w.length=H+weight w+ell := by dsimp [a];omega
  rw [←ac] at stopped
  obtain ⟨p,u,y,P,Q,grade⟩ := split stopped
  obtain ⟨β,len,wt,tail⟩ := word_of_walk Q
  let goal := y-3^p*v
  let origin := z-2^a*v
  have signed : Walk a p origin goal := by
    simpa only [origin,goal,sub_eq_add_neg,mul_neg] using lift P (-v)
  have up : (2:ℤ)^w.length*Y=3^(H+weight w)*v+offset w := upper
  rw [grade,pow_add] at up
  refine ⟨⟨β,a,p,origin,goal,len,ac,by omega,signed,?_,?_,?_⟩⟩
  · simpa [goal] using P
  · dsimp [origin];omega
  · rw [wt]
    dsimp only [goal]
    nlinarith only [up,tail]

theorem Frame.goal_bound {w H ell v z} (F : Frame w H ell v z) :
    |F.goal| ≤ 2 * (3:ℤ)^(w.length-weight F.β) := by
  have wt := weight_le F.β
  rw [F.length_eq] at wt
  have I := intercept_bounds F.β
  rw [F.length_eq] at I
  have tw : 0≤(2:ℤ)^w.length := by positivity
  exact small_state_refined wt (offset_bounds w).1 (offset_bounds w).2
    I.1 (by linarith [I.2]) F.offset_eq

/-- A short even total in the final h odd steps forces an integer
    signed anchor at minus one, without a budget on the full visitor. -/
theorem Frame.forced {w H ell v z} (F : Frame w H ell v z)
    (short : 4*ell+2*(w.length-weight w)+w.length+5 ≤ 2*H) :
    F.goal = -1 ∧ offset F.β = offset w := by
  have P := count_le F.signed
  have U := weight_le F.β
  rw [F.length_eq] at U
  have W := weight_le w
  have T := F.total_clock
  have G := F.total_odds
  have done := MirrorEnergy.sharp_trap F.signed (r:=w.length-weight F.β) (by omega) F.goal_bound
  refine ⟨done,?_⟩
  have E := F.offset_eq
  rw [done] at E
  unfold offset
  unfold offset at E
  linarith only [E]

theorem Frame.scaled_stop {w H ell v z} (F : Frame w H ell v z)
    (short : 4*ell+2*(w.length-weight w)+w.length+5 ≤ 2*H)
    (maximal : Maximal w) (odd : z%2=1) :
    ∃ δ l : ℕ, ∃ M : ℤ, weight F.β+δ=weight w ∧
      l+δ+(w.length-weight w)=ell ∧ 0<M ∧ M%2=1 ∧ M≤(2:ℤ)^l ∧
      z=(2:ℤ)^(l+δ)*(2^H*v)-M ∧
      Walk F.clock F.odds (-M) (-1) ∧
      Walk F.clock F.odds z (3^(H+δ)*v-1) := by
  obtain ⟨goal,eq⟩ := F.forced short
  have wt := maximal F.β F.length_eq eq
  have W := weight_le w
  have U := weight_le F.β
  rw [F.length_eq] at U
  have co := F.total_clock
  have gr := F.total_odds
  have ord := count_le F.signed
  let δ := weight w-weight F.β
  let l := F.clock-F.odds
  have od : F.odds=H+δ := by dsimp [δ];omega
  have clk : F.clock=l+δ+H := by dsimp [l];omega
  have S := F.signed
  rw [goal] at S
  have negative : F.origin<0 := by
    by_contra! h
    have := nonneg_end S h
    omega
  have mag := origin_magnitude S
  have small : -F.origin≤(2:ℤ)^l := by
    simpa only [l,abs_of_neg negative,abs_neg,abs_one,mul_one] using mag
  have even : ((2:ℤ)^F.clock*v)%2=0 := by
    have cc : F.clock=F.clock-1+1 := by omega
    rw [cc,pow_succ]
    apply Int.emod_eq_zero_of_dvd
    exact ⟨(2:ℤ)^(F.clock-1)*v,by ring⟩
  have tr := F.translated
  have parity : (-F.origin)%2=1 := by omega
  have phys := F.physical
  rw [goal,od] at phys
  refine ⟨δ,l,-F.origin,by dsimp [δ];omega,by dsimp [l,δ];omega,by omega,parity,small,?_,?_,?_⟩
  · rw [clk,pow_add] at tr
    nlinarith only [tr]
  · simpa only [neg_neg] using S
  · convert phys using 1
    ring

private theorem three_mod_two (n : ℕ) : (3:ℤ)^n%2=1 := by
  induction n with
  | zero => decide
  | succ n ih => rw [pow_succ,Int.mul_emod,ih];decide

/-- At a fixed physical clock and grade the absolute affine numerator
    determines the entire word. -/
theorem word_unique (a b : Word) (len : a.length=b.length)
    (grade : weight a=weight b) (same : intercept a=intercept b) : a=b := by
  induction a generalizing b with
  | nil => cases b <;> simp_all
  | cons x a ih =>
    cases b with
    | nil => simp at len
    | cons y b =>
      cases x <;> cases y <;> simp only [List.length_cons,Nat.add_right_cancel_iff] at len
      · have T := ih b len grade (by simpa [intercept] using same)
        simp [T]
      · change 2*intercept a = 3^weight b + 2*intercept b at same
        have P := three_mod_two (weight b)
        omega
      · change 3^weight a+2*intercept a = 2*intercept b at same
        have P := three_mod_two (weight a)
        omega
      · simp only [weight] at grade
        have G : weight a=weight b := by omega
        simp only [intercept,G] at same
        have T := ih b len G (by omega)
        simp [T]

/-- For fixed upper data and ell, the single ordinary signed origin
    determines the complete final word and its preceding native clock. -/
theorem Frame.origin_injective {w H ell v z z'} (F : Frame w H ell v z)
    (G : Frame w H ell v z') (same : F.origin=G.origin) :
    F.β=G.β ∧ F.clock=G.clock ∧ F.odds=G.odds ∧ F.goal=G.goal := by
  have fc := F.total_clock
  have gc := G.total_clock
  have clock : F.clock=G.clock := by omega
  have a := readout F.signed
  have b := readout G.signed
  rw [same,clock] at a
  have grade : F.odds=G.odds := a.2.symm.trans b.2
  have goal : F.goal=G.goal := a.1.symm.trans b.1
  have x := F.total_odds
  have y := G.total_odds
  have u : weight F.β=weight G.β := by omega
  have E := F.offset_eq
  rw [u,goal] at E
  exact ⟨word_unique _ _ (F.length_eq.trans G.length_eq.symm) u (by linarith only [E,G.offset_eq]),
    clock,grade,goal⟩

end RampShadow.Postpeak.Stopped

#print axioms RampShadow.Postpeak.Stopped.frame_exists
#print axioms RampShadow.Postpeak.Stopped.Frame.scaled_stop
#print axioms RampShadow.Postpeak.Stopped.Frame.origin_injective
