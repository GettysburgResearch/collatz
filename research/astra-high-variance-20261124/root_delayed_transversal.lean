import Std

set_option autoImplicit false

namespace Collatz.DelayedTransversal

/-- Iteration, with the clock as its first explicit argument. -/
def run {α : Type} (f : α → α) : Nat → α → α
  | 0, x => x
  | n + 1, x => run f n (f x)

theorem run_add {α : Type} (f : α → α) (m n : Nat) (x : α) :
    run f (m + n) x = run f n (run f m x) := by
  induction m generalizing x with
  | zero => simp [run]
  | succ m ih => simpa only [Nat.succ_add, run] using ih (f x)

theorem run_commute {α : Type} (f : α → α) (m n : Nat) (x : α) :
    run f m (run f n x) = run f n (run f m x) := by
  rw [← run_add, ← run_add, Nat.add_comm n m]

/-- An endpoint equality stays valid at any larger common clock. -/
theorem same_clock_persists {α : Type} (f : α → α) (x y : α)
    (r s : Nat) (h : run f r x = run f r y) :
    run f (r + s) x = run f (r + s) y := by
  simp only [run_add, h]

/-- Equal-clock comparisons compose at the larger horizon, not their sum. -/
theorem same_clock_max {α : Type} (f : α → α) (x y z : α)
    (r s : Nat) (hxy : run f r x = run f r y)
    (hyz : run f s y = run f s z) :
    run f (max r s) x = run f (max r s) z := by
  have h1 := same_clock_persists f x y r (max r s - r) hxy
  have h2 := same_clock_persists f y z s (max r s - s) hyz
  have hr : r + (max r s - r) = max r s := by omega
  have hs : s + (max r s - s) = max r s := by omega
  rw [hr] at h1
  rw [hs] at h2
  exact h1.trans h2

/-- Every replacement point carries its original ordinary time.  Different
time tags cannot collide at any common future clock, even when the two
replacement endpoints have different settlement delays. -/
theorem tagged_transversal {α : Type} (f : α → α) (q : Nat → α)
    (advance : ∀ t r, run f r (q t) = q (t + r))
    (qinj : ∀ i j, q i = q j → i = j)
    (x y : α) (t u a b h k future : Nat)
    (hx : run f a x = q (t + a))
    (hy : run f b y = q (u + b))
    (different : t + h ≠ u + k) :
    run f future (run f h x) ≠ run f future (run f k y) := by
  intro collision
  have push := congrArg (run f (a + b)) collision
  have left : run f (a + b) (run f future (run f h x)) =
      q (t + a + (h + future + b)) := by
    calc
      run f (a + b) (run f future (run f h x)) =
          run f (h + future + (a + b)) x := by
            rw [← run_add, ← run_add, Nat.add_assoc]
      _ = run f (a + (h + future + b)) x := by congr 1; omega
      _ = run f (h + future + b) (run f a x) := run_add f a _ x
      _ = q (t + a + (h + future + b)) := by rw [hx, advance]
  have right : run f (a + b) (run f future (run f k y)) =
      q (u + b + (k + future + a)) := by
    calc
      run f (a + b) (run f future (run f k y)) =
          run f (k + future + (a + b)) y := by
            rw [← run_add, ← run_add, Nat.add_assoc]
      _ = run f (b + (k + future + a)) y := by congr 1; omega
      _ = run f (k + future + a) (run f b y) := run_add f b _ y
      _ = q (u + b + (k + future + a)) := by rw [hy, advance]
  rw [left, right] at push
  have clocks := qinj _ _ push
  exact different (by omega)

/-- A state represented after a positive physical delay advances along the
same underlying orbit. This is the finite simulation identity used at each
step of the residual return construction. -/
theorem settled_advance {α : Type} (f : α → α) (source replacement : α)
    (search delay : Nat)
    (meeting : run f delay replacement = run f delay (run f search source)) :
    run f delay replacement = run f (search + delay) source := by
  rw [run_add]
  exact meeting

#print axioms same_clock_max
#print axioms tagged_transversal
#print axioms settled_advance

end Collatz.DelayedTransversal
