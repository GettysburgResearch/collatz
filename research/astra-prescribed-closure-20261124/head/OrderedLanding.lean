import Std

/-! Ordinary finite paths used by the two grade alignments. -/
namespace OrderedLanding

def T (n : Nat) : Nat := if n % 2 = 0 then n / 2 else (3*n+1)/2

def run : Nat → Nat → Nat
  | 0, n => n
  | h+1, n => run h (T n)

theorem joinRuns (i j n : Nat) : run (i+j) n = run j (run i n) := by
  induction i generalizing n with
  | zero => simp [run]
  | succ i ih => simpa [Nat.succ_add, run] using ih (T n)

theorem evens (h x : Nat) : run h (2^h*x) = x := by
  induction h with
  | zero => simp [run]
  | succ h ih =>
    have step : T (2^(h+1)*x) = 2^h*x := by
      simp only [Nat.pow_succ]
      unfold T
      have e : 2^h*2*x = 2*(2^h*x) := by ac_rfl
      rw [e]
      simp
    simpa only [run, step] using ih

theorem odds (h n x : Nat) (hrep : n+1 = 2^h*x) :
    run h n + 1 = 3^h*x := by
  induction h generalizing n x with
  | zero => simpa [run] using hrep
  | succ h ih =>
    have hr : n+1 = 2*(2^h*x) := by simpa only [Nat.pow_succ, Nat.mul_assoc, Nat.mul_left_comm, Nat.mul_comm] using hrep
    have step : T n + 1 = 2^h*(3*x) := by
      have e : 2^h*(3*x) = 3*(2^h*x) := by ac_rfl
      rw [e]
      unfold T
      split <;> omega
    simpa [run, Nat.pow_succ, Nat.mul_assoc, Nat.mul_left_comm, Nat.mul_comm] using ih (T n) (3*x) step

/-- Two actual color-preserving arms of the lift based at the first state. -/
theorem lowerLift (j u A : Nat) (rep : 3*u+1=2^(j+1)*A) :
    run (j+1) u = A ∧ run (j+1) (3*u)+1 = 3^(j+1)*A := by
  have hr : 3*u+1 = 2*(2^j*A) := by simpa only [Nat.pow_succ, Nat.mul_assoc, Nat.mul_left_comm, Nat.mul_comm] using rep
  have step : T u = 2^j*A := by unfold T; split <;> omega
  exact ⟨by simpa only [run, step] using evens j A, odds (j+1) (3*u) A rep⟩

private theorem twoPlusOne (u w : Nat) (rep : u=4*w+1) : run 2 u = 3*w+1 := by
  simp only [run, T]
  split <;> split <;> omega

private theorem plusOne (j B : Nat) : run (2*j) (4^j*B+1) = 3^j*B+1 := by
  induction j generalizing B with
  | zero => simp [run]
  | succ j ih =>
    have clock : 2*(j+1)=2+2*j := by omega
    have e : 4^(j+1)*B = 4*(4^j*B) := by rw [Nat.pow_succ]; ac_rfl
    rw [clock, joinRuns, twoPlusOne _ (4^j*B) (by rw [e])]
    have f : 3*(4^j*B) = 4^j*(3*B) := by ac_rfl
    rw [f, ih]
    simp [Nat.pow_succ, Nat.mul_assoc]

private theorem upperTwo (u A : Nat) (rep : 9*u+1=4*A) :
    run 2 u = A+1 := by
  simp only [run, T]
  split <;> split <;> omega

private theorem powers (j : Nat) : 2^(2*j) = 4^j := by
  simpa using (Nat.pow_mul 2 2 j)

theorem upperEven (j u B : Nat) (rep : 9*u+1=2^(2*j+2)*B) :
    run (2*j+2) (3*u) = B ∧ run (2*j+2) u = 3^j*B+1 := by
  have upper := (lowerLift (2*j+1) (3*u) B (by change 3*(3*u)+1=_; rw [← rep]; omega)).1
  have hr : 9*u+1 = 4*(4^j*B) := by
    rw [Nat.pow_add, powers] at rep
    simpa only [Nat.mul_comm, Nat.mul_left_comm, Nat.mul_assoc] using rep
  have clock : 2*j+2=2+2*j := by omega
  exact ⟨upper, by rw [clock, joinRuns, upperTwo _ _ hr, plusOne]⟩

theorem upperOdd (j u B : Nat) (rep : 9*u+1=2^(2*j+3)*B) :
    run (2*j+3) (3*u) = B ∧ run (2*j+3) u = 3^(j+1)*B+2 := by
  have hr : 9*u+1=2^(2*j+2)*(2*B) := by
    rw [← Nat.mul_assoc, ← Nat.pow_succ]
    exact rep
  have early := (upperEven j u (2*B) hr).2
  have upper := (lowerLift (2*j+2) (3*u) B (by change 3*(3*u)+1=_; rw [← rep]; omega)).1
  have e : 3^j*(2*B) = 2*(3^j*B) := by ac_rfl
  have f : 3^(j+1)*B = 3*(3^j*B) := by rw [Nat.pow_succ]; ac_rfl
  refine ⟨upper, ?_⟩
  rw [show 2*j+3 = (2*j+2)+1 by omega, joinRuns, early, e, f]
  simp only [run, T]
  split <;> omega

/-- Finite residue menus after an arbitrary previously chosen base exponent.
    The input residue is the reduced value of 2^base times the physical state. -/
theorem lowerMenu : ∀ x : Fin 9, x.val % 3 ≠ 0 →
    ∃ j : Fin 6, (2^j.val*x.val)%9=4 := by decide

theorem upperMenu : ∀ x : Fin 27, x.val % 3 ≠ 0 →
    ∃ j : Fin 18, (2^j.val*x.val)%27=10 := by decide

/-- A failed endpoint equality rules out every earlier shared-clock meeting. -/
theorem prefixDistinct (K A B : Nat) (h : run K A ≠ run K B)
    (t : Nat) (ht : t ≤ K) : run t A ≠ run t B := by
  intro eq
  have hk : K=t+(K-t) := by omega
  apply h
  calc
    run K A = run (K-t) (run t A) := (congrArg (fun j => run j A) hk).trans (joinRuns t (K-t) A)
    _ = run (K-t) (run t B) := by rw [eq]
    _ = run K B := ((congrArg (fun j => run j B) hk).trans (joinRuns t (K-t) B)).symm

/-- In the first forced cylinder the two records stay separate through the
    whole prescribed binary word, on every positive ordinary lift. -/
theorem lowerNoSync (j u A t : Nat) (pos : 0<A)
    (rep : 3*u+1=2^(j+1)*A) (ht : t≤j+1) : run t u ≠ run t (3*u) := by
  apply prefixDistinct (j+1) u (3*u) _ t ht
  obtain ⟨lo,hi⟩ := lowerLift j u A rep
  rw [lo]
  intro eq
  have power : 0 < 3^j := Nat.pow_pos (by decide)
  have size : A ≤ 3^j*A := Nat.le_mul_of_pos_left A power
  have ident : 3^(j+1)*A=3*(3^j*A) := by rw [Nat.pow_succ]; ac_rfl
  rw [ident, ← eq] at hi
  omega

theorem upperEvenNoSync (j u B t : Nat)
    (rep : 9*u+1=2^(2*j+2)*B) (ht : t≤2*j+2) :
    run t u ≠ run t (3*u) := by
  apply prefixDistinct (2*j+2) u (3*u) _ t ht
  obtain ⟨hi,lo⟩ := upperEven j u B rep
  have size : B≤3^j*B := Nat.le_mul_of_pos_left B (Nat.pow_pos (by decide))
  rw [hi,lo]
  omega

theorem upperOddNoSync (j u B t : Nat)
    (rep : 9*u+1=2^(2*j+3)*B) (ht : t≤2*j+3) :
    run t u ≠ run t (3*u) := by
  apply prefixDistinct (2*j+3) u (3*u) _ t ht
  obtain ⟨hi,lo⟩ := upperOdd j u B rep
  have size : B≤3^(j+1)*B := Nat.le_mul_of_pos_left B (Nat.pow_pos (by decide))
  rw [hi,lo]
  omega

#print axioms lowerNoSync
#print axioms upperEvenNoSync
#print axioms upperOddNoSync
#print axioms lowerLift
#print axioms upperEven
#print axioms upperOdd
#print axioms lowerMenu
#print axioms upperMenu

end OrderedLanding
