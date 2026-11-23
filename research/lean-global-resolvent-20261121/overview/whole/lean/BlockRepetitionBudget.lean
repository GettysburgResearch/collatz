module

public import Mathlib.Data.Int.Basic
public import Mathlib.RingTheory.Coprime.Lemmas
public import Mathlib.Tactic.NormNum
public import Mathlib.Tactic.Linarith
public import Mathlib.Tactic.Ring
public import Mathlib.Algebra.BigOperators.Group.List.Basic

@[expose] public section

/-!
# Ordinary repeated-block budgets

The arithmetic identity behind periodic-block legality is classical.  This
module verifies it for every supplied binary block, every repetition count,
and every finite concatenation, without a bounded-word census.

`WordPath` records exact integer branch equations.  Every actual shortcut
Collatz path with the supplied parity word satisfies these equations.
`PiecePath` additionally requires each repeated block not to fix its incoming
state.  This condition is essential: an actual cycle block may repeat forever.

The final theorem gives the full-clock inequality
`2^A <= (K*(x+1))^(2^r-1)` for r such nonfixed pieces.  It does not supply an
upper bound on r for an arbitrary orbit, or a transcendence theorem.
-/

namespace CollatzBlockBudget

def defect (a b c x : Int) : Int := (b-a)*x-c

def AffinePath (a b c : Int) : Nat → Int → Int → Prop
  | 0, x, y => x=y
  | k+1, x, y => ∃z, b*z=a*x+c ∧ AffinePath a b c k z y

theorem edge_defect (a b c x y : Int) (h : b*y=a*x+c) :
    b*defect a b c y=a*defect a b c x := by
  dsimp [defect]
  calc
    b*((b-a)*y-c)=(b-a)*(b*y)-b*c := by ring
    _ =(b-a)*(a*x+c)-b*c := by rw [h]
    _ =a*((b-a)*x-c) := by ring

theorem affine_path_defect (a b c : Int) (k : Nat) (x y : Int)
    (h : AffinePath a b c k x y) :
    b^k*defect a b c y=a^k*defect a b c x := by
  induction k generalizing x y with
  | zero => simpa [AffinePath] using congrArg (defect a b c) h.symm
  | succ k ih =>
      obtain ⟨z,first,rest⟩ := h
      have tail := ih z y rest
      have edge := edge_defect a b c x z first
      calc
        b^(k+1)*defect a b c y=b*(b^k*defect a b c y) := by ring
        _ =b*(a^k*defect a b c z) := by rw [tail]
        _ =a^k*(b*defect a b c z) := by ring
        _ =a^k*(a*defect a b c x) := by rw [edge]
        _ =a^(k+1)*defect a b c x := by ring

theorem affine_path_reserve (a b c : Int) (k : Nat) (x y : Int)
    (cop : IsCoprime b a) (h : AffinePath a b c k x y) :
    b^k ∣ defect a b c x := by
  have eqn := affine_path_defect a b c k x y h
  have product : b^k ∣ a^k*defect a b c x := by
    rw [← eqn]
    exact dvd_mul_right _ _
  exact (cop.pow).dvd_of_dvd_mul_left product

def ones : List Bool → Nat
  | [] => 0
  | b::w => (if b then 1 else 0)+ones w

def correction : List Bool → Nat
  | [] => 0
  | b::w => (if b then 3^(ones w) else 0)+2*correction w

def WordPath : List Bool → Nat → Nat → Prop
  | [], x, y => x=y
  | b::w, x, y => ∃z, 2*z=(if b then 3*x+1 else x) ∧ WordPath w z y

def RepeatPath (w : List Bool) : Nat → Nat → Nat → Prop
  | 0, x, y => x=y
  | k+1, x, y => ∃z, WordPath w x z ∧ RepeatPath w k z y

theorem word_affine (w : List Bool) (x y : Nat) (h : WordPath w x y) :
    2^w.length*y=3^(ones w)*x+correction w := by
  induction w generalizing x y with
  | nil => simpa [WordPath,ones,correction] using h.symm
  | cons b w ih =>
      obtain ⟨z,first,rest⟩ := h
      have tail := ih z y rest
      calc
        2^(b::w).length*y=2*(2^w.length*y) := by simp [pow_succ]; ring
        _ =2*(3^(ones w)*z+correction w) := by rw [tail]
        _ =3^(ones w)*(2*z)+2*correction w := by ring
        _ =3^(ones w)*(if b then 3*x+1 else x)+2*correction w := by rw [first]
        _ =3^(ones (b::w))*x+correction (b::w) := by
          cases b <;> simp [ones,correction,pow_add]
          ring

theorem word_growth (w : List Bool) (x y : Nat) (h : WordPath w x y) :
    y+1≤2^w.length*(x+1) := by
  induction w generalizing x y with
  | nil =>
      change x=y at h
      subst y
      simp
  | cons b w ih =>
      obtain ⟨z,first,rest⟩ := h
      have tail := ih z y rest
      have edge : z+1≤2*(x+1) := by
        cases b <;> simp at first <;> omega
      calc
        y+1≤2^w.length*(z+1) := tail
        _ ≤2^w.length*(2*(x+1)) := Nat.mul_le_mul_left _ edge
        _ =2^(b::w).length*(x+1) := by simp [pow_succ]; ring

theorem repeat_affine_path (w : List Bool) (k x y : Nat)
    (h : RepeatPath w k x y) :
    AffinePath (3^(ones w)) (2^w.length) (correction w) k x y := by
  induction k generalizing x y with
  | zero =>
      change x=y at h
      change (x:Int)=(y:Int)
      exact_mod_cast h
  | succ k ih =>
      obtain ⟨z,first,rest⟩ := h
      refine ⟨z,?_,ih z y rest⟩
      exact_mod_cast word_affine w x z first

theorem repeat_growth (w : List Bool) (k x y : Nat)
    (h : RepeatPath w k x y) : y+1≤2^(w.length*k)*(x+1) := by
  induction k generalizing x y with
  | zero =>
      change x=y at h
      subst y
      simp
  | succ k ih =>
      obtain ⟨z,first,rest⟩ := h
      have edge := word_growth w x z first
      calc
        y+1≤2^(w.length*k)*(z+1) := ih z y rest
        _ ≤2^(w.length*k)*(2^w.length*(x+1)) := Nat.mul_le_mul_left _ edge
        _ =2^(w.length*(k+1))*(x+1) := by rw [Nat.mul_succ w.length k,pow_add]; ring

def wordDefect (w : List Bool) (x : Nat) : Int :=
  defect (3^(ones w)) (2^w.length) (correction w) x

def wordCost (w : List Bool) : Nat :=
  ((2:Int)^w.length-3^(ones w)).natAbs+correction w

theorem repeated_word_reserve (w : List Bool) (k x y : Nat)
    (h : RepeatPath w k x y) :
    (2:Int)^(w.length*k) ∣ wordDefect w x := by
  have cop23 : IsCoprime (2:Int) 3 := ⟨-1,1,by norm_num⟩
  have cop : IsCoprime ((2:Int)^w.length) (3^(ones w)) := cop23.pow
  have result := affine_path_reserve _ _ _ k x y cop (repeat_affine_path w k x y h)
  simpa only [← pow_mul,wordDefect] using result

theorem repeated_word_height (w : List Bool) (k x y : Nat)
    (h : RepeatPath w k x y) (nonfixed : wordDefect w x≠0) :
    2^(w.length*k)≤(wordDefect w x).natAbs := by
  have result := Int.natAbs_le_of_dvd_ne_zero (repeated_word_reserve w k x y h) nonfixed
  simpa using result

theorem word_defect_bound (w : List Bool) (x : Nat) :
    (wordDefect w x).natAbs≤wordCost w*(x+1) := by
  have tri := Int.natAbs_sub_le (((2:Int)^w.length-3^(ones w))*x) (correction w)
  simp only [Int.natAbs_mul,Int.natAbs_natCast] at tri
  calc
    (wordDefect w x).natAbs≤((2:Int)^w.length-3^(ones w)).natAbs*x+correction w := by
      simpa only [wordDefect,defect] using tri
    _ ≤((2:Int)^w.length-3^(ones w)).natAbs*(x+1)+correction w*(x+1) := by
      apply Nat.add_le_add
      · exact Nat.mul_le_mul_left _ (Nat.le_succ x)
      · simpa using Nat.mul_le_mul_left (correction w) (by omega : 1≤x+1)
    _ =wordCost w*(x+1) := by dsimp [wordCost]; ring

theorem nonfixed_piece_budget (w : List Bool) (k x y K : Nat)
    (h : RepeatPath w k x y) (nonfixed : wordDefect w x≠0)
    (cost : wordCost w≤K) :
    2^(w.length*k)≤K*(x+1) ∧ K*(y+1)≤(K*(x+1))^2 := by
  have reserve := repeated_word_height w k x y h nonfixed
  have bound := word_defect_bound w x
  have first : 2^(w.length*k)≤K*(x+1) :=
    reserve.trans (bound.trans (Nat.mul_le_mul_right (x+1) cost))
  have grow := repeat_growth w k x y h
  have second := Nat.mul_le_mul_right (x+1) first
  have out : y+1≤K*(x+1)^2 := by nlinarith
  constructor
  · exact first
  · calc
      K*(y+1)≤K*(K*(x+1)^2) := Nat.mul_le_mul_left K out
      _ =(K*(x+1))^2 := by ring

def clock : List (List Bool × Nat) → Nat
  | [] => 0
  | (w,k)::ps => w.length*k+clock ps

def PiecePath (K : Nat) : List (List Bool × Nat) → Nat → Nat → Prop
  | [], x, y => x=y
  | (w,k)::ps, x, y => ∃z, RepeatPath w k x z ∧ wordDefect w x≠0 ∧
      wordCost w≤K ∧ PiecePath K ps z y

theorem full_clock_budget (K : Nat) (ps : List (List Bool × Nat))
    (x y : Nat) (h : PiecePath K ps x y) :
    2^(clock ps)≤(K*(x+1))^(2^ps.length-1) := by
  induction ps generalizing x y with
  | nil => simp [clock]
  | cons p ps ih =>
      rcases p with ⟨w,k⟩
      obtain ⟨z,first,nonfixed,cost,rest⟩ := h
      obtain ⟨reserve,grow⟩ := nonfixed_piece_budget w k x z K first nonfixed cost
      have tail := ih z y rest
      have ep : 0<2^ps.length := by positivity
      have exponent : 1+2*(2^ps.length-1)=2^((w,k)::ps).length-1 := by
        simp only [List.length_cons,pow_succ]
        omega
      calc
        2^(clock ((w,k)::ps))=2^(w.length*k)*2^(clock ps) := by rw [clock,pow_add]
        _ ≤(K*(x+1))*(K*(z+1))^(2^ps.length-1) := Nat.mul_le_mul reserve tail
        _ ≤(K*(x+1))*((K*(x+1))^2)^(2^ps.length-1) :=
          Nat.mul_le_mul_left _ (Nat.pow_le_pow_left grow _)
        _ =(K*(x+1))^(1+2*(2^ps.length-1)) := by rw [pow_add,pow_one,pow_mul]
        _ =(K*(x+1))^(2^((w,k)::ps).length-1) := by rw [exponent]

#print axioms edge_defect
#print axioms affine_path_defect
#print axioms affine_path_reserve
#print axioms word_affine
#print axioms word_growth
#print axioms repeat_affine_path
#print axioms repeat_growth
#print axioms repeated_word_reserve
#print axioms repeated_word_height
#print axioms word_defect_bound
#print axioms nonfixed_piece_budget
#print axioms full_clock_budget

end CollatzBlockBudget
