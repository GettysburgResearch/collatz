import WallRefinement
import WordRank

namespace WallRefinement
open CollatzReverseBasin

def dz (c : Coloring) (n : Nat) : Int :=
  (c.color (n+1)).toNat - (c.color n).toNat

theorem split_difference (c : Coloring) (n : Nat) :
    dz c n = dz c (2*n) + dz c (2*n+1) := by
  have ee : c.color (2*n+1+1) = c.color (n+1) := by
    simpa [Nat.mul_add] using c.evenEq (n+1)
  simp only [dz, ee, c.evenEq]
  omega

theorem propagated (c : Coloring) (n : Nat) : c.color (shortcut n) = c.color n := by
  by_cases hp : n%2=0
  · have eq : n=2*(n/2) := by omega
    calc
      _ = c.color (n/2) := by simp [shortcut,hp]
      _ = c.color (2*(n/2)) := (c.evenEq _).symm
      _ = _ := congrArg c.color eq.symm
  · have eq : n=2*(n/2)+1 := by omega
    calc
      _ = c.color (3*(n/2)+2) := by simp [shortcut,hp]; congr 1; omega
      _ = c.color (2*(n/2)+1) := (c.oddEq _).symm
      _ = _ := congrArg c.color eq.symm

theorem propagated_run (c : Coloring) (j n : Nat) : c.color (WordRank.run j n) = c.color n := by
  induction j generalizing n with
  | zero => rfl
  | succ j ih => exact (ih _).trans (propagated c n)

def fused (h r : Nat) : Bool :=
  decide (WordRank.run h r = WordRank.run h (r+1) ∧
    WordRank.odds h r = WordRank.odds h (r+1))

/-- Counted fusion at the residual index proves oriented cancellation on
every positive lift, and also on the zero lift. -/
theorem fused_zero (c : Coloring) (h r n : Nat) (ok : fused h r = true) :
    dz c (2^h*n+r)=0 := by
  obtain ⟨v,q⟩ := of_decide_eq_true ok
  have same : WordRank.run h (2^h*n+r) = WordRank.run h (2^h*n+r+1) := by
    rw [Nat.add_assoc, (WordRank.liftPrefix h n r).1,
        (WordRank.liftPrefix h n (r+1)).1, v, q]
  have ceq := ((propagated_run c h _).symm.trans (congrArg c.color same)).trans
    (propagated_run c h _)
  simp [dz,ceq]

/-- Send a signed edge down a binary block, dropping each prefix as soon
as its two endpoints provably merge on the entire cylinder. -/
def sparseSum (c : Coloring) (n : Nat) : Nat → Nat → Nat → Int
  | 0, h, r => if fused h r then 0 else dz c (2^h*n+r)
  | k+1, h, r => if fused h r then 0 else
      sparseSum c n k (h+1) (2*r) + sparseSum c n k (h+1) (2*r+1)

theorem exact_sparseSum (c : Coloring) (n k h r : Nat) :
    sparseSum c n k h r = dz c (2^h*n+r) := by
  induction k generalizing h r with
  | zero =>
    by_cases f : fused h r
    · simp [sparseSum,f,fused_zero c h r n f]
    · simp [sparseSum,f]
  | succ k ih =>
    by_cases f : fused h r
    · simp [sparseSum,f,fused_zero c h r n f]
    · simp only [sparseSum,f,Bool.false_eq_true,ite_false,ih]
      convert (split_difference c (2^h*n+r)).symm using 1
      congr 2 <;> ring

theorem source_difference (c : Coloring) (n k : Nat) : sparseSum c n k 0 0 = dz c n := by
  simpa using exact_sparseSum c n k 0 0

theorem twelve_bit_cut (c : Coloring) (n : Nat) : dz c (4096*n+2990)=0 := by
  exact fused_zero c 12 2990 n (by decide)

/-- This second cut is useful in a finite automaton with entropy below one half. -/
theorem thirteen_bit_cut (c : Coloring) (n : Nat) : dz c (8192*n+4014)=0 := by
  exact fused_zero c 13 4014 n (by decide)

private theorem basin_step (n : Nat) : Basin (shortcut n) ↔ Basin n := by
  constructor
  · rintro ⟨k,h⟩
    exact ⟨k+1,h⟩
  · rintro ⟨k,h⟩
    cases k with
    | zero => change n=1 at h; subst n; exact ⟨1,rfl⟩
    | succ k => exact ⟨k,h⟩

noncomputable def bad (n : Nat) : Bool := by
  classical exact decide (0<n ∧ ¬ Basin n)

noncomputable def actual : Coloring where
  color := bad
  evenEq n := by
    classical
    have e : Basin (2*n) ↔ Basin n := by simpa [shortcut] using (basin_step (2*n)).symm
    simp [bad,e]
  oddEq n := by
    classical
    have sc : shortcut (2*n+1)=3*n+2 := by simp [shortcut]; omega
    have e : Basin (2*n+1) ↔ Basin (3*n+2) := by simpa [sc] using (basin_step (2*n+1)).symm
    simp [bad,e]

private theorem mixed_before (c : Coloring) {x : Nat} (pos : 0<x)
    (h : c.color 1 ≠ c.color x) : ∃ n, 0<n ∧ n<x ∧ Mixed c n := by
  induction x with
  | zero => omega
  | succ x ih =>
    by_cases x0 : x=0
    · subst x
      exact False.elim (h rfl)
    · by_cases l : c.color 1 = c.color x
      · exact ⟨x,by omega,by omega,fun e => h (l.trans e)⟩
      · obtain ⟨n,p,t,e⟩ := ih (by omega) l
        exact ⟨n,p,by omega,e⟩

/-- A single specified positive failure forces one and the same ordinary
edge throughout the infinite exact sparse-sum tests. -/
theorem fixed_source {x : Nat} (pos : 0<x) (hx : ¬ Basin x) :
    ∃ n, 0<n ∧ n<x ∧ Mixed actual n ∧
      ∀ j, Mixed actual (index actual n j) ∧ sparseSum actual n j 0 0 = dz actual n := by
  classical
  have h1 : Basin 1 := ⟨0,rfl⟩
  have hd : actual.color 1 ≠ actual.color x := by simp [actual,bad,h1,pos,hx]
  obtain ⟨n,p,t,e⟩ := mixed_before actual pos hd
  exact ⟨n,p,t,e,fun j => ⟨index_mixed actual e j,source_difference actual n j⟩⟩

end WallRefinement
