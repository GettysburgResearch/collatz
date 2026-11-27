import PeakRigidity
import Mathlib.Data.Nat.Factorization.Basic

/-! Integer separation for actual two-clock meetings of `n` and `3*n+2`.
`offset` retains the additive numerator of each of the two physical paths.
The relative guard is finite and can use any validated coefficient bound. -/
set_option autoImplicit false
set_option warningAsError true

namespace AsynchronousGuard
open CoreBranching PeakRigidity

def offset : ℕ → ℕ → ℕ
  | 0, _ => 0
  | k+1, n => 3^(run k n % 2) * offset k n + (run k n % 2) * 2^k

private theorem step_numerator (n : ℕ) :
    2 * step n = 3^(n%2)*n + n%2 := by
  by_cases he : n%2=0
  · simp [step, he]; omega
  · have ho : n%2=1 := by omega
    simp [step, ho]; omega

theorem affine (k n : ℕ) : 2^k * run k n = 3^(grade k n)*n + offset k n := by
  induction k with
  | zero => simp [run, grade, offset]
  | succ k ih =>
    have hlast : run (k+1) n = step (run k n) := by
      simpa [run] using run_add k 1 n
    rw [pow_succ, hlast, grade, pow_add, offset]
    calc
      _ = 2^k * (2 * step (run k n)) := by ring
      _ = 2^k * (3^(run k n % 2) * run k n + run k n % 2) := by rw [step_numerator]
      _ = 3^(run k n%2) * (2^k * run k n) + (run k n%2) * 2^k := by ring
      _ = _ := by rw [ih]; ring

/-- The numerator normalized by its odd multiplier is always below `2^k`.
The strict inequality includes the empty prefix. -/
theorem normalized_offset (k n : ℕ) : offset k n < 2^k * 3^(grade k n) := by
  induction k with
  | zero => simp [grade, offset]
  | succ k ih =>
    simp only [offset, grade, pow_succ 2 k, pow_add 3]
    have hbit := Nat.mod_lt (run k n) (by decide : 0<2)
    rcases (show run k n%2=0 ∨ run k n%2=1 by omega) with h|h
    · simp only [h, pow_zero, one_mul, zero_mul, add_zero, mul_one]
      nlinarith
    · simp only [h, pow_one, one_mul]
      have hpos : 0<(3:ℕ)^(grade k n) := by positivity
      nlinarith [Nat.mul_le_mul_left (2^k) hpos]

def leftSlope (i j n : ℕ) := 2^j * 3^(grade i n)
def rightSlope (i j n : ℕ) := 2^i * 3^(grade j (3*n+2)+1)

/-- Exact identity at any actual intersection, with the two clocks independent. -/
theorem crossing {n i j : ℕ} (h : run i n=run j (3*n+2)) :
    leftSlope i j n*n + 2^j*offset i n =
      rightSlope i j n*n + 2^i*(2*3^(grade j (3*n+2)) + offset j (3*n+2)) := by
  have a := congrArg (fun z : ℕ => 2^j*z) (affine i n)
  have b := congrArg (fun z : ℕ => 2^i*z) (affine j (3*n+2))
  rw [h] at a
  unfold leftSlope rightSlope
  rw [pow_succ]
  nlinarith only [a,b]

/-- A lower bound on the separation between two distinct integer slopes,
combined with bounds on both normalized offsets, excludes an accidental root. -/
theorem relative_separation {P Q L R n A B : ℕ}
    (eqn : P*n+L=Q*n+R) (hl : L≤P*A) (hr : R≤Q*A)
    (hsep : ∀ d, 0<d → (P+d=Q ∨ Q+d=P) → min P Q ≤ B*d)
    (hlarge : B*A<n) : P=Q := by
  by_contra ne
  rcases lt_or_gt_of_ne ne with lt|gt
  · let d := Q-P
    have hd : 0<d := by dsimp [d]; omega
    have he : P+d=Q := by dsimp [d]; omega
    have hs := hsep d hd (Or.inl he)
    rw [min_eq_left (le_of_lt lt)] at hs
    have cross : d*n ≤ L := by rw [←he, Nat.add_mul] at eqn; omega
    have chain : d*n ≤ d*(B*A) := calc
      _ ≤ L := cross
      _ ≤ P*A := hl
      _ ≤ (B*d)*A := Nat.mul_le_mul_right A hs
      _ = _ := by ring
    exact (Nat.mul_lt_mul_of_pos_left hlarge hd).not_ge chain
  · let d := P-Q
    have hd : 0<d := by dsimp [d]; omega
    have he : Q+d=P := by dsimp [d]; omega
    have hs := hsep d hd (Or.inr he)
    rw [min_eq_right (le_of_lt gt)] at hs
    have cross : d*n ≤ R := by rw [←he, Nat.add_mul] at eqn; omega
    have chain : d*n ≤ d*(B*A) := calc
      _ ≤ R := cross
      _ ≤ Q*A := hr
      _ ≤ (B*d)*A := Nat.mul_le_mul_right A hs
      _ = _ := by ring
    exact (Nat.mul_lt_mul_of_pos_left hlarge hd).not_ge chain

private theorem clock_factor (a b : ℕ) : (2^a * 3^b : ℕ).factorization 2 = a := by
  rw [Nat.factorization_mul (by positivity) (by positivity), Finsupp.add_apply,
      Nat.factorization_pow_self Nat.prime_two, Nat.Prime.factorization_pow Nat.prime_three]
  simp

theorem aligned_of_equal_slopes {i j n : ℕ} (h : leftSlope i j n=rightSlope i j n) :
    i=j ∧ grade i n=grade j (3*n+2)+1 := by
  unfold leftSlope rightSlope at h
  have hc := congrArg (fun z : ℕ => z.factorization 2) h
  simp only [clock_factor] at hc
  subst j
  have hh : 3^(grade i n)=3^(grade i (3*n+2)+1) := Nat.eq_of_mul_eq_mul_left (by positivity) h
  exact ⟨rfl,(pow_right_inj₀ (by decide : 0<(3:ℕ)) (by decide : (3:ℕ)≠1)).mp hh⟩

/-- Finite certificate for an actual asynchronous meeting. The offset and
slope hypotheses are computable from the two actual prefixes. -/
theorem meeting_is_aligned {n i j A B : ℕ} (meet : run i n=run j (3*n+2))
    (left : 2^j*offset i n≤leftSlope i j n*A)
    (right : 2^i*(2*3^(grade j (3*n+2))+offset j (3*n+2))≤rightSlope i j n*A)
    (gap : ∀ d, 0<d → (leftSlope i j n+d=rightSlope i j n ∨
      rightSlope i j n+d=leftSlope i j n) → min (leftSlope i j n) (rightSlope i j n)≤B*d)
    (large : B*A<n) : i=j ∧ grade i n=grade j (3*n+2)+1 :=
  aligned_of_equal_slopes (relative_separation (crossing meet) left right gap large)

/-- Individual odd counts change by at most one per physical clock. -/
theorem grade_window (start extra n : ℕ) :
    grade start n ≤ grade (start+extra) n ∧
    grade (start+extra) n ≤ grade start n + extra := by
  induction extra with
  | zero => simp
  | succ e ih =>
    rw [Nat.add_succ,grade]
    have bit := Nat.mod_lt (run (start+e) n) (by decide : 0<2)
    omega

private theorem grade_join (a b n : ℕ) :
    grade (a+b) n=grade a n+grade b (run a n) := by
  induction b with
  | zero => simp [grade]
  | succ b ih => rw [Nat.add_succ,grade,ih,run_add,grade,Nat.add_assoc]

/-- A meeting at matched formal grade remains a meeting at all later clocks. -/
theorem counted_persists {i n : ℕ} (same : run i n=run i (3*n+2))
    (count : grade i n=grade i (3*n+2)+1) (extra : ℕ) :
    run (i+extra) n=run (i+extra) (3*n+2) ∧
      grade (i+extra) n=grade (i+extra) (3*n+2)+1 := by
  constructor
  · rw [run_add,run_add,same]
  · rw [grade_join,grade_join,same,count]
    omega

/-- A signed count gap larger than the time extension precludes every
meeting in the full two-clock square when all physical meetings there align.
The guard tests real integer paths, including both earlier and later clocks. -/
theorem no_meeting_from_gap {n J h : ℕ}
    (large : grade J n+h < grade J (3*n+2)+1 ∨
       grade J (3*n+2)+1+h < grade J n)
    (align : ∀ i j, i≤J+h → j≤J+h → run i n=run j (3*n+2) →
        i=j ∧ grade i n=grade j (3*n+2)+1) :
    ∀ i j, i≤J+h → j≤J+h → run i n≠run j (3*n+2) := by
  intro i j hi hj eqv
  obtain ⟨rfl,counts⟩ := align i j hi hj eqv
  have hfinal := (counted_persists eqv counts (J+h-i)).2
  rw [show i+(J+h-i)=J+h by omega] at hfinal
  have g := grade_window J h n
  have g' := grade_window J h (3*n+2)
  omega

#print axioms affine
#print axioms meeting_is_aligned
#print axioms no_meeting_from_gap

end AsynchronousGuard
