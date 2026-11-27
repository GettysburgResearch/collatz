import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.EuclideanDomain.Int
import Mathlib.Data.Int.Interval
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-!
Two consecutive actual good coordinates on a restricted odd cycle, and the
finite algebra of their completed first-hit grades. The analytic residue
bound is an explicit hypothesis in applications.
-/

namespace CollatzGradeMesh

def shortcut (n : ℕ) : ℕ :=
  if n % 2 = 0 then n/2 else (3*n+1)/2

/-- The inverse direction of the original 1932 permutation. -/
def original (n : ℕ) : ℕ :=
  if n % 2 = 0 then 3*(n/2)
  else if n % 4 = 1 then (3*n+1)/4 else (3*n-1)/4

theorem one_edge (u : ℕ) (hu : 0 < u) :
    original (2*u) = 3*u ∧ shortcut (2*u) = u ∧
      shortcut (2*u-1) = 3*u-1 := by
  simp only [original,shortcut]
  split_ifs <;> omega

theorem two_edge (v : ℕ) :
    original (4*v+1) = 3*v+1 ∧
      shortcut (4*v+1) = 6*v+2 ∧ shortcut (6*v+2) = 3*v+1 ∧
      shortcut (4*v) = 2*v ∧ shortcut (2*v) = v := by
  simp only [original,shortcut]
  split_ifs <;> omega

/-- Sum the local accounting over a finite closed permutation. The function
may count first-hit clocks, odds, or visits to one specified vertex. -/
theorem circulation {ι : Type*} [Fintype ι] (next : ι ≃ ι)
    (potential jumps paid : ι → ℤ)
    (edge : ∀ i, jumps i = paid i + potential (next i) - potential i) :
    ∑ i, jumps i = ∑ i, paid i := by
  simp_rw [edge]
  rw [Finset.sum_sub_distrib, Finset.sum_add_distrib, next.sum_comp]
  exact add_sub_cancel_right _ _

def charge (p h H A K i : ℤ) : ℤ := p*(H+A)-h*(K+i)

/-- Equality in the primitive integer grading is an exact simultaneous
multiple of the period in the two completed counts. -/
theorem grade_link {p h a b : ℤ} (coprime : Int.gcd p h = 1)
    (equal_grade : p*a = h*b) : ∃ m : ℤ, a = m*h ∧ b = m*p := by
  have bez : p*(Int.gcdA p h)+h*(Int.gcdB p h) = 1 := by
    rw [← Int.gcd_eq_gcd_ab, coprime]
    rfl
  refine ⟨Int.gcdA p h*b + Int.gcdB p h*a, ?_, ?_⟩
  · calc
      a = a*(p*(Int.gcdA p h)+h*(Int.gcdB p h)) := by rw [bez,mul_one]
      _ = Int.gcdA p h*(p*a) + Int.gcdB p h*a*h := by ring
      _ = (Int.gcdA p h*b + Int.gcdB p h*a)*h := by rw [equal_grade]; ring
  · calc
      b = b*(p*(Int.gcdA p h)+h*(Int.gcdB p h)) := by rw [bez,mul_one]
      _ = Int.gcdA p h*b*p + Int.gcdB p h*(h*b) := by ring
      _ = (Int.gcdA p h*b + Int.gcdB p h*a)*p := by rw [← equal_grade]; ring

/-- Exact logarithmic-coordinate identity. The caller supplies the two
actual path product identities after taking base-two logarithms. -/
theorem mesh_identity {R : Type*} [CommRing R] {p h H A K i alpha residue deviation drift logscale correction : R}
    (period : drift = h-p*alpha)
    (paths : H+A-(K+i)*alpha = logscale+correction+residue+deviation) :
    p*(H+A)-h*(K+i) =
      p*(logscale+correction+residue+deviation)-(K+i)*drift := by
  rw [period, ← paths]
  ring

/-- A common interval for all the completed integer grades in the
supplied finite grade budget. -/
theorem mesh_interval {R : Type*} [CommRing R] [LinearOrder R] [IsStrictOrderedRing R]
    {p K i budget drift residue deviation correction radius logscale beta grade : R}
    (p0 : 0 ≤ p) (K0 : 0 ≤ K) (Kcap : K ≤ budget)
    (i0 : 0 ≤ i) (icap : i ≤ p) (d0 : 0 ≤ drift)
    (r0 : 0 ≤ residue) (rcap : residue ≤ beta)
    (v0 : 0 ≤ deviation) (vcap : deviation ≤ drift)
    (c0 : -radius ≤ correction) (ccap : correction ≤ radius)
    (identity : grade = p*(logscale+correction+residue+deviation)-(K+i)*drift) :
    p*(logscale-radius)-(budget+p)*drift ≤ grade ∧
      grade ≤ p*(logscale+radius+beta+drift) := by
  rw [identity]
  constructor
  · exact sub_le_sub (mul_le_mul_of_nonneg_left (by linarith) p0)
        (mul_le_mul_of_nonneg_right (by linarith) d0)
  · have leftBound : p*(logscale+correction+residue+deviation) ≤
          p*(logscale+radius+beta+drift) :=
        mul_le_mul_of_nonneg_left (by linarith) p0
    exact le_trans (sub_le_self _ (mul_nonneg (by linarith) d0)) leftBound

theorem integer_capacity {ι : Type*} (sample : Finset ι)
    (grade : ι → ℤ) (a b : ℤ)
    (bounds : ∀ i ∈ sample, a ≤ grade i ∧ grade i ≤ b) :
    (sample.image grade).card ≤ (b+1-a).toNat := by
  rw [← Int.card_Icc]
  apply Finset.card_le_card
  intro y hy
  obtain ⟨i, hi, rfl⟩ := Finset.mem_image.mp hy
  exact Finset.mem_Icc.mpr (bounds i hi)

private def firstHit : ℕ → ℕ → Option (ℕ × ℕ)
  | 0, n => if n = 1 then some (0,0) else none
  | fuel+1, n => if n = 1 then some (0,0) else do
      let (t,k) ← firstHit fuel (shortcut n)
      return (t+1,k+n%2)

private def equalPairs : ℕ → ℕ → ℕ → ℕ → List ℕ
  | 0, _, _, _ => []
  | fuel+1, x, clock, i =>
    let a := if x%4 = 3 then 1 else if x%8 = 1 then 2 else 0
    if a = 0 then [] else
      let y := if a = 1 then (x+1)/2 else (x-1)/2
      let later := equalPairs fuel ((3*x+1)/(2^a)) (clock+a) (i+1)
      match firstHit 150 y with
      | some (t,k) => if clock+t = 136 ∧ i+k = 77 then i::later else later
      | none => later

set_option maxRecDepth 12000 in
set_option maxHeartbeats 2000000 in
theorem fourteen_ordinary_marks :
    equalPairs 25 27367 0 0 = [8,9,10,11,12,14,15,16,18,19,20,22,23,24] := by
  decide

#print axioms fourteen_ordinary_marks
#print axioms one_edge
#print axioms two_edge
#print axioms circulation
#print axioms grade_link
#print axioms mesh_identity
#print axioms mesh_interval
#print axioms integer_capacity
end CollatzGradeMesh
