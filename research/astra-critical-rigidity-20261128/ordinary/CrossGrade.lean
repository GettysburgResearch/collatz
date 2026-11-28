import PairedClock

/-! Separate physical odd-departure costs for the two shortcut trajectories. -/
set_option autoImplicit false
namespace Collatz.PairedClock

/-- The number of common native dates before `t` that have two odd departures. -/
def jointOdds (x y : ℕ) : ℕ → ℕ
  | 0 => 0
  | t+1 => jointOdds x y t + (orbit x t % 2) * (orbit y t % 2)

/-- Local costs with no natural-number subtraction. -/
def crossCost (x y r : ℕ) : ℕ → ℕ
  | 0 => 0
  | t+1 => crossCost x y r t + (orbit x t % 2) * (grade y t+r) +
      (orbit y t % 2) * grade x t

theorem crossCost_add_joint (x y r t : ℕ) :
    crossCost x y r t + jointOdds x y t = grade x t * (grade y t+r) := by
  induction t with
  | zero => simp [crossCost,jointOdds,grade]
  | succ t ih =>
    simp only [crossCost,jointOdds,grade]
    rw [show crossCost x y r t + orbit x t % 2 * (grade y t + r) +
        orbit y t % 2 * grade x t + (jointOdds x y t + orbit x t % 2 * (orbit y t % 2)) =
        (crossCost x y r t + jointOdds x y t) + orbit x t % 2 * (grade y t + r) +
        orbit y t % 2 * grade x t + orbit x t % 2 * (orbit y t % 2) by ring, ih]
    ring

private theorem doubled_step (x : ℕ) : 2 * step x = 3^(x%2)*x + x%2 := by
  by_cases h : x%2=0
  · simp [step,h]; omega
  · have hh : x%2=1 := by omega
    simp [step,hh]; omega

private theorem scaled_gap (p x y : ℕ) : gap (p*x) (p*y) = p * gap x y := by
  simp only [gap,Nat.mul_sub,Nat.mul_add]

private theorem public_gap_charge (p x y u v : ℕ) :
    gap (p*x+u) (p*y+v) ≤ p*gap x y+u+v := by
  rw [←scaled_gap]
  unfold gap
  omega

/-- Doubled discrepancy incurs at most the two signed affine contributions. -/
theorem discrepancy_one_step_charge (x y r t : ℕ) :
    2*discrepancy x y r (t+1) ≤
      3^(orbit x t%2+orbit y t%2)*discrepancy x y r t +
      3^(grade x t+orbit x t%2)*(orbit y t%2) +
      3^(grade y t+r+orbit y t%2)*(orbit x t%2) := by
  let a := orbit x t%2
  let b := orbit y t%2
  let g := grade x t
  let h := grade y t
  have left : 2*(3^(g+a)*step (orbit y t)) =
      3^(a+b)*(3^g*orbit y t)+3^(g+a)*b := by
    calc _ = 3^(g+a)*(2*step (orbit y t)) := by ring
         _ = _ := by rw [doubled_step]; simp only [b,pow_add]; ring
  have right : 2*(3^(h+b+r)*step (orbit x t)) =
      3^(a+b)*(3^(h+r)*orbit x t)+3^(h+r+b)*a := by
    calc _ = 3^(h+b+r)*(2*step (orbit x t)) := by ring
         _ = _ := by rw [doubled_step]; simp only [a,pow_add]; ring
  change 2 * gap (3^(g+a)*step (orbit y t)) (3^(h+b+r)*step (orbit x t)) ≤ _
  rw [←scaled_gap,left,right]
  exact public_gap_charge _ _ _ _ _

private theorem elementary_step_factor (a b P Q D N : ℕ) (ha : a≤1) (hb : b≤1)
    (hp : 0<P) (hq : 0<Q)
    (charge : 2*N ≤ 3^(a+b)*D + P*3^a*b + Q*3^b*a)
    (even_case : a=0 → b=0 → 2*max 1 N ≤ max 1 D) :
    2*max 1 N ≤ 4^(a+b)*(Q^a*P^b)*max 1 D := by
  let W := max 1 D
  have dw : D≤W := le_max_right _ _
  have wo : 1≤W := le_max_left _ _
  have pW : P ≤ P*W := by simpa using Nat.mul_le_mul_left P wo
  have qW : Q ≤ Q*W := by simpa using Nat.mul_le_mul_left Q wo
  have wP : W ≤ P*W := by simpa using Nat.mul_le_mul_right W hp
  have wQ : W ≤ Q*W := by simpa using Nat.mul_le_mul_right W hq
  have pqW : P*W ≤ P*Q*W := by
    simpa only [Nat.mul_assoc] using Nat.mul_le_mul_left P wQ
  have qpW : Q*W ≤ P*Q*W := by
    simpa only [Nat.mul_comm,Nat.mul_left_comm,Nat.mul_assoc] using Nat.mul_le_mul_left Q wP
  rcases Nat.le_one_iff_eq_zero_or_eq_one.mp ha with h | h <;>
    rcases Nat.le_one_iff_eq_zero_or_eq_one.mp hb with h' | h' <;> subst a <;> subst b
  · simpa using even_case rfl rfl
  · simp only [Nat.zero_add,pow_one,pow_zero,Nat.mul_zero,Nat.mul_one,
      Nat.one_mul,Nat.add_zero] at charge ⊢
    change 2*max 1 N ≤ 4*P*W
    rw [Nat.mul_assoc]
    omega
  · simp only [Nat.add_zero,pow_one,pow_zero,Nat.mul_zero,Nat.mul_one,Nat.add_zero] at charge ⊢
    change 2*max 1 N ≤ 4*Q*W
    rw [Nat.mul_assoc]
    omega
  · norm_num at charge ⊢
    have eq : 16*(Q*P)*W = 16*(P*Q*W) := by ring
    change 2*max 1 N ≤ 16*(Q*P)*W
    rw [eq]
    omega

private theorem one_step_budget (x y r t : ℕ)
    (nz : orbit x t%2=0 → orbit y t%2=0 → 0<discrepancy x y r (t+1)) :
    2*max 1 (discrepancy x y r (t+1)) ≤
    4^(orbit x t%2+orbit y t%2) *
    3^((orbit x t%2)*(grade y t+r)+(orbit y t%2)*grade x t) *
    max 1 (discrepancy x y r t) := by
  let a := orbit x t%2
  let b := orbit y t%2
  let g := grade x t
  let h := grade y t
  have charge := discrepancy_one_step_charge x y r t
  have charge' : 2*discrepancy x y r (t+1) ≤
      3^(a+b)*discrepancy x y r t + 3^g*3^a*b + 3^(h+r)*3^b*a := by
    simpa only [pow_add,a,b,g,h] using charge
  have hfactor := elementary_step_factor a b (3^g) (3^(h+r)) _ _
    (by dsimp [a]; omega) (by dsimp [b]; omega) (by positivity) (by positivity) charge'
    (by
      intro ha hb
      have n := nz ha hb
      have ev := even_discrepancy x y r t ha hb
      omega)
  simpa only [a,b,g,h,pow_add,pow_mul,Nat.mul_comm] using hfactor

private theorem total_cross_budget (x y r k : ℕ)
    (nz : ∀t<k, orbit x t%2=0 → orbit y t%2=0 → 0<discrepancy x y r (t+1)) :
    2^k*max 1 (discrepancy x y r k) ≤
    4^(grade x k+grade y k)*3^(crossCost x y r k)*max 1 (discrepancy x y r 0) := by
  induction k with
  | zero => simp [grade,crossCost]
  | succ k ih =>
    have prev := ih (fun t ht => nz t (by omega))
    have inc := one_step_budget x y r k (nz k (by omega))
    let f := 4^(orbit x k%2+orbit y k%2) *
      3^((orbit x k%2)*(grade y k+r)+(orbit y k%2)*grade x k)
    calc 2^(k+1)*max 1 (discrepancy x y r (k+1)) =
        2^k*(2*max 1 (discrepancy x y r (k+1))) := by rw [pow_succ]; ring
         _ ≤ 2^k*(f*max 1 (discrepancy x y r k)) := Nat.mul_le_mul_left _ inc
         _ = f*(2^k*max 1 (discrepancy x y r k)) := by ring
         _ ≤ _ := Nat.mul_le_mul_left _ prev
         _ = _ := by simp only [f,grade,crossCost,pow_add]; ring

private theorem grade_succ_pos (x t : ℕ) (hx : x%2=1) : 0<grade x (t+1) := by
  induction t with
  | zero => simp [grade,orbit,hx]
  | succ t ih => exact Nat.lt_of_lt_of_le ih (Nat.le_add_right _ _)

private theorem odd_power_three (r : ℕ) : 3^r%2=1 := by
  induction r with
  | zero => decide
  | succ r ih => rw [pow_succ,Nat.mul_mod,ih]

/-- The exact two-grade exponential clock budget, retaining the endpoint discrepancy
and the discount for simultaneous odd departures. -/
theorem unmatched_cross_grade (x r k : ℕ) (hx : x%2=1)
    (apart : ∀t≤k, orbit x t ≠ orbit (3^r*x) t) :
    2^k*max 1 (discrepancy x (3^r*x) r k) ≤
      4^(grade x k+grade (3^r*x) k) *
      3^(grade x k*(grade (3^r*x) k+r)-jointOdds x (3^r*x) k) := by
  let y := 3^r*x
  have hy : y%2=1 := by dsimp [y]; rw [Nat.mul_mod,odd_power_three r,hx]
  have nz (t : ℕ) (ht:t<k) (_ : orbit x t%2=0) (_ : orbit y t%2=0) :
      0<discrepancy x y r (t+1) :=
    discrepancy_positive (grade_succ_pos x t hx) (grade_succ_pos y t hy) (apart _ (by omega))
  have total := total_cross_budget x y r k nz
  have d0 : discrepancy x y r 0=0 := by simp [discrepancy,gap,orbit,grade,y]
  rw [d0] at total
  have c := crossCost_add_joint x y r k
  have e : crossCost x y r k = grade x k*(grade y k+r)-jointOdds x y k := by omega
  simpa only [e,Nat.max_eq_left (Nat.zero_le _),Nat.mul_one,y] using total

end Collatz.PairedClock
