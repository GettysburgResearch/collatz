import PrepaidRamp

namespace RampShadow

/-- The full native prefix test at one supplied ordinary source. -/
def BoundedExcess (q : ℤ) : Prop :=
  ∃ L : ℕ, ∀ d p : ℕ, ∀ z : ℤ, Walk d p q z → 2*p≤d+L

private theorem seven_bound {d p x y} (W : Walk d p x y) (hx : 0<x)
    (avoid : ∀ h, run h x≠1) : 0<y ∧ (2:ℤ)^(d+p)*y ≤ 7^p*x := by
  induction W with
  | nil x => simpa using hx
  | @even h p x y W IH =>
    have hx' : 0<x := by omega
    have step' : step (2*x)=x := by simp [step]
    have A (r : ℕ) : run r x≠1 := by simpa [run,step'] using avoid (r+1)
    obtain ⟨ypos,H⟩ := IH hx' A
    refine ⟨ypos,?_⟩
    rw [show h+1+p=(h+p)+1 by omega,pow_succ]
    nlinarith only [H]
  | @odd h p x y z eq W IH =>
    have x2 : 2≤x := by have neq := avoid 0; simp [run] at neq; omega
    have ypos : 0<y := by omega
    have step' : step x=y := by simp only [step,show x%2≠0 by omega,ite_false]; omega
    have A (r : ℕ) : run r y≠1 := by simpa [run,step'] using avoid (r+1)
    obtain ⟨zpos,H⟩ := IH ypos A
    refine ⟨zpos,?_⟩
    rw [show h+1+(p+1)=h+p+2 by omega,pow_add (2:ℤ) (h+p) 2,pow_succ (7:ℤ)]
    have X := mul_le_mul_of_nonneg_left (show 4*y≤7*x by omega)
      (show (0:ℤ)≤7^p by positivity)
    nlinarith only [H,X]

private theorem linear_binomial (a p : ℕ) :
    ((a:ℤ)+p)*a^p ≤ (a:ℤ)*(a+1)^p := by
  induction p with
  | zero => simp
  | succ p IH =>
    simp only [Nat.cast_succ,pow_succ]
    have X := mul_le_mul_of_nonneg_right IH (show (0:ℤ)≤(a:ℤ)+1 by positivity)
    nlinarith [mul_nonneg (Int.natCast_nonneg p) (show (0:ℤ)≤(a:ℤ)^p by positivity)]

private theorem cycle_account {h p : ℕ} {x y : ℤ} (w : Walk h p x y)
    (start : x=1 ∨ x=2) : (y=1 ∨ y=2) ∧ 2*(p:ℤ)+x=(h:ℤ)+y := by
  induction w <;> omega

/-- Finite prefix excess along a fixed ordinary source is equivalent to
    actual convergence. This also treats hypothetical positive cycles. -/
theorem bounded_excess_iff_hits_one (q : ℤ) (qpos : 0<q) :
    BoundedExcess q ↔ ∃ h, run h q=1 := by
  constructor
  · rintro ⟨L,paid⟩
    by_contra! never
    let B := 7*2^L*q.toNat
    have qnat : (q.toNat:ℤ)=q := Int.toNat_of_nonneg (by omega)
    have power_bound (h : ℕ) :
        (2:ℤ)^(h+odds h q) ≤ 7^(odds h q)*q := by
      obtain ⟨pos,G⟩ := seven_bound (walk_run h q) qpos never
      have X := mul_le_mul_of_nonneg_left (show 1≤run h q by omega)
        (show (0:ℤ)≤2^(h+odds h q) by positivity)
      nlinarith only [X,G]
    have count_bound (h : ℕ) : odds h q≤B := by
      let p := odds h q
      have pay := paid _ _ _ (walk_run h q)
      have cap : (8:ℤ)^p ≤ 2^L*(7^p*q) := by
        have P : (2:ℤ)^(3*p)≤2^(L+(h+p)) :=
          pow_le_pow_right₀ (by norm_num) (show 3*p≤L+(h+p) by dsimp [p]; omega)
        rw [pow_mul,pow_add] at P
        norm_num only [Int.reducePow] at P
        exact P.trans (mul_le_mul_of_nonneg_left (power_bound h) (by positivity))
      have linear := linear_binomial 7 p
      norm_num only [Nat.cast_ofNat,Int.reduceAdd] at linear
      have mulbound : (p:ℤ)*7^p ≤ (7*2^L*q)*7^p := by
        nlinarith only [linear,cap,show (0:ℤ)≤7^p by positivity]
      have pB : (p:ℤ) ≤7*2^L*q := le_of_mul_le_mul_right mulbound (by positivity)
      dsimp [B]
      exact_mod_cast (by simpa [qnat] using pB : (p:ℤ)≤7*2^L*(q.toNat:ℤ))
    let h := 7^B*q.toNat+1
    have A : (2:ℤ)^h≤7^B*q := calc
      _ ≤ 2^(h+odds h q) := pow_le_pow_right₀ (by norm_num) (by omega)
      _ ≤ 7^(odds h q)*q := power_bound h
      _ ≤ _ := mul_le_mul_of_nonneg_right
        (pow_le_pow_right₀ (by norm_num) (count_bound h)) (by omega)
    have Hnat : 2^h≤7^B*q.toNat := by
      exact_mod_cast (by simpa [qnat] using A : (2:ℤ)^h≤7^B*(q.toNat:ℤ))
    have gt : h<2^h := Nat.lt_two_pow_self
    dsimp [h] at gt Hnat
    omega
  · rintro ⟨h,hit⟩
    refine ⟨h+1,?_⟩
    intro d p z W
    by_cases low : d≤h
    · have := count_le W; omega
    · obtain ⟨r,hd⟩ := Nat.exists_eq_add_of_le (show h≤d by omega)
      rw [hd] at W
      obtain ⟨a,b,y,P,Q,eq⟩ := split W
      have y1 : y=1 := (readout P).1.symm.trans hit
      have acc := cycle_account Q (Or.inl y1)
      have C := count_le P
      omega

private theorem bounded_on_finite (M : ℕ) (good : ∀ q : ℤ, 0<q → ∃ h, run h q=1) :
    ∃ L : ℕ, ∀ u : ℕ, 0<u → u≤M →
      ∀ d p : ℕ, ∀ z : ℤ, Walk d p u z → 2*p≤d+L := by
  induction M with
  | zero => exact ⟨0,fun u hu hzero => by omega⟩
  | succ M IH =>
    obtain ⟨L,H⟩ := IH
    have J := (bounded_excess_iff_hits_one (M+1) (by positivity)).2 (good _ (by positivity))
    obtain ⟨L',J'⟩ := J
    refine ⟨max L L',?_⟩
    intro u hu ub d p z W
    by_cases low : u≤M
    · have := H u hu low d p z W; omega
    · have eu : u=M+1 := by omega
      subst u
      have bound := J' d p z (by simpa using W)
      omega

/-- Thus assuming the finite-prefix checks at *unbounded* b already assumes
    the whole conjecture. Each one fixed b is an independent finite job. -/
theorem all_prefix_bounds_iff :
    (∀ b, ∃ L, SmallPrefixBound b L) ↔ ∀ q : ℤ, 0<q → ∃ h, run h q=1 := by
  constructor
  · intro all q hq
    obtain ⟨L,H⟩ := all q.toNat
    apply (bounded_excess_iff_hits_one q hq).1
    apply Exists.intro L
    apply H q hq
    have grow := linear_binomial 2 q.toNat
    norm_num only [Nat.cast_ofNat,Int.reduceAdd] at grow
    rw [Int.toNat_of_nonneg (by omega)] at grow
    nlinarith [show (0:ℤ)<3^q.toNat by positivity,show (0:ℤ)≤2^q.toNat by positivity]
  · intro good b
    obtain ⟨L,H⟩ := bounded_on_finite (4*3^b) good
    refine ⟨L,?_⟩
    intro q hq bound
    have one : (1:ℤ)≤2^b := one_le_pow₀ (by norm_num)
    have cap : q≤4*3^b := by nlinarith [mul_le_mul_of_nonneg_right one (show 0≤q by omega)]
    have cap' : q.toNat≤4*3^b := by exact_mod_cast (by simpa [Int.toNat_of_nonneg (by omega : 0≤q)] using cap : (q.toNat:ℤ)≤4*3^b)
    have final := H q.toNat (by omega) cap'
    simpa [Int.toNat_of_nonneg (by omega : 0≤q)] using final

#print axioms bounded_excess_iff_hits_one
#print axioms all_prefix_bounds_iff
end RampShadow
