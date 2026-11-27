import Mathlib.Logic.Function.Iterate
import Mathlib.Data.Rat.Cast.Order
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

/-! The arithmetic odd map has valuation e(x) and corrected height P,
with P(Ux)·2^e(x)=3P(x).  The clock variables below count its actual
iterations.  No probability or density statement is assumed. -/

namespace OddPosterior

variable {A : Type*} {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

def sync (U : A → A) (m x : A) : Prop := ∃ k : ℕ, U^[k] x = U^[k] m

/-- Two distinct members of a synchronous class of an injective orbit
cannot both lie on the forward orbit of any common ordinary source. -/
theorem disjoint_predecessors {U : A → A} {m x y z : A}
    (inj : Function.Injective (fun k : ℕ => U^[k] m)) (hx : sync U m x)
    (hy : sync U m y) {i j : ℕ} (ex : U^[i] z = x) (ey : U^[j] z = y) : x = y := by
  obtain ⟨kx, hx⟩ := hx
  obtain ⟨ky, hy⟩ := hy
  let N := kx + ky
  have ax : U^[N] x = U^[N] m := by
    dsimp [N]
    rw [Nat.add_comm kx, Function.iterate_add_apply, hx, ← Function.iterate_add_apply]
  have ay : U^[N] y = U^[N] m := by
    dsimp [N]
    rw [Function.iterate_add_apply, hy, ← Function.iterate_add_apply]
  have left : U^[N+i+j] z = U^[j+N] m := by
    rw [show N+i+j = j+(N+i) by omega, Function.iterate_add_apply,
      Function.iterate_add_apply, ex, ax, ← Function.iterate_add_apply]
  have right : U^[N+i+j] z = U^[i+N] m := by
    rw [show N+i+j = i+(N+j) by omega, Function.iterate_add_apply,
      Function.iterate_add_apply, ey, ay, ← Function.iterate_add_apply]
  have same : j+N = i+N := inj (left.symm.trans right)
  have : i = j := by omega
  subst j
  exact ex.symm.trans ey

/-- Every old source persists when both actual odd trajectories advance. -/
theorem persist {U : A → A} {x m : A} {k : ℕ} (h : U^[k] x = U^[k] m) :
    U^[k+1] x = U^[k+1] m := by
  simpa only [Function.iterate_succ_apply'] using congrArg U h

def total (U : A → A) (e : A → ℕ) (x : A) : ℕ → ℕ
  | 0 => 0
  | k+1 => total U e x k + e (U^[k] x)

omit [LinearOrder K] [IsStrictOrderedRing K] in
theorem accumulated (U : A → A) (e : A → ℕ) (P : A → K)
    (edge : ∀ x, P (U x) * 2 ^ e x = 3 * P x) (x : A) (k : ℕ) :
    P (U^[k] x) * 2 ^ total U e x k = 3 ^ k * P x := by
  induction k with
  | zero => simp [total]
  | succ k ih =>
    rw [total, pow_add, Function.iterate_succ_apply', pow_succ]
    calc
      P (U (U^[k] x)) * (2 ^ total U e x k * 2 ^ e (U^[k] x)) =
          (P (U (U^[k] x)) * 2 ^ e (U^[k] x)) * 2 ^ total U e x k := by ring
      _ = (3 ^ k * 3) * P x := by rw [edge, mul_assoc, ih]; ring

/-- The posterior term from any common odd-clock source uses a ratio of
its actual corrected heights, independent of the deletion clock. -/
theorem relative_weight (U : A → A) (e : A → ℕ) (P : A → K)
    (edge : ∀ x, P (U x) * 2 ^ e x = 3 * P x) {x m : A} {k : ℕ}
    (merge : U^[k] x = U^[k] m) (pos : 0 < P x) :
    (2 : K) ^ total U e m k / 2 ^ total U e x k = P m / P x := by
  have hx := accumulated U e P edge x k
  have hm := accumulated U e P edge m k
  rw [merge] at hx
  rw [div_eq_div_iff (by positivity) pos.ne']
  apply mul_left_cancel₀ (show (3:K)^k ≠ 0 by positivity)
  calc
    3 ^ k * (2 ^ total U e m k * P x) = 2 ^ total U e m k * (3 ^ k * P x) := by ring
    _ = 2 ^ total U e m k * (P (U^[k] m) * 2 ^ total U e x k) := by rw [hx]
    _ = (P (U^[k] m) * 2 ^ total U e m k) * 2 ^ total U e x k := by ring
    _ = 3 ^ k * (P m * 2 ^ total U e x k) := by rw [hm]; ring

#print axioms disjoint_predecessors
#print axioms persist
#print axioms relative_weight

end OddPosterior
