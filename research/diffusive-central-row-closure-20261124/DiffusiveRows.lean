import Mathlib

/-! Finite arithmetic interfaces. Uncompiled candidate.
    No analytic estimate and no Collatz hypothesis is declared as an axiom. -/

namespace DiffusiveRows

def shortcut (x : ℕ) : ℕ := if x % 2 = 0 then x / 2 else (3*x+1)/2

def walk (F : ℕ → ℕ) : ℕ → ℕ → ℕ
  | 0, x => x
  | k+1, x => walk F k (F x)

theorem walk_add (F : ℕ → ℕ) (i j x : ℕ) :
    walk F (i+j) x = walk F j (walk F i x) := by
  induction i generalizing x with
  | zero => simp [walk]
  | succ i ih =>
    rw [Nat.succ_add]
    change walk F (i+j) (F x) = walk F j (walk F i (F x))
    exact ih (F x)

theorem balanced_clock (b i A : ℕ) (hi : i ≤ b) (hA : A ≤ 2*b) :
    (b-i)+i=b ∧ (2*b-A)+A=2*b := by omega

theorem central_window (b i A n t : ℕ)
    (hi : i ≤ b) (hA : A ≤ 2*b)
    (hn : n=b-i) (ht : t=2*b-A)
    (hlo : i ≤ A) (hhi : A ≤ 3*i) :
    t ≤ 2*n+i ∧ 2*n ≤ t+i := by omega

/-- No repeats on a recorded segment ending at a nonperiodic state. -/
theorem repeat_forces_period (F : ℕ → ℕ) (x q i j b : ℕ)
    (hij : i < j) (hjb : j ≤ b)
    (hrep : walk F i x = walk F j x)
    (hq : walk F b x = q) :
    ∃ k > 0, walk F k q = q := by
  refine ⟨j-i, by omega, ?_⟩
  have h1 : i+(j-i)=j := by omega
  have h2 : j+(b-j)=b := by omega
  have hp : walk F (j-i) (walk F j x) = walk F j x := by
    calc
      walk F (j-i) (walk F j x) = walk F (j-i) (walk F i x) := by rw [hrep]
      _ = walk F (i+(j-i)) x := (walk_add F i (j-i) x).symm
      _ = walk F j x := by rw [h1]
  have hq' : walk F (b-j) (walk F j x) = q := by
    rw [← walk_add, h2, hq]
  calc
    walk F (j-i) q = walk F (j-i) (walk F (b-j) (walk F j x)) :=
      congrArg (walk F (j-i)) hq'.symm
    _ = walk F ((b-j)+(j-i)) (walk F j x) := (walk_add F (b-j) (j-i) _).symm
    _ = walk F ((j-i)+(b-j)) (walk F j x) := by rw [Nat.add_comm (b-j) (j-i)]
    _ = walk F (b-j) (walk F (j-i) (walk F j x)) := walk_add F (j-i) (b-j) _
    _ = q := by rw [hp, hq']

/-- The affine carry of a concatenation, with all divisions cleared. -/
theorem concatenate_carry (x y q A B C D E H : ℤ)
    (h1 : A*y=B*x+C) (h2 : D*q=E*y+H) :
    A*D*q=E*B*x+E*C+A*H := by
  calc
    A*D*q=A*(D*q) := by ring
    _ = A*(E*y+H) := by rw [h2]
    _ = E*(A*y)+A*H := by ring
    _ = E*B*x+E*C+A*H := by rw [h1]; ring

/-- A nonnegative front correction cannot reduce the relative carry of the
    supplied suffix, with the rational threshold u/v cleared. -/
theorem suffix_carry_monotone (A E C H q D u v : ℤ)
    (hA : 0 ≤ A) (hE : 0 ≤ E) (hC : 0 ≤ C) (hv : 0 ≤ v)
    (hs : u*D*q ≤ v*H) :
    u*(A*D)*q ≤ v*(E*C+A*H) := by
  have h := mul_le_mul_of_nonneg_left hs hA
  have hp := mul_nonneg hv (mul_nonneg hE hC)
  nlinarith only [h,hp]

/-- Exact normalization of the prefix amplification, without square roots.
    A0=2^A_i, P0=3^i, X0=original gate, Dnum/Dden=distortion. -/
theorem moving_target_normalization
    (twoPrefix twoSuffix fourTotal threePrefix threeSuffix threeTotal
      a q Dnum Dden : ℤ)
    (ht : twoPrefix*twoSuffix=fourTotal)
    (hb : threePrefix*threeSuffix=threeTotal)
    (ha : twoSuffix*q*Dden=threeSuffix*a*Dnum) :
    twoPrefix*threeTotal*a*Dnum =
      fourTotal*threePrefix*q*Dden := by
  calc
    twoPrefix*threeTotal*a*Dnum =
        (twoPrefix*threePrefix)*(threeSuffix*a*Dnum) := by rw [← hb]; ring
    _ = (twoPrefix*threePrefix)*(twoSuffix*q*Dden) := by rw [ha]
    _ = (twoPrefix*twoSuffix)*threePrefix*q*Dden := by ring
    _ = fourTotal*threePrefix*q*Dden := by rw [ht]

/-- Every selected gate gives a terminal in a finite list of actual orbit
    values. This interface preserves the gate-to-terminal length. -/
theorem gate_terminal (F : ℕ → ℕ) (x g q k b : ℕ)
    (hk : k ≤ b) (hg : walk F k x=g) (hq : walk F b x=q) :
    walk F (b-k) g=q := by
  rw [← hg, ← walk_add]
  have h : k+(b-k)=b := by omega
  rw [h,hq]

/-- The exact clock inequality used by the upper localization. -/
theorem gate_time (total suffix gate first : ℕ)
    (h1 : gate+suffix=total) (h2 : first≤gate) :
    first+suffix≤total := by omega

/-- A full cycle with affine multiplier lambda=B/A has positive
    correction H; its r-fold carry is q(1-lambda^r) after normalization. -/
theorem cycle_lap (B H q : ℚ) (h : q = B*q + H) (x : ℚ) :
    q-(B*x+H)=B*(q-x) := by linarith only [h]

def affineRun (B H : ℚ) (x : ℚ) : ℕ → ℚ
  | 0 => x
  | r+1 => B * affineRun B H x r + H

theorem iterated_cycle_defect (B H q : ℚ) (h : q=B*q+H) (x : ℚ) (r : ℕ) :
    q - affineRun B H x r = B^r*(q-x) := by
  induction r with
  | zero => simp [affineRun]
  | succ r ih =>
    rw [affineRun, cycle_lap B H q h, ih, pow_succ]
    ring

end DiffusiveRows

#print axioms DiffusiveRows.walk_add
#print axioms DiffusiveRows.balanced_clock
#print axioms DiffusiveRows.central_window
#print axioms DiffusiveRows.repeat_forces_period
#print axioms DiffusiveRows.concatenate_carry
#print axioms DiffusiveRows.suffix_carry_monotone
#print axioms DiffusiveRows.moving_target_normalization
#print axioms DiffusiveRows.gate_terminal
#print axioms DiffusiveRows.gate_time
#print axioms DiffusiveRows.cycle_lap
#print axioms DiffusiveRows.iterated_cycle_defect
