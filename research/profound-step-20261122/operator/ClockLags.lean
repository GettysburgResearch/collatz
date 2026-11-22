module

public import ShellCover

@[expose] public section

/-!
# Exact clock lags in an ordinary merger component

These abstract finite-clock facts apply to the actual ordinary map.  They
do not assert existence of a merger or of an escaping Collatz component.
The accompanying Hilbert-space classification is a written theorem.
-/

namespace CollatzShell.ClockLags

variable {X : Type*} (f : X → X)

/-- Two actual trajectories meet after possibly different finite clocks. -/
def Meets (x y : X) : Prop := ∃ i j : Nat, f^[i] x = f^[j] y

/-- Two actual trajectories meet at the same finite clock. -/
def Synchronous (x y : X) : Prop := ∃ k : Nat, f^[k] x = f^[k] y

/-- The signed clock displacement relative to the second source. -/
def HasLag (x y : X) (d : Int) : Prop :=
  ∃ i j : Nat, f^[i] x = f^[j] y ∧ (j : Int) - i = d

theorem lag_refl (x : X) : HasLag f x x 0 := by
  exact ⟨0, 0, rfl, by omega⟩

theorem lag_symm {x y : X} {d : Int} (h : HasLag f x y d) :
    HasLag f y x (-d) := by
  obtain ⟨i, j, hij, hd⟩ := h
  exact ⟨j, i, hij.symm, by omega⟩

theorem lag_trans {x y z : X} {d e : Int}
    (hxy : HasLag f x y d) (hyz : HasLag f y z e) :
    HasLag f x z (d + e) := by
  obtain ⟨i, j, hij, hd⟩ := hxy
  obtain ⟨k, l, hkl, he⟩ := hyz
  refine ⟨k + i, j + l, ?_, ?_⟩
  · calc
      f^[k+i] x = f^[k] (f^[i] x) := Function.iterate_add_apply _ _ _ _
      _ = f^[k] (f^[j] y) := congrArg (f^[k]) hij
      _ = f^[j] (f^[k] y) := by simp only [← Function.iterate_add_apply, Nat.add_comm]
      _ = f^[j] (f^[l] z) := congrArg (f^[j]) hkl
      _ = f^[j+l] z := (Function.iterate_add_apply _ _ _ _).symm
  · push_cast
    omega

/-- The lag is unique when the reference source has no repeated forward state. -/
theorem lag_unique {x y : X} {d e : Int}
    (hy : Function.Injective (fun k : Nat => f^[k] y))
    (hd : HasLag f x y d) (he : HasLag f x y e) : d = e := by
  obtain ⟨i, j, hij, hd⟩ := hd
  obtain ⟨k, l, hkl, he⟩ := he
  have h : f^[k+j] y = f^[i+l] y := by
    calc
      f^[k+j] y = f^[k] (f^[j] y) := Function.iterate_add_apply _ _ _ _
      _ = f^[k] (f^[i] x) := congrArg (f^[k]) hij.symm
      _ = f^[i] (f^[k] x) := by simp only [← Function.iterate_add_apply, Nat.add_comm]
      _ = f^[i] (f^[l] y) := congrArg (f^[i]) hkl
      _ = f^[i+l] y := (Function.iterate_add_apply _ _ _ _).symm
  have hc := hy h
  omega

theorem meets_iff_hasLag (x y : X) :
    Meets f x y ↔ ∃ d : Int, HasLag f x y d := by
  constructor
  · rintro ⟨i, j, h⟩
    exact ⟨(j : Int) - i, i, j, h, rfl⟩
  · rintro ⟨d, i, j, h, _⟩
    exact ⟨i, j, h⟩

theorem synchronous_iff_zero_lag (x y : X) :
    Synchronous f x y ↔ HasLag f x y 0 := by
  constructor
  · rintro ⟨k, h⟩
    exact ⟨k, k, h, by omega⟩
  · rintro ⟨i, j, h, hd⟩
    have : i = j := by omega
    subst j
    exact ⟨i, h⟩

/-- A genuine forward step raises the coordinate by exactly one. -/
theorem lag_step {x y : X} {d : Int} (h : HasLag f x y d) :
    HasLag f (f x) y (d + 1) := by
  obtain ⟨i, j, hij, hd⟩ := h
  refine ⟨i, j+1, ?_, ?_⟩
  · calc
      f^[i] (f x) = f (f^[i] x) := by
        rw [← Function.iterate_succ_apply, Function.iterate_succ_apply']
      _ = f (f^[j] y) := congrArg f hij
      _ = f^[j+1] y := (Function.iterate_succ_apply' _ _ _).symm
  · push_cast
    omega

/-- Equal coordinates give an actual synchronous merger, without a limit argument. -/
theorem same_lag_synchronous {x y z : X} {d : Int}
    (hx : HasLag f x z d) (hy : HasLag f y z d) : Synchronous f x y := by
  apply (synchronous_iff_zero_lag f x y).mpr
  simpa using lag_trans f hx (lag_symm f hy)

/-- Once a meeting is known, every later reference clock gives the same front. -/
theorem extend_meeting {x y : X} {i j : Nat}
    (h : f^[i] x = f^[j] y) (k : Nat) :
    f^[k+i] x = f^[k+j] y := by
  simpa only [Function.iterate_add_apply] using congrArg (f^[k]) h

/-- The front sets of a fixed lag increase as the reference ray advances. -/
theorem front_increasing {x y : X} (a b : Nat)
    (h : f^[a] x = f^[b] y) : f^[a+1] x = f^[b+1] y := by
  simpa only [Function.iterate_succ_apply'] using congrArg f h

end CollatzShell.ClockLags
