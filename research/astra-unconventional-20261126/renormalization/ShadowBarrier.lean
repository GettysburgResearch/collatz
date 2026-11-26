import SignedBudget

/-! All reverse words up to the available ternary precision in an ordinary
endpoint 3^N+c. The bounds use the signed integer c as a comparison root. -/
namespace Collatz.ShadowBarrier
open Collatz.SourceDeletion Collatz.SignedBudget

theorem odd_le (h w : Nat) : odds h w ≤ h := by
  induction h generalizing w with
  | zero => rfl
  | succ h ih => simp only [odds]; have := ih (step w); omega

private theorem digits_le (h : Nat) (x : Int) : digits h x ≤ h := by
  induction h generalizing x with
  | zero => rfl
  | succ h ih => simp only [digits,bit]; split <;> have := ih (signedStep x) <;> omega

/-- The entire reverse path also ends at the stated signed center when the
source is translated by the homogeneous displacement. -/
theorem shadow_coeff {h w N : Nat} {A c : Int}
    (ending : (run h w : Int) = A*3^N+c) (depth : odds h w ≤ N) :
    ∃ s : Int, travel h s = c ∧ digits h s = odds h w ∧
      (w : Int) = s + 2^h*(A*3^(N-odds h w)) := by
  let q := odds h w
  let d : Int := A*3^(N-q)
  let s := (w:Int)-2^h*d
  have src : (w:Int) = s+2^h*d := by dsimp [s]; ring
  obtain ⟨a,b⟩ := signed_lift h s d
  obtain ⟨px,pq⟩ := physical h w
  rw [←src,px] at a
  rw [←src,pq] at b
  have psum : q+(N-q)=N := by dsimp [q]; omega
  have pows : (3:Int)^q*d=A*3^N := by
    dsimp [d]; rw [show (3:Int)^q*(A*3^(N-q))=A*(3^q*3^(N-q)) by ring, ←pow_add, psum]
  rw [←b] at a
  change (run h w:Int) = travel h s+3^q*d at a
  rw [ending, pows] at a
  exact ⟨s,by omega,b.symm,src⟩

theorem shadow {h w N : Nat} {c : Int}
    (ending : (run h w : Int) = 3^N+c) (depth : odds h w ≤ N) :
    ∃ s : Int, travel h s = c ∧ digits h s = odds h w ∧
      (w : Int) = s + 2^h*3^(N-odds h w) := by
  simpa only [one_mul] using shadow_coeff (A:=1) (by simpa only [one_mul] using ending) depth

private theorem affine_lower (h : Nat) (x : Int) :
    3^(digits h x)*x ≤ 2^h*travel h x := by
  induction h generalizing x with
  | zero => simp [digits,travel]
  | succ h ih =>
    have one : 3^(bit x)*x ≤ 2*signedStep x := by
      unfold bit signedStep
      split <;> simp only [pow_zero,pow_one,one_mul] <;> omega
    rw [digits,travel,pow_add,pow_succ]
    calc
      _ = 3^(digits h (signedStep x))*(3^(bit x)*x) := by ring
      _ ≤ 3^(digits h (signedStep x))*(2*signedStep x) :=
        Int.mul_le_mul_of_nonneg_left one (by positivity)
      _ = 2*(3^(digits h (signedStep x))*signedStep x) := by ring
      _ ≤ 2*(2^h*travel h (signedStep x)) := Int.mul_le_mul_of_nonneg_left (ih _) (by decide)
      _ = _ := by ring

private theorem nonpositive (h : Nat) (x : Int) (hx : x ≤ 0) : travel h x ≤ 0 := by
  induction h generalizing x with
  | zero => exact hx
  | succ h ih => apply ih; unfold signedStep; split <;> omega

private theorem above_fixed (h : Nat) (x : Int) (hx : -1 ≤ x) : -1 ≤ travel h x := by
  induction h generalizing x with
  | zero => exact hx
  | succ h ih => apply ih; unfold signedStep; split <;> omega

theorem negative_magnitude (h : Nat) (x : Int) (dst : travel h x ≤ -2) :
    -x ≤ 2^(h-digits h x)*(-travel h x) := by
  induction h generalizing x with
  | zero => simp [travel,digits]
  | succ h ih =>
    change travel h (signedStep x) ≤ -2 at dst
    have sx : signedStep x ≤ -2 := by
      by_contra! fail
      have := above_fixed h (signedStep x) (by omega)
      omega
    have rest := ih (signedStep x) dst
    have le := digits_le h (signedStep x)
    by_cases ev : x%2=0
    · have eqn : 2*signedStep x=x := by simp only [signedStep,ev,ite_true]; omega
      simp only [travel,digits,bit,ev,ite_true,Nat.add_zero]
      rw [show h+1-digits h (signedStep x) = (h-digits h (signedStep x))+1 by omega,pow_succ]
      linarith only [eqn,rest]
    · have eqn : 2*signedStep x=3*x+1 := by simp only [signedStep,ev,ite_false]; omega
      simp only [travel,digits,bit,ev,ite_false,Nat.add_sub_add_right]
      omega

/-- A positive integer center obstructs every small ordinary source with any
number of even moves, through N odd moves. -/
theorem positive_floor {h w N : Nat} {c : Int} (pos : 0<c)
    (ending : (run h w : Int) = 3^N+c) (depth : odds h w ≤ N) :
    (3:Int)^N ≤ c*w := by
  obtain ⟨s,hs,hq,ws⟩ := shadow ending depth
  have sp : 1 ≤ s := by
    by_contra! fail
    have := nonpositive h s (by omega)
    omega
  have a := affine_lower h s
  rw [hs,hq] at a
  let q := odds h w
  have eqn : (3:Int)^q*3^(N-q)=3^N := by rw [←pow_add]; congr 1; dsimp [q]; omega
  have powle : (3:Int)^q ≤ 2^h*c := by
    calc
      _ ≤ 3^q*s := by simpa using (Int.mul_le_mul_of_nonneg_left sp (show 0 ≤ (3:Int)^q by positivity))
      _ ≤ _ := a
  calc
    _ = 3^q*3^(N-q) := eqn.symm
    _ ≤ (2^h*c)*3^(N-q) := Int.mul_le_mul_of_nonneg_right powle (by positivity)
    _ = c*(2^h*3^(N-q)) := by ring
    _ ≤ c*w := Int.mul_le_mul_of_nonneg_left (by change (2:Int)^h*3^(N-odds h w) ≤ w; omega) (by omega)

/-- An integer negative center other than −1 costs at least three half-clocks
per available odd step in the squared estimate. -/
theorem negative_floor {h w N : Nat} {c : Int} (neg : c ≤ -2)
    (room : 2*(-c) ≤ (2:Int)^N)
    (ending : (run h w : Int) = 3^N+c) (depth : odds h w ≤ N) :
    (8:Int)^N ≤ 4*(w:Int)^2*potential c := by
  obtain ⟨s,hs,hq,ws⟩ := shadow ending depth
  have sp : s ≤ -2 := by
    by_contra! fail
    have := above_fixed h s (by omega)
    omega
  let q := odds h w
  let d : Int := 3^(N-q)
  have dq : q ≤ N := depth
  have hq' : q ≤ h := odd_le h w
  have sgn := negative_magnitude h s (hs ▸ neg)
  rw [hs,hq] at sgn
  have budget := negative_budget h s (hs ▸ neg)
  rw [hs,hq] at budget
  have ps : (1:Int) ≤ potential s := by
    have := potential_lower s
    nlinarith [mul_nonneg (show 0≤ -s-1 by omega) (show 0≤ -s+1 by omega)]
  have pc : 0 ≤ potential c := le_trans (sq_nonneg _) (potential_lower c)
  have p2 : (2:Int)^h=2^(h-q)*2^q := by rw [←pow_add]; congr 1; omega
  have pN : (2:Int)^N=2^q*2^(N-q) := by rw [←pow_add]; congr 1; omega
  have dw : 2*(-s) ≤ 2^h*d := calc
    _ ≤ 2*(2^(h-q)*(-c)) := Int.mul_le_mul_of_nonneg_left sgn (by decide)
    _ = 2^(h-q)*(2*(-c)) := by ring
    _ ≤ 2^(h-q)*2^N := Int.mul_le_mul_of_nonneg_left room (by positivity)
    _ = 2^h*2^(N-q) := by rw [pN,p2]; ring
    _ ≤ 2^h*d := Int.mul_le_mul_of_nonneg_left
      (by dsimp [d]; exact pow_le_pow_left₀ (by decide) (by decide) _) (by positivity)
  have ww : 2^h*d ≤ 2*(w:Int) := by change (w:Int)=s+2^h*d at ws; omega
  have source_cost : (8:Int)^q ≤ 4^h*potential c := calc
    _ ≤ 8^q*potential s := by simpa using (Int.mul_le_mul_of_nonneg_left ps (show 0≤(8:Int)^q by positivity))
    _ ≤ _ := budget
  have d8 : (8:Int)^(N-q) ≤ d^2 := by
    dsimp [d]
    rw [show ((3:Int)^(N-q))^2 = 9^(N-q) by rw [←pow_mul, Nat.mul_comm, pow_mul]; norm_num]
    exact pow_le_pow_left₀ (by decide) (by decide) _
  have sq : (2^h*d)^2 ≤ (2*(w:Int))^2 := by
    exact pow_le_pow_left₀ (by dsimp [d]; positivity) ww _
  calc
    _ = 8^q*8^(N-q) := by rw [←pow_add]; congr 1; omega
    _ ≤ (4^h*potential c)*d^2 := mul_le_mul source_cost d8 (by positivity) (by positivity)
    _ = (2^h*d)^2*potential c := by
      have h4 : (4:Int)^h = ((2:Int)^h)^2 := by
        calc
          _ = ((2:Int)^2)^h := by norm_num
          _ = _ := by rw [←pow_mul, Nat.mul_comm, pow_mul]
      rw [mul_pow,h4]; ring
    _ ≤ (2*(w:Int))^2*potential c := Int.mul_le_mul_of_nonneg_right sq pc
    _ = _ := by ring

#print axioms shadow_coeff
#print axioms shadow
#print axioms negative_magnitude
#print axioms positive_floor
#print axioms negative_floor
end Collatz.ShadowBarrier
