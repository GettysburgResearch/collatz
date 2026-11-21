import CollatzGlobal.CommonRank
import CollatzGlobal.PsiNormalization

/-! Exact move guards for the common height/clock rank. The inequalities
below establish strict rank descent; actual ordinary certificate transport
remains a separate premise, supplied by each rule's orbit proof. -/

open CollatzReverseBasin

namespace CollatzGlobal

/-- A finite forward move may increase the ordinary value, provided its
relative growth is paid for by the consumed source-certificate clocks. -/
theorem scoreLT_forward_guard {n q d t : Nat} (ht : t ≤ d)
    (guard : (q+1)*200^t < (n+1)*201^t) :
    ScoreLT (q,d-t) (n,d) := by
  let e := d-t
  have he : d = t+e := by dsimp [e]; omega
  have sub : d-t = e := rfl
  unfold ScoreLT rankNumerator rankDenominator
  rw [sub, he, Nat.pow_add, Nat.pow_add]
  have pos : 0 < 201^e*200^e :=
    Nat.mul_pos (Nat.pow_pos (by decide)) (Nat.pow_pos (by decide))
  calc
    (q+1)*201^e*(200^t*200^e) = ((q+1)*200^t)*(201^e*200^e) := by grind
    _ < ((n+1)*201^t)*(201^e*200^e) := Nat.mul_lt_mul_of_pos_right guard pos
    _ = (n+1)*(201^t*201^e)*200^e := by grind

/-- A height contraction may add source-certificate clocks. The exact
integer test bounds their full exponential cost, for every starting clock. -/
theorem scoreLT_height_clock_guard {n m d a b : Nat}
    (height : (m+1)*3^b ≤ (n+1)*2^a)
    (guard : 402^a < 200^a*3^b) :
    ScoreLT (m,d+a) (n,d) := by
  have hp : 2^a*201^a = 402^a := by
    rw [← Nat.mul_pow]
  have multiplied : ((m+1)*201^a)*3^b < ((n+1)*200^a)*3^b := by
    calc
      ((m+1)*201^a)*3^b = ((m+1)*3^b)*201^a := by grind
      _ ≤ ((n+1)*2^a)*201^a := Nat.mul_le_mul_right _ height
      _ = (n+1)*402^a := by rw [Nat.mul_assoc, hp]
      _ < (n+1)*(200^a*3^b) := Nat.mul_lt_mul_of_pos_left guard (by omega)
      _ = ((n+1)*200^a)*3^b := by grind
  have small := Nat.lt_of_mul_lt_mul_right multiplied
  unfold ScoreLT rankNumerator rankDenominator
  simp only [Nat.pow_add]
  have pos : 0 < 201^d*200^d :=
    Nat.mul_pos (Nat.pow_pos (by decide)) (Nat.pow_pos (by decide))
  calc
    (m+1)*(201^d*201^a)*200^d = ((m+1)*201^a)*(201^d*200^d) := by grind
    _ < ((n+1)*200^a)*(201^d*200^d) := Nat.mul_lt_mul_of_pos_right small pos
    _ = (n+1)*201^d*(200^d*200^a) := by grind

/-- The observed height-increasing return is admitted by the common rank
for every supplied certificate long enough to consume its thirty clocks. -/
theorem expanding_return_rank_guard : (21091+1)*200^30 < (19483+1)*201^30 := by
  decide

theorem expanding_return_decreases_common_rank {d : Nat} (hd : 30 ≤ d) :
    ScoreLT (21091,d-30) (19483,d) :=
  scoreLT_forward_guard hd expanding_return_rank_guard

/-- All exponent pairs used by the eight frozen negative-reference rules
pass the same exact clock-cost inequality. Constants and legality are checked
separately in the source-coordinate transport note. -/
theorem negative_template_clock_guards :
    402^7 < 200^7*3^5 ∧ 402^9 < 200^9*3^6 ∧
    402^11 < 200^11*3^7 ∧ 402^10 < 200^10*3^7 := by decide

/-- Exact source-coordinate transport for a negative-offset template in the
psi chart. The known source is `81*M+2`, not its unknown target `27*M+1`.
The original witness transformation must separately supply clock `d+a`. -/
theorem psi_template_common_rank {M M' C d a b : Nat}
    (affine : 3^b*M'+C = 2^a*M)
    (offset : 3^b ≤ 27*C+2^a)
    (guard : 402^a < 200^a*3^b) :
    ScoreLT (81*M'+2,d+a) (81*M+2,d) := by
  apply scoreLT_height_clock_guard (b := b) ?_ guard
  have h1 := congrArg (fun x : Nat => 81*x) affine
  have h2 := Nat.mul_le_mul_left 3 offset
  grind

/-- The offset tests for every frozen row, in the actual known psi-source
coordinate. These are distinct from the binary-source coordinate tests. -/
theorem psi_template_height_guards :
    3^5 ≤ 27*69+2^7 ∧ 3^6 ≤ 27*271+2^9 ∧
    3^6 ≤ 27*243+2^9 ∧ 3^7 ≤ 27*1069+2^11 ∧
    3^7 ≤ 27*1077+2^11 ∧ 3^7 ≤ 27*1053+2^11 ∧
    3^7 ≤ 27*963+2^11 ∧ 3^7 ≤ 27*579+2^10 := by decide

/-- Specialization to the convergent source coordinate of a psi obligation.
The displayed guard is exactly the score comparison after a psi return. -/
theorem psi_return_common_rank {m d t : Nat} (hm : 0 < m)
    (ht : t ≤ d) (hr : PsiReturn m t)
    (guard : (orbit m t)*200^t < m*201^t) :
    ScoreLT (orbit (3*m-1) t,d-t) (3*m-1,d) := by
  rw [hr]
  have positive := orbit_positive hm t
  apply scoreLT_forward_guard ht
  have h := Nat.mul_lt_mul_of_pos_left guard (show 0<3 by decide)
  have a : 3*orbit m t-1+1 = 3*orbit m t := by omega
  have b : 3*m-1+1 = 3*m := by omega
  rw [a,b]
  simpa only [Nat.mul_assoc] using h

end CollatzGlobal
