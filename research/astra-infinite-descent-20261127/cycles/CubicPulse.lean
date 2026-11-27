import Mathlib.Tactic.Ring

/-! The local four-label sign pulse on ten mechanical edges. -/

namespace Collatz.InfiniteDescent.CubicPulse

structure Quad where
  a : ℤ
  b : ℤ
  c : ℤ
  d : ℤ
deriving DecidableEq, Repr

def third (x : Quad) : ℤ := -x.a + 3*x.b - 3*x.c + x.d

def allOne : Quad := ⟨1,1,1,1⟩

/-- The odd part at each vertex takes a genuine binary native step. -/
def binaryStep (q oldMark newMark : ℤ) : Bool :=
  ((oldMark == 1) || (oldMark == 2)) &&
  ((newMark == 1) || (newMark == 2)) &&
  ((q*newMark == 2*oldMark) || (q*newMark == 4*oldMark))

def compatible (q : ℤ) (m n : Quad) : Bool :=
  binaryStep q m.a n.a && binaryStep q m.b n.b &&
  binaryStep q m.c n.c && binaryStep q m.d n.d

def times : List (ℤ × Quad × ℤ) :=
  [(2, allOne, 0), (4, ⟨1,2,1,2⟩, 0), (2, ⟨1,1,1,2⟩, 1),
   (4, ⟨1,1,2,2⟩, 2), (4, ⟨1,1,2,1⟩, 1), (2, allOne, 0),
   (4, ⟨2,1,2,1⟩, 0), (2, ⟨2,1,1,1⟩, -1), (4, ⟨2,2,1,1⟩, -2),
   (4, ⟨1,2,1,1⟩, -1)]

def check : List (ℤ × Quad × ℤ) → Bool
  | [] => true
  | (q,m,j) :: tail =>
    let next := tail.headD (0,allOne,0)
    ((q == 2) || (q == 4)) && compatible q m next.2.1 &&
      (q*next.2.2 == 3*j + third m) && check tail

theorem ten_edges : check times = true := by decide

theorem position (q : ℤ) (x y m : Quad)
    (ha : q*y.a = 3*x.a+m.a) (hb : q*y.b = 3*x.b+m.b)
    (hc : q*y.c = 3*x.c+m.c) (hd : q*y.d = 3*x.d+m.d) :
    q * third y = 3 * third x + third m := by
  unfold third
  calc
    _ = -(q*y.a)+3*(q*y.b)-3*(q*y.c)+q*y.d := by ring
    _ = _ := by rw [ha,hb,hc,hd]; ring

theorem quadratic_completion (a b c : ℤ) : third ⟨a,b,c,a-3*b+3*c⟩ = 0 := by
  unfold third
  ring

/-- Compatibility of the fourth terminal residue, with no loss of a prime power. -/
theorem backwards_fourth {t k a b c x y z ca cb cc cd : ℤ}
    (ha : t*x = k*a+ca) (hb : t*y = k*b+cb) (hc : t*z = k*c+cc)
    (hcarry : cd = ca-3*cb+3*cc) :
    t*(x-3*y+3*z) = k*(a-3*b+3*c)+cd := by
  calc
    _ = t*x-3*(t*y)+3*(t*z) := by ring
    _ = _ := by rw [ha,hb,hc,hcarry]; ring

#print axioms ten_edges
#print axioms position
#print axioms quadratic_completion
#print axioms backwards_fourth

end Collatz.InfiniteDescent.CubicPulse
