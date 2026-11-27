import PostWords

namespace RampShadow.Sixfold

open Postpeak

/-- The sentinel bit above the last chronological letter keeps terminal
    even letters. The least significant bit is the first departure. -/
def decode (code : ℕ) : Word :=
  if code ≤ 1 then [] else (code % 2 == 1) :: decode (code / 2)
termination_by code
decreasing_by omega

structure Row where
  upperCode : ℕ
  lowerCode : ℕ
  peakClock : ℕ
  inverse : ℤ
deriving DecidableEq

def Row.upper (r : Row) : Word := decode r.upperCode
def Row.lower (r : Row) : Word := decode r.lowerCode
def Row.prefix (r : Row) : Word := r.upper.take r.peakClock

structure Affine where
  den : ℤ
  gain : ℤ
  bias : ℤ

def form (w : Word) : Affine := ⟨2^w.length, 3^weight w, intercept w⟩

def Affine.atPoint (a : Affine) (x y : ℤ) : Prop :=
  a.den * y = a.gain * x + a.bias

instance (a : Affine) (x y : ℤ) : Decidable (a.atPoint x y) :=
  inferInstanceAs (Decidable (_ = _))

structure Family where
  x : ℤ
  m : ℤ
  y : ℤ
  peak : ℤ
  mstep : ℤ
  pstep : ℤ
  u : ℤ
  v : ℤ

/-- Arithmetic at the least positive native source and at the next
    source in its dyadic cylinder determines both affine paths. -/
def family (a b p : Affine) (inverse : ℤ) : Family :=
  let residue := (-inverse * a.bias) % a.den
  let x := if residue = 0 then a.den else residue
  let y := (a.gain * x + a.bias) / a.den
  ⟨x, (b.den*y-b.bias)/b.gain, y, (p.gain*x+p.bias)/p.den,
    b.den*a.gain/b.gain, p.gain*a.den/p.den,
    inverse, (1-inverse*a.gain)/a.den⟩

def Family.Valid (c : Family) (a b p : Affine) : Prop :=
  0 < a.den ∧ c.x ≤ a.den ∧ 0 < c.m ∧ 0 ≤ c.mstep ∧
  a.atPoint c.x c.y ∧ b.atPoint c.m c.y ∧ p.atPoint c.x c.peak ∧
  b.den * a.gain = b.gain * c.mstep ∧ p.den * c.pstep = p.gain * a.den ∧
  c.u * a.gain + c.v * a.den = 1 ∧ 6*c.m < c.peak ∧ 6*c.mstep ≤ c.pstep

instance (c : Family) (a b p : Affine) : Decidable (c.Valid a b p) := by
  unfold Family.Valid
  infer_instance

def Row.Valid (r : Row) : Prop :=
  let a := form r.upper
  let b := form r.lower
  let p := form r.prefix
  (family a b p r.inverse).Valid a b p

instance (r : Row) : Decidable r.Valid := by
  unfold Row.Valid
  infer_instance

private theorem family_sound {a b p : Affine} {c : Family} (V : c.Valid a b p)
    {x y : ℤ} (positive : 0<x) (native : a.atPoint x y) :
    ∃ m peak : ℤ, 0<m ∧ 6*m<peak ∧ b.atPoint m y ∧ p.atPoint x peak := by
  obtain ⟨den, least, mp, ms, a0, b0, p0, bstep, pstep, bezout, low, slope⟩ := V
  unfold Affine.atPoint at native a0 b0 p0 ⊢
  let r := c.u*(y-c.y)+c.v*(x-c.x)
  have diff : a.den*(y-c.y)=a.gain*(x-c.x) := by linarith only [native,a0]
  have source : a.den*r=x-c.x := by
    dsimp only [r]
    linear_combination c.u*diff + (x-c.x)*bezout
  have dest0 : a.den*(y-(c.y+a.gain*r))=0 := by
    linear_combination diff - a.gain*source
  have dest : y=c.y+a.gain*r := by
    have := (mul_eq_zero.mp dest0).resolve_left (ne_of_gt den)
    linarith
  have rn : 0≤r := by
    by_contra! h
    have hr : r≤ -1 := by omega
    have le := mul_le_mul_of_nonneg_left hr den.le
    nlinarith only [positive,least,source,le]
  refine ⟨c.m+c.mstep*r,c.peak+c.pstep*r,?_,?_,?_,?_⟩
  · exact add_pos_of_pos_of_nonneg mp (mul_nonneg ms rn)
  · have le := mul_le_mul_of_nonneg_right slope rn
    linarith only [low,le]
  · linear_combination b0 + r*bstep + b.den*dest
  · linear_combination p0 + r*pstep + p.gain*source

/-- A successfully checked bank row gives a positive ordinary visitor
    below the original threshold at every positive native lift. -/
theorem Row.sound (r : Row) (valid : r.Valid) {X x y : ℤ} (positive : 0<x)
    (native : (form r.upper).atPoint x y) (height : run r.prefix.length x ≤ 6*X) :
    ∃ m : ℤ, 0<m ∧ m<X ∧ Walk r.lower.length (weight r.lower) m y ∧
      Walk r.upper.length (weight r.upper) x y := by
  obtain ⟨m,peak,mp,small,meeting,comparison⟩ := family_sound valid positive native
  have usePeak := (readout (walk_of_word r.prefix x peak comparison)).1
  exact ⟨m,mp,by omega,walk_of_word r.lower m y meeting,walk_of_word r.upper x y native⟩

end RampShadow.Sixfold

#print axioms RampShadow.Sixfold.Row.sound
