import PostWords

/-! Exact arbitrary-clock mirror origins through seven even departures.
The finite table is closed under every odd inverse, including the loop at 1. -/

namespace RampShadow.Postpeak.SignedOrigins

def origins : ℕ → Finset ℤ
  | 0 => {1}
  | 1 => {2}
  | 2 => {3,4}
  | 3 => {6,8}
  | 4 => {11,12,16}
  | 5 => {15,22,24,32}
  | 6 => {29,30,43,44,48,64}
  | 7 => {39,58,59,60,86,88,96,128}
  | _ => ∅

private theorem even_closed : ∀ e ∈ Finset.range 7,
    ∀ m ∈ origins e, 2*m ∈ origins (e+1) := by decide +kernel

private theorem odd_closed : ∀ e ∈ Finset.range 8,
    ∀ m ∈ origins e, (2*m+1)%3=0 → (2*m+1)/3 ∈ origins e := by decide +kernel

/-- Every actual signed source ending at -1 is in the finite table at its
    even count. There is no bound on the number of odd departures or time. -/
private theorem complete_at {h p : ℕ} {x z : ℤ} (W : Walk h p x z)
    (endpoint : z=-1) (few : h-p≤7) :
    -x ∈ origins (h-p) := by
  induction W with
  | nil => rw [endpoint];norm_num [origins]
  | @even h p x y W ih =>
    have hp := count_le W
    have ep : h-p ∈ Finset.range 7 := by simp;omega
    have z := even_closed (h-p) ep (-(x:ℤ)) (ih endpoint (by omega))
    simpa only [show h+1-p=h-p+1 by omega,show -(2*x)=2*(-x) by ring] using z
  | @odd h p x y z edge W ih =>
    have ep : h-p ∈ Finset.range 8 := by simp;omega
    have div : (2*(-y)+1)%3=0 := by omega
    have eq : (2*(-y)+1)/3=-x := by omega
    have z := odd_closed (h-p) ep (-y) (ih endpoint (by omega)) div
    simpa only [show h+1-(p+1)=h-p by omega,eq] using z

theorem complete {h p : ℕ} {x : ℤ} (W : Walk h p x (-1)) (few : h-p≤7) :
    -x ∈ origins (h-p) := complete_at W rfl few

def oddCount (e : ℕ) : ℕ := ((origins e).filter (fun m => m%2=1)).card

theorem odd_counts : (List.range 8).map oddCount = [1,0,1,0,1,1,2,2] := by
  decide +kernel

/-- This is the rational arithmetic consumer of the written stopped-Kraft
    count, including the full geometric tail from eight even departures. -/
theorem common_margin :
    (2/3 : ℚ)-4/15-(4/3)*(1/16+1/256+1/1024+2/4096+2/16384+1/256)
      =9343/30720 ∧ (3/10 : ℚ)<9343/30720 := by norm_num

/-- Residue-sensitive costs in the zero ternary class, plus the same tail. -/
theorem zero_margin :
    (1/3 : ℚ)-1/15-1/30-1/240-17/15360-1/3840-1/61440-17/245760-1/61440-1/192
      =54679/245760 ∧ (2/9 : ℚ)<54679/245760 := by norm_num

/-- First-odd-parity corrections in the two source classes. -/
theorem refined_margins :
    (2/3 : ℚ)-4/15-1/12-1/240-1/768-1/3840-1/15360-1/12288-1/15360-1/192
      =6257/20480 ∧
    (1/3 : ℚ)-4/75-2/75-1/300-17/19200-1/4800-1/76800-17/307200-1/76800-1/192
      =74839/307200 := by norm_num

theorem overshoot_corrections :
    (8/9 : ℚ)<1 ∧ 1<(4/3 : ℚ) ∧ (9/64 : ℚ)-1/9=17/576 ∧
    (64/81 : ℚ)<1 ∧ 1<(32/27 : ℚ) ∧ (81/4096 : ℚ)-1/81=2465/331776 := by
  norm_num

/-- Final exact fractions in the written all-scales counting theorem. -/
theorem strong_margins :
    (6257/20480 : ℚ)+2465/331776+17/576=284051/829440 ∧
    (1/3 : ℚ)<284051/829440 ∧
    (74839/307200 : ℚ)+2465/331776=1041139/4147200 ∧
    (1/4 : ℚ)<1041139/4147200 := by norm_num

#print axioms complete
#print axioms odd_counts
#print axioms common_margin
#print axioms zero_margin
#print axioms refined_margins
#print axioms overshoot_corrections
#print axioms strong_margins
end RampShadow.Postpeak.SignedOrigins
