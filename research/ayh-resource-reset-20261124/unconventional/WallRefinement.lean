import Mathlib.Tactic.Ring
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.SplitIfs
import Mathlib.Tactic.Convert

/-! Adjacent cuts of an ordinary binary coloring of the shortcut Collatz graph.
    The source coloring need not be computable. -/
namespace WallRefinement

structure Coloring where
  color : Nat → Bool
  evenEq : ∀ n, color (2*n) = color n
  oddEq : ∀ n, color (2*n+1) = color (3*n+2)

def Mixed (c : Coloring) (n : Nat) : Prop := c.color n ≠ c.color (n+1)

/-- Subdivide an oriented edge. At a mixed edge exactly one child keeps both colors. -/
def child (c : Coloring) (n : Nat) : Nat :=
  if c.color (2*n+1) = c.color n then 2*n+1 else 2*n

theorem child_eq (c : Coloring) {n : Nat} (h : Mixed c n) :
    c.color (child c n) = c.color n ∧ c.color (child c n+1) = c.color (n+1) := by
  have hev : c.color (2*n+1+1) = c.color (n+1) := by
    simpa [Nat.mul_add] using c.evenEq (n+1)
  unfold child
  split_ifs with hm
  · exact ⟨hm, hev⟩
  · refine ⟨c.evenEq n, ?_⟩
    unfold Mixed at h
    cases h₁ : c.color n <;> cases h₂ : c.color (n+1) <;>
      cases h₃ : c.color (2*n+1) <;> simp_all

def index (c : Coloring) (n : Nat) : Nat → Nat
  | 0 => n
  | j+1 => child c (index c n j)

theorem index_eq (c : Coloring) {n : Nat} (h : Mixed c n) (j : Nat) :
    c.color (index c n j) = c.color n ∧ c.color (index c n j+1) = c.color (n+1) := by
  induction j with
  | zero => exact ⟨rfl, rfl⟩
  | succ j ih =>
    have live : Mixed c (index c n j) := by
      simpa [Mixed, ih.1, ih.2] using h
    obtain ⟨ha,hb⟩ := child_eq c live
    exact ⟨ha.trans ih.1,hb.trans ih.2⟩

theorem index_mixed (c : Coloring) {n : Nat} (h : Mixed c n) (j : Nat) :
    Mixed c (index c n j) := by
  obtain ⟨ha,hb⟩ := index_eq c h j
  simpa [Mixed,ha,hb] using h

/-- One free affine substitution in the signed adjacent difference. -/
theorem triple_four_edge (c : Coloring) (u : Nat) :
    (c.color (4*u+1),c.color (4*u+2)) = (c.color (3*u+1),c.color (3*u+2)) := by
  have h1 : c.color (4*u+1) = c.color (3*u+1) := by
    calc
      _ = c.color (2*(2*u)+1) := by congr 1; omega
      _ = c.color (3*(2*u)+2) := c.oddEq _
      _ = c.color (2*(3*u+1)) := by congr 1; omega
      _ = _ := c.evenEq _
  have h2 : c.color (4*u+2) = c.color (3*u+2) := by
    calc
      _ = c.color (2*(2*u+1)) := by congr 1; omega
      _ = c.color (2*u+1) := c.evenEq _
      _ = _ := c.oddEq _
  exact Prod.ext h1 h2

theorem ones (c : Coloring) (j u : Nat) (hu : 0 < u) :
    c.color (2^j*u-1) = c.color (3^j*u-1) := by
  induction j generalizing u with
  | zero => simp
  | succ j ih =>
    have hp : 0 < 2^j * u := Nat.mul_pos (by positivity) hu
    calc
      _ = c.color (2*(2^j*u-1)+1) := by
        have hex : 2^(j+1)*u = 2*(2^j*u) := by rw [pow_succ]; ring
        congr 1; omega
      _ = c.color (3*(2^j*u-1)+2) := c.oddEq _
      _ = c.color (2^j*(3*u)-1) := by congr 1; rw [show 2^j*(3*u) = 3*(2^j*u) by ring]; omega
      _ = c.color (3^j*(3*u)-1) := ih _ (by omega)
      _ = _ := by rw [pow_succ]; simp only [Nat.mul_assoc, Nat.mul_comm]

theorem even_pair (c : Coloring) (v : Nat) :
    c.color (4*v+2) = c.color (12*v+8) := by
  calc
    _ = c.color (2*(2*v+1)) := by congr 1; omega
    _ = c.color (2*v+1) := c.evenEq _
    _ = c.color (3*v+2) := c.oddEq _
    _ = c.color (2*(3*v+2)) := (c.evenEq _).symm
    _ = c.color (2*(2*(3*v+2))) := (c.evenEq _).symm
    _ = _ := by congr 1; omega

/-- If n+2=2^(s+1)u and 3^s u=3 mod 4, the two endpoints have the same color. -/
theorem run_fusion (c : Coloring) (n s u : Nat) (hu : 0 < u)
    (hn : n+2 = 2^(s+1)*u) (hr : (3^s*u)%4=3) : ¬ Mixed c n := by
  have p : 0<2^s*u := Nat.mul_pos (by positivity) hu
  have q : 0<3^s*u := Nat.mul_pos (by positivity) hu
  have hn' : n+2=2*(2^s*u) := by rw [hn,pow_succ]; ring
  have a : c.color n = c.color (3^s*u-1) := by
    calc
      _ = c.color (2*(2^s*u-1)) := by congr 1; omega
      _ = c.color (2^s*u-1) := c.evenEq _
      _ = _ := ones c s u hu
  have b : c.color (n+1) = c.color (3*(3^s*u)-1) := by
    calc
      _ = c.color (2^(s+1)*u-1) := by congr 1; omega
      _ = c.color (3^(s+1)*u-1) := ones c (s+1) u hu
      _ = _ := by rw [pow_succ]; simp only [Nat.mul_left_comm, Nat.mul_comm]
  intro h
  apply h
  rw [a,b]
  let v := (3^s*u)/4
  have hv : 3^s*u=4*v+3 := by dsimp [v]; omega
  rw [hv]
  have hleft : 4*v+3-1=4*v+2 := by omega
  have hright : 3*(4*v+3)-1=12*v+8 := by omega
  rw [hleft,hright]
  exact even_pair c v

/-- No persistent wall prefix ends with 10, an even number of ones, then 0.
    For k=0 this is the word 100. -/
theorem forbidden_even_run (c : Coloring) {n : Nat} (h : Mixed c n) (j k t : Nat) :
    index c n j + 2 ≠ 2 * 4^k * (4*t+3) := by
  intro he
  apply run_fusion c (index c n j) (2*k) (4*t+3) (by omega) _ _ (index_mixed c h j)
  · rw [he, pow_succ, pow_mul]; ring
  · rw [pow_mul]
    have hm : (9^k)%4 = 1 := by
      clear he
      induction k with
      | zero => decide
      | succ k ih => rw [pow_succ, Nat.mul_mod, ih]
    change (9^k*(4*t+3))%4=3
    rw [Nat.mul_mod,hm]
    omega

end WallRefinement
