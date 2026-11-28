import Mathlib.Algebra.Order.Field.Rat
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Algebra.Order.GroupWithZero.Basic
import Mathlib.Tactic.Ring

/-!
The dyadic input of the true affine native recurrence is U(n)=2^E(n).
One actual valuation mismatch gives a nonzero cross product of four
consecutive shifted inputs. A block of proportional inputs is shorter
than the degree of any monic recurrence of the unfolded native state V.
-/

set_option autoImplicit false

namespace Collatz.RotationRecurrenceRank

def Input (E : ℕ → ℕ) (n : ℕ) : ℚ := 2 ^ E n

def Recurs {d : ℕ} (c : Fin d → ℚ) (v : ℕ → ℚ) : Prop :=
  ∀ n, v (n + d) = ∑ j : Fin d, c j * v (n + j.val)

private theorem shift_sub {d : ℕ} {c : Fin d → ℚ} {v : ℕ → ℚ}
    (hv : Recurs c v) (s : ℕ) (k : ℚ) :
    Recurs c (fun n => v (n+s) - k * v n) := by
  intro n
  change v (n+d+s) - k * v (n+d) = ∑ j : Fin d, c j * (v (n+j.val+s) - k * v (n+j.val))
  rw [show n+d+s = n+s+d by omega, hv, hv, Finset.mul_sum, ← Finset.sum_sub_distrib]
  apply Finset.sum_congr rfl
  intro i _
  rw [show n+s+i.val = n+i.val+s by omega]
  ring

private theorem propagate {d start : ℕ} {c : Fin d → ℚ} {w : ℕ → ℚ}
    (hw : Recurs c w) (init : ∀ j < d, w (start+j) = 0) :
    ∀ t, w (start+t) = 0 := by
  intro t
  induction t using Nat.strong_induction_on with
  | h t ih =>
    by_cases ht : t < d
    · exact init t ht
    · rw [show start+t = (start+(t-d))+d by omega, hw]
      apply Finset.sum_eq_zero
      intro j _
      have hj := j.isLt
      rw [show start+(t-d)+j.val = start+((t-d)+j.val) by omega, ih _ (by omega), mul_zero]

/-- A real circular run of proportional dyadic inputs fits in fewer than
d positions. The comparison is globally nonzero by a native mismatch. -/
theorem native_run_lt {d p A shift start length : ℕ} (hp : 0 < p)
    (E : ℕ → ℕ) (V : ℕ → ℚ) (c : Fin d → ℚ)
    (clock : ∀ n, E (n+p) = E n + A)
    (step : ∀ n, V (n+1) - 3 * V n = Input E n) (recur : Recurs c V)
    (mismatch : ∃ i, Input E (i+1+shift) * Input E i ≠
                      Input E (i+shift) * Input E (i+1))
    (k : ℚ) (run : ∀ j < length, Input E (start+j+shift) = k * Input E (start+j)) :
    length < d := by
  let w (n : ℕ) : ℚ := Input E (n+shift) - k * Input E n
  have hu : Recurs c (Input E) := by
    have h := shift_sub recur 1 3
    simpa only [step] using h
  have hw : Recurs c w := shift_sub hu shift k
  by_contra! hlong
  have zero : ∀ t, w (start+t) = 0 := propagate hw (fun j hj => by
    change Input E (start+j+shift) - k * Input E (start+j) = 0
    rw [run j (lt_of_lt_of_le hj hlong), sub_self])
  have lap (n : ℕ) : Input E (n+p) = (2:ℚ)^A * Input E n := by
    simp only [Input, clock, pow_add, mul_comm]
  have wh (n : ℕ) : w (n+p) = (2:ℚ)^A * w n := by
    change Input E (n+p+shift) - k * Input E (n+p) =
      (2:ℚ)^A * (Input E (n+shift) - k * Input E n)
    rw [show n+p+shift = n+shift+p by omega, lap, lap]
    ring
  have laps (n t : ℕ) : w (n+t*p) = ((2:ℚ)^A)^t * w n := by
    induction t with
    | zero => simp
    | succ t ih =>
      rw [Nat.succ_mul, ← Nat.add_assoc, wh, ih, pow_succ]
      ring
  have flat (n : ℕ) : Input E (n+shift) = k * Input E n := by
    have hsp : start ≤ start*p := Nat.le_mul_of_pos_right start hp
    have hz : w (n+start*p) = 0 := by
      simpa only [show start+(n+start*p-start) = n+start*p by omega] using
        zero (n+start*p-start)
    rw [laps] at hz
    exact sub_eq_zero.mp ((mul_eq_zero.mp hz).resolve_left (pow_ne_zero _ (pow_ne_zero _ (by decide))))
  obtain ⟨i, hi⟩ := mismatch
  apply hi
  rw [flat (i+1), flat i]
  ring

/-- A partition of one lap into runs between actual unequal valuations.
Only the interior valuation agreements and the covered length are supplied;
the dyadic comparison factors are recovered at the true run starts. -/
theorem native_budget_rank {d p A shift u : ℕ} (hp : 0 < p)
    (a E : ℕ → ℕ) (V : ℕ → ℚ) (c : Fin d → ℚ)
    (cumul : ∀ n, E (n+1) = E n + a n) (clock : ∀ n, E (n+p) = E n + A)
    (step : ∀ n, V (n+1) - 3 * V n = Input E n) (recur : Recurs c V)
    (mismatch : ∃ i, a (i+shift) ≠ a i)
    (start length : Fin u → ℕ) (cover : (∑ i, length i) = p)
    (interior : ∀ i j, j+1 < length i → a (start i+j+shift) = a (start i+j)) :
    p ≤ u * (d-1) := by
  obtain ⟨z, hz⟩ := mismatch
  have cross : ∃ i, Input E (i+1+shift) * Input E i ≠
                      Input E (i+shift) * Input E (i+1) := by
    refine ⟨z, fun heq => hz ?_⟩
    simp only [Input, ← pow_add] at heq
    have hE := (pow_right_injective₀ (by decide : (0:ℚ) < 2)
                      (by decide : (2:ℚ) ≠ 1)) heq
    rw [show z+1+shift = (z+shift)+1 by omega, cumul, cumul] at hE
    omega
  have advance (n : ℕ) : Input E (n+1) = Input E n * (2:ℚ)^(a n) := by
    simp only [Input, cumul, pow_add]
  let ratio (i : Fin u) := Input E (start i+shift) / Input E (start i)
  have runs (i : Fin u) (j : ℕ) (hj : j < length i) :
      Input E (start i+j+shift) = ratio i * Input E (start i+j) := by
    induction j with
    | zero =>
      have hn : Input E (start i) ≠ 0 := pow_ne_zero _ (by decide)
      simp [ratio, hn]
    | succ j ih =>
      calc
        _ = Input E (start i+j+shift) * (2:ℚ)^(a (start i+j+shift)) := by
          rw [show start i+j.succ+shift = (start i+j+shift)+1 by omega, advance]
        _ = ratio i * (Input E (start i+j) * (2:ℚ)^(a (start i+j))) := by
          rw [interior i j hj, ih (by omega), mul_assoc]
        _ = _ := by rw [← advance, Nat.add_assoc]
  rw [← cover]
  calc
    _ ≤ ∑ _i : Fin u, (d-1) := Finset.sum_le_sum fun i _ => by
      have := native_run_lt hp E V c clock step recur cross (ratio i) (runs i)
      omega
    _ = _ := by simp

#print axioms native_run_lt
#print axioms native_budget_rank

end Collatz.RotationRecurrenceRank
