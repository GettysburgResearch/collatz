import Std

namespace PrescribedReturns

def step (x : Nat) : Nat := if x % 2 = 0 then x / 2 else (3*x+1)/2

def run : Nat → Nat → Nat
  | 0, x => x
  | h+1, x => run h (step x)

/-- A shortcut ending at a multiple of three was an ordinary halving. -/
theorem onlyEvenPreimage (x z : Nat) (h : step x = 3*z) : x = 2*(3*z) := by
  unfold step at h
  split at h <;> omega

theorem preimageTriple (k x u : Nat) (h : run k x = 3*u) : x = 2^k * (3*u) := by
  induction k generalizing x with
  | zero => simpa [run] using h
  | succ k ih =>
    have a := ih (step x) h
    have b : step x = 3*(2^k*u) := by rw [a]; ac_rfl
    rw [onlyEvenPreimage x _ b, Nat.pow_succ]
    ac_rfl

/-- The inhomogeneous line's second arm can never flow into the homogeneous
    line, even if the first arm is allowed to use an unrelated clock. -/
theorem noReturnToTriple (j x u : Nat) : run j (9*x+2) ≠ 3*u := by
  intro h
  have e := preimageTriple j (9*x+2) u h
  have t : 2^j*(3*u) = 3*(2^j*u) := by ac_rfl
  rw [t] at e
  omega

theorem evenRun (k x : Nat) : run k (2^k*x) = x := by
  induction k with
  | zero => simp [run]
  | succ k ih =>
    rw [Nat.pow_succ]
    have eqn : 2^k*2*x = 2*(2^k*x) := by ac_rfl
    simpa [eqn, run, step] using ih

theorem homogeneousFiber (k x u : Nat) :
    run k (3*x) = 3*u ↔ x = 2^k*u := by
  constructor
  · intro h
    have e := preimageTriple k (3*x) u h
    have ee : 3*x = 3*(2^k*u) := by rw [e]; ac_rfl
    omega
  · rintro rfl
    have e : 3*(2^k*u) = 2^k*(3*u) := by ac_rfl
    rw [e, evenRun]

def odds : Nat → Nat → Nat
  | 0, _ => 0
  | h+1, x => x % 2 + odds h (step x)

private theorem liftStep (t x : Nat) :
    step (2*t+x) = 3^(x%2)*t + step x := by
  have e : (2*t+x)%2=x%2 := by omega
  unfold step
  rw [e]
  by_cases h : x%2=0
  · simp [h]; omega
  · have h1 : x%2=1 := by omega
    simp [h1]
    omega

theorem liftRun (h b x : Nat) :
    run h (2^h*b+x) = 3^(odds h x)*b + run h x := by
  induction h generalizing b x with
  | zero => simp [run, odds]
  | succ h ih =>
    have e : 2^(h+1)*b = 2*(2^h*b) := by rw [Nat.pow_succ]; ac_rfl
    have f : 3^(x%2)*(2^h*b) = 2^h*(3^(x%2)*b) := by ac_rfl
    rw [e, run, liftStep, f, ih, odds, Nat.pow_add, run]
    ac_rfl

theorem merge46 (b : Nat) :
    run 6 (64*b+46) = 27*b+20 ∧ run 6 (9*(64*b+46)+2) = 27*b+20 := by
  have a := liftRun 6 b 46
  have c := liftRun 6 (9*b) 416
  change run 6 (64*b+46) = 27*b+20 at a
  change run 6 (64*(9*b)+416) = 3*(9*b)+20 at c
  constructor
  · exact a
  · rw [show 9*(64*b+46)+2 = 64*(9*b)+416 by omega, c]
    omega

theorem merge23 (b : Nat) :
    run 5 (32*b+23) = 27*b+20 ∧ run 5 (3*(32*b+23)) = 27*b+20 := by
  have a := liftRun 5 b 23
  have c := liftRun 5 (3*b) 69
  change run 5 (32*b+23) = 27*b+20 at a
  change run 5 (32*(3*b)+69) = 9*(3*b)+20 at c
  constructor
  · exact a
  · rw [show 3*(32*b+23) = 32*(3*b)+69 by omega, c]
    omega

theorem return2830 (b : Nat) :
    run 12 (4096*b+2830) = 81*b+56 ∧
    run 12 (9*(4096*b+2830)+2) = 9*(81*b+56)+2 := by
  have a := liftRun 12 b 2830
  have c := liftRun 12 (9*b) 25472
  change run 12 (4096*b+2830) = 81*b+56 at a
  change run 12 (4096*(9*b)+25472) = 81*(9*b)+506 at c
  constructor
  · exact a
  · rw [show 9*(4096*b+2830)+2 = 4096*(9*b)+25472 by omega, c]
    omega

private theorem runAdd (a b x : Nat) : run (a+b) x = run b (run a x) := by
  induction a generalizing x with
  | zero => simp [run]
  | succ a ih => simpa [Nat.succ_add, run] using ih (step x)

private theorem allOdds (h x z : Nat) (rep : x+1=2^h*z) :
    run h x+1=3^h*z := by
  induction h generalizing x z with
  | zero => simpa [run] using rep
  | succ h ih =>
    have eqn : x+1=2*(2^h*z) := by
      simpa only [Nat.pow_succ, Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm] using rep
    have s : step x+1=3*(2^h*z) := by unfold step; split <;> omega
    have s' : step x+1=2^h*(3*z) := s.trans (by ac_rfl)
    simpa [run, Nat.pow_succ, Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm] using ih _ _ s'

private theorem upperThree (x W : Nat) (rep : x+1=8*W) :
    run 3 (3*x)+1=9*W := by
  have Wpos : 0<W := by omega
  obtain ⟨w, rfl⟩ := Nat.exists_eq_succ_of_ne_zero (Nat.ne_of_gt Wpos)
  have a := liftRun 3 (3*w) 21
  change run 3 (8*(3*w)+21) = 3*(3*w)+8 at a
  rw [show 3*x=8*(3*w)+21 by omega, a]
  omega

/-- Transferring h+3 factors of three from u+1 into factors of two gives the
    exact state of both new arms after the common inverse-prefix length. -/
theorem exchangedPrefix (h w u v : Nat)
    (hu : u+1=3^(h+3)*w) (hv : v+1=2^(h+3)*w) :
    run (h+3) v=u ∧ 3*run (h+3) (3*v)+2=u := by
  have first := allOdds _ _ _ hv
  have hv' : v+1=8*(2^h*w) := by
    rw [Nat.pow_add] at hv
    simpa only [Nat.reducePow, Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm] using hv
  have s := upperThree v (2^h*w) hv'
  have s' : run 3 (3*v)+1=2^h*(9*w) := s.trans (by ac_rfl)
  have a := allOdds _ _ _ s'
  have it : run (h+3) (3*v)=run h (run 3 (3*v)) := by
    rw [Nat.add_comm h 3, runAdd]
  have hu' : u+1=3*(3^h*(9*w)) := by
    rw [Nat.pow_add] at hu
    calc
      u+1 = 3^h*(27*w) := by simpa only [Nat.reducePow, Nat.mul_assoc] using hu
      _ = 3^h*((3*9)*w) := rfl
      _ = 3*(3^h*(9*w)) := by ac_rfl
  omega

private theorem replaySeven (u x : Nat) (e : 3*x+2=u) (r : u%8=7) :
    run 3 x=run 3 (3*u) := by
  let a := x/8
  have xrep : x=8*a+7 := by dsimp [a]; omega
  have lo := liftRun 3 a 7
  have hi := liftRun 3 (9*a) 69
  change run 3 (8*a+7)=27*a+26 at lo
  change run 3 (8*(9*a)+69)=3*(9*a)+26 at hi
  rw [show 3*u=8*(9*a)+69 by omega, hi, xrep, lo]
  omega

private theorem replayFive (u x : Nat) (e : 3*x+2=u) (r : u%8=5) :
    run 3 x=run 3 u := by
  let a := x/8
  have xrep : x=8*a+1 := by dsimp [a]; omega
  have lo := liftRun 3 a 1
  have hi := liftRun 3 (3*a) 5
  change run 3 (8*a+1)=9*a+2 at lo
  change run 3 (8*(3*a)+5)=3*(3*a)+2 at hi
  rw [show u=8*(3*a)+5 by omega, hi, xrep, lo]
  omega

theorem exchangedNineReplay (h w u v : Nat) (hu : u+1=3^(h+3)*w)
    (hv : v+1=2^(h+3)*w) (r : u%8=7) :
    run (h+3+3) v=run 3 u ∧ run (h+3+3) (3*v)=run 3 (3*u) := by
  obtain ⟨lo,hi⟩ := exchangedPrefix h w u v hu hv
  rw [runAdd (h+3) 3, runAdd (h+3) 3, lo]
  exact ⟨rfl, replaySeven u _ hi r⟩

theorem exchangedThreeFusion (h w u v : Nat) (hu : u+1=3^(h+3)*w)
    (hv : v+1=2^(h+3)*w) (r : u%8=5) :
    run (h+3+3) v=run 3 u ∧ run (h+3+3) (3*v)=run 3 u := by
  obtain ⟨lo,hi⟩ := exchangedPrefix h w u v hu hv
  rw [runAdd (h+3) 3, runAdd (h+3) 3, lo]
  exact ⟨rfl, replayFive u _ hi r⟩

/-- Positive affine records equal at a large parameter must have equal slopes
when both intercepts are strictly below the parameter. -/
theorem sameSlope (a b c e x : Nat) (eqn : a*x+c = b*x+e)
    (hc : c < x) (he : e < x) : a = b := by
  by_cases hab : a < b
  · have le := Nat.mul_le_mul_right x (show a+1 ≤ b by omega)
    rw [Nat.add_mul, Nat.one_mul] at le
    omega
  · by_cases hba : b < a
    · have le := Nat.mul_le_mul_right x (show b+1 ≤ a by omega)
      rw [Nat.add_mul, Nat.one_mul] at le
      omega
    · omega

/-- A repeated affine inverse block forces exponential divisibility of the
    first displacement, even when only a finite number of repeats is known. -/
theorem repeatDivides (A B : Nat) (cop : B.Coprime A) (d : Nat → Nat)
    (j : Nat) (rec : ∀ i, i < j → B*d (i+1) = A*d i) : B^j ∣ d 0 := by
  have eqn : ∀ k, k ≤ j → B^k*d k = A^k*d 0 := by
    intro k
    induction k with
    | zero => simp
    | succ k ih =>
      intro hk
      calc
        B^(k+1)*d (k+1) = B^k*(B*d (k+1)) := by rw [Nat.pow_succ, Nat.mul_assoc]
        _ = B^k*(A*d k) := by rw [rec k (by omega)]
        _ = A*(B^k*d k) := by ac_rfl
        _ = A*(A^k*d 0) := by rw [ih (by omega)]
        _ = A^(k+1)*d 0 := by rw [Nat.pow_succ]; ac_rfl
  exact (cop.pow j j).dvd_of_dvd_mul_left ⟨d j, (eqn j (by omega)).symm⟩

theorem infiniteRepeatFixed (A B : Nat) (cop : B.Coprime A) (hB : 1 < B)
    (z : Nat → Int) (C : Int) (rec : ∀ i, (A:Int)*z i = (B:Int)*z (i+1)+C) :
    ∀ i, z (i+1) = z i := by
  intro i
  let d (k : Nat) := (z (i+k+1)-z (i+k)).natAbs
  have hrec (k : Nat) : B*d (k+1) = A*d k := by
    have h0 := rec (i+k)
    have h1 := rec (i+k+1)
    have e : (B:Int)*(z (i+k+1+1)-z (i+k+1)) =
             (A:Int)*(z (i+k+1)-z (i+k)) := by
      rw [Int.mul_sub, Int.mul_sub]
      omega
    simpa [d, Int.natAbs_mul, Nat.add_assoc] using congrArg Int.natAbs e
  have div := repeatDivides A B cop d (d 0) (fun k _ => hrec k)
  have small : d 0 < B^(d 0) := Nat.lt_pow_self hB
  have zero : d 0 = 0 := by
    by_cases hz : d 0 = 0
    · exact hz
    · have := Nat.le_of_dvd (Nat.pos_of_ne_zero hz) div
      omega
  have e : (z (i+1)-z i).natAbs = 0 := by simpa [d] using zero
  exact Int.sub_eq_zero.mp (Int.natAbs_eq_zero.mp e)

end PrescribedReturns
