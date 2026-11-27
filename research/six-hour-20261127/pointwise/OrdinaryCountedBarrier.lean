import MultiBlockCompensation

/-! An ordinary counted merger obstruction, uniform in the physical clock. -/
namespace OrdinaryCountedBarrier
open MultiBlockCompensation

def PowerTwo (x : ℕ) : Prop := ∃ n : ℕ, x=2^n

private theorem shortcut_pos {x : ℕ} (p : 0<x) : 0<shortcut x := by
  unfold shortcut
  split <;> omega

private theorem power_step {x : ℕ} (hx : PowerTwo x) :
    PowerTwo (shortcut x) ∧
    (if x%2=1 then 4*x else x) = 2*shortcut x := by
  obtain ⟨n,rfl⟩ := hx
  cases n with
  | zero => exact ⟨⟨1,by decide⟩,by decide⟩
  | succ n =>
    have even : (2^(n+1))%2=0 := by rw [pow_succ]; simp
    have step : shortcut (2^(n+1))=2^n := by simp [shortcut,pow_succ]
    refine ⟨⟨n,step⟩,?_⟩
    rw [step,even]
    simp [pow_succ,Nat.mul_comm]

theorem maximum_growth {w : List Bool} {x z : ℕ}
    (p : 0<x) (h : Realizes w x z) : 2^w.length*z ≤ 4^odds w*x := by
  induction w generalizing x with
  | nil => have eq : x=z := h; simp [eq,odds]
  | cons b w ih =>
    obtain ⟨par,rest⟩ := h
    have tail := ih (shortcut_pos p) rest
    have twice := Nat.mul_le_mul_left 2 tail
    rw [List.length_cons,pow_succ]
    calc
      2^w.length*2*z=2*(2^w.length*z) := by ring
      _≤2*(4^odds w*shortcut x) := twice
      _=4^odds w*(2*shortcut x) := by ring
      _≤_ := by
        cases b with
        | false =>
          have even : x%2=0 := by simp at par; omega
          have eq : 2*shortcut x=x := by simp [shortcut,even]; omega
          simp [odds,eq]
        | true =>
          have odd : x%2≠0 := by have := par.mpr rfl; omega
          have step : 2*shortcut x≤4*x := by simp [shortcut,odd]; omega
          simp only [odds, ↓reduceIte, Nat.add_comm 1 (odds w),pow_succ]
          simpa only [Nat.mul_assoc] using (Nat.mul_le_mul_left (4^odds w) step)

theorem exact_on_power {w : List Bool} {x z : ℕ}
    (p : PowerTwo x) (h : Realizes w x z) : 2^w.length*z=4^odds w*x := by
  induction w generalizing x with
  | nil => have eq : x=z := h; simp [eq,odds]
  | cons b w ih =>
    obtain ⟨par,rest⟩ := h
    obtain ⟨closed,eq⟩ := power_step p
    have tail := ih closed rest
    rw [List.length_cons,pow_succ]
    calc
      2^w.length*2*z=2*(2^w.length*z) := by ring
      _=4^odds w*(2*shortcut x) := by rw [tail]; ring
      _=_ := by
        cases b with
        | false =>
          have even : x%2≠1 := by simp at par; omega
          simp [even] at eq
          simp [odds,←eq]
        | true =>
          have odd : x%2=1 := par.mpr rfl
          simp [odd] at eq
          simp only [odds, ↓reduceIte, Nat.add_comm 1 (odds w),pow_succ]
          rw [←eq]; ring

private theorem first_power {x a : ℕ} (odd : x%2=1)
    (hx : 3*x+1=2^(a+1)) : PowerTwo (shortcut x) ∧ 2*shortcut x=3*x+1 := by
  have p : x%2≠0 := by omega
  have st : shortcut x=2^a := by simp [shortcut,p,hx,pow_succ]
  exact ⟨⟨a,st⟩,by rw [st,hx,pow_succ]; omega⟩

/-- Against any convergent one-odd source whose first step is a power of two,
an odd supplied competitor at equal clocks and counts cannot be smaller.
All positive competitors satisfy the sharp three-quarters bound. -/
theorem counted_extremal {u v : List Bool} {x y z a : ℕ} (pos : 0<y)
    (odd : x%2=1) (hx : 3*x+1=2^(a+1)) (hu : Realizes u x z)
    (hv : Realizes v y z) (len : u.length=v.length) (count : odds u=odds v) :
    3*x+1 ≤ 4*y ∧ (y%2=1 → x≤y) := by
  cases u with
  | nil =>
    cases v with
    | nil =>
      have eq : x=y := hu.trans hv.symm
      omega
    | cons b v => simp at len
  | cons b u =>
    cases v with
    | nil => simp at len
    | cons c v =>
      obtain ⟨bu,ru⟩ := hu
      obtain ⟨cv,rv⟩ := hv
      have beq : b=true := bu.mp odd
      subst b
      obtain ⟨powx,stepx⟩ := first_power odd hx
      have upper := exact_on_power powx ru
      have lower := maximum_growth (shortcut_pos pos) rv
      simp only [List.length_cons,Nat.add_right_cancel_iff] at len
      rw [←len,upper] at lower
      cases c with
      | true =>
        have yo : y%2=1 := cv.mpr rfl
        have stepy : 2*shortcut y=3*y+1 := by
          simp [shortcut,(show y%2≠0 by omega)]; omega
        simp [odds] at count
        rw [←count] at lower
        have c := Nat.le_of_mul_le_mul_left lower (Nat.pow_pos (by decide : 0<4))
        omega
      | false =>
        have ye : y%2≠1 := by simp at cv; omega
        have stepy : 2*shortcut y=y := by
          simp [shortcut,(show y%2=0 by omega)]; omega
        simp [odds] at count
        rw [←count,Nat.add_comm 1 (odds u),pow_succ,Nat.mul_assoc] at lower
        have c := Nat.le_of_mul_le_mul_left lower (Nat.pow_pos (by decide : 0<4))
        omega


def Converges (x : ℕ) := ∃ n : ℕ, shortcut^[n] x=1

private theorem return_one (j : ℕ) : shortcut^[2*j] 1=1 := by
  induction j with
  | zero => rfl
  | succ j ih =>
    rw [Nat.mul_succ,Nat.add_comm (2*j) 2,Function.iterate_add_apply,ih]
    decide

/-- This uses persistence of the actual two-cycle, including when one arm
hits one before it reaches the displayed common state. -/
theorem converges_of_common {x y i j : ℕ} (meet : shortcut^[i] x=shortcut^[j] y)
    (hy : Converges y) : Converges x := by
  obtain ⟨m,hm⟩ := hy
  have far : shortcut^[2*j+m] y=1 := by
    rw [Function.iterate_add_apply, hm, return_one]
  refine ⟨(j+m)+i,?_⟩
  rw [Function.iterate_add_apply,meet,←Function.iterate_add_apply]
  simpa only [show j+m+j=2*j+m by omega] using far

/-- The least bad multiple of three cannot be in the six-block progression. -/
theorem six_block_convergence (k : ℕ) :
    Converges (12977607+25165824*k) ↔ Converges (12977601+25165824*k) :=
  ⟨converges_of_common (same_clock k).symm,converges_of_common (same_clock k)⟩

/-- The strict-rise nine-block progression has the same actual basin label
as its smaller triple. No stopping-time bound is assumed for the latter. -/
theorem nine_block_convergence (k : ℕ) :
    Converges (73870594215+103079215104*k) ↔ Converges (73870594209+103079215104*k) := by
  obtain ⟨_,_,_,_,upper,lower⟩ := nine_block_merger k
  have join := (endpoint upper).trans (endpoint lower).symm
  exact ⟨converges_of_common join.symm,converges_of_common join⟩

end OrdinaryCountedBarrier

#print axioms OrdinaryCountedBarrier.shortcut_pos
#print axioms OrdinaryCountedBarrier.power_step
#print axioms OrdinaryCountedBarrier.maximum_growth
#print axioms OrdinaryCountedBarrier.exact_on_power
#print axioms OrdinaryCountedBarrier.first_power
#print axioms OrdinaryCountedBarrier.counted_extremal

#print axioms OrdinaryCountedBarrier.return_one
#print axioms OrdinaryCountedBarrier.converges_of_common
#print axioms OrdinaryCountedBarrier.six_block_convergence
#print axioms OrdinaryCountedBarrier.nine_block_convergence
