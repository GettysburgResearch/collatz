import PostWords

namespace RampShadow.FirstCrossing

/-- Read inverse branches as rational affine maps on x+1.
    The coefficient just before each listed branch is at least one.
    The final coefficient may be the first one below one. -/
inductive Prefix (c₀ B₀ : ℚ) : ℕ → ℕ → ℚ → ℚ → Prop
  | start : Prefix c₀ B₀ 0 0 c₀ B₀
  | even {d b c B} : Prefix c₀ B₀ d b c B → 1 ≤ c →
      Prefix c₀ B₀ (d+1) b (2*c) (2*B)
  | odd {d b c B} : Prefix c₀ B₀ d b c B → 1 ≤ c →
      Prefix c₀ B₀ (d+1) (b+1) (2*c/3) ((2*B+1)/3)

theorem prefix_identity {c₀ B₀ d b c B} (P : Prefix c₀ B₀ d b c B) :
    (3:ℚ)^b*c=2^d*c₀ := by
  induction P with
  | start => simp
  | even P _ IH => rw [pow_succ];linear_combination 2*IH
  | odd P _ IH => rw [pow_succ,pow_succ];linear_combination 2*IH

/-- With no prior crossing, the normalized offset gains at most a half
    at each reversed odd departure. -/
theorem normalized_offset {c₀ B₀ d b c B} (P : Prefix c₀ B₀ d b c B)
    (start : B₀ ≤ c₀) : 2*B ≤ c*(2+b) := by
  induction P with
  | start => simp;linarith only [start]
  | even P _ IH => nlinarith only [IH]
  | odd P H IH => push_cast;nlinarith only [IH,H]

/-- A smaller point whose inverse coefficient stays above one forces
    an elementary height cutoff of order b*3^b. -/
theorem crossing_free_cutoff {a d b : ℕ} {B₀ c B m n : ℚ}
    (P : Prefix ((2:ℚ)^a) B₀ d b c B) (start : B₀ ≤ 2^a)
    (gain : 1<c) (small : m<n) (eq : m=c*(n+1)-B) :
    2*n < b*((3:ℚ)^b+1) := by
  have I := prefix_identity P
  rw [←pow_add] at I
  have p : (0:ℚ)<3^b := by positivity
  have natlt : (3:ℕ)^b<2^(d+a) := by
    exact_mod_cast (show (3:ℚ)^b<2^(d+a) by nlinarith only [I,mul_lt_mul_of_pos_left gain p])
  have gap : (3:ℚ)^b+1≤2^(d+a) := by exact_mod_cast natlt
  have slope : c≤((3:ℚ)^b+1)*(c-1) := by nlinarith only [gap,I]
  have O := normalized_offset P start
  have H : 2*n*(c-1)<b*c := by nlinarith only [eq,small,O]
  have J := mul_le_mul_of_nonneg_left slope (show 0≤(b:ℚ) by positivity)
  exact (mul_lt_mul_iff_left₀ (sub_pos.mpr gain)).mp (by nlinarith only [H,J])

/-- Sum the ternary cylinder sizes of nodes stopped at the first strict
    contraction, with finite remaining binary depth. Overlaps are allowed. -/
def stoppedMass (a : ℕ) : ℕ → ℕ → ℕ → ℚ
  | 0,d,b => if 2^(a+d)<(3:ℕ)^b then 1/(3:ℚ)^b else 0
  | h+1,d,b => if 2^(a+d)<(3:ℕ)^b then 1/(3:ℚ)^b
                else stoppedMass a h (d+1) b+stoppedMass a h (d+1) (b+1)

private theorem crossing_mass (c b : ℕ) (H : 2^c<(3:ℕ)^b) :
    1/(3:ℚ)^b≤(3:ℚ)^b/4^c := by
  have cmp : (2:ℚ)^c < 3^b := by exact_mod_cast H
  have X : (4:ℚ)^c=((2:ℚ)^c)^2 := by
    rw [show (4:ℚ)=2^2 by norm_num,←pow_mul,mul_comm 2 c,pow_mul]
  rw [div_le_div_iff₀ (by positivity) (by positivity),X,one_mul,←sq]
  exact pow_le_pow_left₀ (by positivity) cmp.le 2

/-- Weaver's squared-gain prefix-free estimate, in finite tree form. -/
theorem stopped_mass_bound (a h d b : ℕ) :
    stoppedMass a h d b ≤ (3:ℚ)^b/4^(a+d) := by
  induction h generalizing d b with
  | zero =>
    simp only [stoppedMass]
    split
    · exact crossing_mass _ _ ‹_›
    · positivity
  | succ h IH =>
    simp only [stoppedMass]
    split
    · exact crossing_mass _ _ ‹_›
    · have E := IH (d+1) b
      have O := IH (d+1) (b+1)
      have S : (3:ℚ)^b/4^(a+(d+1))+3^(b+1)/4^(a+(d+1))=3^b/4^(a+d) := by
        rw [show a+(d+1)=(a+d)+1 by omega,pow_succ,pow_succ];ring
      linarith only [E,O,S]

end RampShadow.FirstCrossing

#print axioms RampShadow.FirstCrossing.normalized_offset
#print axioms RampShadow.FirstCrossing.crossing_free_cutoff
#print axioms RampShadow.FirstCrossing.stopped_mass_bound
