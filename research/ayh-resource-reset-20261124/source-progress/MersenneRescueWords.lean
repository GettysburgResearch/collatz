import MersenneParity

namespace CollatzMersenneRescueWords
open CollatzReverseBasin CollatzMersenneParity

/-- A row acts on y. The indicated sources are A*y−17 and B*y−1. -/
structure Row where
  firstClock : ℕ
  secondClock : ℕ
  A : ℕ
  B : ℕ
  residue : ℕ

def row (i : Fin 11) : Row :=
  match i.val with
  | 0 => ⟨87, 87, 81, 1, 131063258898306574985378419⟩
  | 1 => ⟨43, 42, 2, 27, 5781826967057⟩
  | 2 => ⟨43, 41, 36, 1, 7289720845075⟩
  | 3 => ⟨285, 282, 114791256, 1, 59861120692637604180390742933312097570085441270345039828928682778583143725751066447675⟩
  | 4 => ⟨75, 71, 16, 729, 9885126309049014794163⟩
  | 5 => ⟨37, 32, 32, 3, 88310060929⟩
  | 6 => ⟨33, 27, 64, 729, 3933676667⟩
  | 7 => ⟨40, 33, 128, 19683, 400702687129⟩
  | 8 => ⟨53, 45, 256, 4782969, 8590975546926083⟩
  | 9 => ⟨77, 68, 512, 243, 110202838514788028324337⟩
  | _ => ⟨24, 14, 1024, 729, 4061259⟩

private def walk : ℕ → ℕ → ℕ → Option (ℕ × ℕ)
  | 0, a, b => some (a,b)
  | k+1, a, b => if a%2=0 then
       if b%2=0 then walk k (a/2) (b/2)
       else walk k (3*a/2) ((3*b+1)/2)
    else none

private theorem walk_sound (k a b c d v : ℕ) (h : walk k a b=some (c,d)) :
    atClock k (a*v+b)=c*v+d := by
  induction k generalizing a b with
  | zero =>
    obtain ⟨rfl,rfl⟩ : a=c ∧ b=d := by simpa [walk] using h
    rfl
  | succ k ih =>
    by_cases he : a%2=0
    · obtain ⟨u,rfl⟩ : ∃ u, a=2*u := ⟨a/2,by omega⟩
      by_cases hb : b%2=0
      · simp only [walk,he,hb,ite_true] at h
        rw [atClock,show shortcut (2*u*v+b)=(2*u/2)*v+b/2 by
          unfold shortcut; rw [Nat.mul_assoc]; split <;> simp <;> omega]
        exact ih _ _ h
      · simp only [walk,he,hb,ite_true,ite_false] at h
        rw [atClock,show shortcut (2*u*v+b)=(3*(2*u)/2)*v+(3*b+1)/2 by
          rw [show 2*u*v=2*(u*v) by ring,show 3*(2*u)/2=3*u by omega]
          unfold shortcut; split <;> rw [show 3*u*v=3*(u*v) by ring] <;> omega]
        exact ih _ _ h
    · simp [walk,he] at h

private def ends (s : Row) : Option (ℕ×ℕ) × Option (ℕ×ℕ) :=
  (walk s.firstClock (s.A*2^s.firstClock) (s.A*s.residue-17),
   walk s.secondClock (s.B*2^s.firstClock) (s.B*s.residue-1))

private def valid (s : Row) : Bool :=
  decide (17≤s.A*s.residue ∧ 1≤s.B*s.residue) &&
  match ends s with
  | (some a, some b) => decide (a=b)
  | _ => false

set_option maxRecDepth 8192 in
set_option exponentiation.threshold 512 in
set_option maxHeartbeats 2000000 in
private theorem checked : ∀ i : Fin 11, valid (row i)=true := by decide

/-- All eleven literal post-checkpoint words meet at ordinary clocks on
every positive affine lift of their respective binary residue. -/
theorem ordinary_meet (i : Fin 11) (y : ℕ) (hy : y%2^(row i).firstClock=(row i).residue) :
    atClock (row i).firstClock ((row i).A*y-17)=atClock (row i).secondClock ((row i).B*y-1) := by
  let s:=row i
  change atClock s.firstClock (s.A*y-17)=atClock s.secondClock (s.B*y-1)
  have ok := checked i
  change valid s=true at ok
  obtain ⟨bounds,ev⟩ := Bool.and_eq_true_iff.mp ok
  obtain ⟨lo,hi⟩ : 17≤s.A*s.residue ∧ 1≤s.B*s.residue := of_decide_eq_true bounds
  let v:=y/2^s.firstClock
  have form : y=2^s.firstClock*v+s.residue := by
    rw [← hy]
    exact (Nat.div_add_mod _ _).symm
  have A : s.A*y-17=(s.A*2^s.firstClock)*v+(s.A*s.residue-17) := by
    rw [form,Nat.mul_add,Nat.mul_assoc]; omega
  have B : s.B*y-1=(s.B*2^s.firstClock)*v+(s.B*s.residue-1) := by
    rw [form,Nat.mul_add,Nat.mul_assoc]; omega
  rw [A,B]
  unfold ends at ev
  cases e : walk s.firstClock (s.A*2^s.firstClock) (s.A*s.residue-17) with
  | none => simp [e] at ev
  | some left =>
    cases f : walk s.secondClock (s.B*2^s.firstClock) (s.B*s.residue-1) with
    | none => simp [e,f] at ev
    | some right =>
      have eq : left=right := by simpa [e,f] using ev
      subst right
      exact (walk_sound _ _ _ left.1 left.2 _ e).trans (walk_sound _ _ _ left.1 left.2 _ f).symm

#print axioms ordinary_meet
end CollatzMersenneRescueWords
