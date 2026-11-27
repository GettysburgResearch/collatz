import PostWords

namespace RampShadow.Postpeak

theorem intercept_min (w : Word) : 3^weight w - 2^weight w ≤ intercept w := by
  induction w with
  | nil => norm_num [weight,intercept]
  | cons b w IH =>
    have nn := (intercept_bounds w).1
    cases b <;> simp only [weight,intercept,pow_succ] <;> linarith

private theorem odd_pow (p : ℕ) : (3:ℤ)^p%2 = 1 := by
  induction p with
  | zero => decide
  | succ p ih => rw [pow_succ,Int.mul_emod,ih]; decide

def phaseCost (r : ℕ) : ℤ := 3^r-2^(r+1)

private theorem first_even_bound (w : Word) (odd : offset w % 2 = 1) :
    phaseCost (weight w) ≤ offset w := by
  cases w with
  | nil => norm_num [weight,offset,intercept,phaseCost]
  | cons b w =>
    cases b with
    | false =>
      simp only [weight,offset,intercept,phaseCost,pow_succ]
      linarith only [intercept_min w]
    | true =>
      simp only [weight,offset,intercept,pow_succ] at odd
      have Z : (3:ℤ)^weight w+2*intercept w-3^weight w*3 =
        2*(intercept w-3^weight w) := by ring
      rw [Z] at odd
      omega

private theorem phase_succ {n : ℕ} (positive : 1≤n) : phaseCost n < phaseCost (n+1) := by
  have P : (2:ℤ)^n<3^n := pow_lt_pow_left₀ (by norm_num) (by norm_num) (by omega)
  unfold phaseCost
  rw [pow_succ (3:ℤ) n,pow_succ (2:ℤ) (n+1),pow_succ (2:ℤ) n]
  linarith only [P]

theorem phase_increasing {r u : ℕ} (positive : 1≤r) (less : r<u) :
    phaseCost r < phaseCost u := by
  have H : r+1≤u := by omega
  induction u,H using Nat.le_induction with
  | base => exact phase_succ positive
  | succ u H IH => exact lt_trans (IH (by omega)) (phase_succ (by omega))

/-- An odd signed offset admits only grades below its explicit phase
    threshold. This bound applies uniformly over all word lengths. -/
theorem grade_ceiling (w : Word) (r : ℕ) (positive : 1≤r)
    (odd : offset w % 2 = 1) (cap : offset w ≤ phaseCost r) : weight w≤r := by
  by_contra! h
  have A := first_even_bound w odd
  have B := phase_increasing positive h
  omega

def coast (s : ℕ) : Word := List.replicate s false

def phase (r s : ℕ) : Word := false :: (List.replicate r true ++ coast s)

theorem coast_code (s : ℕ) : weight (coast s)=0 ∧ intercept (coast s)=0 := by
  induction s with
  | zero => decide
  | succ s ih => simp only [coast,List.replicate_succ,weight,intercept] at *;omega

private theorem phase_suffix (r s : ℕ) :
    weight (List.replicate r true ++ coast s)=r ∧
    intercept (List.replicate r true ++ coast s)=3^r-2^r := by
  induction r with
  | zero => simpa using coast_code s
  | succ r ih =>
    simp only [List.replicate_succ,List.cons_append,weight,intercept,ih.1,ih.2,pow_succ]
    constructor <;> first | trivial | ring

theorem phase_code (r s : ℕ) :
    weight (phase r s)=r ∧ offset (phase r s)=phaseCost r := by
  have S := phase_suffix r s
  simp only [phase,weight,offset,intercept,S.1,S.2,phaseCost,pow_succ]
  constructor <;> first | trivial | ring

/-- A first postpeak even followed by at least one odd and then any even
    coast already attains the largest grade of its signed-offset fibre. -/
theorem phase_maximal {r s : ℕ} (positive : 1≤r)
    {w : Word} (same : offset w=offset (phase r s)) : weight w≤r := by
  rw [(phase_code r s).2] at same
  apply grade_ceiling w r positive _ (le_of_eq same)
  rw [same]
  have O := odd_pow r
  unfold phaseCost
  rw [pow_succ]
  omega

theorem pure_coast_ceiling {s : ℕ} {w : Word} (same : offset w=offset (coast s)) :
    weight w≤1 := by
  have C := coast_code s
  have E : offset w = -1 := by simpa [offset,C.1,C.2] using same
  apply grade_ceiling w 1 (by decide)
  · rw [E];decide
  · rw [E];decide

end RampShadow.Postpeak

#print axioms RampShadow.Postpeak.phase_maximal
