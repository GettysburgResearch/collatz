import Mathlib.Tactic.Ring
import Mathlib.Tactic.Positivity

/-! All parameters below are ordinary natural numbers. The two laws are the
shortcut Collatz invariance equations on even and odd inputs. -/
namespace HeadRayRouting

variable {α : Type*} (f : ℕ → α)

/-- A free dyadic multiple keeps its component label. -/
theorem dyadic_label (he : ∀ n, f (2*n) = f n) (k n : ℕ) :
    f (2^k*n) = f n := by
  induction k with
  | zero => simp
  | succ k ih =>
    rw [pow_succ, show 2^k * 2 * n = 2 * (2^k*n) by ring, he, ih]

/-- A block of p initial odd steps on the entire positive progression. -/
theorem odd_run_label (ho : ∀ n, f (2*n+1) = f (3*n+2))
    (p v : ℕ) (hv : 0 < v) : f (2^p*v-1) = f (3^p*v-1) := by
  induction p generalizing v with
  | zero => simp
  | succ p ih =>
    have a : 0 < 2^p*v := Nat.mul_pos (by positivity) hv
    have h₁ : 2^(p+1)*v - 1 = 2*(2^p*v-1)+1 := by
      rw [pow_succ, show 2^p*2*v = 2*(2^p*v) by ring]; omega
    have h₂ : 3*(2^p*v-1)+2 = 2^p*(3*v)-1 := by
      rw [show 2^p*(3*v) = 3*(2^p*v) by ring]; omega
    rw [h₁, ho, h₂, ih (3*v) (by omega), pow_succ, Nat.mul_assoc]

/-- Every unit modulo 27 allows the same three required ternary precisions. -/
theorem unit_phase27 (u : ℕ) (hu : u%3 ≠ 0) :
    ∃ k < 18, (2^k * u)%27 = 26 := by
  have tab : ∀ r : Fin 27, r.val%3 ≠ 0 →
      ∃ k : Fin 18, (2^k.val * r.val)%27 = 26 := by decide
  have hr : (u%27)%3 ≠ 0 := by simpa [Nat.mod_mod_of_dvd u (by decide : 3 ∣ 27)] using hu
  obtain ⟨k, hk⟩ := tab ⟨u%27, Nat.mod_lt _ (by decide)⟩ hr
  refine ⟨k.val, k.isLt, ?_⟩
  simpa only [Nat.mul_mod, Nat.mod_mod] using hk

/-- The exact power returns the ternary phase at simultaneous period 18. -/
theorem repeat_phase27 (u k t : ℕ) (hk : (2^k*u)%27=26) :
    (2^(k+18*t)*u)%27=26 := by
  have h : (2^18:ℕ)%27=1 := by decide
  rw [pow_add, pow_mul]
  rw [show 2^k*(2^18)^t*u = (2^k*u)*(2^18)^t by ring, Nat.mul_mod,
      Nat.pow_mod, h, one_pow, Nat.mod_eq_of_lt (by decide : 1 < 27),
      Nat.mul_one, hk]

/-- The parent and one literal head child realize their desired true labels. -/
theorem exact_head_labels (he : ∀ n, f (2*n)=f n)
    (ho : ∀ n, f (2*n+1)=f (3*n+2)) (p a k u v r : ℕ)
    (hfour : 3^a * 3^p = 81) (hsuf : r + 3^a*2^p = 81)
    (hv : 0 < v) (hphase : 3^p*v = 2^k*u + 1) :
    let m := 2^p*v-1
    f m = f u ∧ f (81*m+r) = f (3^a*u) ∧
      81*m+r = 2^(p+k)*(3^a*u) := by
  dsimp
  have hp : 0 < 2^p*v := Nat.mul_pos (by positivity) hv
  have heq : 81*(2^p*v-1)+r = 2^(p+k)*(3^a*u) := by
    rw [pow_add]
    have hm : 81*(2^p*v-1)+81 = 81*(2^p*v) := by omega
    have hcalc : 2^p*2^k*(3^a*u) + 3^a*2^p = 81*(2^p*v) := by
      calc
        _ = (3^a*2^p)*(2^k*u+1) := by ring
        _ = (3^a*2^p)*(3^p*v) := by rw [hphase]
        _ = (3^a*3^p)*(2^p*v) := by ring
        _ = _ := by rw [hfour]
    omega
  refine ⟨?_, ?_, heq⟩
  · rw [odd_run_label f ho p v hv, hphase, Nat.add_sub_cancel,
        dyadic_label f he]
  · rw [heq, dyadic_label f he]

/-- The four tests remove every multiple of 3 from a component label. -/
theorem power_label (h81 : ∀ n, f (81*n)=f n) (u : ℕ)
    (hu : ∀ j < 4, f (3^j*u)=f u) (k : ℕ) : f (3^k*u)=f u := by
  induction k using Nat.strong_induction_on with
  | h k ih =>
    by_cases hk : k<4
    · exact hu k hk
    · have heq : k = (k-4)+4 := by omega
      have hless : k-4<k := by omega
      calc
        f (3^k*u) = f (81*(3^(k-4)*u)) := by
          congr 1
          calc
            3^k*u = 3^((k-4)+4)*u := by rw [← heq]
            _ = _ := by rw [pow_add]; ring
        _ = f (3^(k-4)*u) := h81 _
        _ = f u := ih (k-4) hless

private theorem exists_unit_part (n : ℕ) (hn : 0<n) :
    ∃ k u : ℕ, u%3 ≠ 0 ∧ n=3^k*u := by
  induction n using Nat.strong_induction_on with
  | h n ih =>
    by_cases h₃ : n%3=0
    · have nd : n=3*(n/3) := by omega
      obtain ⟨k,u,hu,hku⟩ := ih (n/3) (by omega) (by omega)
      refine ⟨k+1,u,hu, ?_⟩
      calc
        n = 3*(n/3) := nd
        _ = 3*(3^k*u) := by rw [hku]
        _ = _ := by rw [pow_succ]; ring
    · exact ⟨0,n,h₃,by simp⟩

theorem tripling_from_four (h81 : ∀ n, f (81*n)=f n)
    (hunit : ∀ u : ℕ, u%3 ≠ 0 → ∀ j<4, f (3^j*u)=f u)
    (n : ℕ) (hn : 0<n) : f (3*n)=f n := by
  obtain ⟨k,u,hu,rfl⟩ := exists_unit_part n hn
  rw [show 3*(3^k*u) = 3^(k+1)*u by rw [pow_succ]; ring,
      power_label f h81 u (hunit u hu), power_label f h81 u (hunit u hu)]

#print axioms dyadic_label
#print axioms odd_run_label
#print axioms unit_phase27
#print axioms repeat_phase27
#print axioms exact_head_labels
#print axioms tripling_from_four

end HeadRayRouting
