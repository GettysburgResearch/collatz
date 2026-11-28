import Lean.Elab.Tactic.Omega

namespace CollatzResearch.UpDownRayBand

def up (x : Nat) : Nat := (3*x+1)/2
def down (x : Nat) : Nat := (x+1)/2

def upIter (m : Nat) : Nat → Nat
  | 0 => m
  | j+1 => up (upIter m j)

private theorem up_injective {a b : Nat} (h : up a = up b) : a = b := by
  unfold up at h
  omega

private theorem iter_ge (m j : Nat) : m ≤ upIter m j := by
  induction j with
  | zero => exact Nat.le_refl _
  | succ j ih =>
    change m ≤ (3*upIter m j + 1)/2
    omega

def inBand (m z : Nat) : Prop :=
  m < z ∧ z < 3*m ∧ z ≠ 2*m ∧ ∀ j, z ≠ upIter m j

def choose (m z : Nat) : Nat := if z < 2*m then up z else down z

/-- Every marker band contains the explicitly given initial state. -/
theorem bandStart (m : Nat) (hr : m%6 = 5) : inBand m (m+1) := by
  have hm : 5 ≤ m := by omega
  refine ⟨by omega, by omega, by omega, ?_⟩
  intro j
  cases j with
  | zero => simp [upIter]
  | succ j =>
    have h := iter_ge m j
    change m+1 ≠ (3 * upIter m j + 1)/2
    omega

/-- The explicit local up/down selector preserves the finite band with its
upward ray and the exceptional midpoint removed. -/
theorem bandClosed (m z : Nat) (hr : m%6 = 5) (hz : inBand m z) :
    inBand m (choose m z) := by
  obtain ⟨hlo,hhi,hmid,hchain⟩ := hz
  by_cases h : z < 2*m
  · simp only [choose, ite_eq_left h]
    refine ⟨?_, ?_, ?_, ?_⟩
    · unfold up; omega
    · unfold up; omega
    · unfold up; omega
    · intro j
      cases j with
      | zero => change (3*z+1)/2 ≠ m; omega
      | succ j =>
        change up z ≠ up (upIter m j)
        exact fun eq => hchain j (up_injective eq)
  · simp only [choose, ite_eq_right h]
    refine ⟨?_, ?_, ?_, ?_⟩
    · unfold down; omega
    · unfold down; omega
    · unfold down; omega
    · intro j
      cases j with
      | zero => change (z+1)/2 ≠ m; omega
      | succ j =>
        have hge := iter_ge m j
        change (z+1)/2 ≠ (3*upIter m j+1)/2
        omega

/-- States and affine coefficients for initial values r + 128q. -/
def rows (r b : Nat) : List Bool → List (Nat × Nat)
  | [] => [(r,b)]
  | u :: w => (r,b) :: rows (if u then up r else down r)
      (if u then 3*b/2 else b/2) w

def scripts : List (List Bool) := [
  [true], [true,true,true], [false,true,true], [true,false,true,true],
  [true,true,true,true,true], [false,true,true,true,true],
  [false,true,true,false,true,true], [true,true,false,true,true],
  [true,true,true,false,true,true], [true,true,true,true,true,true]]

def certifies (r : Nat) (w : List Bool) : Bool :=
  let xs := rows r 128 w
  let last := xs.getLastD (0,0)
  last.1 % 6 == 5 && last.2 % 6 == 0 &&
    xs.dropLast.all (fun x => x.2 % 2 == 0 && x.1 < last.1 && x.2 < last.2)

set_option maxRecDepth 10000 in
set_option maxHeartbeats 5000000 in
theorem residueScripts : ∀ i : Fin 64, scripts.any (certifies (2*i.val+1)) = true := by decide

end CollatzResearch.UpDownRayBand
