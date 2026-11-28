import Std

/-! Removing the unique primitive terminal lap from a joint grade/native-clock row. -/

namespace FirstArrivalLap

def walk {α : Type} (step : α → α) : Nat → α → α
  | 0, x => x
  | n+1, x => step (walk step n x)

def nativeClock {α : Type} (step : α → α) (gap : α → Nat) : Nat → α → Nat
  | 0, _ => 0
  | n+1, x => nativeClock step gap n x + gap (walk step n x)

theorem walk_add {α : Type} (step : α → α) (i j : Nat) (x : α) :
    walk step (i+j) x = walk step j (walk step i x) := by
  induction j with
  | zero => rfl
  | succ j ih =>
      change step (walk step (i+j) x) = step (walk step j (walk step i x))
      rw [ih]

theorem nativeClock_add {α : Type} (step : α → α) (gap : α → Nat)
    (i j : Nat) (x : α) :
    nativeClock step gap (i+j) x =
      nativeClock step gap i x + nativeClock step gap j (walk step i x) := by
  induction j with
  | zero => rfl
  | succ j ih =>
      change nativeClock step gap (i+j) x + gap (walk step (i+j) x) =
        nativeClock step gap i x +
          (nativeClock step gap j (walk step i x) + gap (walk step j (walk step i x)))
      rw [ih, walk_add, Nat.add_assoc]

def PrimitiveLap {α : Type} (step : α → α) (y : α) (lap : Nat) : Prop :=
  0 < lap ∧ walk step lap y = y ∧
    ∀ t, 0 < t → walk step t y = y → lap ≤ t

def Raw {α : Type} (step : α → α) (gap : α → Nat)
    (x y : α) (n s : Nat) : Prop :=
  walk step n x = y ∧ nativeClock step gap n x = s

def Earlier {α : Type} (step : α → α) (x y : α) (n : Nat) : Prop :=
  ∃ j, j < n ∧ walk step j x = y

theorem predecessor_at_lap {α : Type} {step : α → α} {x y : α} {lap k : Nat}
    (hl : PrimitiveLap step y lap) (h : walk step (k+lap) x = y)
    (he : Earlier step x y (k+lap)) : walk step k x = y := by
  obtain ⟨j, hj, hy⟩ := he
  have decomp : j + (k+lap-j) = k+lap := by omega
  have hret : walk step (k+lap-j) y = y := by
    have ht := walk_add step j (k+lap-j) x
    rw [decomp, hy, h] at ht
    exact ht.symm
  have hmin := hl.2.2 (k+lap-j) (by omega) hret
  have dj : j + (k-j) = k := by omega
  have dl : lap + (k-j) = k+lap-j := by omega
  have last := walk_add step lap (k-j) y
  rw [dl, hl.2.1, hret] at last
  have first := walk_add step j (k-j) x
  rw [dj, hy] at first
  exact first.trans last.symm

theorem rejected_iff_shorter {α : Type} {step : α → α} (gap : α → Nat)
    {x y : α} {lap : Nat} (k s : Nat) (hl : PrimitiveLap step y lap) :
    Raw step gap x y (k+lap) s ∧ Earlier step x y (k+lap) ↔
      ∃ u, Raw step gap x y k u ∧ s = u + nativeClock step gap lap y := by
  constructor
  · rintro ⟨⟨hend, hclock⟩, he⟩
    have hk := predecessor_at_lap hl hend he
    refine ⟨nativeClock step gap k x, ⟨hk,rfl⟩, ?_⟩
    rw [← hclock, nativeClock_add, hk]
  · rintro ⟨u, ⟨hk, hu⟩, hs⟩
    constructor
    · constructor
      · rw [walk_add, hk, hl.2.1]
      · rw [nativeClock_add, hk, hu, hs]
    · exact ⟨k, by have := hl.1; omega, hk⟩

theorem no_earlier_below_lap {α : Type} {step : α → α} {x y : α} {lap n : Nat}
    (hl : PrimitiveLap step y lap) (hn : n < lap) (h : walk step n x = y) :
    ¬ Earlier step x y n := by
  rintro ⟨j, hj, hjy⟩
  have hsum : j + (n-j) = n := by omega
  have ht := walk_add step j (n-j) x
  rw [hsum, h, hjy] at ht
  have := hl.2.2 (n-j) (by omega) ht.symm
  omega

#print axioms rejected_iff_shorter
#print axioms no_earlier_below_lap

end FirstArrivalLap
