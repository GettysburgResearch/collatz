import OldHeadBudget

/-! First failure on the small-source side of the odd gate. All orbit data are
the positive ordinary gap equations, including the next state's oddness. -/
set_option autoImplicit false
set_option warningAsError true
namespace OldHeadBudget
open scoped BigOperators

def Orbit.shift (o : Orbit) (p : ℕ) : Orbit where
  x i := o.x (p+i)
  e i := o.e (p+i)
  odd i := o.odd (p+i)
  edge i := by simpa only [Nat.add_assoc] using o.edge (p+i)

private theorem clock_succ (o : Orbit) (n : ℕ) :
    clock o (n+1) = clock o n+o.e n := by simp [clock,Finset.sum_range_succ]

theorem clock_shift (o : Orbit) (p n : ℕ) :
    clock o (p+n)=clock o p+clock (o.shift p) n := by
  induction n with
  | zero => simp [clock]
  | succ n ih =>
    rw [← Nat.add_assoc,clock_succ,ih,clock_succ]
    simp [Orbit.shift,Nat.add_assoc]

private theorem unique_odd_parts {a b x y : ℕ}
    (hx : x%2=1) (hy : y%2=1) (eq : 2^a*x=2^b*y) : a=b ∧ x=y := by
  have h1 : (x:ℤ)%2=1 := by exact_mod_cast hx
  have h2 : (y:ℤ)%2=1 := by exact_mod_cast hy
  have he : (2:ℤ)^a*x=2^b*y := by exact_mod_cast eq
  obtain ⟨hab,hxy⟩ := Collatz.OrdinaryGapWord.odd_part_unique h1 h2 a b he
  exact ⟨hab,by exact_mod_cast hxy⟩

private theorem equal_next (o : Orbit) {i j : ℕ} (eq : o.x i=o.x j) :
    o.e i=o.e j ∧ o.x (i+1)=o.x (j+1) := by
  apply unique_odd_parts (o.odd _) (o.odd _)
  rw [o.edge i,o.edge j,eq]

private theorem equal_ray (o : Orbit) {i j : ℕ} (eq : o.x i=o.x j) (n : ℕ) :
    o.x (i+n)=o.x (j+n) := by
  induction n with
  | zero => simpa
  | succ n ih => exact (equal_next o ih).2

private theorem equal_clocks (o : Orbit) {i j : ℕ} (eq : o.x i=o.x j) (n : ℕ) :
    clock (o.shift i) n=clock (o.shift j) n := by
  unfold clock
  apply Finset.sum_congr rfl
  intro h _
  exact (equal_next o (equal_ray o eq h)).1

private theorem high_affine (o : Orbit) (n : ℕ) (floor : ∀ i<n, 3≤o.x i) :
    3^n*2^(clock o n)*o.x n ≤ 10^n*o.x 0 := by
  induction n with
  | zero => simp [clock]
  | succ n ih =>
    have prev := ih (fun i hi => floor i (by omega))
    have localbound : 3*(3*o.x n+1) ≤ 10*o.x n := by have := floor n (by omega); omega
    calc
      _ = (3^n*2^(clock o n))*(3*(2^(o.e n)*o.x (n+1))) := by
        rw [clock_succ,pow_succ 3 n,pow_add]; ring
      _ ≤ (3^n*2^(clock o n))*(10*o.x n) := by
        rw [o.edge n]; exact Nat.mul_le_mul_left _ localbound
      _ = (3^n*2^(clock o n)*o.x n)*10 := by ring
      _ ≤ (10^n*o.x 0)*10 := Nat.mul_le_mul_right _ prev
      _ = _ := by rw [pow_succ]; ring

theorem nontrivial_lap (o : Orbit) (n : ℕ) (hn : 0<n)
    (floor : ∀ i<n, 3≤o.x i) (ret : o.x n=o.x 0) :
    4*clock o n < 7*n := by
  have hh := high_affine o n floor
  rw [ret] at hh
  have drop := Nat.le_of_mul_le_mul_right hh (o.pos 0)
  by_contra h
  have hpow : 2^(7*n) ≤ (2:ℕ)^(4*clock o n) :=
    Nat.pow_le_pow_right (by decide) (by omega)
  have small := Nat.pow_le_pow_left drop 4
  have impossible : (10368:ℕ)^n ≤ 10000^n := calc
    _ = (3^n)^4*2^(7*n) := by
      rw [← pow_mul, Nat.mul_comm n 4,pow_mul,pow_mul,← mul_pow]
      norm_num
    _ ≤ (3^n)^4*2^(4*clock o n) := Nat.mul_le_mul_left _ hpow
    _ = (3^n*2^(clock o n))^4 := by
      rw [mul_pow,←pow_mul 2,Nat.mul_comm (clock o n) 4]
    _ ≤ (10^n)^4 := small
    _ = _ := by rw [←pow_mul,Nat.mul_comm n 4,pow_mul]; norm_num
  exact (Nat.not_le_of_lt (Nat.pow_lt_pow_left (by decide : 10000<10368)
    (Nat.ne_of_gt hn))) impossible

def Failed (o : Orbit) (n : ℕ) : Prop := 7*n < 4*clock o n

def FirstFailure (o : Orbit) (t : ℕ) : Prop :=
  Failed o t ∧ ∀ s<t, ¬ Failed o s

/-- A nontrivial repeated lap can be removed even when t is beyond the
first return. Thus all departures before the first failure are distinct if
one has not yet been departed. The terminal itself may equal 1. -/
theorem first_failure_simple (o : Orbit) (t : ℕ) (first : FirstFailure o t)
    (noone : ∀ i<t, o.x i ≠ 1) :
    Set.InjOn o.x (Finset.range t : Finset ℕ) := by
  have ordered (i j : ℕ) (lt : i<j) (jt : j<t) (same : o.x i=o.x j) : False := by
    let d := j-i
    let r := t-j
    have jd : j=i+d := by dsimp [d]; omega
    have tr : t=j+r := by dsimp [r]; omega
    have dd : 0<d := by dsimp [d]; omega
    have floor (h : ℕ) (hh : h<d) : 3≤(o.shift i).x h := by
      have neq := noone (i+h) (by omega)
      have odd := o.odd (i+h)
      change 3≤o.x (i+h)
      omega
    have cycle := nontrivial_lap (o.shift i) d dd floor (by
      change o.x (i+d)=o.x (i+0)
      simpa only [←jd,Nat.add_zero] using same.symm)
    have earlier := first.2 (i+r) (by omega)
    have final := first.1
    have forward := clock_shift o j r
    have backwards := clock_shift o i r
    have loop := clock_shift o i d
    have after := equal_clocks o same r
    change 7*t < 4*clock o t at final
    change ¬ 7*(i+r) < 4*clock o (i+r) at earlier
    rw [← tr] at forward
    rw [← jd] at loop
    omega
  intro i hi j hj eq
  simp only [Finset.mem_coe,Finset.mem_range] at hi hj
  by_contra h
  rcases Nat.lt_or_gt_of_ne h with a|a
  · exact ordered i j a hj eq
  · exact ordered j i a hi eq.symm

def Cleared (m n : ℕ) : Prop :=
  3^(12*n)*m^12*(2*n+1)^2 < 2^(21*n)

private theorem cleared_succ (m n : ℕ) (hn : 0<n) (h : Cleared m n) :
    Cleared m (n+1) := by
  have gate : (2*(n+1)+1)^2 ≤ 3*(2*n+1)^2 := by
    obtain ⟨v,hv⟩ := Nat.exists_eq_add_of_le hn
    rw [hv]; nlinarith
  unfold Cleared at *
  rw [Nat.mul_succ,Nat.mul_succ 21 n,pow_add,pow_add (2:ℕ)]
  calc
    _ ≤ 3^(12*n)*3^12*m^12*(3*(2*n+1)^2) := Nat.mul_le_mul_left _ gate
    _ = (3^(12*n)*m^12*(2*n+1)^2)*1594323 := by ring
    _ < 2^(21*n)*1594323 := Nat.mul_lt_mul_of_pos_right h (by decide)
    _ ≤ _ := Nat.mul_le_mul_left _ (by decide)

theorem cleared_later (m n t : ℕ) (hn : 0<n) (ht : n≤t) (h : Cleared m n) :
    Cleared m t := by
  obtain ⟨r,rfl⟩ := Nat.exists_eq_add_of_le ht
  induction r with
  | zero => simpa
  | succ r ih => exact cleared_succ m (n+r) (by omega) (ih (by omega))

private theorem no_simple_failure (o : Orbit) (t : ℕ) (fail : Failed o t)
    (simple : Set.InjOn o.x (Finset.range t : Finset ℕ))
    (floor : ∀ i<t, 3≤o.x i) (small : Cleared (o.x 0) t) : False := by
  have budget := simple_budget o t simple floor
  have base : 2^(clock o t) ≤ (2^(clock o t)*o.x t) :=
    Nat.le_mul_of_pos_right _ (o.pos t)
  have B := (Nat.pow_le_pow_left base 6).trans budget
  have C := Nat.pow_le_pow_left B 2
  have raised : 2^(21*t) ≤ (2:ℕ)^(clock o t*6*2) := by
    apply Nat.pow_le_pow_right (by decide)
    unfold Failed at fail
    omega
  rw [pow_mul (2:ℕ) (clock o t*6) 2,pow_mul (2:ℕ) (clock o t) 6] at raised
  have norm : ((3^t*o.x 0)^6*(2*t+1))^2 =
      3^(12*t)*(o.x 0)^12*(2*t+1)^2 := by
    rw [show 12*t=(t*6)*2 by ring,pow_mul,pow_mul]
    ring
  rw [norm] at C
  exact (Nat.not_le_of_lt small) (raised.trans C)

/-- Every first failure after a cleared head has a genuine preceding
departure from 1. In particular its actual terminal is also 1. -/
theorem first_failure_after_clearance (o : Orbit) (n t : ℕ) (hn : 0<n)
    (nt : n≤t) (small : Cleared (o.x 0) n) (first : FirstFailure o t) :
    ∃ i<t, o.x i=1 := by
  by_contra! noone
  have floors (i : ℕ) (hi : i<t) : 3≤o.x i := by
    have odd := o.odd i
    have neq := noone i hi
    omega
  exact no_simple_failure o t first.1 (first_failure_simple o t first noone)
    floors (cleared_later _ n t hn nt small)

private theorem next_one (o : Orbit) (i : ℕ) (one : o.x i=1) :
    o.e i=2 ∧ o.x (i+1)=1 := by
  apply unique_odd_parts (o.odd _) (by decide)
  rw [o.edge,one]; decide

theorem after_one (o : Orbit) {i : ℕ} (one : o.x i=1) (d : ℕ) :
    o.x (i+d)=1 ∧ clock o (i+d)=clock o i+2*d := by
  induction d with
  | zero => simp [one]
  | succ d ih =>
    obtain ⟨e,x⟩ := next_one o (i+d) ih.1
    refine ⟨x,?_⟩
    rw [←Nat.add_assoc,clock_succ,e,ih.2]; omega

theorem first_failure_clock (o : Orbit) {t : ℕ} (first : FirstFailure o t)
    {i : ℕ} (hi : i<t) (one : o.x i=1) :
    t+4*clock o i=8*i+1 ∧ t%4=1 := by
  obtain ⟨d,hd⟩ : ∃ d, t=i+d+1 := ⟨t-i-1,by omega⟩
  have old := first.2 (i+d) (by omega)
  have after := (after_one o one d).2
  have after' := (after_one o one (d+1)).2
  have fail := first.1
  unfold Failed at old fail
  rw [←Nat.add_assoc,←hd] at after'
  omega

/-- On every cleared source that has passed through n, testing only the
single terminal clock at h exactly decides all the intervening prefix tests. -/
theorem terminal_test (o : Orbit) (n h : ℕ) (hn : 0<n)
    (small : Cleared (o.x 0) n) (alive : ∀ j≤n, ¬ Failed o j) :
    (∃ j≤h, Failed o j) ↔ Failed o h := by
  constructor
  · rintro ⟨z,hz,fail⟩
    classical
    have exists_fail : ∃ j, Failed o j := ⟨z,fail⟩
    let t := Nat.find exists_fail
    have first : FirstFailure o t := ⟨Nat.find_spec exists_fail,
      fun j hj => Nat.find_min exists_fail hj⟩
    have t_le : t≤z := Nat.find_min' exists_fail fail
    have nt : n<t := by
      by_contra! htn
      exact alive t htn first.1
    obtain ⟨i,hi,one⟩ := first_failure_after_clearance o n t hn (by omega) small first
    have t_eq : i+(t-i)=t := by omega
    have h_eq : i+(h-i)=h := by omega
    have b := (after_one o one (t-i)).2
    have a := (after_one o one (h-i)).2
    rw [t_eq] at b
    rw [h_eq] at a
    have ft := first.1
    unfold Failed at ft ⊢
    omega
  · exact fun fh => ⟨h,le_rfl,fh⟩

#print axioms nontrivial_lap
#print axioms first_failure_simple
#print axioms cleared_later
#print axioms first_failure_after_clearance
#print axioms after_one
#print axioms first_failure_clock
#print axioms terminal_test
end OldHeadBudget
