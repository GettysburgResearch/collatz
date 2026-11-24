import Std

namespace Collatz.OrdinaryShadow

def step (n : Nat) : Nat :=
  if n % 2 = 0 then n / 2 else (3*n+1)/2

def iter (k n : Nat) : Nat := Nat.rec n (fun _ a => step a) k

private theorem iter_add (a b n : Nat) :
    iter (a+b) n = iter b (iter a n) := by
  induction b with
  | zero => rfl
  | succ b ih => exact congrArg step ih

private theorem closed (k n : Nat) (h : n=1 ∨ n=2) :
    iter k n=1 ∨ iter k n=2 := by
  induction k with
  | zero => exact h
  | succ k ih =>
    change step (iter k n)=1 ∨ step (iter k n)=2
    rcases ih with h | h <;> rw [h] <;> decide

def lowEdge (q r : Nat) : Prop := 8*r=9*q+7 ∨ 32*r=9*q+5

def shadow (q : Nat) := (60*q+5)/83

private theorem propagates (q r : Nat) (h : lowEdge q r) (hdiv : (q+7)%83=0) :
    (r+7)%83=0 := by
  rcases h with h|h <;> omega

private theorem exact_shadow (q : Nat) (hdiv : (q+7)%83=0) :
    83*shadow q = 60*q+5 ∧ shadow q % 2=1 := by
  unfold shadow
  omega

private theorem block (y z : Nat) (hy : y%2=1) (hz : z%2=1)
    (edge : 8*z=9*y+5 ∨ 32*z=9*y+5) :
    y%4=3 ∧ ∃ k : Nat, 1 ≤ k ∧ iter k y=z := by
  rcases edge with h|h
  · refine ⟨by omega, 3, by decide, ?_⟩
    change step (step (step y)) = z
    unfold step
    repeat' first | split | omega
  · refine ⟨by omega, 5, by decide, ?_⟩
    have hy' : step y = (3*y+1)/2 := by simp [step, show y%2≠0 by omega]
    have hm : step ((3*y+1)/2)=8*z := by
      simp [step, show ((3*y+1)/2)%2≠0 by omega]
      omega
    have halve (n : Nat) : step (2*n)=n := by simp [step]
    change step (step (step (step (step y)))) = z
    rw [hy', hm, show 8*z=2*(4*z) by omega, halve,
      show 4*z=2*(2*z) by omega, halve, halve]

/-- A single infinite ordinary L/P path meeting the divisible residue supplies a
strictly smaller positive ordinary source whose shortcut trajectory never hits 1. -/
theorem smaller_nonconverger (q : Nat → Nat)
    (edges : ∀ j, lowEdge (q j) (q (j+1))) (hdiv : (q 0+7)%83=0) :
    0 < shadow (q 0) ∧ 4*shadow (q 0)<3*q 0+1 ∧
      ∀ t, iter t (shadow (q 0)) ≠ 1 := by
  have divs (j : Nat) : (q j+7)%83=0 := by
    induction j with
    | zero => exact hdiv
    | succ j ih => exact propagates _ _ (edges j) ih
  have blocks (j : Nat) : shadow (q j)%4=3 ∧
      ∃ k : Nat, 1 ≤ k ∧ iter k (shadow (q j))=shadow (q (j+1)) := by
    obtain ⟨a,ha⟩ := exact_shadow _ (divs j)
    obtain ⟨b,hb⟩ := exact_shadow _ (divs (j+1))
    apply block _ _ ha hb
    rcases edges j with h|h
    · left; omega
    · right; omega
  have visits (j : Nat) : ∃ k : Nat, j ≤ k ∧
      iter k (shadow (q 0))=shadow (q j) := by
    induction j with
    | zero => exact ⟨0, Nat.le_refl _, rfl⟩
    | succ j ih =>
      obtain ⟨k,hk,he⟩ := ih
      obtain ⟨d,hd,hdest⟩ := (blocks j).2
      exact ⟨k+d, by omega, by rw [iter_add,he,hdest]⟩
  obtain ⟨a,ha⟩ := exact_shadow _ hdiv
  refine ⟨by omega, by omega, ?_⟩
  intro t hit
  obtain ⟨k,hk,he⟩ := visits t
  have hk' : k=t+(k-t) := by omega
  rw [hk', iter_add, hit] at he
  have hc := closed (k-t) 1 (Or.inl rfl)
  have hm := (blocks t).1
  omega

#print axioms smaller_nonconverger
end Collatz.OrdinaryShadow
