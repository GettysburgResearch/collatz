import Std

set_option autoImplicit false
namespace Collatz.CentralClosure

def stepN (f : Nat → Nat) : Nat → Nat → Nat
  | 0, n => n
  | k+1, n => stepN f k (f n)

private theorem stepAdd (f : Nat → Nat) (i j n : Nat) :
    stepN f (i+j) n = stepN f j (stepN f i n) := by
  induction i generalizing n with
  | zero => simp [stepN]
  | succ i ih => simpa [Nat.succ_add, stepN] using ih (f n)

private theorem fixedOne (f : Nat → Nat) (h : f 1 = 1) (i : Nat) :
    stepN f i 1 = 1 := by
  induction i with
  | zero => rfl
  | succ i ih => simpa only [stepN, h] using ih

def converges (f : Nat → Nat) (n : Nat) : Prop := ∃ k, stepN f k n = 1

/-- The smaller source may meet at a different odd clock. The sufficient
    premise is needed only under the actual strong-induction hypothesis. -/
theorem universal_iff_floor_meeting (f : Nat → Nat) (h : f 1 = 1) :
    (∀ n, n % 2 = 1 → converges f n) ↔
    (∀ n, n % 2 = 1 → 1 < n →
      (∀ m, m < n → m % 2 = 1 → converges f m) →
      ∃ m, m < n ∧ m % 2 = 1 ∧ ∃ a b, stepN f a n = stepN f b m) := by
  constructor
  · intro all n odd big _
    obtain ⟨k,hk⟩ := all n odd
    exact ⟨1,big,rfl,k,0,hk⟩
  · intro bridge n
    induction n using Nat.strongRecOn with
    | ind n ih =>
      intro odd
      by_cases hone : n = 1
      · exact ⟨0,hone⟩
      · have big : 1 < n := by omega
        obtain ⟨m,lt,om,a,b,eq⟩ := bridge n odd big ih
        obtain ⟨k,hk⟩ := ih m lt om
        refine ⟨a+k, ?_⟩
        rw [stepAdd, eq, ←stepAdd, Nat.add_comm b k, stepAdd, hk, fixedOne f h]

/-- An endpoint lift by twice the ternary modulus corresponds to exactly
    one full odd-source cylinder lift, preserving the cleared carry. -/
theorem paired_lift (P Q x y c k : Nat) (h : P*y = Q*x+c) :
    P*(y+2*Q*k) = Q*(x+2*P*k)+c := by
  grind

#print axioms universal_iff_floor_meeting
#print axioms paired_lift
end Collatz.CentralClosure
