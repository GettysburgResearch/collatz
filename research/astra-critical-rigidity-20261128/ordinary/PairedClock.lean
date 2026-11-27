import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity

/-! Native-clock obstruction for two prescribed ordinary Collatz visitors. -/
set_option autoImplicit false
namespace Collatz.PairedClock

def step (n : ℕ) : ℕ := if n % 2 = 0 then n / 2 else (3*n+1)/2
def orbit (n : ℕ) : ℕ → ℕ
  | 0 => n
  | t+1 => step (orbit n t)
def grade (n : ℕ) : ℕ → ℕ
  | 0 => 0
  | t+1 => grade n t + orbit n t % 2
def offset (n : ℕ) : ℕ → ℕ
  | 0 => 0
  | t+1 => 3^(orbit n t%2)*offset n t + 2^t*(orbit n t%2)

private theorem step_eq (x : ℕ) : 2 * step x = 3^(x%2)*x + x%2 := by
  by_cases h : x%2=0
  · simp [step,h]; omega
  · have hh : x%2=1 := by omega
    simp [step,hh]; omega

theorem affine (n t : ℕ) : 2^t*orbit n t = 3^(grade n t)*n+offset n t := by
  induction t with
  | zero => simp [orbit,grade,offset]
  | succ t ih =>
    simp only [orbit,grade,offset,pow_succ,pow_add]
    calc 2^t*2*step (orbit n t) = 2^t*(2*step (orbit n t)) := by ring
         _ = 3^(orbit n t%2)*(2^t*orbit n t)+2^t*(orbit n t%2) := by
              rw [step_eq]; ring
         _ = _ := by rw [ih]; ring

private theorem offset_bound (n t : ℕ) : offset n t ≤ 2^t * 3^(grade n t) := by
  induction t with
  | zero => simp [offset]
  | succ t ih =>
    let e := orbit n t%2
    have he : e ≤ 1 := by dsimp [e]; omega
    have hp : 1 ≤ 3^(grade n t+e) := Nat.one_le_pow _ _ (by decide)
    have he' := he.trans hp
    calc offset n (t+1) = 3^e*offset n t + 2^t*e := rfl
         _ ≤ 3^e*(2^t*3^(grade n t)) + 2^t*3^(grade n t+e) :=
           Nat.add_le_add (Nat.mul_le_mul_left _ ih) (Nat.mul_le_mul_left _ he')
         _ = _ := by simp only [grade,pow_succ,pow_add,e]; ring

def gap (a b : ℕ) : ℕ := (a-b)+(b-a)
private theorem gap_scale (c a b : ℕ) : gap (c*a) (c*b) = c*gap a b := by
  simp only [gap,Nat.mul_sub,Nat.mul_add]
private theorem gap_common (c a b : ℕ) : gap (c+a) (c+b)=gap a b := by
  unfold gap; omega
private theorem gap_upper {a b M : ℕ} (ha : a≤M) (hb : b≤M) : gap a b ≤M := by
  unfold gap; omega
private theorem gap_pos {a b : ℕ} (h:a≠b) : 0<gap a b := by unfold gap; omega

/-! For y=3^r*x+d the possibly huge common multiple of x cancels exactly. -/
def discrepancy (x y r t : ℕ) : ℕ :=
  gap (3^(grade x t)*orbit y t) (3^(grade y t+r)*orbit x t)

theorem discrepancy_bound (x r d t : ℕ) :
    discrepancy x (3^r*x+d) r t ≤ (d+1)*3^(grade x t+grade (3^r*x+d) t+r) := by
  let y := 3^r*x+d
  let p := 3^(grade x t)
  let q := 3^(grade y t)
  have X := affine x t
  have Y := affine y t
  have h1 : 2^t*(p*orbit y t) = (p*q*3^r*x)+(p*q*d+p*offset y t) := by
    calc _ = p*(2^t*orbit y t) := by ring
         _ = _ := by rw [Y]; dsimp [p,q,y]; ring
  have h2 : 2^t*(q*3^r*orbit x t) = (p*q*3^r*x)+(q*3^r*offset x t) := by
    calc _ = q*3^r*(2^t*orbit x t) := by ring
         _ = _ := by rw [X]; dsimp [p]; ring
  have hdy : p*offset y t ≤ p*(2^t*q) := Nat.mul_le_mul_left p (offset_bound y t)
  have hdx : q*3^r*offset x t ≤ q*3^r*(2^t*p) := Nat.mul_le_mul_left _ (offset_bound x t)
  have u : 1 ≤ 2^t*3^r := Nat.one_le_iff_ne_zero.mpr (by positivity)
  have v : 1 ≤ 3^r := Nat.one_le_iff_ne_zero.mpr (by positivity)
  have v' : 1 ≤ d+1 := by omega
  have ud : p*q*d ≤ p*q*d*(2^t*3^r) := by simpa using Nat.mul_le_mul_left (p*q*d) u
  have vy : p*(2^t*q) ≤ p*(2^t*q)*3^r := by simpa using Nat.mul_le_mul_left (p*(2^t*q)) v
  have vx : q*3^r*(2^t*p) ≤ q*3^r*(2^t*p)*(d+1) := by simpa using Nat.mul_le_mul_left (q*3^r*(2^t*p)) v'
  have D : 2^t*gap (p*orbit y t) (q*3^r*orbit x t) ≤ 2^t*((d+1)*(p*q*3^r)) := by
    rw [← gap_scale,h1,h2,gap_common]
    apply gap_upper
    · exact (Nat.add_le_add ud (hdy.trans vy)).trans_eq (by ring)
    · exact (hdx.trans vx).trans_eq (by ring)
  simpa only [discrepancy,pow_add,p,q,y] using Nat.le_of_mul_le_mul_left D (Nat.two_pow_pos _)

private theorem unit_after_odd {x t : ℕ} (h:0<grade x t) : orbit x t%3 ≠ 0 := by
  induction t with
  | zero => simp [grade] at h
  | succ t ih =>
    simp only [grade] at h
    by_cases he : orbit x t%2=0
    · have hu := ih (by omega)
      simp only [orbit,step,he,ite_true]; omega
    · simp only [orbit,step,he,ite_false]; omega

private theorem cancel_units (u v i j : ℕ) (hu : u%3 ≠ 0) (hv : v%3 ≠ 0)
    (eq : 3^i*u=3^j*v) : u=v := by
  induction i generalizing j with
  | zero =>
    cases j with
    | zero => simpa using eq
    | succ j =>
      have ev : u=3*(3^j*v) := by simpa [pow_succ,Nat.mul_comm,Nat.mul_left_comm,Nat.mul_assoc] using eq
      omega
  | succ i ih =>
    cases j with
    | zero =>
      have ev : v=3*(3^i*u) := by simpa [pow_succ,Nat.mul_comm,Nat.mul_left_comm,Nat.mul_assoc] using eq.symm
      omega
    | succ j =>
      apply ih j
      apply Nat.eq_of_mul_eq_mul_left (by decide : 0<3)
      simpa only [pow_succ,Nat.mul_left_comm,Nat.mul_comm,Nat.mul_assoc] using eq

theorem discrepancy_positive {x y r t : ℕ} (g : 0<grade x t) (h : 0<grade y t)
    (ne : orbit x t ≠ orbit y t) : 0<discrepancy x y r t := by
  apply gap_pos
  intro eq
  exact ne (cancel_units _ _ _ _ (unit_after_odd h) (unit_after_odd g) eq).symm

theorem even_discrepancy (x y r t : ℕ) (ha:orbit x t%2=0) (hb:orbit y t%2=0) :
    2*discrepancy x y r (t+1) = discrepancy x y r t := by
  have a : 2*step (orbit x t)=orbit x t := by simp [step_eq,ha]
  have b : 2*step (orbit y t)=orbit y t := by simp [step_eq,hb]
  simp only [discrepancy,grade,orbit,ha,hb,Nat.add_zero]
  rw [←gap_scale, ←Nat.mul_left_comm, b]
  conv_lhs => rhs; rw [Nat.mul_left_comm, a]

private theorem grade_mono (x : ℕ) {t k : ℕ} (h:t≤k) : grade x t ≤ grade x k := by
  induction h with
  | refl => rfl
  | step _ ih => exact ih.trans (Nat.le_add_right _ _)

private theorem odd_first_grade {x t : ℕ} (h:x%2=1) (ht:0<t) : 0<grade x t := by
  have u := grade_mono x (show 1≤t by omega)
  simp [grade,orbit,h] at u
  omega

private theorem three_pow_odd (r : ℕ) : 3^r%2=1 := by
  induction r with
  | zero => decide
  | succ r ih => rw [pow_succ,Nat.mul_mod,ih]

private theorem power_budget (x y r m k : ℕ)
    (bound : ∀ t≤k, discrepancy x y r t ≤ 2^m)
    (nz : ∀t<k, orbit x t%2=0 → orbit y t%2=0 → 0<discrepancy x y r (t+1)) :
    2^k * max 1 (discrepancy x y r k) ≤
      2^((m+1)*(grade x k+grade y k))*max 1 (discrepancy x y r 0) := by
  induction k with
  | zero => simp [grade]
  | succ k ih =>
    have pr := ih (fun t h => bound t (by omega)) (fun t h => nz t (by omega))
    let a := orbit x k%2
    let b := orbit y k%2
    have gg : grade x (k+1)+grade y (k+1)=(grade x k+grade y k)+(a+b) := by
      simp only [grade,a,b]; omega
    have charge :
        2*max 1 (discrepancy x y r (k+1)) ≤
          2^((m+1)*(a+b))*max 1 (discrepancy x y r k) := by
      by_cases e : a+b = 0
      · have ha : orbit x k%2=0 := by change a=0; omega
        have hb : orbit y k%2=0 := by change b=0; omega
        have n := nz k (by omega) ha hb
        have eq := even_discrepancy x y r k ha hb
        rw [e]; simp only [Nat.mul_zero,pow_zero,Nat.one_mul]
        omega
      · have big := bound (k+1) (by omega)
        have h1 : max 1 (discrepancy x y r (k+1)) ≤ 2^m := by
          apply max_le (Nat.two_pow_pos m) big
        have E : m+1 ≤ (m+1)*(a+b) := by
          have h : 1≤a+b := by omega
          simpa using Nat.mul_le_mul_left (m+1) h
        have h2 : 2*2^m ≤ 2^((m+1)*(a+b)) := by
          simpa only [pow_succ,Nat.mul_comm] using Nat.pow_le_pow_right (by decide : 0<2) E
        exact (Nat.mul_le_mul_left 2 h1).trans (h2.trans (Nat.le_mul_of_pos_right _ (by omega)))
    rw [gg,Nat.mul_add,pow_add,pow_succ]
    calc 2^k*2*max 1 (discrepancy x y r (k+1)) =
            2^k*(2*max 1 (discrepancy x y r (k+1))) := by ring
         _ ≤ _ := Nat.mul_le_mul_left (2^k) charge
         _ = 2^((m+1)*(a+b))*(2^k*max 1 (discrepancy x y r k)) := by ring
         _ ≤ _ := Nat.mul_le_mul_left _ pr
         _ = _ := by ring

/-- If the odd source and its ternary-power multiple have distinct endpoints
at every common native date through k, their total grade controls k quadratically. -/
theorem unmatched_ternary_power (x r k : ℕ) (odd : x%2=1)
    (apart : ∀t≤k, orbit x t ≠ orbit (3^r*x) t) :
    k ≤ (2*(grade x k+grade (3^r*x) k+r)+1)*(grade x k+grade (3^r*x) k) := by
  let y := 3^r*x
  let G := grade x k+grade y k
  let m := 2*(G+r)
  have oddY : y%2=1 := by dsimp [y]; rw [Nat.mul_mod,three_pow_odd,odd]
  have bound (t : ℕ) (ht : t≤k) : discrepancy x y r t ≤ 2^m := by
    have h := discrepancy_bound x r 0 t
    simp only [Nat.add_zero,Nat.zero_add,Nat.one_mul] at h
    have e : grade x t+grade y t+r ≤ G+r := by
      have := grade_mono x ht; have := grade_mono y ht; dsimp [G]; omega
    calc discrepancy x y r t ≤ 3^(grade x t+grade y t+r) := h
         _ ≤ 3^(G+r) := Nat.pow_le_pow_right (by decide) e
         _ ≤ 4^(G+r) := Nat.pow_le_pow_left (by decide) _
         _ = 2^m := by dsimp [m]; rw [pow_mul]; rfl
  have nz (t : ℕ) (ht:t<k) (_ : orbit x t%2=0) (_ : orbit y t%2=0) :
      0<discrepancy x y r (t+1) :=
    discrepancy_positive (odd_first_grade odd (by omega)) (odd_first_grade oddY (by omega))
      (apart _ (by omega))
  have p := power_budget x y r m k bound nz
  have d0 : discrepancy x y r 0=0 := by simp [discrepancy,gap,orbit,grade,y]
  rw [d0] at p
  simp only [Nat.max_eq_left (Nat.zero_le _),Nat.mul_one] at p
  apply (Nat.pow_le_pow_iff_right (by decide : 1<2)).mp
  exact (Nat.le_mul_of_pos_right (2^k) (by omega)).trans p

#print axioms unmatched_ternary_power
end Collatz.PairedClock
