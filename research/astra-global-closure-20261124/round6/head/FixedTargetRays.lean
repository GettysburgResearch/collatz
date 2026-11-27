import Mathlib.Tactic.Ring

namespace FixedTargetRays

def T (n : Nat) : Nat := if n % 2 = 0 then n / 2 else (3*n+1)/2

def iter {α : Type*} (f : α → α) : Nat → α → α
  | 0, x => x
  | n+1, x => iter f n (f x)

private theorem append {α : Type*} (f : α → α) (m : Nat) (x : α) :
    iter f (m+1) x = f (iter f m x) := by
  induction m generalizing x with
  | zero => rfl
  | succ m ih => exact ih (f x)

private theorem evenStep (n : Nat) : T (2*n) = n := by
  unfold T
  split <;> omega

private theorem twoSteps (n : Nat) : T (T (4*n+2)) = 3*n+2 := by
  unfold T
  split <;> split <;> omega

theorem halvingRun (m a : Nat) : iter T m (2^m*a) = a := by
  induction m with
  | zero => simp [iter]
  | succ m ih =>
    rw [show 2^(m+1)*a = 2*(2^m*a) by ring]
    change iter T m (T (2*(2^m*a))) = a
    rw [evenStep, ih]

theorem oddRun (m n a : Nat) (hn : n+1 = 2^m*a) :
    iter T m n + 1 = 3^m*a := by
  induction m generalizing n a with
  | zero => simpa [iter] using hn
  | succ m ih =>
    have h : n+1 = 2*(2^m*a) := by rw [hn]; ring
    have step : T n+1 = 3*(2^m*a) := by unfold T; split <;> omega
    change iter T m (T n)+1 = 3^(m+1)*a
    have he : T n+1 = 2^m*(3*a) := by rw [step]; ring
    rw [ih (T n) (3*a) he]
    ring

theorem evenPairs (j b : Nat) : iter T (2*j) (4^j*b+2) = 3^j*b+2 := by
  induction j generalizing b with
  | zero => simp [iter]
  | succ j ih =>
    rw [show 2*(j+1) = 2*j+1+1 by omega,
        show 4^(j+1)*b+2 = 4*(4^j*b)+2 by ring]
    change iter T (2*j) (T (T (4*(4^j*b)+2))) = 3^(j+1)*b+2
    rw [twoSteps, show 3*(4^j*b)+2 = 4^j*(3*b)+2 by ring, ih]
    ring

theorem evenPairsPlusOne (j b : Nat) :
    iter T (2*j+1) (4^j*(2*b)+2) = 3^j*b+1 := by
  rw [append, evenPairs, show 3^j*(2*b)+2 = 2*(3^j*b+1) by ring, evenStep]

theorem oddEndpoints (m v a : Nat) (hm : 0<m) (hv : v%2=1)
    (hs : 3*v+1=2^m*a) :
    iter T m v = a ∧ iter T m (9*v+2)+1 = 3^(m+1)*a := by
  constructor
  · cases m with
    | zero => omega
    | succ k =>
      have h : 3*v+1 = 2*(2^k*a) := by rw [hs]; ring
      have step : T v = 2^k*a := by unfold T; split <;> omega
      change iter T k (T v) = a
      rw [step, halvingRun]
  · have he : (9*v+2)+1 = 2^m*(3*a) := by
      calc (9*v+2)+1 = 3*(3*v+1) := by ring
           _ = _ := by rw [hs]; ring
    rw [oddRun m (9*v+2) (3*a) he]
    ring

theorem originalArms (v : Nat) : iter T 2 (4*v)=v ∧ iter T 3 (8*v+1)=9*v+2 := by
  simp only [iter, T]
  constructor
  · split <;> split <;> omega
  · split <;> split <;> split <;> omega

theorem inverseRescue (r q : Nat) (h : 16*r = 3^15*q+1) :
    iter T 15 (2^15*q-1) = 2*(8*r-1) ∧ 22*(2^15*q-1)<r := by
  have he : (2^15*q-1)+1 = 2^15*q := by omega
  have step := oddRun 15 (2^15*q-1) q he
  constructor <;> omega

theorem smallOfFirstFailure (P G : Nat → Prop) (r : Nat)
    (one : P 1) (good : ∀ s, s<r → G s)
    (route : ∀ n, 1<n → (∀ z, 0<z → z<n → P z) →
                   (∀ s, s<22*n → G s) → P n)
    (n : Nat) (pos : 0<n) (small : 22*n<r) : P n := by
  induction n using Nat.strong_induction_on with
  | h n ih =>
    by_cases base : n=1
    · simpa [base] using one
    · apply route n (by omega)
      · intro z hz hzn
        exact ih z hzn hz (by omega)
      · intro s hs
        exact good s (by omega)

def Hits {α : Type*} (f : α → α) (x z : α) : Prop := ∃ i, iter f i x = z

private theorem hitsStep {α : Type*} (f : α → α) (x z : α) (hx : x ≠ z) :
    Hits f x z ↔ Hits f (f x) z := by
  constructor
  · rintro ⟨i, hi⟩
    cases i with
    | zero => exact (hx hi).elim
    | succ i => exact ⟨i, hi⟩
  · rintro ⟨i, hi⟩
    exact ⟨i+1, hi⟩

inductive Avoiding {α : Type*} (f : α → α) (z : α) : α → α → Prop
  | nil (x) (hx : x ≠ z) : Avoiding f z x x
  | cons {x y b} (hx : x ≠ z) (hy : y ≠ z) (edge : f x=y ∨ f y=x)
            (rest : Avoiding f z y b) : Avoiding f z x b

theorem cut {α : Type*} {f : α → α} {z x y : α}
    (path : Avoiding f z x y) : Hits f x z ↔ Hits f y z := by
  induction path with
  | nil => rfl
  | cons hx hy edge _ ih =>
    apply Iff.trans _ ih
    rcases edge with eq | eq
    · simpa [← eq] using hitsStep f _ _ hx
    · simpa [← eq] using (hitsStep f _ _ hy).symm

theorem forcedPeak (v m a z : Nat) (hs : 3*v+1=2^m*a)
    (hm : 0<m) (hv : v%2=1) (hz : z+1=3^(m+1)*a)
    (bound : ∀ i, iter T i (4*v) ≤ 4*v) (large : 4*v<z) :
    ¬ Avoiding T z (8*v+1) (4*v) := by
  intro path
  have hit : Hits T (8*v+1) z := by
    refine ⟨m+3, ?_⟩
    change iter T m (iter T 3 (8*v+1)) = z
    rw [(originalArms v).2]
    have tail := (oddEndpoints m v a hm hv hs).2
    omega
  obtain ⟨i, hi⟩ := (cut path).mp hit
  have := bound i
  omega

#print axioms oddRun
#print axioms halvingRun
#print axioms evenPairs
#print axioms evenPairsPlusOne
#print axioms oddEndpoints
#print axioms originalArms
#print axioms inverseRescue
#print axioms smallOfFirstFailure
#print axioms cut
#print axioms forcedPeak

end FixedTargetRays
