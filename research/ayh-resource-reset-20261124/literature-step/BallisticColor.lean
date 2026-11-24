import TernaryHeadDescent
import OffsetDescent

/-! A color-discordant pair has an eventually linear signed odd-count excess.
The estimates use actual positive shortcut trajectories and the checked basin
below 600. No upper bound on a hitting time is assumed or concluded. -/
namespace CollatzShell.TernaryHead

open OffsetDescent

private theorem pos_orbit {n : ℕ} (hn : 0 < n) (t : ℕ) : 0 < orbit t n := by
  induction t generalizing n with
  | zero => exact hn
  | succ t ih => apply ih; unfold step; split <;> omega

private theorem bad_floor {n : ℕ} (hn : 0 < n) (bad : ¬ Basin n) (t : ℕ) :
    600 ≤ orbit t n := by
  by_contra! h
  obtain ⟨k,hk⟩ := low_basin (pos_orbit hn t) h
  exact bad ⟨t+k, by simpa [orbit_add] using hk⟩

private theorem odd_power_bound {n : ℕ} (hn : 64 ≤ n) : (3*n+1)^5 ≤ 2^8*n^5 := by
  obtain ⟨k,rfl⟩ := Nat.exists_eq_add_of_le hn
  nlinarith only [Nat.zero_le k, Nat.zero_le (k^2), Nat.zero_le (k^3),
    Nat.zero_le (k^4), Nat.zero_le (k^5)]

private theorem step_power_bound {n : ℕ} (hn : 64 ≤ n) :
    2^5*(step n)^5 ≤ 2^(8*(n%2))*n^5 := by
  by_cases even : n%2=0
  · have eq : 2*step n=n := by simp [step, even]; omega
    rw [← mul_pow, eq, even]; simp
  · have eq : 2*step n=3*n+1 := by simp [step, even]; omega
    have one : n%2=1 := by omega
    rw [← mul_pow, eq, one, Nat.mul_one]
    exact odd_power_bound hn

private theorem prefix_power_bound {n : ℕ} (t : ℕ) (safe : ∀ i < t, 64 ≤ orbit i n) :
    2^(5*t)*(orbit t n)^5 ≤ 2^(8*oddCount t n)*n^5 := by
  induction t generalizing n with
  | zero => simp [oddCount, orbit]
  | succ t ih =>
    have first := step_power_bound (safe 0 (by omega))
    have tail := ih (n := step n) (fun i hi => safe (i+1) (by omega))
    calc
      2^(5*(t+1))*(orbit (t+1) n)^5 = 2^5*(2^(5*t)*(orbit t (step n))^5) := by
        simp only [orbit]; ring
      _ ≤ 2^5*(2^(8*oddCount t (step n))*(step n)^5) := Nat.mul_le_mul_left _ tail
      _ = 2^(8*oddCount t (step n))*(2^5*(step n)^5) := by ring
      _ ≤ 2^(8*oddCount t (step n))*(2^(8*(n%2))*n^5) := Nat.mul_le_mul_left _ first
      _ = 2^(8*oddCount (t+1) n)*n^5 := by simp only [oddCount]; ring

/-- All finite counts on a positive non-one-basin arm. `L` may be any binary
height bound, and `t` is unrestricted. -/
theorem bad_odd_excess {n L : ℕ} (hn : 0 < n) (bad : ¬ Basin n) (size : n ≤ 2^L)
    (t : ℕ) : 5*t ≤ 8*oddCount t n + 5*L := by
  have safe := bad_floor hn bad
  have hp := prefix_power_bound t (n := n) (fun i _ => (by omega : 64 ≤ 600).trans (safe i))
  apply (Nat.pow_le_pow_iff_right (by decide : 1 < 2)).1
  calc
    2^(5*t) ≤ 2^(5*t)*(orbit t n)^5 := Nat.le_mul_of_pos_right _ (by have := pos_orbit hn t; positivity)
    _ ≤ 2^(8*oddCount t n)*n^5 := hp
    _ ≤ 2^(8*oddCount t n)*(2^L)^5 := Nat.mul_le_mul_left _ (Nat.pow_le_pow_left size 5)
    _ = 2^(8*oddCount t n+5*L) := by ring

private theorem count_le (t n : ℕ) : oddCount t n ≤ t := by
  induction t generalizing n with
  | zero => simp [oddCount]
  | succ t ih => simp only [oddCount]; have := ih (step n); omega

private theorem terminal_count (r : ℕ) : 2*oddCount r 1 ≤ r+1 := by
  have e : r = 2*(r/2)+(r%2) := by omega
  conv_lhs => rw [e]
  rw [oddCount_add, oddCount_twice_one, orbit_twice_one]
  have := count_le (r%2) 1
  omega

/-- The additive allowance is an actual first-hit bound supplied by the caller. -/
theorem good_odd_excess {u q : ℕ} (hit : orbit q u = 1) (t : ℕ) :
    2*oddCount t u ≤ t+q+1 := by
  by_cases later : q ≤ t
  · obtain ⟨r,rfl⟩ := Nat.exists_eq_add_of_le later
    rw [oddCount_add, hit]
    have := count_le q u
    have := terminal_count r
    omega
  · have := count_le t u
    omega

/-- The signed excess of the bad arm over the good arm is at least
`(t - 5*L - 4*q - 4)/8` at every physical clock. This also applies when the
two starts are an actual four-trit head edge in either orientation. -/
theorem color_discordant_ballistic {n u L q : ℕ} (hn : 0<n) (bad : ¬ Basin n)
    (size : n ≤ 2^L) (hit : orbit q u = 1) (t : ℕ) :
    t + 8*oddCount t u ≤ 8*oddCount t n + 5*L + 4*q + 4 := by
  have := bad_odd_excess hn bad size t
  have := good_odd_excess hit t
  omega

/-- The allowance depends only on the height loss over this window. At a
future minimum it is zero regardless of the size of the bad arm. -/
theorem bad_window_height_ratio {n L : ℕ} (hn : 0<n) (bad : ¬ Basin n) (t : ℕ)
    (ratio : n ≤ 2^L*orbit t n) : 5*t ≤ 8*oddCount t n + 5*L := by
  have safe := bad_floor hn bad
  have hp := prefix_power_bound t (n := n) (fun i _ => (by omega : 64 ≤ 600).trans (safe i))
  apply (Nat.pow_le_pow_iff_right (by decide : 1 < 2)).1
  apply Nat.le_of_mul_le_mul_right (c := (orbit t n)^5) _ (by have := pos_orbit hn t; positivity)
  calc
    2^(5*t)*(orbit t n)^5 ≤ 2^(8*oddCount t n)*n^5 := hp
    _ ≤ 2^(8*oddCount t n)*(2^L*orbit t n)^5 := Nat.mul_le_mul_left _ (Nat.pow_le_pow_left ratio 5)
    _ = 2^(8*oddCount t n+5*L)*(orbit t n)^5 := by ring

private theorem terminal_state (r : ℕ) : orbit r 1 = 1 ∨ orbit r 1 = 2 := by
  have e : r = 2*(r/2)+(r%2) := by omega
  rw [e, orbit_add, orbit_twice_one]
  rcases (by omega : r%2=0 ∨ r%2=1) with h|h <;> rw [h] <;> decide

private theorem terminal_pair_bound {x : ℕ} (term : x=1 ∨ x=2) (t : ℕ) :
    2*oddCount t x ≤ t+1 := by
  rcases term with rfl|rfl
  · exact terminal_count t
  · cases t with
    | zero => decide
    | succ t => change 2*(0+oddCount t 1) ≤ t+1+1; have := terminal_count t; omega

/-- Above any clock there is a real clock at which the two arms already
have uniform linear separation on *every* subsequent block. The clock may
depend on the infinite bad trajectory; no stopping-time property is assumed. -/
theorem discordant_future_minimum_windows {n u : ℕ} (hn : 0<n) (bad : ¬ Basin n)
    (good : Basin u) (a : ℕ) : ∃ s, a ≤ s ∧
    (∀ b, orbit s n ≤ orbit (s+b) n) ∧
    (∀ b, b + 8*oddCount b (orbit s u) ≤ 8*oddCount b (orbit s n) + 4) := by
  classical
  obtain ⟨q,hq⟩ := good
  have existsValue : ∃ v : ℕ, ∃ s : ℕ, max a q ≤ s ∧ orbit s n=v :=
    ⟨orbit (max a q) n, max a q, le_rfl, rfl⟩
  obtain ⟨s,hs,he⟩ := Nat.find_spec existsValue
  have hmin (b : ℕ) : orbit s n ≤ orbit (s+b) n := by
    rw [he]
    exact Nat.find_min' existsValue ⟨s+b,by omega,rfl⟩
  refine ⟨s,by omega,hmin,?_⟩
  have badTail : ¬ Basin (orbit s n) := by
    rintro ⟨k,hk⟩
    exact bad ⟨s+k,by simpa [orbit_add] using hk⟩
  have term : orbit s u = 1 ∨ orbit s u = 2 := by
    obtain ⟨r,rfl⟩ := Nat.exists_eq_add_of_le (show q≤s by omega)
    rw [orbit_add, hq]
    exact terminal_state r
  intro b
  have hratio : orbit s n ≤ 2^0*orbit b (orbit s n) := by simpa [orbit_add] using hmin b
  have bg := bad_window_height_ratio (pos_orbit hn s) badTail b hratio
  have gg := terminal_pair_bound term b
  omega

private theorem exact_cycle_count (r : ℕ) : 2*oddCount r 1 = r+r%2 := by
  have e : r = 2*(r/2)+(r%2) := by omega
  conv_lhs => rw [e]
  rw [oddCount_add, oddCount_twice_one, orbit_twice_one]
  rcases (by omega : r%2=0 ∨ r%2=1) with h|h <;> rw [h] <;>
    simp only [oddCount, Nat.mod_succ_eq_iff_lt.mpr (by decide : 1<2)] <;> omega

/-- Exact parity count after a literal hit, retaining the signed terminal grade
`q - 2 p_u(q)`, expressed without truncated subtraction. -/
theorem good_exact_grade {u q : ℕ} (hit : orbit q u=1) (b : ℕ) :
    2*oddCount (q+b) u = 2*oddCount q u + b + b%2 := by
  rw [oddCount_add, hit]
  have := exact_cycle_count b
  omega

/-- An integer-valued walk to which bounded-increment forward-record counting
can be directly applied. -/
def ballisticWalk (n u t : ℕ) : ℤ :=
  16*((oddCount t n : ℤ)-(oddCount t u : ℤ))-(t : ℤ)

theorem ballisticWalk_laws {n u L q : ℕ} (hn : 0<n) (bad : ¬ Basin n)
    (size : n≤2^L) (hit : orbit q u=1) :
    ballisticWalk n u 0=0 ∧
    (∀ t : ℕ, (t:ℤ)-2*(5*(L:ℤ)+4*q+4) ≤ ballisticWalk n u t) ∧
    (∀ t, ballisticWalk n u (t+1) ≤ ballisticWalk n u t + 15) ∧
    (∀ s b, ballisticWalk n u s ≤ ballisticWalk n u (s+b) ↔
      b+16*oddCount b (orbit s u) ≤ 16*oddCount b (orbit s n)) := by
  refine ⟨rfl, ?_, ?_, ?_⟩
  · intro t
    have := color_discordant_ballistic hn bad size hit t
    unfold ballisticWalk
    omega
  · intro t
    have cn : oddCount (t+1) n = oddCount t n + (orbit t n)%2 := by
      rw [oddCount_add t 1 n]; rfl
    have cu : oddCount (t+1) u = oddCount t u + (orbit t u)%2 := by
      rw [oddCount_add t 1 u]; rfl
    simp only [ballisticWalk, cn, cu, Nat.cast_add, Nat.cast_one]
    omega
  · intro s b
    simp only [ballisticWalk, oddCount_add, Nat.cast_add]
    omega

#print axioms bad_odd_excess
#print axioms good_odd_excess
#print axioms color_discordant_ballistic
#print axioms bad_window_height_ratio
#print axioms discordant_future_minimum_windows
#print axioms good_exact_grade
#print axioms ballisticWalk_laws

end CollatzShell.TernaryHead
