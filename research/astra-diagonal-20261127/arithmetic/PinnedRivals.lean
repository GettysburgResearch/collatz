import Mathlib.Data.Int.ModEq
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum
import Mathlib.RingTheory.Coprime.Basic

namespace Collatz.Diagonal.PinnedRivals

/-- The affine form of an odd inverse competitor, with dyadic denominators cleared. -/
theorem transport {Q P P' c c' a b x u y : ℤ}
    (hrel : Q*y = P*x+c) (hnative : a*x = 3*u+1)
    (hscale : b*P = a*P') (hcarry : 3*c' = b*c+P'-Q) :
    Q*(b*y-1) = 3*(P'*u+c') := by
  calc
    Q*(b*y-1) = b*(Q*y)-Q := by ring
    _ = (b*P)*x+b*c-Q := by rw [hrel]; ring
    _ = P'*(a*x)+b*c-Q := by rw [hscale]; ring
    _ = 3*(P'*u+c') := by rw [hnative]; linarith only [hcarry]

/-- Every integral carry gives an actual positive integral reverse edge. -/
theorem actual_parent {Q P P' c c' a b x u y : ℤ}
    (hQ : IsCoprime Q 3) (hy : 0 < y) (hb : 2 ≤ b)
    (hrel : Q*y = P*x+c) (hnative : a*x = 3*u+1)
    (hscale : b*P = a*P') (hcarry : 3*c' = b*c+P'-Q) :
    ∃ v : ℤ, 0 < v ∧ b*y = 3*v+1 ∧ Q*v=P'*u+c' := by
  have h := transport hrel hnative hscale hcarry
  obtain ⟨i,j,hbez⟩ := hQ
  have hdiv : 3 ∣ b*y-1 := by
    refine ⟨i*(P'*u+c')+j*(b*y-1), ?_⟩
    calc
      b*y-1 = (i*Q+j*3)*(b*y-1) := by rw [hbez]; ring
      _ = i*(Q*(b*y-1))+3*(j*(b*y-1)) := by ring
      _ = _ := by rw [h]; ring
  obtain ⟨v,hv⟩ := hdiv
  have hpos : 0 < b*y-1 := by nlinarith [mul_nonneg (sub_nonneg.mpr hb) (le_of_lt hy)]
  refine ⟨v, by omega, by omega, ?_⟩
  rw [hv] at h
  linarith only [show 3*(Q*v)=3*(P'*u+c') by calc
    3*(Q*v) = Q*(3*v) := by ring
    _ = _ := h]

/-- A ternary-dead competitor is an actual multiple of three. -/
theorem triple_test {Q P c a x u y : ℤ}
    (hunit : IsCoprime (a*Q) 3)
    (hrel : Q*y=P*x+c) (hnative : a*x=3*u+1) :
    3 ∣ y ↔ 3 ∣ P+a*c := by
  have h : (a*Q)*y = 3*(P*u)+(P+a*c) := by
    calc
      (a*Q)*y = a*(Q*y) := by ring
      _ = P*(a*x)+a*c := by rw [hrel]; ring
      _ = _ := by rw [hnative]; ring
  constructor
  · rintro ⟨k,hk⟩
    refine ⟨(a*Q)*k-P*u, ?_⟩
    rw [hk] at h
    linarith only [show 3*((a*Q)*k)=3*(P*u)+(P+a*c) by calc
      3*((a*Q)*k) = (a*Q)*(3*k) := by ring
      _ = _ := h]
  · rintro ⟨k,hk⟩
    obtain ⟨i,j,hbez⟩ := hunit
    refine ⟨i*(P*u+k)+j*y, ?_⟩
    calc
      y = (i*(a*Q)+j*3)*y := by rw [hbez]; ring
      _ = i*((a*Q)*y)+3*(j*y) := by ring
      _ = _ := by rw [h,hk]; ring

/-- A transition to an actual multiple under the second physical floor. -/
theorem empty_under_triple_floor {bad : ℤ → Prop} {s y : ℤ}
    (hfloor : ∀ z, bad z → 3 ∣ z → 2*s+1 ≤ z)
    (hbad : bad y) (htri : 3 ∣ y) (hbelow : y ≤ 2*s) : False := by
  have := hfloor y hbad htri
  omega

/-- One ordinary shortcut, with the odd output halved once. -/
def shortcut (n : ℕ) : ℕ :=
  if n%2=0 then n/2 else (3*n+1)/2

def go : ℕ → ℕ → ℕ
  | 0, n => n
  | t+1, n => go t (shortcut n)

def eval (s : ℕ × ℕ) (t : ℕ) : ℕ := s.1*t+s.2

/-- A simultaneous trajectory for every member of one arithmetic progression. -/
def replay : ℕ → ℕ × ℕ → Option (ℕ × ℕ)
  | 0, s => some s
  | k+1, (u,c) => if u%2=0 then
      replay k ((if c%2=0 then u/2 else 3*(u/2)), shortcut c)
    else none

private theorem shortcut_lift (u c t : ℕ) (hu : u%2=0) :
    shortcut (u*t+c) = (if c%2=0 then u/2 else 3*(u/2))*t+shortcut c := by
  let z := (u/2)*t
  have h : u*t = 2*z := by
    have he : u=2*(u/2) := by omega
    calc u*t = (2*(u/2))*t := congrArg (·*t) he
         _ = 2*z := by dsimp [z]; ring
  rw [h]
  split <;> rename_i hc
  · simp [shortcut, Nat.add_mod, hc]
    omega
  · have hc' : c%2=1 := by omega
    simp [shortcut, Nat.add_mod, hc']
    have he : (3*(u/2))*t = 3*z := by dsimp [z]; ring
    rw [he]
    omega

theorem replay_sound {k : ℕ} {s out : ℕ × ℕ} (hr : replay k s=some out) (n : ℕ) :
    go k (eval s n)=eval out n := by
  induction k generalizing s with
  | zero =>
    simp [replay] at hr
    simp [go,hr]
  | succ k ih =>
    obtain ⟨u,c⟩ := s
    by_cases hu : u%2=0
    · simp [replay,hu] at hr
      simp only [eval,go,shortcut_lift u c n hu]
      exact ih hr
    · simp [replay,hu] at hr

/-- The two true ordinary arms meet at the same clock for every parameter. -/
theorem upper_neighbor_cylinder (n : ℕ) :
    go 30 (1073741824*n+613089275) =
      go 30 (1073741824*n+613089276) := by
  have h₁ := replay_sound
    (s := (1073741824, 613089275)) (k := 30)
    (out := (1162261467, 663632570)) (by decide) n
  have h₂ := replay_sound
    (s := (1073741824, 613089276)) (k := 30)
    (out := (1162261467, 663632570)) (by decide) n
  exact h₁.trans h₂.symm

/-- Equal-odd-count rivals with shift four merge, including every third residue. -/
theorem shift_four_cylinder (n : ℕ) :
    go 27 (268435456*n+260560107) =
      go 27 (268435456*n+260560111) := by
  have h₁ := replay_sound
    (s := (268435456, 260560107)) (k := 27)
    (out := (258280326, 250702913)) (by decide) n
  have h₂ := replay_sound
    (s := (268435456, 260560111)) (k := 27)
    (out := (258280326, 250702913)) (by decide) n
  exact h₁.trans h₂.symm

/-- Different clocks lead to one ordinary state from heights x and (x-1)/8. -/
theorem one_eighth_cylinder (n : ℕ) :
    go 32 (8589934592*n+7975731193) =
      go 29 (1073741824*n+996966399) := by
  have h₁ := replay_sound
    (s := (8589934592, 7975731193)) (k := 32)
    (out := (6973568802, 6474939905)) (by decide) n
  have h₂ := replay_sound
    (s := (1073741824, 996966399)) (k := 29)
    (out := (6973568802, 6474939905)) (by decide) n
  exact h₁.trans h₂.symm

end Collatz.Diagonal.PinnedRivals
