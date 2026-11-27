import CarryAlignment
import Portal

namespace Collatz.FirstPassage

/-- Cross-product numerator and denominator of the physical multiplicative
correction. They are kept separate so record comparisons use integers. -/
def distortionNum (n h : ℕ) : ℕ := 2^h * run n h

def distortionDen (n h : ℕ) : ℕ := 3^(odds n h)*n

private theorem run_at_succ (n h : ℕ) : run n (h+1)=step (run n h) := by
  induction h generalizing n with
  | zero => rfl
  | succ h ih => exact ih (step n)

private theorem odds_at_succ (n h : ℕ) : odds n (h+1)=odds n h + run n h%2 := by
  induction h generalizing n with
  | zero => simp [odds,run]
  | succ h ih =>
    change n%2+odds (step n) (h+1)=(n%2+odds (step n) h)+run (step n) h%2
    rw [ih]; omega

/-- If a lower odd departure first meets the distortion level at an actual
upper clock, nonnegative mixed clock and odd-grade differences force an exact
dyadic physical meeting at that clock's upper value. -/
theorem mixed_distortion_record {z t j d k : ℕ} (positive : 0<z)
    (oddAt : run z t%2=1)
    (clock : j=t+1+d) (grade : odds z t=odds (3*z) j+k)
    (before : distortionNum z t * distortionDen (3*z) j <
      distortionNum (3*z) j * distortionDen z t)
    (afterAt : distortionNum (3*z) j * distortionDen z (t+1) ≤
      distortionNum z (t+1) * distortionDen (3*z) j) :
    k=0 ∧ run z (t+1)=2^d * run (3*z) j := by
  let Y := run (3*z) j
  let X := run z (t+1)
  let w := run z t
  let q := odds (3*z) j
  let L := 2^t * 3^q*z
  have lpos : 0<L := by dsimp [L]; positivity
  have lpos' : 0<2*L := by positivity
  have extra : odds z (t+1)=q+k+1 := by rw [odds_at_succ,oddAt,grade]
  have sc : 2^j=2^t*2*2^d := by rw [clock]; ring
  have s : 2*X=3*w+1 := by
    have eq : X=step w := run_at_succ z t
    rw [eq]
    have h : w%2=1 := oddAt
    simp [step,h]
    omega
  have b₁ : L*(3*w)< L*(2*(2^d*3^k*Y)) := by
    calc
      _ = distortionNum z t * distortionDen (3*z) j := by
        dsimp [L,w,q,distortionNum,distortionDen]; ring
      _ < _ := before
      _ = _ := by
        simp only [distortionNum,distortionDen,grade,pow_add,sc]
        dsimp [L,Y,q]; ring
  have b₂ : (2*L)*(3*(2^d*3^k*Y)) ≤ (2*L)*(3*X) := by
    calc
      _ = distortionNum (3*z) j * distortionDen z (t+1) := by
        simp only [distortionNum,distortionDen,extra,pow_add,pow_one,sc]
        dsimp [L,Y,q]; ring
      _ ≤ _ := afterAt
      _ = _ := by
        dsimp [L,X,q,distortionNum,distortionDen]; ring
  have lower := (Nat.mul_lt_mul_left lpos).mp b₁
  have upper := (Nat.le_of_mul_le_mul_left b₂ lpos')
  have matchAt : X=2^d*3^k*Y := by omega
  cases k with
  | zero => simpa [X,Y] using matchAt
  | succ k =>
    have bad : X=3*(2^d*3^k*Y) := by rw [matchAt]; ring
    omega

#print axioms mixed_distortion_record

end Collatz.FirstPassage

namespace Collatz.FirstPassage

private theorem word_clock_grade (w : Collatz.TernaryPortal.Word) : w.grade≤w.clock := by
  induction w with
  | finish d => simp [Collatz.TernaryPortal.Word.grade,Collatz.TernaryPortal.Word.clock]
  | stage t ws ih =>
    simp only [Collatz.TernaryPortal.Word.grade, Collatz.TernaryPortal.Word.clock]
    omega

private theorem word_offset_floor (w : Collatz.TernaryPortal.Word) :
    3^w.grade ≤ w.offset+2^w.grade := by
  induction w with
  | finish d => simp [Collatz.TernaryPortal.Word.grade,Collatz.TernaryPortal.Word.offset]
  | stage t ws ih =>
    have hc : 2^ws.grade ≤ (2:ℕ)^ws.clock :=
      Nat.pow_le_pow_right (by decide) (word_clock_grade ws)
    simp only [Collatz.TernaryPortal.Word.grade,Collatz.TernaryPortal.Word.offset,pow_succ]
    omega

private theorem two_thirds_pow {r : ℕ} (big : 2≤r) : 2*2^r≤3^r := by
  obtain ⟨i,rfl⟩ := Nat.exists_eq_add_of_le big
  induction i with
  | zero => decide
  | succ i ih =>
    rw [show 2+(i+1)=(2+i)+1 by omega,pow_succ,pow_succ]
    omega

/-- The actual source decoded from any delayed record residual exceeds twice
the preceding lower odd. It cannot undercut the original least bad integer. -/
theorem decoded_record_size (w : Collatz.TernaryPortal.Word) {x n u : ℕ}
    (atOdd : 2*x=3*u+1) (late : 3≤w.clock)
    (small : 2*w.offset<2^w.clock)
    (link : 2^w.clock*x=3^w.grade*n+w.offset) : 2*u<n := by
  have count : w.grade+2≤w.clock := by
    by_contra! bad
    have big : 2≤w.grade := by omega
    have cl : w.clock≤w.grade+1 := by omega
    have two : 2^w.clock≤2^(w.grade+1) := Nat.pow_le_pow_right (by decide) cl
    rw [pow_succ] at two
    have hc := two_thirds_pow big
    have sub := word_offset_floor w
    omega
  have two : 2^(w.grade+2)≤2^w.clock := Nat.pow_le_pow_right (by decide) count
  rw [show 2^(w.grade+2)=4*2^w.grade by ring] at two
  have strict : 4*3^w.grade<3*2^w.clock := by
    have sub := word_offset_floor w
    omega
  have weak := Nat.mul_le_mul_right u strict.le
  have eq := congrArg (fun z : ℕ => 2^w.clock*z) atOdd
  by_contra! wrong
  have nsmall := Nat.mul_le_mul_left (3^w.grade) wrong
  nlinarith

#print axioms decoded_record_size

end Collatz.FirstPassage
